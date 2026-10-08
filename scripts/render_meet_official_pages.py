#!/usr/bin/env python3
"""Render the supplied MEET combined PDF into authoritative 3x page PNGs.

The rendered pages are visual comparison sources for canonical Markdown
transcription. Existing files are preserved unless --force is supplied.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import fitz


ROOT = Path("자료/MEET_언어추론")
SOURCE = ROOT / "2005~2012_언어추론.pdf"
OUT_ROOT = ROOT / "페이지"
SPECS = {
    "2005예비": (1, 19),
    "2005": (20, 38),
    "2006": (39, 53),
    "2007": (54, 69),
    "2008": (70, 85),
    "2009": (86, 101),
    "2010": (102, 117),
    "2011": (118, 135),
    "2012": (136, 154),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("labels", nargs="*", help="시험 구분. 생략하면 전체")
    parser.add_argument("--force", action="store_true", help="기존 PNG도 다시 렌더링")
    args = parser.parse_args()
    unknown = sorted(set(args.labels) - set(SPECS))
    if unknown:
        parser.error(f"알 수 없는 시험 구분: {', '.join(unknown)}")
    labels = args.labels or list(SPECS)

    records = []
    with fitz.open(SOURCE) as document:
        for label in labels:
            first, last = SPECS[label]
            target_dir = OUT_ROOT / label
            target_dir.mkdir(parents=True, exist_ok=True)
            for page_no in range(first, last + 1):
                target = target_dir / f"official_page_{page_no:03d}_3x.png"
                if args.force or not target.is_file():
                    pixmap = document[page_no - 1].get_pixmap(matrix=fitz.Matrix(3, 3), alpha=False)
                    pixmap.save(target)
                records.append({
                    "label": label,
                    "official_pdf_page": page_no,
                    "file": str(target),
                    "sha256": sha256(target),
                    "render_matrix": [3, 3],
                    "width": fitz.Pixmap(str(target)).width,
                    "height": fitz.Pixmap(str(target)).height,
                })
            print(f"{label}: {last - first + 1} pages")

    prior_records = []
    manifest_path = OUT_ROOT / "manifest.json"
    if manifest_path.is_file() and labels != list(SPECS):
        prior = json.loads(manifest_path.read_text(encoding="utf-8"))
        prior_records = [record for record in prior.get("records", []) if record["label"] not in labels]
    all_records = sorted(prior_records + records, key=lambda record: record["official_pdf_page"])
    manifest = {
        "status": "official_pdf_page_renders_complete" if len(all_records) == 154 else "partial",
        "source": str(SOURCE),
        "source_sha256": sha256(SOURCE),
        "render_matrix": [3, 3],
        "page_count": len(all_records),
        "records": all_records,
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"manifest: {len(all_records)} pages")


if __name__ == "__main__":
    main()
