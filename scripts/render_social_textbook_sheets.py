#!/usr/bin/env python3
"""Render every Integrated Social textbook page into labeled visual contact sheets."""

from __future__ import annotations

from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BOOKS = {
    "통합사회1": ROOT / "통합사회/JIHAKSA_통합사회1_고_교과서.pdf",
    "통합사회2": ROOT / "통합사회/JIHAKSA_통합사회2_고_교과서.pdf",
}
OUT = ROOT / "자료/통합사회_교과서_시각자료"


def render_book(name: str, path: Path) -> None:
    sheet_dir = OUT / name / "접촉표"
    thumb_dir = OUT / name / "페이지_저해상도"
    sheet_dir.mkdir(parents=True, exist_ok=True)
    thumb_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(path)
    expected_sheets = (len(doc) + 11) // 12
    if len(list(thumb_dir.glob("*.jpg"))) == len(doc) and len(list(sheet_dir.glob("*.jpg"))) == expected_sheets:
        print(f"{name}: {len(doc)} pages, {expected_sheets} sheets (existing)")
        return
    font = ImageFont.load_default(size=18)
    thumbs: list[tuple[int, Image.Image]] = []
    for index, page in enumerate(doc, 1):
        pix = page.get_pixmap(matrix=fitz.Matrix(0.9, 0.9), alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        image.thumbnail((500, 680), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (520, 720), "white")
        x = (520 - image.width) // 2
        canvas.paste(image, (x, 32))
        ImageDraw.Draw(canvas).text((12, 8), f"{name} PDF {index:03d}쪽", fill="black", font=font)
        canvas.save(thumb_dir / f"{index:03d}.jpg", quality=88)
        thumbs.append((index, canvas))

    for start in range(0, len(thumbs), 12):
        group = thumbs[start:start + 12]
        sheet = Image.new("RGB", (2080, 2160), "#d8d8d8")
        for position, (_, image) in enumerate(group):
            sheet.paste(image, ((position % 4) * 520, (position // 4) * 720))
        first, last = group[0][0], group[-1][0]
        sheet.save(sheet_dir / f"{first:03d}_{last:03d}.jpg", quality=90)
    print(f"{name}: {len(doc)} pages, {(len(doc) + 11) // 12} sheets")


def main() -> None:
    for name, path in BOOKS.items():
        render_book(name, path)


if __name__ == "__main__":
    main()
