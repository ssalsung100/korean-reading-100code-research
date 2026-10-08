#!/usr/bin/env python3
"""Build a source-linked manual verification queue without inferring text."""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("자료/LEET_언어이해")
OUT_JSON = ROOT / "검증" / "수동대조_작업대기열_v1.json"
OUT_MD = ROOT / "검증" / "수동대조_작업대기열_v1.md"


def main() -> None:
    assets = json.loads((ROOT / "extracted_assets_manifest.json").read_text(encoding="utf-8"))["records"]
    ocr_manifest_path = ROOT / "OCR_초안" / "manifest.json"
    ocr_records = {}
    if ocr_manifest_path.exists():
        data = json.loads(ocr_manifest_path.read_text(encoding="utf-8"))
        ocr_records = {(r["label"], r["kind"]): r for r in data["records"]}
    items = []
    for rec in assets:
        if not rec["kind"].startswith("question"):
            continue
        if rec["method"] == "hwp5txt_direct":
            items.append({
                "id": f"HWP-{rec['label']}-{rec['kind']}", "class": "hwp_layout",
                "label": rec["label"], "kind": rec["kind"], "source_file": rec["source_file"],
                "canonical_text": rec["text_file"], "figure_count": rec["figure_count"],
                "table_count": rec["table_count"], "status": "pending_official_visual_comparison",
                "verified_by": None, "verified_at": None, "notes": None,
            })
        elif rec["page_render_count"]:
            ocr = ocr_records.get((rec["label"], rec["kind"]))
            diagnostics_by_page = {}
            if ocr and Path(ocr["diagnostics_file"]).is_file():
                diagnostics = json.loads(Path(ocr["diagnostics_file"]).read_text(encoding="utf-8"))
                for d in diagnostics:
                    diagnostics_by_page.setdefault(d["page"], []).append(d)
            for page in rec["page_renders"]:
                ds = diagnostics_by_page.get(page["page"], [])
                items.append({
                    "id": f"IMG-{rec['label']}-{rec['kind']}-p{page['page']:03d}",
                    "class": "image_text", "label": rec["label"], "kind": rec["kind"],
                    "page": page["page"], "source_file": rec["source_file"],
                    "official_page_image": page["file"], "official_page_sha256": page.get("sha256"),
                    "ocr_draft": ocr["draft_file"] if ocr else None,
                    "ocr_word_count": sum(d.get("word_count", 0) for d in ds),
                    "ocr_low_confidence_words": sum(d.get("low_confidence_count", 0) for d in ds),
                    "status": "pending_official_visual_comparison",
                    "verified_by": None, "verified_at": None, "notes": None,
                })
    payload = {
        "item_count": len(items),
        "hwp_layout_items": sum(i["class"] == "hwp_layout" for i in items),
        "image_page_items": sum(i["class"] == "image_text" for i in items),
        "policy": "Only official-source visual comparison may change an item to verified. OCR or secondary-site agreement alone is insufficient.",
        "items": items,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# LEET 수동 대조 작업 대기열 v1\n\n",
        f"- 전체: {len(items)}개\n",
        f"- HWP 레이아웃 단위: {payload['hwp_layout_items']}개\n",
        f"- 이미지형 PDF 페이지 단위: {payload['image_page_items']}개\n\n",
        "OCR이나 외부 사이트끼리 일치했다는 이유만으로 완료 처리하지 않는다. 공식 HWP 또는 공식 페이지 이미지를 직접 대조한 경우에만 `verified`로 변경한다.\n\n",
        "| ID | 범위 | 상태 | 원본 대조 대상 |\n",
        "| --- | --- | --- | --- |\n",
    ]
    for item in items:
        if item["class"] == "hwp_layout":
            scope = f"그림 {item['figure_count']} / 표 {item['table_count']}"
            source = item["source_file"]
        else:
            scope = f"page {item['page']} / 저신뢰 OCR {item['ocr_low_confidence_words']}"
            source = item["official_page_image"]
        lines.append(f"| `{item['id']}` | {scope} | `pending` | `{source}` |\n")
    OUT_MD.write_text("".join(lines), encoding="utf-8")
    print(payload["item_count"], payload["hwp_layout_items"], payload["image_page_items"])
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
