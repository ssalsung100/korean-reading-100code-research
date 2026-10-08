#!/usr/bin/env python3
"""Extract every question-linked image from Integrated Social Studies HWPX files."""

from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "분석/통합사회_문항_정규화.json"
OUT = ROOT / "자료/통합사회_문항이미지_완전판"


def main() -> None:
    questions = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    for name in ("원본", "png", "접촉표"):
        (OUT / name).mkdir(parents=True, exist_ok=True)
    by_source: dict[str, list[dict]] = {}
    for q in questions:
        if q["image_ids"]:
            by_source.setdefault(q["source_file"], []).append(q)

    manifest = []
    for source, rows in by_source.items():
        with zipfile.ZipFile(ROOT / source) as archive:
            members = {Path(n).stem: n for n in archive.namelist() if n.startswith("BinData/")}
            for q in rows:
                for position, image_id in enumerate(q["image_ids"], 1):
                    member = members[image_id]
                    raw = archive.read(member)
                    ext = Path(member).suffix.lower()
                    stem = f"{q['id']}_{position:02d}_{image_id}"
                    original = OUT / "원본" / f"{stem}{ext}"
                    png = OUT / "png" / f"{stem}.png"
                    if not original.exists():
                        original.write_bytes(raw)
                    if png.exists():
                        with Image.open(png) as im:
                            width, height = im.size
                    else:
                        with Image.open(io.BytesIO(raw)) as im:
                            rgb = im.convert("RGB")
                            rgb.save(png, "PNG", optimize=True)
                            width, height = rgb.size
                    manifest.append(
                        {
                            "question_id": q["id"],
                            "course": q["course"],
                            "source_group": q["source_group"],
                            "question_number": q["number"],
                            "block": q["block"],
                            "source_file": source,
                            "binary_item_id": image_id,
                            "position": position,
                            "original_path": original.relative_to(ROOT).as_posix(),
                            "png_path": png.relative_to(ROOT).as_posix(),
                            "width": width,
                            "height": height,
                        }
                    )
    order = {q["id"]: i for i, q in enumerate(questions)}
    manifest.sort(key=lambda x: (order[x["question_id"]], x["position"]))
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# 통합사회 문항 이미지 자료실",
        "",
        f"- 이미지 의존 문항: {len({x['question_id'] for x in manifest})}개",
        f"- 문항 연결 이미지: {len(manifest)}개",
        "- `원본/`: HWPX 내장 파일을 그대로 보존",
        "- `png/`: 판독·문항 제작용 무손실 변환본",
        "- 파일명: `문항ID_문항내순서_HWPX이미지ID`",
        "",
        "| # | 문항 | 문제군 | 크기 | 원본 | PNG |",
        "|---:|---|---|---:|---|---|",
    ]
    for i, row in enumerate(manifest, 1):
        out_rel = OUT.relative_to(ROOT)
        op = Path(row["original_path"]).relative_to(out_rel)
        pp = Path(row["png_path"]).relative_to(out_rel)
        lines.append(
            f"| {i} | {row['question_id']} | {row['course']}·{row['source_group']} | "
            f"{row['width']}×{row['height']} | [{op.name}]({op.as_posix()}) | [{pp.name}]({pp.as_posix()}) |"
        )
    (OUT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    font = ImageFont.load_default(size=23)
    for start in range(0, len(manifest), 12):
        batch = manifest[start : start + 12]
        canvas = Image.new("RGB", (3000, 2800), "white")
        draw = ImageDraw.Draw(canvas)
        for j, row in enumerate(batch):
            col, rr = j % 3, j // 3
            x, y = col * 1000, rr * 700
            label = f"{start+j+1:03d} | {row['question_id']} | {row['binary_item_id']}"
            draw.text((x + 12, y + 8), label, fill="black", font=font)
            with Image.open(ROOT / row["png_path"]) as im:
                im = im.convert("RGB")
                im.thumbnail((960, 625), Image.Resampling.LANCZOS)
                canvas.paste(im, (x + (1000 - im.width) // 2, y + 60 + (625 - im.height) // 2))
            draw.rectangle((x, y, x + 999, y + 699), outline="#777", width=2)
        canvas.save(OUT / "접촉표" / f"sheet_{start//12+1:02d}.jpg", quality=92)
    print(f"extracted {len(manifest)} images from {len({x['question_id'] for x in manifest})} questions")


if __name__ == "__main__":
    main()
