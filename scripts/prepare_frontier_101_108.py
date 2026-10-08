#!/usr/bin/env python3
"""Mechanically prepare unused exact-canonical KICE groups after G100."""
import json
from pathlib import Path

from normalize_kice_reading_corpus import answer_is_mechanically_resolved

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/기본기_연구/prepared_backlog"
RULES = [
    "all_group_blind_records_before_any_group_answer_check",
    "all_group_independent_code_records_before_any_group_sdss_disclosure",
]
SPECS = [
    ("G101", ["ON", "OO", "OP", "OQ"], "KICE-2017-6월_모평-Q16-19-S040~043"),
    ("G102", ["OR", "OS", "OT", "OU", "OV", "OW"], "KICE-2017-9월_모평-Q25-30-S079~084"),
    ("G103", ["OX", "OY", "OZ", "PA"], "KICE-2018-수능-Q16-19-S033~036"),
    ("G104", ["PB", "PC", "PD", "PE", "PF", "PG"], "KICE-2018-6월_모평-Q16-21-S037~042"),
    ("G106", ["PH", "PI", "PJ", "PK"], "KICE-2018-6월_모평-Q22-25-S036~039"),
    ("G107", ["PL", "PM", "PN", "PO", "PP"], "KICE-2018-9월_모평-Q38-42-S140~144"),
    ("G108", ["PQ", "PR", "PS", "PT", "PU"], "KICE-2018-수능-Q38-42-S017~021"),
]


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path, rows):
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


def main():
    manifest_path = BASE / "manifest.jsonl"
    mapping_path = BASE / "sealed/provenance_mapping.jsonl"
    answer_path = BASE / "sealed/answer_sdss.jsonl"
    manifest = read_jsonl(manifest_path)
    mapping = read_jsonl(mapping_path)
    answers = read_jsonl(answer_path)
    questions = read_jsonl(ROOT / "data/kice_questions.jsonl")
    passages = {row["passage_id"]: row for row in read_jsonl(ROOT / "data/kice_passages.jsonl")}
    questions_by_passage = {}
    for question in questions:
        questions_by_passage.setdefault(question["passage_id"], []).append(question)
    used_cases = {row["case_id"] for row in manifest}
    used_passages = {row["provenance"]["passage_id"] for row in mapping}
    added_cases = 0
    for group, cases, passage_id in SPECS:
        if set(cases) & used_cases or passage_id in used_passages:
            raise RuntimeError(f"duplicate target: {group}")
        passage = passages[passage_id]
        qs = sorted(questions_by_passage[passage_id], key=lambda row: row["question_number"])
        if len(qs) != len(cases):
            raise RuntimeError(f"case count mismatch: {group}")
        if passage.get("contains_visual_placeholder"):
            raise RuntimeError(f"passage visual placeholder: {group}")
        for q in qs:
            if (q.get("choice_parse_status") != "complete" or len(q.get("choices", [])) != 5
                    or q.get("contains_visual_placeholder") or not answer_is_mechanically_resolved(q)):
                raise RuntimeError(f"question source QA failure: {q['question_id']}")
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
                json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            packet = (
                f"# {case} blind packet\n\n"
                f"- case_id: {case}\n- passage_group: {group}\n"
                f"- blind_source: data/기본기_연구/prepared_backlog/blind_sources/{case}.json\n"
                f"- group_case_ids: {', '.join(cases)}\n"
                "- group_rules: all_group_blind_records_before_any_group_answer_check; "
                "all_group_independent_code_records_before_any_group_sdss_disclosure\n\n"
                "Astra는 anonymous blind-only source만 읽고 group barrier를 지킨다.\n"
            )
            (BASE / "packets" / f"{case}.md").write_text(packet, encoding="utf-8")
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
                "release_rule": RULES[0],
            })
            manifest.append({
                "case_id": case,
                "status": "prepared",
                "passage_group": group,
                "group_case_ids": cases,
                "group_release_rules": RULES,
                "blind_source": f"data/기본기_연구/prepared_backlog/blind_sources/{case}.json",
                "exclusion_checks": {
                    "exposure_status": "unknown",
                    "semantic_review": "not_reviewed",
                    "source_quality": {
                        "visual_placeholder": False,
                        "canonical_link": "exact",
                        "choice_parse": "complete",
                        "text_markers_preserved": True,
                        "formatting_limit": "canonical JSON text; no separate PDF/HWPX visual audit required",
                    },
                },
            })
            added_cases += 1
    write_jsonl(manifest_path, manifest)
    write_jsonl(mapping_path, mapping)
    write_jsonl(answer_path, answers)
    print(json.dumps({"ready_groups": len(SPECS), "ready_cases": added_cases, "groups": [x[0] for x in SPECS]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
