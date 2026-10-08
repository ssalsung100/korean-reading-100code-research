#!/usr/bin/env python3
"""Normalize official LEET language-understanding answer keys.

The original HWP/PDF files remain authoritative. This script creates a
machine-readable index. Image-only answer PDFs are never guessed by OCR;
their separately recorded official-page visual transcriptions are applied
only after strict length and choice-range validation.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

from bs4 import BeautifulSoup

try:
    import fitz  # PyMuPDF
except ImportError:  # pragma: no cover
    fitz = None

ROOT = Path("자료/LEET_언어이해")
MANIFEST = ROOT / "manifest.json"
OUT = ROOT / "normalized_answers.json"
VERIFIED_OVERRIDES = ROOT / "검증" / "verified_image_answer_overrides.json"
CIRCLED = "①②③④⑤"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def variant_from_text(text: str) -> str | None:
    compact = re.sub(r"\s+", "", text)
    if "홀수형" in compact or "[홀]수형" in compact or "(홀)" in compact:
        return "odd"
    if "짝수형" in compact or "[짝]수형" in compact or "(짝)" in compact:
        return "even"
    return None


def parse_hwp(path: Path) -> list[dict]:
    with tempfile.NamedTemporaryFile(suffix=".html") as tmp:
        subprocess.run(
            ["hwp5html", "--html", "--output", tmp.name, str(path)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
        soup = BeautifulSoup(Path(tmp.name).read_text(encoding="utf-8"), "html.parser")

    tables = soup.find_all("table")
    results: list[dict] = []
    for table in tables:
        variant = variant_from_text(table.get_text(" ", strip=True))
        pairs: dict[int, str] = {}
        for row in table.find_all("tr"):
            cells = [" ".join(c.stripped_strings).strip() for c in row.find_all(["td", "th"])]
            for i in range(len(cells) - 1):
                # Do not use str.isdigit(): circled numerals satisfy Unicode
                # numeric predicates on some Python builds.
                if re.fullmatch(r"\d{1,2}", cells[i]) and cells[i + 1] in CIRCLED:
                    pairs[int(cells[i])] = cells[i + 1]
        if pairs:
            results.append({
                "variant": variant,
                "answers": {str(k): v for k, v in sorted(pairs.items())},
                "question_count": len(pairs),
                "status": "parsed",
                "method": "hwp5html_table",
            })
    if not results:
        return [{"variant": None, "answers": {}, "question_count": 0,
                 "status": "parse_failed", "method": "hwp5html_table"}]
    # A few legacy files use no variant heading. Preserve table order while
    # assigning stable labels only when there are exactly two tables.
    if len(results) == 2 and all(r["variant"] is None for r in results):
        results[0]["variant"], results[1]["variant"] = "odd", "even"
    return results


def parse_pdf(path: Path) -> list[dict]:
    if fitz is None:
        return [{"variant": None, "answers": {}, "question_count": 0,
                 "status": "ocr_required", "method": "pymupdf_unavailable"}]
    doc = fitz.open(path)
    text = "\n".join(page.get_text() for page in doc)
    if not re.search(r"\d\s*[①②③④⑤]", text):
        return [{"variant": None, "answers": {}, "question_count": 0,
                 "status": "ocr_required", "method": "pdf_text_empty"}]
    results: list[dict] = []
    current: str | None = None
    buckets: dict[str | None, dict[int, str]] = {}
    # Text extraction places each table cell on its own line. This pattern
    # deliberately accepts whitespace/newlines but never pairs two answers.
    for m in re.finditer(r"(?<!\d)(\d{1,2})\s*([①②③④⑤])", text):
        number, answer = int(m.group(1)), m.group(2)
        heading = text.rfind("홀수형", 0, m.start())
        heading_even = text.rfind("짝수형", 0, m.start())
        if heading_even > heading:
            current = "even"
        elif heading >= 0:
            current = "odd"
        buckets.setdefault(current, {})[number] = answer
    for variant, pairs in buckets.items():
        if pairs:
            results.append({"variant": variant, "answers": {str(k): v for k, v in sorted(pairs.items())},
                            "question_count": len(pairs), "status": "parsed", "method": "pymupdf_text"})
    return results or [{"variant": None, "answers": {}, "question_count": 0,
                        "status": "ocr_required", "method": "pdf_unparsed"}]


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records: list[dict] = []
    for entry in manifest["entries"]:
        if entry["kind"] != "answer":
            continue
        path = Path(entry["file"])
        try:
            parsed = parse_hwp(path) if path.suffix.lower() == ".hwp" else parse_pdf(path)
        except Exception as exc:  # preserve source even if a converter fails
            parsed = [{"variant": None, "answers": {}, "question_count": 0,
                       "status": "parse_failed", "method": type(exc).__name__,
                       "error": str(exc)}]
        for item in parsed:
            records.append({
                "year": entry["year"], "label": entry["label"],
                "variant": item["variant"], "question_count": item["question_count"],
                "answers": item["answers"], "status": item["status"],
                "method": item["method"], "source_file": entry["file"],
                "board_page": entry["board_page"], "source_url": entry["source_url"],
                "sha256": entry["sha256"],
                **({"error": item["error"]} if "error" in item else {}),
            })
    if VERIFIED_OVERRIDES.exists():
        override_data = json.loads(VERIFIED_OVERRIDES.read_text(encoding="utf-8"))
        labels = {o["label"] for o in override_data["records"]}
        source_by_label = {r["label"]: r for r in records if r["label"] in labels}
        records = [r for r in records if r["label"] not in labels]
        for override in override_data["records"]:
            base = source_by_label[override["label"]]
            values = override["answers"]
            if len(values) != 30 or any(v not in range(1, 6) for v in values):
                raise ValueError(f"invalid verified answer override: {override['label']} {override['variant']}")
            records.append({
                **{k: base[k] for k in ["year", "label", "source_file", "board_page", "source_url", "sha256"]},
                "variant": override["variant"], "question_count": len(values),
                "answers": {str(i): CIRCLED[v - 1] for i, v in enumerate(values, 1)},
                "status": "verified_visual", "method": "official_page_visual_transcription",
                "verification_page": override["source_page"],
            })
    records.sort(key=lambda r: (r["year"], r["label"], r["variant"] or "single"))
    payload = {
        "source_manifest": "manifest.json",
        "answer_source_count": len([e for e in manifest["entries"] if e["kind"] == "answer"]),
        "normalized_table_count": len(records),
        "records": records,
        "status_note": (
            "parsed means direct HWP/PDF text-table extraction; verified_visual means manual "
            "transcription from the rendered official answer page. OCR guesses are not used."
        ),
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    from collections import Counter
    print("records", len(records), "status", dict(Counter(r["status"] for r in records)))
    for r in records:
        print(r["label"], r["variant"], r["status"], r["question_count"])


if __name__ == "__main__":
    main()
