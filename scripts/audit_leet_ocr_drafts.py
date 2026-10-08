#!/usr/bin/env python3
"""Structural audit for unverified LEET OCR drafts.

The report deliberately never promotes OCR text to canonical status. It only
detects incomplete output, raw TSV leakage, missing warnings, and mismatched
page/region diagnostics.
"""
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path("자료/LEET_언어이해")
OUT = ROOT / "OCR_초안"
REPORT_JSON = ROOT / "검증" / "OCR_초안_구조검증_v1.json"
REPORT_MD = ROOT / "검증" / "OCR_초안_구조검증_v1.md"


def main() -> None:
    source = json.loads((ROOT / "extracted_assets_manifest.json").read_text(encoding="utf-8"))
    expected = [r for r in source["records"] if r["page_render_count"]]
    manifest_path = OUT / "manifest.json"
    errors: list[str] = []
    records = []
    if not manifest_path.is_file():
        errors.append("OCR 초안 manifest.json 없음")
        manifest_records = {}
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest_records = {(r["label"], r["kind"]): r for r in manifest["records"]}

    for item in expected:
        key = (item["label"], item["kind"])
        rec = manifest_records.get(key)
        item_errors = []
        if rec is None:
            item_errors.append("manifest 기록 없음")
            md_path = OUT / item["label"] / f"{item['label']}_{item['kind']}.md"
            diag_path = md_path.with_name(md_path.stem + "_diagnostics.json")
        else:
            md_path = Path(rec["draft_file"])
            diag_path = Path(rec["diagnostics_file"])
            if rec.get("status") != "unverified_ocr":
                item_errors.append("상태가 unverified_ocr가 아님")
        if not md_path.is_file():
            item_errors.append("Markdown 없음")
            text = ""
        else:
            text = md_path.read_text(encoding="utf-8")
            if "검증 전 OCR 초안" not in text:
                item_errors.append("비정본 경고 없음")
            if "\t" in text:
                item_errors.append("탭/원시 TSV 혼입")
            if "\ufffd" in text:
                item_errors.append("유니코드 대체문자 포함")
        if not diag_path.is_file():
            item_errors.append("진단 JSON 없음")
            diagnostics = []
        else:
            diagnostics = json.loads(diag_path.read_text(encoding="utf-8"))
        question = item["kind"].startswith("question")
        region_count = 3 if question else 1
        expected_regions = item["page_render_count"] * region_count
        if len(diagnostics) != expected_regions:
            item_errors.append(f"진단 영역 수 {len(diagnostics)} != {expected_regions}")
        if len(re.findall(r"(?m)^## page \d+$", text)) != item["page_render_count"]:
            item_errors.append("페이지 표지 수 불일치")
        if len(re.findall(r"(?m)^### (?:header|left|right|full)$", text)) != expected_regions:
            item_errors.append("영역 표지 수 불일치")
        means = [d["mean_confidence"] for d in diagnostics if d.get("mean_confidence") is not None]
        low = sum(d.get("low_confidence_count", 0) for d in diagnostics)
        words = sum(d.get("word_count", 0) for d in diagnostics)
        records.append({
            "label": item["label"], "kind": item["kind"], "status": "STRUCTURE_PASS" if not item_errors else "FAIL",
            "errors": item_errors, "page_count": item["page_render_count"], "region_count": expected_regions,
            "word_count": words, "low_confidence_words": low,
            "mean_region_confidence": sum(means) / len(means) if means else None,
            "draft_file": str(md_path),
        })
        errors.extend(f"{item['label']} {item['kind']}: {x}" for x in item_errors)

    extra = sorted(set(manifest_records) - {(r["label"], r["kind"]) for r in expected})
    errors.extend(f"예상 밖 manifest 기록: {label} {kind}" for label, kind in extra)
    payload = {
        "status": "STRUCTURE_PASS" if not errors else "FAIL",
        "error_count": len(errors), "errors": errors, "records": records,
        "warning": "STRUCTURE_PASS는 OCR 철자 정확성을 뜻하지 않으며 모든 OCR 문장은 원문 페이지 수동 대조 전까지 비정본이다.",
    }
    REPORT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# LEET OCR 초안 구조 검증 v1\n\n",
        f"- 결과: **{payload['status']}**\n",
        f"- 구조 오류: {len(errors)}개\n\n",
        "> 이 검사는 파일 완결성과 원시 TSV 혼입만 검사한다. OCR 철자·문장·선지의 정확성을 인증하지 않는다.\n\n",
        "| 학년도 | 종류 | 판정 | 페이지 | 영역 | OCR 낱말 | 신뢰도 80 미만 |\n",
        "| --- | --- | --- | ---: | ---: | ---: | ---: |\n",
    ]
    for r in records:
        lines.append(f"| {r['label']} | {r['kind']} | `{r['status']}` | {r['page_count']} | {r['region_count']} | {r['word_count']} | {r['low_confidence_words']} |\n")
    lines.extend(["\n## 오류\n\n"])
    lines.extend([f"- {x}\n" for x in errors] or ["- 없음\n"])
    REPORT_MD.write_text("".join(lines), encoding="utf-8")
    print(payload["status"], "errors", len(errors))
    print(REPORT_JSON)
    print(REPORT_MD)
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
