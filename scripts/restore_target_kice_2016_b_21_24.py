#!/usr/bin/env python3
"""Restore the exact official-local 2016 KICE B형 questions 21–24.

Source-preparation only: reads the two official question pages (PDF indices 39–40)
from the local problem archive. It does not read an answer key or candidate labels.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from tempfile import NamedTemporaryFile

import fitz

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/기본기_연구/prepared_backlog"
TARGET = ROOT / "data/기본기_연구/target_completion_crosswalk_v1.jsonl"
MANIFEST = BASE / "manifest.jsonl"
MAPPING = BASE / "sealed/provenance_mapping.jsonl"
ANSWERS = BASE / "sealed/answer_sdss.jsonl"
RESTORE_LOG = BASE / "sealed/source_restorations_v1.jsonl"
PDF = BASE / "sealed/G086_official_provenance/2016_KICE_Korean_B_problem_and_answer_archive.pdf"
RULES = [
    "all_group_blind_records_before_any_group_answer_check",
    "all_group_independent_code_records_before_any_group_sdss_disclosure",
]
QID_PREFIX = "KICE-2016-수능국어B형-Q21-24"


def read_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def alpha_value(value: str) -> int:
    result = 0
    for char in value:
        result = result * 26 + ord(char) - 64
    return result


def alpha(value: int) -> str:
    out = ""
    n = value
    while n:
        n -= 1
        out = chr(65 + n % 26) + out
        n //= 26
    return out


def atomic_jsonl(path: Path, rows):
    data = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    with NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(data)
        temp = Path(handle.name)
    os.replace(temp, path)


def extract_problem_pages():
    pdf_bytes = PDF.read_bytes()
    digest = hashlib.sha256(pdf_bytes).hexdigest()
    document = fitz.open(stream=pdf_bytes, filetype="pdf")
    # Only official question pages 40–41 in the local archive are accessed;
    # no answer-table or later archive pages are read.
    passage_page = document[39].get_text().replace("\r\n", "\n")
    question_page = document[40].get_text().replace("\r\n", "\n")
    range_match = re.search(r"^\[21\s*[～~〜-]\s*24\][^\n]*$", passage_page, re.M)
    if not range_match:
        raise ValueError("official question page lacks the exact [21～24] passage anchor")
    after_anchor = passage_page[range_match.end():]
    passage = after_anchor.strip()
    heads = list(re.finditer(r"^\s*(2[1-4])\.\s*", question_page, re.M))
    if [int(match.group(1)) for match in heads] != [21, 22, 23, 24]:
        raise ValueError("official question page does not link exactly questions 21–24")
    questions = []
    for i, head in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(question_page)
        block = question_page[head.start():end]
        if i == len(heads) - 1:
            next_range = re.search(r"^\[25\s*[～~〜-]", block, re.M)
            if next_range:
                block = block[:next_range.start()]
        labels = list(re.finditer(r"^\s*([①②③④⑤])\s*(.*)$", block, re.M))
        if [m.group(1) for m in labels] != ["①", "②", "③", "④", "⑤"]:
            raise ValueError(f"official choice sequence incomplete for question {head.group(1)}")
        stem = block[:labels[0].start()].strip()
        stem = re.sub(r"^\s*2[1-4]\.\s*", "", stem, count=1)
        choices = []
        for j, label in enumerate(labels):
            stop = labels[j + 1].start() if j + 1 < len(labels) else len(block)
            continuation = block[label.end():stop]
            text = " ".join([label.group(2).strip(), *continuation.splitlines()])
            choices.append(f"{label.group(1)} {' '.join(text.split())}".strip())
        if not stem or any(not choice for choice in choices):
            raise ValueError(f"empty stem or choice for question {head.group(1)}")
        questions.append({"question_number": int(head.group(1)), "stem": stem, "choices": choices})
    if len(passage) < 500:
        raise ValueError("passage text unexpectedly short")
    if re.search(r"<(?:그림|표)>|!\[", passage + "\n" + "\n".join(q["stem"] + "\n" + "\n".join(q["choices"]) for q in questions)):
        raise ValueError("unresolved visual placeholder remains in the official question-page extraction")
    return passage, questions, digest


def main():
    targets = read_jsonl(TARGET)
    candidates = read_jsonl(ROOT / "data/기본기_연구/code_study_candidates_v2.jsonl")
    manifest = read_jsonl(MANIFEST)
    mappings = read_jsonl(MAPPING)
    answers = read_jsonl(ANSWERS)
    restore_log = read_jsonl(RESTORE_LOG) if RESTORE_LOG.exists() else []
    candidate_by_id = {row["candidate_id"]: row for row in candidates}
    target_by_id = {row["candidate_id"]: row for row in targets}

    matched = []
    for candidate in candidates:
        source = candidate.get("source", {})
        if (source.get("exam_family"), source.get("year"), source.get("exam_type"), source.get("question_number")) in {
            ("KICE", 2016, "수능국어B형", number) for number in range(21, 25)
        }:
            matched.append(candidate)
    matched.sort(key=lambda row: row["source"]["question_number"])
    if len(matched) != 4 or [row["source"]["question_number"] for row in matched] != [21, 22, 23, 24]:
        raise ValueError("candidate index does not identify exactly KICE 2016 B형 questions 21–24")
    candidate_ids = [row["candidate_id"] for row in matched]
    if len(set(candidate_ids)) != 4 or any(candidate_id not in target_by_id for candidate_id in candidate_ids):
        raise ValueError("candidate-to-target linkage is incomplete or duplicated")
    for row in matched:
        if target_by_id[row["candidate_id"]].get("status") != "NOT_COMPLETED_SOURCE_MISSING":
            raise ValueError("target status changed; refusing to overwrite an existing completion/hold state")

    passage, questions, pdf_sha = extract_problem_pages()
    max_group = max(int(str(row.get("passage_group", "G000")).removeprefix("G")) for row in manifest)
    group_id = f"G{max_group + 1:03d}"
    used_case_values = [alpha_value(row["case_id"]) for row in manifest if re.fullmatch(r"[A-Z]+", row.get("case_id", ""))]
    next_case = max(used_case_values) + 1
    case_ids = [alpha(next_case + i) for i in range(4)]
    source_rel = PDF.relative_to(ROOT).as_posix()
    question_ids = [f"{QID_PREFIX}-Q{number}" for number in range(21, 25)]
    blind_paths = [BASE / "blind_sources" / f"{case_id}.json" for case_id in case_ids]
    packet_md_paths = [BASE / "packets" / f"{case_id}.md" for case_id in case_ids]
    packet_json_path = BASE / "packets" / f"{case_ids[0]}.json"
    planned = blind_paths + packet_md_paths + [packet_json_path]
    if any(path.exists() for path in planned):
        raise FileExistsError("a planned case or packet path already exists")
    if any(case_id in {row["case_id"] for row in manifest} for case_id in case_ids):
        raise ValueError("case identifier collision")
    if any(row["case_id"] == case_ids[i] for row in mappings for i in range(4)):
        raise ValueError("provenance mapping case collision")

    blind_records, mapping_rows, answer_rows, manifest_rows = [], [], [], []
    target_updates = {row["candidate_id"]: dict(target_by_id[row["candidate_id"]]) for row in matched}
    for i, candidate in enumerate(matched):
        case_id = case_ids[i]
        q = questions[i]
        qid = question_ids[i]
        blind = {
            "blind_only": True,
            "passage_group": group_id,
            "case_id": case_id,
            "provenance": {"source_role": "anonymous_blind_source"},
            "passage_text": passage,
            "stem": q["stem"],
            "choices": q["choices"],
        }
        blind_records.append(blind)
        mapping_rows.append({
            "case_id": case_id,
            "passage_group": group_id,
            "group_case_ids": case_ids,
            "provenance": {
                "candidate_id": candidate["candidate_id"],
                "exam_family": "KICE",
                "academic_year": 2016,
                "exam_label": "수능국어B형",
                "question_number": q["question_number"],
                "question_id": qid,
                "passage_id": QID_PREFIX,
                "source_path": source_rel,
                "canonical_source_path": source_rel,
                "source_sha256": pdf_sha,
                "source_type": "official_kice_question_pdf_page_extract",
                "official_pages": [
                    {"file": source_rel, "pdf_page_index": 39, "scope": "2016 KICE 국어 B형 홀수형 Q21~24 공통 지문", "sha256": pdf_sha},
                    {"file": source_rel, "pdf_page_index": 40, "scope": f"2016 KICE 국어 B형 홀수형 Q{q['question_number']} stem and five choices", "sha256": pdf_sha},
                ],
                "linked_visual_assets": [],
                "source_role": "sealed_provenance_mapping",
            },
            "source_status": "official_local_kice_pdf_page_extract",
        })
        answer_rows.append({
            "case_id": case_id,
            "candidate_id": candidate["candidate_id"],
            "official_answer": None,
            "official_answer_source": "not accessed during source preparation; resolve after group blind barrier",
            "site_original_codes": None,
            "site_marked_answer": None,
            "source_role": "sealed_for_after_blind",
            "passage_group": group_id,
            "release_rule": RULES[0],
        })
        manifest_rows.append({
            "case_id": case_id,
            "status": "prepared",
            "passage_group": group_id,
            "group_case_ids": case_ids,
            "group_release_rules": RULES,
            "blind_source": f"data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json",
            "exclusion_checks": {
                "exposure_status": "unknown",
                "semantic_review": "not_reviewed",
                "source_quality": {
                    "visual_placeholder": False,
                    "canonical_link": "exact_official_local_pdf_page_extract",
                    "choice_parse": "five_official_choices_per_question",
                    "text_markers_preserved": True,
                    "source_verification": "official_local_kice_question_pdf_pages_39_40",
                },
            },
        })
        target = target_updates[candidate["candidate_id"]]
        target["status"] = "NOT_COMPLETED_READY_LOCAL_SOURCE"
        target["local_canonical_id"] = qid
        target["match_method"] = "source_preflight_official_local_pdf"
        target["match_evidence"] = {
            **(target.get("match_evidence") or {}),
            "previous_source_preflight_status": "SOURCE_MISSING",
            "source_restored_from": source_rel,
            "source_pages": [39, 40],
            "source_scope": f"common passage and question {q['question_number']} only",
            "blind_source_linkage": "exact candidate_id + exam family/year/type/question number",
        }
        target["matched_case_id"] = None
        target["matched_passage_group"] = None
    packet = {
        "blind_packet": True,
        "passage_group": group_id,
        "group_case_ids": case_ids,
        "group_release_rules": RULES,
        "source_files": [f"data/기본기_연구/prepared_backlog/blind_sources/{x}.json" for x in case_ids],
    }

    forbidden = re.compile(r"answer|sdss|candidate_id|site_|code|explanation|solution|correct|정답|해설|코드", re.I)
    for source in blind_records:
        if set(source) - {"blind_only", "passage_group", "case_id", "provenance", "passage_text", "stem", "choices"}:
            raise ValueError("blind source contains an unexpected metadata field")
        if source["provenance"] != {"source_role": "anonymous_blind_source"}:
            raise ValueError("blind provenance is not anonymous")
        if any(forbidden.search(key) for key in source):
            raise ValueError("blind source metadata contains an answer/SDSS/identity key")
        if not source["passage_text"].strip() or not source["stem"].strip():
            raise ValueError("empty passage or stem")
        if len(source["choices"]) != 5 or any(not choice.strip() for choice in source["choices"]):
            raise ValueError("invalid five-choice source")
        if re.search(r"<(?:그림|표)>|!\[", source["stem"] + source["passage_text"] + "\n".join(source["choices"])):
            raise ValueError("unresolved visual placeholder")

    # Verify that the page extracts point to the exact questions and the four
    # candidate coordinates before writing any source or status row.
    for i, candidate in enumerate(matched):
        if candidate["source"].get("question_number") != questions[i]["question_number"]:
            raise ValueError("candidate/question number linkage mismatch")
        if candidate["candidate_id"] != target_updates[candidate["candidate_id"]]["candidate_id"]:
            raise ValueError("candidate id linkage mismatch")

    for path, record in zip(blind_paths, blind_records):
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for path, case_id in zip(packet_md_paths, case_ids):
        text = (
            f"# {case_id} blind packet\n\n"
            f"- passage_group: {group_id}\n- group_case_ids: {', '.join(case_ids)}\n"
            f"- blind_source: data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json\n"
            f"- group_rules: {'; '.join(RULES)}\n\n"
            "Astra는 동일 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.\n"
        )
        path.write_text(text, encoding="utf-8")
    packet_json_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    atomic_jsonl(MAPPING, mappings + mapping_rows)
    atomic_jsonl(ANSWERS, answers + answer_rows)
    atomic_jsonl(MANIFEST, manifest + manifest_rows)
    atomic_jsonl(TARGET, [target_updates.get(x["candidate_id"], x) for x in targets])
    atomic_jsonl(RESTORE_LOG, restore_log + [{
        "passage_group": group_id,
        "case_ids": case_ids,
        "candidate_ids": candidate_ids,
        "source_path": source_rel,
        "sha256": pdf_sha,
        "pdf_page_indices": [39, 40],
        "scope": "official question pages only; no answer/SDSS/explanation pages read",
        "status": "official_local_kice_question_source_restored",
    }])
    print(json.dumps({
        "restored_group": group_id,
        "case_ids": case_ids,
        "questions": len(manifest_rows),
        "source_pdf_pages": [39, 40],
        "source_sha256": pdf_sha,
        "official_answer_accessed": False,
        "sdss_accessed": False,
        "target_completed_delta": 0,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
