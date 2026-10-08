#!/usr/bin/env python3
"""Analyze repeated QZip passages as a noncanonical discrepancy locator.

Three consecutive LEET questions normally share one passage. Independent
differences between those repeated secondary transcriptions reveal likely
typos, but no consensus text is promoted to the official corpus.
"""
from __future__ import annotations

import difflib
import json
import re
from pathlib import Path

from rapidfuzz import fuzz


ROOT = Path("자료/LEET_언어이해")
QZIP = ROOT / "검증" / "외부대조_QZip"
OUT_JSON = ROOT / "검증" / "QZip_반복지문_불일치_v1.json"
OUT_MD = ROOT / "검증" / "QZip_반복지문_불일치_v1.md"


def lexical(text: str) -> str:
    return re.sub(r"[^0-9A-Za-z가-힣]", "", text)


def passage_candidate(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^# [^\n]+\n+", "", text)
    text = re.sub(r"^> QZip[^\n]+\n+", "", text)
    text = re.sub(r"^\*\*다음 글을 읽고 물음에 답하시오\.\*\*\n+", "", text)
    choice = re.search(r"(?m)^[①②③④⑤]\s", text)
    if choice:
        text = text[:choice.start()]
    if "\n---\n" in text:
        text = text.split("\n---\n", 1)[0]
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    while paragraphs and ("?" in paragraphs[-1] or paragraphs[-1].endswith("것은？")):
        paragraphs.pop()
    return "\n\n".join(paragraphs).strip()


def diff_ops(a: str, b: str) -> list[dict]:
    ops = []
    matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        ops.append({
            "tag": tag, "a": a[i1:i2], "b": b[j1:j2],
            "a_context": a[max(0, i1 - 18):min(len(a), i2 + 18)],
            "b_context": b[max(0, j1 - 18):min(len(b), j2 + 18)],
        })
    return ops


def main() -> None:
    groups = []
    for year in (2022, 2023, 2024):
        official = None
        if year == 2024:
            official_path = ROOT / "텍스트" / "2024" / "2024_question_odd.md"
            official = lexical(official_path.read_text(encoding="utf-8"))
        for start in range(1, 31, 3):
            candidates = []
            for number in range(start, start + 3):
                path = QZIP / str(year) / f"q{number:02d}.md"
                text = passage_candidate(path)
                norm = lexical(text)
                if len(norm) >= 500:
                    candidates.append({"question": number, "file": str(path), "text": text, "norm": norm})
            if not candidates:
                groups.append({"year": year, "range": f"{start}-{start+2}", "status": "no_text_candidate"})
                continue
            for c in candidates:
                c["total_similarity"] = sum(
                    difflib.SequenceMatcher(None, c["norm"], d["norm"], autojunk=False).ratio()
                    for d in candidates if d is not c
                )
            medoid = max(candidates, key=lambda c: (c["total_similarity"], len(c["norm"])))
            pairwise = []
            for i, a in enumerate(candidates):
                for b in candidates[i + 1:]:
                    pairwise.append({
                        "questions": [a["question"], b["question"]],
                        "similarity": difflib.SequenceMatcher(None, a["norm"], b["norm"], autojunk=False).ratio(),
                        "differences": diff_ops(a["norm"], b["norm"]),
                    })
            group = {
                "year": year, "range": f"{start}-{start+2}", "status": "secondary_candidates_only",
                "candidate_questions": [c["question"] for c in candidates],
                "medoid_question": medoid["question"], "medoid_chars": len(medoid["norm"]),
                "pairwise": pairwise,
            }
            if official:
                alignment = fuzz.partial_ratio_alignment(medoid["norm"], official, score_cutoff=50)
                if alignment:
                    official_span = official[alignment.dest_start:alignment.dest_end]
                    group["official_calibration"] = {
                        "score": alignment.score, "official_start": alignment.dest_start,
                        "official_end": alignment.dest_end,
                        "differences": diff_ops(medoid["norm"], official_span),
                    }
            groups.append(group)

    payload = {
        "status": "secondary_discrepancy_locator_only", "groups": groups,
        "warning": "Repeated-transcription consensus is not official verification and may preserve a typo shared by all copies.",
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# QZip 반복 지문 불일치 분석 v1\n\n",
        "> 외부 2차 전사본의 오타 후보를 찾기 위한 자료다. 세 전사본이 일치해도 공식 원문 검증으로 간주하지 않는다.\n\n",
        "| 연도 | 문항군 | 후보 수 | 기준 후보 | 후보 간 불일치 | 2024 공식본 대조 점수 |\n",
        "| --- | --- | ---: | ---: | ---: | ---: |\n",
    ]
    for g in groups:
        if g["status"] == "no_text_candidate":
            lines.append(f"| {g['year']} | {g['range']} | 0 | - | - | - |\n")
            continue
        diff_count = sum(len(p["differences"]) for p in g["pairwise"])
        score = g.get("official_calibration", {}).get("score")
        score_text = f"{score:.3f}" if score is not None else "-"
        lines.append(f"| {g['year']} | {g['range']} | {len(g['candidate_questions'])} | {g['medoid_question']} | {diff_count} | {score_text} |\n")
    lines.extend(["\n## 상세 불일치\n\n"])
    for g in groups:
        if g.get("status") == "no_text_candidate":
            continue
        details = [(p["questions"], d) for p in g["pairwise"] for d in p["differences"]]
        if not details:
            continue
        lines.append(f"### {g['year']} {g['range']}\n\n")
        for questions, d in details:
            lines.append(f"- q{questions[0]:02d}↔q{questions[1]:02d} `{d['a_context']}` / `{d['b_context']}`\n")
        lines.append("\n")
    OUT_MD.write_text("".join(lines), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    print("groups", len(groups), "candidate groups", sum(g.get("status") != "no_text_candidate" for g in groups))


if __name__ == "__main__":
    main()
