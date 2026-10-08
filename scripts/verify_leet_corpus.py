#!/usr/bin/env python3
"""Fail-closed integrity gate for the selected odd-form LEET corpus.

All downloaded files remain integrity-checked, but only odd forms are promoted
to the analysis corpus.  Residual layout limitations are reported separately
from actual verification blockers.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path("자료/LEET_언어이해")
OUT_JSON = ROOT / "검증" / "코퍼스_검증게이트_v1.json"
OUT_MD = ROOT / "검증" / "코퍼스_검증게이트_v1.md"
CIRCLED = set("①②③④⑤")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def expected_questions(label: str) -> int:
    if label in {"2009", "2009예비"}:
        return 40
    year = int(label)
    return 35 if year <= 2018 else 30


def main() -> None:
    source = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    assets = json.loads((ROOT / "extracted_assets_manifest.json").read_text(encoding="utf-8"))
    audit = json.loads((ROOT / "검증" / "텍스트_전수검증_v1.json").read_text(encoding="utf-8"))
    answers = json.loads((ROOT / "normalized_answers.json").read_text(encoding="utf-8"))
    hwp_mapping = json.loads(
        (ROOT / "검증" / "HWP_홀수형_시각자료_문항매핑_v1.json").read_text(encoding="utf-8")
    )
    hwp_previews = json.loads(
        (ROOT / "검증" / "HWP_홀수형_그림_PNG작업본_manifest.json").read_text(encoding="utf-8")
    )
    transcripts = json.loads((ROOT / "전사_검수완료" / "manifest.json").read_text(encoding="utf-8"))
    visual_catalog = json.loads(
        (ROOT / "검증" / "LEET_홀수형_시각자료_전체목록_v1.json").read_text(encoding="utf-8")
    )
    hwp_coordinates = json.loads(
        (ROOT / "검증" / "HWP_홀수형_페이지좌표_v1.json").read_text(encoding="utf-8")
    )
    hwp_pages = json.loads(
        (ROOT / "HWP_홀수형_페이지_렌더링" / "manifest.json").read_text(encoding="utf-8")
    )
    errors: list[str] = []
    blockers: list[str] = []
    excluded: list[str] = []
    limitations = [
        "2009예비~2021 HWP 홀수형의 재사용 시각 자료 65개는 쪽·단·줄·글자 및 HWP 앵커를 확정했으나 일반 <보기> 배치 상자 125개는 좌표 감사 대상에서 제외함",
        "2024~2026 Markdown은 공식 PDF 텍스트층의 직접 추출문으로, 편집자가 띄어쓰기를 보정한 전사본은 아님",
    ]

    if source.get("file_count") != len(source.get("entries", [])):
        errors.append("manifest file_count와 entries 수가 다름")
    source_by_file = {}
    for item in source["entries"]:
        path = Path(item["file"])
        source_by_file[str(path)] = item
        if not path.is_file():
            errors.append(f"원본 없음: {path}")
            continue
        if path.stat().st_size != item["bytes"]:
            errors.append(f"원본 크기 불일치: {path}")
        if sha256(path) != item["sha256"]:
            errors.append(f"원본 SHA-256 불일치: {path}")

    for item in assets["records"]:
        src = source_by_file.get(item["source_file"])
        if src is None:
            errors.append(f"파생 기록의 원본이 manifest에 없음: {item['source_file']}")
        elif item["source_sha256"] != src["sha256"]:
            errors.append(f"파생 기록 원본 해시 불일치: {item['source_file']}")
        text_path = Path(item["text_file"])
        if not text_path.is_file():
            errors.append(f"정본 Markdown 없음: {text_path}")
        else:
            text = text_path.read_text(encoding="utf-8")
            if "\ufffd" in text:
                errors.append(f"대체문자 포함: {text_path}")
            if "OCR 초안" in text:
                errors.append(f"OCR 초안이 정본 경로에 혼입됨: {text_path}")
        for fig in item.get("figures", []):
            path = Path(fig["file"])
            if not path.is_file() or sha256(path) != fig["sha256"]:
                errors.append(f"그림 없음 또는 해시 불일치: {path}")
        for table in item.get("tables", []):
            path = Path(table["file"])
            if not path.is_file():
                errors.append(f"표 없음: {path}")
        for page in item.get("page_renders", []):
            path = Path(page["file"])
            if not path.is_file() or sha256(path) != page["sha256"]:
                errors.append(f"페이지 렌더 없음 또는 해시 불일치: {path}")

    if hwp_mapping.get("status") != "stream_order_mapped_page_layout_not_asserted":
        errors.append("HWP 홀수형 시각 자료 매핑 상태 오류")
    if hwp_mapping.get("paper_count") != 14 or hwp_mapping.get("review_required_count") != 0:
        errors.append("HWP 홀수형 문항군 매핑 수 또는 재검토 상태 오류")
    if hwp_previews.get("status") != "working_copies_complete_pixel_verified":
        errors.append("HWP 그림 PNG 작업본 상태 오류")
    if hwp_previews.get("figure_count") != 46 or hwp_previews.get("pixel_mismatch_count") != 0:
        errors.append("HWP 그림 수 또는 픽셀 대조 결과 오류")
    if hwp_previews.get("errors"):
        errors.extend(f"HWP 그림 검증: {x}" for x in hwp_previews["errors"])
    if visual_catalog.get("status") != "PASS" or visual_catalog.get("record_count") != 85:
        errors.append("홀수형 시각 자료 전체 목록 상태 또는 수 오류")
    if visual_catalog.get("errors"):
        errors.extend(f"시각 자료 목록: {x}" for x in visual_catalog["errors"])
    if hwp_coordinates.get("status") != "complete" or hwp_coordinates.get("record_count") != 65:
        errors.append("HWP 페이지·좌표 검증 상태 또는 대상 수 오류")
    if hwp_coordinates.get("embedded_figure_count") != 46:
        errors.append("HWP 좌표 검증 그림 수 오류")
    if hwp_coordinates.get("figure_pixel_status_counts") != {"confirmed": 46}:
        errors.append("HWP 그림 페이지 픽셀 대조 결과 오류")
    if hwp_coordinates.get("errors"):
        errors.extend(f"HWP 좌표 검증: {x}" for x in hwp_coordinates["errors"])
    if hwp_pages.get("status") != "complete" or hwp_pages.get("paper_count") != 14:
        errors.append("HWP 페이지 렌더 manifest 상태 또는 문제지 수 오류")
    if hwp_pages.get("page_count") != 216:
        errors.append("HWP 페이지 렌더 총쪽수 오류")
    if hwp_pages.get("errors"):
        errors.extend(f"HWP 페이지 렌더: {x}" for x in hwp_pages["errors"])
    rendered_page_index: dict[tuple[str, int], dict] = {}
    for paper in hwp_pages.get("records", []):
        if len(paper.get("pages", [])) != paper.get("page_count"):
            errors.append(f"HWP 페이지 목록 수 오류: {paper.get('label')}")
        for page in paper.get("pages", []):
            path = Path(page["file"])
            rendered_page_index[(paper["label"], int(page["page"]))] = page
            if not path.is_file() or sha256(path) != page["sha256"]:
                errors.append(f"HWP 페이지 렌더 없음 또는 해시 불일치: {path}")
    for visual in hwp_coordinates.get("records", []):
        asset = Path(visual["asset_file"])
        page = Path(visual["page_image"])
        if not asset.is_file():
            errors.append(f"HWP 좌표 기록 자산 없음: {asset}")
        expected_page = rendered_page_index.get((visual["label"], int(visual["page"])))
        if expected_page is None or page != Path(expected_page["file"]):
            errors.append(f"HWP 좌표 기록 페이지 연결 오류: {visual.get('visual_id')}")
        anchor = visual.get("anchor_coordinate", {})
        if int(anchor.get("printed_page", 0) or 0) != int(visual["page"]):
            errors.append(f"HWP 앵커 쪽 번호 불일치: {visual.get('visual_id')}")
        pixel = visual.get("pixel_verification", {})
        if visual["kind"] == "embedded_figure":
            bbox = pixel.get("bbox_px")
            if pixel.get("status") != "confirmed" or not bbox or len(bbox) != 4:
                errors.append(f"HWP 그림 픽셀 대조 미확정: {visual.get('visual_id')}")
            elif expected_page is not None:
                x0, y0, x1, y1 = map(int, bbox)
                if not (0 <= x0 < x1 <= int(expected_page["width"]) and 0 <= y0 < y1 <= int(expected_page["height"])):
                    errors.append(f"HWP 그림 픽셀 경계 범위 오류: {visual.get('visual_id')}")

    verified_questions: dict[int, set[int]] = {}
    for record in transcripts.get("records", []):
        path = Path(record["file"])
        if not path.is_file() or sha256(path) != record["file_sha256"]:
            errors.append(f"공식 페이지 대조 완료 전사 없음 또는 해시 불일치: {path}")
        verified_questions.setdefault(record["year"], set()).update(record["questions"])
    for year in (2022, 2023, 2027):
        if verified_questions.get(year) != set(range(1, 31)):
            errors.append(f"{year} 홀수형 공식 페이지 대조 완료 문항이 1~30을 덮지 않음")

    mapped_hwp_labels = {str(paper["label"]) for paper in hwp_mapping["papers"]}
    bad_statuses = {"fail_nonreproducible", "answer_image_only"}
    for item in audit["records"]:
        if item["flags"]:
            errors.append(f"텍스트 감사 플래그: {item['label']} {item['kind']} {item['flags']}")
        if item["status"] in bad_statuses:
            errors.append(f"텍스트 감사 실패: {item['label']} {item['kind']} {item['status']}")
        if item["kind"] == "question_even":
            excluded.append(f"{item['label']} 짝수형")
            continue
        if item["status"] == "pass_direct_hwp_text_layout_pending":
            if item["kind"] != "question_odd" or str(item["label"]) not in mapped_hwp_labels:
                blockers.append(f"HWP 홀수형 시각 자료 대조 필요: {item['label']} {item['kind']}")
        if item["status"] == "image_only_no_canonical_text":
            year = int(item["label"])
            if item["kind"] not in {"question_odd", "question"} or verified_questions.get(year) != set(range(1, 31)):
                blockers.append(f"이미지 본문 공식 페이지 대조 필요: {item['label']} {item['kind']}")

    answer_records = answers["records"]
    if answers.get("answer_source_count") != 20:
        errors.append("정답 출처 수가 20이 아님")
    if len(answer_records) != 39:
        errors.append("정규화 정답 형식 수가 39가 아님")
    forms_by_label: dict[str, set[str | None]] = {}
    for item in answer_records:
        forms_by_label.setdefault(item["label"], set()).add(item["variant"])
        expected = expected_questions(item["label"])
        answer_map = item["answers"]
        if item["status"] not in {"parsed", "verified_visual"}:
            errors.append(f"미검증 정답 상태: {item['label']} {item['variant']} {item['status']}")
        if item["question_count"] != expected or len(answer_map) != expected:
            errors.append(f"정답 문항 수 불일치: {item['label']} {item['variant']}")
        if set(map(int, answer_map)) != set(range(1, expected + 1)):
            errors.append(f"정답 번호 연속성 불일치: {item['label']} {item['variant']}")
        if set(answer_map.values()) - CIRCLED:
            errors.append(f"정답 선지 범위 오류: {item['label']} {item['variant']}")
    for label, forms in forms_by_label.items():
        expected_forms = {None} if label == "2027" else {"odd", "even"}
        if forms != expected_forms:
            errors.append(f"홀짝 형식 불일치: {label} {sorted(str(x) for x in forms)}")

    correction_ledger = ROOT / "검증" / "공식페이지_확정교정_v1.json"
    if correction_ledger.exists():
        ledger = json.loads(correction_ledger.read_text(encoding="utf-8"))
        for item in ledger.get("records", []):
            page = Path(item["official_page_image"])
            if not page.is_file():
                errors.append(f"확정 교정의 공식 페이지 없음: {page}")
            elif sha256(page) != item["official_page_sha256"]:
                errors.append(f"확정 교정의 공식 페이지 해시 불일치: {page}")
            if not item.get("verified_text"):
                errors.append(f"확정 교정의 verified_text 없음: {item}")

    status_counts = Counter(r["status"] for r in audit["records"])
    result = {
        "gate": "PASS" if not errors else "FAIL",
        "errors": errors,
        "manual_verification_blockers": blockers,
        "excluded_alternate_forms": excluded,
        "residual_limitations": limitations,
        "counts": {
            "official_source_files": len(source["entries"]),
            "derived_records": len(assets["records"]),
            "embedded_figures": sum(r.get("figure_count", 0) for r in assets["records"]),
            "extracted_tables": sum(r.get("table_count", 0) for r in assets["records"]),
            "page_renders": sum(r.get("page_render_count", 0) for r in assets["records"]),
            "answer_forms": len(answer_records),
            "audit_statuses": dict(status_counts),
            "automatic_errors": len(errors),
            "manual_blockers": len(blockers),
            "excluded_even_forms": len(excluded),
            "verified_transcript_groups": len(transcripts.get("records", [])),
            "verified_transcript_questions": sum(len(x) for x in verified_questions.values()),
            "cataloged_reusable_visuals": visual_catalog.get("record_count", 0),
            "hwp_coordinate_verified_visuals": hwp_coordinates.get("record_count", 0),
            "hwp_rendered_pages": hwp_pages.get("page_count", 0),
        },
        "scope_note": (
            "PASS는 선택된 홀수형 분석 범위에서 원본 무결성, 직접 추출문, 공식 페이지 대조 전사, "
            "정답 형식, 시각 자료 출처가 검증되었다는 뜻이다. 재사용 HWP 시각 자료 65개는 원래 쪽·단·줄·앵커까지 검증되었다."
        ),
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# LEET 언어이해 코퍼스 검증 게이트 v1\n\n",
        f"- 자동 검증 결과: **{result['gate']}**\n",
        f"- 자동 오류: {len(errors)}개\n",
        f"- 선택된 홀수형 범위의 검증 차단 항목: {len(blockers)}개\n",
        f"- 분석 범위에서 제외한 짝수형: {len(excluded)}개\n",
        f"- 공식 페이지 대조 완료 전사: {len(transcripts.get('records', []))}개 문항군, {sum(len(x) for x in verified_questions.values())}문항\n",
        f"- 재사용 가능 시각 자료: {visual_catalog.get('record_count', 0)}개\n\n",
        "PASS는 선택된 홀수형 분석 범위에서 원본 무결성, 직접 추출문 또는 공식 페이지 대조 전사, 정답 형식, 시각 자료의 출처가 검증되었다는 뜻이다. 재사용 HWP 시각 자료 65개는 원래 쪽·단·줄·앵커까지 검증되었다.\n\n",
        "## 자동 검사 항목\n\n",
        "- 공식 원본의 파일 크기와 SHA-256\n",
        "- 파생 기록과 공식 원본의 연결 및 해시\n",
        "- 정본 Markdown의 존재, 대체문자, OCR 초안 혼입\n",
        "- 그림·페이지 렌더의 SHA-256과 표 파일의 존재\n",
        "- 텍스트 재추출 감사의 실패 상태와 플래그\n",
        "- HWP 홀수형 그림 46개의 해독 픽셀 동일성 및 문항군 매핑\n",
        "- 2022·2023·2027 홀수형 90문항의 공식 페이지 대조 완료 전사\n",
        "- 홀수형 재사용 시각 자료 85개의 통합 목록 상태\n",
        "- HWP 재사용 시각 자료 65개의 원래 쪽·단·줄·앵커와 그림 46개의 페이지 픽셀 대조\n",
        "- HWP 홀수형 14개 문제지 216쪽의 한컴 페이지 렌더 및 해시 manifest\n",
        "- 20개 정답 출처, 39개 형식의 문항 수·번호 연속성·선지 범위\n\n",
        "## 자동 오류\n\n",
    ]
    lines.extend([f"- {x}\n" for x in errors] or ["- 없음\n"])
    lines.extend(["\n## 선택 범위의 검증 차단 항목\n\n"])
    lines.extend([f"- {x}\n" for x in blockers] or ["- 없음\n"])
    lines.extend(["\n## 분석 정본에서 제외한 자료\n\n"])
    lines.extend([f"- {x}\n" for x in excluded] or ["- 없음\n"])
    lines.extend(["\n## 남는 한계\n\n"])
    lines.extend([f"- {x}\n" for x in limitations])
    OUT_MD.write_text("".join(lines), encoding="utf-8")
    print(result["gate"], result["counts"])
    print(OUT_JSON)
    print(OUT_MD)
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
