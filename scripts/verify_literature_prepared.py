#!/usr/bin/env python3
"""Validate newly prepared KICE literature cases without treating historical backlog warnings as new failures."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/기본기_연구/prepared_backlog"
MANIFEST = BASE / "manifest.jsonl"
MAPPING = BASE / "sealed/provenance_mapping.jsonl"
ANSWERS = BASE / "sealed/answer_sdss.jsonl"
ALLOWED_SOURCE_KEYS = {"blind_only", "passage_group", "case_id", "provenance", "passage_text", "stem", "choices"}
LEAK_KEYS = {
    "official_answer", "site_marked_answer", "sdss", "sdss_code", "sdss_tag",
    "candidate_code", "candidate_codes", "existing_code", "existing_codes",
    "explanation", "commentary", "judgment", "independent_code", "answer_check",
    "academic_year", "exam_label", "question_number", "question_id", "passage_id",
    "candidate_id", "source_path", "local_source", "source_original_path",
}
def records(path: Path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
def nested_keys(value):
    if isinstance(value, dict):
        for k, v in value.items():
            yield k
            yield from nested_keys(v)
    elif isinstance(value, list):
        for v in value:
            yield from nested_keys(v)

manifest = records(MANIFEST)
mapping = records(MAPPING)
answers = records(ANSWERS)
lit_mapping = [x for x in mapping if x.get("source_status") == "local_complete_literature"]
lit_cases = {x["case_id"] for x in lit_mapping}
manifest_by_case = {x["case_id"]: x for x in manifest}
answer_by_case = {x["case_id"]: x for x in answers}
errors = []
for row in lit_mapping:
    cid = row.get("case_id")
    if cid not in manifest_by_case:
        errors.append(f"missing_manifest:{cid}")
        continue
    if cid not in answer_by_case:
        errors.append(f"missing_sealed_answer:{cid}")
    source_path = ROOT / manifest_by_case[cid]["blind_source"]
    if not source_path.exists():
        errors.append(f"missing_blind_source:{cid}")
        continue
    source = json.loads(source_path.read_text(encoding="utf-8"))
    if set(source) != ALLOWED_SOURCE_KEYS:
        errors.append(f"source_extra_keys:{cid}")
    if source.get("blind_only") is not True or source.get("case_id") != cid:
        errors.append(f"source_identity:{cid}")
    if source.get("provenance") != {"source_role": "anonymous_blind_source"}:
        errors.append(f"source_provenance:{cid}")
    if not source.get("passage_text") or not source.get("stem"):
        errors.append(f"empty_blind_text:{cid}")
    if not isinstance(source.get("choices"), list) or len(source["choices"]) != 5:
        errors.append(f"choice_count:{cid}")
    if any(k in LEAK_KEYS for k in nested_keys(source)):
        errors.append(f"blind_leak:{cid}")
    provenance = row.get("provenance", {})
    for key in ("source_original_path", "central_md_path", "official_answer_source_path"):
        if not provenance.get(key):
            errors.append(f"missing_provenance_field:{cid}:{key}")
    original = Path(provenance["source_original_path"])
    central = ROOT / provenance["central_md_path"]
    answer_source = ROOT / provenance["official_answer_source_path"]
    if not original.exists():
        errors.append(f"missing_original:{cid}")
    elif hashlib.sha256(original.read_bytes()).hexdigest() != provenance.get("source_sha256"):
        errors.append(f"source_sha256:{cid}")
    if not central.exists():
        errors.append(f"missing_central_md:{cid}")
    if not answer_source.exists():
        errors.append(f"missing_answer_source:{cid}")

question_ids = [x.get("provenance", {}).get("question_id") for x in lit_mapping]
candidate_ids = [x.get("provenance", {}).get("candidate_id") for x in lit_mapping]
errors.extend(f"duplicate_question_id:{q}" for q in set(q for q in question_ids if q) if question_ids.count(q) > 1)
errors.extend(f"duplicate_candidate_id:{c}" for c in set(c for c in candidate_ids if c) if candidate_ids.count(c) > 1)
result = {
    "literature_cases": len(lit_mapping),
    "literature_groups": len({x.get("passage_group") for x in lit_mapping}),
    "blind_leakage": sum(x.startswith("blind_leak:") for x in errors),
    "answer_leakage": sum(x.startswith("blind_leak:") and ("answer" in x or "sdss" in x) for x in errors),
    "duplicate": sum(x.startswith("duplicate_") for x in errors),
    "source_provenance_error": sum(x.startswith(("missing_", "source_sha256")) for x in errors),
    "errors": sorted(set(errors)),
    "historical_verifier_warning": "scripts/verify_prepared_backlog.py may report pre-existing non-literature errors separately",
}
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)

