#!/usr/bin/env python3
"""Join third-party 100-code candidates to verified local KICE/LEET sources.

The code-site label is never promoted to a ground-truth annotation here.  This
script only builds a review queue whose local source and official answer can be
opened before a human/model accepts, rejects, or refines the proposed code.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path


SITE = Path("data/sdss_indexed_questions.jsonl")
SITE_EXPANDED = Path("data/code_site_labels.jsonl")
KICE = Path("data/kice_questions.jsonl")
LEET_ANSWERS = Path("자료/LEET_언어이해/normalized_answers.json")
LEET_VERIFIED = Path("자료/LEET_언어이해/전사_검수완료/manifest.json")
MEET_ANSWERS = Path("data/meet_answer_keys.json")
MEET_QUESTIONS = Path("data/meet_questions_raw.jsonl")
OUT = Path("data/code_candidate_review_queue.jsonl")
OUT_EXPANDED = Path("data/code_candidate_review_queue_by_code.jsonl")
REPORT = Path("분석/100코드_로컬원문_연결현황_v1.md")
CIRCLED = "①②③④⑤"


def rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def site_answer_symbol(value: int | None) -> str | None:
    if value is None or not 1 <= value <= 5:
        return None
    return CIRCLED[value - 1]


def kice_target(site: dict) -> tuple[str, str | None, str | None] | None:
    return {
        "수능국어": ("수능", None, None),
        "수능국어B형": ("수능", None, "B"),
        "6평국어": ("수능 모의평가", "6월", None),
        "6평국어A형": ("수능 모의평가", "6월", "A"),
        "9평국어": ("수능 모의평가", "9월", None),
    }.get(site["exam_type"])


def leet_source(year: int, exam_type: str) -> Path | None:
    if exam_type == "리트예비":
        # The code site calls the 2009학년도 preliminary test "2009 리트예비".
        # Its five separately indexed 2008 rows do not belong to our local
        # official corpus and remain deliberately unresolved.
        if year == 2009:
            return Path("자료/LEET_언어이해/텍스트/2009예비/2009예비_question_odd.md")
        return None
    path = Path(f"자료/LEET_언어이해/텍스트/{year}/{year}_question_odd.md")
    return path if path.exists() else None


def main() -> None:
    site_rows = rows(SITE)
    kice_rows = rows(KICE)
    kice_index: dict[tuple, list[dict]] = defaultdict(list)
    for item in kice_rows:
        key = (
            item["academic_year"], item["exam_type"], item.get("month"),
            item.get("variant"), item["question_number"],
        )
        kice_index[key].append(item)

    leet_answer_records = json.loads(LEET_ANSWERS.read_text(encoding="utf-8"))["records"]
    leet_answer_index = {
        (item["label"], item["variant"]): item
        for item in leet_answer_records
        if item.get("status") in {"parsed", "verified_visual"}
    }
    verified_manifest = json.loads(LEET_VERIFIED.read_text(encoding="utf-8"))
    verified_by_question: dict[tuple[int, int], dict] = {}
    for item in verified_manifest["records"]:
        for q in item["questions"]:
            verified_by_question[(item["year"], q)] = item

    meet_answer_data = json.loads(MEET_ANSWERS.read_text(encoding="utf-8"))
    meet_answer_index = meet_answer_data["keys"]
    meet_answer_sources = {
        item["label"]: item for item in meet_answer_data["sources"]
    }
    meet_question_index = {
        (item["label"], item["question"]): item
        for item in rows(MEET_QUESTIONS)
    }

    output = []
    for site in site_rows:
        item = dict(site)
        item["candidate_label_status"] = "unreviewed_third_party_candidate"
        item["local_match_status"] = "unsupported_exam_family"
        item["local_source"] = None
        item["local_question_id"] = None
        item["official_answer"] = None
        item["site_answer_matches_official"] = None

        if site["exam_family"] == "KICE":
            target = kice_target(site)
            if target is None:
                item["local_match_status"] = "unsupported_kice_exam_label"
            else:
                exam, month, variant = target
                key = (site["year"], exam, month, variant, site["question"])
                candidates = kice_index.get(key, [])
                if len(candidates) == 1:
                    local = candidates[0]
                    item["local_question_id"] = local["question_id"]
                    item["local_passage_id"] = local["passage_id"]
                    item["local_source"] = "data/kice_questions.jsonl"
                    item["official_answer"] = local["answer"]
                    item["choice_parse_status"] = local["choice_parse_status"]
                    item["local_match_status"] = (
                        "exact_ready" if local["choice_parse_status"] == "complete"
                        else "exact_visual_choice_review_needed"
                    )
                elif len(candidates) > 1:
                    item["local_match_status"] = "ambiguous_kice_match"
                    item["local_candidate_ids"] = [x["question_id"] for x in candidates]
                else:
                    item["local_match_status"] = "kice_question_not_in_local_reading_scope"

        elif site["exam_family"] == "LEET":
            source = leet_source(site["year"], site["exam_type"])
            if source is None:
                item["local_match_status"] = "leet_source_not_in_local_corpus"
            else:
                label = "2009예비" if site["exam_type"] == "리트예비" else str(site["year"])
                answer_record = leet_answer_index.get((label, "odd"))
                official = (
                    answer_record.get("answers", {}).get(str(site["question"]))
                    if answer_record else None
                )
                item["local_source"] = str(source)
                item["official_answer_source"] = answer_record.get("source_file") if answer_record else None
                item["official_answer"] = official
                item["local_question_id"] = (
                    f"LEET-{label}-odd-Q{site['question']:02d}"
                )
                verified = verified_by_question.get((site["year"], site["question"]))
                if verified:
                    item["verified_transcript"] = verified["file"]
                    item["verified_transcript_sha256"] = verified["file_sha256"]
                    item["local_source"] = verified["file"]
                    item["local_match_status"] = "exact_verified_transcript"
                else:
                    item["local_match_status"] = (
                        "exact_canonical_odd_markdown" if official
                        else "leet_answer_unresolved"
                    )

        elif site["exam_family"] == "MEET":
            label = "2005예비" if site["exam_type"] == "미트예비" else str(site["year"])
            official_int = meet_answer_index.get(label, {}).get(str(site["question"]))
            item["official_answer"] = site_answer_symbol(official_int)
            answer_source = meet_answer_sources.get(label)
            item["official_answer_source"] = answer_source.get("official_file") if answer_source else None
            item["local_question_id"] = f"MEET-{label}-Q{site['question']:02d}"
            local = meet_question_index.get((label, site["question"]))
            if local:
                item["local_source"] = str(MEET_QUESTIONS)
                item["local_passage_id"] = local.get("passage_id")
                item["source_pdf_page"] = local.get("source_pdf_page")
                item["text_status"] = local.get("text_status")
                item["local_match_status"] = "meet_raw_pdf_extraction_verification_pending"
            elif label == "2009":
                item["local_source"] = "자료/MEET_언어추론/OCR_초안_Paddle/2009/manifest.json"
                item["text_status"] = "dual_ocr_official_page_review_pending"
                item["local_match_status"] = "meet_2009_dual_ocr_review_pending"
            else:
                item["local_match_status"] = "meet_question_not_extracted"

        site_symbol = site_answer_symbol(site.get("site_marked_answer"))
        if item["official_answer"] and site_symbol:
            item["site_answer_matches_official"] = item["official_answer"] == site_symbol
        output.append(item)

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", encoding="utf-8") as handle:
        for item in output:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")

    # Preserve one row per canonical queried code as well.  The aggregated
    # queue is convenient per question; this expanded queue is convenient for
    # writing the 100 individual code cards without guessing aliases such as
    # catalog `양질` versus result-page `양/질`.
    joined_index = {
        (x["exam_family"], x["year"], x["exam_type"], x["question"]): x
        for x in output
    }
    expanded_output = []
    for label in rows(SITE_EXPANDED):
        key = (label["exam_family"], label["year"], label["exam_type"], label["question"])
        joined = joined_index[key]
        expanded_output.append({
            **label,
            "candidate_label_status": joined["candidate_label_status"],
            "local_match_status": joined["local_match_status"],
            "local_source": joined.get("local_source"),
            "local_question_id": joined.get("local_question_id"),
            "local_passage_id": joined.get("local_passage_id"),
            "official_answer": joined.get("official_answer"),
            "official_answer_source": joined.get("official_answer_source"),
            "site_answer_matches_official": joined.get("site_answer_matches_official"),
            "choice_parse_status": joined.get("choice_parse_status"),
            "verified_transcript": joined.get("verified_transcript"),
            "source_pdf_page": joined.get("source_pdf_page"),
            "text_status": joined.get("text_status"),
        })
    with OUT_EXPANDED.open("w", encoding="utf-8") as handle:
        for item in expanded_output:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")

    status = Counter(x["local_match_status"] for x in output)
    answer_compared = [x for x in output if x["site_answer_matches_official"] is not None]
    answer_mismatch = [x for x in answer_compared if not x["site_answer_matches_official"]]
    by_family = Counter(x["exam_family"] for x in output)
    code_ready = defaultdict(int)
    for item in output:
        if item["local_match_status"] in {
            "exact_ready", "exact_verified_transcript", "exact_canonical_odd_markdown"
        }:
            for code in item["site_codes"]:
                code_ready[code] += 1

    lines = [
        "# 100코드 후보 색인–로컬 원문 연결 현황 v1",
        "",
        "> 이 문서는 제3자 코드 표지를 정답으로 확정한 결과가 아니다. 사이트 표지를 후보로만 수집하고, 공식 원문·공식 정답을 다시 읽어 코드의 성립 범위와 문항 내 기능을 판독하기 위한 작업 큐의 검증 보고서이다.",
        "",
        "## 전체 결과",
        "",
        f"- 후보 문항: {len(output):,}개",
        f"- 시험군: " + ", ".join(f"{k} {v:,}개" for k, v in sorted(by_family.items())),
        f"- 공식 정답 비교 가능: {len(answer_compared):,}개",
        f"- 사이트 표시 정답과 공식 정답 일치: {len(answer_compared) - len(answer_mismatch):,}개",
        f"- 불일치: {len(answer_mismatch):,}개",
        "",
        "## 로컬 연결 상태",
        "",
    ]
    lines.extend(f"- `{key}`: {value:,}개" for key, value in sorted(status.items()))
    lines.extend([
        "",
        "## 해석 원칙",
        "",
        "1. `site_codes`는 제3자 후보 태그이며 확정 주석이 아니다.",
        "2. 공식 정답과 다른 사이트 레코드는 코드 판독 전에 원문 번호·형식부터 재확인한다.",
        "3. 평가원 문항은 선지 5개가 완전히 정규화된 `exact_ready`만 자동 본판독 대상으로 삼는다.",
        "4. LEET의 `exact_canonical_odd_markdown`은 공식 홀수형 정답이 연결된 정본이나, 개별 코드 확정 시 해당 문항과 시각 자료를 다시 대조한다.",
        "5. MEET는 공식 합본 PDF와 공식 답을 연결했다. 2009 이외 연도는 PDF 문자층 자동 추출본, 2009는 이중 OCR 초안이므로 공식 페이지 직접 대조 전에는 확정 코드 근거로 인용하지 않는다.",
        "",
        "## 코드별 즉시 판독 가능한 후보 수",
        "",
    ])
    lines.extend(f"- {code}: {count:,}개" for code, count in sorted(code_ready.items(), key=lambda x: (-x[1], x[0])))
    lines.extend([
        "",
        "## 정답 불일치 목록",
        "",
    ])
    if answer_mismatch:
        lines.extend(
            f"- {x['exam_family']} {x['year']} {x['exam_type']} {x['question']}번 "
            f"({x['title']}): 사이트 {site_answer_symbol(x.get('site_marked_answer'))}, 공식 {x['official_answer']}"
            for x in answer_mismatch
        )
    else:
        lines.append("- 없음")
    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT}: {len(output)} rows")
    print(f"wrote {OUT_EXPANDED}: {len(expanded_output)} rows")
    print(f"official answer comparisons={len(answer_compared)}, mismatches={len(answer_mismatch)}")
    print(dict(status))
    print(REPORT)


if __name__ == "__main__":
    main()
