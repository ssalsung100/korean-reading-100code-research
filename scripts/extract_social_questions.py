#!/usr/bin/env python3
"""Extract reviewable text and media metadata from Integrated Social Studies HWPX files.

This is intentionally a loss-aware extractor: it preserves the HWPX preview text,
also extracts paragraph text from section XML, and records embedded images so that
image-dependent questions can be routed to OCR/manual review instead of silently
losing their stimuli.
"""

from __future__ import annotations

import argparse
import html
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET


HP_NS = "http://www.hancom.co.kr/hwpml/2011/paragraph"


@dataclass
class ExtractedHwpx:
    path: Path
    preview: str
    paragraphs: list[str]
    images: list[str]


def normalize_preview(raw: str) -> str:
    text = html.unescape(raw).replace("\r\n", "\n").replace("\r", "\n")
    # Preview text uses angle brackets as coarse cell/paragraph delimiters.
    text = re.sub(r"><", "\n", text)
    text = re.sub(r"[<>]", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_section_paragraphs(xml_bytes: bytes) -> list[str]:
    root = ET.fromstring(xml_bytes)
    paragraphs: list[str] = []
    for paragraph in root.iter(f"{{{HP_NS}}}p"):
        pieces = [node.text or "" for node in paragraph.iter(f"{{{HP_NS}}}t")]
        text = re.sub(r"\s+", " ", "".join(pieces)).strip()
        if text and not text.startswith("Copyright ⓒ"):
            paragraphs.append(text)
    return paragraphs


def extract_hwpx(path: Path) -> ExtractedHwpx:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        preview_name = "Preview/PrvText.txt"
        preview_raw = (
            archive.read(preview_name).decode("utf-8", errors="replace")
            if preview_name in names
            else ""
        )
        paragraphs: list[str] = []
        for name in sorted(n for n in names if re.fullmatch(r"Contents/section\d+\.xml", n)):
            paragraphs.extend(extract_section_paragraphs(archive.read(name)))
        images = sorted(n for n in names if n.startswith("BinData/") and not n.endswith("/"))
    return ExtractedHwpx(path, normalize_preview(preview_raw), paragraphs, images)


def render_markdown(items: list[ExtractedHwpx], source_root: Path) -> str:
    lines = [
        "# 통합사회 문제 원문 추출본",
        "",
        "> HWPX의 미리보기 텍스트와 본문 XML을 함께 추출한 중간 자료이다. ",
        "> 이미지 자료가 있는 문항은 OCR 또는 수동 판독 전까지 개념 분석을 확정하지 않는다.",
        "",
    ]
    for item in items:
        rel = item.path.relative_to(source_root.parent)
        lines.extend(
            [
                f"## {item.path.stem}",
                "",
                f"- 원본: `{rel.as_posix()}`",
                f"- 포함 이미지: {len(item.images)}개",
                "- 이미지 판독 상태: 미완료" if item.images else "- 이미지 판독 상태: 해당 없음",
                "",
                "### 미리보기 기반 텍스트",
                "",
                item.preview or "(미리보기 텍스트 없음)",
                "",
                "### XML 문단 텍스트",
                "",
            ]
        )
        lines.extend(f"- {paragraph}" for paragraph in item.paragraphs)
        lines.extend(["", "### 이미지 목록", ""])
        lines.extend(f"- `{name}`" for name in item.images)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Directory containing HWPX files")
    parser.add_argument("output", type=Path, help="Markdown output path")
    args = parser.parse_args()

    paths = sorted(args.source.glob("*.hwpx"))
    if not paths:
        raise SystemExit(f"no HWPX files found in {args.source}")
    extracted = [extract_hwpx(path) for path in paths]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_markdown(extracted, args.source), encoding="utf-8")
    print(f"extracted {len(extracted)} HWPX files to {args.output}")


if __name__ == "__main__":
    main()
