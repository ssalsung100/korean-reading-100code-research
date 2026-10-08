#!/usr/bin/env python3
"""Collect the public sdss.kr 100-code search index with provenance.

The site's tags are stored as third-party candidate labels.  This script does
not promote them to project-verified passage/question codes.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup


BASE = "https://sdss.kr/code/"
CATALOG_URL = urljoin(BASE, "100.html")
SEARCH_URL = urljoin(BASE, "search.asp")
ROOT = Path("data")
RAW = ROOT / "sdss_code_search_raw"
CATALOG_OUT = ROOT / "sdss_100codes_catalog.json"
LABELS_OUT = ROOT / "code_site_labels.jsonl"
QUESTIONS_OUT = ROOT / "sdss_indexed_questions.jsonl"
REPORT = Path("분석/100코드_사이트색인_수집현황_v1.md")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def percent(text: str) -> int | None:
    match = re.fullmatch(r"\s*(\d+)\s*%\s*", text)
    return int(match.group(1)) if match else None


def exam_family(exam_type: str) -> str:
    if "리트" in exam_type:
        return "LEET"
    if any(token in exam_type for token in ("수능", "평국어", "평가원")):
        return "KICE"
    if "미트" in exam_type:
        return "MEET"
    return "OTHER"


def parse_catalog(html: str) -> tuple[list[dict], dict]:
    match = re.search(r"const\s+codeCategories\s*=\s*(\{.*?\})\s*;", html, re.S)
    if not match:
        raise ValueError("100.html에서 codeCategories를 찾지 못함")
    categories = json.loads(match.group(1))
    codes = []
    number = 0
    for category, items in categories.items():
        for name, aliases in items.items():
            number += 1
            codes.append({
                "number": number,
                "name": name,
                "category": category,
                "aliases": aliases,
            })
    if len(codes) != 100:
        raise ValueError(f"코드 수가 100이 아님: {len(codes)}")
    return codes, categories


def parse_search(html: str, query_code: dict, fetched_at: str, url: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for tr in soup.select("table tbody tr"):
        cells = tr.find_all("td", recursive=False)
        if len(cells) < 12:
            continue
        cell_text = [cell.get_text(" ", strip=True) for cell in cells]
        try:
            year = int(cell_text[0])
            question = int(cell_text[2])
        except ValueError as exc:
            raise ValueError(f"행의 연도/문항 번호 해석 실패: {cell_text[:4]}") from exc
        exam_type = cell_text[1]
        code_links = cells[4].select("a.code-tag")
        listed_codes = [a.get_text(" ", strip=True) for a in code_links]
        option_rates = [percent(x) for x in cell_text[7:12]]
        answer = None
        for index, cell in enumerate(cells[7:12], start=1):
            if "correct-answer-cell" in (cell.get("class") or []):
                answer = index
                break
        title_link = cells[3].find("a")
        exam_link = cells[1].find("a")
        rows.append({
            "queried_code_number": query_code["number"],
            "queried_code_name": query_code["name"],
            "exam_family": exam_family(exam_type),
            "year": year,
            "exam_type": exam_type,
            "question": question,
            "title": cell_text[3],
            "listed_codes": listed_codes,
            "domain": cell_text[5],
            "estimated_correct_rate_percent": percent(cell_text[6]),
            "option_selection_rates_percent": option_rates,
            "site_marked_answer": answer,
            "exam_search_url": urljoin(BASE, exam_link["href"]) if exam_link else None,
            "title_search_url": urljoin(BASE, title_link["href"]) if title_link else None,
            "code_search_url": url,
            "fetched_at": fetched_at,
            "source_role": "third_party_candidate_label",
        })
    return rows


def key(row: dict) -> tuple:
    return row["year"], row["exam_type"], row["question"], row["title"]


def main() -> None:
    ROOT.mkdir(exist_ok=True)
    RAW.mkdir(exist_ok=True)
    REPORT.parent.mkdir(exist_ok=True)
    fetched_at = datetime.now(ZoneInfo("Asia/Seoul")).isoformat(timespec="seconds")
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; local-research-index/1.0)",
        "Accept-Language": "ko-KR,ko;q=0.9",
    })

    catalog_response = session.get(CATALOG_URL, timeout=30)
    catalog_response.raise_for_status()
    catalog_response.encoding = "utf-8"
    codes, categories = parse_catalog(catalog_response.text)

    all_rows = []
    search_sources = []
    for code in codes:
        response = session.get(SEARCH_URL, params={"CodeName": code["name"]}, timeout=30)
        response.raise_for_status()
        response.encoding = "utf-8"
        raw_path = RAW / f"{code['number']:03d}_{code['name'].replace('/', '_')}.html"
        raw_path.write_bytes(response.content)
        rows = parse_search(response.text, code, fetched_at, response.url)
        all_rows.extend(rows)
        search_sources.append({
            "code_number": code["number"],
            "code_name": code["name"],
            "url": response.url,
            "status_code": response.status_code,
            "sha256": sha256_bytes(response.content),
            "row_count": len(rows),
            "raw_file": str(raw_path),
        })
        time.sleep(0.08)

    with LABELS_OUT.open("w", encoding="utf-8") as handle:
        for row in all_rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    grouped: dict[tuple, dict] = {}
    for row in all_rows:
        item = grouped.setdefault(key(row), {
            **{field: row[field] for field in (
                "exam_family", "year", "exam_type", "question", "title", "domain",
                "estimated_correct_rate_percent", "option_selection_rates_percent",
                "site_marked_answer", "exam_search_url", "title_search_url",
            )},
            "site_codes": set(),
            "queried_codes_matched": set(),
            "source_role": "third_party_candidate_label",
        })
        item["site_codes"].update(row["listed_codes"])
        item["queried_codes_matched"].add(row["queried_code_name"])
    unique_rows = []
    for item in grouped.values():
        item["site_codes"] = sorted(item["site_codes"])
        item["queried_codes_matched"] = sorted(item["queried_codes_matched"])
        unique_rows.append(item)
    unique_rows.sort(key=lambda x: (-x["year"], x["exam_type"], x["question"], x["title"]))
    with QUESTIONS_OUT.open("w", encoding="utf-8") as handle:
        for row in unique_rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    catalog_payload = {
        "status": "collected_unverified_third_party_index",
        "fetched_at": fetched_at,
        "catalog_url": CATALOG_URL,
        "catalog_sha256": sha256_bytes(catalog_response.content),
        "code_count": len(codes),
        "category_count": len(categories),
        "label_hit_count": len(all_rows),
        "unique_question_count": len(unique_rows),
        "codes": codes,
        "search_sources": search_sources,
        "disclaimer": (
            "사이트 코드는 제3자 후보 라벨이다. 로컬 원문·선지·정답을 다시 판독하기 전에는 "
            "프로젝트 확정 코드로 사용하지 않는다. 정답률도 사이트가 명시한 추정치이다."
        ),
    }
    CATALOG_OUT.write_text(json.dumps(catalog_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    family_counts = Counter(row["exam_family"] for row in unique_rows)
    code_counts = {source["code_number"]: source["row_count"] for source in search_sources}
    no_hits = [code for code in codes if code_counts[code["number"]] == 0]
    lines = [
        "# 100코드 사이트 색인 수집 현황 v1",
        "",
        f"- 수집 시각: {fetched_at}",
        f"- 코드 원표: [{CATALOG_URL}]({CATALOG_URL})",
        f"- 코드 수: {len(codes)}개",
        f"- 코드별 검색 적중 행: {len(all_rows)}건",
        f"- 중복 통합 문항: {len(unique_rows)}개",
        f"- 평가원 계열: {family_counts['KICE']}개",
        f"- LEET: {family_counts['LEET']}개",
        f"- MEET: {family_counts['MEET']}개",
        f"- 기타: {family_counts['OTHER']}개",
        "",
        "> 이 자료는 제3자 사이트가 붙인 **후보 코드 색인**이다. 코드가 비어 있거나 붙어 있다는 사실만으로 프로젝트의 확정 판정이 되지 않는다. 정답률은 사이트 안내대로 추정치로만 보존한다.",
        "",
        "## 코드별 적중 수",
        "",
        "| 번호 | 범주 | 코드 | 별칭 | 적중 | 검색 |",
        "| ---: | --- | --- | --- | ---: | --- |",
    ]
    for code, source in zip(codes, search_sources):
        aliases = ", ".join(code["aliases"])
        lines.append(
            f"| #{code['number']} | {code['category']} | {code['name']} | {aliases} | "
            f"{source['row_count']} | [검색 결과]({source['url']}) |"
        )
    lines.extend(["", "## 적중 0건 코드", ""])
    lines.append("- " + ", ".join(f"#{c['number']} {c['name']}" for c in no_hits) if no_hits else "- 없음")
    lines.extend([
        "",
        "## 생성 파일",
        "",
        f"- 코드 원표·응답 해시: `{CATALOG_OUT}`",
        f"- 코드별 적중 행: `{LABELS_OUT}`",
        f"- 문항별 중복 통합 색인: `{QUESTIONS_OUT}`",
        f"- 원시 HTML: `{RAW}/`",
        "",
        "## 다음 검증 단계",
        "",
        "1. KICE·LEET 문항을 로컬 정본과 시험명·연도·문항 번호로 연결한다.",
        "2. 지문 근거와 정답 결정 관계를 읽어 주 코드·보조 코드를 다시 판정한다.",
        "3. 비슷한 코드가 왜 주 코드가 아닌지와 각 오답의 변형 지점을 기록한다.",
    ])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"codes={len(codes)} hits={len(all_rows)} unique={len(unique_rows)} "
        f"families={dict(family_counts)} no_hits={len(no_hits)}"
    )
    print(CATALOG_OUT)
    print(LABELS_OUT)
    print(QUESTIONS_OUT)
    print(REPORT)


if __name__ == "__main__":
    main()
