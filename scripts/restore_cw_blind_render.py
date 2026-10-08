#!/usr/bin/env python3
"""Crop the mechanically rendered CW graph from a local HWPX-to-PDF render.

The input PDF is produced by Hancom HWPFrame.HwpObject.SaveAs(..., 'PDF', '').
This script only crops the graphic region; it does not read or export page text.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import fitz


SOURCE = "고3 기출/2027 고3 국어 독서_Ⅳ. 기술.hwpx"
PAGE_INDEX = 17
# PDF points measured from the original HWP application render. The crop includes
# the graph's full external arrows and all five ellipses, with a small margin.
CROP = (48.0, 123.0, 281.0, 230.0)
SCALE = 4.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path, help="Hancom-rendered local PDF")
    parser.add_argument("output", type=Path, help="blind-only PNG output")
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()

    document = fitz.open(args.pdf)
    if len(document) <= PAGE_INDEX:
        raise SystemExit(f"PDF has {len(document)} pages; expected page index {PAGE_INDEX}")
    page = document[PAGE_INDEX]
    clip = fitz.Rect(*CROP)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=clip, alpha=False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pixmap.save(args.output)

    if args.manifest:
        manifest = {
            "blind_only": True,
            "passage_group": "G019",
            "case_id": "CW",
            "supplement_role": "original_hwpx_application_render_crop",
            "source_role": "anonymous_blind_source_supplement",
            "source_container": SOURCE,
            "source_render": "Hancom HWPFrame.HwpObject.SaveAs PDF; PyMuPDF crop",
            "rendered_pdf_page_index_zero_based": PAGE_INDEX,
            "crop_pdf_points": list(CROP),
            "scale": SCALE,
            "output": str(args.output),
            "quality": {
                "source_application_render": True,
                "full_graph_crop_verified_visually": True,
                "graph_interpretation_added": False,
                "answer_or_sdss_included": False,
                "reasoning_included": False,
            },
        }
        args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
