#!/usr/bin/env python3
"""Index the completed textbook-page visual audit and export key pages."""

from __future__ import annotations

import json
from pathlib import Path

import fitz
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "자료/통합사회_교과서_시각자료"
AUDIT_JSON = ROOT / "분석/통합사회_교과서_시각자료_전수판독.json"
AUDIT_MD = ROOT / "분석/통합사회_교과서_시각자료_전수판독.md"
BOOKS = {
    "통합사회1": ROOT / "통합사회/JIHAKSA_통합사회1_고_교과서.pdf",
    "통합사회2": ROOT / "통합사회/JIHAKSA_통합사회2_고_교과서.pdf",
}

# Contact-sheet visual audit: theme, concept links, and PDF page numbers worth retaining.
GROUPS = {
    "통합사회1": [
        ("통합적 관점·행복 지표", ["integrated_view", "conditions_happiness"], [23, 24, 25, 41, 42, 43, 48]),
        ("기후 지역·기후 그래프", ["climate_regions", "climate_graph_reasoning"], [57, 58, 61]),
        ("재해·환경 문제·생태 윤리", ["disaster_risk_management", "environmental_problem", "environmental_governance", "ecocentrism"], [63, 78, 81, 87]),
        ("문화권·종교·문화 다양성", ["cultural_regions", "religious_landscape", "cultural_change", "cultural_identity"], [91, 92, 95, 96, 105, 113, 115, 116, 117]),
        ("도시화·교통·지역 조사", ["urbanization", "urban_structure", "transport_development", "regional_research"], [130, 131, 133, 135, 137, 140, 145, 148, 149, 150]),
        ("정보화·스마트 도시·미래 사회", ["information_society", "smart_sustainable_city", "fourth_industrial_revolution"], [139, 142, 143]),
    ],
    "통합사회2": [
        ("인권 확장·헌법·인권 지표", ["rights_history", "constitutional_rights", "new_rights", "rights_remedies"], [13, 17, 19, 28, 31, 36, 37]),
        ("정의·불평등·재분배", ["distributive_justice", "equality_principles", "social_inequality", "inequality_indicators", "welfare_policy"], [42, 43, 53, 55, 58, 61]),
        ("자본주의·합리적 선택·시장 참여", ["capitalism_history", "rational_choice", "opportunity_cost", "external_effects", "corporate_responsibility"], [71, 72, 81, 83]),
        ("금융·경제 지표·생애 설계", ["financial_properties", "financial_return_risk", "economic_indicators", "financial_life"], [87, 90, 91, 104, 105]),
        ("무역·세계화·공정 무역", ["international_trade", "comparative_advantage", "production_possibility", "globalization", "fair_trade"], [93, 94, 98, 99, 100, 109, 112]),
        ("국제 평화·분단·동아시아", ["international_peace", "division_unification", "east_asia_conflict", "world_citizenship"], [116, 120, 121, 122, 123, 126, 130, 131]),
        ("인구 구조·인구 정책", ["population_structure", "population_indicators", "demographic_transition", "population_policy"], [134, 135, 136, 138, 139]),
        ("자원·에너지·지속가능발전", ["resource_distribution", "resource_security", "energy_mix_transition", "renewable_energy", "sustainable_development"], [140, 141, 142, 145, 152, 157]),
        ("미래 기술·기술 윤리", ["fourth_industrial_revolution", "technology_ethics_regulation", "future_society"], [148, 151]),
    ],
}


def main() -> None:
    rows = []
    selected_count = 0
    for book, pdf_path in BOOKS.items():
        page_meta = {}
        for theme, concepts, pages in GROUPS[book]:
            for page in pages:
                page_meta[page] = {"theme": theme, "linked_concepts": concepts}
        key_dir = OUT / book / "핵심페이지_고해상도"
        key_dir.mkdir(parents=True, exist_ok=True)
        doc = fitz.open(pdf_path)
        for page_number, page in enumerate(doc, 1):
            selected = page_number in page_meta
            row = {
                "book": book,
                "pdf_page": page_number,
                "inspection_status": "접촉표 육안 판독 완료",
                "key_visual_selected": selected,
                "classification": page_meta.get(page_number, {}).get(
                    "theme", "핵심 문항 자료 비선정(본문·사진·활동·정리·부록 포함)"
                ),
                "linked_concepts": page_meta.get(page_number, {}).get("linked_concepts", []),
                "thumbnail_path": f"자료/통합사회_교과서_시각자료/{book}/페이지_저해상도/{page_number:03d}.jpg",
                "source_pdf": str(pdf_path.relative_to(ROOT)),
            }
            if selected:
                target = key_dir / f"{page_number:03d}.jpg"
                if not target.exists():
                    pix = page.get_pixmap(matrix=fitz.Matrix(1.7, 1.7), alpha=False)
                    image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
                    image.save(target, quality=93, optimize=True)
                row["high_resolution_path"] = str(target.relative_to(ROOT))
                selected_count += 1
            rows.append(row)

    payload = {
        "status": "complete",
        "method": "교과서 336쪽을 28개 접촉표로 전수 육안 판독하고 핵심 자료 쪽은 고해상도로 재추출",
        "scope": {"books": 2, "pages": len(rows), "contact_sheets": 28, "selected_key_pages": selected_count},
        "pages": rows,
    }
    AUDIT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# 통합사회 교과서 시각 자료 전수 판독 장부", "",
        f"- 판독 범위: 교과서 {payload['scope']['books']}권, {len(rows)}쪽",
        f"- 접촉표: {payload['scope']['contact_sheets']}장",
        f"- 문제 제작용 핵심 쪽: {selected_count}쪽",
        "- 상태: 전 쪽 접촉표 육안 판독 완료",
        "- 쪽수는 책에 인쇄된 면수가 아니라 PDF 파일의 페이지 번호이다.", "",
    ]
    for book in BOOKS:
        lines += [f"## {book}", "", "| 주제 | PDF 쪽 | 연결 개념 |", "|---|---|---|"]
        for theme, concepts, pages in GROUPS[book]:
            links = ", ".join(
                f"[{p}](../자료/통합사회_교과서_시각자료/{book}/핵심페이지_고해상도/{p:03d}.jpg)"
                for p in pages
            )
            lines.append(f"| {theme} | {links} | {', '.join(concepts)} |")
        lines.append("")
    lines += [
        "## 이용 원칙", "",
        "- 내부 문제 설계에서는 고해상도 페이지를 자료 후보 탐색과 재도식화의 근거로 쓴다.",
        "- 원본 지면이나 사진을 그대로 외부 배포할 때는 출판물·사진의 이용 권한을 별도로 확인한다.",
        "- 실제 문항에는 수치·관계를 검증한 뒤 새 표·그래프·지도로 재제작하는 방식을 우선한다.",
    ]
    AUDIT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"audited {len(rows)} textbook pages; exported {selected_count} key pages")


if __name__ == "__main__":
    main()
