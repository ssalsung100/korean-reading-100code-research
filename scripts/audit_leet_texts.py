#!/usr/bin/env python3
"""Audit LEET derived Markdown without inventing missing source text."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

import fitz

ROOT = Path("자료/LEET_언어이해")
REPORT_DIR = ROOT / "검증"
JSON_OUT = REPORT_DIR / "텍스트_전수검증_v1.json"
MD_OUT = REPORT_DIR / "텍스트_전수검증_v1.md"


def clean_text(s: str) -> str:
    s = s.replace("\r\n", "\n").replace("\r", "\n").replace("\u00a0", " ")
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{4,}", "\n\n\n", s)
    return s.strip()


def md_body(text: str) -> str:
    text = re.sub(r"^# [^\n]+\n+", "", text, count=1)
    text = re.sub(r"^\[공식 PDF에 텍스트 레이어가 없음\.[^\n]+\]\n+", "", text, count=1)
    return text.rstrip("\n")


def source_comparable_body(text: str) -> str:
    """Remove provenance-marked visual links that are not PDF text."""
    body = md_body(text)
    # Visual links were inserted as their own Markdown paragraphs.  Remove the
    # complete paragraph, including its leading separator, so that the result
    # is byte-for-byte comparable with the original PDF text extraction.
    body = re.sub(r"\n+!\[[^\n]*\]\([^\n]+\)\n+", "\n", body)
    body = re.sub(r"(?m)^!\[[^\n]*\]\([^\n]+\)\n?", "", body)
    return body.rstrip("\n")


def direct_source_text(path: Path, kind: str) -> str | None:
    if path.suffix.lower() == ".hwp":
        if kind == "answer":
            return None  # answer tables are checked against normalized keys
        out = subprocess.run(["hwp5txt", str(path)], check=True, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout
        return clean_text(out)
    if path.suffix.lower() == ".pdf":
        doc = fitz.open(path)
        chunks = [f"<!-- page {i} -->\n\n{page.get_text('text').strip()}"
                  for i, page in enumerate(doc, 1)]
        return clean_text("\n\n".join(chunks))
    return None


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main() -> None:
    extracted = json.loads((ROOT / "extracted_assets_manifest.json").read_text(encoding="utf-8"))
    answers = json.loads((ROOT / "normalized_answers.json").read_text(encoding="utf-8"))["records"]
    answer_by_label = {}
    for a in answers:
        answer_by_label.setdefault(a["label"], []).append(a)

    records = []
    for item in extracted["records"]:
        src = Path(item["source_file"])
        target = Path(item["text_file"])
        text = target.read_text(encoding="utf-8")
        body = md_body(text)
        comparable_body = source_comparable_body(text)
        rerun = direct_source_text(src, item["kind"])
        flags = []
        if "\ufffd" in text:
            flags.append("replacement_character")
        if "추출 실패" in text:
            flags.append("extract_failure_marker")
        source_has_text = bool(rerun and re.search(r"[가-힣A-Za-z0-9]", re.sub(r"<!--.*?-->", "", rerun, flags=re.S)))
        reproducible = rerun is not None and comparable_body == rerun

        if item["kind"] == "answer":
            ars = answer_by_label.get(item["label"], [])
            parsed = [a for a in ars if a["status"] in {"parsed", "verified_visual"}]
            status = "answer_key_parsed" if parsed else "answer_image_only"
            expected = sum(a["question_count"] for a in parsed)
        elif not source_has_text:
            status = "image_only_no_canonical_text"
            expected = 0
        elif reproducible and src.suffix.lower() == ".pdf":
            status = (
                "pass_direct_pdf_text_with_visual_links"
                if comparable_body != body else "pass_direct_pdf_text"
            )
            expected = 0
        elif reproducible and src.suffix.lower() == ".hwp":
            status = "pass_direct_hwp_text_layout_pending"
            expected = 0
        else:
            status = "fail_nonreproducible"
            expected = 0
            flags.append("source_rerun_mismatch")

        qnums = [int(x) for x in re.findall(r"(?m)^\s*(\d{1,2})[.]", body)]
        choice_counts = {c: body.count(c) for c in "①②③④⑤"}
        records.append({
            "label": item["label"], "kind": item["kind"], "source_file": str(src),
            "text_file": str(target), "status": status, "flags": flags,
            "source_text_reproducible": reproducible, "body_chars": len(body),
            "body_sha256": sha256_text(body), "numbered_question_lines": len(qnums),
            "first_question_numbers": qnums[:10], "figure_count": item["figure_count"],
            "choice_counts": choice_counts, "choice_total": sum(choice_counts.values()),
            "table_count": item.get("table_count", 0), "page_render_count": item["page_render_count"],
            "parsed_answer_cells": expected,
        })

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {"record_count": len(records), "status_counts": dict(Counter(r["status"] for r in records)),
               "records": records}
    JSON_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# LEET 언어이해 텍스트 전수 검증 v1\n\n",
        "## 판정 원칙\n\n",
        "- 원본에 없는 문장을 추정하여 정본 Markdown에 넣지 않는다.\n",
        "- `pass_direct_*`는 같은 원본에서 추출기를 다시 실행한 결과와 Markdown 본문이 문자 단위로 일치한다는 뜻이다.\n",
        "- `layout_pending`은 본문 문자는 직접 추출되었지만 HWP의 자동 문항 번호·표·그림 배치를 별도로 대조해야 한다는 뜻이다.\n",
        "- `image_only_no_canonical_text`는 페이지 이미지만 정본이며 OCR 문장은 아직 정본이 아니라는 뜻이다.\n",
        "- 정답표는 `normalized_answers.json`과 원본 정답표를 기준으로 관리한다.\n\n",
        "## 요약\n\n",
    ]
    for status, count in sorted(payload["status_counts"].items()):
        lines.append(f"- `{status}`: {count}개\n")
    lines.extend(["\n## 파일별 판정\n\n",
                  "| 학년도 | 종류 | 판정 | 본문 문자 | 문항 번호행 | 선지 표지 | 그림 | 표 | 페이지 렌더 |\n",
                  "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |\n"])
    for r in records:
        lines.append(f"| {r['label']} | {r['kind']} | `{r['status']}` | {r['body_chars']} | "
                     f"{r['numbered_question_lines']} | {r['choice_total']} | {r['figure_count']} | {r['table_count']} | {r['page_render_count']} |\n")
    lines.extend([
        "\n## 현재 사용 금지 범위\n\n",
        "- 이미지형 PDF의 빈 Markdown을 본문 데이터로 사용하지 않는다.\n",
        "- OCR 초안은 원문 페이지 대조 전에는 지문·문항 분석 데이터에 합치지 않는다.\n",
        "- HWP의 `<표>`와 `<그림>` 위치는 별도 자산과 매핑되기 전까지 해당 문항의 완전한 본문으로 간주하지 않는다.\n",
    ])
    MD_OUT.write_text("".join(lines), encoding="utf-8")
    print(JSON_OUT)
    print(MD_OUT)
    print(payload["status_counts"])


if __name__ == "__main__":
    main()
