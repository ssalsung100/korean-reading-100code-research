#!/usr/bin/env python3
"""Build analysis JSONL files from the visually verified MEET Markdown corpus.

The OCR-derived ``*_raw.jsonl`` files are deliberately left untouched.  This
builder treats the canonical Markdown manifest as the only transcription
authority and preserves enough source metadata to audit every record.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_ROOT = ROOT / "자료/MEET_언어추론/전사_검수완료"
MANIFEST_PATH = CANONICAL_ROOT / "manifest.json"
PASSAGES_PATH = ROOT / "data/meet_passages.jsonl"
QUESTIONS_PATH = ROOT / "data/meet_questions.jsonl"
REPORT_JSON = ROOT / "자료/MEET_언어추론/검증/MEET_정본_JSONL_검증_v1.json"
REPORT_MD = ROOT / "자료/MEET_언어추론/검증/MEET_정본_JSONL_검증_v1.md"

QUESTION_HEADING_RE = re.compile(r"(?m)^##\s+(\d+)\.\s*(.+?)\s*$")
ANSWER_HEADING_RE = re.compile(r"(?m)^##\s+정답\s*$")
NOTE_HEADING_RE = re.compile(r"(?m)^##\s+대조 메모\s*$")
CHOICE_RE = re.compile(r"(?<![㉠-㉿])([①②③④⑤])")
ANSWER_RE = re.compile(r"(?m)^\s*(\d+)\.\s*([①②③④⑤])\s*$")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def clean_context(text: str) -> str:
    """Remove title/source block while retaining the actual common context."""
    lines = text.strip().splitlines()
    if lines and lines[0].startswith("# "):
        lines.pop(0)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and lines[0].startswith(">"):
        lines.pop(0)
    while lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join(lines).strip()


def parse_choices(body: str) -> tuple[str, list[dict[str, str]]]:
    matches = list(CHOICE_RE.finditer(body))
    if len(matches) != 5 or [m.group(1) for m in matches] != list("①②③④⑤"):
        return body.strip(), []
    prompt = body[: matches[0].start()].strip()
    choices = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        choices.append({
            "label": match.group(1),
            "text": body[match.end():end].strip(),
        })
    return prompt, choices


def dump_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=False) + "\n")


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    records = manifest["records"]
    passages: list[dict] = []
    questions: list[dict] = []
    errors: list[str] = []

    for item in records:
        md_path = ROOT / item["file"]
        raw = md_path.read_bytes()
        text = raw.decode("utf-8")
        actual_sha = sha256_bytes(raw)
        if actual_sha != item["file_sha256"]:
            errors.append(f"SHA mismatch: {item['file']}")

        answer_heading = ANSWER_HEADING_RE.search(text)
        note_heading = NOTE_HEADING_RE.search(text)
        content_end = answer_heading.start() if answer_heading else (note_heading.start() if note_heading else len(text))
        content = text[:content_end].rstrip()
        q_matches = list(QUESTION_HEADING_RE.finditer(content))
        found_numbers = [int(match.group(1)) for match in q_matches]
        expected_numbers = [int(number) for number in item["questions"]]
        if found_numbers != expected_numbers:
            errors.append(f"question heading mismatch: {item['file']} expected={expected_numbers} found={found_numbers}")
            continue

        answers_from_md = {
            int(number): symbol
            for number, symbol in ANSWER_RE.findall(
                text[answer_heading.end() : note_heading.start() if note_heading else len(text)]
                if answer_heading else ""
            )
        }
        answers_from_manifest = {int(number): symbol for number, symbol in item["answers"].items()}
        if answers_from_md != answers_from_manifest:
            errors.append(f"answer mismatch: {item['file']}")

        label = str(item["label"])
        q_start, q_end = expected_numbers[0], expected_numbers[-1]
        group_id = f"MEET-{label}-Q{q_start:02d}-{q_end:02d}"
        context_markdown = clean_context(content[: q_matches[0].start()])
        visual_assets = item.get("visual_assets", [])
        common_source = {
            "canonical_markdown": item["file"],
            "canonical_markdown_sha256": actual_sha,
            "official_pages": item.get("official_pages", []),
            "visual_assets": visual_assets,
            "verification_status": item["status"],
        }

        passages.append({
            "exam_family": "MEET",
            "group_id": group_id,
            "label": label,
            "year": item["year"],
            "variant": item["variant"],
            "question_numbers": expected_numbers,
            "context_markdown": context_markdown,
            "has_common_passage": bool(context_markdown),
            "source": common_source,
        })

        for index, match in enumerate(q_matches):
            number = int(match.group(1))
            end = q_matches[index + 1].start() if index + 1 < len(q_matches) else len(content)
            question_markdown = content[match.start():end].strip()
            body = content[match.end():end].strip()
            prompt_markdown, choices = parse_choices(body)
            if len(choices) != 5:
                errors.append(f"choice parse failure: {item['file']} Q{number}")
            question_id = f"MEET-{label}-Q{number:02d}"
            questions.append({
                "exam_family": "MEET",
                "question_id": question_id,
                "group_id": group_id,
                "label": label,
                "year": item["year"],
                "variant": item["variant"],
                "number": number,
                "stem": match.group(2).strip(),
                "prompt_markdown": prompt_markdown,
                "choices": choices,
                "answer": answers_from_manifest.get(number),
                "question_markdown": question_markdown,
                "source": common_source,
            })

    passage_ids = [row["group_id"] for row in passages]
    question_ids = [row["question_id"] for row in questions]
    if len(passage_ids) != len(set(passage_ids)):
        errors.append("duplicate group_id")
    if len(question_ids) != len(set(question_ids)):
        errors.append("duplicate question_id")
    if len(passages) != 125:
        errors.append(f"expected 125 groups, got {len(passages)}")
    if len(questions) != 380:
        errors.append(f"expected 380 questions, got {len(questions)}")

    dump_jsonl(PASSAGES_PATH, passages)
    dump_jsonl(QUESTIONS_PATH, questions)

    by_label = Counter(row["label"] for row in questions)
    report = {
        "status": "PASS" if not errors else "FAIL",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "authority": rel(MANIFEST_PATH),
        "authority_sha256": sha256_bytes(MANIFEST_PATH.read_bytes()),
        "outputs": {
            rel(PASSAGES_PATH): {"records": len(passages), "sha256": sha256_bytes(PASSAGES_PATH.read_bytes())},
            rel(QUESTIONS_PATH): {"records": len(questions), "sha256": sha256_bytes(QUESTIONS_PATH.read_bytes())},
        },
        "counts": {
            "groups": len(passages),
            "questions": len(questions),
            "questions_with_five_choices": sum(len(row["choices"]) == 5 for row in questions),
            "questions_with_answer": sum(bool(row["answer"]) for row in questions),
            "groups_with_visual_assets": sum(bool(row["source"]["visual_assets"]) for row in passages),
            "questions_by_label": dict(sorted(by_label.items())),
        },
        "errors": errors,
        "provenance_note": "OCR 초안이 아니라 공식 지면 직접 대조 완료 Markdown과 그 manifest만을 입력으로 사용했다.",
    }
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# MEET 정본 JSONL 검증 보고서 v1",
        "",
        f"- 판정: **{report['status']}**",
        f"- 정본 문항군: **{len(passages)}개**",
        f"- 정본 문항: **{len(questions)}개**",
        f"- 5개 선지 파싱 완료: **{report['counts']['questions_with_five_choices']}문항**",
        f"- 공식 정답 연결: **{report['counts']['questions_with_answer']}문항**",
        f"- 입력 권위 파일: `{rel(MANIFEST_PATH)}`",
        "",
        "## 산출물",
        "",
        f"- `{rel(PASSAGES_PATH)}` — 문항군/공통 지문 단위",
        f"- `{rel(QUESTIONS_PATH)}` — 개별 문항·선지·정답 단위",
        "",
        "기존 `meet_passages_raw.jsonl`, `meet_questions_raw.jsonl`은 OCR 기반 초안이므로 정본 분석 입력으로 사용하지 않는다.",
        "",
        "## 연도별 문항 수",
        "",
    ]
    lines.extend(f"- {label}: {count}문항" for label, count in sorted(by_label.items()))
    if errors:
        lines.extend(["", "## 오류", ""] + [f"- {error}" for error in errors])
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
