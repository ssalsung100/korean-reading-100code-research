#!/usr/bin/env python3
"""Attach exact HWP page/anchor coordinates to reusable LEET visuals."""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

import cv2
import numpy as np
from PIL import Image


ROOT = Path("자료/LEET_언어이해")
MAP = ROOT / "검증/HWP_홀수형_시각자료_문항매핑_v1.json"
SOURCE = ROOT / "extracted_assets_manifest.json"
CONTROL_ROOT = ROOT / "검증/HWP_홀수형_컨트롤_좌표"
PAGE_ROOT = ROOT / "HWP_홀수형_페이지_렌더링"
OUT_JSON = ROOT / "검증/HWP_홀수형_페이지좌표_v1.json"
OUT_MD = ROOT / "검증/HWP_홀수형_페이지좌표_v1.md"
REUSABLE = {"embedded_figure", "data_table", "choice_table"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def is_picture_control(record: dict) -> bool:
    if record.get("ctrl_id") != "gso":
        return False
    name = record.get("control_name") or ""
    props = record.get("properties") or {}
    if "그림" in name:
        return True
    return (
        not name
        and int(props.get("Width", 0) or 0) > 1000
        and int(props.get("Height", 0) or 0) > 5000
        and props.get("TextWrap") == 0
    )


def to_gray(path: Path) -> np.ndarray:
    with Image.open(path) as image:
        return np.asarray(image.convert("L"))


def match_picture(asset_path: Path, page_path: Path, width_unit: int, height_unit: int) -> dict:
    page = cv2.imread(str(page_path), cv2.IMREAD_GRAYSCALE)
    template = to_gray(asset_path)
    if page is None or template.size == 0:
        return {"status": "unavailable", "score": None, "bbox_px": None}

    expected_w = max(8, round(width_unit * 144 / 7200))
    expected_h = max(8, round(height_unit * 144 / 7200))
    best_score = -1.0
    best: tuple[int, int, int, int, float] | None = None
    for factor in np.linspace(0.90, 1.10, 41):
        width = max(8, round(expected_w * float(factor)))
        height = max(8, round(expected_h * float(factor)))
        if width >= page.shape[1] or height >= page.shape[0]:
            continue
        resized = cv2.resize(template, (width, height), interpolation=cv2.INTER_AREA)
        result = cv2.matchTemplate(page, resized, cv2.TM_CCOEFF_NORMED)
        _, score, _, location = cv2.minMaxLoc(result)
        if score > best_score:
            best_score = float(score)
            best = (location[0], location[1], width, height, float(factor))

    if best is None:
        return {"status": "unavailable", "score": None, "bbox_px": None}
    x, y, width, height, factor = best
    if best_score >= 0.65:
        status = "confirmed"
    elif best_score >= 0.45:
        status = "supporting_match"
    else:
        status = "anchor_only"
    return {
        "status": status,
        "score": round(best_score, 6),
        "bbox_px": [x, y, x + width, y + height],
        "bbox_normalized": [
            round(x / page.shape[1], 6),
            round(y / page.shape[0], 6),
            round((x + width) / page.shape[1], 6),
            round((y + height) / page.shape[0], 6),
        ],
        "scale_vs_hwp_size": round(factor, 4),
        "page_size_px": [page.shape[1], page.shape[0]],
    }


def coordinate(control: dict) -> dict:
    props = control.get("properties") or {}
    return {
        "section_number": control.get("section_number"),
        "printed_page": control.get("printed_page"),
        "column_number": control.get("column_number"),
        "line_number": control.get("line_number"),
        "char_position": control.get("char_position"),
        "anchor_list": control.get("anchor_list"),
        "anchor_para": control.get("anchor_para"),
        "anchor_pos": control.get("anchor_pos"),
        "width_hwpunit": props.get("Width"),
        "height_hwpunit": props.get("Height"),
        "horizontal_offset_hwpunit": props.get("HorzOffset"),
        "vertical_offset_hwpunit": props.get("VertOffset"),
        "horizontal_relative_to": props.get("HorzRelTo"),
        "vertical_relative_to": props.get("VertRelTo"),
        "treat_as_character": props.get("TreatAsChar"),
        "text_wrap": props.get("TextWrap"),
        "control_order": control.get("control_order"),
        "control_name": control.get("control_name"),
    }


def main() -> None:
    mapping = json.loads(MAP.read_text(encoding="utf-8"))
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    source_by_label = {
        item["label"]: item
        for item in source["records"]
        if item["kind"] == "question_odd"
        and item["method"] == "hwp5txt_direct"
        and int(item["year"]) <= 2021
    }
    errors: list[str] = []
    records: list[dict] = []
    page_manifest_records: list[dict] = []

    for paper in mapping["papers"]:
        label = paper["label"]
        controls_path = CONTROL_ROOT / f"{label}.json"
        if not controls_path.is_file():
            errors.append(f"{label}: control coordinate file missing")
            continue
        controls_data = json.loads(controls_path.read_text(encoding="utf-8-sig"))
        controls = controls_data["records"]
        pictures = [item for item in controls if is_picture_control(item)]
        tables = [item for item in controls if item.get("ctrl_id") == "tbl"]
        source_record = source_by_label[label]

        if len(pictures) != int(paper["embedded_figure_count"]):
            errors.append(
                f"{label}: picture control count {len(pictures)} != mapped {paper['embedded_figure_count']}"
            )
        if len(tables) != len(source_record["tables"]):
            errors.append(
                f"{label}: table control count {len(tables)} != source {len(source_record['tables'])}"
            )

        page_files = sorted((PAGE_ROOT / label).glob("page_*.png"))
        page_count = int(controls_data["page_count"])
        if len(page_files) != page_count:
            errors.append(f"{label}: page PNG count {len(page_files)} != HWP {page_count}")
        pages = []
        for number, page_path in enumerate(page_files, 1):
            with Image.open(page_path) as image:
                width, height = image.size
            pages.append(
                {
                    "page": number,
                    "file": str(page_path),
                    "sha256": sha256(page_path),
                    "width": width,
                    "height": height,
                }
            )
        page_manifest_records.append(
            {
                "label": label,
                "year": int(paper["year"]),
                "source_file": paper["source_file"],
                "source_sha256": paper["source_sha256"],
                "page_count": page_count,
                "resolution_dpi": 144,
                "format": "png",
                "pages": pages,
            }
        )

        picture_by_number = {number: item for number, item in enumerate(pictures, 1)}
        for asset in paper["assets"]:
            if asset["kind"] not in REUSABLE:
                continue
            if asset["kind"] == "embedded_figure":
                control = picture_by_number.get(int(asset["asset_number"]))
                basis = "nth_picture_control_in_hwp_control_stream"
            else:
                index = int(asset["asset_number"]) - 1
                control = tables[index] if 0 <= index < len(tables) else None
                basis = "same_ordinal_table_in_hwp_control_stream"
            if control is None:
                errors.append(
                    f"{label} {asset['kind']} #{asset['asset_number']}: control missing"
                )
                continue
            page = int(control["printed_page"])
            page_path = PAGE_ROOT / label / f"page_{page:03d}.png"
            if not page_path.is_file():
                errors.append(f"{label}: rendered page missing: {page_path}")
                continue
            coords = coordinate(control)
            record = {
                "visual_id": f"leet-{label}-{asset['kind']}-{int(asset['asset_number']):03d}",
                "year": int(paper["year"]),
                "label": label,
                "kind": asset["kind"],
                "asset_number": int(asset["asset_number"]),
                "question_group": asset.get("question_group"),
                "asset_file": asset["file"],
                "page_image": str(page_path),
                "page": page,
                "anchor_coordinate": coords,
                "mapping_basis": basis,
                "mapping_confidence": "exact_hwp_anchor",
            }
            if asset["kind"] == "embedded_figure":
                props = control.get("properties") or {}
                record["pixel_verification"] = match_picture(
                    Path(asset["file"]),
                    page_path,
                    int(props.get("Width", 0) or 0),
                    int(props.get("Height", 0) or 0),
                )
            else:
                record["pixel_verification"] = {
                    "status": "not_required",
                    "reason": "table position is represented by the exact HWP anchor; the Markdown table is semantic, not a raster template",
                }
            records.append(record)

    page_manifest = {
        "status": "complete" if not errors else "partial",
        "paper_count": len(page_manifest_records),
        "page_count": sum(item["page_count"] for item in page_manifest_records),
        "renderer": "Hancom HWPFrame.HwpObject.CreatePageImage",
        "records": page_manifest_records,
        "errors": errors,
    }
    (PAGE_ROOT / "manifest.json").write_text(
        json.dumps(page_manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    status_counts = Counter(
        item["pixel_verification"]["status"]
        for item in records
        if item["kind"] == "embedded_figure"
    )
    payload = {
        "status": "complete" if not errors else "partial",
        "scope": "2009예비~2021 LEET 언어이해 홀수형 HWP reusable visual objects",
        "paper_count": len(mapping["papers"]),
        "record_count": len(records),
        "embedded_figure_count": sum(item["kind"] == "embedded_figure" for item in records),
        "data_table_count": sum(item["kind"] == "data_table" for item in records),
        "choice_table_count": sum(item["kind"] == "choice_table" for item in records),
        "page_image_count": page_manifest["page_count"],
        "coordinate_definition": "one-based printed page/column/line plus HWP list-para-pos anchor; picture records also carry pixel bounding boxes when template verification succeeds",
        "figure_pixel_status_counts": dict(status_counts),
        "view_box_policy": "125 generic view-box layout containers remain question-linked in v1 mapping but are excluded from the reusable-visual coordinate audit",
        "records": records,
        "errors": errors,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# LEET HWP 홀수형 페이지·좌표 검증 v1",
        "",
        f"- 상태: **{payload['status']}**",
        f"- 문제지: {payload['paper_count']}개 / 렌더링 페이지: {payload['page_image_count']}쪽",
        f"- 좌표 확정 대상: {payload['record_count']}개(그림 {payload['embedded_figure_count']}, 자료표 {payload['data_table_count']}, 선지표 {payload['choice_table_count']})",
        f"- 그림 픽셀 대조: {dict(status_counts)}",
        "- 좌표 기준: HWP의 1부터 시작하는 인쇄 쪽·단·줄·글자 위치와 List/Para/Pos 앵커",
        "- 일반 `<보기>` 배치 상자 125개는 기존 문항 연결을 유지하되 재사용 시각 자료 좌표 전수 대상에서는 제외했다.",
        "",
        "## 문항별 좌표",
        "",
        "| 연도 | 종류 | 번호 | 문항 | 쪽 | 단 | 줄 | 글자 | 픽셀 대조 |",
        "|---:|---|---:|---|---:|---:|---:|---:|---|",
    ]
    for item in records:
        anchor = item["anchor_coordinate"]
        group = item.get("question_group") or []
        group_text = (
            str(group[0]) if len(group) == 2 and group[0] == group[1] else f"{group[0]}~{group[1]}"
        ) if group else "-"
        pixel = item["pixel_verification"]["status"]
        lines.append(
            f"| {item['label']} | {item['kind']} | {item['asset_number']} | {group_text} | "
            f"{item['page']} | {anchor['column_number']} | {anchor['line_number']} | "
            f"{anchor['char_position']} | {pixel} |"
        )
    lines += ["", "## 오류", ""]
    lines += [f"- {error}" for error in errors] if errors else ["- 없음"]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"{payload['status'].upper()} records={len(records)} pages={payload['page_image_count']} "
        f"figures={payload['embedded_figure_count']} tables={payload['data_table_count'] + payload['choice_table_count']} "
        f"pixel={dict(status_counts)} errors={len(errors)}"
    )
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
