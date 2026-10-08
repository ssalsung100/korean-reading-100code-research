#!/usr/bin/env python3
"""Build a noncanonical 2027 LEET dual-OCR manual review queue.

Tesseract and PaddleOCR are used only to rank official pages for visual
review. Agreement is not treated as proof, and neither OCR is promoted.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from rapidfuzz import fuzz


ROOT = Path("자료/LEET_언어이해")
TESSERACT_MD = ROOT / "OCR_초안" / "2027" / "2027_question.md"
PADDLE_DIR = ROOT / "OCR_초안_Paddle" / "2027" / "question"
OUT_JSON = ROOT / "검증" / "2027_이중OCR_공식페이지_수동대조대기열_v1.json"
OUT_MD = ROOT / "검증" / "2027_이중OCR_공식페이지_수동대조대기열_v1.md"
REQUIRED_ENGINE = "korean_PP-OCRv4_official_pdf_3x_det2400_v2"


def lexical(text: str) -> str:
    return re.sub(r"[^0-9A-Za-z가-힣]", "", text)


def tesseract_pages() -> dict[int, str]:
    text = TESSERACT_MD.read_text(encoding="utf-8")
    chunks = re.split(r"(?m)^## page (\d+)\s*$", text)
    return {int(chunks[i]): chunks[i + 1] for i in range(1, len(chunks), 2)}


def main() -> None:
    tess = tesseract_pages()
    errors: list[str] = []
    records: list[dict] = []

    for page in range(1, 16):
        path = PADDLE_DIR / f"page_{page:03d}.json"
        if not path.is_file():
            errors.append(f"PaddleOCR {page}쪽 없음")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("engine_version") != REQUIRED_ENGINE:
            errors.append(f"PaddleOCR {page}쪽 엔진 버전 불일치")
        if page not in tess:
            errors.append(f"Tesseract {page}쪽 없음")
            tess_text = ""
        else:
            tess_text = tess[page]

        paddle_text = "\n".join(
            line for region in data.get("regions", []) for line in region.get("lines", [])
        )
        paddle_norm = lexical(paddle_text)
        tess_norm = lexical(tess_text)
        tokens = [
            {
                "region": region.get("name"),
                "text": token.get("text", ""),
                "confidence": token.get("confidence"),
                "left": token.get("left"),
                "top": token.get("top"),
                "right": token.get("right"),
                "bottom": token.get("bottom"),
            }
            for region in data.get("regions", [])
            for token in region.get("tokens", [])
            if token.get("confidence") is not None
        ]
        low_tokens = sorted(tokens, key=lambda token: token["confidence"])[:25]
        below_95 = sum(token["confidence"] < 0.95 for token in tokens)
        below_98 = sum(token["confidence"] < 0.98 for token in tokens)
        mean_conf = sum(token["confidence"] for token in tokens) / len(tokens) if tokens else None
        similarity = fuzz.ratio(paddle_norm, tess_norm) if paddle_norm and tess_norm else 0.0
        priority_score = below_95 * 4 + below_98 + max(0.0, 80.0 - similarity)
        records.append({
            "page": page,
            "status": "pending_official_visual_review",
            "official_page_image": data.get("official_page_image"),
            "official_page_sha256": data.get("official_page_sha256"),
            "paddle_json": str(path),
            "tesseract_draft": str(TESSERACT_MD),
            "paddle_chars": len(paddle_norm),
            "tesseract_chars": len(tess_norm),
            "lexical_similarity": similarity,
            "paddle_token_count": len(tokens),
            "paddle_mean_confidence": mean_conf,
            "paddle_below_0_95": below_95,
            "paddle_below_0_98": below_98,
            "priority_score": priority_score,
            "lowest_confidence_tokens": low_tokens,
        })

    ranked = sorted(records, key=lambda record: record["priority_score"], reverse=True)
    for rank, record in enumerate(ranked, 1):
        record["review_rank"] = rank

    payload = {
        "status": "review_queue_noncanonical" if not errors else "FAIL",
        "error_count": len(errors),
        "errors": errors,
        "records": sorted(records, key=lambda record: record["page"]),
        "warning": "두 OCR의 일치도는 원문 인증이 아니다. 모든 문자는 연결된 공식 페이지 이미지에서만 최종 판정한다.",
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# 2027 LEET 이중 OCR 공식 페이지 수동 대조 대기열 v1\n\n",
        "> Tesseract와 PaddleOCR은 검토 순위를 정하는 데만 사용한다. 두 결과가 일치해도 공식 원문으로 확정하지 않는다.\n\n",
        "| 순위 | 쪽 | OCR 문자열 일치도 | Paddle 평균 신뢰도 | 0.95 미만 | 0.98 미만 | 상태 |\n",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |\n",
    ]
    for record in ranked:
        lines.append(
            f"| {record['review_rank']} | {record['page']} | {record['lexical_similarity']:.3f} | "
            f"{record['paddle_mean_confidence']:.5f} | {record['paddle_below_0_95']} | "
            f"{record['paddle_below_0_98']} | `pending` |\n"
        )
    lines.append("\n## 페이지별 Paddle 저신뢰 후보\n\n")
    for record in ranked:
        lines.append(f"### 검토 {record['review_rank']}순위 · {record['page']}쪽\n\n")
        lines.append(f"- 공식 페이지: `{record['official_page_image']}`\n")
        lines.append(f"- 공식 페이지 SHA-256: `{record['official_page_sha256']}`\n")
        lines.append("- 최저 신뢰도 토큰(판정 전 후보):\n")
        for token in record["lowest_confidence_tokens"]:
            lines.append(
                f"  - `{token['text']}` · {token['confidence']:.5f} · {token['region']} "
                f"({token['left']:.0f}, {token['top']:.0f})–({token['right']:.0f}, {token['bottom']:.0f})\n"
            )
        lines.append("\n")
    if errors:
        lines.append("## 구조 오류\n\n")
        lines.extend(f"- {error}\n" for error in errors)
    OUT_MD.write_text("".join(lines), encoding="utf-8")
    print(payload["status"], "errors", len(errors), "pages", len(records))
    print(OUT_JSON)
    print(OUT_MD)
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
