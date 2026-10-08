#!/usr/bin/env python3
"""Render and OCR the 2009 MEET pages whose PDF text layer is unusable.

Outputs are explicitly noncanonical.  Each OCR region retains the official
page render hash and word-confidence diagnostics so that every line can later
be checked against the supplied PDF page before promotion.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path

import fitz
from PIL import Image


ROOT = Path("자료/MEET_언어추론")
SOURCE = ROOT / "2005~2012_언어추론.pdf"
PAGE_DIR = ROOT / "페이지" / "2009"
OUT_DIR = ROOT / "OCR_초안" / "2009"
TOOL_ROOT = Path(".tools/tesseract/root").resolve()
TESSDATA = Path(".tools/tesseract/tessdata_best").resolve()
TESSERACT = TOOL_ROOT / "usr/bin/tesseract"
TORCH_LIB = Path.home() / ".local/lib/python3.10/site-packages/torch/lib"
FIRST_PAGE = 86
LAST_PAGE = 101
RENDER_MATRIX = (3, 3)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def regions(image: Image.Image) -> list[tuple[str, Image.Image, tuple[int, int, int, int]]]:
    width, height = image.size
    boxes = [
        ("header", (int(width * .04), int(height * .025), int(width * .96), int(height * .19))),
        ("left", (int(width * .045), int(height * .15), int(width * .497), int(height * .98))),
        ("right", (int(width * .503), int(height * .15), int(width * .955), int(height * .98))),
    ]
    return [(name, image.crop(box), box) for name, box in boxes]


def run_tesseract(image: Image.Image) -> tuple[list[str], list[dict]]:
    with tempfile.TemporaryDirectory(prefix="meet-ocr-") as temp:
        temp_path = Path(temp)
        image_path = temp_path / "input.png"
        output_base = temp_path / "out"
        image.save(image_path, dpi=(300, 300))
        env = os.environ.copy()
        env["LD_LIBRARY_PATH"] = f"{TOOL_ROOT / 'usr/lib/x86_64-linux-gnu'}:{TORCH_LIB}"
        env["TESSDATA_PREFIX"] = str(TESSDATA)
        subprocess.run(
            [
                str(TESSERACT), str(image_path), str(output_base),
                "-l", "kor+eng", "--psm", "6", "--dpi", "300", "tsv",
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            env=env,
        )
        raw_lines = output_base.with_suffix(".tsv").read_text(encoding="utf-8").splitlines()
        header = raw_lines[0].split("\t")
        words = []
        grouped: dict[tuple[str, str, str, str], list[str]] = {}
        for raw in raw_lines[1:]:
            values = raw.split("\t", len(header) - 1)
            if len(values) != len(header):
                continue
            row = dict(zip(header, values))
            token = (row.get("text") or "").strip()
            if not token:
                continue
            try:
                confidence = float(row.get("conf", -1))
                record = {
                    "text": token,
                    "confidence": confidence,
                    "left": int(row["left"]),
                    "top": int(row["top"]),
                    "width": int(row["width"]),
                    "height": int(row["height"]),
                }
            except (KeyError, ValueError):
                continue
            words.append(record)
            key = (row["page_num"], row["block_num"], row["par_num"], row["line_num"])
            grouped.setdefault(key, []).append(token)
        lines = [" ".join(tokens) for tokens in grouped.values()]
        return lines, words


def main() -> None:
    if not TESSERACT.is_file() or not (TESSDATA / "kor.traineddata").is_file():
        raise SystemExit("project-local Tesseract or Korean tessdata is missing")
    PAGE_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    source_hash = sha256(SOURCE)
    page_records = []

    with fitz.open(SOURCE) as document:
        for official_page in range(FIRST_PAGE, LAST_PAGE + 1):
            page_path = PAGE_DIR / f"official_page_{official_page:03d}_3x.png"
            if not page_path.is_file():
                pixmap = document[official_page - 1].get_pixmap(matrix=fitz.Matrix(*RENDER_MATRIX), alpha=False)
                pixmap.save(page_path)
            image = Image.open(page_path).convert("RGB")
            region_records = []
            markdown = [
                f"# 2009 MEET 언어추론 공식 PDF {official_page}쪽 OCR 초안\n\n",
                "> **비정본 OCR 초안.** 공식 페이지 이미지와 직접 대조하기 전에는 인용하거나 코드 판정에 사용하지 않는다.\n",
            ]
            for name, crop, box in regions(image):
                lines, words = run_tesseract(crop)
                markdown.extend([f"\n## {name}\n\n", "\n".join(lines), "\n"])
                valid_conf = [word["confidence"] for word in words if word["confidence"] >= 0]
                region_records.append({
                    "name": name,
                    "crop_box": list(box),
                    "line_count": len(lines),
                    "word_count": len(words),
                    "mean_confidence": sum(valid_conf) / len(valid_conf) if valid_conf else None,
                    "low_confidence_words": [word for word in words if 0 <= word["confidence"] < 80],
                    "lines": lines,
                    "words": words,
                })
                print(official_page, name, len(lines), len(words), flush=True)
            md_path = OUT_DIR / f"official_page_{official_page:03d}.md"
            json_path = OUT_DIR / f"official_page_{official_page:03d}.json"
            md_path.write_text("".join(markdown), encoding="utf-8")
            record = {
                "status": "unverified_tesseract_ocr",
                "engine": "project_local_tesseract_4_kor_eng_best",
                "source_pdf": str(SOURCE),
                "source_pdf_sha256": source_hash,
                "official_pdf_page": official_page,
                "official_page_image": str(page_path),
                "official_page_image_sha256": sha256(page_path),
                "render_matrix": list(RENDER_MATRIX),
                "markdown": str(md_path),
                "regions": region_records,
            }
            json_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
            page_records.append({
                "official_pdf_page": official_page,
                "page_image": str(page_path),
                "page_image_sha256": record["official_page_image_sha256"],
                "ocr_json": str(json_path),
                "ocr_markdown": str(md_path),
                "status": record["status"],
            })
    (OUT_DIR / "manifest.json").write_text(
        json.dumps({
            "status": "unverified_ocr",
            "source_pdf": str(SOURCE),
            "source_pdf_sha256": source_hash,
            "pages": page_records,
            "warning": "OCR wording is noncanonical until every line is checked against the linked official page image.",
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("wrote pages", len(page_records), flush=True)


if __name__ == "__main__":
    main()
