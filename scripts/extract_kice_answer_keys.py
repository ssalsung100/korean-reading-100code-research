#!/usr/bin/env python3
"""Normalize downloaded KICE answer tables into question-number mappings."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path("자료/평가원_정답표")
manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
OVERRIDES = ROOT / "verified_scan_answer_overrides.json"
CIRCLED = "①②③④⑤"


def text_of(pdf: Path) -> str:
    doc = fitz.open(pdf)
    return "\n".join(page.get_text() for page in doc)


def parse_answers(text: str) -> dict[str, str]:
    # Tables repeat (question number, choice, point value). Requiring the
    # point value avoids matching years and ordinary prose.
    # Some older PDFs use full-width Arabic numerals for point values.
    text = text.translate(str.maketrans("０１２３４５６７８９", "0123456789"))
    pairs = re.findall(r"(?<!\d)(\d{1,2})\s*([①②③④⑤])\s*([123])(?=\s|$)", text)
    out: dict[str, str] = {}
    for q, a, _ in pairs:
        out.setdefault(q, a)
    return out


def variant(text: str, name: str = "") -> str | None:
    probe = f"{name}\n{text[:1200]}"
    m = re.search(r"\(\s*([AB])형\s*\)|[_ -]([AB])(?:형)?", probe, re.I)
    return (m.group(1) or m.group(2)).upper() if m else None


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


normalized: list[dict] = []
for entry in manifest["entries"]:
    base = ROOT / ("원본/수능" if entry["exam_type"] == "수능" else "원본/모의평가")
    source = base / entry["local_name"]
    if not source.exists():
        entry["status"] = "missing_download"
        continue
    entry["sha256"] = sha256(source)
    entry["bytes"] = source.stat().st_size
    pdfs: list[Path] = []
    if entry["container"] == "pdf":
        pdfs = [source]
    else:
        dest = ROOT / "추출" / ("수능" if entry["exam_type"] == "수능" else "모의평가") / source.stem
        if not dest.exists():
            import zipfile
            dest.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(source) as zf:
                zf.extractall(dest)
        pdfs = sorted(dest.rglob("*.pdf"))
    child_count = 0
    for pdf in pdfs:
        try:
            txt = text_of(pdf)
        except Exception:
            continue
        answers = parse_answers(txt)
        if len(answers) < 10 or not ("정답" in txt[:3000] or "문항 번호" in txt[:3000]):
            continue
        normalized.append({
            "exam_type": entry["exam_type"],
            "academic_year": entry["academic_year"],
            "month": entry.get("month"),
            "board_seq": entry["board_seq"],
            "file_seq": entry["file_seq"],
            "official_page": entry["official_page"],
            "source_download": entry["download_url"],
            "source_container": entry["container"],
            "source_file": str(source),
            "answer_pdf": str(pdf),
            "variant": variant(txt, pdf.name),
            "question_count": len(answers),
            "answers": {str(k): answers[k] for k in sorted(answers, key=lambda x: int(x))},
            "sha256": sha256(pdf),
        })
        child_count += 1
    if child_count:
        entry["status"] = "parsed"
    elif pdfs:
        # The oldest scans contain the answer table as an image; retaining an
        # explicit OCR status prevents them from being mistaken for missing
        # official data.
        entry["status"] = "ocr_required"
        entry["answer_pdf_candidates"] = [str(p) for p in pdfs]
    else:
        entry["status"] = "no_answer_table_found"
    entry["parsed_tables"] = child_count

# A small set of official answer sheets are image-only scans.  Their answer
# rows were transcribed only after rendering and visually checking the
# official PDF.  Keep those records separate from machine-parsed tables so
# provenance and verification method remain explicit.
if OVERRIDES.exists():
    override_records = json.loads(OVERRIDES.read_text(encoding="utf-8"))["records"]
    existing_keys = {
        (x["exam_type"], x["academic_year"], x.get("month"), x.get("variant"))
        for x in normalized
    }
    for record in override_records:
        digits = record["answers_digits"]
        if len(digits) != record["question_count"] or any(x not in "12345" for x in digits):
            raise ValueError(
                f"invalid verified scan transcription: "
                f"{record['academic_year']} {record['exam_type']} {record.get('month')}"
            )
        key = (
            record["exam_type"], record["academic_year"],
            record.get("month"), record.get("variant"),
        )
        if key in existing_keys:
            continue
        source_pdf = Path(record["source_pdf"])
        page_image = Path(record["page_image"])
        if not source_pdf.exists() or not page_image.exists():
            raise FileNotFoundError(f"verified scan source missing: {record}")
        if sha256(page_image) != record["page_image_sha256"]:
            raise ValueError(f"verified page image hash changed: {page_image}")
        table = {
            k: v for k, v in record.items()
            if k not in {"answers_digits"}
        }
        table["answers"] = {
            str(i): CIRCLED[int(digit) - 1]
            for i, digit in enumerate(digits, 1)
        }
        table["answer_pdf"] = str(source_pdf)
        table["sha256"] = sha256(source_pdf)
        normalized.append(table)
        existing_keys.add(key)

        for entry in manifest["entries"]:
            if (
                entry["exam_type"] == record["exam_type"]
                and entry["academic_year"] == record["academic_year"]
                and entry.get("month") == record.get("month")
            ):
                entry["status"] = "verified_visual"
                entry["parsed_tables"] = 1
                entry["verified_page_image"] = record["page_image"]
                entry["verified_page_image_sha256"] = record["page_image_sha256"]
                break

out = ROOT / "normalized_answer_keys.json"
for idx, table in enumerate(normalized, 1):
    table["table_id"] = f"KICE-{idx:03d}"
out.write_text(json.dumps({
    "source": "한국교육과정평가원 수능 홈페이지",
    "scope": manifest["scope"],
    "answer_symbol": "①~⑤",
    "table_count": len(normalized),
    "tables": normalized,
}, ensure_ascii=False, indent=2), encoding="utf-8")
(ROOT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"normalized tables: {len(normalized)}")
print("question counts:", sorted({x['question_count'] for x in normalized}))
statuses = sorted({e.get("status") for e in manifest["entries"]})
print("entry statuses:", {s: sum(e.get("status") == s for e in manifest["entries"]) for s in statuses})
