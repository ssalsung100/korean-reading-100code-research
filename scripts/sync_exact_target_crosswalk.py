#!/usr/bin/env python3
"""Synchronize only mechanically exact consumed-source links into target crosswalks.

This touches the two crosswalk JSONL files only. It never reads answer/SDSS
content, research judgments, or writes semantic ledgers.
"""
import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/기본기_연구"
BACKLOG = DATA / "prepared_backlog"
TARGET = DATA / "target_completion_crosswalk_v1.jsonl"
RESEARCH = DATA / "research_case_target_crosswalk_v1.jsonl"


def rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def atomic_jsonl(path, values):
    text = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in values)
    with NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(text)
        temp = Path(handle.name)
    os.replace(temp, path)


def normalize_exam(family, label):
    s = "".join(str(label or "").replace("국어", "").split()).replace("_", "")
    if family == "KICE":
        s = s.replace("6평", "6월모평").replace("9평", "9월모평")
        if s.endswith("A형") or s.endswith("B형"):
            s = s[:-2] + s[-2]
    return s


def main():
    targets = rows(TARGET)
    research = rows(RESEARCH)
    candidates = rows(DATA / "code_study_candidates_v2.jsonl")
    manifest = rows(BACKLOG / "manifest.jsonl")
    provenance = rows(BACKLOG / "sealed/provenance_mapping.jsonl")

    target_by_candidate = {x["candidate_id"]: x for x in targets}
    candidate_by_id = {x["candidate_id"]: x for x in candidates}
    provenance_by_case = {x["case_id"]: x.get("provenance", {}) for x in provenance}
    research_by_case = {x["case_id"]: x for x in research}
    if len(target_by_candidate) != len(targets) or len(candidate_by_id) != len(candidates):
        raise SystemExit("candidate_id duplicate in target or candidate index")

    consumed = [x for x in manifest if x.get("status") == "consumed_sdss"]
    additions = []
    target_updates = {}
    conflicts = []
    for item in consumed:
        case_id = item["case_id"]
        p = provenance_by_case.get(case_id, {})
        candidate_id = p.get("candidate_id")
        if not candidate_id:
            continue
        target = target_by_candidate.get(candidate_id)
        candidate = candidate_by_id.get(candidate_id)
        if not target or not candidate:
            conflicts.append((case_id, candidate_id, "candidate linkage missing"))
            continue
        if target["status"] == "COMPLETED_TARGET" and target.get("matched_case_id") == case_id:
            linked = research_by_case.get(case_id)
            if linked and linked.get("candidate_id") == candidate_id:
                # Exact candidate linkage is already synchronized even when an
                # older target row lacks a canonical question-id field.
                continue
        qid = p.get("question_id")
        passage_id = p.get("passage_id")
        cc = candidate.get("canonical_connection", {})
        if not qid or qid != target.get("target_question_id") or qid != cc.get("question_id"):
            conflicts.append((case_id, candidate_id, "question_id exact-link mismatch"))
            continue
        if not passage_id or passage_id != cc.get("passage_id"):
            conflicts.append((case_id, candidate_id, "passage_id exact-link mismatch"))
            continue
        if target["status"] in ("HOLD", "AMBIGUOUS_COMPLETION"):
            conflicts.append((case_id, candidate_id, f"protected target status={target['status']}"))
            continue
        if target["status"] == "COMPLETED_TARGET":
            if target.get("matched_case_id") != case_id:
                conflicts.append((case_id, candidate_id, "already completed by another case"))
            continue
        if case_id in research_by_case:
            continue

        coordinate = target["target_source_coordinate"]
        family = coordinate.get("exam_family")
        year = coordinate.get("year")
        raw_label = coordinate.get("exam_label")
        qnum = coordinate.get("question_number")
        normalized = normalize_exam(family, raw_label)
        hits = {key: [candidate_id] for key in ("candidate_id", "question_id", "source_coordinate", "passage_question")}
        match_evidence = {
            "matched_candidate_id": candidate_id,
            "matched_target_question_id": qid,
            "matched_target_passage_id": passage_id,
            "matched_target_coordinate": {
                "exam_family": family,
                "year": year,
                "normalized_exam_label": normalized,
                "raw_exam_label": raw_label,
                "question_number": qnum,
            },
            "case_provenance_question_id": qid,
            "case_source_ids": [x for x in [p.get("canonical_source_path"), p.get("source_path")] if x],
            "case_question_ids": [qid],
            "exact_identifier_hits": hits,
            "provenance_source_type": p.get("source_type"),
            "sealed_source_role": "sealed_provenance_mapping",
        }
        target_updates[candidate_id] = {
            **target,
            "status": "COMPLETED_TARGET",
            "matched_case_id": case_id,
            "matched_passage_group": item["passage_group"],
            "match_method": "candidate_id_exact",
            "match_evidence": {
                "consumed_case_ids": [case_id],
                "consumed_case_count": 1,
                "case_match_evidence": match_evidence,
                "previous_source_preflight_status": target["status"].removeprefix("NOT_COMPLETED_")
                if target["status"].startswith("NOT_COMPLETED_") else target["status"],
            },
            "confidence": "high",
            "ambiguity_reason": None,
            "duplicate_history_case_ids": [],
        }
        additions.append({
            "case_id": case_id,
            "research_passage_group": item["passage_group"],
            "status": "TARGET_MATCHED",
            "candidate_id": candidate_id,
            "match_method": "candidate_id_exact",
            "evidence": match_evidence,
            "canonical_question_id": qid,
            "canonical_passage_id": passage_id,
            "source_coordinate": {
                "exam_family": family,
                "year": year,
                "normalized_exam_label": normalized,
                "raw_exam_label": raw_label,
                "question_number": qnum,
            },
            "source_path": p.get("canonical_source_path") or p.get("source_path"),
            "legacy_source_ids": [],
            "raw_question_ids": [],
            "original_source_ids": [],
            "local_canonical_id": target.get("local_canonical_id"),
            "case_document_question_id_mentions": [],
            "case_document_candidate_id_mentions": [],
            "case_document_files": [],
        })

    if conflicts:
        raise SystemExit("exact-link conflict; no crosswalk files changed: " + repr(conflicts[:20]))
    if len({x["case_id"] for x in additions}) != len(additions):
        raise SystemExit("duplicate case in proposed research crosswalk additions")
    if len({x["candidate_id"] for x in additions}) != len(additions):
        raise SystemExit("duplicate candidate in proposed crosswalk additions")
    if any(x["case_id"] in research_by_case for x in additions):
        raise SystemExit("research crosswalk overlap; no files changed")

    updated_targets = [target_updates.get(x["candidate_id"], x) for x in targets]
    updated_research = research + additions
    # Verify all consumed source mappings now have exactly one research row and
    # every completed target still has an exact one-to-one research link.
    if len({x["case_id"] for x in updated_research}) != len(updated_research):
        raise SystemExit("research case duplicate after sync")
    target_lookup = {x["candidate_id"]: x for x in updated_targets}
    research_lookup = {x["case_id"]: x for x in updated_research}
    for row in updated_targets:
        if row["status"] == "COMPLETED_TARGET":
            linked = research_lookup.get(row.get("matched_case_id"))
            if not linked or linked.get("candidate_id") != row["candidate_id"] or linked.get("status") != "TARGET_MATCHED":
                raise SystemExit("completed target lacks exact research crosswalk link")

    atomic_jsonl(TARGET, updated_targets)
    atomic_jsonl(RESEARCH, updated_research)
    print(json.dumps({
        "exact_completion_rows_added": len(additions),
        "target_crosswalk_rows": len(updated_targets),
        "research_crosswalk_rows": len(updated_research),
        "target_completed": sum(x["status"] == "COMPLETED_TARGET" for x in updated_targets),
        "completed_target_delta": len(additions),
        "semantic_ledgers_modified": False,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
