#!/usr/bin/env python3
"""Extract answer keys and errata text from the local Integrated Social PDFs."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from pypdf import PdfReader


def clean(text: str) -> str:
    text = text.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    pdfs = sorted(args.source.glob("*.pdf"))
    lines = [
        "# 통합사회 정답표·정오표 텍스트 추출본",
        "",
        "> 정답 결정력과 오류 경계를 분석하기 위한 로컬 근거 자료이다.",
        "",
    ]
    for path in pdfs:
        reader = PdfReader(path)
        lines.extend([f"## {path.stem}", "", f"- 원본: `{path.as_posix()}`", f"- 페이지: {len(reader.pages)}", ""])
        for index, page in enumerate(reader.pages, start=1):
            lines.extend([f"### {index}쪽", "", clean(page.extract_text() or "") or "(추출 텍스트 없음)", ""])

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"extracted {len(pdfs)} PDFs to {args.output}")


if __name__ == "__main__":
    main()
