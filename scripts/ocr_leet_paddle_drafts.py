#!/usr/bin/env python3
"""Create a second, noncanonical PaddleOCR draft for image-only LEET pages.

Odd and single question forms are targeted by default because they are the
working forms for passage analysis. An even form can be requested explicitly.
Every token retains its official-page coordinates and confidence. Output never
enters the canonical ``텍스트`` directory.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import fitz
import numpy as np
from PIL import Image


ROOT = Path("자료/LEET_언어이해")
OUT = ROOT / "OCR_초안_Paddle"
TORCH_LIB = Path.home() / ".local/lib/python3.10/site-packages/torch/lib"
ENGINE_VERSION = "korean_PP-OCRv4_official_pdf_3x_det2400_v2"


def prepare_imports():
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
    return PaddleOCR


def regions(image: Image.Image):
    w, h = image.size
    return [
        ("left", (int(w * .045), int(h * .035), int(w * .497), int(h * .975))),
        ("right", (int(w * .503), int(h * .035), int(w * .955), int(h * .975))),
    ]


def token_record(item, offset_x: int, offset_y: int) -> dict:
    box, (text, confidence) = item
    points = [[float(x) + offset_x, float(y) + offset_y] for x, y in box]
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return {
        "text": text, "confidence": float(confidence), "box": points,
        "left": min(xs), "right": max(xs), "top": min(ys), "bottom": max(ys),
        "center_y": (min(ys) + max(ys)) / 2,
    }


def group_lines(tokens: list[dict]) -> list[list[dict]]:
    lines: list[list[dict]] = []
    for token in sorted(tokens, key=lambda t: (t["center_y"], t["left"])):
        height = max(1.0, token["bottom"] - token["top"])
        chosen = None
        for line in reversed(lines[-4:]):
            center = sum(t["center_y"] for t in line) / len(line)
            line_height = sum(t["bottom"] - t["top"] for t in line) / len(line)
            if abs(token["center_y"] - center) <= max(5.0, min(height, line_height) * .45):
                chosen = line
                break
        if chosen is None:
            chosen = []
            lines.append(chosen)
        chosen.append(token)
    for line in lines:
        line.sort(key=lambda t: t["left"])
    return lines


def page_complete(json_path: Path) -> bool:
    if not json_path.is_file():
        return False
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return (data.get("status") == "unverified_paddle_ocr" and
            data.get("engine_version") == ENGINE_VERSION and len(data.get("regions", [])) == 2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--years", nargs="*", default=["2022", "2023", "2027"])
    parser.add_argument(
        "--forms",
        nargs="*",
        choices=["question_odd", "question_even", "question"],
        default=["question_odd", "question"],
        help="처리할 문제지 형식(기본값: 홀수형·단일형)",
    )
    parser.add_argument("--max-pages", type=int, default=0)
    args = parser.parse_args()
    years = set(args.years)
    forms = set(args.forms)
    records = json.loads((ROOT / "extracted_assets_manifest.json").read_text(encoding="utf-8"))["records"]
    targets = [r for r in records if r["label"] in years and r["page_render_count"] and
               r["kind"] in forms]
    PaddleOCR = prepare_imports()
    ocr = PaddleOCR(lang="korean", use_angle_cls=False, show_log=False, det_limit_side_len=2400)
    manifest = []
    processed = 0
    for rec in targets:
        source_doc = fitz.open(rec["source_file"])
        target_dir = OUT / rec["label"] / rec["kind"]
        target_dir.mkdir(parents=True, exist_ok=True)
        pages = []
        for page in rec["page_renders"]:
            if args.max_pages and processed >= args.max_pages:
                break
            page_no = page["page"]
            json_path = target_dir / f"page_{page_no:03d}.json"
            md_path = target_dir / f"page_{page_no:03d}.md"
            if page_complete(json_path) and md_path.is_file():
                pages.append({"page": page_no, "json": str(json_path), "markdown": str(md_path), "reused": True})
                processed += 1
                print(rec["label"], rec["kind"], page_no, "reuse", flush=True)
                continue
            source_page = source_doc[page_no - 1]
            pix = source_page.get_pixmap(matrix=fitz.Matrix(3, 3), alpha=False)
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            page_regions = []
            md = [f"# {rec['label']} {rec['kind']} page {page_no} PaddleOCR 초안\n\n",
                  "> 비정본 OCR 초안이다. 공식 페이지와 직접 대조하기 전에는 사용하지 않는다.\n"]
            for name, box in regions(image):
                crop = image.crop(box)
                result = ocr.ocr(np.asarray(crop), cls=False)
                raw = result[0] if result and len(result) == 1 else (result or [])
                tokens = [token_record(item, box[0], box[1]) for item in raw if item and item[1][0].strip()]
                lines = group_lines(tokens)
                text_lines = [" ".join(t["text"] for t in line) for line in lines]
                md.extend([f"\n\n## {name}\n\n", "\n".join(text_lines), "\n"])
                page_regions.append({
                    "name": name, "crop_box": list(box), "token_count": len(tokens),
                    "mean_confidence": sum(t["confidence"] for t in tokens) / len(tokens) if tokens else None,
                    "tokens": tokens, "lines": text_lines,
                })
                print(rec["label"], rec["kind"], page_no, name, len(tokens), flush=True)
            data = {
                "status": "unverified_paddle_ocr", "engine_version": ENGINE_VERSION,
                "label": rec["label"], "kind": rec["kind"],
                "page": page_no, "official_page_image": page["file"],
                "official_page_sha256": page.get("sha256"), "source_file": rec["source_file"],
                "source_sha256": rec["source_sha256"], "render_matrix": [3, 3], "regions": page_regions,
            }
            json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            md_path.write_text("".join(md), encoding="utf-8")
            pages.append({"page": page_no, "json": str(json_path), "markdown": str(md_path), "reused": False})
            processed += 1
        manifest.append({"label": rec["label"], "kind": rec["kind"], "pages": pages})
        source_doc.close()
        if args.max_pages and processed >= args.max_pages:
            break
    (OUT / "manifest.json").write_text(json.dumps({
        "status": "unverified_secondary_ocr", "records": manifest,
        "warning": "No OCR text is canonical before direct official-page comparison."
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print("processed", processed, flush=True)


if __name__ == "__main__":
    main()
