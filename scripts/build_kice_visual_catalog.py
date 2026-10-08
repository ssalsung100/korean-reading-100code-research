#!/usr/bin/env python3
"""Extract and link the KICE-compilation HWPX visual assets to question IDs.

The seven HWPX files are local compilation sources, not asserted to be the
original KICE containers.  Every link therefore records both the compilation
file and the normalized KICE question identifier.
"""

from __future__ import annotations

import hashlib
import io
import json
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

from lxml import etree
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "고3 기출"
OUT_ROOT = ROOT / "자료/평가원_독서_시각자료_원본"
MANIFEST_JSON = OUT_ROOT / "manifest.json"
CATALOG_MD = OUT_ROOT / "평가원_시각자료_문항별_목록_v1.md"
CONTACT_ROOT = OUT_ROOT / "접촉판"
QUESTIONS_JSONL = ROOT / "data/kice_questions.jsonl"

# Visual inspection overrides.  These labels describe the representation
# actually present in each extracted binary, rather than guessing from nearby
# words alone.  Keys use a stable substring of the source filename.
KIND_OVERRIDES = {
    "인문_독서": {
        1: "annotated_text_excerpt", 2: "annotation_mark", 3: "annotation_mark",
        4: "annotation_mark", 5: "annotation_mark", 6: "annotation_mark",
        7: "cycle_diagram", 8: "response_template", 9: "line_graph",
        10: "photograph", 11: "response_template",
    },
    "사회": {1: "multi_line_graph", 2: "comment_thread_diagram", 3: "supply_cost_graph"},
    "과학": {
        1: "text_excerpt", 2: "annotation_mark", 3: "line_graph",
        4: "pendulum_diagram", 5: "layered_strip_diagram", 6: "experiment_apparatus_diagram",
        7: "motion_sequence_diagram", 8: "experiment_apparatus_diagram",
        9: "distribution_graph", 10: "scatter_plot", 11: "multi_curve_graph",
        12: "scatter_regression_graph", 13: "text_and_illustration", 14: "path_diagram",
        15: "direction_annotation", 16: "direction_annotation", 17: "spatial_layout_diagram",
        18: "line_graph_choice", 19: "line_graph_choice", 20: "line_graph_choice",
        21: "line_graph_choice", 22: "line_graph_choice",
    },
    "기술": {
        1: "image_sequence", 2: "worksheet_table", 3: "process_diagram",
        4: "flowchart", 5: "flowchart", 6: "image_mapping_diagram",
        7: "mechanism_diagram", 8: "data_table", 9: "semiconductor_diagram",
        10: "mechanical_diagram", 11: "algorithm_trace_graph", 12: "algorithm_trace_graph",
        13: "apparatus_diagram", 14: "projection_geometry_diagram", 15: "projection_annotation",
        16: "graph_choice", 17: "graph_choice", 18: "graph_choice", 19: "graph_choice",
        20: "graph_choice", 21: "geometric_projection_diagram", 22: "sensor_diagram",
        23: "system_block_diagram", 24: "document_excerpt", 25: "response_curve_graph",
        26: "image_comparison", 27: "image_comparison", 28: "trilateration_diagram",
        29: "deformation_diagram", 30: "process_sequence_diagram", 31: "fabrication_sequence_diagram",
        32: "illustrated_choice", 33: "illustrated_choice", 34: "illustrated_choice",
        35: "illustrated_choice", 36: "illustrated_choice",
    },
    "예술": {
        1: "artwork_comparison", 2: "comic_sequence", 3: "architectural_plan",
        4: "response_template", 5: "artwork", 6: "architectural_illustration",
        7: "musical_score",
    },
    "복합_지문": {1: "musical_score", 2: "geometry_diagram", 3: "frequency_bar_graph"},
    "미니모의고사": {
        1: "multi_curve_graph", 2: "anatomical_diagram", 3: "experiment_apparatus_diagram",
        4: "relation_diagram", 5: "illustrated_sequence", 6: "orbital_diagram",
        7: "line_graph",
    },
}


def inspected_kind(source_name: str, binary_ref: str, fallback: str) -> tuple[str, str]:
    number = int(re.search(r"\d+", binary_ref).group())
    for source_key, values in KIND_OVERRIDES.items():
        if source_key in source_name and number in values:
            return values[number], "visual_inspection_override"
    return fallback, "context_heuristic"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_slug(name: str) -> str:
    return re.sub(r"[^0-9A-Za-z가-힣._-]+", "_", name).strip("_")


def paragraph_text(node) -> str:
    return "".join(node.xpath('.//*[local-name()="t"]/text()')).strip()


SECTION_RE = re.compile(r"[\[［](\d{3})[~～](\d{3})[\]］]")


def nearest_question_context(pic, paragraphs: list, para_index: dict[int, int]) -> tuple[str | None, str | None, str, str]:
    ancestor = pic.xpath('ancestor::*[local-name()="p"][1]')
    if not ancestor:
        return None, None, "", ""
    current = ancestor[0]
    index = para_index[id(current)]
    dataset_id = None
    dataset_section_id = None
    context_parts = []
    for para in reversed(paragraphs[: index + 1]):
        text = paragraph_text(para)
        if text:
            context_parts.append(text)
        if dataset_id is None and re.fullmatch(r"\d{3}", text):
            dataset_id = text
        section_match = SECTION_RE.search(text)
        if section_match:
            dataset_section_id = f"{section_match.group(1)}~{section_match.group(2)}"
            break
        # Do not accidentally walk into a preceding group if a malformed
        # heading is encountered; ordinary contexts are much shorter.
        if len(context_parts) >= 80:
            break
    context = "\n".join(reversed(context_parts))
    return dataset_id, dataset_section_id, paragraph_text(current), context


def role_from_context(current: str, context: str, same_question_count: int) -> str:
    compact = re.sub(r"\s+", "", context)
    if "①②③④⑤" in compact or same_question_count == 5:
        return "choice_visual"
    if "<보기>" in compact or "<보기" in compact or "<보기>" in current.replace(" ", ""):
        return "view_visual"
    if "<그림>" in compact or "그림" in current:
        return "passage_figure"
    return "question_or_passage_visual"


def kind_from_context(current: str, context: str, role: str, width: int, height: int) -> str:
    compact = re.sub(r"\s+", "", context)
    if role == "choice_visual":
        return "illustrated_choice"
    if "그래프" in compact or "가로축" in compact or "세로축" in compact:
        return "graph_or_chart"
    if "평면도" in compact or "도식" in compact or "과정" in compact or "화살표" in compact:
        return "diagram"
    if any(word in compact for word in ("사진", "작품", "피카소", "화가", "조각", "성당", "정자")):
        return "photograph_or_artwork"
    if any(word in compact for word in ("지도", "상자", "센서", "장치", "촬영", "경로", "회로", "셀")):
        return "technical_diagram"
    if width / max(height, 1) > 3.5:
        return "strip_or_annotation"
    if width > 1800 and height > 1000:
        return "document_or_composite"
    return "illustration_or_diagram"


def lexical_tokens(text: str) -> set[str]:
    return {
        token.lower()
        for token in re.findall(r"[가-힣A-Za-z0-9]{2,}", text)
        if token not in {"보기", "윗글", "적절한", "적절하지", "다음", "내용", "것은"}
    }


def choose_question_links(
    source_name: str,
    dataset_ids: list[str],
    dataset_section_ids: list[str],
    context: str,
    by_source_and_dataset_id: dict[tuple[str, str], list[dict]],
    questions_by_source: dict[str, list[dict]],
    passage_by_id: dict[str, dict],
    passage_by_source_and_section: dict[tuple[str, str], dict],
) -> tuple[list[dict], str, float]:
    section_passages = [
        passage_by_source_and_section[(source_name, section_id)]
        for section_id in dataset_section_ids
        if (source_name, section_id) in passage_by_source_and_section
    ]
    candidates = []
    for dataset_id in dataset_ids:
        candidates.extend(by_source_and_dataset_id.get((source_name, dataset_id), []))
    if section_passages:
        allowed_passages = {row["passage_id"] for row in section_passages}
        candidates = [row for row in candidates if row["passage_id"] in allowed_passages]
    method = "hwpx_dataset_id"
    if not candidates and len(section_passages) == 1:
        selected = [
            row for row in questions_by_source[source_name]
            if row["passage_id"] == section_passages[0]["passage_id"]
        ]
        return selected, "hwpx_section_range_common_passage", 1.0
    if len(candidates) != 1:
        candidates = questions_by_source.get(source_name, []) if not candidates else candidates
        method = "hwpx_context_similarity"
    if not candidates:
        return [], "unlinked", 0.0
    if len(candidates) == 1:
        return candidates, method, 1.0
    context_tokens = lexical_tokens(context)
    scored = []
    for question in candidates:
        passage = passage_by_id[question["passage_id"]]
        candidate_text = question["stem"] + "\n" + passage["passage_text"]
        candidate_tokens = lexical_tokens(candidate_text)
        overlap = context_tokens & candidate_tokens
        score = sum(len(token) for token in overlap) / max(sum(len(token) for token in context_tokens), 1)
        scored.append((score, question))
    scored.sort(key=lambda item: (item[0], item[1]["question_id"]), reverse=True)
    best_score = scored[0][0]
    # A visual may sit in the common passage rather than in a single question.
    # Preserve all tied questions from that same passage, but do not mix passages.
    best_passage = scored[0][1]["passage_id"]
    selected = [
        question for score, question in scored
        if question["passage_id"] == best_passage and score >= best_score - 1e-12
    ]
    return selected, method, round(best_score, 6)


def make_contact_sheet(rows: list[dict], output: Path) -> None:
    thumbs = []
    for row in rows:
        image_path = ROOT / row["preview_file"]
        image = Image.open(image_path).convert("RGB")
        image.thumbnail((350, 260))
        thumbs.append((row, image.copy()))
    if not thumbs:
        return
    cols = 3
    cell_w, cell_h = 390, 330
    sheet = Image.new("RGB", (cols * cell_w, ((len(thumbs) + cols - 1) // cols) * cell_h), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for index, (row, image) in enumerate(thumbs):
        x = (index % cols) * cell_w + 12
        y = (index // cols) * cell_h + 8
        label = f"{row['asset_id']}  Q={','.join(row['dataset_question_ids']) or '?'}\n{row['role']} / {row['kind']}"
        draw.multiline_text((x, y), label, fill="black", font=font, spacing=2)
        sheet.paste(image, (x, y + 40))
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def table_classification(table, text: str, context: str) -> tuple[str, str, bool, int]:
    def int_attr(name: str) -> int:
        value = table.get(name)
        return int(value) if value and value.isdigit() else 0
    rows = int_attr("rowCnt")
    cols = int_attr("colCnt")
    cell_texts = [paragraph_text(cell) for cell in table.xpath('.//*[local-name()="tc"]')]
    nonempty_cells = sum(bool(value.strip()) for value in cell_texts)
    compact = re.sub(r"\s+", "", text)
    circled = sum(symbol in compact for symbol in "①②③④⑤")
    surrounding = re.sub(r"\s+", "", context)
    if rows >= 2 and cols >= 2 and nonempty_cells >= 4 and circled >= 3:
        return "choice_matrix", "question_table", True, nonempty_cells
    if rows >= 2 and cols >= 2 and nonempty_cells >= 4:
        return "data_or_relation_table", "view_or_question_table", True, nonempty_cells
    if "<보기>" in surrounding or "<보기>" in compact:
        return "view_box_layout", "layout_container", False, nonempty_cells
    if circled >= 3:
        return "choice_layout_table", "layout_container", False, nonempty_cells
    return "text_layout_table", "layout_container", False, nonempty_cells


def main() -> None:
    question_rows = [json.loads(line) for line in QUESTIONS_JSONL.read_text(encoding="utf-8").splitlines() if line]
    passage_rows = [json.loads(line) for line in (ROOT / "data/kice_passages.jsonl").read_text(encoding="utf-8").splitlines() if line]
    passage_by_id = {row["passage_id"]: row for row in passage_rows}
    passage_by_source_and_section = {
        (row["source_hwpx"], row["dataset_section_id"]): row
        for row in passage_rows
    }
    by_source_and_dataset_id: dict[tuple[str, str], list[dict]] = defaultdict(list)
    questions_by_source: dict[str, list[dict]] = defaultdict(list)
    for row in question_rows:
        source_hwpx = passage_by_id[row["passage_id"]]["source_hwpx"]
        by_source_and_dataset_id[(source_hwpx, row["dataset_question_id"])].append(row)
        questions_by_source[source_hwpx].append(row)

    extracted: list[dict] = []
    for source in sorted(SOURCE_DIR.glob("*.hwpx")):
        source_slug = safe_slug(source.stem)
        with zipfile.ZipFile(source) as archive:
            xml = archive.read("Contents/section0.xml")
            root = etree.fromstring(xml)
            paragraphs = root.xpath('//*[local-name()="p"]')
            para_index = {id(node): index for index, node in enumerate(paragraphs)}
            raw_occurrences = []
            for pic in root.xpath('//*[local-name()="pic"]'):
                refs = pic.xpath('.//@*[local-name()="binaryItemIDRef"]')
                if not refs:
                    continue
                dataset_id, dataset_section_id, current, context = nearest_question_context(pic, paragraphs, para_index)
                raw_occurrences.append((refs[0], dataset_id, dataset_section_id, current, context, pic))
            per_question_counts = Counter(dataset_id for _, dataset_id, _, _, _, _ in raw_occurrences if dataset_id)
            grouped: dict[str, list] = defaultdict(list)
            for occurrence in raw_occurrences:
                grouped[occurrence[0]].append(occurrence)

            for binary_ref, occurrences in grouped.items():
                member = next((name for name in archive.namelist() if Path(name).stem == binary_ref and name.startswith("BinData/")), None)
                if member is None:
                    raise RuntimeError(f"missing BinData member {binary_ref} in {source}")
                data = archive.read(member)
                image = Image.open(io.BytesIO(data))
                width, height = image.size
                suffix = Path(member).suffix.lower()
                source_out = OUT_ROOT / source_slug
                source_out.mkdir(parents=True, exist_ok=True)
                original_path = source_out / f"{binary_ref}{suffix}"
                original_path.write_bytes(data)
                preview_path = source_out / f"{binary_ref}.png"
                if suffix == ".png":
                    preview_path.write_bytes(data)
                else:
                    image.convert("RGB").save(preview_path)

                dataset_ids = sorted({item[1] for item in occurrences if item[1]})
                dataset_section_ids = sorted({item[2] for item in occurrences if item[2]})
                current = "\n".join(item[3] for item in occurrences if item[3])
                context = max((item[4] for item in occurrences), key=len, default="")
                selected_questions, link_method, link_score = choose_question_links(
                    source.name,
                    dataset_ids,
                    dataset_section_ids,
                    current + "\n" + context,
                    by_source_and_dataset_id,
                    questions_by_source,
                    passage_by_id,
                    passage_by_source_and_section,
                )
                linked_questions = []
                for question in selected_questions:
                    linked_questions.append({
                            "question_id": question["question_id"],
                            "passage_id": question["passage_id"],
                            "dataset_question_id": question["dataset_question_id"],
                            "academic_year": question["academic_year"],
                            "exam_label": question["exam_label"],
                            "question_number": question["question_number"],
                        })
                max_same_count = max((per_question_counts[item[1]] for item in occurrences if item[1]), default=0)
                role = role_from_context(current, context, max_same_count)
                inferred_kind = kind_from_context(current, context, role, width, height)
                kind, classification_method = inspected_kind(source.name, binary_ref, inferred_kind)
                extracted.append({
                    "asset_id": f"KICE-HWPX-{source_slug}-{binary_ref}",
                    "source_hwpx": source.relative_to(ROOT).as_posix(),
                    "source_hwpx_sha256": sha256(source.read_bytes()),
                    "binary_item": member,
                    "binary_ref": binary_ref,
                    "original_file": original_path.relative_to(ROOT).as_posix(),
                    "preview_file": preview_path.relative_to(ROOT).as_posix(),
                    "sha256": sha256(data),
                    "width": width,
                    "height": height,
                    "dataset_question_ids": dataset_ids,
                    "dataset_section_ids": dataset_section_ids,
                    "linked_questions": linked_questions,
                    "role": role,
                    "kind": kind,
                    "classification_method": classification_method,
                    "context_excerpt": context[:1000],
                    "link_method": link_method,
                    "link_score": link_score,
                    "link_status": "linked" if linked_questions else "unlinked",
                    "provenance_status": "extracted_from_local_kice_compilation_hwpx",
                })

            for table_index, table in enumerate(root.xpath('//*[local-name()="tbl"]'), 1):
                dataset_id, dataset_section_id, current, context = nearest_question_context(table, paragraphs, para_index)
                dataset_ids = [dataset_id] if dataset_id else []
                dataset_section_ids = [dataset_section_id] if dataset_section_id else []
                selected_questions, link_method, link_score = choose_question_links(
                    source.name,
                    dataset_ids,
                    dataset_section_ids,
                    current + "\n" + context,
                    by_source_and_dataset_id,
                    questions_by_source,
                    passage_by_id,
                    passage_by_source_and_section,
                )
                linked_questions = [{
                    "question_id": question["question_id"],
                    "passage_id": question["passage_id"],
                    "dataset_question_id": question["dataset_question_id"],
                    "academic_year": question["academic_year"],
                    "exam_label": question["exam_label"],
                    "question_number": question["question_number"],
                } for question in selected_questions]
                table_text = paragraph_text(table)
                representation, role, semantic, nonempty_cells = table_classification(table, table_text, context)
                table_xml = etree.tostring(table, encoding="utf-8", with_tail=False)
                extracted.append({
                    "asset_id": f"KICE-HWPX-{source_slug}-table{table_index:03d}",
                    "source_hwpx": source.relative_to(ROOT).as_posix(),
                    "source_hwpx_sha256": sha256(source.read_bytes()),
                    "object_type": "hwpx_table",
                    "table_index": table_index,
                    "table_rows": int(table.get("rowCnt") or 0),
                    "table_columns": int(table.get("colCnt") or 0),
                    "nonempty_cells": nonempty_cells,
                    "object_xml_sha256": sha256(table_xml),
                    "dataset_question_ids": dataset_ids,
                    "dataset_section_ids": dataset_section_ids,
                    "linked_questions": linked_questions,
                    "role": role,
                    "kind": representation,
                    "semantic_visual": semantic,
                    "classification_method": "hwpx_table_structure_and_text",
                    "content_excerpt": table_text[:1200],
                    "context_excerpt": context[:1000],
                    "link_method": link_method,
                    "link_score": link_score,
                    "link_status": "linked" if linked_questions else "unlinked",
                    "provenance_status": "indexed_from_local_kice_compilation_hwpx_xml",
                })

    extracted.sort(key=lambda row: (row["source_hwpx"], row.get("object_type", "image"), row.get("table_index", int(re.search(r"\d+", row.get("binary_ref", "0")).group()))))
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    payload = {
        "status": "complete_with_explicit_unlinked_flags",
        "scope": "seven local KICE reading compilation HWPX files",
        "provenance_warning": "HWPX는 평가원 원본 배포 컨테이너가 아니라 로컬 기출 편집본이다. 시험·문항 식별은 정규화 DB와 연결했다.",
        "record_count": len(extracted),
        "image_record_count": sum("binary_item" in row for row in extracted),
        "table_record_count": sum(row.get("object_type") == "hwpx_table" for row in extracted),
        "semantic_visual_count": sum(row.get("semantic_visual", True) for row in extracted),
        "records": extracted,
    }
    MANIFEST_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    by_source: dict[str, list[dict]] = defaultdict(list)
    for row in extracted:
        by_source[row["source_hwpx"]].append(row)
    for source_name, rows in by_source.items():
        make_contact_sheet([row for row in rows if "preview_file" in row], CONTACT_ROOT / f"{safe_slug(Path(source_name).stem)}_접촉판.png")

    role_counts = Counter(row["role"] for row in extracted)
    kind_counts = Counter(row["kind"] for row in extracted)
    lines = [
        "# 평가원 독서 시각 자료 문항별 목록 v1",
        "",
        f"- 전체 시각/레이아웃 객체: **{len(extracted)}개**",
        f"- 원본 이미지: **{sum('binary_item' in row for row in extracted)}개**",
        f"- HWPX 표 객체: **{sum(row.get('object_type') == 'hwpx_table' for row in extracted)}개**",
        f"- 의미 시각 자료: **{sum(row.get('semantic_visual', True) for row in extracted)}개**",
        f"- 문항 연결 완료: **{sum(bool(row['linked_questions']) for row in extracted)}개**",
        f"- 연결 보류: **{sum(not row['linked_questions'] for row in extracted)}개**",
        "- 출처 주의: 아래 HWPX는 로컬 기출 편집본이다. 평가원 원본 파일 자체라고 단정하지 않는다.",
        "",
        "## 역할 분류",
        "",
    ]
    lines.extend(f"- {key}: {value}개" for key, value in sorted(role_counts.items()))
    lines.extend(["", "## 표현 형식 분류", ""])
    lines.extend(f"- {key}: {value}개" for key, value in sorted(kind_counts.items()))
    lines.extend(["", "## 문항별 연결", "", "| 자료 ID | 정규화 문항 | 역할 | 형식 | 원본 |", "|---|---|---|---|---|"])
    for row in extracted:
        questions = ", ".join(link["question_id"] for link in row["linked_questions"]) or "연결 보류"
        if "original_file" in row:
            source_cell = f"[{Path(row['original_file']).name}](../{Path(row['original_file']).relative_to('자료/평가원_독서_시각자료_원본').as_posix()})"
        else:
            source_cell = f"`{Path(row['source_hwpx']).name}#table{row['table_index']:03d}`"
        lines.append(f"| {row['asset_id']} | {questions} | {row['role']} | {row['kind']} | {source_cell} |")
    CATALOG_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({
        "records": len(extracted),
        "images": sum("binary_item" in row for row in extracted),
        "tables": sum(row.get("object_type") == "hwpx_table" for row in extracted),
        "linked": sum(bool(row["linked_questions"]) for row in extracted),
        "roles": role_counts,
        "kinds": kind_counts,
    }, ensure_ascii=False, default=dict, indent=2))


if __name__ == "__main__":
    main()
