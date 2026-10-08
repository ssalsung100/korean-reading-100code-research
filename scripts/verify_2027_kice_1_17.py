#!/usr/bin/env python3
"""Integrity gate for the 2027 KICE June/September Q1-17 corpus."""
from __future__ import annotations

import importlib.util
import json
import re
import sys
import unicodedata
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "자료" / "평가원_국어"
TRANSCRIPTS = BASE / "전사_검수완료" / "2027"
REPORT_DIR = BASE / "검증"
CHOICES = "①②③④⑤"


def load_builder():
    path = ROOT / "scripts" / "build_2027_kice_transcripts.py"
    spec = importlib.util.spec_from_file_location("kice2027_builder", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def comparable(text: str) -> str:
    text = text.replace("․", "·").replace("󰡔", "『").replace("󰡕", "』")
    return "".join(
        char for char in text
        if unicodedata.category(char)[0] in {"L", "N"}
        or char in "①②③④⑤㉠㉡㉢㉣㉤㉮㉯ⓐⓑⓒⓓⓔ"
    )


def official_answers(answer_pdf: Path) -> dict[int, int]:
    page = fitz.open(answer_pdf)[0]
    words = page.get_text("words")
    result: dict[int, int] = {}
    by_row: dict[float, list[tuple[float, str]]] = {}
    for x0, y0, _, _, text, *_ in words:
        if 250 <= y0 <= 620:
            by_row.setdefault(round(y0, 1), []).append((x0, text))
    for row in by_row.values():
        number = next((text for x, text in row if 95 <= x <= 115 and text.isdigit()), None)
        answer = next((text for x, text in row if 128 <= x <= 145 and text in CHOICES), None)
        if number and answer and 1 <= int(number) <= 17:
            result[int(number)] = CHOICES.index(answer) + 1
    return result


def body_text(markdown: str) -> str:
    start = re.search(r"(?m)^## \[\d+~\d+\]", markdown)
    end = re.search(r"(?m)^## 정답\s*$", markdown)
    assert start and end
    body = markdown[start.start():end.start()]
    body = "\n".join(line for line in body.splitlines() if not line.startswith("!["))
    return body


def linked_files(markdown_path: Path, markdown: str) -> list[Path]:
    targets = re.findall(r"!?(?:\[[^\]]*\])\(([^)]+)\)", markdown)
    return [(markdown_path.parent / target).resolve() for target in targets]


def main() -> None:
    builder = load_builder()
    manifest = json.loads((BASE / "2027_6·9월_1-17_자산_원장.json").read_text(encoding="utf-8"))
    checks = []
    errors = []

    for month, spec in builder.SPECS.items():
        answer_pdf = BASE / "원본" / "2027" / f"2027_{month}_모의평가_국어_정답.pdf"
        parsed_answers = official_answers(answer_pdf)
        answer_ok = parsed_answers == spec["answers"]
        checks.append({"month": month, "check": "official_answers_1_17", "pass": answer_ok,
                       "count": len(parsed_answers)})
        if not answer_ok:
            errors.append(f"{month}: official answer mismatch")

        segments = builder.segment_lines(builder.source_lines(spec["pdf"]))
        seen_questions = []
        for start_q, end_q, _ in builder.GROUPS:
            path = TRANSCRIPTS / month / f"q{start_q:02d}-{end_q:02d}.md"
            markdown = path.read_text(encoding="utf-8")
            if "�" in markdown:
                errors.append(f"{month} {start_q}-{end_q}: U+FFFD")

            expected_segments = builder.group_slice(segments, start_q, end_q)
            expected = comparable("".join(segment.text for segment in expected_segments))
            actual = comparable(body_text(markdown))
            content_ok = expected == actual
            checks.append({"month": month, "range": f"{start_q}-{end_q}",
                           "check": "pdf_text_content_equivalence", "pass": content_ok,
                           "expected_chars": len(expected), "actual_chars": len(actual)})
            if not content_ok:
                mismatch = next((i for i, pair in enumerate(zip(expected, actual)) if pair[0] != pair[1]),
                                min(len(expected), len(actual)))
                errors.append(
                    f"{month} {start_q}-{end_q}: content mismatch at {mismatch}: "
                    f"{expected[mismatch:mismatch+30]!r} != {actual[mismatch:mismatch+30]!r}"
                )

            questions = list(re.finditer(r"(?m)^## (\d{1,2})\. ", markdown))
            q_numbers = [int(match.group(1)) for match in questions]
            seen_questions.extend(q_numbers)
            q_counts_ok = q_numbers == list(range(start_q, end_q + 1))
            checks.append({"month": month, "range": f"{start_q}-{end_q}",
                           "check": "question_sequence", "pass": q_counts_ok,
                           "questions": q_numbers})
            if not q_counts_ok:
                errors.append(f"{month} {start_q}-{end_q}: question sequence {q_numbers}")

            for index, match in enumerate(questions):
                q = int(match.group(1))
                chunk_end = questions[index + 1].start() if index + 1 < len(questions) else markdown.index("## 정답")
                chunk = markdown[match.start():chunk_end]
                found = re.findall(r"(?m)^(?:[①②③④⑤]|\|\s*[①②③④⑤]\s*\|)", chunk)
                choice_ok = len(found) == 5
                checks.append({"month": month, "question": q, "check": "five_choices",
                               "pass": choice_ok, "count": len(found)})
                if not choice_ok:
                    errors.append(f"{month} Q{q}: {len(found)} choices")

            broken = [str(target) for target in linked_files(path, markdown) if not target.is_file()]
            links_ok = not broken
            checks.append({"month": month, "range": f"{start_q}-{end_q}",
                           "check": "linked_assets_exist", "pass": links_ok,
                           "broken": broken})
            if broken:
                errors.extend(f"broken link: {target}" for target in broken)

        all_questions_ok = seen_questions == list(range(1, 18))
        checks.append({"month": month, "check": "complete_1_17", "pass": all_questions_ok,
                       "questions": seen_questions})
        if not all_questions_ok:
            errors.append(f"{month}: incomplete question set")

    visual_records = manifest["visuals"]
    visual_ok = len(visual_records) == 2 and all((ROOT / row["path"]).is_file() for row in visual_records)
    checks.append({"check": "semantic_visuals", "pass": visual_ok,
                   "count": len(visual_records), "ids": [row["asset_id"] for row in visual_records]})
    if not visual_ok:
        errors.append("semantic visual manifest mismatch")

    passed = not errors and all(row["pass"] for row in checks)
    payload = {
        "schema_version": "1.0",
        "scope": "2027학년도 평가원 6월·9월 모의평가 국어 1~17번",
        "status": "PASS" if passed else "FAIL",
        "counts": {
            "exams": 2,
            "transcript_groups": 8,
            "questions": 34,
            "semantic_visuals": len(visual_records),
            "checks": len(checks),
            "errors": len(errors),
        },
        "checks": checks,
        "errors": errors,
    }
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    json_path = REPORT_DIR / "2027_6·9월_1-17_검증_v1.json"
    md_path = REPORT_DIR / "2027_6·9월_1-17_검증_v1.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# 2027학년도 6·9월 모의평가 국어 1~17번 검증",
        "",
        f"- 최종 판정: **{payload['status']}**",
        "- 범위: 2회 × 17문항 = 34문항",
        "- 전사 문항군: 8개",
        f"- 의미 시각 자료: {len(visual_records)}개",
        f"- 검사항목: {len(checks)}개",
        f"- 오류: {len(errors)}개",
        "",
        "## 검증 항목",
        "",
        "- 공식 정답표의 1~17번을 좌표 기반으로 다시 추출하여 전사 정답과 대조",
        "- 문제 번호 1~17의 연속성과 문항별 ①~⑤ 완비 여부 확인",
        "- PDF 텍스트 레이어와 Markdown 본문의 공백·서식 제외 문자열 전수 대조",
        "- 원본 페이지 및 시각 자료 링크의 실제 파일 존재 확인",
        "- 대체 문자(U+FFFD)와 시각 자료 원장 누락 여부 확인",
        "",
        "## 오류",
        "",
    ]
    lines.extend([f"- {error}" for error in errors] or ["- 없음"])
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(payload["status"], json_path.relative_to(ROOT), f"checks={len(checks)} errors={len(errors)}")
    if not passed:
        for error in errors:
            print("ERROR", error)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
