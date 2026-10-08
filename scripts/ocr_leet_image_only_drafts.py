#!/usr/bin/env python3
"""Create explicitly UNVERIFIED OCR drafts for image-only LEET PDFs.

OCR output is never written into the canonical ``텍스트`` directory.  Each
draft retains page/region boundaries and confidence diagnostics so that it can
be compared with the official page render before promotion.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path("자료/LEET_언어이해")
EXTRACTED = ROOT / "extracted_assets_manifest.json"
OUT_ROOT = ROOT / "OCR_초안"
TOOL_ROOT = Path(".tools/tesseract/root").resolve()
TESSDATA = Path(".tools/tesseract/tessdata_best").resolve()
TESSERACT = TOOL_ROOT / "usr/bin/tesseract"
TORCH_LIB = Path.home() / ".local/lib/python3.10/site-packages/torch/lib"


def existing_draft_is_complete(md_path: Path, json_path: Path, page_count: int,
                               question: bool) -> bool:
    """Reuse only a structurally complete draft made by the corrected parser."""
    if not md_path.exists() or not json_path.exists():
        return False
    try:
        text = md_path.read_text(encoding="utf-8")
        diagnostics = json.loads(json_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return False
    expected_regions = page_count * (3 if question else 1)
    if len(diagnostics) != expected_regions:
        return False
    if len(re.findall(r"(?m)^## page \d+$", text)) != page_count:
        return False
    if len(re.findall(r"(?m)^### (?:header|left|right|full)$", text)) != expected_regions:
        return False
    # A previous parser accidentally leaked raw TSV rows into Markdown.
    if "\t" in text or "검증 전 OCR 초안" not in text:
        return False
    return True


def run_ocr(image: Image.Image, psm: int = 6) -> tuple[str, list[dict]]:
    with tempfile.TemporaryDirectory(prefix="leet-ocr-") as tmp:
        tmp_path = Path(tmp)
        image_path = tmp_path / "input.png"
        output_base = tmp_path / "out"
        image.save(image_path, dpi=(150, 150))
        env = os.environ.copy()
        env["LD_LIBRARY_PATH"] = f"{TOOL_ROOT / 'usr/lib/x86_64-linux-gnu'}:{TORCH_LIB}"
        env["TESSDATA_PREFIX"] = str(TESSDATA)
        subprocess.run([
            str(TESSERACT), str(image_path), str(output_base),
            "-l", "kor+eng", "--psm", str(psm), "--dpi", "150", "tsv",
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, env=env)
        rows = []
        lines: dict[tuple[str, str, str, str], list[str]] = {}
        raw_lines = (output_base.with_suffix(".tsv")).read_text(encoding="utf-8").splitlines()
        header = raw_lines[0].split("\t")
        for raw_line in raw_lines[1:]:
            # Tesseract's TSV is not RFC CSV: recognized quote characters are
            # literal cell data. Splitting on tabs avoids multiline corruption
            # when a token is a double quotation mark.
            values = raw_line.split("\t", len(header) - 1)
            if len(values) != len(header):
                continue
            row = dict(zip(header, values))
            try:
                token = (row.get("text") or "").strip()
                if not token:
                    continue
                try:
                    conf = float(row.get("conf", -1))
                except ValueError:
                    conf = -1
                rows.append({"text": token, "confidence": conf,
                             "left": int(row["left"]), "top": int(row["top"]),
                             "width": int(row["width"]), "height": int(row["height"])})
                key = (row["page_num"], row["block_num"], row["par_num"], row["line_num"])
                lines.setdefault(key, []).append(token)
            except (KeyError, ValueError):
                continue
        text = "\n".join(" ".join(tokens) for tokens in lines.values()).strip()
        return text, rows


def question_regions(image: Image.Image) -> list[tuple[str, Image.Image]]:
    w, h = image.size
    return [
        ("header", image.crop((int(w * .05), int(h * .04), int(w * .95), int(h * .22)))),
        ("left", image.crop((int(w * .065), int(h * .19), int(w * .495), int(h * .965)))),
        ("right", image.crop((int(w * .505), int(h * .19), int(w * .935), int(h * .965)))),
    ]


def main() -> None:
    if not TESSERACT.exists() or not (TESSDATA / "kor.traineddata").exists():
        raise SystemExit("local Tesseract/tessdata_best is missing")
    data = json.loads(EXTRACTED.read_text(encoding="utf-8"))
    targets = [r for r in data["records"] if r["page_render_count"] and
               (r["kind"].startswith("question") or r["kind"] == "answer")]
    manifest = []
    for rec in targets:
        base = f"{rec['label']}_{rec['kind']}"
        target_dir = OUT_ROOT / rec["label"]
        target_dir.mkdir(parents=True, exist_ok=True)
        md_path = target_dir / f"{base}.md"
        json_path = target_dir / f"{base}_diagnostics.json"
        question = rec["kind"].startswith("question")
        if existing_draft_is_complete(md_path, json_path, rec["page_render_count"], question):
            manifest.append({"label": rec["label"], "kind": rec["kind"],
                             "source_file": rec["source_file"], "draft_file": str(md_path),
                             "diagnostics_file": str(json_path), "status": "unverified_ocr",
                             "page_count": rec["page_render_count"], "reused": True})
            print(base, "reuse complete draft", flush=True)
            continue
        md_parts = [f"# {base} OCR 초안\n\n",
                    "> 검증 전 OCR 초안이다. 원문 페이지와 대조하기 전에는 정본·분석 데이터로 사용하지 않는다.\n"]
        diagnostics = []
        for page in rec["page_renders"]:
            page_no = page["page"]
            image = Image.open(page["file"]).convert("RGB")
            regions = question_regions(image) if question else [("full", image)]
            md_parts.append(f"\n\n## page {page_no}\n")
            for region_name, crop in regions:
                text, words = run_ocr(crop, 6)
                md_parts.append(f"\n### {region_name}\n\n{text}\n")
                good = [w["confidence"] for w in words if w["confidence"] >= 0]
                low = [w for w in words if 0 <= w["confidence"] < 80]
                diagnostics.append({
                    "page": page_no, "region": region_name, "word_count": len(words),
                    "mean_confidence": (sum(good) / len(good)) if good else None,
                    "low_confidence_count": len(low), "low_confidence_words": low,
                })
                print(base, "page", page_no, region_name, "words", len(words), "low", len(low), flush=True)
        md_path.write_text("".join(md_parts), encoding="utf-8")
        json_path.write_text(json.dumps(diagnostics, ensure_ascii=False, indent=2), encoding="utf-8")
        manifest.append({"label": rec["label"], "kind": rec["kind"],
                         "source_file": rec["source_file"], "draft_file": str(md_path),
                         "diagnostics_file": str(json_path), "status": "unverified_ocr",
                         "page_count": rec["page_render_count"]})
    (OUT_ROOT / "manifest.json").write_text(json.dumps({"records": manifest}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", OUT_ROOT / "manifest.json")


if __name__ == "__main__":
    main()
