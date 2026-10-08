#!/usr/bin/env python3
"""Restore only the mechanically incomplete G071-G100 source groups.

This script intentionally does not inspect or use SDSS data for restoration.
It recovers choice text from local canonical HWPX XML (including hp:tab tails),
extracts the two referenced embedded visual assets, writes anonymous blind
sources, and updates the prepared-backlog indexes mechanically.
"""
from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from PIL import Image

from normalize_kice_reading_corpus import answer_is_mechanically_resolved


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/기본기_연구/prepared_backlog"
BLIND = BASE / "blind_sources"
PACKETS = BASE / "packets"
SEALED = BASE / "sealed"

RULES = [
    "all_group_blind_records_before_any_group_answer_check",
    "all_group_independent_code_records_before_any_group_sdss_disclosure",
]


TARGETS = [
    {
        "group": "G071", "cases": ["KF", "KG", "KH", "KI"],
        "passage_id": "KICE-2012-수능-Q21-24-S009~012",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅲ. 과학.hwpx",
        "query": "㉠～㉤을 바꾸어 쓴 말로 적절하지 않은 것은?",
        "target_case": "KI",
    },
    {
        "group": "G072", "cases": ["KJ", "KK", "KL", "KM"],
        "passage_id": "KICE-2013-수능-Q21-24-S079~082",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅰ. 인문, 독서.hwpx",
        "query": "문맥상 ⓐ～ⓔ를 바꿔 쓰기에 적절하지 않은 것은?",
        "target_case": "KM",
    },
    {
        "group": "G073", "cases": ["KN", "KO", "KP"],
        "passage_id": "KICE-2013-6월_모평-Q23-25-S097~099",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅲ. 과학.hwpx",
        "query": "㉠의 내용으로 옳은 것만을 <보기>에서 있는 대로 고른 것은?",
        "target_case": "KO",
        "choice_asset_members": [
            "BinData/image18.bmp", "BinData/image19.bmp", "BinData/image20.bmp",
            "BinData/image21.bmp", "BinData/image22.bmp",
        ],
        "choice_asset_refs": ["image18", "image19", "image20", "image21", "image22"],
        "choice_asset_stem": "G073_KP_choice",
        "choice_asset_case": "KP",
    },
    {
        "group": "G074", "cases": ["KQ", "KR", "KS", "KT"],
        "passage_id": "KICE-2013-수능-Q25-28-S011~014",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅴ. 예술.hwpx",
        "query": "<보기>를 바탕으로 할 때, 윗글의 ⓐ와 같은 방식으로 이루어진 것은?",
        "target_case": "KT",
    },
    {
        "group": "G075", "cases": ["KU", "KV", "KW"],
        "passage_id": "KICE-2014-수능A-Q19-21-S035~037",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅴ. 예술.hwpx",
        "query": "문맥상 ㉠∼㉤을 바꿔 쓰기에 적절하지 않은 것은?",
        "target_case": "KW",
    },
    {
        "group": "G081", "cases": ["LN", "LO", "LP"],
        "passage_id": "KICE-2015-수능A-Q20-22-S027~029",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅳ. 기술.hwpx",
        "query": "윗글의 <그림>에 ㉠, ㉡을 적용했을 때",
        "target_case": "LO",
        "asset_member": "BinData/image6.bmp",
        "asset_stem": "G081_LO_figure",
        "asset_ref": "image6",
    },
    {
        "group": "G084", "cases": ["LZ", "MA", "MB", "MC"],
        "passage_id": "KICE-2016-6월_모평B-Q17-20-S043~046",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅰ. 인문, 독서.hwpx",
        "query": "문맥상 ㉠～㉤과 바꿔 쓰기에 적절하지 않은 것은?",
        "target_case": "MC",
    },
    {
        "group": "G086", "cases": ["MH", "MI", "MJ", "MK"],
        "passage_id": "KICE-2016-수능B-Q17-20-S116~119",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅰ. 인문, 독서.hwpx",
        "query": "㉡의 관점에 따를 때",
        "target_case": "MI",
    },
    {
        "group": "G090", "cases": ["MW", "MX"],
        "passage_id": "KICE-2016-6월_모평B-Q25-26-S013~014",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅲ. 과학.hwpx",
        "query": "<그림>의 곡선 B에 대한 설명",
        "target_case": "MX",
        "asset_member": "BinData/image3.bmp",
        "asset_stem": "G090_MX_curve",
        "asset_ref": "image3",
    },
    {
        "group": "G095", "cases": ["NK", "NL", "NM", "NN", "NO"],
        "passage_id": "KICE-2017-수능-Q16-20-S065~069",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅰ. 인문, 독서.hwpx",
        "query": "문맥상 ㉢과 바꿔 쓰기에 가장 적절한 것은?",
        "target_case": "NO",
    },
    {
        "group": "G096", "cases": ["NP", "NQ", "NR", "NS", "NT"],
        "passage_id": "KICE-2017-6월_모평-Q20-24-S070~074",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅰ. 인문, 독서.hwpx",
        "query": "문맥상 ㉢과 바꿔 쓰기에 적절하지 않은 것은?",
        "target_case": "NT",
    },
    {
        "group": "G098", "cases": ["OA", "OB", "OC", "OD", "OE"],
        "passage_id": "KICE-2017-9월_모평-Q35-39-S064~068",
        "hwpx": "고3 기출/2027 고3 국어 독서_Ⅱ. 사회.hwpx",
        "query": "문맥상 ㉠과 바꿔 쓰기에 가장 적절한 것은?",
        "target_case": "OE",
    },
]


def read_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows), encoding="utf-8")


def group_sort(row):
    group_cases = row.get("group_case_ids", [])
    case_index = group_cases.index(row["case_id"]) if row["case_id"] in group_cases else 0
    return (int(row["passage_group"][1:]), case_index, row["case_id"])


def hwpx_paragraphs(path: Path):
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("Contents/section0.xml"))
    paragraphs = []
    for paragraph in root.findall(".//{*}p"):
        # HWPX places text after hp:tab as a tail of hp:t. itertext is required.
        text = "".join(paragraph.itertext()).replace("\u00a0", " ").strip()
        if text:
            paragraphs.append(text)
    return paragraphs


def choices_from_hwpx(paragraphs, query):
    hits = [i for i, text in enumerate(paragraphs) if query in text]
    if len(hits) != 1:
        raise RuntimeError(f"query_hits={len(hits)} query={query}")
    start = hits[0]
    collected = []
    for text in paragraphs[start + 1 :]:
        if re.fullmatch(r"\d{3}", text) or re.match(r"^\[\d+~\d+\]", text):
            break
        collected.append(text)
        merged = " ".join(collected)
        pieces = re.split(r"(?=[①②③④⑤])", merged)
        choices = []
        for piece in pieces:
            piece = re.sub(r"\s+", " ", piece).strip()
            if not piece or not piece[0] in "①②③④⑤":
                continue
            choices.append(piece[1:].strip())
        # Stop at the fifth option; the next paragraph may already be the
        # following unit/passage and must not be absorbed into choice ⑤.
        if len(choices) == 5:
            return choices
    raise RuntimeError(f"choice_count<5 query={query} choices={choices if 'choices' in locals() else []}")


def extract_asset(spec):
    if "choice_asset_members" in spec:
        stem = spec["choice_asset_stem"]
        assets = []
        mapping = []
        with zipfile.ZipFile(ROOT / spec["hwpx"]) as archive:
            for index, (member, ref) in enumerate(zip(spec["choice_asset_members"], spec["choice_asset_refs"]), 1):
                bmp = BLIND / f"{stem}_{index}.bmp"
                png = BLIND / f"{stem}_{index}.png"
                bmp.write_bytes(archive.read(member))
                Image.open(bmp).save(png)
                with Image.open(bmp) as image:
                    dims = [image.width, image.height]
                assets.append(png.name)
                mapping.append({
                    "choice_number": index,
                    "embedded_asset_reference": ref,
                    "asset": f"data/기본기_연구/prepared_backlog/blind_sources/{png.name}",
                    "original_dimensions_px": dims,
                })
        write_json(BLIND / f"{stem}.provenance.json", {
            "blind_only": True,
            "passage_group": spec["group"],
            "case_id": spec["target_case"],
            "supplement_role": "anonymous_blind_source_supplement",
            "supplement_type": "embedded_visual_choice_assets",
            "choice_asset_mapping": mapping,
            "provenance": {
                "artifact_scope": "local canonical HWPX Contents/section0.xml embedded bitmap",
                "answer_or_sdss_included": False,
                "interpretation_added": False,
            },
        })
        return {"choice_assets": assets, "choice_asset_mapping": mapping}
    if "asset_member" not in spec:
        return None
    stem = spec["asset_stem"]
    bmp = BLIND / f"{stem}.bmp"
    png = BLIND / f"{stem}.png"
    with zipfile.ZipFile(ROOT / spec["hwpx"]) as archive:
        bmp.write_bytes(archive.read(spec["asset_member"]))
    Image.open(bmp).save(png)
    with Image.open(bmp) as image:
        dims = [image.width, image.height]
    supplement = {
        "blind_only": True,
        "passage_group": spec["group"],
        "case_id": spec["target_case"],
        "supplement_role": "anonymous_blind_source_supplement",
        "supplement_type": "embedded_visual_asset",
        "diagram_asset": f"data/기본기_연구/prepared_backlog/blind_sources/{png.name}",
        "parallel_original_asset": f"data/기본기_연구/prepared_backlog/blind_sources/{bmp.name}",
        "provenance": {
            "artifact_scope": "local canonical HWPX Contents/section0.xml embedded bitmap",
            "embedded_asset_reference": spec["asset_ref"],
            "original_dimensions_px": dims,
            "answer_or_sdss_included": False,
            "interpretation_added": False,
        },
    }
    write_json(BLIND / f"{stem}.provenance.json", supplement)
    return png.name


def main():
    passages = {row["passage_id"]: row for row in read_jsonl(ROOT / "data/kice_passages.jsonl")}
    questions = read_jsonl(ROOT / "data/kice_questions.jsonl")
    questions_by_passage = {}
    for row in questions:
        questions_by_passage.setdefault(row["passage_id"], []).append(row)

    manifest_path = BASE / "manifest.jsonl"
    mapping_path = SEALED / "provenance_mapping.jsonl"
    answer_path = SEALED / "answer_sdss.jsonl"
    manifest = read_jsonl(manifest_path)
    mapping = read_jsonl(mapping_path)
    answers = read_jsonl(answer_path)
    target_groups = {spec["group"] for spec in TARGETS}
    # Make recovery idempotent if a prior run stopped after one index was written.
    manifest = [row for row in manifest if row.get("passage_group") not in target_groups]
    mapping = [row for row in mapping if row.get("passage_group") not in target_groups]
    answers = [row for row in answers if row.get("case_id") not in {case for spec in TARGETS for case in spec["cases"]}]

    restored_manifest = []
    restored_mapping = []
    restored_answers = []
    report = []
    for spec in TARGETS:
        passage = passages[spec["passage_id"]]
        qs = sorted(questions_by_passage[spec["passage_id"]], key=lambda row: row["question_number"])
        if len(qs) != len(spec["cases"]):
            raise RuntimeError(f"case count mismatch {spec['group']}")
        paragraphs = hwpx_paragraphs(ROOT / spec["hwpx"])
        restored_choices = choices_from_hwpx(paragraphs, spec["query"])
        target_q = next(q for q in qs if q["question_id"] and q["question_number"] == qs[-1]["question_number"])
        # The target case is supplied explicitly; use group order rather than any answer/code field.
        target_index = spec["cases"].index(spec["target_case"])
        target_q = qs[target_index]
        asset_info = extract_asset(spec)
        asset_name = asset_info if isinstance(asset_info, str) else None

        for index, (case_id, question) in enumerate(zip(spec["cases"], qs)):
            choices = restored_choices if index == target_index else question["choices"]
            choice_visual_assets = None
            if case_id == spec.get("choice_asset_case") and isinstance(asset_info, dict) and asset_info.get("choice_assets"):
                choice_visual_assets = asset_info["choice_asset_mapping"]
                choices = [
                    f"{number}번 선택지 [embedded visual asset: {mapping['asset']}]"
                    for number, mapping in enumerate(choice_visual_assets, 1)
                ]
            if not isinstance(choices, list) or len(choices) != 5:
                raise RuntimeError(f"choice_count after restore {case_id}")
            if index == target_index and any(not str(c).strip() for c in choices):
                raise RuntimeError(f"target choices remain incomplete after restore {case_id}")
            source = {
                "blind_only": True,
                "passage_group": spec["group"],
                "case_id": case_id,
                "provenance": {"source_role": "anonymous_blind_source"},
                "passage_text": passage["passage_text"],
                "stem": question["stem"],
                "choices": choices,
            }
            write_json(BLIND / f"{case_id}.json", source)
            packet = [
                f"# {case_id} blind packet", "",
                f"- passage_group: {spec['group']}",
                f"- group_case_ids: {', '.join(spec['cases'])}",
                f"- blind_source: data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json",
                f"- group_rules: {'; '.join(RULES)}", "",
                "Astra는 anonymous blind-only source만 읽고 group barrier를 지킨다.", "",
            ]
            (PACKETS / f"{case_id}.md").write_text("\n".join(packet), encoding="utf-8")
            quality = {
                "visual_placeholder": False,
                "canonical_link": "exact",
                "choice_parse": "complete",
                "text_markers_preserved": True,
                "restoration_basis": "local_canonical_hwpx_xml",
            }
            if asset_name:
                quality["visual_asset_status"] = "restored_embedded_asset"
                quality["visual_asset"] = f"data/기본기_연구/prepared_backlog/blind_sources/{asset_name}"
            if choice_visual_assets:
                quality["visual_asset_status"] = "restored_embedded_asset"
                quality["visual_choice_assets"] = choice_visual_assets
            restored_manifest.append({
                "case_id": case_id,
                "status": "prepared",
                "passage_group": spec["group"],
                "group_case_ids": spec["cases"],
                "group_release_rules": RULES,
                "blind_source": f"data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json",
                "exclusion_checks": {
                    "exposure_status": "unknown",
                    "semantic_review": "not_reviewed",
                    "source_quality": quality,
                },
            })
            restored_mapping.append({
                "case_id": case_id,
                "passage_group": spec["group"],
                "group_case_ids": spec["cases"],
                "provenance": {
                    "exam_family": passage["exam_family"],
                    "academic_year": passage["academic_year"],
                    "exam_label": passage["exam_label"],
                    "question_number": question["question_number"],
                    "question_id": question["question_id"],
                    "passage_id": passage["passage_id"],
                },
                "source_status": "exact_canonical_kice_question",
                "source_role": "sealed_provenance_mapping",
            })
            # This sealed row is produced mechanically and is not read by the restoration checks.
            restored_answers.append({
                "case_id": case_id,
                "candidate_id": None,
                "official_answer": question.get("answer") if answer_is_mechanically_resolved(question) else None,
                "official_answer_source": "data/kice_questions.jsonl (answer field; mechanical linkage only)",
                "site_original_codes": [],
                "site_marked_answer": None,
                "source_role": "sealed_for_after_blind",
                "passage_group": spec["group"],
                "release_rule": RULES[0],
            })
        report.append({
            "passage_group": spec["group"],
            "cases": spec["cases"],
            "restored_case": spec["target_case"],
            "status": "READY",
            "choice_source": "local canonical HWPX XML hp:t + hp:tab tails",
            "visual_asset": asset_name or ("choice_assets" if isinstance(asset_info, dict) else None),
            "mechanical_check": "pass",
        })

    manifest.extend(restored_manifest)
    mapping.extend(restored_mapping)
    answers.extend(restored_answers)
    write_jsonl(manifest_path, sorted(manifest, key=group_sort))
    write_jsonl(mapping_path, sorted(mapping, key=group_sort))
    write_jsonl(answer_path, sorted(answers, key=lambda row: row["case_id"]))

    restore_report = {
        "scope": [spec["group"] for spec in TARGETS],
        "restored_cases": sum(len(spec["cases"]) for spec in TARGETS),
        "ready_groups": len(TARGETS),
        "not_started": "G101 and later",
        "semantic_work": False,
        "answer_or_sdss_used_as_restoration_basis": False,
        "groups": report,
    }
    write_json(BASE / "SOURCE_RESTORE_20260917.json", restore_report)
    print(json.dumps(restore_report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
