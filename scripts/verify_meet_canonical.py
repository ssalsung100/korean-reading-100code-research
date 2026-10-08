#!/usr/bin/env python3
"""Fail-closed integrity gate for directly verified MEET transcripts.

The gate validates only files already placed under 전사_검수완료.  It does
not promote OCR drafts and it does not call an incomplete year complete.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path("자료/MEET_언어추론")
TRANSCRIPT_DIR = ROOT / "전사_검수완료"
VERIFY_DIR = ROOT / "검증"
ANSWER_PATH = Path("data/meet_answer_keys.json")
MANIFEST_PATH = TRANSCRIPT_DIR / "manifest.json"
REPORT_JSON = VERIFY_DIR / "MEET_정본_검증게이트_v1.json"
REPORT_MD = VERIFY_DIR / "MEET_정본_검증게이트_v1.md"

CIRCLED = {1: "①", 2: "②", 3: "③", 4: "④", 5: "⑤"}
EXPECTED = {
    "2005예비": 50,
    "2005": 50,
    "2006": 40,
    "2007": 40,
    "2008": 40,
    "2009": 40,
    "2010": 40,
    "2011": 40,
    "2012": 40,
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_group(path: Path, answer_keys: dict[str, dict[str, int]]) -> tuple[dict | None, list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    label = path.parent.name
    if label not in answer_keys:
        return None, [f"알 수 없는 시험 폴더: {path}"]

    filename_match = re.fullmatch(r"q(\d{2})-(\d{2})\.md", path.name)
    if not filename_match:
        return None, [f"정본 파일명 규격 불일치: {path}"]
    first, last = map(int, filename_match.groups())
    expected_questions = list(range(first, last + 1))

    headings = [int(value) for value in re.findall(r"(?m)^##\s+(\d+)\.\s", text)]
    if headings != expected_questions:
        errors.append(f"문항 제목 연속성 불일치: {path} {headings}")

    answer_section = text.split("\n## 정답\n", 1)
    if len(answer_section) != 2:
        errors.append(f"정답 절 없음: {path}")
        answer_map: dict[int, str] = {}
        question_body = text
    else:
        question_body, answer_tail = answer_section
        answer_map = {
            int(question): answer
            for question, answer in re.findall(r"(?m)^(\d+)\.\s*([①②③④⑤])\s*$", answer_tail)
        }
        if sorted(answer_map) != expected_questions:
            errors.append(f"정답 번호 연속성 불일치: {path} {sorted(answer_map)}")

    for question in expected_questions:
        expected_answer = CIRCLED[answer_keys[label][str(question)]]
        if answer_map.get(question) != expected_answer:
            errors.append(
                f"공식 답 불일치: {path} {question}번 "
                f"정본={answer_map.get(question)} 공식={expected_answer}"
            )

    for index, question in enumerate(headings):
        start = re.search(rf"(?m)^##\s+{question}\.\s", question_body)
        if start is None:
            continue
        end_position = len(question_body)
        if index + 1 < len(headings):
            next_heading = re.search(rf"(?m)^##\s+{headings[index + 1]}\.\s", question_body[start.end():])
            if next_heading:
                end_position = start.end() + next_heading.start()
        block = question_body[start.start():end_position]
        for symbol in "①②③④⑤":
            if block.count(symbol) != 1:
                errors.append(
                    f"선지 기호 수 오류: {path} {question}번 {symbol}={block.count(symbol)}"
                )

    if "\ufffd" in text:
        errors.append(f"유니코드 대체문자 포함: {path}")
    for forbidden in ("OCR 초안", "비정본 자동 추출본", "비정본 보조 OCR"):
        if forbidden in text:
            errors.append(f"정본 경로에 비정본 표지 혼입: {path} ({forbidden})")

    page_links = re.findall(r"\[(\d+)쪽\]\(([^)]+)\)", text)
    hash_rows = dict(re.findall(r"(?m)^>\s*(\d+)쪽 SHA-256:\s*`([0-9a-f]{64})`", text))
    official_pages = []
    if not page_links:
        errors.append(f"공식 페이지 링크 없음: {path}")
    for page_number, relative in page_links:
        source = (path.parent / relative).resolve()
        if not source.is_file():
            errors.append(f"공식 페이지 이미지 없음: {path} -> {source}")
            continue
        recorded_hash = hash_rows.get(page_number)
        actual_hash = sha256(source)
        if recorded_hash != actual_hash:
            errors.append(
                f"공식 페이지 해시 불일치: {path} {page_number}쪽 "
                f"기록={recorded_hash} 실제={actual_hash}"
            )
        official_pages.append({
            "display_page": int(page_number),
            "file": str(source.relative_to(Path.cwd())),
            "sha256": actual_hash,
        })

    visual_assets = []
    visual_links = re.findall(r"(?m)^>\s*시각 자료 원본:\s*\[[^]]+\]\(([^)]+)\)", text)
    visual_hashes = re.findall(r"(?m)^>\s*시각 자료 SHA-256:\s*`([0-9a-f]{64})`", text)
    if len(visual_links) != len(visual_hashes):
        errors.append(f"시각 자료 링크·해시 수 불일치: {path}")
    for relative, recorded_hash in zip(visual_links, visual_hashes):
        source = (path.parent / relative).resolve()
        if not source.is_file():
            errors.append(f"시각 자료 원본 없음: {path} -> {source}")
            continue
        actual_hash = sha256(source)
        if recorded_hash != actual_hash:
            errors.append(
                f"시각 자료 해시 불일치: {path} 기록={recorded_hash} 실제={actual_hash}"
            )
        visual_assets.append({
            "file": str(source.relative_to(Path.cwd())),
            "sha256": actual_hash,
        })

    record = {
        "label": label,
        "year": 2005 if label == "2005예비" else int(label),
        "variant": "odd" if label not in {"2011", "2012"} else "single",
        "questions": expected_questions,
        "file": str(path),
        "file_sha256": sha256(path),
        "answers": {str(question): answer_map.get(question) for question in expected_questions},
        "official_pages": official_pages,
        "visual_assets": visual_assets,
        "status": "official_page_visual_transcription_verified",
    }
    return record, errors


def main() -> None:
    answer_payload = json.loads(ANSWER_PATH.read_text(encoding="utf-8"))
    if answer_payload.get("status") != "official_verified":
        raise ValueError("MEET 공식 답 데이터가 검증 상태가 아님")
    answer_keys = answer_payload["keys"]

    records: list[dict] = []
    errors: list[str] = []
    for path in sorted(TRANSCRIPT_DIR.glob("*/q??-??.md")):
        record, record_errors = parse_group(path, answer_keys)
        if record:
            records.append(record)
        errors.extend(record_errors)

    covered = {label: set() for label in EXPECTED}
    for record in records:
        duplicate = covered[record["label"]].intersection(record["questions"])
        if duplicate:
            errors.append(f"중복 문항: {record['label']} {sorted(duplicate)}")
        covered[record["label"]].update(record["questions"])

    progress = {
        label: {
            "verified": len(covered[label]),
            "expected": total,
            "complete": covered[label] == set(range(1, total + 1)),
            "missing": sorted(set(range(1, total + 1)) - covered[label]),
        }
        for label, total in EXPECTED.items()
    }
    verified_total = sum(item["verified"] for item in progress.values())
    expected_total = sum(EXPECTED.values())

    manifest = {
        "status": "official_page_visual_transcription_verified_partial" if verified_total < expected_total else "complete",
        "scope_note": "등록된 문항군만 공식 지면 직접 대조를 완료했다. 미등록 문항의 정본화를 뜻하지 않는다.",
        "record_count": len(records),
        "verified_question_count": verified_total,
        "expected_question_count": expected_total,
        "records": records,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    gate = "PASS_REGISTERED_SCOPE" if not errors else "FAIL"
    result = {
        "gate": gate,
        "errors": errors,
        "records": len(records),
        "verified_questions": verified_total,
        "expected_questions": expected_total,
        "progress": progress,
        "scope_note": "PASS_REGISTERED_SCOPE는 등록된 정본 파일의 무결성 통과만 뜻한다.",
    }
    VERIFY_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# MEET 언어추론 정본 검증 게이트 v1",
        "",
        f"- 등록 범위 자동 검증: **{gate}**",
        f"- 공식 지면 직접 대조 정본: {verified_total}/{expected_total}문항, {len(records)}개 문항군",
        f"- 자동 오류: {len(errors)}개",
        "",
        "> PASS_REGISTERED_SCOPE는 이미 등록된 정본의 문항 연속성, 선지 기호, 공식 답, 원본 이미지 해시가 맞는다는 뜻이다. 전 연도 정본화 완료를 뜻하지 않는다.",
        "",
        "## 연도별 진행률",
        "",
        "| 시험 | 정본 | 전체 | 완료 |",
        "|---|---:|---:|---|",
    ]
    for label, item in progress.items():
        lines.append(f"| {label} | {item['verified']} | {item['expected']} | {'예' if item['complete'] else '아니요'} |")
    lines += ["", "## 자동 오류", ""]
    lines.extend(f"- {error}" for error in errors)
    if not errors:
        lines.append("- 없음")
    lines += [
        "",
        "## 검사 항목",
        "",
        "- 파일명과 문항 제목의 연속성",
        "- 각 문항의 선지 기호 ①~⑤ 각 1회",
        "- 정본 답과 공식 홀수형·단일형 답의 일치",
        "- 공식 페이지 이미지 존재와 SHA-256 일치",
        "- 유니코드 대체문자와 비정본 OCR 경고문 혼입 여부",
    ]
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(gate, f"{verified_total}/{expected_total}", f"errors={len(errors)}")
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
