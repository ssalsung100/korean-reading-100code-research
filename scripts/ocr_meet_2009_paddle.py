#!/usr/bin/env python3
"""Create a second, noncanonical PaddleOCR draft for 2009 MEET pages."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from PIL import Image


ROOT = Path("자료/MEET_언어추론")
SOURCE = ROOT / "2005~2012_언어추론.pdf"
PAGE_DIR = ROOT / "페이지" / "2009"
OUT_DIR = ROOT / "OCR_초안_Paddle" / "2009"
TORCH_LIB = Path.home() / ".local/lib/python3.10/site-packages/torch/lib"
ENGINE = "korean_PP-OCRv4_meet_official_page_3x_v1"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def prepare_engine():
    os.environ["LD_LIBRARY_PATH"] = str(TORCH_LIB) + ":" + os.environ.get("LD_LIBRARY_PATH", "")
    if not hasattr(np, "sctypes"):
        np.sctypes = {
            "int": [np.int8, np.int16, np.int32, np.int64],
            "uint": [np.uint8, np.uint16, np.uint32, np.uint64],
            "float": [np.float16, np.float32, np.float64],
            "complex": [np.complex64, np.complex128],
            "others": [bool, object, str, bytes],
        }
    from paddleocr import PaddleOCR
    return PaddleOCR(lang="korean", use_angle_cls=False, show_log=False, det_limit_side_len=2400)


def region_boxes(image: Image.Image):
    width, height = image.size
    return [
        ("header", (int(width * .04), int(height * .025), int(width * .96), int(height * .19))),
        ("left", (int(width * .045), int(height * .15), int(width * .497), int(height * .98))),
        ("right", (int(width * .503), int(height * .15), int(width * .955), int(height * .98))),
    ]


def token_record(item, offset_x: int, offset_y: int) -> dict:
    box, (text, confidence) = item
    points = [[float(x) + offset_x, float(y) + offset_y] for x, y in box]
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return {
        "text": text,
        "confidence": float(confidence),
        "box": points,
        "left": min(xs),
        "right": max(xs),
        "top": min(ys),
        "bottom": max(ys),
        "center_y": (min(ys) + max(ys)) / 2,
    }


def group_lines(tokens: list[dict]) -> list[list[dict]]:
    lines: list[list[dict]] = []
    for token in sorted(tokens, key=lambda item: (item["center_y"], item["left"])):
        height = max(1.0, token["bottom"] - token["top"])
        chosen = None
        for line in reversed(lines[-5:]):
            center = sum(item["center_y"] for item in line) / len(line)
            line_height = sum(item["bottom"] - item["top"] for item in line) / len(line)
            if abs(token["center_y"] - center) <= max(5.0, min(height, line_height) * .45):
                chosen = line
                break
        if chosen is None:
            chosen = []
            lines.append(chosen)
        chosen.append(token)
    for line in lines:
        line.sort(key=lambda item: item["left"])
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-pages", type=int, default=0)
    args = parser.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pages = sorted(PAGE_DIR.glob("official_page_*_3x.png"))
    if args.max_pages:
        pages = pages[:args.max_pages]
    if not pages:
        raise SystemExit("rendered 2009 official pages are missing")
    engine = prepare_engine()
    records = []
    for page_path in pages:
        official_page = int(page_path.stem.split("_")[2])
        image = Image.open(page_path).convert("RGB")
        regions = []
        markdown = [
            f"# 2009 MEET 공식 PDF {official_page}쪽 PaddleOCR 초안\n\n",
            "> **비정본 보조 OCR.** 공식 페이지와 직접 대조하기 전에는 확정 원문으로 사용하지 않는다.\n",
        ]
        for name, box in region_boxes(image):
            crop = image.crop(box)
            result = engine.ocr(np.asarray(crop), cls=False)
            raw = result[0] if result and len(result) == 1 else (result or [])
            tokens = [token_record(item, box[0], box[1]) for item in raw if item and item[1][0].strip()]
            lines = group_lines(tokens)
            text_lines = [" ".join(item["text"] for item in line) for line in lines]
            markdown.extend([f"\n## {name}\n\n", "\n".join(text_lines), "\n"])
            regions.append({
                "name": name,
                "crop_box": list(box),
                "token_count": len(tokens),
                "mean_confidence": sum(item["confidence"] for item in tokens) / len(tokens) if tokens else None,
                "tokens": tokens,
                "lines": text_lines,
            })
            print(official_page, name, len(tokens), flush=True)
        md_path = OUT_DIR / f"official_page_{official_page:03d}.md"
        json_path = OUT_DIR / f"official_page_{official_page:03d}.json"
        md_path.write_text("".join(markdown), encoding="utf-8")
        data = {
            "status": "unverified_paddle_ocr",
            "engine": ENGINE,
            "source_pdf": str(SOURCE),
            "source_pdf_sha256": sha256(SOURCE),
            "official_pdf_page": official_page,
            "official_page_image": str(page_path),
            "official_page_image_sha256": sha256(page_path),
            "render_matrix": [3, 3],
            "regions": regions,
        }
        json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        records.append({
            "official_pdf_page": official_page,
            "page_image": str(page_path),
            "page_image_sha256": data["official_page_image_sha256"],
            "json": str(json_path),
            "markdown": str(md_path),
            "status": data["status"],
        })
    (OUT_DIR / "manifest.json").write_text(json.dumps({
        "status": "unverified_secondary_ocr",
        "engine": ENGINE,
        "pages": records,
        "warning": "PaddleOCR is an independent aid; the official page image remains authoritative.",
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", len(records), "pages", flush=True)


if __name__ == "__main__":
    main()
