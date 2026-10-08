#!/usr/bin/env python3
"""Mechanically prepare the next three exact KICE passage groups.

This script only packages source text and sealed provenance. It performs no
semantic review or code judgement.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/기본기_연구/prepared_backlog"
SPEC = [
    ("G061", ["JC", "JD", "JE", "JF"], "KICE-2014-9월_모평B-Q17-20-S051~054"),
    ("G062", ["JG", "JH", "JI"], "KICE-2014-수능B-Q19-21-S120~122"),
    ("G063", ["JJ", "JK", "JL", "JM"], "KICE-2014-6월_모평B-Q17-20-S170~173"),
]


def rows(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def dump(path: Path, values):
    path.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in values) + "\n", encoding="utf-8")


def main():
    manifest_path = BASE / "manifest.jsonl"
    mapping_path = BASE / "sealed/provenance_mapping.jsonl"
    answer_path = BASE / "sealed/answer_sdss.jsonl"
    manifest = rows(manifest_path)
    mapping = rows(mapping_path)
    answers = rows(answer_path)
    questions = rows(ROOT / "data/kice_questions.jsonl")
    passages = {x["passage_id"]: x for x in rows(ROOT / "data/kice_passages.jsonl")}
    q_by_passage = {}
    for q in questions:
        q_by_passage.setdefault(q["passage_id"], []).append(q)
    used_cases = {x["case_id"] for x in manifest}
    used_passages = {x["provenance"]["passage_id"] for x in mapping}
    for group, cases, passage_id in SPEC:
        if any(case in used_cases for case in cases) or passage_id in used_passages:
            raise SystemExit(f"already prepared: {group} {passage_id}")
        passage = passages.get(passage_id)
        qs = sorted(q_by_passage.get(passage_id, []), key=lambda x: x["question_number"])
        if passage is None or len(qs) != len(cases):
            raise SystemExit(f"incomplete canonical group: {group}")
        for q in qs:
            if q.get("choice_parse_status") != "complete" or len(q.get("choices", [])) != 5:
                raise SystemExit(f"choice parse failure: {q['question_id']}")
            if q.get("contains_visual_placeholder") or not q.get("official_answer_verified"):
                raise SystemExit(f"source QA failure: {q['question_id']}")
        for case, q in zip(cases, qs):
            source = {
                "blind_only": True,
                "passage_group": group,
                "case_id": case,
                "provenance": {"source_role": "anonymous_blind_source"},
                "passage_text": passage["passage_text"],
                "stem": q["stem"],
                "choices": q["choices"],
            }
            (BASE / "blind_sources" / f"{case}.json").write_text(
                json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
            (BASE / "packets" / f"{case}.md").write_text(
                f"# {case} blind packet\n\n"
                f"- case_id: {case}\n"
                f"- passage_group: {group}\n"
                f"- blind_source: data/기본기_연구/prepared_backlog/blind_sources/{case}.json\n"
                f"- group_case_ids: {', '.join(cases)}\n"
                "- group_rules: all_group_blind_records_before_any_group_answer_check; "
                "all_group_independent_code_records_before_any_group_sdss_disclosure\n\n"
                "Astra는 이 anonymous blind-only source만 읽는다. group 전체 blind raw와 "
                "independent_code raw 저장 전에는 봉인 자료를 열지 않는다.\n",
                encoding="utf-8",
            )
            mapping.append({
                "case_id": case,
                "passage_group": group,
                "group_case_ids": cases,
                "provenance": {
                    "exam_family": q["exam_family"],
                    "academic_year": q["academic_year"],
                    "exam_label": q["exam_label"],
                    "question_number": q["question_number"],
                    "question_id": q["question_id"],
                    "passage_id": q["passage_id"],
                },
                "source_status": "exact_canonical_kice_question",
                "source_role": "sealed_provenance_mapping",
            })
            answers.append({
                "case_id": case,
                "candidate_id": None,
                "official_answer": q["answer"],
                "official_answer_source": "data/kice_questions.jsonl (official_answer_verified)",
                "site_original_codes": [],
                "site_marked_answer": None,
                "source_role": "sealed_for_after_blind",
                "passage_group": group,
                "release_rule": "all_group_blind_records_before_any_group_answer_check",
            })
            manifest.append({
                "case_id": case,
                "status": "prepared",
                "passage_group": group,
                "group_case_ids": cases,
                "group_release_rules": [
                    "all_group_blind_records_before_any_group_answer_check",
                    "all_group_independent_code_records_before_any_group_sdss_disclosure",
                ],
                "blind_source": f"data/기본기_연구/prepared_backlog/blind_sources/{case}.json",
                "exclusion_checks": {
                    "exposure_status": "unknown",
                    "semantic_review": "not_reviewed",
                    "source_quality": {
                        "visual_placeholder": False,
                        "canonical_link": "exact",
                        "choice_parse": "complete",
                    },
                },
            })
    dump(manifest_path, manifest)
    dump(mapping_path, mapping)
    dump(answer_path, answers)
    print("prepared", ", ".join(f"{g}:{','.join(c)}" for g, c, _ in SPEC))


if __name__ == "__main__":
    main()
