#!/usr/bin/env python3
"""Prepare four LEET passages from canonical Markdown plus exact visual crops.

Markdown supplies every passage, stem, and choice. HWP page renders are used
only to crop the boxed target terms that the Markdown marks as <그림>.
No answer key, SDSS tag, or semantic research record is read or used.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from tempfile import NamedTemporaryFile

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/기본기_연구/prepared_backlog"
TARGET = ROOT / "data/기본기_연구/target_completion_crosswalk_v1.jsonl"
MANIFEST = BASE / "manifest.jsonl"
MAPPING = BASE / "sealed/provenance_mapping.jsonl"
ANSWERS = BASE / "sealed/answer_sdss.jsonl"
RESTORATIONS = BASE / "sealed/source_restorations_v1.jsonl"
RULES = [
    "all_group_blind_records_before_any_group_answer_check",
    "all_group_independent_code_records_before_any_group_sdss_disclosure",
]
VISUAL_MAP = ROOT / "자료/LEET_언어이해/검증/HWP_홀수형_시각자료_문항매핑_v1.json"

GROUPS = [
    {
        "year": 2017, "start": 1, "end": 3,
        "page": "자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2017/page_001.png",
        "crops": [
            {"key": "passage", "box": [698, 1182, 758, 1230], "scope": "Q1-3 common passage boxed target term"},
            {"key": "q1", "box": [892, 1597, 963, 1646], "scope": "Q1 stem boxed target term"},
        ],
    },
    {
        "year": 2017, "start": 11, "end": 13,
        "page": "자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2017/page_006.png",
        "crops": [
            {"key": "target", "box": [226, 638, 378, 685], "scope": "Q11-13 common passage boxed target term; Q12 stem reference"},
        ],
    },
    {
        "year": 2018, "start": 10, "end": 12,
        "page": "자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2018/page_005.png",
        "crops": [
            {"key": "target", "box": [878, 680, 1052, 732], "scope": "Q10-12 common passage boxed target phrase; Q12 stem reference"},
        ],
    },
    {
        "year": 2019, "start": 1, "end": 3,
        "page": "자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2019/page_001.png",
        "crops": [
            {"key": "target", "box": [246, 910, 350, 960], "scope": "Q1-3 common passage boxed target term; Q3 stem reference"},
        ],
    },
    {
        "year": 2018, "start": 13, "end": 15,
        "page": "자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2018/page_007.png",
        "crops": [
            {"key": "passage", "box": [493, 1375, 570, 1445], "scope": "Q13-15 common passage boxed target term"},
            {"key": "q14", "box": [905, 1380, 976, 1440], "scope": "Q14 stem boxed target term"},
        ],
    },
]


def read_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(path: Path) -> str:
    return sha256(path.read_bytes())


def atomic_write(path: Path, data: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile("wb", dir=path.parent, delete=False) as handle:
        handle.write(data)
        temp = Path(handle.name)
    os.replace(temp, path)


def jsonl_bytes(rows) -> bytes:
    return "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows).encode("utf-8")


def parse_group(markdown: str, start: int, end: int):
    ranges = list(re.finditer(r"^\[(\d+)\s*[~～〜-]\s*(\d+)\][^\n]*$", markdown, re.M))
    found = [i for i, match in enumerate(ranges) if int(match.group(1)) == start and int(match.group(2)) == end]
    if len(found) != 1:
        raise ValueError(f"canonical Markdown lacks one exact [{start}~{end}] passage anchor")
    index = found[0]
    anchor = ranges[index]
    block_end = ranges[index + 1].start() if index + 1 < len(ranges) else len(markdown)
    block = markdown[anchor.end():block_end]
    heads = list(re.finditer(r"^\s*(\d+)\.\s*", block, re.M))
    expected = list(range(start, end + 1))
    if [int(head.group(1)) for head in heads] != expected:
        raise ValueError(f"question linkage is not exact for {start}~{end}")
    passage = block[:heads[0].start()].strip()
    if not passage:
        raise ValueError("empty canonical passage")
    questions = {}
    for i, head in enumerate(heads):
        section_end = heads[i + 1].start() if i + 1 < len(heads) else len(block)
        body = block[head.end():section_end].strip()
        marks = list(re.finditer(r"([①②③④⑤])\s*", body))
        if [mark.group(1) for mark in marks] != ["①", "②", "③", "④", "⑤"]:
            raise ValueError(f"five-choice boundary incomplete at Q{head.group(1)}")
        stem = body[:marks[0].start()].strip()
        choices = [body[mark.end():marks[j + 1].start() if j + 1 < len(marks) else len(body)].strip()
                   for j, mark in enumerate(marks)]
        if not stem or any(not choice for choice in choices):
            raise ValueError(f"empty stem or choice at Q{head.group(1)}")
        questions[int(head.group(1))] = {"stem": stem, "choices": choices}
    return passage, questions


def main():
    candidates = read_jsonl(ROOT / "data/기본기_연구/code_study_candidates_v2.jsonl")
    targets = read_jsonl(TARGET)
    manifest = read_jsonl(MANIFEST)
    mappings = read_jsonl(MAPPING)
    answer_rows = read_jsonl(ANSWERS)
    restoration_rows = read_jsonl(RESTORATIONS) if RESTORATIONS.exists() else []
    candidate_by_id = {row["candidate_id"]: row for row in candidates}
    target_by_id = {row["candidate_id"]: row for row in targets}
    map_by_case = {row["case_id"]: row for row in mappings}
    prepared_ids = {row.get("candidate_id") for row in mappings if row.get("candidate_id")}
    prepared_ids.update(row.get("provenance", {}).get("candidate_id") for row in mappings)
    if len(candidate_by_id) != len(candidates) or len(target_by_id) != len(targets):
        raise ValueError("candidate/target identifier duplicates exist")

    map_index = json.loads(VISUAL_MAP.read_text(encoding="utf-8"))
    paper_by_year = {row["year"]: row for row in map_index["papers"] if row.get("label") == str(row.get("year"))}
    max_group = max(int(str(row.get("passage_group", "G000")).removeprefix("G")) for row in manifest)
    group_cursor = max_group + 1
    case_values = [sum((ord(ch) - 64) * (26 ** power) for power, ch in enumerate(reversed(row["case_id"])))
                   for row in manifest if re.fullmatch(r"[A-Z]+", row.get("case_id", ""))]
    case_cursor = max(case_values, default=0) + 1

    def alpha(number: int) -> str:
        chars = []
        while number:
            number, rem = divmod(number - 1, 26)
            chars.append(chr(65 + rem))
        return "".join(reversed(chars))

    staged = []
    for spec in GROUPS:
        year, start, end = spec["year"], spec["start"], spec["end"]
        source_rel = f"자료/LEET_언어이해/텍스트/{year}/{year}_question_odd.md"
        source_path = ROOT / source_rel
        source_bytes = source_path.read_bytes()
        source_text = source_bytes.decode("utf-8")
        passage, questions = parse_group(source_text, start, end)
        found = []
        for candidate in candidates:
            source = candidate.get("source", {})
            conn = candidate.get("canonical_connection", {})
            if source.get("exam_family") == "LEET" and source.get("year") == year and start <= source.get("question_number", -1) <= end:
                if conn.get("passage_id") == f"LEET-{year}-odd-Q{start:02d}-{end:02d}":
                    found.append(candidate)
        found.sort(key=lambda row: row["source"]["question_number"])
        if [row["source"]["question_number"] for row in found] != list(range(start, end + 1)):
            raise ValueError(f"candidate index does not identify exact LEET {year} Q{start}-{end}")
        already_prepared = [row["candidate_id"] in prepared_ids for row in found]
        if all(already_prepared):
            continue
        if any(already_prepared):
            raise ValueError(f"partially prepared candidate group; refusing overlap: {year} Q{start}-{end}")
        for candidate in found:
            cid = candidate["candidate_id"]
            if cid in prepared_ids:
                raise ValueError(f"candidate already prepared; refusing duplicate: {cid}")
            if target_by_id[cid].get("status") != "NOT_COMPLETED_NEEDS_RESTORE":
                raise ValueError(f"protected or changed target status; refusing: {cid} {target_by_id[cid].get('status')}")

        page_rel = spec["page"]
        page_path = ROOT / page_rel
        page_bytes = page_path.read_bytes()
        page_sha = sha256(page_bytes)
        page_image = Image.open(page_path)
        paper = paper_by_year.get(year)
        if not paper or paper.get("source_sha256") != sha_file(ROOT / paper["source_file"]):
            raise ValueError(f"official HWP page-render provenance mismatch for {year}")
        crop_records = {}
        for index, crop in enumerate(spec["crops"], start=1):
            box = tuple(crop["box"])
            if not (0 <= box[0] < box[2] <= page_image.width and 0 <= box[1] < box[3] <= page_image.height):
                raise ValueError("crop outside official rendered page")
            rel = f"data/기본기_연구/prepared_backlog/blind_sources/G{group_cursor:03d}_visual{index:02d}.png"
            out = ROOT / rel
            if out.exists():
                raise FileExistsError(f"visual output path conflict: {rel}")
            crop_image = page_image.crop(box)
            from io import BytesIO
            buff = BytesIO()
            crop_image.save(buff, format="PNG")
            data = buff.getvalue()
            crop_records[crop["key"]] = {
                "rel": rel, "bytes": data, "sha256": sha256(data), "box": list(box),
                "scope": crop["scope"], "page_sha256": page_sha,
                "render_path": page_rel, "official_hwp_source": paper["source_file"],
                "official_hwp_sha256": paper["source_sha256"],
                "page_index_zero_based": int(Path(page_rel).stem.split("_")[-1]) - 1,
            }

        group_id = f"G{group_cursor:03d}"
        group_case_ids = [alpha(case_cursor + i) for i in range(len(found))]
        case_ids_all = {row["case_id"] for row in manifest}
        if any(case_id in case_ids_all for case_id in group_case_ids):
            raise ValueError("case identifier collision")
        blind_dir = BASE / "blind_sources"
        packet_dir = BASE / "packets"
        planned_paths = [blind_dir / f"{case_id}.json" for case_id in group_case_ids]
        planned_paths += [packet_dir / f"{case_id}.md" for case_id in group_case_ids]
        planned_paths += [packet_dir / f"{group_case_ids[0]}.json"]
        if any(path.exists() for path in planned_paths):
            raise FileExistsError("case/packet output path conflict")

        group_blinds, group_maps, group_manifest, group_answers, group_target_updates = [], [], [], [], []
        for i, candidate in enumerate(found):
            qn = candidate["source"]["question_number"]
            case_id = group_case_ids[i]
            q = questions[qn]
            passage_text = passage
            stem = q["stem"]
            supplements = []
            linked_assets = []
            marker_crop_keys = ["passage"] if "passage" in crop_records else ["target"]
            for key in marker_crop_keys:
                record = crop_records[key]
                if record["rel"] not in [item["file"] for item in supplements]:
                    supplements.append({"file": record["rel"], "media_type": "image/png"})
                linked_assets.append({**{k: v for k, v in record.items() if k not in {"bytes", "rel"}},
                                      "blind_asset": record["rel"], "blind_asset_sha256": record["sha256"]})
            passage_text, count = re.subn(r"\s*<(?:그림|표)>\s*", " [시각 자료 1] ", passage_text)
            if count != 1:
                raise ValueError(f"expected exactly one common-passage visual marker, found {count}: {year} Q{start}-{end}")
            stem_marker = re.search(r"<(?:그림|표)>", stem)
            if stem_marker:
                q_key = f"q{qn}"
                if q_key in crop_records:
                    record = crop_records[q_key]
                else:
                    record = crop_records.get("target")
                if record is None:
                    raise ValueError("question stem visual has no exact crop source")
                if record["rel"] not in [item["file"] for item in supplements]:
                    supplements.append({"file": record["rel"], "media_type": "image/png"})
                linked_assets.append({**{k: v for k, v in record.items() if k not in {"bytes", "rel"}},
                                      "blind_asset": record["rel"], "blind_asset_sha256": record["sha256"],
                                      "scope": f"Q{qn} stem target reference"})
                stem = re.sub(r"\s*<(?:그림|표)>\s*", " [시각 자료 2] " if record["rel"] != crop_records[marker_crop_keys[0]]["rel"] else " [시각 자료 1] ", stem)
            all_texts = [passage_text, stem, *q["choices"]]
            if any(re.search(r"<(?:그림|표)>|!\[", value) for value in all_texts):
                raise ValueError("unresolved required visual marker")
            blind = {
                "blind_only": True, "passage_group": group_id, "case_id": case_id,
                "provenance": {"source_role": "anonymous_blind_source"},
                "passage_text": passage_text, "stem": stem, "choices": q["choices"],
                "visual_supplements": supplements,
            }
            allowed_keys = {"blind_only", "passage_group", "case_id", "provenance", "passage_text", "stem", "choices", "visual_supplements"}
            if set(blind) != allowed_keys or len(blind["choices"]) != 5 or not blind["stem"].strip() or not blind["passage_text"].strip():
                raise ValueError("blind source structure invalid")
            if any(not choice.strip() for choice in blind["choices"]):
                raise ValueError("empty choice")
            blind_rel = f"data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json"
            group_blinds.append((blind_rel, blind))
            conn = candidate["canonical_connection"]
            source_meta = {
                "candidate_id": candidate["candidate_id"],
                "exam_family": "LEET", "academic_year": year,
                "exam_label": candidate["source"]["exam_type"], "question_number": qn,
                "question_id": conn["question_id"], "passage_id": conn["passage_id"],
                "source_path": source_rel, "canonical_source_path": source_rel,
                "source_sha256": sha256(source_bytes), "source_type": "canonical_leet_odd_markdown",
                "official_pages": [], "linked_visual_assets": linked_assets,
                "source_role": "sealed_provenance_mapping",
            }
            group_maps.append({"case_id": case_id, "passage_group": group_id, "group_case_ids": group_case_ids,
                               "provenance": source_meta, "source_status": "exact_canonical_leet_odd"})
            group_answers.append({"case_id": case_id, "candidate_id": candidate["candidate_id"],
                                  "official_answer": None,
                                  "official_answer_source": "not accessed during source preparation; resolve after group blind barrier",
                                  "site_original_codes": None, "site_marked_answer": None,
                                  "source_role": "sealed_for_after_blind", "passage_group": conn["passage_id"],
                                  "release_rule": RULES[0]})
            group_manifest.append({"case_id": case_id, "status": "prepared", "passage_group": group_id,
                                  "group_case_ids": group_case_ids, "group_release_rules": RULES,
                                  "blind_source": blind_rel,
                                  "exclusion_checks": {"exposure_status": "unknown", "semantic_review": "not_reviewed",
                                    "source_quality": {"visual_placeholder": False, "canonical_link": "exact",
                                      "choice_parse": "complete", "text_markers_preserved": True,
                                      "source_verification": "exact_canonical_leet_odd_markdown_with_targeted_official_visual_crop"}}})
            target = dict(target_by_id[candidate["candidate_id"]])
            target["status"] = "NOT_COMPLETED_READY_LOCAL_SOURCE"
            target["match_method"] = "canonical_markdown_plus_exact_official_visual_crop"
            target["match_evidence"] = {**(target.get("match_evidence") or {}),
                "previous_source_preflight_status": "NEEDS_RESTORE", "source_path": source_rel,
                "source_sha256": sha256(source_bytes), "required_visual_restore": "exact cropped marked target only",
                "blind_linkage": "exact candidate_id + canonical question_id + passage range"}
            target["matched_case_id"] = None
            target["matched_passage_group"] = None
            group_target_updates.append(target)

        packet = {"blind_packet": True, "passage_group": group_id, "group_case_ids": group_case_ids,
                  "group_release_rules": RULES,
                  "source_files": [f"data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json" for case_id in group_case_ids]}
        packet_md = "\n".join([f"# Blind source packet — {group_id}", "",
                               "all_group_blind_records_before_any_group_answer_check",
                               "all_group_independent_code_records_before_any_group_sdss_disclosure", "",
                               *[f"- {case_id}: `{blind_rel}`" for case_id, (blind_rel, _) in zip(group_case_ids, group_blinds)], ""])
        restore_log = {"passage_group": group_id, "family": "LEET", "year": year,
            "question_range": [start, end], "source_priority": "verified transcript if exact; otherwise canonical odd Markdown",
            "selected_text_source": source_rel, "source_sha256": sha256(source_bytes),
            "visual_fallback": [{k: v for k, v in record.items() if k not in {"bytes", "rel"}}
                                for record in crop_records.values()],
            "case_ids": group_case_ids, "restoration_type": "source_preparation_only"}
        staged.append({"group_id": group_id, "case_ids": group_case_ids, "crops": crop_records,
                       "blinds": group_blinds, "maps": group_maps, "answers": group_answers,
                       "manifest": group_manifest, "target_updates": group_target_updates,
                       "packet": packet, "packet_md": packet_md, "restore_log": restore_log,
                       "case_cursor": case_cursor, "group_number": group_cursor})
        prepared_ids.update(row["candidate_id"] for row in found)
        group_cursor += 1
        case_cursor += len(found)

    # Validate all output paths and duplicate identities before writing.
    all_case_ids = [case_id for item in staged for case_id in item["case_ids"]]
    if len(set(all_case_ids)) != len(all_case_ids):
        raise ValueError("duplicate new case IDs")
    all_candidate_ids = [row["provenance"]["candidate_id"] for item in staged for row in item["maps"]]
    if len(set(all_candidate_ids)) != len(all_candidate_ids):
        raise ValueError("duplicate new candidate IDs")
    existing_case_ids = {row["case_id"] for row in manifest}
    existing_candidate_ids = {row.get("provenance", {}).get("candidate_id") for row in mappings}
    if set(all_case_ids) & existing_case_ids or set(all_candidate_ids) & existing_candidate_ids:
        raise ValueError("duplicate with existing manifest/provenance")

    target_updates = {row["candidate_id"]: row for item in staged for row in item["target_updates"]}
    updated_targets = [target_updates.get(row["candidate_id"], row) for row in targets]
    new_manifest = manifest + [row for item in staged for row in item["manifest"]]
    new_mappings = mappings + [row for item in staged for row in item["maps"]]
    new_answers = answer_rows + [row for item in staged for row in item["answers"]]
    new_restorations = restoration_rows + [item["restore_log"] for item in staged]

    writes = []
    for item in staged:
        for record in item["crops"].values():
            writes.append((ROOT / record["rel"], record["bytes"]))
        for rel, blind in item["blinds"]:
            writes.append((ROOT / rel, (json.dumps(blind, ensure_ascii=False, indent=2) + "\n").encode("utf-8")))
            cid = blind["case_id"]
            writes.append((BASE / "packets" / f"{cid}.md", item["packet_md"].encode("utf-8")))
        writes.append((BASE / "packets" / f"{item['case_ids'][0]}.json", (json.dumps(item["packet"], ensure_ascii=False, indent=2) + "\n").encode("utf-8")))
    writes.extend([
        (MANIFEST, jsonl_bytes(new_manifest)), (MAPPING, jsonl_bytes(new_mappings)),
        (ANSWERS, jsonl_bytes(new_answers)), (TARGET, jsonl_bytes(updated_targets)),
        (RESTORATIONS, jsonl_bytes(new_restorations)),
    ])
    paths = [path for path, _ in writes]
    if len(set(paths)) != len(paths) or any(path.exists() for path in paths if path not in {MANIFEST, MAPPING, ANSWERS, TARGET, RESTORATIONS}):
        raise FileExistsError("one or more prepared output paths conflict")
    for path, data in writes:
        atomic_write(path, data)
    print(json.dumps({"prepared_groups": len(staged), "prepared_questions": len(all_case_ids),
                      "group_range": [staged[0]["group_id"], staged[-1]["group_id"]],
                      "case_range": [all_case_ids[0], all_case_ids[-1]],
                      "candidate_count": len(all_candidate_ids), "queue_processed_touched": False}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
