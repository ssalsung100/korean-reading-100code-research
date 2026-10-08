#!/usr/bin/env python3
"""Persist mechanical cross-group meta control state; never infer semantics."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/기본기_연구"
QUEUE = DATA / "astra_handoff_queue.jsonl"
MANIFEST = DATA / "prepared_backlog/manifest.jsonl"
STATE = DATA / "meta_state.json"

META_FIELDS = {"window_groups","window_cases","strengthened_boundaries","falsification_attempts","revised_boundaries","subtype_candidates","primary_aux_revisions","unresolved_boundaries","next_falsification_targets","generation_principles","confidence","carryover_questions"}
AUDIT_FIELDS = {"for_meta_count","sample_case_ids","dimension_scores","gaps","depth_backfill_case_ids","confidence"}
BACKFILL_FIELDS = {"case_ids","original_blind_preserved","evidence_additions","boundary_or_generation_impact","confidence"}

def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists(): return []
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def _manifest_info(manifest):
    case_ids = {str(x["case_id"]) for x in manifest if x.get("case_id")}
    groups = {}
    for x in manifest:
        if x.get("case_id") and x.get("passage_group"):
            groups.setdefault(str(x["passage_group"]), set()).add(str(x["case_id"]))
    return case_ids, groups

def _done_cases(records, case_ids):
    return {str(r.get("case")) for r in records if str(r.get("case")) in case_ids and r.get("stage") == "sdss_compare" and r.get("status") == "done"}

def _counts(records, manifest):
    case_ids, group_members = _manifest_info(manifest)
    complete_cases = _done_cases(records, case_ids)
    complete_groups = {g for g, members in group_members.items() if members and members <= complete_cases}
    return complete_cases, complete_groups

def _explicit_ids(value):
    if isinstance(value, str): return {value}
    if isinstance(value, list): return {str(x) for x in value if isinstance(x, (str, int))}
    return set()

def calculate_state(records, manifest, old=None):
    """Pure production calculation, injectable for fixture tests."""
    old = old or {}
    case_ids, group_members = _manifest_info(manifest)
    complete_cases, complete_groups = _counts(records, manifest)
    raw_metas = [r for r in records if r.get("stage") == "meta_induction" and r.get("status") == "done"]
    valid_metas = [r for r in raw_metas if META_FIELDS <= set(r.get("payload", {}))]
    valid_indexes = [i for i, r in enumerate(records) if r.get("stage") == "meta_induction" and r.get("status") == "done" and META_FIELDS <= set(r.get("payload", {}))]
    latest_index = valid_indexes[-1] if valid_indexes else None
    latest = records[latest_index] if latest_index is not None else None
    latest_id = latest.get("record_id") if latest else old.get("last_meta_induction_id")
    if latest_index is not None:
        prefix_cases, prefix_groups = _counts(records[:latest_index], manifest)
        baseline_groups, baseline_questions = len(prefix_groups), len(prefix_cases)
        post_meta_incomplete = any(i > latest_index and r.get("stage") == "meta_induction" and r.get("status") == "done" and not META_FIELDS <= set(r.get("payload", {})) for i, r in enumerate(records))
    else:
        baseline_groups = int(old.get("baseline_completed_groups", 0))
        baseline_questions = int(old.get("baseline_completed_questions", 0))
        post_meta_incomplete = bool(raw_metas)
    meta_due = bool(post_meta_incomplete or old.get("meta_due", False)) if latest_index is None else bool(post_meta_incomplete)
    groups_since = max(0, len(complete_groups) - baseline_groups)
    questions_since = max(0, len(complete_cases) - baseline_questions)
    if groups_since >= 3 or questions_since >= 12: meta_due = True

    review = list(old.get("semantic_state_review", []))
    review.extend(f"{r.get('record_id')}:incomplete_meta" for r in raw_metas if r not in valid_metas)
    targets, unresolved = old.get("next_falsification_targets", []), old.get("unresolved_boundaries", [])
    if latest:
        payload = latest.get("payload", {})
        if "next_falsification_targets" in payload: targets = payload["next_falsification_targets"]
        else: review.append(f"{latest.get('record_id')}:missing next_falsification_targets")
        if "unresolved_boundaries" in payload: unresolved = payload["unresolved_boundaries"]
        else: review.append(f"{latest.get('record_id')}:missing unresolved_boundaries")

    meta_count = len(valid_metas)
    last_audited = int(old.get("last_manual_parity_audited_meta_count", 0))
    pending = set(str(x) for x in old.get("depth_backfill_pending", []))
    for r in records:
        payload = r.get("payload", {})
        valid_audit_target = isinstance(payload.get("for_meta_count"), int) and 0 < payload.get("for_meta_count") <= meta_count
        if r.get("stage") == "manual_parity_audit" and r.get("status") == "done" and AUDIT_FIELDS <= set(payload) and valid_audit_target:
            last_audited = max(last_audited, payload["for_meta_count"])
            pending |= _explicit_ids(payload.get("depth_backfill_case_ids"))
        if r.get("stage") == "depth_backfill" and r.get("status") == "done" and BACKFILL_FIELDS <= set(payload):
            pending -= _explicit_ids(payload.get("case_ids"))
    debt = meta_count - last_audited
    return {"schema_version": 2, "last_meta_induction_id": latest_id, "baseline_completed_groups": baseline_groups, "baseline_completed_questions": baseline_questions, "completed_passage_groups_total": len(complete_groups), "completed_questions_total": len(complete_cases), "completed_groups_since_last_meta": groups_since, "completed_questions_since_last_meta": questions_since, "meta_due": meta_due, "meta_induction_count": meta_count, "last_manual_parity_audited_meta_count": last_audited, "manual_parity_audit_due": debt >= 3, "manual_parity_audits_remaining_to_next": max(0, 3 - debt), "next_falsification_targets": targets, "unresolved_boundaries": unresolved, "depth_backfill_pending": sorted(pending), "semantic_state_review": sorted(set(review)), "completed_group_ids": sorted(complete_groups), "completed_case_ids": sorted(complete_cases)}

def sync():
    old = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    state = calculate_state(read_jsonl(QUEUE), read_jsonl(MANIFEST), old)
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return state

if __name__ == "__main__":
    print(json.dumps(sync(), ensure_ascii=False, indent=2))
