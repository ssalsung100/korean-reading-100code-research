#!/usr/bin/env python3
"""Parse the two-column question tables in Integrated Social Studies HWPX files."""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path
from xml.etree import ElementTree as ET


HP = "{http://www.hancom.co.kr/hwpml/2011/paragraph}"
HC = "{http://www.hancom.co.kr/hwpml/2011/core}"


@dataclass
class Question:
    id: str
    course: str
    source_group: str
    source_file: str
    block: int
    sequence: int
    number: int
    text: str
    image_ids: list[str]
    needs_image_review: bool


def cell_text(cell: ET.Element) -> str:
    chunks: list[str] = []
    for paragraph in cell.iter(f"{HP}p"):
        # Only leaf paragraphs prevent nested table text from being emitted twice.
        if any(child is not paragraph for child in paragraph.iter(f"{HP}p")):
            continue
        text = "".join(node.text or "" for node in paragraph.iter(f"{HP}t"))
        text = re.sub(r"\s+", " ", text).strip()
        if text and (not chunks or chunks[-1] != text):
            chunks.append(text)
    text = "\n".join(chunks)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def cell_images(cell: ET.Element) -> list[str]:
    return sorted(
        {
            node.get("binaryItemIDRef", "")
            for node in cell.iter(f"{HC}img")
            if node.get("binaryItemIDRef")
        }
    )


def direct_question_tables(root: ET.Element) -> list[ET.Element]:
    tables: list[ET.Element] = []
    for paragraph in root.findall(f"./{HP}p"):
        for run in paragraph.findall(f"./{HP}run"):
            for table in run.findall(f"./{HP}tbl"):
                # The publisher uses 2-, 4-, and 6-row variants depending on
                # page breaks and whether source metadata is printed beside a
                # question number.  Restricting this to 4 rows silently lost
                # complete questions.
                if table.get("colCnt") == "4" and int(table.get("rowCnt", "0")) in {2, 4, 6}:
                    tables.append(table)
    return tables


def is_multiple_choice(text: str, images: list[str]) -> bool:
    """Separate answer-keyed questions from the following essay section."""
    if text.startswith("다음 자료를 읽고 물음에 답하시오"):
        return False
    if re.search(r"[①②③④⑤]", text):
        return True
    # A small number of graph-choice questions store every choice in images.
    return bool(
        images
        and re.search(r"(?:옳|적절|해당|고른).*(?:것은|고른)", text, re.DOTALL)
    )


def parse_file(path: Path, workspace: Path) -> list[Question]:
    with zipfile.ZipFile(path) as archive:
        section_names = sorted(
            name for name in archive.namelist() if re.fullmatch(r"Contents/section\d+\.xml", name)
        )
        roots = [ET.fromstring(archive.read(name)) for name in section_names]

    course_match = re.search(r"통합사회([12])", path.name)
    course = f"통합사회{course_match.group(1)}" if course_match else "통합사회"
    group_match = re.search(r"문제편_(.+?)\.hwpx$", path.name)
    source_group = group_match.group(1) if group_match else path.stem
    rel = path.resolve().relative_to(workspace.resolve()).as_posix()
    raw_questions: list[dict] = []
    block = 1
    previous_table_max = 0

    for root in roots:
        for table in direct_question_tables(root):
            rows = table.findall(f"./{HP}tr")
            if len(rows) not in {2, 4, 6} or len(rows) % 2:
                continue
            table_items: list[tuple[int | None, ET.Element]] = []
            pending_numbers: list[str] = []
            for row in rows:
                cells = row.findall(f"./{HP}tc")
                cell_values = [cell_text(cell) for cell in cells]
                if any(value.isdigit() for value in cell_values):
                    if len(cells) >= 4:
                        pending_numbers.extend([cell_values[0], cell_values[2]])
                    else:
                        pending_numbers.append(cell_values[0] if cell_values else "")
                    continue
                if not cells:
                    continue
                raw_numbers = pending_numbers[: len(cells)]
                pending_numbers = pending_numbers[len(cells) :]
                if len(raw_numbers) < len(cells):
                    raw_numbers.extend([""] * (len(cells) - len(raw_numbers)))
                for raw_number, cell in zip(raw_numbers, cells):
                    text = cell_text(cell)
                    images = cell_images(cell)
                    if text and is_multiple_choice(text, images):
                        number = int(raw_number) if raw_number.isdigit() else None
                        table_items.append((number, cell))
            if not table_items:
                continue
            explicit = [number for number, _ in table_items if number is not None]
            if explicit:
                table_min, table_max = min(explicit), max(explicit)
                if previous_table_max and table_min < previous_table_max:
                    block += 1
                previous_table_max = table_max
            ordered_items = (
                table_items
                if any(number is None for number, _ in table_items)
                else sorted(table_items, key=lambda item: item[0])
            )
            for number, cell in ordered_items:
                text = cell_text(cell)
                images = cell_images(cell)
                if not text:
                    continue
                raw_questions.append({"block": block, "number": number, "text": text, "images": images})

    # Some shared-stimulus layouts intentionally leave a number cell blank.
    # Restore those numbers from the missing sequence inside the same block.
    by_block: dict[int, list[dict]] = {}
    for item in raw_questions:
        by_block.setdefault(item["block"], []).append(item)
    for items in by_block.values():
        used = {item["number"] for item in items if item["number"] is not None}
        maximum = max(used, default=0)
        missing = [number for number in range(1, maximum + 1) if number not in used]
        next_number = maximum + 1
        for item in items:
            if item["number"] is None:
                if missing:
                    item["number"] = missing.pop(0)
                else:
                    item["number"] = next_number
                    next_number += 1
        numbers = [item["number"] for item in items]
        if sorted(numbers) != list(range(1, len(items) + 1)):
            for number, item in enumerate(items, 1):
                item["number"] = number

    ordered_questions = [
        item
        for block_number in sorted(by_block)
        for item in sorted(by_block[block_number], key=lambda row: row["number"])
    ]
    questions: list[Question] = []
    for sequence, item in enumerate(ordered_questions, 1):
        questions.append(
            Question(
                id=f"{course}-{source_group}-Q{sequence:03d}",
                course=course,
                source_group=source_group,
                source_file=rel,
                block=item["block"],
                sequence=sequence,
                number=item["number"],
                text=item["text"],
                image_ids=item["images"],
                needs_image_review=bool(item["images"]),
            )
        )
    return questions


def render_markdown(questions: list[Question]) -> str:
    lines = [
        "# 통합사회 문항 정규화본",
        "",
        f"- 추출 문항: {len(questions)}개",
        f"- 이미지 판독 필요: {sum(q.needs_image_review for q in questions)}개",
        "",
    ]
    current = None
    for question in questions:
        key = (question.course, question.source_group)
        if key != current:
            lines.extend([f"## {question.course} · {question.source_group}", ""])
            current = key
        lines.extend(
            [
                f"### {question.number}번",
                "",
                f"- ID: `{question.id}`",
                f"- 문제군 블록: {question.block}",
                f"- 이미지: {', '.join(question.image_ids) if question.image_ids else '없음'}",
                "",
                question.text,
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("json_output", type=Path)
    parser.add_argument("markdown_output", type=Path)
    args = parser.parse_args()

    workspace = Path.cwd()
    questions: list[Question] = []
    for path in sorted(args.source.glob("*.hwpx")):
        questions.extend(parse_file(path, workspace))
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps([asdict(q) for q in questions], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.markdown_output.write_text(render_markdown(questions), encoding="utf-8")
    print(
        f"parsed {len(questions)} questions; "
        f"{sum(q.needs_image_review for q in questions)} require image review"
    )


if __name__ == "__main__":
    main()
