#!/usr/bin/env python3
"""Mechanically reflect Astra raw handoff records without semantic edits."""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/기본기_연구"
QUEUE = DATA / "astra_handoff_queue.jsonl"
PROCESSED = DATA / "astra_handoff_processed.jsonl"
DOCS = DATA / "독립풀이_04"
MANIFEST = DATA / "prepared_backlog/manifest.jsonl"

def read_jsonl(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def manifest_case_ids():
    return {str(x.get("case_id")) for x in read_jsonl(MANIFEST) if x.get("case_id")}

def target_for(record):
    case = str(record.get("case", ""))
    stage = record.get("stage")
    if stage in {"meta_induction", "manual_parity_audit", "depth_backfill"}:
        return [str(ROOT / "분석/기본기_연구/독립연구_04_절차와_진행기록.md")]
    if case in manifest_case_ids():
        # Boundary revisions are follow-up evidence for an already completed
        # case.  Route them to the SDSS/comparison record so the revision is
        # present in the detailed case history; do not leave it only in the
        # queue or processed ledger.
        suffix = {"blind": "01_최초풀이", "answer_check": "02_정답대조와_독립코드", "independent_code": "02_정답대조와_독립코드", "sdss_compare": "03_SDSS대조", "boundary_revision": "03_SDSS대조"}.get(stage)
        if suffix:
            return [str(DOCS / f"{case}_{suffix}.md")]
    if stage == "induction":
        return [str(ROOT / "분석/기본기_연구/독립연구_04_절차와_진행기록.md")]
    if stage == "hold":
        return [str(ROOT / "분석/기본기_연구/CURRENT.md")]
    return [str(DATA / "astra_handoff_queue.jsonl")]

def reflect_doc(record, target):
    path = Path(target)
    if path.suffix != ".md":
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    case = record.get("case", "")
    stage = record.get("stage", "")
    marker = f"<!-- luna-raw:{record['record_id']} -->"
    if path.exists() and marker in path.read_text(encoding="utf-8"):
        return
    payload = json.dumps(record.get("payload", {}), ensure_ascii=False, indent=2)
    block = f"\n\n{marker}\n## Astra raw handoff — {stage}\n\n원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.\n\n```json\n{payload}\n```\n"
    with path.open("a", encoding="utf-8") as f:
        f.write(block)

def main():
    queue = read_jsonl(QUEUE)
    processed = read_jsonl(PROCESSED) if PROCESSED.exists() else []
    known = {x.get("source_record_id") for x in processed}
    pending = [x for x in queue if x.get("record_id") not in known]
    valid_meta_count = sum(
        1 for x in queue
        if x.get("stage") == "meta_induction" and x.get("status") == "done"
        and {"window_groups", "window_cases", "strengthened_boundaries", "falsification_attempts", "revised_boundaries", "subtype_candidates", "primary_aux_revisions", "unresolved_boundaries", "next_falsification_targets", "generation_principles", "confidence", "carryover_questions"} <= set(x.get("payload", {}))
    )
    # Preflight the critical control state before reflecting or marking any
    # record processed.  A stale/failed state must fail closed.
    import subprocess
    try:
        subprocess.run([sys.executable, str(ROOT / "scripts/meta_state.py")], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as exc:
        print(f"luna_process_handoff: meta state sync failed: {exc.stderr.strip()}", file=sys.stderr)
        return 14
    with PROCESSED.open("a", encoding="utf-8") as out:
        for record in pending:
            targets = target_for(record)
            for target in targets:
                reflect_doc(record, target)
            entry = {
                "source_record_id": record["record_id"],
                "processed": True,
                "processed_at": datetime.now(timezone.utc).isoformat(),
                "targets": targets,
                "action": "Astra raw 의미 보존·기계적 반영; Luna 의미 재판정 없음",
                "review": None,
            }
            if record.get("stage") == "meta_induction":
                required = {
                    "window_groups", "window_cases", "strengthened_boundaries",
                    "falsification_attempts", "revised_boundaries", "subtype_candidates",
                    "primary_aux_revisions", "unresolved_boundaries", "next_falsification_targets",
                    "generation_principles", "confidence", "carryover_questions",
                }
                missing = sorted(required - set(record.get("payload", {})))
                if missing:
                    entry["review"] = "needs_astra_review"
                    entry["missing_meta_fields"] = missing
            if record.get("stage") == "manual_parity_audit":
                required = {"for_meta_count", "sample_case_ids", "dimension_scores", "gaps", "depth_backfill_case_ids", "confidence"}
                missing = sorted(required - set(record.get("payload", {})))
                target = record.get("payload", {}).get("for_meta_count")
                if not missing and (not isinstance(target, int) or target <= 0 or target > valid_meta_count):
                    missing.append("valid_for_meta_count")
                if missing:
                    entry["review"] = "needs_astra_review"
                    entry["missing_manual_parity_fields"] = missing
            if record.get("stage") == "depth_backfill":
                required = {"case_ids", "original_blind_preserved", "evidence_additions", "boundary_or_generation_impact", "confidence"}
                missing = sorted(required - set(record.get("payload", {})))
                if missing:
                    entry["review"] = "needs_astra_review"
                    entry["missing_depth_backfill_fields"] = missing
            if record.get("status") != "done" or record.get("stage") in {"hold"}:
                entry["review"] = "needs_astra_review"
                entry["note"] = "미완료 또는 hold 상태를 보존함"
            out.write(json.dumps(entry, ensure_ascii=False) + "\n")
    # Manifest status is mechanical state only; it never creates a semantic judgment.
    manifest = DATA / "prepared_backlog/manifest.jsonl"
    if manifest.exists():
        rows = read_jsonl(manifest)
        by_case = {}
        known_case_ids = manifest_case_ids()
        for record in queue:
            case = record.get("case")
            if case in known_case_ids:
                by_case.setdefault(case, set()).add(record.get("stage"))
        for row in rows:
            case = row.get("case_id")
            stages = by_case.get(case, set())
            if "sdss_compare" in stages:
                row["status"] = "consumed_sdss"
                row["sdss_disclosure"] = "complete"
            elif "independent_code" in stages:
                row["status"] = "consumed_independent_code"
                row["sdss_disclosure"] = "pending_group_barrier"
        manifest.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + "\n", encoding="utf-8")
    print(f"processed {len(pending)} raw records; manifest mechanically synchronized")

if __name__ == "__main__":
    raise SystemExit(main() or 0)
