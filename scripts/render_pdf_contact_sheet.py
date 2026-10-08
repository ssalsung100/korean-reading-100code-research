#!/usr/bin/env python3
"""Render selected PDF pages into a labeled contact sheet for visual audit."""

from __future__ import annotations

import argparse
from pathlib import Path

import fitz
from PIL import Image, ImageDraw


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("pages", help="Comma-separated 1-based page numbers")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    page_numbers = [int(value) for value in args.pages.split(",") if value.strip()]
    document = fitz.open(args.pdf)
    thumbs: list[tuple[int, Image.Image]] = []
    for number in page_numbers:
        pixmap = document[number - 1].get_pixmap(matrix=fitz.Matrix(1.2, 1.2), alpha=False)
        image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
        image.thumbnail((700, 980))
        thumbs.append((number, image))

    columns = 2
    cell_w, cell_h = 720, 1030
    rows = (len(thumbs) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "white")
    draw = ImageDraw.Draw(sheet)
    for index, (number, image) in enumerate(thumbs):
        x = (index % columns) * cell_w
        y = (index // columns) * cell_h
        draw.text((x + 10, y + 8), f"PDF page {number}", fill="black")
        sheet.paste(image, (x + 10, y + 38))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.output)
    print(f"rendered {len(thumbs)} pages to {args.output}")


if __name__ == "__main__":
    main()
