#!/usr/bin/env python3
"""Integrity gate for KICE-compilation and MEET visual-question links."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_JSON = ROOT / "분석/평가원_MEET_시각자료_연결_검증_v1.json"
REPORT_MD = ROOT / "분석/평가원_MEET_시각자료_연결_검증_v1.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    kice = json.loads((ROOT / "자료/평가원_독서_시각자료_원본/manifest.json").read_text(encoding="utf-8"))
    meet = json.loads((ROOT / "자료/MEET_언어추론/검증/MEET_시각자료_문항별_분류_v1.json").read_text(encoding="utf-8"))
    kice_questions = {json.loads(line)["question_id"] for line in (ROOT / "data/kice_questions.jsonl").read_text(encoding="utf-8").splitlines() if line}
    meet_questions = {json.loads(line)["question_id"] for line in (ROOT / "data/meet_questions.jsonl").read_text(encoding="utf-8").splitlines() if line}
    errors = []

    for row in kice["records"]:
        for link in row["linked_questions"]:
            if link["question_id"] not in kice_questions:
                errors.append(f"KICE unknown question: {row['asset_id']} -> {link['question_id']}")
        if "original_file" in row:
            path = ROOT / row["original_file"]
            if not path.exists() or sha256(path) != row["sha256"]:
                errors.append(f"KICE image hash/file error: {row['asset_id']}")
    for row in meet["records"]:
        for question_id in row["linked_question_ids"]:
            if question_id not in meet_questions:
                errors.append(f"MEET unknown question: {row['visual_id']} -> {question_id}")
        if "original_file" in row:
            path = ROOT / row["original_file"]
            if not path.exists() or sha256(path) != row["sha256"]:
                errors.append(f"MEET image hash/file error: {row['visual_id']}")

    counts = {
        "kice_records": len(kice["records"]),
        "kice_images": sum("original_file" in row for row in kice["records"]),
        "kice_hwpx_tables": sum(row.get("object_type") == "hwpx_table" for row in kice["records"]),
        "kice_semantic_objects": sum(row.get("semantic_visual", True) for row in kice["records"]),
        "kice_records_linked": sum(bool(row["linked_questions"]) for row in kice["records"]),
        "meet_records": len(meet["records"]),
        "meet_embedded_images": sum("original_file" in row for row in meet["records"]),
        "meet_markdown_tables": sum("markdown_line" in row for row in meet["records"]),
        "meet_semantic_objects": sum(row["semantic_visual"] for row in meet["records"]),
        "meet_records_linked": sum(bool(row["linked_question_ids"]) for row in meet["records"]),
    }
    result = {"status": "PASS" if not errors else "FAIL", "counts": counts, "errors": errors}
    REPORT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# 평가원·MEET 시각 자료 연결 검증 v1",
        "",
        f"- 판정: **{result['status']}**",
        "",
        "## 평가원 독서 편집 HWPX",
        "",
        f"- 전체 객체: {counts['kice_records']}개",
        f"- 내장 이미지: {counts['kice_images']}개",
        f"- HWPX 표 객체: {counts['kice_hwpx_tables']}개",
        f"- 의미 시각 객체: {counts['kice_semantic_objects']}개",
        f"- 문항 연결 완료: {counts['kice_records_linked']}개",
        "- 주의: 이 HWPX는 로컬 기출 편집본이며, 원본 평가원 컨테이너라고 주장하지 않는다.",
        "",
        "## MEET 정본",
        "",
        f"- 전체 객체: {counts['meet_records']}개",
        f"- PDF 내장 이미지: {counts['meet_embedded_images']}개",
        f"- 정본 Markdown 표: {counts['meet_markdown_tables']}개",
        f"- 의미 시각 객체: {counts['meet_semantic_objects']}개",
        f"- 문항 연결 완료: {counts['meet_records_linked']}개 (지면 장식 1개는 의도적으로 무연결)",
        "",
        "## 오류",
        "",
    ]
    lines.extend(f"- {error}" for error in errors) if errors else lines.append("- 없음")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
