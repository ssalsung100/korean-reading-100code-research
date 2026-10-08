#!/usr/bin/env python3
"""Render all raster files below a directory into a labeled contact sheet."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


def get_font(size: int) -> ImageFont.ImageFont:
    for path in (
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ):
        if Path(path).is_file():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--columns", type=int, default=3)
    args = parser.parse_args()

    files = sorted(
        path for path in args.source.rglob("*")
        if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".tif", ".tiff"}
    )
    cell_w, cell_h = 560, 480
    rows = (len(files) + args.columns - 1) // args.columns
    sheet = Image.new("RGB", (cell_w * args.columns, cell_h * rows), "white")
    draw = ImageDraw.Draw(sheet)
    label_font = get_font(17)

    for index, path in enumerate(files):
        with Image.open(path) as source:
            image = ImageOps.exif_transpose(source).convert("RGB")
        image.thumbnail((cell_w - 30, cell_h - 90), Image.Resampling.LANCZOS)
        x = (index % args.columns) * cell_w + 15
        y = (index // args.columns) * cell_h + 15
        label = str(path.relative_to(args.source))
        draw.text((x, y), label, fill="black", font=label_font)
        draw.text((x, y + 28), f"{source.width}×{source.height}", fill="black", font=label_font)
        sheet.paste(image, (x, y + 62))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.output, optimize=True)
    print(f"rendered {len(files)} images to {args.output}")


if __name__ == "__main__":
    main()
