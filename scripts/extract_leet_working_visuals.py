#!/usr/bin/env python3
"""Crop reusable LEET tables, graphs, and diagrams from official page renders.

The crop is a lossless region of an official full-page PNG. The manifest keeps
the source-page hash and pixel rectangle so every asset can be traced back to
the official page. Question text outside the crop is not reconstructed.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image


ROOT = Path("자료/LEET_언어이해")
OUT = ROOT / "시각자료_원본"

# Coordinates are normalized to the official page PNG: left, top, right, bottom.
SPECS = [
    (2022, "2022_question_odd", 6, "q11_망막_밝기와_출력신호_보기", (.528, .173, .895, .501)),
    (2022, "2022_question_odd", 8, "그림1_분할법의_예", (.540, .755, .895, .910)),
    (2022, "2022_question_odd", 9, "그림2_계층법의_예", (.115, .545, .485, .700)),
    (2023, "2023_question_odd", 8, "q15_나이의_정치적효과_연구디자인", (.115, .510, .485, .716)),
    (2023, "2023_question_odd", 10, "제도가능곡선_모델", (.520, .270, .895, .490)),
    (2023, "2023_question_odd", 13, "그림1과2_라이고_간섭계", (.115, .210, .490, .505)),
    (2023, "2023_question_odd", 14, "q27_중력파검출기_민감도_그래프", (.115, .565, .485, .868)),
    (2024, "2024_question_odd", 7, "사회적가치_이해관계자_성과와비용", (.120, .245, .485, .390)),
    (2025, "2025_question_odd", 6, "q12_사법심사_법개정_여론변화", (.545, .317, .890, .430)),
    (2025, "2025_question_odd", 8, "솔로우성장모형_생산량저축량감가상각량", (.580, .600, .880, .695)),
    (2025, "2025_question_odd", 13, "q27_데이터베이스_트랜잭션_상황", (.530, .220, .895, .575)),
    (2026, "2026_question_odd", 3, "DRD와_의사결정테이블", (.125, .240, .485, .380)),
    (2026, "2026_question_odd", 5, "q9_유권자_민주주의신념과이념성향", (.115, .155, .485, .430)),
    (2026, "2026_question_odd", 14, "q27_혼합물_전체부피_그래프", (.115, .155, .485, .405)),
    (2027, "2027_question", 3, "q5_제도결합_가치곡선", (.115, .540, .485, .780)),
    (2027, "2027_question", 5, "대류권_고도와_대기온도", (.150, .580, .480, .763)),
    (2027, "2027_question", 6, "q12_시대X와Y_복사에너지_표", (.115, .157, .485, .276)),
    (2027, "2027_question", 8, "그림1_신뢰게임", (.540, .360, .890, .505)),
    (2027, "2027_question", 8, "그림2_보복가능_신뢰게임", (.540, .507, .890, .645)),
    (2027, "2027_question", 9, "q18_보복선호_신뢰게임", (.115, .508, .485, .705)),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    records = []
    for year, kind, page, name, normalized_box in SPECS:
        source = ROOT / "페이지" / str(year) / kind / f"page_{page:03d}.png"
        if not source.is_file():
            raise FileNotFoundError(source)
        with Image.open(source) as image:
            width, height = image.size
            box = (
                round(normalized_box[0] * width),
                round(normalized_box[1] * height),
                round(normalized_box[2] * width),
                round(normalized_box[3] * height),
            )
            target_dir = OUT / str(year)
            target_dir.mkdir(parents=True, exist_ok=True)
            target = target_dir / f"p{page:02d}_{name}.png"
            image.crop(box).save(target, optimize=True)
        records.append({
            "year": year,
            "kind": kind,
            "page": page,
            "name": name,
            "file": str(target),
            "file_sha256": sha256(target),
            "official_page": str(source),
            "official_page_sha256": sha256(source),
            "crop_box_pixels": list(box),
            "crop_box_normalized": list(normalized_box),
        })
        print(target)

    manifest = OUT / "manifest.json"
    manifest.write_text(json.dumps({
        "status": "lossless_crops_from_official_page_renders",
        "record_count": len(records),
        "records": records,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(manifest)


if __name__ == "__main__":
    main()
