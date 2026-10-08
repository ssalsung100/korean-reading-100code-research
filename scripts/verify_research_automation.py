#!/usr/bin/env python3
"""Static checks for Astra/Luna meta-induction automation contracts."""
from pathlib import Path
import json
import sys
import subprocess

ROOT = Path(__file__).resolve().parents[1]
errors = []
astra = (ROOT / "scripts/cxcycle_astra_prompt.md").read_text(encoding="utf-8")
research = (ROOT / "scripts/cxresearch_prompt.md").read_text(encoding="utf-8")
luna = (ROOT / "scripts/cxcycle_luna_prompt.md").read_text(encoding="utf-8")
processor = (ROOT / "scripts/luna_process_handoff.py").read_text(encoding="utf-8")
for name, text in [("astra", astra), ("research", research)]:
    for needle in ("meta_induction", "manual_parity_audit", "depth_backfill", "3 groups", "12 questions", "falsification"):
        if needle not in text:
            errors.append(f"{name}:missing:{needle}")
if "meta_due" not in astra or "meta_due" not in research:
    errors.append("meta_due precedence missing")
for name, text in [("astra", astra), ("research", research)]:
    if "python3 scripts/meta_state.py" not in text:
        errors.append(f"{name}:decision_point_sync_missing")
    if "manual_parity_audit_due=true" not in text:
        errors.append(f"{name}:audit_priority_missing")
    if "meta_due=false" not in text:
        errors.append(f"{name}:post_meta_sync_verification_missing")
    if text.find("manual_parity_audit_due=true") > text.find("meta_due=true"):
        errors.append(f"{name}:meta_precedes_audit")
if "does not" not in luna and "금지" not in luna:
    errors.append("Luna semantic prohibition missing")
for stage in ("meta_induction", "manual_parity_audit", "depth_backfill"):
    if stage not in processor:
        errors.append(f"processor:missing:{stage}")
for field in ("for_meta_count", "dimension_scores", "depth_backfill_case_ids", "original_blind_preserved", "evidence_additions"):
    if field not in processor:
        errors.append(f"processor:missing_schema_field:{field}")
state = ROOT / "data/기본기_연구/meta_state.json"
if not state.exists():
    errors.append("meta_state.json missing")
else:
    data = json.loads(state.read_text(encoding="utf-8"))
    for key in ("last_meta_induction_id", "meta_due", "manual_parity_audit_due", "next_falsification_targets", "unresolved_boundaries", "depth_backfill_pending"):
        if key not in data:
            errors.append(f"state:missing:{key}")
fixture = subprocess.run([sys.executable, str(ROOT / "scripts/test_meta_state.py")], capture_output=True, text=True)
if fixture.returncode != 0:
    errors.append("production_fixture_failed:" + fixture.stderr.strip())
quota_fixture = subprocess.run([sys.executable, str(ROOT / "scripts/test_quota_emergency.py")], capture_output=True, text=True)
if quota_fixture.returncode != 0:
    errors.append("quota_emergency_fixture_failed:" + (quota_fixture.stderr.strip() or quota_fixture.stdout.strip()))
print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)
