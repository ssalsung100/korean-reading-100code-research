#!/usr/bin/env python3
"""Validate the anonymous prepared backlog without reading sealed semantics into blind sources."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/기본기_연구/prepared_backlog"
MANIFEST = BASE / "manifest.jsonl"
MAPPING = BASE / "sealed/provenance_mapping.jsonl"
ANSWERS = BASE / "sealed/answer_sdss.jsonl"
SOURCES = BASE / "blind_sources"
PACKETS = BASE / "packets"
QUEUE = ROOT / "data/기본기_연구/astra_handoff_queue.jsonl"
EXISTING = ROOT / "분석/기본기_연구/독립연구_03_최초풀이.md"

CASE_RE = re.compile(r"^[A-Z]+$")
GROUP_RE = re.compile(r"^G\d{3}$")
CONTENT_KEYS = {
    "official_answer", "site_marked_answer", "sdss", "sdss_code", "sdss_tag",
    "candidate_code", "candidate_codes", "existing_code", "existing_codes",
    "explanation", "commentary", "judgment", "independent_code", "answer_check",
}
IDENTITY_KEYS = {
    "year", "academic_year", "exam_year", "exam_label", "exam_name", "exam_type",
    "month", "variant", "question_number", "question_id", "passage_id",
    "canonical_id", "canonical_question_id", "canonical_passage_id", "candidate_id",
    "site_title", "title_search_url", "exam_search_url", "source_path", "local_source",
    "provenance_identifier", "site_marked_answer", "official_answer",
}
ALLOWED_SOURCE_KEYS = {"blind_only", "passage_group", "case_id", "provenance", "passage_text", "stem", "choices", "visual_supplements"}
BLIND_RULE = "all_group_blind_records_before_any_group_answer_check"
CODE_RULE = "all_group_independent_code_records_before_any_group_sdss_disclosure"


def lines(path: Path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def nested_keys(value):
    if isinstance(value, dict):
        for k, v in value.items():
            yield k
            yield from nested_keys(v)
    elif isinstance(value, list):
        for v in value:
            yield from nested_keys(v)


def main() -> int:
    manifest = lines(MANIFEST)
    mapping = lines(MAPPING)
    answers = lines(ANSWERS)
    errors = []
    content_leaks = []
    identity_leaks = []

    expected_count = len(manifest)
    if expected_count < 50:
        errors.append(f"manifest_below_minimum={expected_count} minimum=50")
    if len(mapping) != expected_count:
        errors.append(f"mapping_count={len(mapping)} expected={expected_count}")
    if len(answers) != expected_count:
        errors.append(f"sealed_answer_count={len(answers)} expected={expected_count}")

    manifest_ids = [x.get("case_id") for x in manifest]
    if len(set(manifest_ids)) != len(manifest_ids):
        errors.append("case_id_duplicate")
    mapping_by_case = {x.get("case_id"): x for x in mapping}
    question_ids = [x.get("provenance", {}).get("question_id") for x in mapping]
    question_duplicates = len(question_ids) - len(set(question_ids))
    if question_duplicates:
        errors.append("question_id_duplicate")
    existing_text = EXISTING.read_text(encoding="utf-8") if EXISTING.exists() else ""
    queue_text = QUEUE.read_text(encoding="utf-8") if QUEUE.exists() else ""
    existing_overlap = sum(1 for q in set(question_ids) if q and (q in existing_text or q in queue_text))

    groups = {}
    blind_visible_text = MANIFEST.read_text(encoding="utf-8") if MANIFEST.exists() else ""
    for visible_path in (ROOT / "분석/기본기_연구/CURRENT.md", ROOT / "scripts/cxcycle_astra_prompt.md"):
        if visible_path.exists():
            blind_visible_text += visible_path.read_text(encoding="utf-8")
    for item in manifest:
        cid = item.get("case_id")
        gid = item.get("passage_group")
        if not cid or not CASE_RE.fullmatch(cid):
            errors.append(f"bad_case_id:{cid}")
        if not gid or not GROUP_RE.fullmatch(gid):
            errors.append(f"bad_passage_group:{cid}")
        groups.setdefault(gid, []).append(cid)
        if item.get("group_case_ids") != item.get("group_case_ids", []):
            errors.append(f"bad_group_case_ids:{cid}")
        rules = item.get("group_release_rules", [])
        if BLIND_RULE not in rules or CODE_RULE not in rules:
            errors.append(f"missing_stage_barrier:{cid}")
        if any(k in IDENTITY_KEYS for k in nested_keys(item)):
            identity_leaks.append(f"manifest:{cid}")
        source_path = ROOT / item.get("blind_source", "")
        if not source_path.exists():
            errors.append(f"missing_source:{cid}")
            continue
        source = json.loads(source_path.read_text(encoding="utf-8"))
        meta = {k: v for k, v in source.items() if k not in {"passage_text", "stem", "choices"}}
        blind_visible_text += json.dumps(meta, ensure_ascii=False)
        if set(source) - ALLOWED_SOURCE_KEYS:
            errors.append(f"source_extra_keys:{cid}")
        if source.get("blind_only") is not True or source.get("case_id") != cid or source.get("passage_group") != gid:
            errors.append(f"source_identity_mismatch:{cid}")
        if source.get("provenance") != {"source_role": "anonymous_blind_source"}:
            errors.append(f"source_provenance_not_anonymous:{cid}")
        for visual in source.get("visual_supplements", []):
            if not isinstance(visual, dict) or not visual.get("file"):
                errors.append(f"bad_visual_link:{cid}")
                continue
            visual_path = ROOT / visual["file"]
            if not visual_path.exists() or visual_path.stat().st_size == 0:
                errors.append(f"missing_visual:{cid}:{visual.get('file')}")
            if set(visual) - {"file", "media_type"}:
                errors.append(f"visual_extra_metadata:{cid}")
        if any(k in CONTENT_KEYS for k in nested_keys(source)):
            content_leaks.append(f"source:{cid}")
        if any(k in IDENTITY_KEYS for k in nested_keys(meta)):
            identity_leaks.append(f"source:{cid}")
        packet_path = PACKETS / f"{cid}.md"
        if not packet_path.exists():
            errors.append(f"missing_packet:{cid}")
        else:
            packet = packet_path.read_text(encoding="utf-8")
            blind_visible_text += packet
            if BLIND_RULE not in packet or CODE_RULE not in packet:
                errors.append(f"packet_missing_barrier:{cid}")

    for gid, ids in groups.items():
        expected = next((x.get("group_case_ids") for x in manifest if x.get("passage_group") == gid), [])
        if ids != expected:
            errors.append(f"group_membership:{gid}")

    # Compare actual sealed identifiers only against blind metadata/instructions, never passage prose.
    actual_values = []
    for item in mapping:
        provenance = item.get("provenance", {})
        for key in IDENTITY_KEYS:
            value = provenance.get(key, item.get(key))
            if isinstance(value, str) and value:
                actual_values.append(value)
    for value in set(actual_values):
        if value in blind_visible_text:
            identity_leaks.append(f"value:{value}")

    result = {
        "questions": len(manifest),
        "unique_passages": len(groups),
        "content_leakage": len(set(content_leaks)),
        "blind_leaks": len(set(content_leaks)),
        "identity_leaks": len(set(identity_leaks)),
        "question_duplicates": question_duplicates,
        "existing_case_overlap": existing_overlap,
        "group_blind_barrier": BLIND_RULE,
        "group_independent_code_before_sdss_barrier": CODE_RULE,
        "stage_order": ["all_group_blind", "all_group_answer_check", "all_group_independent_code", "all_group_sdss_compare", "group_induction_or_boundary_revision"],
        "exposure_review_status": "unknown",
        "errors": sorted(set(errors)),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors or content_leaks or identity_leaks or question_duplicates or existing_overlap else 0


if __name__ == "__main__":
    raise SystemExit(main())
