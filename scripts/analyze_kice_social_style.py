#!/usr/bin/env python3
"""평가원 사회계열 MD에서 지문 본문만 분리해 문체 통계를 만든다."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "고3 기출" / "hwpx_텍스트_소재별.md"
OUT_JSON = ROOT / "분석" / "평가원_사회지문_문체통계_v1.json"
OUT_MD = ROOT / "분석" / "평가원_사회지문_문체통계_v1.md"


text = SOURCE.read_text(encoding="utf-8")
social = text.split("## Ⅱ. 사회", 1)[1].split("## Ⅲ.", 1)[0]

subsections = re.split(r"(?m)^### ", social)
records: list[dict] = []
for subsection in subsections[1:]:
    lines = subsection.splitlines()
    category = lines[0].strip()
    body = "\n".join(lines[1:])
    blocks = re.split(r"(?m)^#### ", body)
    for block in blocks[1:]:
        block_lines = block.splitlines()
        title = block_lines[0].strip()
        block_body = "\n".join(block_lines[1:])
        matches = re.findall(r"(?ms)^-{20,}\s*$\n(.*?)\n^-{20,}\s*$", block_body)
        if not matches:
            continue
        passage = matches[0].strip()
        passage = re.sub(r"(?m)^- 원본:.*$", "", passage).strip()
        records.append({"category": category, "title": title, "passage": passage})


def clean_for_sentences(passage: str) -> str:
    value = re.sub(r"&lt;|&gt;", "", passage)
    value = re.sub(r"(?m)^\s*\[[A-Z가-힣]+\]\s*$", "", value)
    value = re.sub(r"(?m)^\s*\([가-힣]\)\s*$", "", value)
    value = re.sub(r"(?m)^\s*✽.*$", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def split_sentences(passage: str) -> list[str]:
    cleaned = clean_for_sentences(passage)
    parts = re.split(r"(?<=[.!?])\s+(?=[‘“" + "'" + r"(㉠-㉿가-힣A-Z0-9])", cleaned)
    return [p.strip() for p in parts if len(p.strip()) >= 8]


sentences: list[dict] = []
for record in records:
    for sentence in split_sentences(record["passage"]):
        sentences.append({
            "category": record["category"],
            "title": record["title"],
            "sentence": sentence,
        })

start_connectors = [
    "그러나", "하지만", "반면", "한편", "따라서", "그러므로", "이때", "이처럼",
    "이에", "또한", "다만", "즉", "예를 들어", "가령", "그런데", "결국", "우선",
]
connector_counts = Counter()
for row in sentences:
    sentence = row["sentence"]
    for connector in start_connectors:
        if sentence.startswith(connector):
            connector_counts[connector] += 1
            break

ending_patterns = [
    ("~할 수 있다", r"할 수 있다\.$"),
    ("~할 수 없다", r"할 수 없다\.$"),
    ("~한다", r"한다\.$"),
    ("~된다", r"된다\.$"),
    ("~있다", r"있다\.$"),
    ("~없다", r"없다\.$"),
    ("~이다", r"이다\.$"),
    ("~아니다", r"아니다\.$"),
    ("~것이다", r"것이다\.$"),
    ("~본다", r"본다\.$"),
    ("~말한다", r"말한다\.$"),
    ("~부른다", r"부른다\.$"),
    ("~의미한다", r"의미한다\.$"),
    ("~뜻한다", r"뜻한다\.$"),
    ("~하였다", r"하였다\.$"),
    ("~했다", r"했다\.$"),
]
ending_counts = Counter()
for row in sentences:
    sentence = row["sentence"]
    matched = False
    for name, pattern in ending_patterns:
        if re.search(pattern, sentence):
            ending_counts[name] += 1
            matched = True
            break
    if not matched:
        ending_counts["기타"] += 1

function_patterns = {
    "definition": r"(?:이라 한다|라고 한다|라 한다|을 말한다|를 말한다|뜻한다|의미한다|부른다|정의한다)",
    "condition": r"(?:경우|때에는|때는|하면|한다면|라면|이면|수록)",
    "cause_result": r"(?:때문이다|때문에|로 인해|에 따라|결과|초래|이어져|따라서)",
    "comparison": r"(?:반면|와 달리|에 비해|보다|공통점|차이)",
    "exception_limit": r"(?:다만|예외|그러나|반드시 .* 필요는|수는 없다|에 불과|한정)",
    "example": r"(?:예를 들어|예컨대|가령|사례|이를테면)",
}
function_rows: dict[str, list[dict]] = defaultdict(list)
for row in sentences:
    for name, pattern in function_patterns.items():
        if re.search(pattern, row["sentence"]):
            function_rows[name].append(row)

phrase_counts = {
    "이라 하자": sum(row["sentence"].count("이라 하자") for row in sentences),
    "라고 하자": sum(row["sentence"].count("라고 하자") for row in sentences),
    "라 하자": sum(row["sentence"].count("라 하자") for row in sentences),
    "이라 한다": sum(row["sentence"].count("이라 한다") for row in sentences),
    "라고 한다": sum(row["sentence"].count("라고 한다") for row in sentences),
    "라 한다": sum(row["sentence"].count("라 한다") for row in sentences),
    "수 있다": sum(row["sentence"].count("수 있다") for row in sentences),
    "것이다": sum(row["sentence"].count("것이다") for row in sentences),
}

lengths = [len(re.sub(r"\s+", "", row["sentence"])) for row in sentences]
category_counts = Counter(record["category"] for record in records)

result = {
    "source": str(SOURCE.relative_to(ROOT)),
    "passage_count": len(records),
    "sentence_count": len(sentences),
    "category_passage_counts": dict(category_counts),
    "sentence_length_nonspace": {
        "mean": round(sum(lengths) / len(lengths), 1),
        "min": min(lengths),
        "max": max(lengths),
        "median": sorted(lengths)[len(lengths) // 2],
    },
    "connector_counts": dict(connector_counts.most_common()),
    "ending_counts": dict(ending_counts.most_common()),
    "phrase_counts": phrase_counts,
    "function_counts": {name: len(rows) for name, rows in function_rows.items()},
    "records": records,
    "examples": {
        name: rows[:12] for name, rows in function_rows.items()
    },
}
OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def compact(sentence: str, limit: int = 150) -> str:
    sentence = sentence.replace("|", "\\|")
    return sentence if len(sentence) <= limit else sentence[: limit - 1] + "…"


example_sections = []
for name, rows in function_rows.items():
    lines = [f"### {name}", "", "| 기출 | 문장 |", "|---|---|"]
    for row in rows[:12]:
        lines.append(f"| {row['title']} | {compact(row['sentence'])} |")
    example_sections.append("\n".join(lines))

report = f"""# 평가원 사회 지문 문체 통계 v1

## 범위

- 원본: `{result['source']}`
- 추출 지문: {len(records)}개
- 추출 문장: {len(sentences)}개
- 범주별 지문: {dict(category_counts)}

## 문장 길이

- 공백 제외 평균: {result['sentence_length_nonspace']['mean']}자
- 중앙값: {result['sentence_length_nonspace']['median']}자
- 최소~최대: {result['sentence_length_nonspace']['min']}~{result['sentence_length_nonspace']['max']}자

## 정의 어조 확인

| 표현 | 횟수 |
|---|---:|
""" + "\n".join(f"| `{key}` | {value} |" for key, value in phrase_counts.items()) + f"""

## 문두 연결어

| 연결어 | 횟수 |
|---|---:|
""" + "\n".join(f"| {key} | {value} |" for key, value in connector_counts.most_common()) + f"""

## 종결형

| 종결 | 횟수 |
|---|---:|
""" + "\n".join(f"| {key} | {value} |" for key, value in ending_counts.most_common()) + f"""

## 문장 기능별 후보 수

""" + "\n".join(f"- {key}: {len(value)}문장" for key, value in function_rows.items()) + "\n\n" + "\n\n".join(example_sections) + "\n"

OUT_MD.write_text(report, encoding="utf-8")
print(json.dumps({
    "passages": len(records),
    "sentences": len(sentences),
    "mean_nonspace": result["sentence_length_nonspace"]["mean"],
    "haja": phrase_counts["이라 하자"] + phrase_counts["라고 하자"] + phrase_counts["라 하자"],
}, ensure_ascii=False))
