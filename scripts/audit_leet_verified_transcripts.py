#!/usr/bin/env python3
"""Audit manually verified LEET transcript groups and their provenance."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path("자료/LEET_언어이해")
TRANSCRIPTS = ROOT / "전사_검수완료"
MANIFEST = TRANSCRIPTS / "manifest.json"
ANSWERS = ROOT / "normalized_answers.json"
REPORT = ROOT / "검증" / "공식페이지_대조완료_전사검증_v1.md"
CHOICE_MARKS = "①②③④⑤"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def official_answer_map() -> dict[tuple[int, str], dict[str, str]]:
    payload = json.loads(ANSWERS.read_text(encoding="utf-8"))
    result = {}
    for record in payload["records"]:
        result[(record["year"], record["variant"])] = record["answers"]
    return result


def question_sections(text: str) -> dict[int, str]:
    matches = list(re.finditer(r"(?m)^## (\d+)\. ", text))
    sections = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else text.find("\n## 정답", match.end())
        if end < 0:
            end = len(text)
        sections[int(match.group(1))] = text[match.start():end]
    return sections


def main() -> None:
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = payload.get("records", [])
    official_answers = official_answer_map()
    errors: list[str] = []
    seen_questions: set[tuple[int, str, int]] = set()
    listed_files: set[Path] = set()
    rows = []

    if payload.get("record_count") != len(records):
        errors.append("manifest record_count와 실제 records 수가 다름")

    for index, record in enumerate(records, start=1):
        label = f"record {index} ({record.get('year')} {record.get('variant')})"
        transcript = Path(record.get("file", ""))
        listed_files.add(transcript)
        if not transcript.is_file():
            errors.append(f"{label}: 전사 파일 없음: {transcript}")
            continue
        if sha256(transcript) != record.get("file_sha256"):
            errors.append(f"{label}: 전사 파일 SHA-256 불일치")

        text = transcript.read_text(encoding="utf-8")
        body = text.split("\n## 대조 메모", 1)[0]
        sections = question_sections(body)
        expected_questions = record.get("questions", [])
        if sorted(sections) != expected_questions:
            errors.append(
                f"{label}: 문항 절 불일치 {sorted(sections)} != {expected_questions}"
            )

        for question in expected_questions:
            key = (record["year"], record["variant"], question)
            if key in seen_questions:
                errors.append(f"{label}: 문항 중복 등록 {question}번")
            seen_questions.add(key)
            section = sections.get(question, "")
            choice_lines = re.findall(rf"(?m)^[{CHOICE_MARKS}] .+$", section)
            marks = [line[0] for line in choice_lines]
            if marks != list(CHOICE_MARKS):
                errors.append(f"{label}: {question}번 선지 표지 오류 {marks}")

            manifest_answer = record.get("answers", {}).get(str(question))
            official_answer = official_answers.get((record["year"], record["variant"]), {}).get(str(question))
            if manifest_answer != official_answer:
                errors.append(
                    f"{label}: {question}번 정답 불일치 {manifest_answer} != {official_answer}"
                )
            if f"\n{question}. {manifest_answer}\n" not in body:
                errors.append(f"{label}: {question}번 정답이 전사 파일에 없거나 형식이 다름")

        for page in record.get("official_pages", []):
            page_path = Path(page.get("file", ""))
            if not page_path.is_file():
                errors.append(f"{label}: 공식 페이지 없음: {page_path}")
            elif sha256(page_path) != page.get("sha256"):
                errors.append(f"{label}: 공식 페이지 SHA-256 불일치: {page_path}")

        if re.search(r"(?m)^## (left|right)$", body):
            errors.append(f"{label}: OCR 단 구획 표지가 남아 있음")
        rows.append((record["year"], record["variant"], expected_questions, transcript))

    actual_files = set(TRANSCRIPTS.glob("[0-9][0-9][0-9][0-9]/q*.md"))
    for extra in sorted(actual_files - listed_files):
        errors.append(f"manifest에 없는 전사 파일: {extra}")
    for missing in sorted(listed_files - actual_files):
        errors.append(f"manifest에는 있으나 검색되지 않은 전사 파일: {missing}")

    status = "PASS" if not errors else "FAIL"
    lines = [
        "# 공식 페이지 대조 완료 LEET 전사 검증",
        "",
        f"- 결과: **{status}**",
        f"- 문항군: {len(records)}개",
        f"- 문항: {len(seen_questions)}개",
        f"- 파일: {len(actual_files)}개",
        "- 자동 검사: 전사·공식 페이지 SHA-256, 문항 범위, 문항별 ①~⑤, 공식 정답 일치, 중복·미등록 파일",
        "- 한계: 자동 검사는 글자의 의미상 정확성을 판독하지 않는다. `검수완료` 승격 전 공식 페이지 육안 대조가 선행되어야 한다.",
        "",
        "## 검증된 문항군",
        "",
        "| 학년도 | 유형 | 문항 | 파일 |",
        "| --- | --- | --- | --- |",
    ]
    for year, variant, questions, transcript in rows:
        relative = Path("..") / transcript.relative_to(ROOT)
        question_range = f"{min(questions)}~{max(questions)}"
        lines.append(
            f"| {year} | {variant} | {question_range} | [{transcript.name}]({relative.as_posix()}) |"
        )
    lines.extend(["", "## 오류", ""])
    lines.extend(f"- {error}" for error in errors) if errors else lines.append("- 없음")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        f"{status} groups={len(records)} questions={len(seen_questions)} "
        f"files={len(actual_files)} errors={len(errors)}"
    )
    print(REPORT)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
