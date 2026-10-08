#!/usr/bin/env python3
"""Preserve the official 2027 KICE June/September Korean Q1-17 assets.

This script copies the four supplied PDFs, renders only source pages 1-6,
records positioned text lines, and exports the semantic visual objects used by
questions 1-17.  It deliberately does not OCR or rewrite the source text.
"""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "자료" / "평가원_국어"

EXAMS = {
    "6월": {
        "question": ROOT / "2027학년도-6월-모의평가-국어-문제 (2).pdf",
        "answer": ROOT / "2027학년도-6월-모의평가-국어-정답 (1).pdf",
        "visuals": [],
    },
    "9월": {
        "question": ROOT / "2027학년도-9월-모의평가-국어-문제 (1).pdf",
        "answer": ROOT / "2027학년도-9월-모의평가-국어-정답 (1).pdf",
        "visuals": [
            {
                "asset_id": "KICE-2027-09-Q09-choice-table",
                "question_number": 9,
                "page": 3,
                "kind": "choice_table",
                "method": "page_crop",
                "clip": [430.0, 950.0, 625.0, 1075.0],
                "filename": "q09_선지_대응표.png",
            },
            {
                "asset_id": "KICE-2027-09-Q13-adapter-diagram",
                "question_number": 13,
                "page": 5,
                "kind": "process_diagram",
                "method": "embedded_image",
                "xref": 13,
                "filename": "q13_어댑터_구조도.png",
            },
        ],
    },
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def positioned_lines(page: fitz.Page) -> list[dict]:
    rows: list[dict] = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            text = "".join(span["text"] for span in line["spans"])
            if not text.strip():
                continue
            x0, y0, x1, y1 = line["bbox"]
            rows.append({
                "bbox": [round(x0, 3), round(y0, 3), round(x1, 3), round(y1, 3)],
                "text": text,
            })
    return rows


def main() -> None:
    original_dir = BASE / "원본" / "2027"
    raw_dir = BASE / "좌표텍스트" / "2027"
    visual_dir = BASE / "시각자료_원본" / "2027"
    original_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)
    visual_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "schema_version": "1.0",
        "scope": "2027학년도 6월·9월 모의평가 국어 공통 1~17번",
        "exams": [],
        "visuals": [],
    }

    for month, spec in EXAMS.items():
        question_src: Path = spec["question"]
        answer_src: Path = spec["answer"]
        if not question_src.exists() or not answer_src.exists():
            raise FileNotFoundError(f"missing source PDF for {month}")

        question_dst = original_dir / f"2027_{month}_모의평가_국어_문제.pdf"
        answer_dst = original_dir / f"2027_{month}_모의평가_국어_정답.pdf"
        shutil.copy2(question_src, question_dst)
        shutil.copy2(answer_src, answer_dst)

        document = fitz.open(question_src)
        if len(document) < 6:
            raise ValueError(f"{month}: expected at least six pages")

        page_dir = BASE / "페이지" / "2027" / month
        page_dir.mkdir(parents=True, exist_ok=True)
        page_records = []
        raw_pages = []
        for page_index in range(6):
            page = document[page_index]
            page_path = page_dir / f"page_{page_index + 1:03d}.png"
            page.get_pixmap(matrix=fitz.Matrix(3, 3), alpha=False).save(page_path)
            page_records.append({
                "page": page_index + 1,
                "path": str(page_path.relative_to(ROOT)),
                "sha256": sha256(page_path),
                "width": fitz.Pixmap(page_path).width,
                "height": fitz.Pixmap(page_path).height,
            })
            raw_pages.append({
                "page": page_index + 1,
                "width": page.rect.width,
                "height": page.rect.height,
                "lines": positioned_lines(page),
            })

        raw_path = raw_dir / f"2027_{month}_모의평가_1-17_좌표텍스트.json"
        raw_path.write_text(json.dumps(raw_pages, ensure_ascii=False, indent=2), encoding="utf-8")

        for visual in spec["visuals"]:
            page = document[visual["page"] - 1]
            out_path = visual_dir / visual["filename"]
            if visual["method"] == "embedded_image":
                payload = document.extract_image(visual["xref"])
                if payload["ext"].lower() != "png":
                    raise ValueError(f"unexpected embedded image type: {payload['ext']}")
                out_path.write_bytes(payload["image"])
                source_bbox = [
                    list(rect) for rect in page.get_image_rects(visual["xref"])
                ]
            else:
                clip = fitz.Rect(*visual["clip"])
                page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False).save(out_path)
                source_bbox = [visual["clip"]]
            pix = fitz.Pixmap(out_path)
            manifest["visuals"].append({
                **{key: value for key, value in visual.items() if key not in {"clip", "xref"}},
                "month": month,
                "source_page": visual["page"],
                "source_bbox": source_bbox,
                "path": str(out_path.relative_to(ROOT)),
                "sha256": sha256(out_path),
                "width": pix.width,
                "height": pix.height,
            })

        manifest["exams"].append({
            "month": month,
            "question_pdf": str(question_dst.relative_to(ROOT)),
            "question_pdf_sha256": sha256(question_dst),
            "answer_pdf": str(answer_dst.relative_to(ROOT)),
            "answer_pdf_sha256": sha256(answer_dst),
            "source_pages": page_records,
            "positioned_text": str(raw_path.relative_to(ROOT)),
        })

    manifest_path = BASE / "2027_6·9월_1-17_자산_원장.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"WROTE {manifest_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
