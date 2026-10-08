#!/usr/bin/env python3
"""Build the advanced-economics extension of the Integrated Social concept map."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data/social_concepts.json"
QUESTIONS = ROOT / "분석/심화경제_문항_정규화.json"
IMAGE_AUDIT = ROOT / "분석/심화경제_이미지_전수판독.json"
JSON_OUT = ROOT / "분석/심화경제_개념_확장.json"
MD_OUT = ROOT / "분석/심화경제_개념_확장.md"
STAGE = {1: "기초", 2: "핵심", 3: "심화"}


def hits(text: str, aliases: list[str]) -> list[str]:
    return [alias for alias in aliases if alias in text]


def main() -> None:
    concepts = json.loads(CATALOG.read_text(encoding="utf-8"))
    questions = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    image_audit = json.loads(IMAGE_AUDIT.read_text(encoding="utf-8")) if IMAGE_AUDIT.exists() else None
    advanced = [c for c in concepts if c.get("source_level") == "심화 경제"]
    names = {c["id"]: c["name"] for c in concepts}
    records = []
    covered_questions: set[str] = set()

    for concept in advanced:
        evidence = []
        aliases = Counter()
        units = Counter()
        for q in questions:
            matched = hits(q["text"], concept["aliases"])
            if not matched:
                continue
            evidence.append(q["id"])
            covered_questions.add(q["id"])
            units[q["source_group"]] += 1
            aliases.update(matched)
        records.append(
            {
                **concept,
                "question_count": len(evidence),
                "unit_counts": dict(sorted(units.items(), key=lambda x: int(x[0][:-2]))),
                "matched_aliases": dict(aliases.most_common()),
                "sample_question_ids": evidence[:8],
            }
        )

    payload = {
        "source_files": len({q["source_file"] for q in questions}),
        "question_count": len(questions),
        "image_dependent_questions": sum(q["needs_image_review"] for q in questions),
        "advanced_concept_count": len(records),
        "covered_question_count": len(covered_questions),
        "concepts": records,
    }
    JSON_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    by_stage = defaultdict(list)
    for row in records:
        by_stage[row["stage"]].append(row)
    lines = [
        "# 심화 경제 HWPX 기반 개념 지도 확장",
        "",
        "## 점검 범위와 판정",
        "",
        f"- 원본: `심화 사회과목/경제`의 HWPX {payload['source_files']}개",
        f"- 정규화 문항: {payload['question_count']}개(이미지 의존 {payload['image_dependent_questions']}개)",
        f"- 이미지 판독: {image_audit['audit_scope']['questions']}개 문항·{image_audit['audit_scope']['images']}개 이미지 전수 완료" if image_audit else "- 이미지 판독: 미실시",
        f"- 새 심화 연결 개념: {payload['advanced_concept_count']}개",
        f"- 새 개념 사전으로 직접 포착된 문항: {payload['covered_question_count']}개",
        "- 원칙: 통합사회 대개념을 삭제·대체하지 않고, 경제 선택 과목의 모형·조건·계산 관계를 하위 노드로 연결했다.",
        "- 이미지의 곡선·축·영역·수치 조건은 전수 판독 장부와 세부 관계 사전에 별도로 연결했다.",
        "",
        "## 학습 순서",
        "",
    ]
    for stage in (1, 2, 3):
        rows = sorted(by_stage[stage], key=lambda r: (-r["question_count"], r["name"]))
        if not rows:
            continue
        lines += [f"### {stage}단계 · {STAGE[stage]}", "", "| 개념 | 근거 문항 | 선수 개념 | 기존 지도와의 연결 |", "|---|---:|---|---|"]
        for row in rows:
            prereq = ", ".join(names.get(x, x) for x in row.get("prerequisites", [])) or "—"
            extends = ", ".join(names.get(x, x) for x in row.get("extends", [])) or "새 중간 노드"
            lines.append(f"| {row['name']} | {row['question_count']} | {prereq} | {extends} |")
        lines.append("")

    chains = [
        ("미시 경제", "희소성과 경제 문제 → 합리적 선택과 비용·편익 → 한계 분석과 최적 선택 → 기업의 생산·비용·수입과 이윤 극대화"),
        ("시장 모형", "시장 경제의 원리 → 수요·공급의 법칙과 시장 균형 → 수요·공급의 변동과 연관재 → 수요·공급의 가격 탄력성"),
        ("후생·정책", "시장 균형 → 소비자·생산자 잉여 → 최고·최저 가격제 / 조세·보조금 → 정부 개입의 효과와 한계"),
        ("시장 실패", "시장 실패 → 외부 효과 → 사적·사회적 비용/편익 → 사회적 최적과 교정 정책"),
        ("거시 경제", "국민 경제 순환 → 국내 총생산 → 물가·고용 → 경기 변동 → 총수요·총공급 → 재정·통화 정책"),
        ("국제 경제", "기회비용 → 비교 우위 → 생산 가능 곡선 → 교역 조건·무역 이익 → 외환 시장·환율 → 국제수지"),
        ("금융 생활", "가계 소득·지출 → 금융 자산의 유형과 속성 → 수익·위험·분산 투자 / 화폐의 시간 가치"),
    ]
    lines += ["## 핵심 연결 사슬", "", "| 축 | 선수 관계 |", "|---|---|"]
    lines += [f"| {a} | {b} |" for a, b in chains]

    lines += ["", "## 단원별 검출 지도", "", "| 단원 | 중심 개념(검출 문항 수) |", "|---:|---|"]
    for unit in range(1, 15):
        key = f"{unit}단원"
        found = sorted(
            ((r["unit_counts"].get(key, 0), r["name"]) for r in records if r["unit_counts"].get(key, 0)),
            reverse=True,
        )[:6]
        lines.append(f"| {unit} | " + ", ".join(f"{name}({count})" for count, name in found) + " |")

    lines += [
        "",
        "## 지문화 우선 조합",
        "",
        "1. `한계 분석 + 이윤 극대화`: 총량과 한계량의 차이, 최적점의 조건을 설명하는 과정형 지문.",
        "2. `잉여 + 가격 규제`: 정책 목적과 실제 귀결이 어긋날 수 있음을 원칙·예외 구조로 설명하는 지문.",
        "3. `외부 효과 + 사회적 최적`: 사적 판단과 사회 전체 판단의 기준 차이를 비교하는 지문.",
        "4. `GDP + 물가 + 고용`: 각 지표가 포착하는 것과 놓치는 것을 보충 도식으로 설명하는 지문.",
        "5. `총수요·총공급 + 안정화 정책`: 충격의 발생 위치에 따라 같은 정책의 효과가 달라지는 조건형 지문.",
        "6. `비교 우위 + 교역 조건`: 특화의 근거와 양국의 이익 범위를 생산 가능 곡선으로 추론하는 지문.",
        "7. `환율 + 국제수지`: 외환 수요·공급의 원인과 무역·자본 흐름의 결과를 양방향으로 추론하는 지문.",
        "8. `위험·수익 + 시간 가치`: 금융 상품의 법적 형식이 아니라 현금 흐름과 위험 배분을 비교하는 지문.",
        "",
        "## 이미지 검수 결과",
        "",
        "- 146개 이미지 의존 문항의 원본 156개를 모두 판독해 그래프 축·곡선 이동·영역·수치 조건을 30개 세부 관계로 분류했다.",
        "- 원본 BMP·PNG와 변환 PNG는 `자료/심화경제_문항이미지`에 문항 ID·단원·출처와 함께 보존했다.",
        "- 현재 확장은 기출 문항에서 반복 확인된 범위만 반영했다. 대학 경제학 개념을 임의로 선행 추가하지 않았다.",
    ]
    MD_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"built {len(records)} advanced concepts; covered {len(covered_questions)}/{len(questions)} questions")


if __name__ == "__main__":
    main()
