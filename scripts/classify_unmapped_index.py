#!/usr/bin/env python3
"""Triage textbook index entries not yet connected to a core ontology concept."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


PEOPLE = {
    "간디", "그레타 툰베리", "노자", "달라이 라마", "데일 카네기", "레오폴드", "맹자", "밀",
    "박연", "베이컨", "부탄", "소로", "아리스토텔레스", "이태석 신부", "정약용", "칸트",
    "토머스 쿤", "토머스 모어", "헬렌 켈러", "갈퉁", "노직", "루소", "롤스", "말랄라 유사프자이",
    "매킨타이어", "모겐소", "벤담", "샌델", "애덤 스미스", "에밀리 데이비슨", "왈처", "요나스",
    "제프 멀건", "커즈와일", "케인스", "프리드먼", "하이에크",
}

INSTITUTION_PATTERNS = (
    "법", "협약", "협정", "의정서", "선언", "위원회", "기구", "연합", "회의", "제도", "정책",
    "사업", "조약", "재판", "심판", "공청회", "협의체", "기금", "계획",
)
INDICATOR_PATTERNS = ("지수", "지표", "비율", "율", "부양비", "출산율", "성장률", "수익성", "안전성", "유동성")
JOB_PATTERNS = ("전문가", "관리자", "상담원", "조종사", "평가사", "장의사", "탐정", "크리에이터")
CONCEPT_PATTERNS = (
    "주의", "권리", "정의", "평등", "효과", "비용", "구조", "현상", "문제", "과정", "관점",
    "관계", "체제", "시장", "경제", "문화", "자원", "에너지", "인구", "사회", "환경", "평화",
    "세계화", "도시화", "산업화", "민주주의", "자본주의", "분업", "무역", "소비", "생산",
    "소득", "금융", "기후", "지형", "농업", "윤리", "가치", "격차", "차별", "폭력", "자유",
)


def category(term: str) -> str:
    if term in PEOPLE:
        return "인물·사상가"
    if term.endswith(JOB_PATTERNS):
        return "미래 직업·사례"
    if any(pattern in term for pattern in INSTITUTION_PATTERNS):
        return "법·제도·기관·문서"
    if any(term.endswith(pattern) or pattern in term for pattern in INDICATOR_PATTERNS):
        return "지표·측정 개념"
    if any(pattern in term for pattern in CONCEPT_PATTERNS):
        return "하위 개념 후보"
    if re.search(r"(공화국|도시|지역|국가|아시아|유럽|아메리카|아프리카|오세아니아)$", term):
        return "지역·공간 사례"
    return "사례·세부 용어"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audit_json", type=Path)
    parser.add_argument("json_output", type=Path)
    parser.add_argument("markdown_output", type=Path)
    args = parser.parse_args()

    audit = json.loads(args.audit_json.read_text(encoding="utf-8"))
    entries = []
    for item in audit["unmapped_index"]:
        term = item["term"].replace("\xad", "")
        entries.append({**item, "term": term, "category": category(term)})
    entries.sort(key=lambda item: (item["category"], item["course"], item["term"]))
    counts = Counter(item["category"] for item in entries)

    args.json_output.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# 교과서 색인 미연결 항목 1차 분류",
        "",
        "> 자동 분류 결과이며, `하위 개념 후보`는 독립 온톨로지 승격 여부를 수동 검토한다.",
        "",
        "## 분류 집계",
        "",
        "| 분류 | 항목 수 |",
        "|---|---:|",
    ]
    for name, count in sorted(counts.items()):
        lines.append(f"| {name} | {count} |")
    for name in sorted(counts):
        lines.extend(["", f"## {name}", "", "| 과목 | 항목 | 교과서 쪽 |", "|---|---|---|"])
        for item in entries:
            if item["category"] != name:
                continue
            lines.append(
                f"| {item['course']} | {item['term']} | {', '.join(map(str, item['textbook_pages']))} |"
            )
    args.markdown_output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"classified {len(entries)} unmapped index entries")


if __name__ == "__main__":
    main()
