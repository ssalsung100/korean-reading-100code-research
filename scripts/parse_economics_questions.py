#!/usr/bin/env python3
"""Parse the advanced Economics HWPX question banks into normalized JSON/Markdown."""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from dataclasses import asdict
from pathlib import Path
from xml.etree import ElementTree as ET

from parse_social_questions import Question, cell_images, cell_text, direct_question_tables


HP = "{http://www.hancom.co.kr/hwpml/2011/paragraph}"


def parse_file(path: Path, workspace: Path) -> list[Question]:
    unit_match = re.search(r"경제_(\d+단원)", path.name)
    source_group = unit_match.group(1) if unit_match else path.stem
    with zipfile.ZipFile(path) as archive:
        section_names = sorted(
            name for name in archive.namelist() if re.fullmatch(r"Contents/section\d+\.xml", name)
        )
        roots = [ET.fromstring(archive.read(name)) for name in section_names]

    rel = path.resolve().relative_to(workspace.resolve()).as_posix()
    questions: list[Question] = []
    sequence = 0
    block = 1
    previous_table_max = 0
    for root in roots:
        for table in direct_question_tables(root):
            rows = table.findall(f"./{HP}tr")
            if len(rows) != 4:
                continue
            table_items = []
            for number_row, question_row in zip((rows[0], rows[2]), (rows[1], rows[3])):
                number_cells = number_row.findall(f"./{HP}tc")
                question_cells = question_row.findall(f"./{HP}tc")
                numbers = [cell_text(cell) for cell in number_cells if cell_text(cell)]
                for raw_number, cell in zip(numbers[:2], question_cells[:2]):
                    if raw_number.isdigit():
                        table_items.append((int(raw_number), cell))
            if not table_items:
                continue
            table_min = min(number for number, _ in table_items)
            table_max = max(number for number, _ in table_items)
            if previous_table_max and table_min <= previous_table_max:
                block += 1
            previous_table_max = table_max
            for number, cell in sorted(table_items, key=lambda item: item[0]):
                sequence += 1
                text = cell_text(cell)
                images = cell_images(cell)
                if not text:
                    continue
                questions.append(
                    Question(
                        id=f"경제-{source_group}-Q{sequence:03d}",
                        course="경제",
                        source_group=source_group,
                        source_file=rel,
                        block=block,
                        sequence=sequence,
                        number=number,
                        text=text,
                        image_ids=images,
                        needs_image_review=bool(images),
                    )
                )
    return questions


def render(questions: list[Question]) -> str:
    lines = [
        "# 심화 경제 문항 정규화본",
        "",
        f"- 추출 문항: {len(questions)}개",
        f"- 이미지 판독 필요: {sum(q.needs_image_review for q in questions)}개",
        "",
    ]
    current = None
    for question in questions:
        if question.source_group != current:
            lines.extend([f"## {question.source_group}", ""])
            current = question.source_group
        lines.extend(
            [
                f"### {question.number}번 · `{question.id}`",
                "",
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
    questions = []
    for path in sorted(args.source.glob("*.hwpx"), key=lambda p: int(re.search(r"경제_(\d+)단원", p.name).group(1))):
        questions.extend(parse_file(path, workspace))
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps([asdict(q) for q in questions], ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    args.markdown_output.write_text(render(questions), encoding="utf-8")
    print(f"parsed {len(questions)} advanced Economics questions")


if __name__ == "__main__":
    main()
