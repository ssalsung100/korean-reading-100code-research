#!/usr/bin/env python3
"""Map figures and semantic tables in legacy LEET HWP odd-form papers.

The HWP body stream and embedded binaries are authoritative.  HTML produced
by hwp5html is used only to recover object order and anchors; it is never
treated as a page-faithful rendering.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
from collections import deque
from pathlib import Path

from bs4 import BeautifulSoup, Tag
from PIL import Image


ROOT = Path("자료/LEET_언어이해")
SOURCE_MANIFEST = ROOT / "extracted_assets_manifest.json"
OUT_JSON = ROOT / "검증" / "HWP_홀수형_시각자료_문항매핑_v1.json"
OUT_MD = ROOT / "검증" / "HWP_홀수형_시각자료_문항매핑_v1.md"
GROUP_RE = re.compile(r"[\[［]\s*(\d{1,2})\s*[~～〜-]\s*(\d{1,2})\s*[\]］]")

# Before the first passage group, early LEET papers contain independent
# language-use questions.  HWP stores their numbers as auto-numbering fields,
# which hwp5html omits.  These anchors were recovered from the canonical text
# and the immediately surrounding question prompt.
PREPASS_TABLE_QUESTION = {
    "2009": {7: 1, 8: 2, 9: 3, 10: 4},
    "2009예비": {4: 2, 5: 3, 6: 4},
    "2010": {7: 1, 8: 2, 9: 3},
    "2012": {7: 3},
    "2013": {7: 1, 8: 1, 9: 2},
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def text_of(tag: Tag) -> str:
    return re.sub(r"\s+", " ", " ".join(tag.stripped_strings)).strip()


def direct_rows(table: Tag) -> list[list[str]]:
    rows: list[list[str]] = []
    for tr in table.find_all("tr"):
        if tr.find_parent("table") is not table:
            continue
        cells = [text_of(cell) for cell in tr.find_all(["td", "th"], recursive=False)]
        if cells:
            rows.append(cells)
    return rows


def classify_table(table: Tag) -> tuple[str, list[list[str]]]:
    rows = direct_rows(table)
    flat = " ".join(cell for row in rows for cell in row if cell)
    meaningful_rows = [row for row in rows if sum(bool(cell) for cell in row) >= 2]

    layout_terms = ("수험번호", "필적확인란", "확인 사항", "법학적성시험")
    if any(term in flat for term in layout_terms):
        return "layout", rows
    if len(flat) <= 12 and re.fullmatch(r"[\d\s홀짝수형언어이해]*", flat):
        return "layout", rows
    if "<보 기>" in flat or "<보기>" in flat:
        if len(meaningful_rows) < 2:
            return "view_box", rows
    if len(set(re.findall(r"[①②③④⑤]", flat))) >= 4:
        return "choice_table", rows
    if len(meaningful_rows) >= 2:
        return "data_table", rows
    return "layout", rows


def nearest_next_text(tag: Tag, limit: int = 180) -> str:
    for nxt in tag.find_all_next("p"):
        value = text_of(nxt)
        if value:
            return value[:limit]
    return ""


def image_metadata(path: Path) -> dict:
    with Image.open(path) as image:
        return {
            "format": image.format,
            "width": image.width,
            "height": image.height,
            "mode": image.mode,
        }


def main() -> None:
    source = json.loads(SOURCE_MANIFEST.read_text(encoding="utf-8"))
    records = [
        record
        for record in source["records"]
        if record["kind"] == "question_odd"
        and record["method"] == "hwp5txt_direct"
        and int(record["year"]) <= 2021
    ]
    records.sort(key=lambda record: (int(record["year"]), record["label"]))

    papers: list[dict] = []
    all_assets: list[dict] = []
    errors: list[str] = []

    for record in records:
        hwp = Path(record["source_file"])
        figure_by_source = {item["source"]: item for item in record["figures"]}
        table_by_number = {index: item for index, item in enumerate(record["tables"], 1)}

        with tempfile.TemporaryDirectory(prefix="leet-hwp-map-") as temp_dir:
            html_dir = Path(temp_dir) / "html"
            result = subprocess.run(
                ["hwp5html", "--output", str(html_dir), str(hwp)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            if result.returncode != 0:
                errors.append(f"{record['label']}: hwp5html 실패: {result.stderr[-300:]}")
                continue
            soup = BeautifulSoup((html_dir / "index.xhtml").read_text(encoding="utf-8"), "html.parser")

            current_group: list[int] | None = None
            previous = deque(maxlen=4)
            image_number = 0
            table_numbers = {id(tag): index for index, tag in enumerate(soup.find_all("table"), 1)}
            paper_assets: list[dict] = []

            for tag in soup.find_all(["p", "img", "table"]):
                if tag.name == "p":
                    value = text_of(tag)
                    # Character runs such as ``33～3`` + ``5`` are split into
                    # separate spans in several HWP files.  Whitespace-free
                    # matching reconstructs the printed range without joining
                    # unrelated digits because the brackets bound the pattern.
                    match = GROUP_RE.search(re.sub(r"\s+", "", value))
                    if match:
                        current_group = [int(match.group(1)), int(match.group(2))]
                    if value:
                        previous.append(value[:180])
                    continue

                if tag.name == "img":
                    image_number += 1
                    src = tag.get("src", "")
                    manifest_figure = figure_by_source.get(src)
                    if manifest_figure is None:
                        errors.append(f"{record['label']}: HTML 그림을 manifest에서 찾지 못함: {src}")
                        continue
                    target = Path(manifest_figure["file"])
                    if not target.is_file() or sha256(target) != manifest_figure["sha256"]:
                        errors.append(f"{record['label']}: 그림 파일 또는 해시 오류: {target}")
                        continue
                    context = " / ".join(previous)
                    confidence = "high" if current_group else "review_required"
                    asset = {
                        "year": int(record["year"]),
                        "label": record["label"],
                        "kind": "embedded_figure",
                        "asset_number": image_number,
                        "file": str(target),
                        "sha256": manifest_figure["sha256"],
                        "hwp_source": src,
                        "question_group": current_group,
                        "mapping_confidence": confidence,
                        "preceding_context": context[-500:],
                        "following_context": nearest_next_text(tag),
                        **image_metadata(target),
                    }
                    paper_assets.append(asset)
                    all_assets.append(asset)
                    continue

                table_number = table_numbers[id(tag)]
                table_class, rows = classify_table(tag)
                if table_class not in {"data_table", "choice_table", "view_box"}:
                    continue
                manifest_table = table_by_number.get(table_number)
                if manifest_table is None:
                    errors.append(f"{record['label']}: 표 번호를 manifest에서 찾지 못함: {table_number}")
                    continue
                target = Path(manifest_table["file"])
                if not target.is_file():
                    errors.append(f"{record['label']}: 표 파일 없음: {target}")
                    continue
                flat = " ".join(cell for row in rows for cell in row if cell)
                mapped_group = current_group
                mapping_basis = "explicit_passage_range"
                if mapped_group is None:
                    question = PREPASS_TABLE_QUESTION.get(record["label"], {}).get(table_number)
                    if question is not None:
                        mapped_group = [question, question]
                        mapping_basis = "canonical_question_anchor"
                confidence = "high" if mapped_group else "review_required"
                asset = {
                    "year": int(record["year"]),
                    "label": record["label"],
                    "kind": table_class,
                    "asset_number": table_number,
                    "file": str(target),
                    "question_group": mapped_group,
                    "mapping_confidence": confidence,
                    "mapping_basis": mapping_basis if mapped_group else "none",
                    "row_count": len(rows),
                    "column_count_max": max((len(row) for row in rows), default=0),
                    "content_preview": flat[:350],
                    "preceding_context": " / ".join(previous)[-500:],
                }
                paper_assets.append(asset)
                all_assets.append(asset)

            papers.append({
                "year": int(record["year"]),
                "label": record["label"],
                "source_file": record["source_file"],
                "source_sha256": record["source_sha256"],
                "embedded_figure_count": sum(a["kind"] == "embedded_figure" for a in paper_assets),
                "data_table_count": sum(a["kind"] == "data_table" for a in paper_assets),
                "choice_table_count": sum(a["kind"] == "choice_table" for a in paper_assets),
                "view_box_count": sum(a["kind"] == "view_box" for a in paper_assets),
                "review_required_count": sum(a["mapping_confidence"] == "review_required" for a in paper_assets),
                "assets": paper_assets,
            })

    payload = {
        "status": "stream_order_mapped_page_layout_not_asserted",
        "scope": "2009예비~2021 LEET 언어이해 홀수형 HWP",
        "paper_count": len(papers),
        "asset_count": len(all_assets),
        "embedded_figure_count": sum(a["kind"] == "embedded_figure" for a in all_assets),
        "data_table_count": sum(a["kind"] == "data_table" for a in all_assets),
        "choice_table_count": sum(a["kind"] == "choice_table" for a in all_assets),
        "view_box_count": sum(a["kind"] == "view_box" for a in all_assets),
        "review_required_count": sum(a["mapping_confidence"] == "review_required" for a in all_assets),
        "method": "official HWP body/object stream via hwp5html; binary figures verified against extracted_assets_manifest.json",
        "warning": "HTML stream order does not prove original page or column position. review_required records must be checked in Hancom or an official PDF before promotion.",
        "papers": papers,
        "errors": errors,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# LEET HWP 홀수형 시각 자료·문항 매핑 v1",
        "",
        f"- 범위: {payload['scope']}",
        f"- 문제지: {payload['paper_count']}개",
        f"- 포함 그림: {payload['embedded_figure_count']}개",
        f"- 의미 표: {payload['data_table_count']}개",
        f"- 선지 표: {payload['choice_table_count']}개",
        f"- 구조화된 〈보기〉 상자: {payload['view_box_count']}개",
        f"- 원본 화면 확인 필요: {payload['review_required_count']}개",
        f"- 처리 오류: {len(errors)}개",
        "",
        "HWP 내부 본문·객체 순서로 문항군을 연결했다. 포함 그림은 HWP의 원본 바이너리와 SHA-256을 대조했다. 이 결과는 쪽·좌우 단의 원래 배치를 보증하지 않으며, 문항군을 찾지 못한 객체는 `review_required`로 남겼다.",
        "",
        "## 연도별 요약",
        "",
        "| 학년도 | 그림 | 의미 표 | 선지 표 | 〈보기〉 상자 | 확인 필요 |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for paper in papers:
        lines.append(
            f"| {paper['label']} | {paper['embedded_figure_count']} | {paper['data_table_count']} | "
            f"{paper['choice_table_count']} | {paper['view_box_count']} | {paper['review_required_count']} |"
        )

    lines.extend([
        "",
        "## 그림·의미 표 목록",
        "",
        "| 학년도 | 종류 | 번호 | 연결 문항군 | 신뢰 | 파일 | 내용·문맥 |",
        "| --- | --- | ---: | --- | --- | --- | --- |",
    ])
    for asset in all_assets:
        if asset["kind"] == "view_box":
            continue
        group = (
            f"{asset['question_group'][0]}~{asset['question_group'][1]}"
            if asset["question_group"]
            else "미확정"
        )
        relative = Path("..") / Path(asset["file"]).relative_to(ROOT)
        preview = asset.get("content_preview") or asset.get("preceding_context") or asset.get("following_context", "")
        preview = preview.replace("|", "\\|")[:180]
        lines.append(
            f"| {asset['label']} | `{asset['kind']}` | {asset['asset_number']} | {group} | "
            f"`{asset['mapping_confidence']}` | [{Path(asset['file']).name}]({relative.as_posix()}) | {preview} |"
        )

    lines.extend(["", "## 원본 화면 확인 대기열", ""])
    review_assets = [a for a in all_assets if a["mapping_confidence"] == "review_required"]
    if review_assets:
        for asset in review_assets:
            lines.append(
                f"- {asset['label']} `{asset['kind']}` #{asset['asset_number']}: "
                f"`{asset['file']}` — {asset.get('preceding_context', '')[-180:]}"
            )
    else:
        lines.append("- 없음")
    lines.extend(["", "## 처리 오류", ""])
    lines.extend(f"- {error}" for error in errors) if errors else lines.append("- 없음")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        f"papers={len(papers)} figures={payload['embedded_figure_count']} "
        f"tables={payload['data_table_count']} views={payload['view_box_count']} "
        f"review={payload['review_required_count']} errors={len(errors)}"
    )
    print(OUT_JSON)
    print(OUT_MD)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
