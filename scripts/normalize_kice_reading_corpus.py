#!/usr/bin/env python3
"""Normalize the local KICE reading collection into passage/question JSONL."""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


SOURCE = Path("고3 기출/hwpx_텍스트_연도별.md")
ANSWER_LINKS = Path("자료/평가원_정답표/passage_answer_links.json")
ANSWER_KEYS = Path("자료/평가원_정답표/normalized_answer_keys.json")
PASSAGES_OUT = Path("data/kice_passages.jsonl")
QUESTIONS_OUT = Path("data/kice_questions.jsonl")
REPORT = Path("분석/평가원_독서_DB_정규화_검증_v1.md")
HEADER = re.compile(
    r"^### \[(\d{3})~(\d{3})\] (\d{4})학년도 (.+?) (\d+)번~(\d+)번$", re.M
)
CHOICES = "①②③④⑤"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exam_parts(label: str) -> tuple[str, str | None, str | None]:
    variant = None
    if label.endswith("AB"):
        variant = "AB"
        label = label[:-2]
    elif label.endswith(("A", "B")):
        variant = label[-1]
        label = label[:-1]
    if label == "수능":
        return "수능", None, variant
    if label == "예시문항":
        return "예시문항", None, variant
    month = label.split("월", 1)[0] + "월" if "월" in label else None
    return "수능 모의평가", month, variant


def first_value(lines: list[str], prefix: str) -> str | None:
    for line in lines:
        if line.startswith(prefix):
            return line[len(prefix):].strip(" `")
    return None


def split_choices(section: str) -> tuple[str, list[str], str]:
    positions = []
    for mark in CHOICES:
        # Some HWPX tables place several options on one physical line.  A
        # unique, ordered occurrence of each circled number is still safe to
        # split; repeated or missing marks remain unresolved.
        found = list(re.finditer(rf"{re.escape(mark)}\s*", section))
        if len(found) != 1:
            return section.strip(), [], "incomplete_visual_or_table"
        positions.append(found[0])
    if [m.start() for m in positions] != sorted(m.start() for m in positions):
        return section.strip(), [], "order_error"
    stem = section[:positions[0].start()].strip()
    choices = []
    for index, match in enumerate(positions):
        end = positions[index + 1].start() if index + 1 < len(positions) else len(section)
        choices.append(section[match.end():end].strip())
    return stem, choices, "complete"


def choose_answer(link: dict, tables: dict[str, dict], question: int, variant: str | None) -> tuple[str | None, dict]:
    # Keep every value seen for a variant.  A later table must not silently
    # overwrite an earlier table: that can turn a conflicting answer key into
    # a false verified answer.
    raw_candidates: dict[str, list[str]] = {}
    for table_id in link.get("answer_table_ids", []):
        table = tables[table_id]
        table_variant = table.get("variant") or "common"
        value = table.get("answers", {}).get(str(question))
        if value:
            raw_candidates.setdefault(table_variant, [])
            if value not in raw_candidates[table_variant]:
                raw_candidates[table_variant].append(value)
    candidates = {
        key: values[0] if len(values) == 1 else values
        for key, values in raw_candidates.items()
    }
    if not candidates:
        return None, candidates
    if variant in {"A", "B"}:
        # An explicit A/B request is never satisfied by common or the other
        # variant.  Conflicting values for the requested variant remain
        # visible in candidates and stay unresolved.
        value = candidates.get(variant)
        return (value if isinstance(value, str) else None), candidates
    values = {
        value
        for candidate in candidates.values()
        for value in (candidate if isinstance(candidate, list) else [candidate])
    }
    return (next(iter(values)) if len(values) == 1 else None), candidates


def answer_is_mechanically_resolved(question: dict) -> bool:
    """Accept an answer only when candidates support the exact stored value."""
    if question.get("official_answer_verified") is not True or question.get("answer") is None:
        return False
    candidates = question.get("answer_candidates") or {}
    variant = question.get("variant")
    if variant in {"A", "B"}:
        candidate = candidates.get(variant)
        return isinstance(candidate, str) and candidate == question["answer"]
    values = [
        value
        for candidate in candidates.values()
        for value in (candidate if isinstance(candidate, list) else [candidate])
    ]
    return bool(values) and len(set(values)) == 1 and values[0] == question["answer"]


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    matches = list(HEADER.finditer(text))
    answer_links_payload = json.loads(ANSWER_LINKS.read_text(encoding="utf-8"))
    link_by_key = {
        (item["section_id"], item["heading"]): item
        for item in answer_links_payload["links"]
    }
    answer_tables = {
        item["table_id"]: item
        for item in json.loads(ANSWER_KEYS.read_text(encoding="utf-8"))["tables"]
    }

    passages = []
    questions = []
    errors = []
    for index, match in enumerate(matches):
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.end():block_end]
        global_start, global_end = int(match.group(1)), int(match.group(2))
        year, exam_label = int(match.group(3)), match.group(4)
        original_start, original_end = int(match.group(5)), int(match.group(6))
        expected_count = global_end - global_start + 1
        if expected_count != original_end - original_start + 1:
            errors.append(f"문항 범위 길이 불일치: {match.group(0)}")
            continue

        q_positions = []
        cursor = 0
        for global_id in range(global_start, global_end + 1):
            found = re.search(rf"(?m)^{global_id:03d}\s*$", block[cursor:])
            if not found:
                errors.append(f"전역 문항 번호 없음: {year} {exam_label} {global_id:03d}")
                break
            q_positions.append((global_id, cursor + found.start(), cursor + found.end()))
            cursor += found.end()
        if len(q_positions) != expected_count:
            continue

        before_questions = block[:q_positions[0][1]]
        separators = list(re.finditer(r"(?m)^-{20,}\s*$", before_questions))
        if len(separators) != 2:
            errors.append(f"본문 구분선 수 오류: {year} {exam_label}")
            continue
        preface = before_questions[:separators[0].start()].strip()
        passage_text = before_questions[separators[0].end():separators[1].start()].strip()
        preface_lines = preface.splitlines()
        source_hwpx = first_value(preface_lines, "- 원본:")
        unit = first_value(preface_lines, "- 단원:")
        exam_type, month, variant = exam_parts(exam_label)
        section_id = f"{global_start:03d}~{global_end:03d}"
        heading = f"{year}학년도 {exam_label} {original_start}번~{original_end}번"
        passage_id = (
            f"KICE-{year}-{exam_label.replace(' ', '_')}-"
            f"Q{original_start:02d}-{original_end:02d}-S{section_id}"
        )
        link = link_by_key.get((section_id, heading), {
            "link_status": "missing_link_record", "answer_table_ids": []
        })
        passage = {
            "passage_id": passage_id,
            "exam_family": "KICE",
            "academic_year": year,
            "exam_label": exam_label,
            "exam_type": exam_type,
            "month": month,
            "variant": variant,
            "question_start": original_start,
            "question_end": original_end,
            "question_count": expected_count,
            "dataset_section_id": section_id,
            "source_hwpx": source_hwpx,
            "unit": unit,
            "passage_text": passage_text,
            "passage_sha256": sha256_text(passage_text),
            "contains_visual_placeholder": any(
                x in passage_text for x in ("<그림>", "<표>", "&lt;그림&gt;", "&lt;표&gt;")
            ),
            "answer_link_status": link.get("link_status"),
            "answer_table_ids": link.get("answer_table_ids", []),
            "source_markdown": str(SOURCE),
        }
        passages.append(passage)

        for offset, (global_id, _, content_start) in enumerate(q_positions):
            section_end = q_positions[offset + 1][1] if offset + 1 < len(q_positions) else len(block)
            raw_section = block[content_start:section_end].strip()
            original_question = original_start + offset
            stem, choices, choice_status = split_choices(raw_section)
            answer, answer_candidates = choose_answer(
                link, answer_tables, original_question, variant
            )
            questions.append({
                "question_id": f"{passage_id}-Q{original_question:02d}",
                "passage_id": passage_id,
                "exam_family": "KICE",
                "academic_year": year,
                "exam_label": exam_label,
                "exam_type": exam_type,
                "month": month,
                "variant": variant,
                "question_number": original_question,
                "dataset_question_id": f"{global_id:03d}",
                "stem": stem,
                "choices": choices,
                "choice_parse_status": choice_status,
                "contains_visual_placeholder": any(
                    x in raw_section for x in ("<그림>", "<표>", "&lt;그림&gt;", "&lt;표&gt;")
                ),
                "answer": answer,
                "answer_candidates": answer_candidates,
                "official_answer_verified": answer is not None,
                "answer_link_status": link.get("link_status"),
                "raw_section_sha256": sha256_text(raw_section),
            })

    PASSAGES_OUT.parent.mkdir(exist_ok=True)
    with PASSAGES_OUT.open("w", encoding="utf-8") as handle:
        for row in passages:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    with QUESTIONS_OUT.open("w", encoding="utf-8") as handle:
        for row in questions:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    choice_counts = Counter(row["choice_parse_status"] for row in questions)
    answer_counts = Counter(
        "verified" if row["official_answer_verified"] else "unresolved"
        for row in questions
    )
    visual_questions = sum(row["contains_visual_placeholder"] for row in questions)
    lines = [
        "# 평가원 독서 DB 정규화 검증 v1",
        "",
        f"- 원본 세트: {len(matches)}개",
        f"- 정규화 지문: {len(passages)}개",
        f"- 정규화 문항: {len(questions)}개",
        f"- ①~⑤ 완전 추출: {choice_counts['complete']}개",
        f"- 표·이미지 배치로 선지 불완전: {choice_counts['incomplete_visual_or_table']}개",
        f"- 공식 정답 연결: {answer_counts['verified']}개",
        f"- 공식 정답 미연결·모호: {answer_counts['unresolved']}개",
        f"- 문항 내부 `<그림>`·`<표>` 표지: {visual_questions}개",
        f"- 구조 오류: {len(errors)}개",
        "",
        "## 판정",
        "",
        "텍스트 선지 5개가 모두 존재하고 공식 정답이 연결된 문항만 코드 본판독에 자동 투입한다. 선지가 표나 이미지로 누락된 문항은 원본 HWPX의 해당 시각 자료를 대조하기 전까지 후보 목록에만 둔다.",
        "",
        "## 출력",
        "",
        f"- 지문: `{PASSAGES_OUT}`",
        f"- 문항: `{QUESTIONS_OUT}`",
        "",
        "## 구조 오류",
        "",
    ]
    lines.extend(f"- {error}" for error in errors) if errors else lines.append("- 없음")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"passages={len(passages)} questions={len(questions)} "
        f"choices={dict(choice_counts)} answers={dict(answer_counts)} errors={len(errors)}"
    )
    print(PASSAGES_OUT)
    print(QUESTIONS_OUT)
    print(REPORT)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
