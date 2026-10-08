#!/usr/bin/env python3
"""Link the official answer tables to passage ranges in the HWPX text corpus."""
from __future__ import annotations

import json
import re
from pathlib import Path

text_path = Path("고3 기출/hwpx_텍스트_연도별.md")
answer_path = Path("자료/평가원_정답표/normalized_answer_keys.json")
out_path = Path("자료/평가원_정답표/passage_answer_links.json")

source = text_path.read_text(encoding="utf-8")
tables = json.loads(answer_path.read_text(encoding="utf-8"))["tables"]


def parse_exam(title: str) -> tuple[int, str, str | None, list[str]] | None:
    y = re.search(r"(20\d{2})학년도", title)
    if not y:
        return None
    year = int(y.group(1))
    if "수능" in title and "모평" not in title and "예시" not in title and "예비" not in title:
        exam = "수능"
        month = None
    else:
        exam = "수능 모의평가"
        if "6월" in title:
            month = "6월"
        elif "9월" in title:
            month = "9월"
        elif "예시" in title:
            month = "예시"
        elif "예비" in title:
            month = "예비"
        else:
            month = None
    variants: list[str] = []
    # The corpus uses A/B/AB suffixes in the title for the two-track years.
    suffix = re.search(r"(?:모평|수능)(AB|A|B)\s*$", title)
    if suffix:
        variants = list(suffix.group(1))
    return year, exam, month, variants


links = []
for m in re.finditer(r"^### \[([^]]+)\]\s*(.+)$", source, re.M):
    range_id, title = m.groups()
    parsed = parse_exam(title.strip())
    if not parsed:
        continue
    year, exam, month, variants = parsed
    q = re.match(r"(\d+)(?:번~(\d+)번)?", title)
    # The title itself contains the question span after the exam name; use the
    # final occurrences to avoid confusing the academic year with question #.
    nums = re.findall(r"(\d+)번", title)
    q_start = int(nums[-2]) if len(nums) >= 2 else (int(nums[-1]) if nums else None)
    q_end = int(nums[-1]) if len(nums) >= 2 else q_start
    candidates = []
    for table in tables:
        if table["academic_year"] != year or table["exam_type"] != exam:
            continue
        if exam == "수능 모의평가" and table.get("month") != month:
            continue
        if variants and table.get("variant") not in variants:
            continue
        candidates.append(table["table_id"])
    links.append({
        "section_id": range_id,
        "heading": title.strip(),
        "academic_year": year,
        "exam_type": exam,
        "month": month,
        "variants": variants,
        "question_start": q_start,
        "question_end": q_end,
        "answer_table_ids": candidates,
        "link_status": "linked" if candidates else "ocr_or_missing",
    })

payload = {
    "source_passages": str(text_path),
    "source_answers": str(answer_path),
    "section_count": len(links),
    "linked_sections": sum(x["link_status"] == "linked" for x in links),
    "unlinked_sections": sum(x["link_status"] != "linked" for x in links),
    "links": links,
}
out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"wrote {out_path}: {len(links)} sections, {payload['linked_sections']} linked")
