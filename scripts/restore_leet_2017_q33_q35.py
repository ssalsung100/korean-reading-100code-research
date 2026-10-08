#!/usr/bin/env python3
"""Prepare the exact 2017 LEET Q33/Q35 Markdown targets.

The canonical Markdown contains the full passage, stems, and choices. Its
single terminal <표> is outside Q35; the official rendered page had previously
been checked and shows only the standard administrative confirmation box
after the question. That non-question footer is omitted from blind sources.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from tempfile import NamedTemporaryFile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/기본기_연구/prepared_backlog"
TARGET = ROOT / "data/기본기_연구/target_completion_crosswalk_v1.jsonl"
MANIFEST = BASE / "manifest.jsonl"
MAPPING = BASE / "sealed/provenance_mapping.jsonl"
ANSWERS = BASE / "sealed/answer_sdss.jsonl"
RESTORATIONS = BASE / "sealed/source_restorations_v1.jsonl"
SOURCE = ROOT / "자료/LEET_언어이해/텍스트/2017/2017_question_odd.md"
SOURCE_REL = SOURCE.relative_to(ROOT).as_posix()
PASSAGE_ID = "LEET-2017-odd-Q33-35"
WANTED = {33, 35}
RULES = [
    "all_group_blind_records_before_any_group_answer_check",
    "all_group_independent_code_records_before_any_group_sdss_disclosure",
]


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_atomic(path: Path, data: bytes):
    with NamedTemporaryFile("wb", dir=path.parent, delete=False) as handle:
        handle.write(data)
        temp = Path(handle.name)
    os.replace(temp, path)


def jsonl(rows):
    return "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows).encode("utf-8")


def alpha_value(value):
    number = 0
    for char in value:
        number = number * 26 + ord(char) - 64
    return number


def alpha(number):
    result = ""
    while number:
        number, rem = divmod(number - 1, 26)
        result = chr(65 + rem) + result
    return result


def parse_group(markdown: str):
    ranges = list(re.finditer(r"^\[(\d+)\s*[~～〜-]\s*(\d+)\][^\n]*$", markdown, re.M))
    anchors = [i for i, row in enumerate(ranges) if (int(row[1]), int(row[2])) == (33, 35)]
    if len(anchors) != 1:
        raise ValueError("exact [33~35] canonical passage anchor missing")
    i = anchors[0]
    anchor = ranges[i]
    end = ranges[i + 1].start() if i + 1 < len(ranges) else len(markdown)
    block = markdown[anchor.end():end]
    if not re.search(r"\n\s*<표>\s*$", block):
        raise ValueError("expected one terminal <표> footer marker")
    block = re.sub(r"\n\s*<표>\s*$", "\n", block)
    heads = list(re.finditer(r"^\s*(3[3-5])\.\s*", block, re.M))
    if [int(m[1]) for m in heads] != [33, 34, 35]:
        raise ValueError("exact Q33–35 question linkage missing")
    passage = block[:heads[0].start()].strip()
    questions = {}
    for j, head in enumerate(heads):
        stop = heads[j + 1].start() if j + 1 < len(heads) else len(block)
        body = block[head.end():stop].strip()
        labels = list(re.finditer(r"([①②③④⑤])\s*", body))
        if [m[1] for m in labels] != ["①", "②", "③", "④", "⑤"]:
            raise ValueError(f"choice sequence incomplete at Q{head[1]}")
        stem = body[:labels[0].start()].strip()
        choices = [body[m.end():labels[k + 1].start() if k + 1 < len(labels) else len(body)].strip()
                   for k, m in enumerate(labels)]
        if not stem or any(not x for x in choices) or re.search(r"<(?:그림|표)>|!\[", stem + passage + "".join(choices)):
            raise ValueError(f"source text or visual marker incomplete at Q{head[1]}")
        questions[int(head[1])] = {"stem": stem, "choices": choices}
    return passage, questions


def main():
    candidates = read_jsonl(ROOT / "data/기본기_연구/code_study_candidates_v2.jsonl")
    targets = read_jsonl(TARGET)
    manifest = read_jsonl(MANIFEST)
    mappings = read_jsonl(MAPPING)
    answers = read_jsonl(ANSWERS)
    restoration_rows = read_jsonl(RESTORATIONS) if RESTORATIONS.exists() else []
    by_candidate = {row["candidate_id"]: row for row in candidates}
    target_by_id = {row["candidate_id"]: row for row in targets}
    selected = []
    for candidate in candidates:
        src, conn = candidate.get("source", {}), candidate.get("canonical_connection", {})
        if (src.get("exam_family"), src.get("year"), src.get("question_number"), conn.get("passage_id")) in {
            ("LEET", 2017, qn, PASSAGE_ID) for qn in WANTED
        }:
            selected.append(candidate)
    selected.sort(key=lambda row: row["source"]["question_number"])
    if [row["source"]["question_number"] for row in selected] != [33, 35]:
        raise ValueError("candidate index does not identify exactly Q33 and Q35")
    for candidate in selected:
        if candidate["candidate_id"] not in target_by_id or target_by_id[candidate["candidate_id"]].get("status") != "NOT_COMPLETED_NEEDS_RESTORE":
            raise ValueError("target is protected or changed; refusing to overwrite")
    passage, questions = parse_group(SOURCE.read_text(encoding="utf-8"))

    group_number = max(int(str(row.get("passage_group", "G000")).removeprefix("G")) for row in manifest) + 1
    group_id = f"G{group_number:03d}"
    case_start = max((alpha_value(row["case_id"]) for row in manifest if re.fullmatch(r"[A-Z]+", row.get("case_id", ""))), default=0) + 1
    case_ids = [alpha(case_start + i) for i in range(2)]
    paths = [BASE / "blind_sources" / f"{case_id}.json" for case_id in case_ids]
    paths += [BASE / "packets" / f"{case_id}.md" for case_id in case_ids]
    paths += [BASE / "packets" / f"{case_ids[0]}.json"]
    if any(path.exists() for path in paths):
        raise FileExistsError("blind/packet output path conflict")
    if set(case_ids) & {row["case_id"] for row in manifest}:
        raise ValueError("case ID collision")
    old_candidate_ids = {row.get("provenance", {}).get("candidate_id") for row in mappings}
    if any(row["candidate_id"] in old_candidate_ids for row in selected):
        raise ValueError("candidate already present in provenance; refusing duplicate")

    source_bytes = SOURCE.read_bytes()
    source_hash = hashlib.sha256(source_bytes).hexdigest()
    blind_rows, map_rows, answer_rows, manifest_rows, updated_targets = [], [], [], [], []
    for i, candidate in enumerate(selected):
        qn, case_id = candidate["source"]["question_number"], case_ids[i]
        q = questions[qn]
        blind = {"blind_only": True, "passage_group": group_id, "case_id": case_id,
                 "provenance": {"source_role": "anonymous_blind_source"},
                 "passage_text": passage, "stem": q["stem"], "choices": q["choices"]}
        if set(blind) != {"blind_only", "passage_group", "case_id", "provenance", "passage_text", "stem", "choices"}:
            raise ValueError("unexpected blind metadata")
        blind_rows.append((BASE / "blind_sources" / f"{case_id}.json", blind))
        conn = candidate["canonical_connection"]
        map_rows.append({"case_id": case_id, "passage_group": group_id, "group_case_ids": case_ids,
                         "provenance": {"candidate_id": candidate["candidate_id"], "exam_family": "LEET",
                           "academic_year": 2017, "exam_label": candidate["source"]["exam_type"],
                           "question_number": qn, "question_id": conn["question_id"], "passage_id": PASSAGE_ID,
                           "source_path": SOURCE_REL, "canonical_source_path": SOURCE_REL,
                           "source_sha256": source_hash, "source_type": "canonical_leet_odd_markdown",
                           "official_pages": [], "linked_visual_assets": [], "source_role": "sealed_provenance_mapping"},
                         "source_status": "exact_canonical_leet_odd"})
        answer_rows.append({"case_id": case_id, "candidate_id": candidate["candidate_id"],
                            "official_answer": None,
                            "official_answer_source": "not accessed during source preparation; resolve after group blind barrier",
                            "site_original_codes": None, "site_marked_answer": None,
                            "source_role": "sealed_for_after_blind", "passage_group": PASSAGE_ID,
                            "release_rule": RULES[0]})
        manifest_rows.append({"case_id": case_id, "status": "prepared", "passage_group": group_id,
                              "group_case_ids": case_ids, "group_release_rules": RULES,
                              "blind_source": f"data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json",
                              "exclusion_checks": {"exposure_status": "unknown", "semantic_review": "not_reviewed",
                                "source_quality": {"visual_placeholder": False, "canonical_link": "exact",
                                  "choice_parse": "complete", "text_markers_preserved": True,
                                  "source_verification": "exact_canonical_leet_odd_markdown_terminal_admin_marker_excluded"}}})
        target = dict(target_by_id[candidate["candidate_id"]])
        target["status"] = "NOT_COMPLETED_READY_LOCAL_SOURCE"
        target["match_method"] = "canonical_markdown_exact_question_terminal_admin_marker_excluded"
        target["match_evidence"] = {**(target.get("match_evidence") or {}),
            "previous_source_preflight_status": "NEEDS_RESTORE", "source_path": SOURCE_REL,
            "source_sha256": source_hash,
            "footer_marker_disposition": "terminal <표> excluded as non-question administrative confirmation box, verified from official local page",
            "blind_linkage": "exact candidate_id + canonical question_id + passage range"}
        target["matched_case_id"] = None
        target["matched_passage_group"] = None
        updated_targets.append(target)

    packet = {"blind_packet": True, "passage_group": group_id, "group_case_ids": case_ids,
              "group_release_rules": RULES,
              "source_files": [f"data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json" for case_id in case_ids]}
    packet_md = "\n".join([f"# Blind source packet — {group_id}", "",
                           "all_group_blind_records_before_any_group_answer_check",
                           "all_group_independent_code_records_before_any_group_sdss_disclosure", "",
                          *[f"- {case_id}: `data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json`" for case_id in case_ids], ""])
    updates = {row["candidate_id"]: row for row in updated_targets}
    next_targets = [updates.get(row["candidate_id"], row) for row in targets]
    restore = {"passage_group": group_id, "family": "LEET", "year": 2017, "question_range": [33, 35],
               "selected_text_source": SOURCE_REL, "source_sha256": source_hash,
               "terminal_marker": "<표>", "terminal_marker_disposition": "excluded after official page verification as administrative confirmation box outside Q35",
               "case_ids": case_ids, "restoration_type": "source_preparation_only"}
    next_manifest = manifest + manifest_rows
    next_mappings = mappings + map_rows
    next_answers = answers + answer_rows
    next_restores = restoration_rows + [restore]
    writes = []
    for path, blind in blind_rows:
        writes.append((path, (json.dumps(blind, ensure_ascii=False, indent=2) + "\n").encode("utf-8")))
        packet_path = BASE / "packets" / f"{blind['case_id']}.md"
        writes.append((packet_path, packet_md.encode("utf-8")))
    writes.append((BASE / "packets" / f"{case_ids[0]}.json", (json.dumps(packet, ensure_ascii=False, indent=2) + "\n").encode("utf-8")))
    writes.extend([(MANIFEST, jsonl(next_manifest)), (MAPPING, jsonl(next_mappings)),
                   (ANSWERS, jsonl(next_answers)), (TARGET, jsonl(next_targets)),
                   (RESTORATIONS, jsonl(next_restores))])
    if len({path for path, _ in writes}) != len(writes):
        raise ValueError("output path collision")
    for path, data in writes:
        write_atomic(path, data)
    print(json.dumps({"prepared_groups": 1, "prepared_questions": len(case_ids), "group": group_id,
                      "case_ids": case_ids, "candidate_ids": [row["candidate_id"] for row in selected],
                      "answer_or_SDSS_used": False}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
