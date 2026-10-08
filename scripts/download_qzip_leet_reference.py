#!/usr/bin/env python3
"""Download QZip text only as a secondary LEET transcription reference.

This material is never treated as the official/canonical source. It is useful
for locating OCR discrepancies in image-only 2022/2023 PDFs, and 2024 (which
has an official text layer) is collected as a calibration year.
"""
from __future__ import annotations

import hashlib
import json
import time
import urllib.parse
import argparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path("자료/LEET_언어이해/검증/외부대조_QZip")
SUBJECT = urllib.parse.quote("언어이해")
BASE = f"https://www.qzip.io/solutions/leet/{SUBJECT}"


def extract_question(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    for script in soup.find_all("script"):
        value = script.string or ""
        if "@context" not in value or "QAPage" not in value:
            continue
        prefix = "self.__next_f.push("
        if not value.startswith(prefix) or not value.endswith(")"):
            continue
        try:
            outer = json.loads(value[len(prefix):-1])
            if not isinstance(outer, list) or len(outer) < 2 or not isinstance(outer[1], str):
                continue
            obj = json.loads(outer[1])
            entity = obj["mainEntity"]
            if not isinstance(entity, dict) or "name" not in entity:
                continue
        except (json.JSONDecodeError, KeyError, TypeError):
            continue
        return {"name": entity["name"], "text": entity.get("text", "")}
    raise ValueError("QAPage JSON-LD not found")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--years", nargs="+", type=int, default=[2022, 2023, 2024])
    args = parser.parse_args()
    ROOT.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (LEET source verification; non-canonical reference)"
    manifest_path = ROOT / "manifest.json"
    existing = []
    failures = []
    if manifest_path.is_file():
        prior_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        existing = prior_manifest.get("records", [])
        failures = prior_manifest.get("failures", [])
    failures_by_key = {(failure["year"], failure["question"]): failure for failure in failures}
    records_by_key = {(record["year"], record["question"]): record for record in existing}
    for year in args.years:
        year_dir = ROOT / str(year)
        year_dir.mkdir(parents=True, exist_ok=True)
        for number in range(1, 31):
            url = f"{BASE}/{year}/{number}"
            response = session.get(url, timeout=30)
            response.raise_for_status()
            try:
                parsed = extract_question(response.text)
            except ValueError as exc:
                failures_by_key[(year, number)] = {
                    "year": year,
                    "question": number,
                    "url": url,
                    "reason": str(exc),
                    "html_sha256": hashlib.sha256(response.content).hexdigest(),
                }
                print(year, number, "no_qapage_text", flush=True)
                continue
            target = year_dir / f"q{number:02d}.md"
            target.write_text(
                f"# {parsed['name']}\n\n> QZip의 2차 전사 자료이며 공식 정본이 아니다. 원문 대조용으로만 사용한다.\n\n"
                + parsed["text"].strip() + "\n", encoding="utf-8"
            )
            records_by_key[(year, number)] = {
                "year": year, "question": number, "url": url,
                "file": str(target), "html_sha256": hashlib.sha256(response.content).hexdigest(),
                "text_sha256": hashlib.sha256(parsed["text"].encode()).hexdigest(),
                "text_chars": len(parsed["text"]),
            }
            failures_by_key.pop((year, number), None)
            print(year, number, len(parsed["text"]), flush=True)
            time.sleep(0.05)
    records = [records_by_key[key] for key in sorted(records_by_key)]
    failures = [failures_by_key[key] for key in sorted(failures_by_key)]
    manifest_path.write_text(json.dumps({
        "status": "secondary_noncanonical_reference", "records": records,
        "failures": failures,
    }, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
