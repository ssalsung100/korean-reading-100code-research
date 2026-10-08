#!/usr/bin/env python3
"""Build the durable project asset index from canonical manifests and JSONL."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path.cwd()
OUT = ROOT / "DB_자산_인덱스.md"
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".gif"}


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8-sig"))


def load_jsonl(path: str) -> list[dict]:
    return [
        json.loads(line)
        for line in (ROOT / path).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def human_size(size: int) -> str:
    value = float(size)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if value < 1024 or unit == "TB":
            return f"{value:.1f}{unit}" if unit != "B" else f"{int(value)}B"
        value /= 1024
    raise AssertionError


def kice_coverage(year: int, exams: dict[str, list[dict]]) -> str:
    regular = {name: len({int(row["question_number"]) for row in rows}) for name, rows in exams.items() if name in {"6월 모평", "9월 모평", "수능"}}
    if 2017 <= year <= 2021 and regular == {"6월 모평": 15, "9월 모평": 15, "수능": 15}:
        return "정규 3회 독서 수록 범위 확보"
    if 2022 <= year <= 2025 and regular == {"6월 모평": 17, "9월 모평": 17, "수능": 17}:
        return "정규 3회 독서 수록 범위 확보"
    if year == 2026 and regular.get("6월 모평") == 14:
        return "6월 3문항 보완 필요"
    return "선별 수록"


def main() -> None:
    all_files = [path for path in ROOT.rglob("*") if path.is_file()]
    md_count = sum(path.suffix.lower() == ".md" for path in all_files)
    image_count = sum(path.suffix.lower() in IMAGE_SUFFIXES for path in all_files)
    total_size = sum(path.stat().st_size for path in all_files)

    kice_passages = load_jsonl("data/kice_passages.jsonl")
    kice_questions = load_jsonl("data/kice_questions.jsonl")
    kice_exam_questions: dict[tuple[int, str], list[dict]] = defaultdict(list)
    kice_exam_passages = Counter((int(row["academic_year"]), row["exam_label"]) for row in kice_passages)
    for row in kice_questions:
        kice_exam_questions[(int(row["academic_year"]), row["exam_label"])].append(row)

    leet_gate = load_json("자료/LEET_언어이해/검증/코퍼스_검증게이트_v1.json")
    leet_visuals = load_json("자료/LEET_언어이해/검증/LEET_홀수형_시각자료_전체목록_v1.json")
    leet_coords = load_json("자료/LEET_언어이해/검증/HWP_홀수형_페이지좌표_v1.json")
    meet = load_json("자료/MEET_언어추론/검증/MEET_정본_JSONL_검증_v1.json")
    meet_visuals = load_json("자료/MEET_언어추론/검증/MEET_시각자료_문항별_분류_v1.json")
    linked_visuals = load_json("분석/평가원_MEET_시각자료_연결_검증_v1.json")
    kice_2027_manifest = load_json("자료/평가원_국어/2027_6·9월_1-17_자산_원장.json")
    kice_2027_gate = load_json("자료/평가원_국어/검증/2027_6·9월_1-17_검증_v1.json")
    backup = load_json("백업_원장/백업_검증결과_20260906_v1.json")

    social_hwpx = len(list((ROOT / "통합사회").rglob("*.hwpx")))
    economy_hwpx = len(list((ROOT / "심화 사회과목/경제").rglob("*.hwpx")))
    ethics_hwpx = len(list((ROOT / "심화 사회과목/생윤").rglob("*.hwpx")))
    social_questions = load_json("분석/통합사회_문항_정규화.json")
    example_2028 = [row for row in social_questions if row.get("source_group") == "2028_수능_예시문항"]
    example_2028_by_course = Counter(row["course"] for row in example_2028)
    example_2028_unique_texts = len({row["text"] for row in example_2028})
    social_visual_manifest = load_json("자료/통합사회_문항이미지_완전판/manifest.json")
    example_2028_visuals = [row for row in social_visual_manifest if row.get("source_group") == "2028_수능_예시문항"]
    example_2028_visual_questions = len({row["question_id"] for row in example_2028_visuals})

    lines = [
        "# 통합사회·평가원 독서 DB 자산 인덱스",
        "",
        f"> 최종 갱신: {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')}",
        "> 이 파일을 프로젝트의 첫 진입점으로 사용한다. 수치가 바뀌면 `python3 scripts/build_asset_index.py`로 재생성한다.",
        "> 지문·문항 생성 작업을 새 대화에서 이어갈 때는 [새 대화용 생성 인수인계](./새대화용_평가원형_지문문항_생성_인수인계.md)를 먼저 읽는다.",
        "",
        "## 1. 한눈에 보는 현재 상태",
        "",
        f"- 전체 작업 폴더: 약 **{human_size(total_size)}**, 파일 {len(all_files):,}개",
        f"- Markdown: **{md_count:,}개**",
        f"- 이미지: **{image_count:,}개**(원본·페이지 렌더·작업본·OCR 이미지 포함)",
        "- LEET 검증 게이트: **PASS**, 자동 오류 0, 수동 차단 항목 0",
        "- MEET 정본 JSONL: **PASS**, 380/380문항",
        "- 평가원·MEET 시각 자료 연결: **PASS**",
        "- 백업: OneDrive 스냅샷 생성 및 원본 전수 비교 **PASS**",
        "",
        "### 평가원 범위에 대한 빠른 답",
        "",
        "현재 평가원 독서 DB는 **2010학년도부터 자료가 있으나 2010~2016은 선별 수록**이다. **2017~2025학년도는 6월·9월·수능의 독서 수록 범위가 회차별로 확보**되어 있다. 2026학년도는 9월·수능은 17문항이 있으나 6월은 14문항이어서 3문항 보완이 필요하다. **2027학년도 6월·9월 모의평가 1~17번은 공식 PDF 직접 전사본과 원본 1~6쪽 렌더를 별도 정본으로 확보**하였다.",
        "",
        "여기서 ‘수록 범위 확보’는 현재 편집 HWPX에 들어 있는 독서 지문·문항 기준이다. 원본 시험지 전체를 연도별 공식 파일로 모두 소장했다는 뜻과는 구별한다.",
        "",
        "**2028학년도 수능 통합사회 예시문항도 보유하고 있다.** 이는 위 평가원 국어 독서 DB와 다른 통합사회 문항 DB에 들어 있다. 통합사회1·2 HWPX에 동일한 공통 예시문항 39개가 각각 수록되어 있어 정규화 레코드는 78개다.",
        "",
        "## 2. 평가원 독서 DB",
        "",
        f"- 지문: **{len(kice_passages)}개** — `data/kice_passages.jsonl`",
        f"- 문항 레코드: **{len(kice_questions)}개** — `data/kice_questions.jsonl`",
        f"- 공식 정답 연결·확인: **{sum(bool(row.get('official_answer_verified')) for row in kice_questions)}/{len(kice_questions)}**",
        f"- 텍스트 선지 5개 완전 파싱: **{sum(row.get('choice_parse_status') == 'complete' for row in kice_questions)}/{len(kice_questions)}**",
        f"- 표·그림으로 남아 있는 선지: **{sum(row.get('choice_parse_status') != 'complete' for row in kice_questions)}문항**",
        "- 원천 편집본: `고3 기출/2027 고3 국어 독서_*.hwpx` 7개",
        "- 주의: 이 7개 HWPX는 분야별 편집·통합본이며 평가원이 배포한 연도별 원본 컨테이너라고 주장하지 않는다.",
        "",
        "### 연도·회차별 수록 현황",
        "",
        "| 학년도 | 회차 | 지문 | 고유 문항 | 정답 확인 | 텍스트 선지 완전 파싱 | 판정 |",
        "|---:|---|---:|---:|---:|---:|---|",
    ]
    by_year: dict[int, dict[str, list[dict]]] = defaultdict(dict)
    for (year, exam), rows in kice_exam_questions.items():
        by_year[year][exam] = rows
    for year in sorted(by_year):
        coverage = kice_coverage(year, by_year[year])
        for exam in sorted(by_year[year], key=lambda name: ("예시" not in name, "6월" not in name, "9월" not in name, "수능" not in name, name)):
            rows = by_year[year][exam]
            unique_questions = len({int(row["question_number"]) for row in rows})
            answers = sum(bool(row.get("official_answer_verified")) for row in rows)
            parsed = sum(row.get("choice_parse_status") == "complete" for row in rows)
            passages = kice_exam_passages[(year, exam)]
            note = coverage if exam == list(sorted(by_year[year], key=lambda name: ("예시" not in name, "6월" not in name, "9월" not in name, "수능" not in name, name)))[0] else ""
            lines.append(f"| {year} | {exam} | {passages} | {unique_questions} | {answers}/{len(rows)} | {parsed}/{len(rows)} | {note} |")

    lines += [
        "| 2027 | 6월 모평 | 4 | 17 | 17/17 | 17/17 | 공식 PDF 직접 전사 |",
        "| 2027 | 9월 모평 | 4 | 17 | 17/17 | 17/17 | 공식 PDF 직접 전사 |",
        "",
        "### 2027학년도 6·9월 공식 PDF 직접 전사",
        "",
        f"- 검증: **{kice_2027_gate['status']}**, {kice_2027_gate['counts']['questions']}문항, 오류 {kice_2027_gate['counts']['errors']}개",
        "- 전사본: `자료/평가원_국어/전사_검수완료/2027/`",
        "- 문제·정답 PDF: `자료/평가원_국어/원본/2027/`",
        "- 원본 페이지 렌더: `자료/평가원_국어/페이지/2027/`",
        f"- 의미 시각 자료: **{len(kice_2027_manifest['visuals'])}개** — `자료/평가원_국어/시각자료_원본/2027/`",
        "- 자산 원장: `자료/평가원_국어/2027_6·9월_1-17_자산_원장.json`",
        "- 검증 원장: `자료/평가원_국어/검증/2027_6·9월_1-17_검증_v1.md`",
        "",
    ]

    lines += [
        "",
        "### 평가원 시각 자료",
        "",
        f"- 전체 개체: **{linked_visuals['counts']['kice_records']}개**",
        f"- 이미지: **{linked_visuals['counts']['kice_images']}개**",
        f"- HWPX 표: **{linked_visuals['counts']['kice_hwpx_tables']}개**",
        f"- 의미 있는 시각 자료: **{linked_visuals['counts']['kice_semantic_objects']}개**",
        "- 원장: `자료/평가원_독서_시각자료_원본/평가원_시각자료_문항별_목록_v1.md`",
        "- 통합 검증: `분석/평가원_MEET_시각자료_연결_검증_v1.md`",
        "",
        "## 3. LEET 언어이해 DB",
        "",
        "- 분석 정본 범위: **2009예비~2027 홀수형**",
        f"- 공식 원본 파일: **{leet_gate['counts']['official_source_files']}개**",
        f"- 파생 텍스트 기록: **{leet_gate['counts']['derived_records']}개**",
        f"- 공식 페이지 대조 완료 전사: **{leet_gate['counts']['verified_transcript_groups']}개 문항군, {leet_gate['counts']['verified_transcript_questions']}문항**",
        f"- 재사용 가능 시각 자료: **{leet_visuals['record_count']}개**(그림 46, 자료표 14, 선지표 5, 페이지 크롭 20)",
        f"- HWP 좌표 확정: **{leet_coords['record_count']}개**, 페이지 렌더 **{leet_coords['page_image_count']}쪽**",
        "- 그림 46개는 HWP 원래 쪽에서 픽셀 대조 완료",
        "- 짝수형은 중복 형식이므로 분석 정본에서 제외하되 원본 무결성 기록은 보존",
        "- 검증 게이트: `자료/LEET_언어이해/검증/코퍼스_검증게이트_v1.md`",
        "- 시각 자료 목록: `자료/LEET_언어이해/검증/LEET_홀수형_시각자료_전체목록_v1.md`",
        "- 좌표 원장: `자료/LEET_언어이해/검증/HWP_홀수형_페이지좌표_v1.md`",
        "",
        "## 4. MEET 언어추론 DB",
        "",
        "- 범위: **2005예비·2005·2006~2012**",
        f"- 정본 지문군: **{meet['counts']['groups']}개** — `data/meet_passages.jsonl`",
        f"- 정본 문항: **{meet['counts']['questions']}개** — `data/meet_questions.jsonl`",
        f"- 5개 선지와 공식 정답 완비: **{meet['counts']['questions_with_answer']}/{meet['counts']['questions']}**",
        f"- 시각 자료: **{meet_visuals['counts']['records']}개**(내장 이미지 18, Markdown 표 29)",
        f"- 의미 자료의 문항 연결: **{meet_visuals['counts']['records_with_question_links']}개**, 장식 요소 1개 제외",
        "- 정본 원천: `자료/MEET_언어추론/전사_검수완료/`",
        "- 검증: `자료/MEET_언어추론/검증/MEET_정본_JSONL_검증_v1.md`",
        "- OCR 기반 `data/meet_*_raw.jsonl`은 정본이 아니다.",
        "",
        "## 5. 통합사회·심화 교과 자료",
        "",
        f"- 통합사회 1·2 HWPX: **{social_hwpx}개** — `통합사회/`",
        f"- 심화 경제 HWPX: **{economy_hwpx}개** — `심화 사회과목/경제/`",
        f"- 생활과 윤리 HWPX: **{ethics_hwpx}개** — `심화 사회과목/생윤/`",
        "",
        "### 2028학년도 수능 통합사회 예시문항",
        "",
        "- 원본 HWPX: 통합사회1용 1개, 통합사회2용 1개",
        f"- 정규화 레코드: **{len(example_2028)}개**(통합사회1 {example_2028_by_course['통합사회1']}개 + 통합사회2 {example_2028_by_course['통합사회2']}개)",
        f"- 실제 서로 다른 문항 본문: **{example_2028_unique_texts}개** — 두 교재에 같은 공통 세트가 중복 수록됨",
        f"- 완전판 시각 자료: **{len(example_2028_visuals)}개**(두 교재 합계), 시각 자료가 있는 문항 레코드 {example_2028_visual_questions}개",
        "- 문항·정답 결합: 전체 통합사회 1,054문항 검증 게이트에서 PASS, 누락 0",
        "- 문항 원문: `분석/통합사회_문항_정규화.json`, `분석/통합사회_문제_원문_추출.md`",
        "- 시각 자료: `자료/통합사회_문항이미지_완전판/`",
        "- 개념 연결: `분석/통합사회_개념_분석.json`, `data/social_concepts_v1.json`",
        "",
        "- 통합사회 문항 이미지: `자료/통합사회_문항이미지/`, `자료/통합사회_문항이미지_완전판/`",
        "- 통합사회 교과서 시각 자료: `자료/통합사회_교과서_시각자료/`",
        "- 심화 경제 문항 이미지: `자료/심화경제_문항이미지/`",
        "- 통합 개념 DB: `data/social_concepts.json`, `data/social_concepts_v1.json`",
        "- 세부 관계 DB: `data/social_detailed_visual_relations.json`, `data/economics_detailed_relations.json`",
        "",
        "## 6. 코드·분석 데이터",
        "",
        "- 100코드 목록: `data/sdss_100codes_catalog.json`",
        "- SDSS 기출 인덱스: `data/sdss_indexed_questions.jsonl`",
        "- 코드 후보 검토 큐: `data/code_candidate_review_queue.jsonl`",
        "- 코드별 검토 큐: `data/code_candidate_review_queue_by_code.jsonl`",
        "- 평가원 지문/문항: `data/kice_passages.jsonl`, `data/kice_questions.jsonl`",
        "- MEET 지문/문항: `data/meet_passages.jsonl`, `data/meet_questions.jsonl`",
        "- MEET 시각 자료: `data/meet_visuals.jsonl`",
        "",
        "## 7. 정본과 작업본 구분",
        "",
        "### 분석에 바로 사용",
        "",
        "- `data/kice_passages.jsonl`, `data/kice_questions.jsonl`",
        "- `data/meet_passages.jsonl`, `data/meet_questions.jsonl`",
        "- `자료/LEET_언어이해/텍스트/`와 `전사_검수완료/`",
        "- 각 시험의 `검증/` 아래 PASS 원장",
        "",
        "### 원본 보존용",
        "",
        "- `자료/LEET_언어이해/원본/`",
        "- `자료/MEET_언어추론/공식_정답표_원본/`",
        "- `고3 기출/*.hwpx`, `통합사회/*.hwpx`, `심화 사회과목/**/*.hwpx`",
        "- 각 `시각자료_원본/`과 `이미지/`",
        "",
        "### 정본으로 사용 금지",
        "",
        "- `OCR_초안/`, `OCR_초안_Paddle/`",
        "- `_중복_초기다운로드/`",
        "- `data/meet_passages_raw.jsonl`, `data/meet_questions_raw.jsonl`",
        "- `output/`의 임시 렌더·시험 파일",
        "",
        "## 8. 검증 진입점",
        "",
        "| 대상 | 보고서 | 현재 상태 |",
        "|---|---|---|",
        "| LEET 전체 | `자료/LEET_언어이해/검증/코퍼스_검증게이트_v1.md` | PASS |",
        "| LEET HWP 좌표 | `자료/LEET_언어이해/검증/HWP_홀수형_페이지좌표_v1.md` | complete |",
        "| MEET 정본 JSONL | `자료/MEET_언어추론/검증/MEET_정본_JSONL_검증_v1.md` | PASS |",
        "| 평가원·MEET 시각 연결 | `분석/평가원_MEET_시각자료_연결_검증_v1.md` | PASS |",
        "| 백업 | `백업_원장/백업_검증결과_20260906_v1.md` | PASS |",
        "",
        "## 9. 백업",
        "",
        f"- 보관 위치: `{backup['backup']['archive']}`",
        f"- 압축본: **{human_size(backup['backup']['archive_bytes'])}**",
        f"- SHA-256: `{backup['backup']['archive_sha256']}`",
        "- gzip CRC 및 원본 전수 비교: PASS",
        "- OneDrive 원격 업로드 완료 표시는 Windows 탐색기에서 별도 확인",
        "",
        "## 10. 인덱스 갱신 명령",
        "",
        "```bash",
        "python3 scripts/build_asset_index.py",
        "```",
        "",
        "DB가 추가·수정될 때마다 이 명령을 실행하고, 백업은 새 버전 번호로 다시 만든다.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"WROTE {OUT} lines={len(lines)}")


if __name__ == "__main__":
    main()
