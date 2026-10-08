#!/usr/bin/env python3
"""Restore LEET groups whose only missing marker is a terminal admin box."""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from tempfile import NamedTemporaryFile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/기본기_연구/prepared_backlog"
TARGET = ROOT / "data/기본기_연구/target_completion_crosswalk_v1.jsonl"
MANIFEST = BASE / "manifest.jsonl"
MAPPING = BASE / "sealed/provenance_mapping.jsonl"
ANSWERS = BASE / "sealed/answer_sdss.jsonl"
RESTORATIONS = BASE / "sealed/source_restorations_v1.jsonl"
RULES = ["all_group_blind_records_before_any_group_answer_check",
         "all_group_independent_code_records_before_any_group_sdss_disclosure"]
GROUPS = [
    {"year": 2012, "page": "자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2012/page_015.png",
     "hwp": "자료/LEET_언어이해/원본/2012/2012_question_odd_2012_법학적성시험_언어이해(홀수형).hwp"},
]


def read_jsonl(p):
    return [json.loads(s) for s in p.read_text(encoding="utf-8").splitlines() if s.strip()]


def digest(b):
    return hashlib.sha256(b).hexdigest()


def atomic(p, b):
    with NamedTemporaryFile("wb", dir=p.parent, delete=False) as f:
        f.write(b); tmp = Path(f.name)
    os.replace(tmp, p)


def as_jsonl(rows):
    return "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in rows).encode()


def alpha_value(s):
    n = 0
    for ch in s: n = n * 26 + ord(ch) - 64
    return n


def alpha(n):
    out = ""
    while n:
        n, r = divmod(n - 1, 26); out = chr(65 + r) + out
    return out


def extract(markdown):
    ranges = list(re.finditer(r"^\[(\d+)\s*[~～〜-](\d+)\][^\n]*$", markdown, re.M))
    found = [i for i, m in enumerate(ranges) if (int(m[1]), int(m[2])) == (33, 35)]
    if len(found) != 1: raise ValueError("exact [33~35] range missing")
    i = found[0]; m = ranges[i]
    end = ranges[i + 1].start() if i + 1 < len(ranges) else len(markdown)
    block = markdown[m.end():end]
    if not re.search(r"\n\s*<표>\s*$", block): raise ValueError("terminal admin marker is not exact")
    block = re.sub(r"\n\s*<표>\s*$", "\n", block)
    heads = list(re.finditer(r"^\s*(3[3-5])\.\s*", block, re.M))
    questions = {}
    if [int(x[1]) for x in heads] == [33, 34, 35]:
        passage = block[:heads[0].start()].strip()
        for j, h in enumerate(heads):
            body = block[h.end():heads[j + 1].start() if j + 1 < len(heads) else len(block)].strip()
            marks = list(re.finditer(r"([①②③④⑤])\s*", body))
            if [x[1] for x in marks] != list("①②③④⑤"): raise ValueError(f"choice boundary invalid at {h[1]}")
            stem = body[:marks[0].start()].strip()
            choices = [body[x.end():marks[k + 1].start() if k + 1 < len(marks) else len(body)].strip() for k, x in enumerate(marks)]
            if not stem or any(not x for x in choices): raise ValueError(f"empty source at Q{h[1]}")
            questions[int(h[1])] = {"stem": stem, "choices": choices}
    else:
        # Exact range and five-choice cycles are preserved in the 2012
        # canonical transcription even though its question stems are unnumbered.
        labels = [m for m in re.finditer(r"([①②③④⑤])\s*", block)]
        cycles = []
        i = 0
        while i + 4 < len(labels):
            if "".join(m[1] for m in labels[i:i + 5]) == "①②③④⑤":
                cycles.append(labels[i:i + 5]); i += 5
            else: i += 1
        if len(cycles) != 3: raise ValueError("legacy Q33-35 five-choice cycles missing")
        def stem_cut(tail):
            def prompt_ok(right):
                prompt = re.split(r"\n\s*<(?:그림|표)", right, maxsplit=1)[0].strip()
                return len(prompt) >= 12 and prompt.endswith(("?", "？")) and not re.search(r"[①②③④⑤]", prompt)
            blanks = list(re.finditer(r"\n\s*\n", tail))
            for match in reversed(blanks):
                left = tail[:match.start()].strip(); right = tail[match.end():].strip()
                if left and prompt_ok(right): return match.start()
            for match in reversed(list(re.finditer(r"\n", tail))):
                left = tail[:match.start()].strip(); right = tail[match.end():].strip()
                if left and prompt_ok(right): return match.start()
            return -1
        prefix = block[:cycles[0][0].start()]
        first_cut = stem_cut(prefix)
        if first_cut < 0: raise ValueError("legacy first stem boundary missing")
        passage = prefix[:first_cut].strip()
        first_stem = prefix[first_cut:].strip()
        stems = [first_stem]
        choice_ends = [None, None, len(block)]
        for ci in (1, 2):
            prev = cycles[ci - 1][4]
            current = cycles[ci][0]
            between = block[prev.end():current.start()]
            cut = stem_cut(between)
            if cut < 0: raise ValueError(f"legacy Q{32+ci} stem boundary missing")
            sep = 2 if between[cut:cut + 2] == "\n\n" else 1
            choice_ends[ci - 1] = prev.end() + cut
            stems.append(between[cut + sep:].strip())
        for ci, cycle in enumerate(cycles):
            choice_end = choice_ends[ci]
            choices = []
            for j, mark in enumerate(cycle):
                stop = cycle[j + 1].start() if j < 4 else choice_end
                choices.append(block[mark.end():stop].strip())
            qn = 33 + ci
            if not stems[ci] or any(not x for x in choices): raise ValueError(f"legacy source incomplete at Q{qn}")
            questions[qn] = {"stem": stems[ci], "choices": choices}
    if set(questions) != {33, 34, 35} or not passage:
        raise ValueError("Q33-35 passage linkage incomplete")
    if re.search(r"<(?:그림|표)>|!\[", passage + "".join(q["stem"] + "".join(q["choices"]) for q in questions.values())):
        raise ValueError("unresolved source visual marker after footer removal")
    return passage, questions


def main():
    candidates = read_jsonl(ROOT / "data/기본기_연구/code_study_candidates_v2.jsonl")
    targets = read_jsonl(TARGET); manifest = read_jsonl(MANIFEST)
    mappings = read_jsonl(MAPPING); answers = read_jsonl(ANSWERS)
    logs = read_jsonl(RESTORATIONS) if RESTORATIONS.exists() else []
    target_by_id = {x["candidate_id"]: x for x in targets}
    prepared_candidates = {x.get("provenance", {}).get("candidate_id") for x in mappings}
    next_group = max(int(str(x.get("passage_group", "G000")).removeprefix("G")) for x in manifest) + 1
    next_case = max((alpha_value(x["case_id"]) for x in manifest if re.fullmatch(r"[A-Z]+", x.get("case_id", ""))), default=0) + 1
    added_manifest, added_maps, added_answers, updates, added_logs, writes = [], [], [], {}, [], []

    for spec in GROUPS:
        year = spec["year"]; pid = f"LEET-{year}-odd-Q33-35"
        selected = [x for x in candidates if x.get("source", {}).get("exam_family") == "LEET"
                    and x.get("source", {}).get("year") == year and x.get("source", {}).get("question_number") in (33, 34, 35)
                    and x.get("canonical_connection", {}).get("passage_id") == pid]
        selected.sort(key=lambda x: x["source"]["question_number"])
        if [x["source"]["question_number"] for x in selected] != [33, 34, 35]:
            raise ValueError(f"candidate linkage incomplete for {pid}")
        if all(x["candidate_id"] in prepared_candidates for x in selected):
            continue
        if any(x["candidate_id"] in prepared_candidates for x in selected):
            raise ValueError(f"partially prepared passage group {pid}")
        for x in selected:
            if target_by_id[x["candidate_id"]]["status"] != "NOT_COMPLETED_NEEDS_RESTORE":
                raise ValueError(f"protected target encountered: {x['candidate_id']}")

        source_rel = f"자료/LEET_언어이해/텍스트/{year}/{year}_question_odd.md"
        source_path = ROOT / source_rel; source_bytes = source_path.read_bytes()
        passage, qs = extract(source_bytes.decode("utf-8"))
        page_path = ROOT / spec["page"]; page_bytes = page_path.read_bytes()
        hwp_path = ROOT / spec["hwp"]
        if not hwp_path.is_file(): raise FileNotFoundError(spec["hwp"])
        group_id = f"G{next_group:03d}"; cases = [alpha(next_case + i) for i in range(3)]
        for case_id in cases:
            if (BASE / "blind_sources" / f"{case_id}.json").exists() or (BASE / "packets" / f"{case_id}.md").exists():
                raise FileExistsError(f"output conflict at {case_id}")
        if (BASE / "packets" / f"{cases[0]}.json").exists(): raise FileExistsError("packet JSON conflict")
        log = {"passage_group": group_id, "family": "LEET", "year": year, "question_range": [33, 35],
               "selected_text_source": source_rel, "source_sha256": digest(source_bytes),
               "terminal_marker": "<표>", "terminal_marker_disposition": "excluded after page-local official visual verification as administrative confirmation box after Q35",
               "page_render_verification": {"file": spec["page"], "sha256": digest(page_bytes), "hwp_source": spec["hwp"],
                  "hwp_sha256": digest(hwp_path.read_bytes()), "scope": "last-page administrative confirmation box only; no blind asset created"},
               "case_ids": cases, "restoration_type": "source_preparation_only"}
        for i, candidate in enumerate(selected):
            qn = candidate["source"]["question_number"]
            case_id = cases[i]; conn = candidate["canonical_connection"]
            blind = {"blind_only": True, "passage_group": group_id, "case_id": case_id,
                     "provenance": {"source_role": "anonymous_blind_source"}, "passage_text": passage,
                     "stem": qs[qn]["stem"], "choices": qs[qn]["choices"]}
            rel = f"data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json"
            writes.append((BASE / "blind_sources" / f"{case_id}.json", (json.dumps(blind, ensure_ascii=False, indent=2) + "\n").encode()))
            source_meta = {"candidate_id": candidate["candidate_id"], "exam_family": "LEET", "academic_year": year,
                "exam_label": candidate["source"]["exam_type"], "question_number": qn, "question_id": conn["question_id"],
                "passage_id": pid, "source_path": source_rel, "canonical_source_path": source_rel,
                "source_sha256": digest(source_bytes), "source_type": "canonical_leet_odd_markdown",
                "official_pages": [], "linked_visual_assets": [], "source_role": "sealed_provenance_mapping"}
            added_maps.append({"case_id": case_id, "passage_group": group_id, "group_case_ids": cases,
                               "provenance": source_meta, "source_status": "exact_canonical_leet_odd"})
            added_answers.append({"case_id": case_id, "candidate_id": candidate["candidate_id"], "official_answer": None,
                "official_answer_source": "not accessed during source preparation; resolve after group blind barrier",
                "site_original_codes": None, "site_marked_answer": None, "source_role": "sealed_for_after_blind",
                "passage_group": pid, "release_rule": RULES[0]})
            added_manifest.append({"case_id": case_id, "status": "prepared", "passage_group": group_id,
                "group_case_ids": cases, "group_release_rules": RULES, "blind_source": rel,
                "exclusion_checks": {"exposure_status": "unknown", "semantic_review": "not_reviewed",
                    "source_quality": {"visual_placeholder": False, "canonical_link": "exact", "choice_parse": "complete",
                        "text_markers_preserved": True, "source_verification": "canonical_markdown_terminal_admin_marker_excluded"}}})
            target = dict(target_by_id[candidate["candidate_id"]]); target["status"] = "NOT_COMPLETED_READY_LOCAL_SOURCE"
            target["match_method"] = "canonical_markdown_terminal_admin_marker_excluded"
            target["match_evidence"] = {**(target.get("match_evidence") or {}), "previous_source_preflight_status": "NEEDS_RESTORE",
                "source_path": source_rel, "source_sha256": digest(source_bytes),
                "footer_marker_disposition": "terminal <표> excluded as administrative confirmation box after Q35, verified on official last page",
                "blind_linkage": "exact candidate_id + canonical question_id + passage range"}
            target["matched_case_id"] = None; target["matched_passage_group"] = None; updates[target["candidate_id"]] = target
        packet = {"blind_packet": True, "passage_group": group_id, "group_case_ids": cases,
                  "group_release_rules": RULES, "source_files": [f"data/기본기_연구/prepared_backlog/blind_sources/{c}.json" for c in cases]}
        packet_md = "\n".join([f"# Blind source packet — {group_id}", "",
                              "all_group_blind_records_before_any_group_answer_check",
                              "all_group_independent_code_records_before_any_group_sdss_disclosure", "",
                              *[f"- {case_id}: `data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json`" for case_id in cases], ""])
        for case_id in cases: writes.append((BASE / "packets" / f"{case_id}.md", packet_md.encode()))
        writes.append((BASE / "packets" / f"{cases[0]}.json", (json.dumps(packet, ensure_ascii=False, indent=2) + "\n").encode()))
        added_logs.append(log); next_group += 1; next_case += 3
        prepared_candidates.update(x["candidate_id"] for x in selected)

    next_targets = [updates.get(row["candidate_id"], row) for row in targets]
    files = [p for p, _ in writes] + [MANIFEST, MAPPING, ANSWERS, TARGET, RESTORATIONS]
    if len(files) != len(set(files)): raise ValueError("write path collision")
    for p, data in writes: atomic(p, data)
    for p, rows in [(MANIFEST, manifest + added_manifest), (MAPPING, mappings + added_maps),
                    (ANSWERS, answers + added_answers), (TARGET, next_targets), (RESTORATIONS, logs + added_logs)]:
        atomic(p, as_jsonl(rows))
    print(json.dumps({"prepared_groups": len(added_logs), "prepared_questions": len(added_manifest),
                      "group_range": [log["passage_group"] for log in added_logs] if added_logs else [],
                      "case_ids": [row["case_id"] for row in added_manifest], "answer_or_SDSS_used": False}, ensure_ascii=False, indent=2))


if __name__ == "__main__": main()
