#!/usr/bin/env python3
"""Build a provenance-preserving first-pass MEET language-reasoning corpus.

The source supplied by the user is a single 154-page PDF containing the 2005
preliminary test and the 2005–2012 tests.  Official answer files are kept
separately.  This script never promotes OCR or raw PDF extraction to canonical
text. It records extraction quality and, when present, reports the separately
managed official-page-verified transcript manifest.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

import fitz


ROOT = Path("자료/MEET_언어추론")
SOURCE_PDF = ROOT / "2005~2012_언어추론.pdf"
ANSWER_DIR = ROOT / "공식_정답표_원본"
TEXT_DIR = ROOT / "텍스트_추출본"
VISUAL_DIR = ROOT / "시각자료_원본"
VERIFY_DIR = ROOT / "검증"
TRANSCRIPT_MANIFEST = ROOT / "전사_검수완료" / "manifest.json"
DATA_DIR = Path("data")

YEAR_SPECS = {
    "2005예비": {"year": 2005, "exam_type": "미트예비", "pages": (1, 19), "questions": 50},
    "2005": {"year": 2005, "exam_type": "미트언어", "pages": (20, 38), "questions": 50},
    "2006": {"year": 2006, "exam_type": "미트언어", "pages": (39, 53), "questions": 40},
    "2007": {"year": 2007, "exam_type": "미트언어", "pages": (54, 69), "questions": 40},
    "2008": {"year": 2008, "exam_type": "미트언어", "pages": (70, 85), "questions": 40},
    "2009": {"year": 2009, "exam_type": "미트언어", "pages": (86, 101), "questions": 40},
    "2010": {"year": 2010, "exam_type": "미트언어", "pages": (102, 117), "questions": 40},
    "2011": {"year": 2011, "exam_type": "미트언어", "pages": (118, 135), "questions": 40},
    "2012": {"year": 2012, "exam_type": "미트언어", "pages": (136, 154), "questions": 40},
}

ANSWER_SOURCES = {
    "2005예비": {
        "file": "2005예비_언어추론_정답표.hwp",
        "verification_pdf": "2005예비_언어추론_정답표_검증용.pdf",
        "post_id": 10,
        "file_id": 44,
        "download_url": "https://www.mdeet.org/file/board_download.jsp?bbs_name=BANK&file_mng_num=44",
        "method": "official_hwp3_rendered_to_pdf_page_1",
    },
    "2005": {
        "file": "2005_언어추론_정답표.hwp",
        "post_id": 25,
        "file_id": 79,
        "download_url": "https://www.mdeet.org/file/board_download.jsp?bbs_name=BANK&file_mng_num=79",
        "method": "official_hwp5_table_1",
    },
    "2006": {
        "file": "2006_언어추론_정답표.hwp",
        "verification_pdf": "2006_언어추론_정답표_검증용.pdf",
        "post_id": 35,
        "file_id": 145,
        "download_url": "https://www.mdeet.org/file/board_download.jsp?bbs_name=BANK&file_mng_num=145",
        "method": "official_hwp3_rendered_to_pdf_page_1",
    },
    "2007": {
        "file": "2007_언어추론_정답표.hwp",
        "post_id": 46,
        "file_id": 177,
        "download_url": "https://www.mdeet.org/file/board_download.jsp?bbs_name=BANK&file_mng_num=177",
        "method": "official_hwp5_table_1",
    },
    "2008": {
        "file": "2008_언어추론_정답표.hwp",
        "post_id": 57,
        "file_id": 205,
        "download_url": "https://www.mdeet.org/file/board_download.jsp?bbs_name=BANK&file_mng_num=205",
        "method": "official_hwp5_table_1",
    },
    "2009": {
        "file": "2009_통합_정답표.pdf",
        "post_id": 74,
        "file_id": 230,
        "download_url": "https://www.mdeet.org/file/board_download.jsp?bbs_name=BANK&file_mng_num=230",
        "method": "official_pdf_page_1",
    },
    "2010": {
        "file": "2010_통합_정답표.pdf",
        "post_id": 83,
        "file_id": 254,
        "download_url": "https://www.mdeet.org/file/board_download.jsp?bbs_name=BANK&file_mng_num=254",
        "method": "official_pdf_page_1",
    },
    "2011": {
        "file": "2011_통합_정답표.pdf",
        "post_id": 88,
        "file_id": 276,
        "download_url": "https://www.mdeet.org/file/board_download.jsp?bbs_name=BANK&file_mng_num=276",
        "method": "official_pdf_page_1",
    },
    "2012": {
        "file": "2012_통합_정답표.pdf",
        "post_id": 95,
        "file_id": 328,
        "download_url": "https://www.mdeet.org/file/board_download.jsp?bbs_name=BANK&file_mng_num=328",
        "method": "official_pdf_page_1",
    },
}

CIRCLED_TO_INT = {"①": 1, "②": 2, "③": 3, "④": 4, "⑤": 5}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_answer_pairs(text: str, expected: int) -> dict[int, int]:
    pairs = [(int(q), CIRCLED_TO_INT[a]) for q, a in re.findall(r"(?<!\d)(\d{1,2})\s*([①②③④⑤])", text)]
    answers: dict[int, int] = {}
    for question, answer in pairs:
        if 1 <= question <= expected and question not in answers:
            answers[question] = answer
    if sorted(answers) != list(range(1, expected + 1)):
        missing = sorted(set(range(1, expected + 1)) - set(answers))
        raise ValueError(f"answer parsing failed: expected={expected}, missing={missing}, pairs={len(pairs)}")
    return answers


def parse_hwp5_table(path: Path, expected: int) -> dict[int, int]:
    raw = subprocess.run(["hwp5proc", "xml", str(path)], check=True, capture_output=True).stdout
    root = ET.fromstring(raw)
    tables = list(root.iter("TableControl"))
    if len(tables) < 2:
        raise ValueError(f"no answer table in {path}")
    cells: list[str] = []
    for row in tables[1].iter("TableRow"):
        for cell in row.findall("TableCell"):
            cells.append("".join(node.text or "" for node in cell.iter("Text")).strip())
    return parse_answer_pairs(" ".join(cells), expected)


def parse_pdf_first_page(path: Path, expected: int) -> dict[int, int]:
    with fitz.open(path) as document:
        text = document[0].get_text("text")
    return parse_answer_pairs(text, expected)


def build_answers() -> tuple[dict[str, dict[str, int]], list[dict]]:
    keys: dict[str, dict[str, int]] = {}
    source_records: list[dict] = []
    for label, spec in YEAR_SPECS.items():
        source = ANSWER_SOURCES[label]
        answer_path = ANSWER_DIR / source["file"]
        if source["method"] == "official_hwp5_table_1":
            parsed = parse_hwp5_table(answer_path, spec["questions"])
        else:
            pdf_name = source.get("verification_pdf", source["file"])
            parsed = parse_pdf_first_page(ANSWER_DIR / pdf_name, spec["questions"])
        keys[label] = {str(q): parsed[q] for q in sorted(parsed)}
        record = {
            "label": label,
            "official_file": str(answer_path),
            "official_file_sha256": sha256(answer_path),
            "official_post_id": source["post_id"],
            "official_file_id": source["file_id"],
            "official_download_url": source["download_url"],
            "extraction_method": source["method"],
            "answer_count": len(parsed),
            "form": "odd_or_single",
        }
        if source.get("verification_pdf"):
            rendered = ANSWER_DIR / source["verification_pdf"]
            record.update({
                "verification_pdf": str(rendered),
                "verification_pdf_sha256": sha256(rendered),
                "verification_pdf_role": "rendered_from_official_hwp_for_visual_verification",
            })
        source_records.append(record)
    return keys, source_records


def page_markdown(label: str, page_no: int, text: str, source_hash: str) -> str:
    warning = (
        "> **비정본 자동 추출본.** 공식 PDF 페이지와 직접 대조하기 전에는 인용·문항 분석의 확정 원문으로 사용하지 않는다.\n\n"
    )
    return (
        f"# {label} MEET 언어추론 자동 추출본\n\n"
        f"- 원본: `{SOURCE_PDF}`\n"
        f"- 원본 SHA-256: `{source_hash}`\n"
        f"- 시작 공식 PDF 페이지: {page_no}\n\n"
        f"{warning}"
        f"## 공식 PDF {page_no}쪽부터\n\n{text}"
    )


def extract_questions(raw_text: str, label: str, spec: dict, answers: dict[str, int], page_offsets: list[tuple[int, int, int]]) -> list[dict]:
    starts = list(re.finditer(r"(?m)^\s*(\d{1,2})\.\s", raw_text))
    question_numbers = [int(match.group(1)) for match in starts]
    expected_numbers = list(range(1, spec["questions"] + 1))
    if question_numbers != expected_numbers:
        raise ValueError(f"{label}: question sequence mismatch: {question_numbers}")

    def source_page(position: int) -> int:
        for start, end, page_no in page_offsets:
            if start <= position < end:
                return page_no
        return page_offsets[-1][2]

    records = []
    for index, match in enumerate(starts):
        question = int(match.group(1))
        end = starts[index + 1].start() if index + 1 < len(starts) else len(raw_text)
        block = raw_text[match.start():end].strip()
        next_group = re.search(r"(?m)^\s*\[\s*\d{1,2}\s*[～~\-]\s*\d{1,2}\s*\]\s*다음", block)
        if next_group:
            block = block[:next_group.start()].rstrip()
        choice_markers = re.findall(r"[①②③④⑤]", block)
        records.append({
            "exam_family": "MEET",
            "label": label,
            "year": spec["year"],
            "exam_type": spec["exam_type"],
            "question": question,
            "answer": answers[str(question)],
            "official_answer_verified": True,
            "source_pdf": str(SOURCE_PDF),
            "source_pdf_page": source_page(match.start()),
            "raw_question_text": block,
            "choice_marker_count": len(choice_markers),
            "text_status": "raw_pdf_extraction_unverified",
        })
    return records


def extract_passages(raw_text: str, label: str, spec: dict, page_offsets: list[tuple[int, int, int]]) -> list[dict]:
    group_pattern = re.compile(
        r"(?m)^\s*\[\s*(\d{1,2})\s*[～~\-]\s*(\d{1,2})\s*\]\s*다음[^\n]*\n"
    )
    question_starts = {
        int(match.group(1)): match.start()
        for match in re.finditer(r"(?m)^\s*(\d{1,2})\.\s", raw_text)
    }

    def source_page(position: int) -> int:
        for start, end, page_no in page_offsets:
            if start <= position < end:
                return page_no
        return page_offsets[-1][2]

    records = []
    for match in group_pattern.finditer(raw_text):
        start_question, end_question = int(match.group(1)), int(match.group(2))
        first_question_position = question_starts.get(start_question)
        if first_question_position is None or first_question_position <= match.end():
            continue
        passage_text = raw_text[match.end():first_question_position].strip()
        records.append({
            "exam_family": "MEET",
            "passage_id": f"MEET-{label}-Q{start_question:02d}-{end_question:02d}",
            "label": label,
            "year": spec["year"],
            "exam_type": spec["exam_type"],
            "question_range": [start_question, end_question],
            "source_pdf": str(SOURCE_PDF),
            "source_pdf_start_page": source_page(match.start()),
            "raw_passage_text": passage_text,
            "text_status": "raw_pdf_extraction_unverified",
        })
    return records


def build_text_and_raw_questions(document: fitz.Document, answer_keys: dict[str, dict[str, int]]) -> tuple[list[dict], list[dict], list[dict]]:
    source_hash = sha256(SOURCE_PDF)
    year_records: list[dict] = []
    question_records: list[dict] = []
    passage_records: list[dict] = []
    TEXT_DIR.mkdir(parents=True, exist_ok=True)

    for label, spec in YEAR_SPECS.items():
        first, last = spec["pages"]
        chunks: list[str] = []
        offsets: list[tuple[int, int, int]] = []
        cursor = 0
        per_page_chars = []
        for page_no in range(first, last + 1):
            text = document[page_no - 1].get_text("text")
            sentinel = f"\n\n<!-- OFFICIAL_PDF_PAGE_{page_no} -->\n\n"
            chunk = sentinel + text
            start, end = cursor, cursor + len(chunk)
            chunks.append(chunk)
            offsets.append((start, end, page_no))
            per_page_chars.append(len(text.strip()))
            cursor = end
        raw_text = "".join(chunks)
        markdown = page_markdown(label, first, raw_text, source_hash)
        text_path = TEXT_DIR / f"{label}_언어추론_자동추출.md"
        text_path.write_text(markdown, encoding="utf-8")

        low_text_pages = [first + i for i, count in enumerate(per_page_chars) if count < 100]
        sequence = [int(value) for value in re.findall(r"(?m)^\s*(\d{1,2})\.\s", raw_text)]
        extraction_ok = sequence == list(range(1, spec["questions"] + 1))
        status = "raw_extraction_complete_unverified" if extraction_ok and not low_text_pages else "ocr_and_direct_verification_required"
        if extraction_ok:
            year_questions = extract_questions(raw_text, label, spec, answer_keys[label], offsets)
            year_passages = extract_passages(raw_text, label, spec, offsets)
            passage_by_question = {
                question: passage["passage_id"]
                for passage in year_passages
                for question in range(passage["question_range"][0], passage["question_range"][1] + 1)
            }
            for question in year_questions:
                question["passage_id"] = passage_by_question.get(question["question"])
            question_records.extend(year_questions)
            passage_records.extend(year_passages)

        year_records.append({
            "label": label,
            "year": spec["year"],
            "exam_type": spec["exam_type"],
            "official_pdf_pages": [first, last],
            "page_count": last - first + 1,
            "expected_questions": spec["questions"],
            "detected_question_sequence": sequence,
            "detected_question_count": len(sequence),
            "low_text_pages": low_text_pages,
            "text_file": str(text_path),
            "text_status": status,
            "detected_passage_groups": len(year_passages) if extraction_ok else 0,
        })
    return year_records, passage_records, question_records


def extract_embedded_visuals(document: fitz.Document) -> list[dict]:
    VISUAL_DIR.mkdir(parents=True, exist_ok=True)
    records: list[dict] = []
    seen: set[int] = set()
    for page_no, page in enumerate(document, start=1):
        label = next(label for label, spec in YEAR_SPECS.items() if spec["pages"][0] <= page_no <= spec["pages"][1])
        for image_index, image in enumerate(page.get_images(full=True), start=1):
            xref = image[0]
            if xref in seen:
                continue
            seen.add(xref)
            extracted = document.extract_image(xref)
            target_dir = VISUAL_DIR / label
            target_dir.mkdir(parents=True, exist_ok=True)
            path = target_dir / f"page_{page_no:03d}_image_{image_index:02d}_xref_{xref}.{extracted['ext']}"
            path.write_bytes(extracted["image"])
            records.append({
                "label": label,
                "official_pdf_page": page_no,
                "xref": xref,
                "width": extracted["width"],
                "height": extracted["height"],
                "extension": extracted["ext"],
                "file": str(path),
                "sha256": sha256(path),
                "status": "extracted_from_supplied_pdf_not_yet_semantically_classified",
            })
    return records


def validate_site_answers(answer_keys: dict[str, dict[str, int]]) -> dict:
    source = DATA_DIR / "sdss_indexed_questions.jsonl"
    if not source.is_file():
        return {"source": str(source), "status": "source_missing", "rows": 0}
    rows = [json.loads(line) for line in source.read_text(encoding="utf-8").splitlines() if line.strip()]
    meet_rows = [row for row in rows if row.get("exam_family") == "MEET"]
    comparisons = []
    for row in meet_rows:
        label = "2005예비" if row.get("exam_type") == "미트예비" else str(row["year"])
        official = answer_keys[label][str(row["question"])]
        comparisons.append({
            "label": label,
            "question": row["question"],
            "site_marked_answer": row["site_marked_answer"],
            "official_answer": official,
            "matches": row["site_marked_answer"] == official,
        })
    mismatches = [record for record in comparisons if not record["matches"]]
    return {
        "source": str(source),
        "status": "ALL_MATCH" if not mismatches else "OFFICIAL_SITE_MISMATCH_FOUND",
        "rows": len(comparisons),
        "matched": len(comparisons) - len(mismatches),
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "note": "Agreement validates answer-number linkage only; it does not validate third-party code labels.",
    }


def write_report(year_records: list[dict], answer_sources: list[dict], passage_records: list[dict], question_records: list[dict], visuals: list[dict], site_check: dict) -> None:
    VERIFY_DIR.mkdir(parents=True, exist_ok=True)
    canonical = (
        json.loads(TRANSCRIPT_MANIFEST.read_text(encoding="utf-8"))
        if TRANSCRIPT_MANIFEST.is_file()
        else {"records": [], "verified_question_count": 0, "expected_question_count": 380}
    )
    canonical_by_label: dict[str, int] = {}
    for record in canonical.get("records", []):
        canonical_by_label[record["label"]] = canonical_by_label.get(record["label"], 0) + len(record["questions"])
    canonical_count = canonical.get("verified_question_count", 0)
    canonical_expected = canonical.get("expected_question_count", 380)
    report_years = []
    for record in year_records:
        verified = canonical_by_label.get(record["label"], 0)
        expected = record["expected_questions"]
        if verified == expected:
            canonical_status = "official_page_verified_canonical_complete"
        elif verified:
            canonical_status = "official_page_verified_partial"
        else:
            canonical_status = record["text_status"]
        report_record = dict(record)
        report_record["raw_text_status"] = record["text_status"]
        report_record["canonical_status"] = canonical_status
        report_record["canonical_question_count"] = verified
        report_years.append(report_record)

    blocking_items = []
    if canonical_by_label.get("2009", 0) < YEAR_SPECS["2009"]["questions"]:
        blocking_items.append(
            "2009학년도는 이중 OCR과 문항 경계 검증을 마쳤으나 공식 지면 직접 대조 정본은 "
            f"{canonical_by_label.get('2009', 0)}/40문항임."
        )
    blocking_items.extend([
        "2005예비·2006 HWP3 답안의 검증용 PDF는 공식 HWP를 변환한 파생물이며 공식 원본 HWP 해시를 함께 보존함.",
        "2009 외 연도 텍스트도 아직 페이지 직접 대조 전인 자동 추출본이므로 정본으로 승격하지 않음.",
        "임베디드 이미지 외 벡터 도형·표는 전 페이지 접촉판 판독으로 추가 식별해야 함.",
    ])
    payload = {
        "status": "PARTIAL_PASS_DIRECT_TRANSCRIPTION_IN_PROGRESS",
        "source_pdf": str(SOURCE_PDF),
        "source_pdf_sha256": sha256(SOURCE_PDF),
        "source_pdf_pages": 154,
        "answer_sources": answer_sources,
        "years": report_years,
        "raw_question_records": len(question_records),
        "raw_passage_records": len(passage_records),
        "embedded_visual_records": len(visuals),
        "official_page_verified_transcript_manifest": str(TRANSCRIPT_MANIFEST),
        "official_page_verified_questions": canonical_count,
        "official_page_verified_expected_questions": canonical_expected,
        "site_answer_crosscheck": site_check,
        "blocking_items": blocking_items,
    }
    json_path = VERIFY_DIR / "MEET_코퍼스_1차구축_v1.json"
    md_path = VERIFY_DIR / "MEET_코퍼스_1차구축_v1.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# MEET 언어추론 코퍼스 1차 구축 검증 v1\n\n",
        "- 판정: **PARTIAL PASS — 공식 지면 직접 대조 정본화 진행 중**\n",
        f"- 합본 원본: `{SOURCE_PDF}` (154쪽)\n",
        f"- 공식 홀수형·단일형 답: {sum(r['answer_count'] for r in answer_sources)}개 확보\n",
        f"- 자동 분리된 문항: {len(question_records)}개\n",
        f"- 자동 분리된 지문군: {len(passage_records)}개\n",
        f"- 추출된 임베디드 시각 자료: {len(visuals)}개\n",
        f"- 공식 지면 직접 대조 정본: {canonical_count}/{canonical_expected}문항\n",
        f"- sdss MEET 후보 답 번호 대조: {site_check.get('matched', 0)}/{site_check.get('rows', 0)} 일치, "
        f"공식 답과 다른 사이트 기재 {site_check.get('mismatch_count', 0)}건\n\n",
        "> 자동 추출 성공은 정본 인증이 아니다. 원문·선지의 확정 인용은 공식 PDF 페이지와 직접 대조한 뒤에만 한다.\n\n",
        "## 연도별 상태\n\n",
        "| 구분 | 공식 PDF 쪽 | 문항 | 자동 감지 | 직접 대조 정본 | 상태 |\n",
        "| --- | ---: | ---: | ---: | ---: | --- |\n",
    ]
    for record in report_years:
        first, last = record["official_pdf_pages"]
        lines.append(
            f"| {record['label']} | {first}–{last} | {record['expected_questions']} | "
            f"{record['detected_question_count']} | {canonical_by_label.get(record['label'], 0)} | "
            f"`{record['canonical_status']}` |\n"
        )
    lines.extend([
        "\n## 남은 검증\n\n",
        "1. 나머지 8개 시험의 자동 추출본을 문항군 단위로 공식 페이지와 대조하고 정본 Markdown으로 승격한다.\n",
        "2. 전 페이지 접촉판에서 표·그래프·그림·수식 배치를 판독하고 재사용 가능 원본을 문항에 연결한다.\n",
        "3. 337개 sdss MEET 코드 후보를 정본 지문·문항에 조인한 뒤 코드별 타당성을 판독한다.\n",
        "\n## 답안 검증 원칙\n\n",
        "- 2005예비·2006: 공식 HWP3 원본을 한컴으로 PDF화한 첫 쪽 홀수형 표를 판독했다.\n",
        "- 2005·2007·2008: 공식 HWP5의 홀수형 표 셀을 직접 추출했다.\n",
        "- 2009·2010: 공식 통합 답안 PDF 첫 쪽의 언어추론 홀수형 표를 사용했다.\n",
        "- 2011·2012: 단일형 공식 통합 답안 PDF 첫 쪽을 사용했다.\n",
        "- sdss 답 번호와의 일치는 문항 번호 연결을 검증할 뿐, 사이트 코드 라벨의 타당성을 검증하지 않는다.\n",
    ])
    if site_check.get("mismatches"):
        lines.extend(["\n## 공식 답과 다른 사이트 기재\n\n"])
        for mismatch in site_check["mismatches"]:
            lines.append(
                f"- {mismatch['label']}학년도 {mismatch['question']}번: 사이트 {mismatch['site_marked_answer']}, "
                f"공식 {mismatch['official_answer']} — 공식 답을 사용한다.\n"
            )
    md_path.write_text("".join(lines), encoding="utf-8")


def write_answer_markdown(answer_keys: dict[str, dict[str, int]], answer_sources: list[dict]) -> None:
    source_by_label = {record["label"]: record for record in answer_sources}
    lines = [
        "# MEET 언어추론 공식 답 정규화\n\n",
        "> 홀수형이 있는 연도는 홀수형, 단일형 연도는 단일형 답이다. 각 표의 근거 원본과 해시는 `source_manifest.json`에 보존했다.\n\n",
    ]
    for label in YEAR_SPECS:
        source = source_by_label[label]
        values = answer_keys[label]
        lines.extend([
            f"## {label}\n\n",
            f"- 추출 방식: `{source['extraction_method']}`\n",
            f"- 공식 원본: `{source['official_file']}`\n\n",
        ])
        items = [f"{number}번 {values[str(number)]}" for number in range(1, YEAR_SPECS[label]["questions"] + 1)]
        for start in range(0, len(items), 10):
            lines.append(" · ".join(items[start:start + 10]) + "\n\n")
    (ANSWER_DIR / "MEET_언어추론_공식답_정규화.md").write_text("".join(lines), encoding="utf-8")


def main() -> None:
    for directory in (ANSWER_DIR, TEXT_DIR, VISUAL_DIR, VERIFY_DIR, DATA_DIR):
        directory.mkdir(parents=True, exist_ok=True)
    answer_keys, answer_sources = build_answers()
    (DATA_DIR / "meet_answer_keys.json").write_text(
        json.dumps({"status": "official_verified", "keys": answer_keys, "sources": answer_sources}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (ANSWER_DIR / "source_manifest.json").write_text(json.dumps(answer_sources, ensure_ascii=False, indent=2), encoding="utf-8")
    write_answer_markdown(answer_keys, answer_sources)

    with fitz.open(SOURCE_PDF) as document:
        if len(document) != 154:
            raise ValueError(f"unexpected source page count: {len(document)}")
        year_records, passage_records, question_records = build_text_and_raw_questions(document, answer_keys)
        visuals = extract_embedded_visuals(document)

    with (DATA_DIR / "meet_passages_raw.jsonl").open("w", encoding="utf-8") as handle:
        for record in passage_records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    with (DATA_DIR / "meet_questions_raw.jsonl").open("w", encoding="utf-8") as handle:
        for record in question_records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    (VISUAL_DIR / "manifest.json").write_text(json.dumps(visuals, ensure_ascii=False, indent=2), encoding="utf-8")
    site_check = validate_site_answers(answer_keys)
    write_report(year_records, answer_sources, passage_records, question_records, visuals, site_check)
    print("official answers", sum(len(values) for values in answer_keys.values()))
    print("raw passages", len(passage_records))
    print("raw questions", len(question_records))
    print("visuals", len(visuals))
    print("site", site_check["status"], site_check.get("matched"), "/", site_check.get("rows"))


if __name__ == "__main__":
    main()
