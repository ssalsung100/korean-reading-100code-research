#!/usr/bin/env python3
"""Build one provenance-aware catalog of reusable odd-form LEET visuals."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path("자료/LEET_언어이해")
VERIFY = ROOT / "검증"
OUT_JSON = VERIFY / "LEET_홀수형_시각자료_전체목록_v1.json"
OUT_MD = VERIFY / "LEET_홀수형_시각자료_전체목록_v1.md"

# The crop belongs to the passage/question group containing the official page.
PDF_GROUPS = {
    (2022, "q11_망막_밝기와_출력신호_보기"): [10, 12],
    (2022, "그림1_분할법의_예"): [16, 18],
    (2022, "그림2_계층법의_예"): [16, 18],
    (2023, "q15_나이의_정치적효과_연구디자인"): [13, 15],
    (2023, "제도가능곡선_모델"): [19, 21],
    (2023, "그림1과2_라이고_간섭계"): [25, 27],
    (2023, "q27_중력파검출기_민감도_그래프"): [25, 27],
    (2024, "사회적가치_이해관계자_성과와비용"): [13, 15],
    (2025, "q12_사법심사_법개정_여론변화"): [10, 12],
    (2025, "솔로우성장모형_생산량저축량감가상각량"): [16, 18],
    (2025, "q27_데이터베이스_트랜잭션_상황"): [25, 27],
    (2026, "DRD와_의사결정테이블"): [4, 6],
    (2026, "q9_유권자_민주주의신념과이념성향"): [7, 9],
    (2026, "q27_혼합물_전체부피_그래프"): [25, 27],
    (2027, "q5_제도결합_가치곡선"): [4, 6],
    (2027, "대류권_고도와_대기온도"): [10, 12],
    (2027, "q12_시대X와Y_복사에너지_표"): [10, 12],
    (2027, "그림1_신뢰게임"): [16, 18],
    (2027, "그림2_보복가능_신뢰게임"): [16, 18],
    (2027, "q18_보복선호_신뢰게임"): [16, 18],
}


def rel_link(path: str) -> str:
    return (Path("..") / Path(path).relative_to(ROOT)).as_posix()


def group_text(group: list[int]) -> str:
    return str(group[0]) if group[0] == group[1] else f"{group[0]}~{group[1]}"


def main() -> None:
    mapping = json.loads(
        (VERIFY / "HWP_홀수형_시각자료_문항매핑_v1.json").read_text(encoding="utf-8")
    )
    previews = json.loads(
        (VERIFY / "HWP_홀수형_그림_PNG작업본_manifest.json").read_text(encoding="utf-8")
    )
    pdf = json.loads((ROOT / "시각자료_원본" / "manifest.json").read_text(encoding="utf-8"))

    preview_by_key = {
        (paper["label"], item["asset_number"]): item
        for paper in previews["papers"]
        for item in paper["items"]
    }
    records: list[dict] = []
    errors: list[str] = []

    for paper in mapping["papers"]:
        for asset in paper["assets"]:
            if asset["kind"] == "view_box":
                continue
            row = {
                "year": asset["year"],
                "label": asset["label"],
                "source_type": "official_hwp_embedded",
                "asset_kind": asset["kind"],
                "asset_number": asset["asset_number"],
                "question_group": asset["question_group"],
                "mapping_confidence": asset["mapping_confidence"],
                "authoritative_file": asset["file"],
                "authoritative_sha256": asset.get("sha256"),
                "working_file": None,
                "verification": "stream-order question-group mapping",
            }
            if asset["kind"] == "embedded_figure":
                preview = preview_by_key.get((asset["label"], asset["asset_number"]))
                if preview is None:
                    errors.append(
                        f"PNG 작업본 누락: {asset['label']} figure {asset['asset_number']}"
                    )
                else:
                    row["working_file"] = preview["preview_file"]
                    row["working_sha256"] = preview["preview_sha256"]
                    row["pixel_match"] = preview["pixel_match"]
                    row["verification"] = (
                        "embedded binary hash + decoded-pixel-identical PNG + "
                        "stream-order question-group mapping"
                    )
            records.append(row)

    for item in pdf["records"]:
        key = (item["year"], item["name"])
        group = PDF_GROUPS.get(key)
        if group is None:
            errors.append(f"PDF 문항군 매핑 누락: {key}")
            continue
        records.append({
            "year": item["year"],
            "label": str(item["year"]),
            "source_type": "official_pdf_page_crop",
            "asset_kind": "page_crop",
            "asset_number": None,
            "name": item["name"],
            "page": item["page"],
            "question_group": group,
            "mapping_confidence": "high",
            "authoritative_file": item["official_page"],
            "authoritative_sha256": item["official_page_sha256"],
            "working_file": item["file"],
            "working_sha256": item["file_sha256"],
            "crop_box_pixels": item["crop_box_pixels"],
            "verification": "pixel-identical crop from official page render",
        })

    counts = Counter(row["asset_kind"] for row in records)
    expected = {
        "embedded_figure": mapping["embedded_figure_count"],
        "data_table": mapping["data_table_count"],
        "choice_table": mapping["choice_table_count"],
        "page_crop": pdf["record_count"],
    }
    if dict(counts) != expected:
        errors.append(f"종류별 수 불일치: {dict(counts)} != {expected}")
    for row in records:
        for field in ("authoritative_file", "working_file"):
            value = row.get(field)
            if value and not Path(value).is_file():
                errors.append(f"파일 없음: {value}")

    payload = {
        "status": "PASS" if not errors else "FAIL",
        "scope": "2009예비~2027 LEET 언어이해 홀수형의 재사용 가능 시각 자료",
        "record_count": len(records),
        "counts": expected,
        "structured_view_box_count_not_listed": mapping["view_box_count"],
        "notes": [
            "HWP 원본의 페이지·단 위치는 스트림 순서만으로 단정하지 않는다.",
            "HWP PNG는 원본 바이너리와 해독 픽셀이 같은 작업본이며 원본 바이너리가 정본이다.",
            "PDF PNG는 공식 페이지 렌더에서 자른 픽셀 동일 사본이다.",
            "구조화된 <보기> 125개는 HWP 문항 매핑 원장에 별도로 보존한다.",
        ],
        "errors": errors,
        "records": records,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# LEET 언어이해 홀수형 시각 자료 전체 목록 v1",
        "",
        f"- 결과: **{payload['status']}**",
        f"- 재사용 가능 자산: **{len(records)}개**",
        f"- HWP 원본 내장 그림: {expected['embedded_figure']}개",
        f"- HWP 의미 자료표: {expected['data_table']}개",
        f"- HWP 선지 배열표: {expected['choice_table']}개",
        f"- 공식 PDF 페이지 무손실 크롭: {expected['page_crop']}개",
        f"- 별도 구조 색인: `<보기>` {mapping['view_box_count']}개",
        "",
        "## 판정 범위",
        "",
        "HWP 그림 작업본은 원본 내장 바이너리와 해독 픽셀이 모두 일치하고, PDF 크롭은 공식 페이지 렌더의 해당 영역과 픽셀 단위로 일치한다. HWP 자산의 문항군은 본문·개체 스트림 순서로 확정했으나 원래 페이지와 단 위치까지 같다고 주장하지 않는다.",
        "",
        "## 자산 목록",
        "",
        "| 학년도 | 문항군 | 종류 | 이름/번호 | 정본 | 작업본 | 검증 |",
        "| --- | ---: | --- | --- | --- | --- | --- |",
    ]
    labels = {
        "embedded_figure": "내장 그림",
        "data_table": "자료표",
        "choice_table": "선지표",
        "page_crop": "공식 페이지 크롭",
    }
    for row in records:
        name = row.get("name") or f"#{row['asset_number']}"
        authoritative = Path(row["authoritative_file"])
        a_link = f"[{authoritative.name}]({rel_link(str(authoritative))})"
        working = row.get("working_file")
        w_link = "-"
        if working:
            working_path = Path(working)
            w_link = f"[{working_path.name}]({rel_link(str(working_path))})"
        lines.append(
            f"| {row['label']} | {group_text(row['question_group'])} | "
            f"{labels[row['asset_kind']]} | {name} | {a_link} | {w_link} | "
            f"{row['verification']} |"
        )
    lines.extend(["", "## 오류", ""])
    lines.extend(f"- {error}" for error in errors) if errors else lines.append("- 없음")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{payload['status']} records={len(records)} counts={expected} errors={len(errors)}")
    print(OUT_JSON)
    print(OUT_MD)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
