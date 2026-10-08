#!/usr/bin/env python3
"""Structurally audit noncanonical high-resolution LEET PaddleOCR drafts.

This audit checks provenance, hashes, page completeness, and the separation
from the canonical text tree. It never treats OCR wording as verified text.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path("자료/LEET_언어이해")
PADDLE = ROOT / "OCR_초안_Paddle"
CANONICAL = ROOT / "텍스트"
REPORT_JSON = ROOT / "검증" / "PaddleOCR_초안_구조검증_v1.json"
REPORT_MD = ROOT / "검증" / "PaddleOCR_초안_구조검증_v1.md"
REQUIRED_ENGINE = "korean_PP-OCRv4_official_pdf_3x_det2400_v2"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    errors: list[str] = []
    records: list[dict] = []
    canonical_root = CANONICAL.resolve()

    for directory in sorted(path for path in PADDLE.glob("*/question*") if path.is_dir()):
        label, kind = directory.parent.name, directory.name
        json_paths = sorted(directory.glob("page_*.json"))
        md_paths = sorted(directory.glob("page_*.md"))
        item_errors: list[str] = []
        page_numbers: list[int] = []
        official_images: list[str] = []

        if not json_paths:
            item_errors.append("페이지 JSON 없음")

        for json_path in json_paths:
            try:
                data = json.loads(json_path.read_text(encoding="utf-8"))
            except Exception as exc:  # noqa: BLE001 - audit must report malformed JSON
                item_errors.append(f"{json_path.name}: JSON 해석 실패: {exc}")
                continue

            page = data.get("page")
            page_numbers.append(page)
            expected_stem = f"page_{page:03d}"
            if json_path.stem != expected_stem:
                item_errors.append(f"{json_path.name}: 페이지 번호와 파일명 불일치")
            if data.get("status") != "unverified_paddle_ocr":
                item_errors.append(f"{json_path.name}: 비정본 상태 표지 불일치")
            if data.get("engine_version") != REQUIRED_ENGINE:
                item_errors.append(f"{json_path.name}: OCR 엔진 버전 불일치")
            if data.get("label") != label or data.get("kind") != kind:
                item_errors.append(f"{json_path.name}: 학년도/종류 메타데이터 불일치")
            if data.get("render_matrix") != [3, 3]:
                item_errors.append(f"{json_path.name}: 3배 렌더링 기록 불일치")

            regions = data.get("regions") or []
            if len(regions) != 2 or [r.get("name") for r in regions] != ["left", "right"]:
                item_errors.append(f"{json_path.name}: 좌·우 2영역 구조 불일치")
            for region in regions:
                tokens = region.get("tokens") or []
                if region.get("token_count") != len(tokens):
                    item_errors.append(f"{json_path.name}/{region.get('name')}: 토큰 수 불일치")
                if region.get("lines") is None:
                    item_errors.append(f"{json_path.name}/{region.get('name')}: 줄 텍스트 없음")

            image_path = Path(data.get("official_page_image", ""))
            official_images.append(str(image_path))
            if not image_path.is_file():
                item_errors.append(f"{json_path.name}: 공식 페이지 이미지 없음")
            elif sha256(image_path) != data.get("official_page_sha256"):
                item_errors.append(f"{json_path.name}: 공식 페이지 이미지 해시 불일치")

            source_path = Path(data.get("source_file", ""))
            if not source_path.is_file():
                item_errors.append(f"{json_path.name}: 공식 원본 파일 없음")
            elif sha256(source_path) != data.get("source_sha256"):
                item_errors.append(f"{json_path.name}: 공식 원본 해시 불일치")

            md_path = json_path.with_suffix(".md")
            if not md_path.is_file():
                item_errors.append(f"{md_path.name}: Markdown 없음")
            else:
                text = md_path.read_text(encoding="utf-8")
                if "비정본 OCR 초안" not in text or "공식 페이지와 직접 대조" not in text:
                    item_errors.append(f"{md_path.name}: 비정본 경고 없음")
                if len(re.findall(r"(?m)^## (?:left|right)$", text)) != 2:
                    item_errors.append(f"{md_path.name}: 좌·우 영역 표지 불일치")
                if "\ufffd" in text:
                    item_errors.append(f"{md_path.name}: 유니코드 대체문자 포함")
                try:
                    md_path.resolve().relative_to(canonical_root)
                except ValueError:
                    pass
                else:
                    item_errors.append(f"{md_path.name}: 정본 텍스트 트리에 혼입")

        expected_pages = list(range(1, len(list((ROOT / "페이지" / label / f"{label}_{kind}").glob("page_*.png"))) + 1))
        if page_numbers != expected_pages:
            item_errors.append(f"페이지 연속성 불일치: OCR={page_numbers}, 공식={expected_pages}")
        expected_md = {path.with_suffix(".md").name for path in json_paths}
        actual_md = {path.name for path in md_paths}
        if actual_md != expected_md:
            item_errors.append("JSON과 Markdown 페이지 집합 불일치")

        records.append({
            "label": label,
            "kind": kind,
            "status": "STRUCTURE_PASS" if not item_errors else "FAIL",
            "page_count": len(json_paths),
            "page_numbers": page_numbers,
            "official_page_images": official_images,
            "errors": item_errors,
        })
        errors.extend(f"{label} {kind}: {error}" for error in item_errors)

    if not records:
        errors.append("PaddleOCR 초안 디렉터리 없음")

    payload = {
        "status": "STRUCTURE_PASS" if not errors else "FAIL",
        "required_engine": REQUIRED_ENGINE,
        "error_count": len(errors),
        "errors": errors,
        "records": records,
        "warning": "STRUCTURE_PASS는 OCR 철자 정확성을 뜻하지 않는다. 공식 페이지 수동 대조 전까지 모든 OCR 문장은 비정본이다.",
    }
    REPORT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# PaddleOCR 초안 구조 검증 v1\n\n",
        f"- 결과: **{payload['status']}**\n",
        f"- 구조 오류: {len(errors)}개\n",
        f"- 요구 엔진: `{REQUIRED_ENGINE}`\n\n",
        "> 이 검사는 출처·해시·페이지 완결성과 정본 격리만 확인한다. OCR 철자 정확성을 인증하지 않는다.\n\n",
        "| 학년도 | 종류 | 판정 | 페이지 | 범위 |\n",
        "| --- | --- | --- | ---: | --- |\n",
    ]
    for record in records:
        pages = record["page_numbers"]
        page_range = f"{pages[0]}–{pages[-1]}" if pages else "-"
        lines.append(f"| {record['label']} | {record['kind']} | `{record['status']}` | {record['page_count']} | {page_range} |\n")
    lines.extend(["\n## 오류\n\n"])
    lines.extend([f"- {error}\n" for error in errors] or ["- 없음\n"])
    REPORT_MD.write_text("".join(lines), encoding="utf-8")
    print(payload["status"], "errors", len(errors), "records", len(records))
    print(REPORT_JSON)
    print(REPORT_MD)
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
