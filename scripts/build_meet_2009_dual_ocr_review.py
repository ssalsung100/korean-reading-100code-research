#!/usr/bin/env python3
"""Build a review queue for the noncanonical 2009 MEET dual-OCR drafts.

Neither OCR output is promoted to canonical text. The official 3x page
image is the authority; this script only prioritizes manual comparison.
"""

from __future__ import annotations

import difflib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TESS_DIR = ROOT / "자료/MEET_언어추론/OCR_초안/2009"
PADDLE_DIR = ROOT / "자료/MEET_언어추론/OCR_초안_Paddle/2009"
OUT_DIR = ROOT / "자료/MEET_언어추론/검증"

EXPECTED = {
    86: [], 87: [1, 2, 3, 4], 88: [5, 6, 7], 89: [8, 9, 10],
    90: [11, 12, 13], 91: [], 92: [14, 15, 16],
    93: [17, 18, 19], 94: [20, 21, 22], 95: [23],
    96: [24, 25], 97: [26, 27, 28], 98: [29, 30, 31],
    99: [32, 33, 34], 100: [35, 36, 37], 101: [38, 39, 40],
}

DIRECT_BOUNDARY_VERIFIED = {
    87: {
        3: "<보기> 안의 ‘예’로 추가하기에 가장 적절한 것은?",
    },
    88: {
        7: "위 글에 나타난 세 사람의 이론을 현대적 관점에서 평가했을 때 적절하지 않은 것은?",
    },
    89: {
        8: "워홀의 <브릴로 상자>에 대한 단토의 생각과 거리가 먼 것은?",
    },
    92: {
        15: "위 글을 연극으로 상연할 때, ㉠～㉤에 대한 연출가의 지시로 적절하지 않은 것은?",
    },
    93: {
        18: "(가)～(마)의 말하기 방식에 대한 설명으로 옳지 않은 것은?",
    },
    94: {
        20: "위 글의 내용과 일치하는 것은?",
    },
    96: {
        25: "㉠에 근거하여 ‘과장’이 ‘젊은 축들’에게 할 수 있는 비판과 시적 의미가 가장 가까운 것은?",
    },
    97: {
        28: "의사인 김 박사에게 55세 여성 박 여사가 폐경 후 호르몬 대체 요법을 받기 위해 찾아왔다. ‘여성건강연구’의 결론으로 미루어 볼 때, 김 박사의 상담 내용 중 적절한 것만을 <보기>에서 고른 것은?",
    },
}


def compact(text: str) -> str:
    text = re.sub(r"^#.*$", "", text, flags=re.M)
    text = re.sub(r"^>.*$", "", text, flags=re.M)
    text = re.sub(r"^##\s+\w+\s*$", "", text, flags=re.M)
    return re.sub(r"[^0-9A-Za-z가-힣]", "", text)


def question_hits(text: str, expected: list[int]) -> list[int]:
    """Conservative detector: only report expected numbers seen at line starts."""
    found = []
    for number in expected:
        if re.search(rf"(?m)^\s*{number}\s*(?:[.]|\s)", text):
            found.append(number)
    return found


def region_confidences(data: dict) -> list[float]:
    result = []
    for region in data.get("regions", []):
        if region.get("name") == "header":
            continue
        value = region.get("mean_confidence")
        if value is None:
            continue
        value = float(value)
        if value <= 1:
            value *= 100
        result.append(value)
    return result


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []

    for page, expected in EXPECTED.items():
        name = f"official_page_{page:03}"
        t_md_path = TESS_DIR / f"{name}.md"
        p_md_path = PADDLE_DIR / f"{name}.md"
        t_json_path = TESS_DIR / f"{name}.json"
        p_json_path = PADDLE_DIR / f"{name}.json"

        t_text = t_md_path.read_text(encoding="utf-8")
        p_text = p_md_path.read_text(encoding="utf-8")
        t_data = json.loads(t_json_path.read_text(encoding="utf-8"))
        p_data = json.loads(p_json_path.read_text(encoding="utf-8"))

        t_compact = compact(t_text)
        p_compact = compact(p_text)
        ratio = difflib.SequenceMatcher(None, t_compact, p_compact, autojunk=False).ratio()
        t_found = question_hits(t_text, expected)
        p_found = question_hits(p_text, expected)
        t_conf = region_confidences(t_data)
        p_conf = region_confidences(p_data)
        missing_both = sorted(set(expected) - set(t_found) - set(p_found))
        verified_stems = DIRECT_BOUNDARY_VERIFIED.get(page, {})
        unresolved_missing = sorted(set(missing_both) - set(verified_stems))
        unresolved_detection_disagreement = sorted(
            (set(t_found) ^ set(p_found)) - set(verified_stems)
        )

        if unresolved_missing or ratio < 0.55:
            priority = "high"
        elif unresolved_detection_disagreement or ratio < 0.72:
            priority = "medium"
        else:
            priority = "normal"

        rows.append({
            "exam_family": "MEET",
            "year": 2009,
            "official_pdf_page": page,
            "expected_question_numbers": expected,
            "tesseract_detected_question_numbers": t_found,
            "paddle_detected_question_numbers": p_found,
            "question_numbers_missing_in_both": missing_both,
            "question_numbers_resolved_by_direct_page_review": sorted(verified_stems),
            "directly_verified_stems": {str(key): value for key, value in verified_stems.items()},
            "unresolved_question_numbers": unresolved_missing,
            "unresolved_detection_disagreement": unresolved_detection_disagreement,
            "normalized_text_similarity": round(ratio, 4),
            "tesseract_mean_region_confidence_percent": round(sum(t_conf) / len(t_conf), 2) if t_conf else None,
            "paddle_mean_region_confidence_percent": round(sum(p_conf) / len(p_conf), 2) if p_conf else None,
            "review_priority": priority,
            "authority": f"자료/MEET_언어추론/페이지/2009/{name}_3x.png",
            "tesseract_draft": str(t_md_path.relative_to(ROOT)),
            "paddle_draft": str(p_md_path.relative_to(ROOT)),
            "status": "direct_official_page_comparison_required",
            "promotion_rule": "Neither OCR wording may be promoted without direct visual comparison.",
        })

    json_path = OUT_DIR / "MEET_2009_이중OCR_검토큐_v1.json"
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    priority_counts = {key: sum(row["review_priority"] == key for row in rows) for key in ("high", "medium", "normal")}
    missing_pages = [row for row in rows if row["question_numbers_missing_in_both"]]
    unresolved_pages = [row for row in rows if row["unresolved_question_numbers"]]

    lines = [
        "# 2009 MEET 언어추론 이중 OCR 검토 큐 v1",
        "",
        "- 상태: **비정본 OCR 비교 완료 — 공식 페이지 직접 대조 필요**",
        "- 기준 원본: 3배율 공식 페이지 PNG 16쪽",
        "- 독립 초안: Tesseract 4 kor+eng best / Korean PP-OCRv4",
        f"- 우선순위: high {priority_counts['high']}쪽, medium {priority_counts['medium']}쪽, normal {priority_counts['normal']}쪽",
        f"- 양쪽 OCR에서 문항 번호가 모두 누락된 페이지: {len(missing_pages)}쪽",
        f"- 공식 페이지 직접 판독으로 번호·발문을 복원한 페이지: {len(DIRECT_BOUNDARY_VERIFIED)}쪽",
        f"- 미해결 문항 번호가 남은 페이지: {len(unresolved_pages)}쪽",
        "",
        "> 유사도와 신뢰도는 검토 순서를 정하기 위한 보조값이다. 높은 값도 원문 정확성을 보증하지 않으며, 공식 페이지를 보지 않은 자동 합성문은 정본으로 인정하지 않는다.",
        "",
        "## 페이지별 큐",
        "",
        "| 공식 쪽 | 예상 문항 | T 감지 | P 감지 | 양쪽 누락 | 직접 복원 | 미해결 | 정규화 유사도 | 우선 |",
        "|---:|---|---|---|---|---|---|---:|---|",
    ]
    for row in rows:
        fmt = lambda values: ", ".join(map(str, values)) if values else "—"
        lines.append(
            f"| {row['official_pdf_page']} | {fmt(row['expected_question_numbers'])} | "
            f"{fmt(row['tesseract_detected_question_numbers'])} | "
            f"{fmt(row['paddle_detected_question_numbers'])} | "
            f"{fmt(row['question_numbers_missing_in_both'])} | "
            f"{fmt(row['question_numbers_resolved_by_direct_page_review'])} | "
            f"{fmt(row['unresolved_question_numbers'])} | "
            f"{row['normalized_text_similarity']:.4f} | "
            f"{row['review_priority']} |"
        )

    lines += [
        "",
        "## 직접 대조 순서",
        "",
        "1. 양쪽에서 문항 번호가 누락된 쪽을 먼저 열어 발문과 번호를 확정한다.",
        "2. 지문은 문단 경계, 고유명사, 한자·영문, 부정 표현, 수치와 단위를 우선 대조한다.",
        "3. 선지는 ①~⑤의 시작·끝과 부정어, 비교항, 지시 대상을 한 줄씩 대조한다.",
        "4. 표·그림·보기는 OCR에 의존하지 않고 페이지 좌표와 별도 원본 이미지를 연결한다.",
        "5. 공식 정답 40개를 문항에 연결한 뒤 블라인드 재풀이로 정답 유일성을 확인한다.",
        "",
        "## 이번 직접 판독에서 확정한 발문",
        "",
    ]
    for page, stems in sorted(DIRECT_BOUNDARY_VERIFIED.items()):
        for question, stem in sorted(stems.items()):
            lines.append(f"- 공식 {page}쪽 {question}번: {stem}")
    lines += [
        "",
        f"> 위 {sum(len(stems) for stems in DIRECT_BOUNDARY_VERIFIED.values())}건은 문항 번호와 발문만 직접 확정한 것이다. 해당 쪽의 지문·선지 전체가 정본으로 승격된 것은 아니다.",
        "",
        "## 알려진 자동 감지 한계",
        "",
        "- PaddleOCR은 '5. 위 글'을 '5위 글'처럼 붙여 읽는 경우가 있다.",
        "- Tesseract는 글자 사이에 과도한 공백을 넣고 원문자 선지 기호를 손상시키는 경우가 있다.",
        "- 문항이 오른쪽 단에서 시작하면 단순 행 시작 정규식이 번호를 놓칠 수 있다.",
        "- 표와 그림 속 글자는 본문 읽기 순서와 분리하여 검수해야 한다.",
        "",
        "## 산출물",
        "",
        f"- {json_path.relative_to(ROOT)}",
        "- 자료/MEET_언어추론/검증/2009_공식페이지_접촉판.png",
        "- 자료/MEET_언어추론/OCR_초안/2009/",
        "- 자료/MEET_언어추론/OCR_초안_Paddle/2009/",
    ]
    md_path = OUT_DIR / "MEET_2009_이중OCR_검토큐_v1.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "pages": len(rows),
        "priority_counts": priority_counts,
        "missing_both_pages": len(missing_pages),
        "direct_boundary_verified_pages": len(DIRECT_BOUNDARY_VERIFIED),
        "unresolved_missing_pages": len(unresolved_pages),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
