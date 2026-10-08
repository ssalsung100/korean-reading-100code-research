#!/usr/bin/env python3
"""Render official LEET PDF pages to deterministic PNG files."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import fitz


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--scale", type=float, default=1.5)
    parser.add_argument("--pages", help="comma-separated 1-based pages; default all")
    args = parser.parse_args()

    document = fitz.open(args.pdf)
    numbers = (
        [int(value) for value in args.pages.split(",") if value.strip()]
        if args.pages else list(range(1, len(document) + 1))
    )
    args.output.mkdir(parents=True, exist_ok=True)
    records = []
    for number in numbers:
        target = args.output / f"page_{number:03d}.png"
        pixmap = document[number - 1].get_pixmap(
            matrix=fitz.Matrix(args.scale, args.scale), alpha=False
        )
        pixmap.save(str(target))
        records.append({
            "page": number,
            "file": str(target),
            "width": pixmap.width,
            "height": pixmap.height,
            "sha256": sha256(target),
        })
    manifest = args.output / "render_manifest.json"
    manifest.write_text(json.dumps({
        "source_pdf": str(args.pdf),
        "source_sha256": sha256(args.pdf),
        "scale": args.scale,
        "page_count": len(records),
        "pages": records,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"rendered={len(records)} output={args.output}")


if __name__ == "__main__":
    main()
