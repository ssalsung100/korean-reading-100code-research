#!/usr/bin/env python3
"""Classify MEET visual materials and link them to canonical question IDs."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_MANIFEST = ROOT / "자료/MEET_언어추론/전사_검수완료/manifest.json"
EMBEDDED_MANIFEST = ROOT / "자료/MEET_언어추론/시각자료_원본/manifest.json"
OUT_JSON = ROOT / "자료/MEET_언어추론/검증/MEET_시각자료_문항별_분류_v1.json"
OUT_MD = ROOT / "자료/MEET_언어추론/검증/MEET_시각자료_문항별_분류_v1.md"
OUT_JSONL = ROOT / "data/meet_visuals.jsonl"


# (label, supplied-PDF page index, xref) -> inspected semantic metadata.
IMAGE_META = {
    ("2005예비", 4, 14): ("biological_illustration", "passage_figure", [12, 13, 14], True),
    ("2005예비", 4, 15): ("biological_illustration", "passage_figure", [12, 13, 14], True),
    ("2005", 26, 91): ("causal_flow_diagram_fragment", "question_figure", [20], True),
    ("2005", 26, 92): ("causal_flow_diagram_fragment", "question_figure", [20], True),
    ("2005", 26, 93): ("causal_flow_diagram_fragment", "question_figure", [20], True),
    ("2005", 26, 94): ("causal_flow_diagram_fragment", "question_figure", [20], True),
    ("2008", 75, 252): ("technical_diagram", "view_figure", [13], True),
    ("2009", 89, 295): ("artwork_photograph", "passage_figure", [8, 9, 10], True),
    ("2010", 107, 352): ("layout_rule", "layout_artifact", [], False),
    ("2011", 130, 426): ("architectural_diagram", "passage_figure", [29, 30, 31], True),
    ("2011", 131, 430): ("architectural_photograph", "view_figure", [31], True),
    ("2011", 133, 437): ("photograph", "passage_figure", [35, 36, 37], True),
    ("2011", 133, 438): ("sculpture_photograph", "passage_figure", [35, 36, 37], True),
    ("2011", 135, 445): ("map_projection_diagram", "view_figure", [40], True),
    ("2011", 135, 446): ("map_projection_diagram", "view_figure", [40], True),
    ("2012", 150, 494): ("annotated_photograph", "question_figure", [31], True),
    ("2012", 152, 501): ("artwork", "passage_figure", [35, 36, 37], True),
    ("2012", 152, 502): ("artwork", "passage_figure", [35, 36, 37], True),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def group_id(item: dict) -> str:
    numbers = item["questions"]
    return f"MEET-{item['label']}-Q{numbers[0]:02d}-{numbers[-1]:02d}"


def question_id(label: str, number: int) -> str:
    return f"MEET-{label}-Q{number:02d}"


def table_blocks(lines: list[str]) -> list[tuple[int, int, str]]:
    blocks = []
    index = 0
    while index < len(lines):
        if lines[index].lstrip().startswith("|"):
            start = index
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                index += 1
            block = "\n".join(lines[start:index])
            if re.search(r"(?m)^\|?\s*:?-{3,}", block) or "|---" in block:
                blocks.append((start + 1, index, block))
        else:
            index += 1
    return blocks


def table_kind(block: str) -> tuple[str, str]:
    choice_count = sum(symbol in block for symbol in "①②③④⑤")
    if choice_count >= 3:
        return "choice_matrix", "answer_options_encoded_as_table"
    if re.search(r"\d", block) and len(block.splitlines()) >= 4:
        return "data_table", "data_or_case_information"
    return "relation_table", "classification_or_correspondence"


def main() -> None:
    canonical = json.loads(CANONICAL_MANIFEST.read_text(encoding="utf-8"))["records"]
    embedded = json.loads(EMBEDDED_MANIFEST.read_text(encoding="utf-8"))
    records = []

    for asset in embedded:
        key = (str(asset["label"]), int(asset["official_pdf_page"]), int(asset["xref"]))
        if key not in IMAGE_META:
            raise RuntimeError(f"unclassified embedded asset: {key}")
        kind, role, direct_numbers, reusable = IMAGE_META[key]
        matching_groups = []
        needle = f"official_page_{asset['official_pdf_page']:03d}"
        for item in canonical:
            if str(item["label"]) == str(asset["label"]) and any(needle in page["file"] for page in item.get("official_pages", [])):
                matching_groups.append(item)
        if len(matching_groups) != 1:
            raise RuntimeError(f"page-to-group ambiguity {key}: {len(matching_groups)}")
        item = matching_groups[0]
        original = ROOT / asset["file"]
        records.append({
            "visual_id": f"MEET-{asset['label']}-P{asset['official_pdf_page']:03d}-X{asset['xref']}",
            "representation": kind,
            "role": role,
            "semantic_visual": role != "layout_artifact",
            "reusable_for_generation": reusable,
            "group_id": group_id(item),
            "linked_question_ids": [question_id(str(asset["label"]), number) for number in direct_numbers],
            "canonical_markdown": item["file"],
            "source_pdf_page_index": asset["official_pdf_page"],
            "display_pages": [page["display_page"] for page in item.get("official_pages", []) if needle in page["file"]],
            "original_file": asset["file"],
            "sha256": sha256(original.read_bytes()),
            "width": asset["width"],
            "height": asset["height"],
            "verification_status": "visually_classified_and_linked_to_canonical_group",
        })

    # Tables reconstructed in canonical Markdown are visual/relational assets
    # even when the PDF stored them as vector text rather than bitmap images.
    for item in canonical:
        path = ROOT / item["file"]
        lines = path.read_text(encoding="utf-8").splitlines()
        current_question = None
        question_at_line = {}
        for line_number, line in enumerate(lines, 1):
            match = re.match(r"^##\s+(\d+)\.", line)
            if match:
                current_question = int(match.group(1))
            question_at_line[line_number] = current_question
        for table_index, (start_line, end_line, block) in enumerate(table_blocks(lines), 1):
            number = question_at_line.get(start_line)
            kind, role = table_kind(block)
            records.append({
                "visual_id": f"{group_id(item)}-T{table_index:02d}",
                "representation": kind,
                "role": role,
                "semantic_visual": True,
                "reusable_for_generation": kind != "choice_matrix",
                "group_id": group_id(item),
                "linked_question_ids": [question_id(str(item["label"]), number)] if number else [question_id(str(item["label"]), q) for q in item["questions"]],
                "canonical_markdown": item["file"],
                "markdown_line": start_line,
                "markdown_line_end": end_line,
                "markdown_sha256": item["file_sha256"],
                "content_sha256": sha256(block.encode("utf-8")),
                "content_preview": block[:800],
                "verification_status": "canonical_markdown_structure_linked",
            })

    records.sort(key=lambda row: row["visual_id"])
    errors = []
    known_questions = {question_id(str(item["label"]), q) for item in canonical for q in item["questions"]}
    for row in records:
        unknown = set(row["linked_question_ids"]) - known_questions
        if unknown:
            errors.append(f"unknown question link {row['visual_id']}: {sorted(unknown)}")
    duplicate_ids = [key for key, value in Counter(row["visual_id"] for row in records).items() if value > 1]
    if duplicate_ids:
        errors.append(f"duplicate visual IDs: {duplicate_ids}")

    payload = {
        "status": "PASS" if not errors else "FAIL",
        "scope": "MEET 2005 preliminary, 2005, 2006-2012 canonical corpus",
        "counts": {
            "records": len(records),
            "embedded_images": sum("original_file" in row for row in records),
            "semantic_embedded_images": sum("original_file" in row and row["semantic_visual"] for row in records),
            "layout_artifacts": sum(not row["semantic_visual"] for row in records),
            "markdown_tables": sum("markdown_line" in row for row in records),
            "records_with_question_links": sum(bool(row["linked_question_ids"]) for row in records),
        },
        "representation_counts": dict(sorted(Counter(row["representation"] for row in records).items())),
        "role_counts": dict(sorted(Counter(row["role"] for row in records).items())),
        "errors": errors,
        "records": records,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSONL.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in records), encoding="utf-8")
    lines = [
        "# MEET 시각 자료 문항별 분류 v1",
        "",
        f"- 판정: **{payload['status']}**",
        f"- 전체 시각 레코드: **{payload['counts']['records']}개**",
        f"- PDF 내장 이미지: **{payload['counts']['embedded_images']}개** (의미 자료 {payload['counts']['semantic_embedded_images']}개, 지면 장식 {payload['counts']['layout_artifacts']}개)",
        f"- 정본 Markdown 표: **{payload['counts']['markdown_tables']}개**",
        f"- 문항 ID 연결: **{payload['counts']['records_with_question_links']}개**",
        "",
        "## 분류 원칙",
        "",
        "- PDF 내장 이미지는 접촉판으로 전수 판독하여 그림·사진·도식·장식물을 구분했다.",
        "- PDF에서 벡터/문자로 구성된 표는 정본 Markdown의 줄 위치와 문항 번호로 연결했다.",
        "- `layout_artifact`는 보존하되 문제 생성용 재사용 대상에서는 제외했다.",
        "",
        "## 문항별 연결",
        "",
        "| 자료 ID | 문항 | 역할 | 표현 | 정본/원본 |",
        "|---|---|---|---|---|",
    ]
    for row in records:
        source = row.get("original_file", f"{row['canonical_markdown']}:{row.get('markdown_line')}")
        lines.append(f"| {row['visual_id']} | {', '.join(row['linked_question_ids'])} | {row['role']} | {row['representation']} | `{source}` |")
    if errors:
        lines.extend(["", "## 오류", ""] + [f"- {error}" for error in errors])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({key: payload[key] for key in ("status", "counts", "representation_counts", "role_counts", "errors")}, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
