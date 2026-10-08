#!/usr/bin/env python3
"""Build a preliminary, problem-evidenced concept map from normalized questions."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


STAGE_LABELS = {1: "기초", 2: "핵심", 3: "심화"}
GRADE_ORDER = {"A": 0, "B": 1, "C": 2, "미검출": 3}


def match_concept(text: str, aliases: list[str]) -> list[str]:
    return [alias for alias in aliases if alias in text]


def grade(question_count: int, group_count: int, hub: bool) -> tuple[str, int]:
    score = question_count + max(0, group_count - 1) * 3 + (5 if hub and question_count else 0)
    if question_count >= 15 or score >= 25:
        return "A", score
    if question_count >= 5 or score >= 10:
        return "B", score
    if question_count:
        return "C", score
    return "미검출", 0


def analyze(concepts: list[dict], questions: list[dict], audited_question_ids: set[str] | None = None) -> list[dict]:
    audited_question_ids = audited_question_ids or set()
    results: list[dict] = []
    for concept in concepts:
        evidence = []
        alias_counts: dict[str, int] = defaultdict(int)
        for question in questions:
            matches = match_concept(question["text"], concept["aliases"])
            if not matches:
                continue
            evidence.append(question)
            for alias in matches:
                alias_counts[alias] += 1
        groups = sorted({f"{q['course']}·{q['source_group']}" for q in evidence})
        importance, score = grade(len(evidence), len(groups), concept.get("hub", False))
        results.append(
            {
                **concept,
                "stage_label": STAGE_LABELS[concept["stage"]],
                "importance": importance,
                "score": score,
                "question_count": len(evidence),
                "source_group_count": len(groups),
                "source_groups": groups,
                "matched_aliases": dict(sorted(alias_counts.items(), key=lambda item: (-item[1], item[0]))),
                "sample_question_ids": [q["id"] for q in evidence[:8]],
                "image_review_evidence": sum(
                    q["needs_image_review"] and q["id"] not in audited_question_ids for q in evidence
                ),
                "audited_image_evidence": sum(
                    q["needs_image_review"] and q["id"] in audited_question_ids for q in evidence
                ),
            }
        )
    return results


def learning_order(items: list[dict]) -> list[dict]:
    """Return a dependency-respecting order, using stage/importance as tie breakers."""
    by_id = {item["id"]: item for item in items}
    remaining = set(by_id)
    ordered: list[dict] = []
    while remaining:
        ready = [
            by_id[item_id]
            for item_id in remaining
            if not ({p for p in by_id[item_id]["prerequisites"] if p in by_id} & remaining)
        ]
        if not ready:  # Defensive fallback for an accidental dependency cycle.
            ready = [by_id[item_id] for item_id in remaining]
        ready.sort(key=lambda item: (item["stage"], GRADE_ORDER[item["importance"]], -item["score"], item["name"]))
        chosen = ready[0]
        ordered.append(chosen)
        remaining.remove(chosen["id"])
    return ordered


def render_summary(results: list[dict], question_count: int, image_audit_complete: bool = False) -> str:
    detected = [item for item in results if item["question_count"]]
    names = {item["id"]: item["name"] for item in results}
    lines = [
        "# 통합사회 문제 역분석 기반 개념 지도",
        "",
        f"- 분석 문항: {question_count}개",
        f"- 개념 후보: {len(results)}개",
        f"- 문제에서 직접 검출된 개념: {len(detected)}개",
        "- 상태: 문제 텍스트 자동 분석·이미지 전수 판독 반영" if image_audit_complete else "- 상태: 1차 자동 분석(정답표 결합·이미지 판독 전)",
        "",
        "## 두 축의 의미",
        "",
        "- **출제 중요도 A~C**: 문항 출현 수, 여러 문제군에서의 반복, 개념 연결 허브 여부를 반영한다.",
        "- **학습 단계**: 1 기초(정의·기본 구분), 2 핵심(관계·원리·적용), 3 심화(이론 비교·조건·예외·다단 추론) 순이다.",
        "- 두 축은 독립적이다. 예를 들어 `A·기초`는 자주 쓰이는 토대이고, `A·심화`는 고난도 지문의 중심 후보이다.",
        "",
        "## 우선순위 요약",
        "",
        "| 중요도 | 기초 | 핵심 | 심화 |",
        "|---|---:|---:|---:|",
    ]
    for grade_name in ("A", "B", "C", "미검출"):
        counts = [sum(r["importance"] == grade_name and r["stage"] == stage for r in results) for stage in (1, 2, 3)]
        lines.append(f"| {grade_name} | {counts[0]} | {counts[1]} | {counts[2]} |")

    domains = ["윤리", "지리", "사회문화", "경제", "법과 정치", "역사", "융합"]
    for domain in domains:
        domain_items = [item for item in results if domain in item["domains"]]
        domain_items = learning_order(domain_items)
        lines.extend(
            [
                "",
                f"## {domain}",
                "",
                "| 학습 순서 | 개념 | 중요도 | 근거 문항 | 문제군 | 선수 개념 | 상태 |",
                "|---:|---|:---:|---:|---:|---|---|",
            ]
        )
        for position, item in enumerate(domain_items, start=1):
            prereqs = ", ".join(names.get(p, p) for p in item["prerequisites"]) or "—"
            state = "이미지 재검수" if item["image_review_evidence"] else "텍스트 확인"
            if item["audited_image_evidence"] and not item["image_review_evidence"]:
                state = "이미지 확인"
            if item["importance"] == "미검출":
                state = "외부·이미지 확인"
            lines.append(
                f"| {item['stage']}-{position:02d} {item['stage_label']} | {item['name']} | {item['importance']} | "
                f"{item['question_count']} | {item['source_group_count']} | {prereqs} | {state} |"
            )

    lines.extend(
        [
            "",
            "## 해석 및 다음 검수",
            "",
            "- 현재 등급은 정답 선지의 결정력까지 반영하지 않은 빈도 기반 1차 등급이다.",
            "- 이미지 의존 문항은 전수 판독 장부의 시각 관계와 연결했으며, 텍스트 빈도 등급과 별도로 활용한다." if image_audit_complete else "- 이미지 의존 문항은 그림·지도·그래프의 핵심 개념이 텍스트에 없을 수 있으므로 OCR 뒤 등급을 다시 계산한다.",
            "- 빠른정답표를 문항 묶음과 연결한 뒤 정답 선지 가중치와 오답 경계 개념을 추가한다.",
            "- 미검출 개념은 곧 중요하지 않다는 뜻이 아니다. 표현 변형, 이미지 수록, 자료 누락 여부를 먼저 확인한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("concepts", type=Path)
    parser.add_argument("questions", type=Path)
    parser.add_argument("json_output", type=Path)
    parser.add_argument("markdown_output", type=Path)
    parser.add_argument("--image-audit", type=Path)
    args = parser.parse_args()

    concepts = json.loads(args.concepts.read_text(encoding="utf-8"))
    questions = json.loads(args.questions.read_text(encoding="utf-8"))
    audited_question_ids: set[str] = set()
    image_audit_complete = False
    if args.image_audit:
        audit = json.loads(args.image_audit.read_text(encoding="utf-8"))
        audited_question_ids = {
            image["question_id"]
            for image in audit.get("images", [])
            if image.get("inspection_status") == "원본 육안 판독 완료"
        }
        image_audit_complete = audit.get("status") == "complete"
    results = analyze(concepts, questions, audited_question_ids)
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.markdown_output.write_text(
        render_summary(results, len(questions), image_audit_complete), encoding="utf-8"
    )
    print(f"analyzed {len(concepts)} concepts against {len(questions)} questions")


if __name__ == "__main__":
    main()
