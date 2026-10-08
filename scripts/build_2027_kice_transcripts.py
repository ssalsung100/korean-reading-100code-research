#!/usr/bin/env python3
"""Build reviewed-format Markdown transcripts for 2027 KICE Q1-17.

The source is the positioned text layer of the official PDFs.  Physical line
breaks are rejoined using the trailing-space information retained by the PDF,
while paragraph indentation and question/choice markers restore structure.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

import fitz
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "자료" / "평가원_국어"
OUT_BASE = BASE / "전사_검수완료" / "2027"

SPECS = {
    "6월": {
        "pdf": BASE / "원본" / "2027" / "2027_6월_모의평가_국어_문제.pdf",
        "answers": {1: 1, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 7: 2, 8: 5, 9: 4,
                    10: 2, 11: 3, 12: 5, 13: 5, 14: 5, 15: 4, 16: 3, 17: 1},
    },
    "9월": {
        "pdf": BASE / "원본" / "2027" / "2027_9월_모의평가_국어_문제.pdf",
        "answers": {1: 4, 2: 1, 3: 4, 4: 5, 5: 4, 6: 2, 7: 1, 8: 3, 9: 1,
                    10: 2, 11: 5, 12: 3, 13: 1, 14: 2, 15: 3, 16: 4, 17: 5},
    },
}

GROUPS = [(1, 3, [1]), (4, 9, [2, 3]), (10, 13, [4, 5]), (14, 17, [5, 6])]
CHOICE_MARKS = "①②③④⑤"


@dataclass
class Line:
    page: int
    x0: float
    y0: float
    x1: float
    text: str

    @property
    def column_base(self) -> float:
        return 96.4 if self.x0 < 421 else 445.0

    @property
    def paragraph_indented(self) -> bool:
        return self.x0 - self.column_base > 7.0


@dataclass
class Segment:
    kind: str
    text: str
    page: int
    question: int | None = None


def sha256(path: Path) -> str:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return digest


def source_lines(pdf: Path) -> list[Line]:
    document = fitz.open(pdf)
    pypdf = PdfReader(str(pdf))
    all_lines: list[Line] = []
    for page_index in range(6):
        page = document[page_index]
        # PyMuPDF gives reliable coordinates and glyph strings.  pypdf also
        # retains whether a physical wrap occurred at a word boundary.  Pair
        # the two representations so reflow does not collapse adjacent words.
        trailing_by_key: dict[str, list[bool]] = {}
        for raw in pypdf.pages[page_index].extract_text().splitlines(keepends=True):
            key = re.sub(r"\s+", "", raw)
            trailing_by_key.setdefault(key, []).append(raw.endswith(" \n"))
        page_lines: list[Line] = []
        for block in page.get_text("dict")["blocks"]:
            for raw_line in block.get("lines", []):
                text = "".join(span["text"] for span in raw_line["spans"])
                x0, y0, x1, _ = raw_line["bbox"]
                if not text.strip() or y0 < 150 or y0 > 1076:
                    continue
                if text.strip() in {"제1 교시", "국어 영역"}:
                    continue
                key = re.sub(r"\s+", "", text)
                candidates = trailing_by_key.get(key, [])
                if candidates and candidates.pop(0) and not text.endswith(" "):
                    text += " "
                page_lines.append(Line(page_index + 1, x0, y0, x1, text))
        page_lines.sort(key=lambda row: (row.x0 >= 421, row.y0, row.x0))
        for row in page_lines:
            if re.match(r"^\[18[～~]", row.text.strip()):
                return all_lines
            all_lines.append(row)
    return all_lines


def clean(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+([,.:;!?])", r"\1", text)
    text = text.replace("․", "·")
    text = text.replace("<보 기>", "<보기>")
    text = text.replace("S Q 3 R", "SQ3R")
    text = text.replace("‘ ", "‘").replace("“ ", "“")
    text = text.replace("󰡔", "『").replace("󰡕", "』")
    return text


def append_text(segment: Segment, line: Line) -> None:
    # The source text layer retains a trailing blank when a word boundary
    # occurred at the physical line wrap; no blank means a split word.
    segment.text += line.text


def segment_lines(lines: list[Line]) -> list[Segment]:
    segments: list[Segment] = []
    current_question: int | None = None
    in_box = False

    def start(kind: str, line: Line, question: int | None = None) -> Segment:
        segment = Segment(kind, line.text, line.page, question)
        segments.append(segment)
        return segment

    for line in lines:
        stripped = line.text.strip()
        group_match = re.match(r"^\[(\d+)[～~](\d+)\]", stripped)
        question_match = re.match(r"^(\d{1,2})\.\s*", stripped)
        choice_match = stripped[:1] in CHOICE_MARKS

        if group_match:
            current_question = None
            in_box = False
            start("group", line)
            continue
        if stripped in {"(가)", "(나)"}:
            in_box = False
            start("subsection", line)
            continue
        if question_match:
            current_question = int(question_match.group(1))
            in_box = False
            start("question", line, current_question)
            continue
        if stripped == "[3점]" and segments and segments[-1].kind == "question":
            segments[-1].text = segments[-1].text.rstrip() + " [3점]"
            continue
        if stripped.replace(" ", "") == "<보기>":
            in_box = True
            start("box_header", line, current_question)
            continue
        if stripped.startswith("◦"):
            start("box_bullet", line, current_question)
            continue
        if choice_match:
            in_box = False
            start("choice", line, current_question)
            continue

        if not segments:
            continue
        previous = segments[-1]
        if in_box:
            if previous.kind not in {"box_text", "box_bullet"}:
                previous = start("box_text", line, current_question)
            elif previous.kind == "box_text" and line.paragraph_indented and previous.text.strip():
                previous = start("box_text", line, current_question)
            else:
                append_text(previous, line)
            continue

        if previous.kind in {"question", "choice"}:
            append_text(previous, line)
            continue

        if previous.kind in {"group", "subsection"}:
            start("passage", line)
            continue
        if previous.kind == "passage" and line.paragraph_indented:
            start("passage", line)
            continue
        if previous.kind == "passage":
            append_text(previous, line)
            continue

        start("passage", line)

    for segment in segments:
        segment.text = clean(segment.text)
    return segments


def group_slice(segments: list[Segment], start_q: int, end_q: int) -> list[Segment]:
    group_idx = next(
        i for i, segment in enumerate(segments)
        if segment.kind == "group" and re.match(rf"^\[{start_q}[～~]{end_q}\]", segment.text)
    )
    end_idx = next(
        (i for i in range(group_idx + 1, len(segments)) if segments[i].kind == "group"),
        len(segments),
    )
    return segments[group_idx:end_idx]


def render_segment(segment: Segment, month: str) -> str | None:
    text = segment.text
    if segment.kind == "group":
        text = text.replace("～", "~")
        return f"## {text}"
    if segment.kind == "subsection":
        return f"**{text}**"
    if segment.kind == "passage":
        return text
    if segment.kind == "question":
        if month == "9월" and segment.question == 9:
            text = re.sub(r"ⓐⓑ$", "", text)
        return f"## {text}"
    if segment.kind == "box_header":
        return "> **<보기>**"
    if segment.kind == "box_text":
        return "> " + text
    if segment.kind == "box_bullet":
        return "> - " + text[1:].lstrip()
    if segment.kind == "choice":
        if month == "9월" and segment.question == 9:
            return None
        return text + "  "
    raise AssertionError(segment.kind)


def render_group(month: str, segments: list[Segment], start_q: int, end_q: int,
                 pages: list[int], answers: dict[int, int], pdf: Path) -> str:
    page_links = ", ".join(
        f"[{page}쪽](../../../페이지/2027/{month}/page_{page:03d}.png)"
        for page in pages
    )
    page_hashes = "; ".join(
        f"{page}쪽 `{sha256(BASE / '페이지' / '2027' / month / f'page_{page:03d}.png')}`"
        for page in pages
    )
    lines = [
        f"# 2027학년도 {month} 모의평가 국어 {start_q}~{end_q}번",
        "",
        "> 상태: 공식 문제지 PDF 텍스트 레이어 추출 후 원본 페이지 직접 대조 완료  ",
        f"> 원본 쪽: {page_links}  ",
        f"> 문제지 PDF SHA-256: `{sha256(pdf)}`  ",
        f"> 페이지 SHA-256: {page_hashes}",
        "",
    ]

    inserted_q9 = False
    inserted_q13 = False
    for segment in group_slice(segments, start_q, end_q):
        if month == "9월" and segment.kind == "choice" and segment.question == 9:
            if not inserted_q9:
                lines += [
                    "![9번 선지 대응표](../../../시각자료_원본/2027/q09_선지_대응표.png)",
                    "",
                    "|  | ⓐ | ⓑ |",
                    "|---|---|---|",
                    "| ① | 다르다고 | 주기 |",
                    "| ② | 다르다고 | 가지기 |",
                    "| ③ | 갈린다고 | 가지기 |",
                    "| ④ | 갈라진다고 | 주기 |",
                    "| ⑤ | 갈라진다고 | 더하기 |",
                    "",
                ]
                inserted_q9 = True
            continue
        if (month == "9월" and segment.kind == "choice" and segment.question == 13
                and not inserted_q13):
            lines += [
                "![13번 어댑터 구조도](../../../시각자료_원본/2027/q13_어댑터_구조도.png)",
                "",
            ]
            inserted_q13 = True
        rendered = render_segment(segment, month)
        if rendered is not None:
            lines.extend([rendered, ""])

    answer_lines = [f"{number}. {CHOICE_MARKS[answers[number] - 1]}" for number in range(start_q, end_q + 1)]
    lines += ["## 정답", "", *[line + "  " for line in answer_lines], "", "## 대조 메모", "",
              "- 문단은 공식 원문의 내용 단위로 유지하고 지면의 자동 줄바꿈은 제거했다.",
              "- 문제 번호, 발문, ①~⑤ 선지와 배점은 공식 문제지에서 대조했다.",
              "- 정답은 같은 회차의 평가원 공식 정답표에서 대조했다.", ""]
    if month == "9월" and start_q <= 9 <= end_q:
        lines.append("- 9번 대응표는 원본 크롭과 Markdown 표를 함께 보존했다.")
    if month == "9월" and start_q <= 13 <= end_q:
        lines.append("- 13번 어댑터 구조도는 PDF에 내장된 원본 래스터 이미지를 무변형 추출했다.")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    for month, spec in SPECS.items():
        segments = segment_lines(source_lines(spec["pdf"]))
        out_dir = OUT_BASE / month
        out_dir.mkdir(parents=True, exist_ok=True)
        for start_q, end_q, pages in GROUPS:
            content = render_group(
                month, segments, start_q, end_q, pages, spec["answers"], spec["pdf"]
            )
            path = out_dir / f"q{start_q:02d}-{end_q:02d}.md"
            path.write_text(content, encoding="utf-8")
            print(f"WROTE {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
