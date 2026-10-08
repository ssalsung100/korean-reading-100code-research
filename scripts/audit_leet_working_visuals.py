#!/usr/bin/env python3
"""Audit LEET visual crops against their official page renders and manifest."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image


ROOT = Path("자료/LEET_언어이해")
VISUAL_ROOT = ROOT / "시각자료_원본"
MANIFEST = VISUAL_ROOT / "manifest.json"
REPORT = ROOT / "검증" / "작업형_시각자료_검증_v1.md"
EXPECTED_BY_YEAR = {2022: 3, 2023: 4, 2024: 1, 2025: 3, 2026: 3, 2027: 6}
EXPECTED_RECORDS = sum(EXPECTED_BY_YEAR.values())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = payload.get("records", [])
    errors: list[str] = []

    if payload.get("status") != "lossless_crops_from_official_page_renders":
        errors.append("manifest status가 예상값과 다름")
    if payload.get("record_count") != len(records):
        errors.append("manifest record_count와 실제 records 수가 다름")
    if len(records) != EXPECTED_RECORDS:
        errors.append(f"시각 자료 수가 {EXPECTED_RECORDS}개가 아님: {len(records)}개")
    counts_by_year = {
        year: sum(record.get("year") == year for record in records)
        for year in EXPECTED_BY_YEAR
    }
    if counts_by_year != EXPECTED_BY_YEAR:
        errors.append(f"학년도별 시각 자료 수 불일치: {counts_by_year}")

    listed_files: set[Path] = set()
    rows: list[tuple[int, int, str, str]] = []
    for index, record in enumerate(records, start=1):
        label = f"record {index} ({record.get('year')} p.{record.get('page')})"
        target = Path(record.get("file", ""))
        source = Path(record.get("official_page", ""))
        listed_files.add(target)

        if not target.is_file():
            errors.append(f"{label}: 결과 PNG 없음: {target}")
            continue
        if not source.is_file():
            errors.append(f"{label}: 공식 페이지 PNG 없음: {source}")
            continue
        if sha256(target) != record.get("file_sha256"):
            errors.append(f"{label}: 결과 PNG SHA-256 불일치")
        if sha256(source) != record.get("official_page_sha256"):
            errors.append(f"{label}: 공식 페이지 SHA-256 불일치")

        normalized = record.get("crop_box_normalized")
        pixels = record.get("crop_box_pixels")
        if not isinstance(normalized, list) or len(normalized) != 4:
            errors.append(f"{label}: 정규화 좌표 형식 오류")
            continue
        if not isinstance(pixels, list) or len(pixels) != 4:
            errors.append(f"{label}: 픽셀 좌표 형식 오류")
            continue

        with Image.open(source) as source_image, Image.open(target) as target_image:
            width, height = source_image.size
            expected_pixels = [
                round(normalized[0] * width),
                round(normalized[1] * height),
                round(normalized[2] * width),
                round(normalized[3] * height),
            ]
            if pixels != expected_pixels:
                errors.append(f"{label}: 정규화 좌표와 픽셀 좌표 불일치")
            expected_size = (pixels[2] - pixels[0], pixels[3] - pixels[1])
            if target_image.size != expected_size:
                errors.append(
                    f"{label}: 결과 크기 불일치 {target_image.size} != {expected_size}"
                )
            if target_image.mode not in {"RGB", "RGBA", "L"}:
                errors.append(f"{label}: 예상하지 않은 이미지 모드 {target_image.mode}")
            expected_crop = source_image.crop(tuple(pixels)).convert("RGBA")
            actual_crop = target_image.convert("RGBA")
            if expected_crop.tobytes() != actual_crop.tobytes():
                errors.append(f"{label}: 공식 페이지 픽셀과 결과 PNG 픽셀 불일치")

        rows.append((record["year"], record["page"], record["name"], str(target)))

    actual_files = set(VISUAL_ROOT.glob("[0-9][0-9][0-9][0-9]/*.png"))
    for extra in sorted(actual_files - listed_files):
        errors.append(f"manifest에 없는 PNG: {extra}")
    for missing in sorted(listed_files - actual_files):
        errors.append(f"manifest에는 있으나 검색되지 않은 PNG: {missing}")

    status = "PASS" if not errors else "FAIL"
    lines = [
        "# 작업형 LEET 시각 자료 검증",
        "",
        f"- 결과: **{status}**",
        f"- manifest 기록: {len(records)}개",
        f"- 실제 PNG: {len(actual_files)}개",
        "- 검사: 파일 존재, 원본·결과 SHA-256, 정규화·픽셀 좌표 일치, 공식 페이지와 자르기 결과의 픽셀 전수 일치, 결과 크기, 미등록 PNG",
        "- 주의: 이 자동 검사는 자산의 동일성과 완결성을 검사한다. 도표 경계와 글자 잘림은 별도 육안 검수 사항이다.",
        "",
        "## 자산",
        "",
        "| 학년도 | 쪽 | 이름 | 파일 |",
        "| --- | ---: | --- | --- |",
    ]
    for year, page, name, target in rows:
        relative = Path("..") / Path(target).relative_to(ROOT)
        lines.append(f"| {year} | {page} | {name} | [{Path(target).name}]({relative.as_posix()}) |")

    lines.extend(["", "## 오류", ""])
    if errors:
        lines.extend(f"- {error}" for error in errors)
    else:
        lines.append("- 없음")

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{status} records={len(records)} files={len(actual_files)} errors={len(errors)}")
    print(REPORT)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
