#!/usr/bin/env python3
"""Merge per-page textbook extracts and audit concept coverage against the ontology."""

from __future__ import annotations

import argparse
import glob
import json
import re
from collections import defaultdict
from pathlib import Path


UNITS = {
    "통합사회1": [
        (11, 30, "통합적 관점"),
        (31, 54, "인간, 사회, 환경과 행복"),
        (55, 88, "자연환경과 인간"),
        (89, 128, "문화와 다양성"),
        (129, 157, "생활공간과 사회"),
    ],
    "통합사회2": [
        (11, 38, "인권 보장과 헌법"),
        (39, 68, "사회정의와 불평등"),
        (69, 106, "시장경제와 지속가능발전"),
        (107, 132, "세계화와 평화"),
        (133, 157, "미래와 지속가능한 삶"),
    ],
}

VISUALLY_REVIEWED = {
    "통합사회1": {1, 7, 9, 11, 31, 55, 61, 87, 89, 126, 127, 129, 156, 157},
    "통합사회2": {1, 9, 11, 36, 39, 69, 107, 133},
}


def normalize(value: str) -> str:
    value = value.replace("\xad", "").replace("·", "").replace("ㆍ", "")
    return re.sub(r"\s+", "", value).lower()


def course_for(source_file: str) -> str:
    return "통합사회1" if "통합사회1" in source_file else "통합사회2"


def concept_matches_text(concept: dict, text: str) -> bool:
    return any(alias in text for alias in concept["aliases"])


def index_mappings(term: str, concepts: list[dict]) -> list[str]:
    normalized_term = normalize(term)
    matches = []
    for concept in concepts:
        candidates = [concept["name"], *concept["aliases"]]
        for candidate in candidates:
            normalized_candidate = normalize(candidate)
            if normalized_term == normalized_candidate:
                matches.append(concept["id"])
                break
    return matches


def render_page_text(course: str, pages: list[dict]) -> str:
    lines = [
        f"# {course} 교과서 페이지별 전수 추출",
        "",
        f"- 전체 페이지: {len(pages)}쪽",
        f"- 추출 문자: {sum(page['char_count'] for page in pages):,}자",
        "- 페이지마다 원문 텍스트, 이미지 수, 시각 검수 여부를 보존한다.",
        "",
    ]
    for page in pages:
        visual = page["pdf_page"] in VISUALLY_REVIEWED[course]
        lines.extend(
            [
                f"## PDF {page['pdf_page']}쪽",
                "",
                f"- 문자 수: {page['char_count']}",
                f"- 이미지 수: {page['image_count']}",
                f"- 시각 검수: {'완료' if visual else '텍스트층 확인'}",
                f"- 표제 후보: {', '.join(page['headings']) if page['headings'] else '없음'}",
                "",
                page["text"] or "(표지 또는 텍스트 없는 이미지 페이지)",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("page_glob")
    parser.add_argument("concepts", type=Path)
    parser.add_argument("index", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    pages = []
    for filename in sorted(glob.glob(args.page_glob)):
        pages.extend(json.loads(Path(filename).read_text(encoding="utf-8")))
    pages.sort(key=lambda page: (course_for(page["source_file"]), page["pdf_page"]))
    concepts = json.loads(args.concepts.read_text(encoding="utf-8"))
    index_entries = json.loads(args.index.read_text(encoding="utf-8"))
    first_added = next(i for i, concept in enumerate(concepts) if concept["id"] == "integrated_inquiry_attitudes")
    added_ids = {concept["id"] for concept in concepts[first_added:]}
    names = {concept["id"]: concept["name"] for concept in concepts}

    by_course: dict[str, list[dict]] = defaultdict(list)
    for page in pages:
        by_course[course_for(page["source_file"])].append(page)
    for course, course_pages in by_course.items():
        expected = list(range(1, 169))
        actual = [page["pdf_page"] for page in course_pages]
        if actual != expected:
            raise SystemExit(f"{course}: page sequence is incomplete or duplicated")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for course, course_pages in by_course.items():
        (args.output_dir / f"{course}_교과서_페이지별.md").write_text(
            render_page_text(course, course_pages), encoding="utf-8"
        )

    mapped_index = []
    unmapped_index = []
    for entry in index_entries:
        mappings = index_mappings(entry["term"], concepts)
        enriched = {**entry, "concept_ids": mappings}
        (mapped_index if mappings else unmapped_index).append(enriched)

    # The textbook's own index is the primary concept-to-page authority. Body-text
    # matching is used only when an ontology concept has no index connection at all.
    concept_pages: dict[tuple[str, str], list[int]] = defaultdict(list)
    for entry in mapped_index:
        for concept_id in entry["concept_ids"]:
            concept_pages[(entry["course"], concept_id)].extend(entry["textbook_pages"])
    for key in list(concept_pages):
        concept_pages[key] = sorted(set(concept_pages[key]))
    for course, course_pages in by_course.items():
        for concept in concepts:
            key = (course, concept["id"])
            if concept_pages.get(key):
                continue
            if any(concept_pages.get((other_course, concept["id"])) for other_course in by_course):
                continue
            fallback_terms = [concept["name"], *[alias for alias in concept["aliases"] if len(alias) >= 8]]
            fallback = [
                page["pdf_page"]
                for page in course_pages
                if any(term in page["text"] for term in fallback_terms)
            ]
            if fallback:
                concept_pages[key] = fallback

    audit_json = {
        "page_count": len(pages),
        "courses": {course: len(course_pages) for course, course_pages in by_course.items()},
        "index_entry_count": len(index_entries),
        "mapped_index_entry_count": len(mapped_index),
        "unmapped_index_entry_count": len(unmapped_index),
        "added_concept_count": len(added_ids),
        "concept_pages": {
            f"{course}:{concept_id}": refs for (course, concept_id), refs in sorted(concept_pages.items())
        },
        "unmapped_index": unmapped_index,
    }
    (args.output_dir / "통합사회_교과서_전수점검.json").write_text(
        json.dumps(audit_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# 통합사회 1·2 교과서 전수 점검",
        "",
        "## 완전성 확인",
        "",
        f"- PDF: 2권, 총 {len(pages)}쪽",
        f"- 통합사회1: {len(by_course['통합사회1'])}쪽, {sum(p['char_count'] for p in by_course['통합사회1']):,}자",
        f"- 통합사회2: {len(by_course['통합사회2'])}쪽, {sum(p['char_count'] for p in by_course['통합사회2']):,}자",
        f"- 찾아보기 원장: {len(index_entries)}항목",
        f"- 기존 온톨로지에 직접 연결된 색인: {len(mapped_index)}항목",
        f"- 사례·인물·세부 제도 등을 포함한 미연결 색인: {len(unmapped_index)}항목",
        f"- 이미지·표지 중심 시각 검수: {sum(len(v) for v in VISUALLY_REVIEWED.values())}쪽 완료",
        "",
        "## 단원별 개념 범위",
        "",
    ]
    for course in ("통합사회1", "통합사회2"):
        lines.extend([f"### {course}", ""])
        for start, end, unit_name in UNITS[course]:
            ids = []
            for concept in concepts:
                refs = concept_pages.get((course, concept["id"]), [])
                if any(start <= ref <= end for ref in refs):
                    ids.append(concept["id"])
            core = [names[item] for item in ids if item not in added_ids]
            added = [names[item] for item in ids if item in added_ids]
            lines.extend(
                [
                    f"#### {unit_name} ({start}~{end}쪽)",
                    "",
                    f"- 기존 개념군: {', '.join(core) if core else '없음'}",
                    f"- 교과서 대조로 추가한 개념군: {', '.join(added) if added else '없음'}",
                    "",
                ]
            )

    lines.extend(
        [
            "## 새로 추가한 개념군",
            "",
            "| 영역 | 단계 | 개념 | 교과서 확인 쪽 |",
            "|---|:---:|---|---|",
        ]
    )
    for concept in concepts[first_added:]:
        refs = []
        for course in ("통합사회1", "통합사회2"):
            pages_text = ", ".join(map(str, concept_pages.get((course, concept["id"]), [])))
            if pages_text:
                refs.append(f"{course[-1]}권 {pages_text}")
        lines.append(
            f"| {'·'.join(concept['domains'])} | {concept['stage']} | {concept['name']} | {'; '.join(refs) or '표현·이미지 재검수'} |"
        )

    lines.extend(
        [
            "",
            "## 누락 방지 원칙",
            "",
            "- 777개 찾아보기 항목은 핵심 개념, 하위 개념, 인물, 법·제도, 지역·사례가 섞여 있으므로 모두 원장에 보존한다.",
            "- 온톨로지에 연결되지 않은 항목을 삭제하지 않고 별도 검토 대상으로 유지한다.",
            "- 지문 소재를 정할 때 핵심 개념뿐 아니라 관련 인물·제도·사례를 원장 쪽수로 다시 확인한다.",
            "- 표·지도·사진 중심 페이지는 렌더링 결과와 텍스트층을 함께 확인한다.",
        ]
    )
    (args.output_dir / "통합사회_교과서_전수점검.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    review_lines = [
        "# 교과서 색인 미연결 항목 검토 목록",
        "",
        "> 핵심 개념이 아니라 사례·인물·법률·기관일 수 있으나, 누락 방지를 위해 전부 보존한다.",
        "",
        "| 과목 | 항목 | 교과서 쪽 |",
        "|---|---|---|",
    ]
    for entry in unmapped_index:
        review_lines.append(
            f"| {entry['course']} | {entry['term'].replace(chr(173), '')} | {', '.join(map(str, entry['textbook_pages']))} |"
        )
    (args.output_dir / "통합사회_교과서_색인_미연결_검토.md").write_text(
        "\n".join(review_lines) + "\n", encoding="utf-8"
    )
    print(
        f"audited {len(pages)} pages and {len(index_entries)} index entries; "
        f"added {len(added_ids)} concept clusters"
    )


if __name__ == "__main__":
    main()
