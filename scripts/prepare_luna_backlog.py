#!/usr/bin/env python3
"""Mechanically add an unused exact-canonical KICE passage group to the blind backlog."""
import json
from pathlib import Path

from normalize_kice_reading_corpus import answer_is_mechanically_resolved

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/기본기_연구/prepared_backlog"
GROUP = "G047"
CASES = ["HJ", "HK", "HL", "HM"]
PASSAGE = "KICE-2026-수능-Q10-13-S021~024"

def rows(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def dump(path, values):
    path.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in values) + "\n", encoding="utf-8")

def main():
    manifest_path = BASE / "manifest.jsonl"
    mapping_path = BASE / "sealed/provenance_mapping.jsonl"
    answer_path = BASE / "sealed/answer_sdss.jsonl"
    manifest = rows(manifest_path)
    mapping = rows(mapping_path)
    answers = rows(answer_path)
    candidates = rows(ROOT / "data/기본기_연구/code_study_candidates_v2.jsonl")
    questions = {x["question_id"]: x for x in rows(ROOT / "data/kice_questions.jsonl")}
    passages = {x["passage_id"]: x for x in rows(ROOT / "data/kice_passages.jsonl")}
    used = {x["provenance"]["question_id"] for x in mapping}
    selected = []
    for c in candidates:
        cc = c.get("canonical_connection", {})
        if cc.get("passage_id") != PASSAGE or cc.get("question_id") in used:
            continue
        qid = cc["question_id"]
        if cc.get("status") != "exact_canonical_kice_question":
            continue
        if not answer_is_mechanically_resolved(questions[qid]):
            continue
        selected.append((c, questions[qid]))
    selected.sort(key=lambda pair: pair[1]["question_number"])
    if len(selected) != len(CASES):
        raise SystemExit(f"expected {len(CASES)} unused canonical questions, found {len(selected)}")
    if any(x.get("case_id") in CASES for x in manifest):
        raise SystemExit("case id already exists")
    passage = passages[PASSAGE]
    group_ids = CASES[:]
    for case, (candidate, question) in zip(CASES, selected):
        source = {
            "blind_only": True,
            "passage_group": GROUP,
            "case_id": case,
            "provenance": {"source_role": "anonymous_blind_source"},
            "passage_text": passage["passage_text"],
            "stem": question["stem"],
            "choices": question["choices"],
        }
        (BASE / "blind_sources" / f"{case}.json").write_text(
            json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        packet = f"""# {case} blind packet

- case_id: {case}
- passage_group: {GROUP}
- blind_source: data/기본기_연구/prepared_backlog/blind_sources/{case}.json
- group_case_ids: {', '.join(group_ids)}
- group_rules: all_group_blind_records_before_any_group_answer_check; all_group_independent_code_records_before_any_group_sdss_disclosure

Astra는 이 anonymous blind-only source만 읽는다. 동일 passage group의 모든 case에 대해 blind record를 queue에 저장하고, group 전체 independent_code raw 저장까지 확인한 뒤에만 봉인된 후속 자료에 접근한다. 실제 시험 식별 정보는 blind 단계에서 제공하지 않는다.
"""
        (BASE / "packets" / f"{case}.md").write_text(packet, encoding="utf-8")
        cc = candidate["canonical_connection"]
        provenance = {
            "case_id": case,
            "passage_group": GROUP,
            "group_case_ids": group_ids,
            "provenance": {
                "exam_family": question["exam_family"],
                "academic_year": question["academic_year"],
                "exam_label": question["exam_label"],
                "question_number": question["question_number"],
                "question_id": question["question_id"],
                "passage_id": question["passage_id"],
            },
            "source_status": "exact_canonical_kice_question",
            "source_role": "sealed_provenance_mapping",
        }
        mapping.append(provenance)
        site = candidate.get("site_candidate", {})
        answers.append({
            "case_id": case,
            "candidate_id": candidate["candidate_id"],
            "official_answer": question["answer"] if answer_is_mechanically_resolved(question) else None,
            "official_answer_source": "data/kice_questions.jsonl (answer field; mechanical linkage only)",
            "site_original_codes": site.get("site_original_codes", []),
            "site_marked_answer": site.get("site_marked_answer"),
            "source_role": "sealed_for_after_blind",
            "passage_group": GROUP,
            "release_rule": "all_group_blind_records_before_any_group_answer_check",
        })
        manifest.append({
            "case_id": case,
            "status": "prepared",
            "passage_group": GROUP,
            "group_case_ids": group_ids,
            "group_release_rules": ["all_group_blind_records_before_any_group_answer_check", "all_group_independent_code_records_before_any_group_sdss_disclosure"],
            "blind_source": f"data/기본기_연구/prepared_backlog/blind_sources/{case}.json",
            "exclusion_checks": {"exposure_status": "unknown", "semantic_review": "not_reviewed", "source_quality": {"visual_placeholder": False, "canonical_link": "exact", "choice_parse": "complete"}},
        })
    dump(manifest_path, manifest)
    dump(mapping_path, mapping)
    dump(answer_path, answers)
    print(f"prepared {len(CASES)} cases in {GROUP}: {', '.join(CASES)}")

if __name__ == "__main__":
    main()
