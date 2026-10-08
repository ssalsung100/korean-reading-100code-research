#!/usr/bin/env python3
"""Extract textbook back-of-book index entries with page references."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import fitz


ENTRY = re.compile(r"^(.+?)\x08\s*([0-9]+(?:\s*,\s*[0-9]+)*)\s*$")


def parse_index(pdf: Path, pages: list[int], course: str) -> list[dict]:
    document = fitz.open(pdf)
    entries: list[dict] = []
    for pdf_page in pages:
        page = document[pdf_page - 1]
        for block in page.get_text("blocks", sort=True):
            x0, y0, x1, y1, text, *_ = block
            text = text.strip()
            match = ENTRY.match(text)
            if not match:
                continue
            term = re.sub(r"\s+", " ", match.group(1)).strip()
            refs = [int(value.strip()) for value in match.group(2).split(",")]
            if len(term) < 2 or term in {"부록", "찾아 보기"}:
                continue
            entries.append(
                {
                    "course": course,
                    "term": term,
                    "textbook_pages": refs,
                    "index_pdf_page": pdf_page,
                    "column_x": round(x0, 1),
                    "y": round(y0, 1),
                }
            )
    return entries


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("social1", type=Path)
    parser.add_argument("social2", type=Path)
    parser.add_argument("json_output", type=Path)
    parser.add_argument("markdown_output", type=Path)
    args = parser.parse_args()

    entries = parse_index(args.social1, [161, 162, 163], "통합사회1")
    entries += parse_index(args.social2, [161, 162, 163, 164], "통합사회2")
    entries.sort(key=lambda item: (item["course"], item["term"]))

    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# 통합사회 교과서 찾아보기 전수 추출",
        "",
        f"- 추출 항목: {len(entries)}개",
        "- 용도: 개념·하위 개념·인물·제도·사례가 누락되지 않았는지 확인하는 원장",
        "",
        "| 과목 | 항목 | 교과서 쪽 | 색인 PDF 쪽 |",
        "|---|---|---|---:|",
    ]
    for entry in entries:
        refs = ", ".join(map(str, entry["textbook_pages"]))
        lines.append(f"| {entry['course']} | {entry['term']} | {refs} | {entry['index_pdf_page']} |")
    args.markdown_output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"extracted {len(entries)} textbook index entries")


if __name__ == "__main__":
    main()
