#!/usr/bin/env python3
"""Create lossless PNG working copies and contact sheets for legacy LEET art.

The embedded HWP binary remains authoritative.  PNG files are convenience
copies for Markdown/browser inspection and never replace the source object.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path("자료/LEET_언어이해")
MAP_JSON = ROOT / "검증" / "HWP_홀수형_시각자료_문항매핑_v1.json"
OUT_ROOT = ROOT / "시각자료_작업본_HWP"
OUT_MANIFEST = ROOT / "검증" / "HWP_홀수형_그림_PNG작업본_manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def font(size: int) -> ImageFont.ImageFont:
    candidates = [
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("/usr/share/fonts/truetype/nanum/NanumGothic.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def display_image(path: Path) -> tuple[Image.Image, int]:
    with Image.open(path) as source:
        frames = getattr(source, "n_frames", 1)
        source.seek(0)
        image = ImageOps.exif_transpose(source).copy()
    if image.mode in {"RGBA", "LA"}:
        canvas = Image.new("RGBA", image.size, "white")
        canvas.alpha_composite(image.convert("RGBA"))
        image = canvas.convert("RGB")
    elif image.mode not in {"RGB", "L", "1"}:
        image = image.convert("RGB")
    return image, frames


def pixel_sha256(image: Image.Image) -> str:
    normalized = image.convert("RGBA")
    digest = hashlib.sha256()
    digest.update(f"{normalized.width}x{normalized.height}:RGBA:".encode("ascii"))
    digest.update(normalized.tobytes())
    return digest.hexdigest()


def make_contact_sheet(label: str, items: list[dict], target: Path) -> None:
    heading_font = font(30)
    label_font = font(22)
    margin = 32
    gap = 30
    column_width = 650
    max_image_height = 530
    cells: list[tuple[Image.Image, str, int]] = []

    for item in items:
        image = Image.open(item["preview_file"]).convert("RGB")
        scale = min(column_width / image.width, max_image_height / image.height, 1.0)
        shown = image.resize(
            (max(1, round(image.width * scale)), max(1, round(image.height * scale))),
            Image.Resampling.LANCZOS,
        )
        group = item["question_group"]
        group_text = f"{group[0]}~{group[1]}" if group[0] != group[1] else str(group[0])
        text = (
            f"#{item['asset_number']}  문항 {group_text}  "
            f"{item['source_width']}×{item['source_height']}  {item['source_format']}"
        )
        cells.append((shown, text, shown.height + 48))

    rows = (len(cells) + 1) // 2
    row_heights = [
        max((cells[i][2] for i in range(row * 2, min(row * 2 + 2, len(cells)))), default=0)
        for row in range(rows)
    ]
    width = margin * 2 + column_width * 2 + gap
    height = margin + 52 + sum(row_heights) + max(0, rows - 1) * gap + margin
    sheet = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(sheet)
    draw.text((margin, margin), f"{label} LEET 홀수형 포함 그림", fill="black", font=heading_font)
    y = margin + 52
    for index, (image, text, _) in enumerate(cells):
        row = index // 2
        if index % 2 == 0 and row:
            y += row_heights[row - 1] + gap
        x = margin + (index % 2) * (column_width + gap)
        draw.text((x, y), text, fill="black", font=label_font)
        sheet.paste(image, (x, y + 38))
    target.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(target, format="PNG", optimize=True)


def main() -> None:
    mapping = json.loads(MAP_JSON.read_text(encoding="utf-8"))
    papers: list[dict] = []
    all_items: list[dict] = []
    errors: list[str] = []

    for paper in mapping["papers"]:
        figures = [asset for asset in paper["assets"] if asset["kind"] == "embedded_figure"]
        items: list[dict] = []
        paper_dir = OUT_ROOT / paper["label"]
        paper_dir.mkdir(parents=True, exist_ok=True)
        for asset in figures:
            source = Path(asset["file"])
            target = paper_dir / f"image_{asset['asset_number']:03d}.png"
            try:
                converted, frame_count = display_image(source)
                source_pixel_sha256 = pixel_sha256(converted)
                converted.save(target, format="PNG", optimize=True)
                preview, _ = display_image(target)
                preview_pixel_sha256 = pixel_sha256(preview)
                item = {
                    "year": asset["year"],
                    "label": asset["label"],
                    "asset_number": asset["asset_number"],
                    "question_group": asset["question_group"],
                    "source_file": str(source),
                    "source_sha256": asset["sha256"],
                    "source_format": asset["format"],
                    "source_width": asset["width"],
                    "source_height": asset["height"],
                    "source_frame_count": frame_count,
                    "preview_file": str(target),
                    "preview_sha256": sha256(target),
                    "source_decoded_pixel_sha256": source_pixel_sha256,
                    "preview_decoded_pixel_sha256": preview_pixel_sha256,
                    "pixel_match": source_pixel_sha256 == preview_pixel_sha256,
                    "conversion": "Pillow first-frame lossless PNG; source binary remains authoritative",
                }
                items.append(item)
                all_items.append(item)
            except Exception as exc:  # pragma: no cover - batch diagnostics
                errors.append(f"{paper['label']} #{asset['asset_number']}: {exc}")

        contact_sheet = None
        if items:
            contact = paper_dir / f"{paper['label']}_contact_sheet.png"
            make_contact_sheet(paper["label"], items, contact)
            contact_sheet = str(contact)
        papers.append({
            "year": paper["year"],
            "label": paper["label"],
            "figure_count": len(items),
            "contact_sheet": contact_sheet,
            "items": items,
        })

    payload = {
        "status": "working_copies_complete_pixel_verified",
        "scope": mapping["scope"],
        "figure_count": len(all_items),
        "paper_count": len(papers),
        "note": "PNG files are inspection/Markdown working copies. Embedded HWP binaries and their hashes are authoritative.",
        "pixel_mismatch_count": sum(not item["pixel_match"] for item in all_items),
        "papers": papers,
        "errors": errors,
    }
    OUT_MANIFEST.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"papers={len(papers)} figures={len(all_items)} "
        f"pixel_mismatches={payload['pixel_mismatch_count']} errors={len(errors)}"
    )
    print(OUT_MANIFEST)
    if errors or payload["pixel_mismatch_count"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
