#!/usr/bin/env python3
"""Compose a canonical LEET question Markdown from verified passage groups."""
from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path("자료/LEET_언어이해")


def group_number(path: Path) -> int:
    match = re.fullmatch(r"q(\d{2})-(\d{2})\.md", path.name)
    if match is None:
        raise ValueError(f"unexpected group filename: {path}")
    return int(match.group(1))


def extract_question_block(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    start = re.search(r"(?m)^## \[\d+~\d+\] ", text)
    end = re.search(r"(?m)^## 정답\s*$", text)
    if start is None or end is None or start.start() >= end.start():
        raise ValueError(f"question block markers missing: {path}")
    return text[start.start():end.start()].rstrip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int)
    parser.add_argument(
        "--variant",
        choices=("odd", "even", "single"),
        default="odd",
        help="single은 홀짝 구분이 없는 문제지이며 출력 파일명에 유형 접미사를 붙이지 않는다.",
    )
    args = parser.parse_args()

    source_dir = ROOT / "전사_검수완료" / str(args.year)
    groups = sorted(source_dir.glob("q??-??.md"), key=group_number)
    if not groups:
        raise SystemExit(f"verified groups not found: {source_dir}")

    starts = [group_number(path) for path in groups]
    expected = list(range(1, 31, 3))
    if starts != expected:
        raise SystemExit(f"incomplete/non-contiguous groups: {starts}")

    filename = (
        f"{args.year}_question.md"
        if args.variant == "single"
        else f"{args.year}_question_{args.variant}.md"
    )
    title_variant = "question" if args.variant == "single" else f"question_{args.variant}"
    out = ROOT / "텍스트" / str(args.year) / filename
    title = f"# {args.year} LEET 언어이해 {title_variant}"
    note = (
        "> 공식 문제지 페이지 직접 대조 완료본. 문항군별 원본 페이지와 해시는 "
        "[전사 검수 manifest](../../전사_검수완료/manifest.json)에 기록되어 있다."
    )
    body = "\n\n".join(extract_question_block(path) for path in groups)
    out.write_text(f"{title}\n\n{note}\n\n{body}\n", encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
