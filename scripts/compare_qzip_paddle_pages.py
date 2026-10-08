#!/usr/bin/env python3
"""Locate secondary QZip passage discrepancies on PaddleOCR official pages.

This creates a review queue only. PaddleOCR and QZip remain noncanonical; the
official page image linked in each record is the sole visual authority.
"""
from __future__ import annotations

import json
from pathlib import Path

from rapidfuzz import fuzz

from analyze_qzip_repeated_passages import diff_ops, lexical, passage_candidate


ROOT = Path("자료/LEET_언어이해")
QZIP = ROOT / "검증" / "외부대조_QZip"
PADDLE = ROOT / "OCR_초안_Paddle"
OUT_JSON = ROOT / "검증" / "QZip_Paddle_공식페이지_대조대기열_v1.json"
OUT_MD = ROOT / "검증" / "QZip_Paddle_공식페이지_대조대기열_v1.md"
REQUIRED_ENGINE = "korean_PP-OCRv4_official_pdf_3x_det2400_v2"


def paddle_pages(year: int) -> list[dict]:
    kind = "question" if year == 2027 else "question_odd"
    directory = PADDLE / str(year) / kind
    pages = []
    for path in sorted(directory.glob("page_*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("engine_version") != REQUIRED_ENGINE:
            continue
        text = "\n".join(line for region in data["regions"] for line in region["lines"])
        pages.append({
            "page": data["page"], "norm": lexical(text), "json": str(path),
            "official_page_image": data["official_page_image"],
            "official_page_sha256": data["official_page_sha256"],
        })
    return pages


def main() -> None:
    records = []
    for year in (2022, 2023):
        pages = paddle_pages(year)
        if not pages:
            continue
        windows = []
        for i, page in enumerate(pages):
            windows.append({"pages": [page], "norm": page["norm"]})
            if i + 1 < len(pages) and pages[i + 1]["page"] == page["page"] + 1:
                windows.append({"pages": [page, pages[i + 1]], "norm": page["norm"] + pages[i + 1]["norm"]})
        for start in range(1, 31, 3):
            candidates = []
            for number in range(start, start + 3):
                path = QZIP / str(year) / f"q{number:02d}.md"
                norm = lexical(passage_candidate(path))
                if len(norm) >= 500:
                    candidates.append({"question": number, "file": str(path), "norm": norm})
            if not candidates:
                records.append({"year": year, "range": f"{start}-{start+2}", "status": "no_qzip_text"})
                continue
            ranked = []
            for candidate in candidates:
                for window in windows:
                    alignment = fuzz.partial_ratio_alignment(candidate["norm"], window["norm"], score_cutoff=45)
                    if alignment:
                        ranked.append((alignment.score, candidate, window, alignment))
            if not ranked:
                records.append({"year": year, "range": f"{start}-{start+2}", "status": "no_alignment"})
                continue
            score, candidate, window, alignment = max(ranked, key=lambda x: x[0])
            official_span = window["norm"][alignment.dest_start:alignment.dest_end]
            differences = diff_ops(candidate["norm"], official_span)
            records.append({
                "year": year, "range": f"{start}-{start+2}", "status": "pending_official_visual_review",
                "best_secondary_question": candidate["question"], "secondary_file": candidate["file"],
                "paddle_score": score, "candidate_chars": len(candidate["norm"]),
                "official_pages": [p["page"] for p in window["pages"]],
                "official_page_images": [p["official_page_image"] for p in window["pages"]],
                "official_page_sha256": [p["official_page_sha256"] for p in window["pages"]],
                "paddle_json": [p["json"] for p in window["pages"]],
                "differences": differences,
            })
    payload = {
        "status": "review_queue_noncanonical", "records": records,
        "warning": "Every difference must be decided from the linked official page image; neither side is canonical."
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# QZip·PaddleOCR 공식 페이지 대조 대기열 v1\n\n",
        "> 두 비정본을 비교하여 사람이 볼 위치를 좁힌 목록이다. 최종 판정은 연결된 공식 페이지 이미지에서만 한다.\n\n",
        "| 연도 | 문항군 | 가장 가까운 외부본 | 공식 쪽 | 일치 점수 | 불일치 묶음 | 상태 |\n",
        "| --- | --- | ---: | --- | ---: | ---: | --- |\n",
    ]
    for r in records:
        if r["status"] != "pending_official_visual_review":
            lines.append(f"| {r['year']} | {r['range']} | - | - | - | - | `{r['status']}` |\n")
        else:
            pages = ",".join(map(str, r["official_pages"]))
            lines.append(f"| {r['year']} | {r['range']} | q{r['best_secondary_question']:02d} | p{pages} | {r['paddle_score']:.3f} | {len(r['differences'])} | `pending` |\n")
    lines.extend(["\n## 불일치 문맥\n\n"])
    for r in records:
        if r.get("status") != "pending_official_visual_review" or not r["differences"]:
            continue
        lines.append(f"### {r['year']} {r['range']} · 공식 페이지 {r['official_pages']}\n\n")
        for d in r["differences"]:
            lines.append(f"- 외부본 `{d['a_context']}` / OCR `{d['b_context']}`\n")
        lines.append("\n")
    OUT_MD.write_text("".join(lines), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    print("records", len(records))


if __name__ == "__main__":
    main()
