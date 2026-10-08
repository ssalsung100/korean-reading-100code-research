#!/usr/bin/env python3
"""Extract a bounded page range from a textbook PDF into loss-aware JSON."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import fitz


def normalize(text: str) -> str:
    text = text.replace("\x00", "").replace("\u200b", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def extract_headings(page: fitz.Page) -> list[str]:
    data = page.get_text("dict", sort=True)
    candidates: list[tuple[float, str]] = []
    for block in data.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            text = normalize("".join(span.get("text", "") for span in spans))
            if not text or len(text) > 90:
                continue
            size = max((float(span.get("size", 0)) for span in spans), default=0)
            if size >= 13:
                candidates.append((size, text))
    candidates.sort(key=lambda item: -item[0])
    seen: set[str] = set()
    headings = []
    for _, text in candidates:
        if text not in seen:
            seen.add(text)
            headings.append(text)
    return headings[:12]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("start", type=int, help="1-based inclusive page")
    parser.add_argument("end", type=int, help="1-based inclusive page")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    document = fitz.open(args.pdf)
    start = max(1, args.start)
    end = min(len(document), args.end)
    pages = []
    for page_number in range(start, end + 1):
        page = document[page_number - 1]
        text = normalize(page.get_text("text", sort=True))
        image_count = len(page.get_images(full=True))
        pages.append(
            {
                "source_file": args.pdf.as_posix(),
                "pdf_page": page_number,
                "text": text,
                "char_count": len(text),
                "image_count": image_count,
                "headings": extract_headings(page),
                "needs_visual_review": len(text) < 180 or image_count >= 8,
            }
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(pages, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{args.pdf.name}: extracted pages {start}-{end} ({len(pages)} pages)")


if __name__ == "__main__":
    main()
