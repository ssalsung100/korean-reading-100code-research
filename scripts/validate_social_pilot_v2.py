#!/usr/bin/env python3
"""통합사회 고난도 파일럿 v2의 노출면과 설계면을 분리해 검수한다."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "파일럿" / "통합사회_평가원형_고난도_파일럿_v2_경제.md"
OUT_JSON = ROOT / "분석" / "통합사회_고난도_파일럿_v2_경제_검수.json"
OUT_MD = ROOT / "분석" / "통합사회_고난도_파일럿_v2_경제_검수.md"


def between(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0].strip()


text = SOURCE.read_text(encoding="utf-8")
passage = between(text, "## 1. 지문", "## 2. 문항")
questions = between(text, "## 2. 문항", "## 3. 정답 및 근거")
surface = f"{passage}\n{questions}"

question_blocks = re.split(r"(?m)^### (?=\d+\.)", questions)[1:]
choice_counts = [len(re.findall(r"(?m)^[①②③④⑤]", block)) for block in question_blocks]
paragraphs = [p for p in re.split(r"\n\s*\n", passage) if p.strip()]
nonspace_length = len(re.sub(r"\s+", "", passage))

absolute_terms = ["반드시", "언제나", "전혀", "자동으로", "무조건", "모든 경우"]
meta_terms = [
    "필요조건", "충분조건", "필요충분조건", "독립변수", "이항대립",
    "부분/전체", "부분과 전체", "비례·반비례", "함수 코드", "조건문 코드",
]
# 직접 회수형은 단어 하나가 아니라 발문의 기능으로 판정한다. 두 문단의 결합을
# 명시한 문항은 '설명'이라는 말이 있어도 직접 회수형으로 세지 않는다.
direct_stem_patterns = [
    r"윗글의 내용과 일치(?:하지 않)?는",
    r"윗글에 대한 설명으로 적절(?:하지 않)?은",
]

absolute_hits = {term: surface.count(term) for term in absolute_terms if term in surface}
meta_hits = {term: surface.count(term) for term in meta_terms if term in surface}
direct_hits = {
    pattern: len(re.findall(pattern, questions))
    for pattern in direct_stem_patterns
    if re.search(pattern, questions)
}

endings = re.findall(r"(?m)^[①②③④⑤].*?(하겠군\.|한다\.|된다\.|있다\.|없다\.|않는다\.|크다\.|작다\.|같다\.|낮다\.|높다\.)$", questions)

checks = {
    "passage_length_1050_1250": 1050 <= nonspace_length <= 1250,
    "five_paragraphs": len(paragraphs) == 5,
    "four_questions": len(question_blocks) == 4,
    "five_choices_each": choice_counts == [5, 5, 5, 5],
    "no_exposed_meta_terms": not meta_hits,
    "no_absolute_signal_terms": not absolute_hits,
    "no_direct_recall_stems": not direct_hits,
    "inference_endings_present": questions.count("겠군.") >= 10,
    "answers_present": all(f"- {n}번 " in text for n in range(1, 5)),
}

# 실질 난도는 자동 판정만으로 확정하지 않고 설계 증거를 함께 요구한다.
design_evidence = {
    "delayed_retrieval": "2문단의 ‘관찰값과 피해의 대응’ → 5문단" in text,
    "two_paragraph_integration_q1_q2": "1·2번 정답은 각각 두 문단의 정보를 결합" in text,
    "variable_mapping_q3": "기업별 추가 감축 비용을 부담액 5와 차례로 대조" in text,
    "part_whole_q4": "부분적 개선과 순이득이라는 전체 평가" in text,
    "single_mutation_distractors": "각 오답의 핵심 변형은 한 곳으로 제한" in text,
}

result = {
    "source": str(SOURCE.relative_to(ROOT)),
    "metrics": {
        "passage_nonspace_chars": nonspace_length,
        "paragraphs": len(paragraphs),
        "questions": len(question_blocks),
        "choice_counts": choice_counts,
        "inference_ending_count": questions.count("겠군."),
        "absolute_signal_hits": absolute_hits,
        "exposed_meta_hits": meta_hits,
        "direct_recall_stem_hits": direct_hits,
    },
    "formal_checks": checks,
    "design_evidence": design_evidence,
    "formal_status": "PASS" if all(checks.values()) else "FAIL",
    "difficulty_status": "PASS_PROVISIONAL" if all(design_evidence.values()) else "FAIL",
    "manual_audit": {
        "q3": "A는 2, 4가 모두 5보다 작아 2단위, B는 3만 5보다 작아 1단위 감축. ④가 유일.",
        "q4": "정책 이득 30+15=45, 행정 비용 55 증가이므로 순이득 10 감소. ④가 유일.",
        "caveat": "평가원 체감 난도는 실제 풀이 또는 사용자 캘리브레이션 전까지 확정하지 않음.",
    },
}

OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

rows = "\n".join(
    f"| {name} | {'PASS' if ok else 'FAIL'} |" for name, ok in checks.items()
)
design_rows = "\n".join(
    f"| {name} | {'확인' if ok else '미확인'} |" for name, ok in design_evidence.items()
)
report = f"""# 통합사회 고난도 파일럿 v2 경제 검수

## 판정

- 형식·노출면: **{result['formal_status']}**
- 실질 난도 설계 증거: **{result['difficulty_status']}**
- 주의: 체감 난도는 블라인드 풀이 또는 사용자 캘리브레이션 전까지 확정하지 않는다.

## 계량 지표

- 지문 길이(공백 제외): {nonspace_length}자
- 문단 수: {len(paragraphs)}
- 문항 수: {len(question_blocks)}
- 문항별 선지 수: {choice_counts}
- `~겠군.` 계열 종결: {questions.count('겠군.')}회
- 노골적 절대어: {absolute_hits or '없음'}
- 수험생 노출면의 코드 메타어: {meta_hits or '없음'}
- 직접 회수형 발문: {direct_hits or '없음'}

## 형식 검사

| 항목 | 결과 |
|---|---|
{rows}

## 실질 난도 설계 증거

| 항목 | 결과 |
|---|---|
{design_rows}

## 수동 재계산

- 3번: A는 2단위, B는 1단위를 감축하므로 ④가 유일하다.
- 4번: 30+15-55=-10이므로 ④가 유일하다.

## 남은 검수

- 제작 의도를 보지 않은 블라인드 풀이
- 정답률·풀이 시간 또는 사용자 체감에 따른 난도 보정
- 경제형에서 확정한 규격을 다른 여섯 분야에 그대로 복제하지 않고 분야별 논리 구조로 변주
"""
OUT_MD.write_text(report, encoding="utf-8")

print(json.dumps({
    "formal_status": result["formal_status"],
    "difficulty_status": result["difficulty_status"],
    "passage_nonspace_chars": nonspace_length,
}, ensure_ascii=False))
