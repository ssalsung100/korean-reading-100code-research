#!/usr/bin/env python3
"""Production-logic fixture tests; no repository queue/manifest is modified."""
from __future__ import annotations
import copy
from meta_state import META_FIELDS, AUDIT_FIELDS, BACKFILL_FIELDS, calculate_state

def manifest(groups):
    return [{"case_id": case, "passage_group": group} for group, cases in groups.items() for case in cases]

def sdss(case, status="done"):
    return {"case": case, "stage": "sdss_compare", "status": status, "payload": {"passage_group": "fixture"}}

def meta(i, targets=None, unresolved=None):
    payload = {key: [] for key in META_FIELDS}
    payload.update(record_id=f"META-{i}", next_falsification_targets=targets or [f"target-{i}"], unresolved_boundaries=unresolved or [])
    return {"record_id": f"META-{i}", "case": "META", "stage": "meta_induction", "status": "done", "payload": payload}

def audit(n, gaps=None):
    return {"record_id": f"AUDIT-{n}", "case": "META", "stage": "manual_parity_audit", "status": "done", "payload": {"for_meta_count": n, "sample_case_ids": [], "dimension_scores": {}, "gaps": gaps or [], "depth_backfill_case_ids": [], "confidence": "high"}}

def test():
    groups = {"G1": ["A"], "G2": ["B"], "G3": ["C"], "G4": ["D"]}
    m = manifest(groups)
    records = [sdss(x) for x in ["A", "B"]] + [sdss(str(x)) for x in range(1, 10)]
    # 2 groups / 11 eligible questions (the extra IDs are in G5 as one-case groups).
    m11 = manifest({"G1":["A","1","2","3","4","5"],"G2":["B","6","7","8","9"]})
    s = calculate_state(records, m11, {})
    assert (s["completed_passage_groups_total"], s["completed_questions_total"], s["meta_due"]) == (2, 11, False)
    s = calculate_state(records + [sdss("C")], manifest({"G1":["A"],"G2":["B"],"G3":["C"]}), {})
    assert s["meta_due"] is True  # 3 complete groups
    m12 = manifest({"G1":["A"], **{f"G{i}":[str(i-1)] for i in range(2,13)}})
    r12 = [sdss("A")] + [sdss(str(i)) for i in range(11)]
    assert calculate_state(r12, m12, {})["meta_due"] is True

    # A completed meta consumes an existing due flag and establishes baseline.
    old = {"meta_due": True, "last_meta_induction_id": None}
    post = calculate_state([sdss("A"), meta(1)], manifest({"G1":["A"]}), old)
    assert post["meta_due"] is False and post["last_meta_induction_id"] == "META-1"
    incomplete_meta = meta(2)
    del incomplete_meta["payload"]["falsification_attempts"]
    incomplete_state = calculate_state([incomplete_meta], [], old)
    assert incomplete_state["meta_induction_count"] == 0
    assert incomplete_state["last_meta_induction_id"] is None
    assert incomplete_state["meta_due"] is True
    assert "META-2:incomplete_meta" in incomplete_state["semantic_state_review"]
    one_more = calculate_state([sdss("A"), sdss("B"), meta(1)], manifest({"G1":["A"],"G2":["B"]}), post)
    assert one_more["meta_due"] is False
    three_more = calculate_state([sdss("A"), meta(1)] + [sdss(x) for x in "BCD"], manifest({f"G{i}":[x] for i,(x) in enumerate("ABCD",1)}), post)
    assert three_more["meta_due"] is True

    # Manifest membership is authoritative; partial groups never count.
    partial_m = manifest({"G14":["BY","BZ","CA","CB"]})
    assert calculate_state([sdss("BY")], partial_m, {})["completed_passage_groups_total"] == 0
    assert calculate_state([sdss(x) for x in ["BY","BZ","CA","CB"]], partial_m, {})["completed_passage_groups_total"] == 1
    assert calculate_state([sdss("BY", "hold")], manifest({"G1":["BY"]}), {})["completed_questions_total"] == 0
    variable = manifest({"GV":["A","Z","AA","ZZ","AAA"]})
    variable_records = [sdss(x) for x in ["A","Z","AA","ZZ","AAA"]] + [meta(99)]
    variable_state = calculate_state(variable_records, variable, {})
    assert variable_state["completed_questions_total"] == 5 and variable_state["completed_passage_groups_total"] == 1

    # Durable parity debt: 3 metas due; a fourth does not erase it; audit clears it.
    r3 = [meta(i) for i in range(1,4)]
    s3 = calculate_state(r3, [], {})
    assert s3["manual_parity_audit_due"] is True
    s4 = calculate_state(r3 + [meta(4)], [], s3)
    assert s4["manual_parity_audit_due"] is True
    s4a = calculate_state(r3 + [meta(4), audit(4)], [], s4)
    assert s4a["manual_parity_audit_due"] is False and s4a["last_manual_parity_audited_meta_count"] == 4
    incomplete_audit = audit(3)
    del incomplete_audit["payload"]["gaps"]
    assert calculate_state(r3 + [incomplete_audit], [], {})["manual_parity_audit_due"] is True

    # Incomplete backfill cannot erase an explicit pending case; complete can.
    incomplete_backfill = {"record_id":"BACKFILL-1","case":"A","stage":"depth_backfill","status":"done","payload":{key: [] for key in BACKFILL_FIELDS}}
    del incomplete_backfill["payload"]["evidence_additions"]
    incomplete_backfill["payload"]["case_ids"] = ["A"]
    old_pending = {"depth_backfill_pending": ["A"]}
    assert calculate_state([incomplete_backfill], [], old_pending)["depth_backfill_pending"] == ["A"]
    complete_backfill = copy.deepcopy(incomplete_backfill)
    complete_backfill["payload"]["evidence_additions"] = ["evidence"]
    assert calculate_state([complete_backfill], [], old_pending)["depth_backfill_pending"] == []

    # Explicit semantic lists and restart are mechanically stable.
    latest = calculate_state([meta(1, ["x"], ["u"])], [], {})
    assert latest["next_falsification_targets"] == ["x"] and latest["unresolved_boundaries"] == ["u"]
    assert calculate_state([meta(1, ["x"], ["u"])], [], latest) == latest

    # Delayed sync: baseline is the queue prefix before META-1, not sync time.
    chronology_manifest = manifest({f"G{i}":[f"Q{i}"] for i in range(1,7)})
    chronology = [sdss(f"Q{i}") for i in range(1,4)] + [meta(1)] + [sdss("Q4"), sdss("Q5")]
    delayed = calculate_state(chronology, chronology_manifest, {})
    assert delayed["completed_passage_groups_total"] == 5
    assert delayed["last_meta_induction_id"] == "META-1"
    assert delayed["baseline_completed_groups"] == 3
    assert delayed["completed_groups_since_last_meta"] == 2
    assert delayed["meta_due"] is False
    delayed_g6 = calculate_state(chronology + [sdss("Q6")], chronology_manifest, delayed)
    assert delayed_g6["completed_groups_since_last_meta"] == 3 and delayed_g6["meta_due"] is True
    assert calculate_state(chronology, chronology_manifest, delayed) == delayed

    # Regression: an incomplete meta with an extra field remains incomplete.
    meta2_incomplete = meta(2)
    del meta2_incomplete["payload"]["falsification_attempts"]
    meta2_incomplete["payload"]["extra_field"] = "ignored"
    regression = calculate_state(chronology + [meta2_incomplete], chronology_manifest, delayed)
    assert regression["meta_induction_count"] == 1
    assert regression["last_meta_induction_id"] == "META-1"
    assert regression["meta_due"] is True
    assert regression["baseline_completed_groups"] == 3
    assert "META-2:incomplete_meta" in regression["semantic_state_review"]
    print("meta_state fixture tests: 12 scenarios passed")

if __name__ == "__main__":
    test()
