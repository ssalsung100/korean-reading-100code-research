#!/usr/bin/env python3
"""Build a review-only 100-code study index from local canonical corpora.

This is deliberately a join, not a code classifier.  SDSS labels remain
third-party candidate labels; an official answer match only establishes that
the local question/answer reference is usable for later human review.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "data/code_candidate_review_queue.jsonl"
CATALOG = ROOT / "data/sdss_100codes_catalog.json"
KICE_QUESTIONS = ROOT / "data/kice_questions.jsonl"
MEET_QUESTIONS = ROOT / "data/meet_questions.jsonl"
MEET_VISUALS = ROOT / "data/meet_visuals.jsonl"
LEET_ANSWERS = ROOT / "자료/LEET_언어이해/normalized_answers.json"
LEET_VISUALS = ROOT / "자료/LEET_언어이해/검증/LEET_홀수형_시각자료_전체목록_v1.json"
LEET_VISUAL_MAPPING = ROOT / "자료/LEET_언어이해/검증/HWP_홀수형_시각자료_문항매핑_v1.json"
LEET_VERIFIED = ROOT / "자료/LEET_언어이해/전사_검수완료/manifest.json"

OUT_DIR = ROOT / "data/기본기_연구"
OUT_CANDIDATES = OUT_DIR / "code_study_candidates_v2.jsonl"
OUT_COVERAGE = OUT_DIR / "code_study_coverage_v2.json"
OUT_REPORT = ROOT / "분석/기본기_연구/100코드_사례연결_현황_v2.md"
CIRCLED = "①②③④⑤"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def compact_label(value: str) -> str:
    """Normalize display-only differences, without semantic synonym guessing."""
    return re.sub(r"[\s·ㆍ\-_/]", "", value).lower()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def answer_symbol(value: int | None) -> str | None:
    return CIRCLED[value - 1] if value is not None and 1 <= value <= 5 else None


def kice_target(site: dict[str, Any]) -> tuple[str, str | None, str | None] | None:
    return {
        "수능국어": ("수능", None, None),
        "수능국어B형": ("수능", None, "B"),
        "6평국어": ("수능 모의평가", "6월", None),
        "6평국어A형": ("수능 모의평가", "6월", "A"),
        "9평국어": ("수능 모의평가", "9월", None),
    }.get(site["exam_type"])


def make_catalog_maps(catalog: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, set[int]], dict[str, set[int]], dict[str, str]]:
    by_name = {code["name"]: code for code in catalog["codes"]}
    canonical: dict[str, set[int]] = defaultdict(set)
    aliases: dict[str, set[int]] = defaultdict(set)
    urls: dict[str, str] = {}
    for code in catalog["codes"]:
        canonical[compact_label(code["name"])].add(code["number"])
        for alias in code["aliases"]:
            aliases[compact_label(alias)].add(code["number"])
    for item in catalog.get("search_sources", []):
        urls[item["code_name"]] = item["url"]
    return by_name, canonical, aliases, urls


def resolve_display_label(label: str, canonical: dict[str, set[int]], aliases: dict[str, set[int]]) -> dict[str, Any]:
    key = compact_label(label)
    canonical_ids = sorted(canonical.get(key, set()))
    alias_ids = sorted(aliases.get(key, set()))
    all_ids = sorted(set(canonical_ids) | set(alias_ids))
    # A catalog's canonical display name has an explicit hierarchy over an
    # alias.  Equal-level multiple canonical/alias hits are never guessed.
    if len(canonical_ids) == 1:
        status = "canonical_name_exact"
        resolved = canonical_ids
    elif len(canonical_ids) > 1 or len(all_ids) > 1:
        status = "ambiguous_catalog_name_or_alias"
        resolved = []
    elif len(alias_ids) == 1:
        status = "unique_catalog_alias"
        resolved = alias_ids
    else:
        status = "unresolved_catalog_name"
        resolved = []
    return {
        "site_label": label,
        "normalized_label": key,
        "status": status,
        "resolved_code_ids": resolved,
        "canonical_name_candidate_ids": canonical_ids,
        "alias_candidate_ids": alias_ids,
    }


def leet_group_index() -> dict[tuple[str, int], tuple[str, str]]:
    """Return stable group IDs from printed [start~end] ranges, never titles."""
    output: dict[tuple[str, int], tuple[str, str]] = {}
    text_root = ROOT / "자료/LEET_언어이해/텍스트"
    for path in text_root.glob("*/**/*question_odd.md"):
        label = path.parent.name
        matches = re.findall(r"\[(\d+)(?:\s*[~∼～\-]\s*(\d+))?\]", path.read_text(encoding="utf-8"))
        for start_text, end_text in matches:
            start = int(start_text)
            end = int(end_text or start_text)
            group_id = f"LEET-{label}-odd-Q{start:02d}-{end:02d}"
            for question in range(start, end + 1):
                old = output.get((label, question))
                if old and old[0] != group_id:
                    raise ValueError(f"LEET printed range overlap: {label} {question}")
                output[(label, question)] = (group_id, str(path.relative_to(ROOT)))
    return output


def source_visuals() -> tuple[dict[str, list[dict[str, Any]]], dict[tuple[str, int], list[dict[str, Any]]]]:
    meet: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in read_jsonl(MEET_VISUALS):
        for question_id in item.get("linked_question_ids", []):
            meet[question_id].append({
                "visual_id": item["visual_id"],
                "role": item["role"],
                "representation": item["representation"],
                "semantic_visual": item["semantic_visual"],
                "source_file": item.get("original_file") or item.get("canonical_markdown"),
            })
    leet: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    payload = json.loads(LEET_VISUALS.read_text(encoding="utf-8"))
    for item in payload.get("records", []):
        start, end = item["question_group"]
        for question in range(start, end + 1):
            leet[(item["label"], question)].append({
                "asset_kind": item["asset_kind"],
                "authoritative_file": item["authoritative_file"],
                "mapping_confidence": item["mapping_confidence"],
            })
    # The reusable catalog intentionally omits ordinary structured <보기>
    # boxes.  The HWP mapping is therefore also consulted and retained as a
    # conservative review link; it does not claim page-layout certainty.
    mapping = json.loads(LEET_VISUAL_MAPPING.read_text(encoding="utf-8"))
    for paper in mapping.get("papers", []):
        for item in paper.get("assets", []):
            start, end = item["question_group"]
            for question in range(start, end + 1):
                leet[(item["label"], question)].append({
                    "asset_kind": item["kind"],
                    "authoritative_file": item["file"],
                    "mapping_confidence": item.get("mapping_confidence", "stream_order_mapped"),
                    "mapping_source": "HWP_홀수형_시각자료_문항매핑_v1.json",
                })
    return meet, leet


def build_indexes() -> dict[str, Any]:
    kice = defaultdict(list)
    for question in read_jsonl(KICE_QUESTIONS):
        key = (question["academic_year"], question["exam_type"], question.get("month"), question.get("variant"), question["question_number"])
        kice[key].append(question)
    meet = {(item["label"], item["number"]): item for item in read_jsonl(MEET_QUESTIONS)}
    answers = json.loads(LEET_ANSWERS.read_text(encoding="utf-8"))["records"]
    leet_answers = {(item["label"], item["variant"]): item for item in answers if item.get("status") in {"parsed", "verified_visual"}}
    verified = json.loads(LEET_VERIFIED.read_text(encoding="utf-8"))["records"]
    leet_verified = {(item["year"], question): item for item in verified for question in item["questions"]}
    meet_visuals, leet_visuals = source_visuals()
    return {
        "kice": kice, "meet": meet, "leet_answers": leet_answers,
        "leet_verified": leet_verified, "leet_groups": leet_group_index(),
        "meet_visuals": meet_visuals, "leet_visuals": leet_visuals,
    }


def connect_kice(site: dict[str, Any], indexes: dict[str, Any]) -> dict[str, Any]:
    target = kice_target(site)
    if target is None:
        return {"status": "unsupported_kice_exam_label", "question_id": None, "passage_id": None, "source_path": None, "official_answer": None, "official_answer_source": None, "visual_material": {"status": "unknown"}}
    exam_type, month, variant = target
    candidates = indexes["kice"].get((site["year"], exam_type, month, variant, site["question"]), [])
    if len(candidates) != 1:
        return {"status": "ambiguous_kice_match" if candidates else "kice_question_not_in_local_reading_scope", "question_id": None, "passage_id": None, "source_path": "data/kice_questions.jsonl" if candidates else None, "official_answer": None, "official_answer_source": None, "visual_material": {"status": "unknown"}}
    item = candidates[0]
    # `choice_parse_status=complete` is not enough: one known KICE record has
    # five empty strings because the answer table was not captured as text.
    choices_complete = (
        isinstance(item.get("choices"), list)
        and len(item["choices"]) == 5
        and all(isinstance(choice, str) and choice.strip() for choice in item["choices"])
    )
    visual = item.get("contains_visual_placeholder", False) or not choices_complete
    return {
        "status": "exact_canonical_kice_question" if choices_complete else "exact_canonical_kice_question_visual_choice_review_required",
        "question_id": item["question_id"], "passage_id": item["passage_id"],
        "source_path": "data/kice_questions.jsonl", "official_answer": item["answer"],
        "official_answer_source": "data/kice_questions.jsonl (official_answer_verified)",
        "source_verification": {"official_answer_verified": item["official_answer_verified"], "answer_link_status": item["answer_link_status"], "choice_parse_status": item["choice_parse_status"], "five_nonempty_text_choices": choices_complete},
        "visual_material": {"status": "review_required" if visual else "not_indicated_by_question_record", "evidence": "contains_visual_placeholder_or_missing_choice_text" if visual else None},
    }


def connect_meet(site: dict[str, Any], indexes: dict[str, Any]) -> dict[str, Any]:
    label = "2005예비" if site["exam_type"] == "미트예비" else str(site["year"])
    item = indexes["meet"].get((label, site["question"]))
    if item is None:
        return {"status": "meet_question_not_in_canonical_jsonl", "question_id": None, "passage_id": None, "source_path": None, "official_answer": None, "official_answer_source": None, "visual_material": {"status": "unknown"}}
    visuals = indexes["meet_visuals"].get(item["question_id"], [])
    return {
        "status": "exact_canonical_meet_jsonl",
        "question_id": item["question_id"], "passage_id": item["group_id"],
        "source_path": "data/meet_questions.jsonl", "official_answer": item["answer"],
        "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
        "source_verification": item["source"].get("verification_status"),
        "visual_material": {"status": "review_required" if visuals else "not_indicated_by_meet_visual_index", "linked_assets": visuals},
    }


def connect_leet(site: dict[str, Any], indexes: dict[str, Any]) -> dict[str, Any]:
    if site["exam_type"] == "리트예비" and site["year"] != 2009:
        # The site has legacy 2008 preliminary rows, but the local canonical
        # scope starts with the 2009 preliminary paper.  Do not coerce them.
        return {"status": "leet_preliminary_year_not_in_canonical_scope", "question_id": None, "passage_id": None, "source_path": None, "official_answer": None, "official_answer_source": None, "visual_material": {"status": "unknown"}}
    label = "2009예비" if site["exam_type"] == "리트예비" else str(site["year"])
    answer_record = indexes["leet_answers"].get((label, "odd"))
    group = indexes["leet_groups"].get((label, site["question"]))
    if answer_record is None or group is None:
        return {"status": "leet_question_not_in_canonical_odd_scope", "question_id": None, "passage_id": None, "source_path": None, "official_answer": None, "official_answer_source": None, "visual_material": {"status": "unknown"}}
    verified = indexes["leet_verified"].get((site["year"], site["question"]))
    assets = indexes["leet_visuals"].get((label, site["question"]), [])
    source_path = verified["file"] if verified else group[1]
    return {
        "status": "exact_verified_leet_transcript" if verified else "exact_canonical_leet_odd",
        "question_id": f"LEET-{label}-odd-Q{site['question']:02d}", "passage_id": group[0],
        "source_path": source_path, "official_answer": answer_record["answers"].get(str(site["question"])),
        "official_answer_source": answer_record["source_file"],
        "source_verification": "official_page_visual_transcription_verified" if verified else "LEET corpus verification gate PASS; canonical odd-form text",
        "visual_material": {"status": "review_required" if assets else "not_indicated_by_reusable_visual_catalog", "linked_assets": assets, "caveat": "The LEET catalog separately notes uncataloged structured <보기> boxes."},
    }


def connect(site: dict[str, Any], indexes: dict[str, Any]) -> dict[str, Any]:
    if site["exam_family"] == "KICE":
        return connect_kice(site, indexes)
    if site["exam_family"] == "MEET":
        return connect_meet(site, indexes)
    if site["exam_family"] == "LEET":
        return connect_leet(site, indexes)
    return {"status": "unsupported_exam_family", "question_id": None, "passage_id": None, "source_path": None, "official_answer": None, "official_answer_source": None, "visual_material": {"status": "unknown"}}


def is_canonical(connection: dict[str, Any]) -> bool:
    return connection["status"].startswith("exact_canonical_") or connection["status"].startswith("exact_verified_")


def candidate_id(site: dict[str, Any]) -> str:
    payload = "|".join(str(site[key]) for key in ("exam_family", "year", "exam_type", "question", "title"))
    return "CAND-" + hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def choose_diverse(records: list[dict[str, Any]], code_id: int, limit: int = 10) -> list[dict[str, Any]]:
    eligible = [r for r in records if code_id in r["code_normalization"]["query_catalog_code_ids"] and is_canonical(r["canonical_connection"])]
    # Passage ID is the de-duplication key; titles deliberately do not decide it.
    eligible.sort(key=lambda r: (r["source"]["exam_family"], r["source"]["year"], r["canonical_connection"]["passage_id"] or "", r["source"]["question_number"], r["candidate_id"]))
    selected, used_passages, used_families = [], set(), set()
    for prefer_new_family in (True, False):
        for record in eligible:
            passage = record["canonical_connection"]["passage_id"]
            family = record["source"]["exam_family"]
            if passage in used_passages or (prefer_new_family and family in used_families):
                continue
            selected.append(record)
            used_passages.add(passage)
            used_families.add(family)
            if len(selected) == limit:
                return selected
    return selected


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_by_name, canonical_names, aliases, search_urls = make_catalog_maps(catalog)
    indexes = build_indexes()
    results: list[dict[str, Any]] = []
    for site in read_jsonl(QUEUE):
        queried = site["queried_codes_matched"]
        missing_query_names = [name for name in queried if name not in catalog_by_name]
        query_ids = sorted({catalog_by_name[name]["number"] for name in queried if name in catalog_by_name})
        site_label_resolution = [resolve_display_label(label, canonical_names, aliases) for label in site["site_codes"]]
        connection = connect(site, indexes)
        site_answer = answer_symbol(site.get("site_marked_answer"))
        official = connection["official_answer"]
        results.append({
            "schema_version": "code_study_candidates_v2",
            "candidate_id": candidate_id(site),
            "source": {"exam_family": site["exam_family"], "year": site["year"], "exam_type": site["exam_type"], "question_number": site["question"], "site_title": site["title"], "domain": site.get("domain")},
            "site_candidate": {
                "source_role": "third_party_candidate_label", "site_marked_answer": site.get("site_marked_answer"), "site_marked_answer_symbol": site_answer,
                "estimated_correct_rate_percent": site.get("estimated_correct_rate_percent"), "option_selection_rates_percent": site.get("option_selection_rates_percent"),
                "site_original_codes": site["site_codes"], "site_queried_code_names": queried,
                "exam_search_url": site.get("exam_search_url"), "title_search_url": site.get("title_search_url"),
                "code_search_urls": {name: search_urls.get(name) for name in queried},
            },
            "code_normalization": {
                "catalog_status": catalog["status"],
                "query_catalog_code_ids": query_ids,
                "query_catalog_codes": [{"id": number, "name": catalog_by_name[name]["name"]} for name in queried if name in catalog_by_name for number in [catalog_by_name[name]["number"]]],
                "unresolved_query_code_names": missing_query_names,
                "site_label_resolution": site_label_resolution,
                "unresolved_or_ambiguous_site_labels": [x for x in site_label_resolution if not x["resolved_code_ids"]],
            },
            "canonical_connection": connection,
            "official_answer_comparison": {"official_answer": official, "site_answer_matches_official": official == site_answer if official and site_answer else None, "note": "Answer agreement verifies only answer-key alignment; it does not validate a candidate code."},
            "legacy_queue_reference": {"previous_local_match_status": site.get("local_match_status"), "previous_local_source": site.get("local_source"), "previous_local_question_id": site.get("local_question_id"), "previous_local_passage_id": site.get("local_passage_id"), "previous_text_status": site.get("text_status")},
            "semantic_review": "not_reviewed",
        })
    results.sort(key=lambda r: (r["source"]["exam_family"], r["source"]["year"], r["source"]["exam_type"], r["source"]["question_number"], r["candidate_id"]))

    source_keys = [
        (r["source"]["exam_family"], r["source"]["year"], r["source"]["exam_type"], r["source"]["question_number"], r["source"]["site_title"])
        for r in results
    ]
    if len(source_keys) != len(set(source_keys)) or len(results) != len({r["candidate_id"] for r in results}):
        raise ValueError("candidate source key or generated candidate_id is duplicated")
    meet_results = [r for r in results if r["source"]["exam_family"] == "MEET"]
    if any(r["canonical_connection"]["status"] != "exact_canonical_meet_jsonl" for r in meet_results):
        raise ValueError("a MEET candidate did not rejoin to the current canonical JSONL")

    coverage_codes = []
    recommendations: dict[str, list[str]] = {}
    for code in catalog["codes"]:
        code_id = code["number"]
        tagged = [r for r in results if code_id in r["code_normalization"]["query_catalog_code_ids"]]
        connected = [r for r in tagged if is_canonical(r["canonical_connection"])]
        passage_ids = {r["canonical_connection"]["passage_id"] for r in connected if r["canonical_connection"]["passage_id"]}
        samples = choose_diverse(results, code_id)
        recommendations[str(code_id)] = [r["candidate_id"] for r in samples]
        coverage_codes.append({
            "id": code_id, "name": code["name"], "category": code["category"], "aliases": code["aliases"],
            "candidate_count": len(tagged), "exam_families_with_candidates": sorted({r["source"]["exam_family"] for r in tagged}),
            "canonical_connection_count": len(connected), "distinct_canonical_passage_count": len(passage_ids),
            "sample_shortage": max(0, 5 - len(samples)), "recommended_comparison_candidate_ids": recommendations[str(code_id)],
        })
    recommendation_membership = defaultdict(list)
    for code_id, candidate_ids in recommendations.items():
        for item in candidate_ids:
            recommendation_membership[item].append(int(code_id))
    for record in results:
        record["recommended_for_code_ids"] = sorted(recommendation_membership[record["candidate_id"]])

    statuses = Counter(r["canonical_connection"]["status"] for r in results)
    comparisons = [r for r in results if r["official_answer_comparison"]["site_answer_matches_official"] is not None]
    mismatches = [r for r in comparisons if not r["official_answer_comparison"]["site_answer_matches_official"]]
    mismatch_keys = {(r["source"]["exam_family"], r["source"]["year"], r["source"]["exam_type"], r["source"]["question_number"]) for r in mismatches}
    expected_mismatches = {("MEET", 2012, "미트언어", 5), ("MEET", 2012, "미트언어", 7), ("MEET", 2012, "미트언어", 28)}
    if mismatch_keys != expected_mismatches:
        raise ValueError(f"unexpected answer-mismatch set: {sorted(mismatch_keys)}")
    coverage = {
        "schema_version": "code_study_coverage_v2", "purpose": "Review queue coverage only; no code-semantic determination is made.",
        "input_files": {str(path.relative_to(ROOT)): sha256(path) for path in (QUEUE, CATALOG, KICE_QUESTIONS, MEET_QUESTIONS, MEET_VISUALS, LEET_ANSWERS, LEET_VISUALS, LEET_VISUAL_MAPPING, LEET_VERIFIED)},
        "validation": {"unique_source_candidate_keys": len(set(source_keys)), "unique_candidate_ids": len({r["candidate_id"] for r in results}), "meet_candidates_all_rejoined_to_current_canonical_jsonl": len(meet_results), "official_answers_preserved_separately_from_site_answers": True, "preserved_site_answer_mismatch_keys": sorted([list(key) for key in mismatch_keys])},
        "summary": {"candidate_count": len(results), "candidate_exam_families": dict(sorted(Counter(r["source"]["exam_family"] for r in results).items())), "canonical_connection_statuses": dict(sorted(statuses.items())), "official_answer_comparisons": len(comparisons), "site_answer_mismatch_count": len(mismatches), "semantic_review_status": "not_reviewed_for_all_candidates"},
        "known_site_answer_mismatches": [{"candidate_id": r["candidate_id"], "source": r["source"], "site_answer": r["site_candidate"]["site_marked_answer_symbol"], "official_answer": r["canonical_connection"]["official_answer"]} for r in mismatches],
        "code_coverage": coverage_codes,
        "unresolved_catalog_query_names": sorted({name for r in results for name in r["code_normalization"]["unresolved_query_code_names"]}),
        "ambiguous_or_unresolved_site_labels": sorted({x["site_label"] for r in results for x in r["code_normalization"]["unresolved_or_ambiguous_site_labels"]}),
        "limitations": ["A code-site tag is a third-party candidate, not a semantic finding.", "Official-answer agreement is kept separate from code validation.", "Passage diversity is based on canonical passage/group IDs or printed LEET question ranges, never on matching titles.", "LEET reusable-visual catalog does not enumerate every structured <보기> box."],
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CANDIDATES.open("w", encoding="utf-8") as handle:
        for record in results:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    OUT_COVERAGE.write_text(json.dumps(coverage, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# 100코드 사례 연결 현황 v2", "",
        "> 이 문서는 사이트의 코드 태그를 확정하지 않는다. 정본 연결과 공식 정답 비교는 후속 사람이 원문·선지·시각 자료를 열어 코드의 성립 여부를 판독할 수 있게 하는 준비 단계이며, `semantic_review`는 전부 `not_reviewed`다.", "",
        "## 전체", "",
        f"- 제3자 후보 문항: {len(results):,}개", f"- 시험군: " + ", ".join(f"{family} {count:,}개" for family, count in sorted(Counter(r['source']['exam_family'] for r in results).items())),
        f"- 정본 연결 상태: " + ", ".join(f"`{status}` {count:,}개" for status, count in sorted(statuses.items())),
        f"- 공식 정답 비교 가능: {len(comparisons):,}개 / 사이트 표시 정답 불일치: {len(mismatches):,}개", "",
        "MEET의 기존 raw/OCR 대기 상태는 파생 인덱스에서 사용하지 않았다. 현재 `data/meet_questions.jsonl`의 380문항 정본으로 문항 ID·문항군·공식 답을 재연결했다. 원래 큐와 원본 데이터는 변경하지 않았다.", "",
        "## 코드별 연구 표본", "", "| 번호 | 정본명 | 후보 | 시험군 | 정본 연결 | 다른 지문 | 비교 표본 | 표본 부족 |", "| ---: | --- | ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for row in coverage_codes:
        lines.append(f"| #{row['id']} | {row['name']} | {row['candidate_count']} | {', '.join(row['exam_families_with_candidates']) or '-'} | {row['canonical_connection_count']} | {row['distinct_canonical_passage_count']} | {len(row['recommended_comparison_candidate_ids'])} | {row['sample_shortage']} |")
    lines.extend(["", "`다른 지문`은 KICE/MEET의 정본 passage/group ID와 LEET의 시험지 인쇄 문항 범위 ID로만 계산했으며, 사이트 제목은 판정에 사용하지 않았다.", "", "## 사이트 정답 불일치 (보존)", ""])
    if mismatches:
        for row in mismatches:
            source = row["source"]
            lines.append(f"- {source['exam_family']} {source['year']} {source['exam_type']} {source['question_number']}번 (`{row['candidate_id']}`): 사이트 {row['site_candidate']['site_marked_answer_symbol']}, 정본 {row['canonical_connection']['official_answer']}")
    else:
        lines.append("- 없음")
    lines.extend(["", "## 다음 수동 판독", "", "1. `code_study_candidates_v2.jsonl`에서 코드 번호의 추천 `candidate_id`를 열고 정본 원문·선지·필요 시 시각 자료를 대조한다.", "2. 사이트 원코드와 코드 검색 URL은 보존하되, 후보 태그와 코드 의미 판정은 분리해서 기록한다.", "3. 같은 제목이라는 이유로 동일 지문이라고 결론 내리지 않는다. `canonical_connection.passage_id`만 비교 단위로 쓴다.", "", "## 한계", "", "- 이 스크립트는 정답의 의미적 적합성, 코드의 성립 범위, 정답 유일성을 판정하거나 점수화하지 않는다.", "- 별칭은 정본명 우선·유일 별칭만 기계적으로 해석하고, 충돌한 별칭은 `ambiguous_catalog_name_or_alias`로 남긴다."])
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"candidates": len(results), "statuses": dict(statuses), "answer_mismatches": len(mismatches), "outputs": [str(OUT_CANDIDATES.relative_to(ROOT)), str(OUT_COVERAGE.relative_to(ROOT)), str(OUT_REPORT.relative_to(ROOT))]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
