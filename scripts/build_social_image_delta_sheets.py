#!/usr/bin/env python3
"""Build contact sheets only for images restored by the lossless question parser."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / "자료/통합사회_문항이미지/manifest.json"
NEW = ROOT / "자료/통합사회_문항이미지_완전판/manifest.json"
OUT = ROOT / "자료/통합사회_문항이미지_완전판/추가복원_접촉표"
DELTA = ROOT / "자료/통합사회_문항이미지_완전판/추가복원_manifest.json"


def main() -> None:
    old = json.loads(OLD.read_text(encoding="utf-8"))
    new = json.loads(NEW.read_text(encoding="utf-8"))
    old_keys = {(row["source_file"], row["binary_item_id"]) for row in old}
    rows = [row for row in new if (row["source_file"], row["binary_item_id"]) not in old_keys]
    DELTA.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    font = ImageFont.load_default(size=23)
    for start in range(0, len(rows), 12):
        batch = rows[start:start + 12]
        canvas = Image.new("RGB", (3000, 2800), "white")
        draw = ImageDraw.Draw(canvas)
        for offset, row in enumerate(batch):
            col, rr = offset % 3, offset // 3
            x, y = col * 1000, rr * 700
            label = f"{start+offset+1:03d} | {row['question_id']} | {row['binary_item_id']}"
            draw.text((x + 12, y + 8), label, fill="black", font=font)
            with Image.open(ROOT / row["png_path"]) as image:
                image = image.convert("RGB")
                image.thumbnail((960, 625), Image.Resampling.LANCZOS)
                canvas.paste(image, (x + (1000-image.width)//2, y + 60 + (625-image.height)//2))
            draw.rectangle((x, y, x + 999, y + 699), outline="#777", width=2)
        canvas.save(OUT / f"delta_{start//12+1:02d}.jpg", quality=92)
    print(f"restored-image delta: {len(rows)} images, {(len(rows)+11)//12} sheets")


if __name__ == "__main__":
    main()
