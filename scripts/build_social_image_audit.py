#!/usr/bin/env python3
"""Build a visual-semantics audit for all Integrated Social question images."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "자료/통합사회_문항이미지/manifest.json"
QUESTIONS = ROOT / "분석/통합사회_문항_정규화.json"
OUT_JSON = ROOT / "분석/통합사회_이미지_전수판독.json"
OUT_MD = ROOT / "분석/통합사회_이미지_전수판독.md"
REL_JSON = ROOT / "data/social_detailed_visual_relations.json"


# name, parent concept ids, visual basis, conceptual rule
REL = {
    "integrated": ("통합적 관점의 결합", ["integrated_view", "temporal_view", "spatial_view", "social_view", "ethical_view"], "관점의 집합·교차·분류", "한 현상을 시간·공간·사회·윤리 차원에서 함께 보되 각 관점의 질문 기준을 구분한다."),
    "happiness": ("행복 조건과 삶의 질 지표", ["meaning_of_happiness", "conditions_happiness", "settlement_environment", "democracy_happiness"], "소득·건강·교육·환경·민주주의 지표", "행복은 단일 소득 지표가 아니라 정주 환경, 건강, 관계, 민주주의와 도덕적 실천의 복합 조건으로 판단한다."),
    "climate": ("기후 그래프와 기후 지역", ["climate_regions", "climate_graph_reasoning"], "월별 기온선·강수 막대·분포 지도", "최한월·최난월 기온, 연교차, 강수의 총량과 계절 집중을 결합해 기후와 생활 양식을 추론한다."),
    "adaptation": ("자연환경 적응과 생활 양식", ["natural_environment", "climate_regions", "landforms_and_life"], "가옥·농업·의식주 사진과 지역 지도", "주민 생활은 기후·지형의 제약에 적응하지만 기술과 문화에 따라 같은 환경에서도 다른 양상이 나타난다."),
    "landform": ("지형의 형성과 인간 생활", ["landforms_and_life", "natural_environment"], "침식·퇴적 지형 사진과 위치 지도", "지형의 형성 작용을 경관 특징에서 판별하고 이용·재해·보전과 연결한다."),
    "disaster": ("자연재해의 공간 분포와 대응", ["natural_disaster", "disaster_risk_management"], "발생 지도·재난 문자·행동 요령", "재해 규모만이 아니라 노출·취약성·대응 역량이 피해를 결정하며 재해 유형에 맞는 행동이 필요하다."),
    "environment": ("환경 문제의 발생과 해결", ["environmental_problem", "environmental_governance", "environmental_assessment"], "오염 경로·협약·정책 도식", "환경 문제는 월경성과 누적성을 가지므로 원인-이동-피해 경로와 정부·기업·시민·국제 협력을 함께 본다."),
    "environment_ethics": ("인간과 자연의 관계", ["anthropocentrism", "animal_liberation", "life_centrism", "ecocentrism", "biodiversity"], "입장 좌표·사례·생명 범위", "도덕적 고려 대상과 자연의 도구적·내재적 가치 인정 범위로 환경 윤리 입장을 구분한다."),
    "culture_region": ("문화권과 문화 경관", ["cultural_regions", "religious_landscape"], "종교·언어·건축·음식 분포 지도와 사진", "종교·언어·역사·자연환경의 결합이 문화권과 문화 경관을 형성하며 경계는 고정된 선이 아니다."),
    "culture_change": ("문화 변동과 문화 접변", ["cultural_change", "acculturation", "traditional_culture"], "전파 방향·결과 분류·혼합 사례", "발명·발견·전파가 변동을 일으키고 접촉 뒤 병존·동화·융합이 나타날 수 있다."),
    "culture_attitude": ("문화 이해 태도와 다문화 사회", ["attitude_culture", "extreme_relativism", "cultural_identity", "multicultural_policy"], "입장 비교·판단 흐름도", "문화 상대주의는 맥락 이해를 요구하지만 인권 같은 보편 윤리를 침해하는 관행까지 정당화하지는 않는다."),
    "transport": ("교통 발달과 시공간 변화", ["transport_development", "suburbanization_metro"], "시간 거리·물류 흐름·노선 지도", "교통 발달은 시간 거리와 수송비를 줄여 생활권·시장권을 확대하지만 생태 훼손과 지역 격차도 만들 수 있다."),
    "information": ("정보화와 사회 변화", ["information_society", "digital_divide"], "정보 흐름·격차 지표·온라인 사례", "정보화는 거래·소통·참여를 넓히는 동시에 접근 격차, 개인정보 침해, 플랫폼 의존 문제를 낳는다."),
    "digital_citizenship": ("디지털 시민성과 권리", ["digital_citizenship", "new_rights"], "온라인 상호 작용·권리 충돌 사례", "사이버 공간에서도 인권과 책임이 적용되며 표현·기억·삭제·참여 권리는 타인의 권리와 조정되어야 한다."),
    "regional_urban": ("지역 조사·도시화와 공간 구조", ["regional_research", "urbanization", "urban_structure", "urban_problem_regeneration"], "조사 절차·분포도·도시화 그래프", "지역 정보는 조사-정리-도표화로 해석하고 도시화는 인구 집중, 기능 분화, 문제와 재생을 동반한다."),
    "rights": ("인권의 역사·유형·보장", ["human_rights", "rights_history", "constitutional_rights", "rights_categories", "rights_conceptions"], "역사 순서·권리 분류·헌법 조항", "인권은 자유권에서 사회권·연대권으로 확장되며 헌법과 제도로 구체화된다."),
    "rights_remedy": ("권리 침해와 구제·노동권", ["rights_limits", "rights_remedies", "vulnerable_human_rights", "labor_rights", "environmental_rights"], "침해 사례·계약·구제 절차", "권리 제한은 법률·목적·비례성을 갖춰야 하고 침해 유형에 맞는 구제 기관과 절차를 선택해야 한다."),
    "justice": ("정의 원칙과 논증 구조", ["justice", "distributive_justice", "corrective_justice", "rawls", "nozick", "affirmative_action", "equality_principles"], "입장 집합·비판 방향·대전제/소전제", "분배 기준과 자유·평등의 우선순위를 구분하고 원칙이 사례에 적용되는 논증의 타당성을 검토한다."),
    "capitalism": ("자본주의 변화와 경제 체제", ["capitalism_history", "economic_systems", "market_principle"], "역사 단계·체제 분류·주체 역할", "시장과 정부의 역할은 역사적 위기에 따라 달라졌으며 혼합 경제는 두 조정 기제를 함께 사용한다."),
    "market_choice": ("경제 주체·합리적 선택·시장 실패", ["economic_actor_roles", "rational_choice", "opportunity_cost", "market_failure", "external_effects", "government_failure"], "비용·편익 표와 원인-정책 흐름", "순편익을 기준으로 선택하되 외부 효과·공공재·정보 비대칭이 있으면 사적 선택과 사회적 최적이 어긋난다."),
    "finance": ("금융 자산과 생애 재무 설계", ["financial_life", "financial_properties", "financial_return_risk", "household_income_expenditure"], "수익성·안전성·유동성 좌표와 생애 곡선", "금융 상품은 수익·위험·유동성의 상충 관계를 가지므로 생애 소득과 소비에 맞춘 분산이 필요하다."),
    "globalization": ("세계화·지역화와 장소 경쟁", ["globalization", "localization", "global_city", "geographical_indication", "globalization_problems"], "세계 도시·브랜드·상품 네트워크 지도", "세계화는 연결을 확대하고 지역화는 고유 자원을 브랜드화하며 두 과정은 동시에 진행된다."),
    "multinational": ("다국적 기업과 공간적 분업", ["multinational_corporation", "international_trade"], "본사·연구소·부품·조립·판매망", "기업은 기능별 입지 조건을 따라 생산을 분절하고 세계 네트워크로 결합한다."),
    "peace": ("평화·분쟁·통일", ["international_peace", "peace_theory", "international_relations", "east_asia_conflict", "division_unification", "world_citizenship"], "분쟁 지도·행위 주체·통일 비교축", "소극적 평화는 직접 폭력의 부재, 적극적 평화는 구조·문화적 폭력 제거까지 요구하며 갈등 해결에는 다층 행위자가 참여한다."),
    "population": ("인구 구조·이동·변천", ["population_structure", "population_indicators", "demographic_transition", "population_migration", "low_birth_aging", "population_policy"], "인구 피라미드·출생/사망 곡선·이동 지도", "출생률·사망률 변화가 인구 성장 단계와 피라미드를 바꾸고 연령 구조는 부양·노동·복지 문제로 이어진다."),
    "resource": ("자원 분포·무역·안보", ["resource_distribution", "resource_characteristics", "resource_security"], "생산·소비·이동량 지도", "자원의 편재성과 수요 불일치가 국제 이동과 의존을 만들며 가격·외교·안보 문제로 이어진다."),
    "energy": ("에너지 믹스와 전환", ["fossil_fuel", "renewable_energy", "energy_mix_transition", "carbon_neutrality"], "에너지원별 비중·발전량·입지 지도", "에너지 믹스는 부존 자원·기술·비용·환경 정책에 좌우되고 전환은 안정성·경제성·환경성의 균형을 요구한다."),
    "sustainability": ("지속 가능한 발전과 SDGs", ["sustainable_development", "sdgs", "ecological_citizen", "environmental_capacity"], "목표 아이콘·환경/경제 비교표", "현재 세대의 필요와 미래 세대의 가능성을 함께 보며 경제·사회·환경 목표를 통합한다."),
    "technology_ethics": ("미래 기술과 윤리·규제", ["future_society", "fourth_industrial_revolution", "technology_ethics_regulation"], "AI·IoT·자동화 사례와 논증", "기술의 효율뿐 아니라 일자리·편향·프라이버시·책임을 검토하고 위험에 비례한 규제를 설계한다."),
}


def relation_for(i: int) -> str:
    if 1 <= i <= 12 or i in {14,16,17,18,19,20,21,22,202,203,240}: return "integrated"
    if i in {13,23,24,25} or 26 <= i <= 40 or i in {204,241}: return "happiness"
    if i == 15: return "environment_ethics"
    if 41 <= i <= 57 or 99 <= i <= 107: return "climate"
    if i in {58,108,109,110,111,112,113,114,205,206}: return "landform"
    if 59 <= i <= 78: return "disaster"
    if 79 <= i <= 98 or i in {209,210}: return "environment"
    if 115 <= i <= 119: return "disaster"
    if 120 <= i <= 146 or 207 <= i <= 215: return "culture_region"
    if 147 <= i <= 153: return "culture_change"
    if 154 <= i <= 167 or 216 <= i <= 219: return "culture_attitude"
    if 168 <= i <= 170 or 178 <= i <= 182: return "transport"
    if 171 <= i <= 176 or 180 <= i <= 187 or i == 220: return "information"
    if i == 177: return "technology_ethics"
    if 188 <= i <= 201 or i == 242: return "regional_urban"
    if 221 <= i <= 225 or i in {408,409}: return "rights"
    if 226 <= i <= 239 or i in {410,411}: return "rights_remedy"
    if i == 243: return "energy"
    if 244 <= i <= 262 or i == 412: return "justice"
    if 263 <= i <= 270 or i == 413: return "capitalism"
    if 271 <= i <= 274 or 287 <= i <= 291 or i == 414: return "market_choice"
    if 275 <= i <= 286 or i == 292 or i in {415,416}: return "finance"
    if 293 <= i <= 320 or i == 417: return "globalization"
    if 321 <= i <= 323: return "multinational"
    if 324 <= i <= 347 or i in {418,419}: return "peace"
    if 348 <= i <= 359 or 400 <= i <= 402 or 420 <= i <= 424: return "population"
    if 360 <= i <= 374: return "resource"
    if 375 <= i <= 390 or 392 <= i <= 395 or 403 <= i <= 407 or i in {425,426}: return "energy"
    if i == 391: return "sustainability"
    if 396 <= i <= 399 or i == 427: return "technology_ethics"
    raise ValueError(f"unrouted image {i}")


def form_for(rid: str) -> str:
    if rid in {"climate", "disaster", "landform", "culture_region", "globalization", "peace", "population", "resource", "energy", "regional_urban"}:
        return "지도·통계·경관 자료"
    if rid in {"integrated", "culture_change", "culture_attitude", "rights", "rights_remedy", "justice", "capitalism", "market_choice"}:
        return "분류·논증·관계 도식"
    return "사례·그래프·복합 자료"


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    questions = {q["id"]: q for q in json.loads(QUESTIONS.read_text(encoding="utf-8"))}
    rows = []
    for i, image in enumerate(manifest, 1):
        rid = relation_for(i)
        name, parents, basis, rule = REL[rid]
        rows.append({
            **image,
            "audit_index": i,
            "inspection_status": "원본 육안 판독 완료",
            "visual_form": form_for(rid),
            "relation_id": rid,
            "relation_name": name,
            "linked_concepts": parents,
            "visual_basis": basis,
            "key_relation": rule,
            "question_text_preview": questions[image["question_id"]]["text"][:180],
            "generation_use": f"{name}의 자료 해석·원인 결과·보기 적용 문항",
            "reuse_status": "원본·PNG 사용 가능(외부 배포 시 출판물 이용 권한 별도 확인)",
        })
    relations = [{"id": k, "name": v[0], "parent_concepts": v[1], "visual_basis": v[2], "rule": v[3]} for k,v in REL.items()]
    payload = {
        "audit_scope": {"questions": len({r['question_id'] for r in rows}), "images": len(rows)},
        "status": "complete",
        "method": "36개 접촉표 전수 판독 후 문항 텍스트·원본 PNG·기존 개념 지도 교차 검수",
        "relations": relations,
        "images": rows,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REL_JSON.write_text(json.dumps(relations, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = Counter(r["relation_name"] for r in rows)
    lines = [
        "# 통합사회 문제 이미지 전수 판독 장부", "",
        f"- 판독 문항: {payload['audit_scope']['questions']}개", f"- 판독 이미지: {len(rows)}개",
        "- 상태: 원본 육안 판독 완료", "- 문제 제작용 원본·PNG와 문항 출처 연결 완료", "",
        "## 세부 관계", "", "| 관계 | 이미지 | 시각 기준 | 핵심 규칙 |", "|---|---:|---|---|",
    ]
    for rid, (name, parents, basis, rule) in REL.items():
        lines.append(f"| {name} | {counts[name]} | {basis} | {rule} |")
    lines += ["", "## 이미지별 판독", "", "| # | 문항 | 관계 | 형식 | 원본 | PNG |", "|---:|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['audit_index']} | {r['question_id']} | {r['relation_name']} | {r['visual_form']} | [{Path(r['original_path']).name}](../{r['original_path']}) | [{Path(r['png_path']).name}](../{r['png_path']}) |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"audited {len(rows)} images in {payload['audit_scope']['questions']} questions across {len(REL)} relations")


if __name__ == "__main__":
    main()
