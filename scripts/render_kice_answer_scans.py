#!/usr/bin/env python3
"""Render official image-only KICE answer sheets for visual transcription."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import fitz


ROOT = Path("자료/평가원_정답표")
OUT = ROOT / "OCR대조_페이지"
MANIFEST_OUT = OUT / "manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def select_answer_pdf(candidates: list[str]) -> Path:
    ranked = []
    for value in candidates:
        path = Path(value)
        document = fitz.open(path)
        # A one-page candidate is the answer table rather than the test paper
        # or commentary.  Preserve all pages if the only official candidate is
        # a multi-page answer PDF (e.g. 2025).
        ranked.append((len(document), path))
        document.close()
    one_page = [path for pages, path in ranked if pages == 1]
    return one_page[-1] if one_page else min(ranked, key=lambda x: x[0])[1]


def main() -> None:
    source = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    records = []
    OUT.mkdir(parents=True, exist_ok=True)
    for item in source["entries"]:
        if item.get("status") != "ocr_required":
            continue
        pdf = select_answer_pdf(item["answer_pdf_candidates"])
        month = item.get("month") or "수능"
        target_dir = OUT / f"{item['academic_year']}_{month}"
        target_dir.mkdir(parents=True, exist_ok=True)
        document = fitz.open(pdf)
        pages = []
        for page_number, page in enumerate(document, start=1):
            pixmap = page.get_pixmap(matrix=fitz.Matrix(3.0, 3.0), alpha=False)
            target = target_dir / f"page_{page_number:03d}.png"
            pixmap.save(target)
            pages.append({
                "page": page_number,
                "file": str(target),
                "sha256": sha256(target),
                "width": pixmap.width,
                "height": pixmap.height,
            })
        document.close()
        records.append({
            "academic_year": item["academic_year"],
            "exam_type": item["exam_type"],
            "month": item.get("month"),
            "official_page": item["official_page"],
            "source_pdf": str(pdf),
            "source_pdf_sha256": sha256(pdf),
            "pages": pages,
        })
        print(pdf, "->", len(pages), "page(s)")
    MANIFEST_OUT.write_text(json.dumps({
        "status": "official_scan_pages_rendered",
        "record_count": len(records),
        "records": records,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(MANIFEST_OUT)


if __name__ == "__main__":
    main()
