#!/usr/bin/env python3
"""Extract question-linked images from Economics HWPX files with provenance."""

from __future__ import annotations

import io
import json
import re
import shutil
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "분석/심화경제_문항_정규화.json"
OUT = ROOT / "자료/심화경제_문항이미지"


def unit_number(group: str) -> int:
    return int(re.search(r"\d+", group).group())


def main() -> None:
    questions = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    originals = OUT / "원본"
    pngs = OUT / "png"
    sheets = OUT / "접촉표"
    originals.mkdir(parents=True, exist_ok=True)
    pngs.mkdir(parents=True, exist_ok=True)
    sheets.mkdir(parents=True, exist_ok=True)
    manifest = []

    by_source: dict[str, list[dict]] = {}
    for q in questions:
        if q["image_ids"]:
            by_source.setdefault(q["source_file"], []).append(q)

    for source, source_questions in by_source.items():
        source_path = ROOT / source
        unit = unit_number(source_questions[0]["source_group"])
        with zipfile.ZipFile(source_path) as archive:
            members = {Path(n).stem: n for n in archive.namelist() if n.startswith("BinData/")}
            for q in source_questions:
                for position, image_id in enumerate(q["image_ids"], 1):
                    member = members[image_id]
                    raw = archive.read(member)
                    ext = Path(member).suffix.lower()
                    stem = f"{q['id']}_{position:02d}_{image_id}"
                    original_rel = Path("원본") / f"{stem}{ext}"
                    png_rel = Path("png") / f"{stem}.png"
                    (OUT / original_rel).write_bytes(raw)
                    with Image.open(io.BytesIO(raw)) as im:
                        rgb = im.convert("RGB")
                        rgb.save(OUT / png_rel, "PNG", optimize=True)
                        width, height = rgb.size
                    manifest.append(
                        {
                            "question_id": q["id"],
                            "unit": unit,
                            "question_number": q["number"],
                            "block": q["block"],
                            "source_file": source,
                            "binary_item_id": image_id,
                            "position": position,
                            "original_path": (Path("자료/심화경제_문항이미지") / original_rel).as_posix(),
                            "png_path": (Path("자료/심화경제_문항이미지") / png_rel).as_posix(),
                            "width": width,
                            "height": height,
                        }
                    )

    manifest.sort(key=lambda x: (x["unit"], x["question_id"], x["position"]))
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# 심화 경제 문항 이미지 자료실",
        "",
        f"- 문항 연결 이미지: {len(manifest)}개",
        "- `원본/`: HWPX에 내장된 BMP·PNG를 바이트 그대로 보존",
        "- `png/`: 문제 제작과 판독에 쓰기 쉽게 무손실 PNG로 변환",
        "- 파일명: `문항ID_문항내순서_HWPX이미지ID`",
        "",
        "| 문항 ID | 단원·번호 | 크기 | 원본 | PNG |",
        "|---|---|---:|---|---|",
    ]
    for row in manifest:
        original_link = Path(row["original_path"]).relative_to("자료/심화경제_문항이미지")
        png_link = Path(row["png_path"]).relative_to("자료/심화경제_문항이미지")
        lines.append(
            f"| {row['question_id']} | {row['unit']}단원 {row['question_number']}번 | "
            f"{row['width']}×{row['height']} | [{Path(row['original_path']).name}]({original_link.as_posix()}) | "
            f"[{Path(row['png_path']).name}]({png_link.as_posix()}) |"
        )
    (OUT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Twelve labeled images per sheet; originals remain available for fine inspection.
    font = ImageFont.load_default(size=24)
    for start in range(0, len(manifest), 12):
        batch = manifest[start : start + 12]
        canvas = Image.new("RGB", (3000, 2800), "white")
        draw = ImageDraw.Draw(canvas)
        for i, row in enumerate(batch):
            col, rr = i % 3, i // 3
            x, y = col * 1000, rr * 700
            label = f"{start+i+1:03d} | {row['question_id']} | {row['binary_item_id']}"
            draw.text((x + 15, y + 10), label, fill="black", font=font)
            with Image.open(ROOT / row["png_path"]) as im:
                im = im.convert("RGB")
                im.thumbnail((960, 625), Image.Resampling.LANCZOS)
                canvas.paste(im, (x + (1000 - im.width) // 2, y + 60 + (625 - im.height) // 2))
            draw.rectangle((x, y, x + 999, y + 699), outline="#777777", width=2)
        sheet_no = start // 12 + 1
        canvas.save(sheets / f"sheet_{sheet_no:02d}.jpg", quality=92)

    print(f"extracted {len(manifest)} linked images; built {(len(manifest)+11)//12} contact sheets")


if __name__ == "__main__":
    main()
