#!/usr/bin/env python3
"""174개 개념을 출제 가능한 묶음과 전 범위 배분표로 변환한다."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONCEPT_PATH = ROOT / "data/social_concepts_v1.json"
OUT = ROOT / "분석"


def b(code, area, title, focus, concepts, core=2, visual="개념 관계도 또는 사례 자료"):
    return {
        "id": code,
        "area": area,
        "title": title,
        "focus": focus,
        "concept_ids": concepts,
        "core_count": core,
        "recommended_visual": visual,
    }


# 교과서 목차 순서가 아니라 사회과 영역별 설명 가능성과 개념 선후 관계로 묶었다.
# 각 묶음의 첫 core_count개는 본문 중심, 나머지는 본문 연계 개념이다.
BUNDLES = [
    # 윤리
    b("ETH-01", "윤리", "행복을 무엇으로 판단하는가", "행복의 기준을 덕·쾌락·평정·동양 사상의 관점에서 비교", ["meaning_of_happiness", "eudaimonia", "pleasure_happiness", "stoic_happiness", "eastern_happiness"], 2, "사상가 발언·입장 비교표"),
    b("ETH-02", "윤리", "행복의 개인적·사회적 조건", "좋은 삶을 개인의 실천과 정주·정치 조건의 결합으로 설명", ["conditions_happiness", "moral_practice_happiness", "settlement_environment", "democracy_happiness"], 2, "행복 조건 지표·사례 비교표"),
    b("ETH-03", "윤리", "도덕적 고려의 범위는 어디까지인가", "인간 중심주의에서 동물·생명·생태 중심주의로 고려 범위를 확장", ["ethical_view", "anthropocentrism", "animal_liberation", "life_centrism", "ecocentrism"], 2, "도덕적 고려 대상의 포함 관계도"),
    b("ETH-04", "윤리", "분배 정의의 기준과 소유 권리", "평등 기준과 롤스·노직·공동체주의의 분배 원칙을 대조", ["justice", "distributive_justice", "equality_principles", "rawls", "nozick", "liberal_communitarian"], 2, "분배 원칙·가상 배분 결과표"),
    b("ETH-05", "윤리", "잘못을 어떻게 바로잡을 것인가", "교정적 정의와 형벌 정당화, 부정의한 법에 대한 시민 불복종의 조건", ["corrective_justice", "punishment_theories", "civil_disobedience", "justice"], 2, "판결 사례·행위 조건 도식"),
    b("ETH-06", "윤리", "확장되는 시민의 책임", "소비·생태·세계·기술 영역으로 확장되는 시민 윤리", ["ecological_citizen", "ethical_consumption", "world_citizenship", "technology_ethics_regulation"], 2, "행위 주체별 책임 매트릭스"),

    # 지리
    b("GEO-01", "지리", "기후 자료로 생활 양식을 추론하는 법", "공간적 관점과 기후 그래프를 이용해 기후 지역의 생활을 추론", ["spatial_view", "natural_environment", "climate_regions", "climate_graph_reasoning"], 2, "세계 기후 지도·기후 그래프"),
    b("GEO-02", "지리", "지형은 인간 생활의 조건이 되는가", "지형 형성과 토지 이용·산업·정주 방식의 관계", ["landforms_and_life", "natural_environment", "settlement_environment"], 2, "지형 단면도·토지 이용 사진"),
    b("GEO-03", "지리", "재해와 위험은 같은 말이 아니다", "자연현상, 노출, 취약성, 대응 역량을 구분하여 재해 위험을 설명", ["natural_disaster", "disaster_risk_management", "spatial_view"], 2, "재해 위험 함수·지역별 취약성 지도"),
    b("GEO-04", "지리", "환경 문제의 발생과 개발의 한계", "환경 용량을 넘는 이용이 생태계·생물 다양성과 환경 갈등에 미치는 영향", ["environmental_problem", "environmental_capacity", "biodiversity", "environmental_assessment", "environmental_conflict"], 2, "개발 전후 생태 자료·이해관계자 도식"),
    b("GEO-05", "지리", "기후 위기를 다층적으로 다스리는 방법", "지속가능발전에서 국제 협약·국내 거버넌스·탄소중립으로 이어지는 대응", ["sustainable_development", "climate_governance", "environmental_governance", "carbon_neutrality", "sdgs"], 2, "국가·정부·기업·시민 역할 도식"),
    b("GEO-06", "지리", "도시는 어떻게 분화하고 확장하는가", "도시화, 내부 구조, 교외화, 도시 문제와 재생·스마트 도시의 관계", ["urbanization", "urban_structure", "suburbanization_metro", "urban_problem_regeneration", "smart_sustainable_city"], 2, "도시 내부 구조 모식도·시계열 항공 사진"),
    b("GEO-07", "지리", "교통과 정보가 지역을 바꾸는 방식", "접근성 변화와 지역 조사 자료를 이용해 지역 격차를 분석", ["transport_development", "regional_research", "regional_inequality", "spatial_view"], 2, "교통망 변화 지도·GIS 중첩도"),
    b("GEO-08", "지리", "문화권과 종교 경관의 형성", "문화권 구분과 종교 확산이 지역 경관에 남긴 흔적", ["cultural_regions", "religious_landscape", "culture"], 2, "문화권·종교 분포 지도"),
    b("GEO-09", "지리", "세계화와 지역화는 반대인가", "다국적 기업·세계 도시와 장소 마케팅·지리적 표시제가 공존하는 구조", ["globalization", "localization", "multinational_corporation", "global_city", "geographical_indication", "globalization_problems"], 2, "다국적 기업 기능 입지 지도·지역 상품 사례"),
    b("GEO-10", "지리", "인구 구조와 이동의 연쇄", "인구 지표와 인구 변천을 바탕으로 저출산·고령화·이주·정책을 연결", ["population_structure", "population_indicators", "demographic_transition", "low_birth_aging", "population_migration", "population_policy"], 2, "인구 피라미드·인구 이동 흐름도"),
    b("GEO-11", "지리", "자원의 편재와 에너지 전환", "자원의 특성과 공간적 편재가 자원 안보와 에너지 믹스 전환에 미치는 영향", ["resource_distribution", "resource_characteristics", "resource_security", "fossil_fuel", "renewable_energy", "energy_mix_transition"], 2, "자원 분포 지도·국가별 에너지 믹스"),

    # 사회·문화
    b("SOC-01", "사회문화", "문화를 이해하는 기준과 한계", "문화의 속성·보편성·다양성에서 문화 상대주의의 적용 한계까지", ["social_view", "culture", "cultural_universality", "attitude_culture", "extreme_relativism"], 2, "문화 사례 판정표·입장 비교"),
    b("SOC-02", "사회문화", "문화는 어떻게 변하고 정체성이 되는가", "문화 변동과 접변, 전통의 재구성, 다문화 정체성과 통합 정책", ["cultural_change", "acculturation", "traditional_culture", "cultural_identity", "multicultural_policy"], 2, "문화 접변 결과 벤다이어그램·사례 계보"),
    b("SOC-03", "사회문화", "산업화에서 정보화까지의 사회 변화", "산업·정보 기술 변화가 문화 지체·격차·시민 책임을 발생시키는 과정", ["industrial_social_change", "information_society", "cultural_lag", "digital_divide", "digital_citizenship"], 2, "산업 구조 시계열·정보 격차 통계"),
    b("SOC-04", "사회문화", "불평등은 어떻게 측정하고 완화하는가", "불평등 양상과 지표, 복지 정책 및 적극적 우대 조치의 기준", ["social_inequality", "inequality_indicators", "welfare_policy", "affirmative_action", "equality_principles"], 2, "소득 분포·불평등 지수·정책 효과표"),
    b("SOC-05", "사회문화", "인공지능 시대의 사회 변화", "제4차 산업 혁명과 미래 사회에서 기술 규제와 사회 제도의 대응", ["future_society", "fourth_industrial_revolution", "technology_ethics_regulation", "information_society"], 2, "기술 확산 시나리오·이해관계자 표"),

    # 경제
    b("ECO-01", "경제", "희소성에서 최적 선택까지", "비용·편익과 기회비용을 한계적으로 비교하는 선택 원리", ["scarcity", "rational_choice", "opportunity_cost", "marginal_analysis"], 2, "선택 대안별 편익·비용 표"),
    b("ECO-02", "경제", "경제 체제와 경제 주체의 역할", "국민 경제 순환 속 가계·기업·정부의 목적과 경제 체제의 차이", ["economic_activity_flow", "economic_systems", "economic_agent_objectives", "economic_actor_roles", "capitalism_history"], 2, "국민 경제 순환도·경제 체제 비교표"),
    b("ECO-03", "경제", "소비자는 예산 안에서 무엇을 선택하는가", "가계 소득·지출과 예산 제약 아래 효용 및 윤리적 소비를 함께 고려", ["consumer_choice_budget", "household_income_expenditure", "rational_choice", "ethical_consumption"], 2, "예산선·소비 조합표"),
    b("ECO-04", "경제", "기업의 이윤과 책임은 충돌하는가", "생산·비용·수입에 따른 이윤 극대화와 기업의 사회적 책임", ["firm_production_cost", "corporate_responsibility", "economic_agent_objectives"], 2, "생산량별 비용·수입 그래프"),
    b("ECO-05", "경제", "시장 균형은 어떻게 움직이는가", "수요·공급, 연관재, 동시 변동과 탄력성으로 균형 변화를 추론", ["market_principle", "demand_supply", "demand_supply_shift", "simultaneous_market_shift", "elasticity"], 2, "수요·공급 곡선과 이동 도식"),
    b("ECO-06", "경제", "시장 규제와 후생의 변화", "경제적 잉여를 기준으로 가격 규제·조세·독과점 정책의 효과를 평가", ["economic_surplus_efficiency", "price_regulation", "tax_subsidy_incidence", "monopoly_competition"], 2, "잉여 영역·거래량 변화 그래프"),
    b("ECO-07", "경제", "시장은 왜 실패하고 정부도 왜 실패하는가", "외부 효과·공공재·정보 비대칭을 교정하는 정책과 정부 실패의 가능성", ["market_failure", "external_effects", "public_goods", "information_asymmetry", "externality_correction", "government_failure"], 2, "사적·사회적 비용 곡선·정책 비교"),
    b("ECO-08", "경제", "국민소득과 경제 지표를 읽는 법", "국민소득 측정, 명목·실질 구분, 증가율의 누적 효과", ["national_income_accounting", "nominal_real_indicators", "compound_rate_change", "economic_indicators"], 2, "명목·실질 지표 시계열 표"),
    b("ECO-09", "경제", "물가와 고용 지표의 함정", "인플레이션 유형과 고용 상태 이동, 실망 실업자가 지표에 미치는 영향", ["price_level_inflation", "employment_indicators", "inflation_types", "labor_market_wage", "discouraged_worker_effect"], 2, "고용 상태 이동도·물가 지수표"),
    b("ECO-10", "경제", "경기 변동과 안정화 정책", "총수요·총공급 충격에 재정·통화 정책과 정책 조합이 작동하는 경로", ["business_cycle", "aggregate_demand_supply", "fiscal_policy", "fiscal_balance", "monetary_policy", "policy_mix"], 2, "총수요·총공급 그래프·정책 전달 경로"),
    b("ECO-11", "경제", "비교 우위에서 무역 정책까지", "생산 가능 곡선과 비교 우위, 교역 조건, 관세가 무역 후생에 미치는 영향", ["international_trade", "comparative_advantage", "production_possibility", "terms_of_trade", "trade_policy_welfare", "fair_trade"], 2, "생산 가능 곡선·교역 전후 소비표"),
    b("ECO-12", "경제", "환율과 국제수지의 연결", "외환 시장의 수요·공급과 환율 변동이 무역·자본 이동·국제수지에 미치는 영향", ["foreign_exchange_market", "exchange_rate_effects", "cross_exchange_rate", "balance_of_payments"], 2, "외환 시장 그래프·국제 거래표"),
    b("ECO-13", "경제", "수익·위험·시간을 고려한 자산 관리", "금융 자산의 유동성·안전성·수익성과 분산 투자·복리·실질 수익률", ["financial_life", "financial_properties", "financial_return_risk", "time_value_of_money", "real_interest_return", "economic_indicators"], 2, "포트폴리오 원그래프·복리 계산표"),
    b("ECO-14", "경제", "조세 구조와 소득 재분배", "비례·누진·역진적 조세 부담과 재정 수지·복지 정책의 관계", ["tax_structure", "fiscal_balance", "welfare_policy", "social_inequality"], 2, "소득 계층별 조세 부담률 표"),

    # 법과 정치
    b("LAW-01", "법과 정치", "인권은 어떻게 권리로 확장되었는가", "자연권에서 실정법적 권리와 현대적 인권으로 확장되는 과정", ["human_rights", "rights_conceptions", "rights_history", "new_rights"], 2, "인권 선언·헌법 조항 연표"),
    b("LAW-02", "법과 정치", "헌법은 기본권을 어떻게 보장하고 제한하는가", "기본권 유형, 법치주의·권력 분립, 기본권 제한의 한계", ["constitutional_rights", "rights_categories", "rule_of_law_separation", "rights_limits"], 2, "기본권 분류표·과잉금지 심사 도식"),
    b("LAW-03", "법과 정치", "새로운 권리와 사회적 약자의 보호", "환경·안전·노동 권리와 사회적 약자 보호의 구체적 조건", ["vulnerable_human_rights", "new_rights", "environmental_rights", "labor_rights"], 2, "권리 침해 사례·구제 수단 표"),
    b("LAW-04", "법과 정치", "권리 침해에 대응하는 시민과 제도", "기본권 구제 제도와 민주적 참여·시민 불복종의 요건", ["rights_remedies", "democratic_participation", "civil_disobedience", "constitutional_rights"], 2, "침해 유형별 구제 절차도"),
    b("LAW-05", "법과 정치", "국제 사회에서 평화는 어떻게 가능한가", "국제 행위 주체와 현실주의·이상주의, 소극적·적극적 평화의 차이", ["international_peace", "international_relations", "peace_theory", "world_citizenship"], 2, "국제 행위 주체 관계망·평화 개념 비교표"),

    # 역사
    b("HIS-01", "역사", "산업화와 자본주의는 공간과 사회를 어떻게 바꾸었는가", "시간적 관점에서 자본주의·산업화·도시화와 사회 변화를 추적", ["temporal_view", "capitalism_history", "industrialization", "urbanization", "industrial_social_change"], 2, "산업 구조·도시 인구 시계열"),
    b("HIS-02", "역사", "인권 보장의 역사적 확대", "시민권에서 사회권·연대권으로 확대되는 역사적 맥락", ["rights_history", "human_rights", "constitutional_rights", "temporal_view"], 2, "권리 세대·역사 사건 연표"),
    b("HIS-03", "역사", "분단과 동아시아 갈등을 평화로 전환하기", "분단의 역사성과 동아시아 기억 갈등, 평화 구축의 조건", ["division_unification", "east_asia_conflict", "international_peace", "peace_theory"], 2, "분단·갈등 사건 지도와 연표"),

    # 융합형: A급 개념의 재노출과 영역 간 전이를 담당한다.
    b("INT-01", "융합", "하나의 사회 문제를 여러 관점으로 읽기", "시간·공간·사회·윤리 질문을 결합하되 각 관점의 판단 기준을 구분", ["integrated_view", "temporal_view", "spatial_view", "social_view", "ethical_view", "integrated_inquiry_attitudes"], 2, "관점별 질문 매트릭스"),
    b("INT-02", "융합", "기후 위기의 경제학과 정치", "환경 문제를 외부 효과로 설명하고 탄소중립·국제 협력·지속가능발전으로 해결", ["environmental_problem", "external_effects", "externality_correction", "carbon_neutrality", "climate_governance", "sustainable_development", "sdgs"], 2, "탄소 배출 비용 곡선·국제 협약 자료"),
    b("INT-03", "융합", "세계 상품의 가치 사슬과 공정성", "비교 우위·다국적 기업·지역화·공정 무역이 생산자와 지역에 미치는 영향", ["international_trade", "comparative_advantage", "multinational_corporation", "globalization", "localization", "fair_trade", "corporate_responsibility"], 2, "세계 생산 네트워크 지도·판매액 배분표"),
    b("INT-04", "융합", "저출산·고령화와 노동·복지의 재설계", "인구 구조 변화가 노동 시장·재정·복지와 세대 간 정의에 미치는 영향", ["low_birth_aging", "population_structure", "labor_market_wage", "employment_indicators", "fiscal_balance", "welfare_policy", "distributive_justice"], 2, "인구 피라미드·재정 수지 전망표"),
    b("INT-05", "융합", "인공지능 사회의 권리와 규제", "정보 격차·새로운 인권·시장 실패·기술 윤리를 결합한 규제 설계", ["fourth_industrial_revolution", "information_society", "digital_divide", "digital_citizenship", "new_rights", "technology_ethics_regulation", "information_asymmetry"], 2, "알고리즘 의사 결정 사례·규제 비교표"),
    b("INT-06", "융합", "불평등을 줄이는 정책은 언제 정당한가", "불평등 지표와 분배 정의를 바탕으로 조세·복지·적극적 우대 조치를 평가", ["social_inequality", "inequality_indicators", "justice", "rawls", "tax_structure", "welfare_policy", "affirmative_action"], 2, "분배 결과표·정책 전후 불평등 지표"),
]

# 본문 묶음에서 한 번만 등장하는 A급 개념의 두 번째 노출 위치를 수동 지정한다.
# 재노출은 새 개념 설명이 아니라 이미 배운 개념을 사례·보기에서 전이하는 용도다.
A_REINFORCEMENT = {
    "integrated_view": "INT-02",
    "meaning_of_happiness": "ETH-02",
    "conditions_happiness": "ETH-01",
    "climate_regions": "GEO-02",
    "landforms_and_life": "GEO-01",
    "cultural_change": "SOC-03",
    "acculturation": "GEO-08",
    "cultural_identity": "SOC-01",
    "cultural_regions": "GEO-09",
    "industrialization": "SOC-03",
    "urban_structure": "HIS-01",
    "rights_categories": "LAW-04",
    "vulnerable_human_rights": "INT-06",
    "division_unification": "LAW-05",
    "resource_distribution": "INT-02",
    "fossil_fuel": "INT-02",
    "opportunity_cost": "ECO-11",
    "market_principle": "ECO-07",
    "government_failure": "ECO-10",
    "financial_life": "ECO-03",
    "financial_properties": "ECO-03",
    "firm_production_cost": "ECO-06",
    "demand_supply": "ECO-06",
    "economic_surplus_efficiency": "ECO-07",
    "national_income_accounting": "ECO-10",
    "price_level_inflation": "ECO-10",
    "business_cycle": "ECO-09",
    "household_income_expenditure": "ECO-13",
    "financial_return_risk": "ECO-03",
}


AREA_ORDER = {x: i for i, x in enumerate(["윤리", "지리", "사회문화", "경제", "법과 정치", "역사", "융합"], 1)}
ROLE_WEIGHT = {"본문 중심": 4, "본문 연계": 3, "문항·보기 재노출": 2, "해설 확장": 1}


def load():
    return json.loads(CONCEPT_PATH.read_text(encoding="utf-8"))


def main():
    concepts = load()
    cmap = {c["id"]: c for c in concepts}
    all_ids = set(cmap)
    used_ids = {cid for x in BUNDLES for cid in x["concept_ids"]}
    unknown = sorted(used_ids - all_ids)
    omitted = sorted(all_ids - used_ids)
    assert not unknown, f"unknown concept ids: {unknown}"
    assert not omitted, f"omitted concept ids: {omitted}"

    placements = defaultdict(list)
    bundles = []
    for order, raw in enumerate(BUNDLES, 1):
        ids = sorted(raw["concept_ids"], key=lambda cid: (cmap[cid]["stage"], raw["concept_ids"].index(cid)))
        core_original = set(raw["concept_ids"][:raw["core_count"]])
        sequence = []
        for cid in ids:
            role = "본문 중심" if cid in core_original else "본문 연계"
            placements[cid].append({"set_id": raw["id"], "area": raw["area"], "role": role})
            c = cmap[cid]
            sequence.append({
                "order": len(sequence) + 1,
                "concept_id": cid,
                "name": c["name"],
                "stage": c["stage"],
                "stage_label": c["stage_label"],
                "importance": c["importance"],
                "role": role,
            })
        prereq = sorted({p for cid in ids for p in cmap[cid].get("prerequisites", []) if p not in ids})
        stages = Counter(cmap[cid]["stage"] for cid in ids)
        bundles.append({
            "order": order,
            **{k: v for k, v in raw.items() if k not in {"concept_ids", "core_count"}},
            "difficulty_band": "심화" if stages[3] >= 2 else "중상" if stages[3] else "기초·핵심",
            "learning_sequence": sequence,
            "core_concepts": [cid for cid in raw["concept_ids"][:raw["core_count"]]],
            "supporting_concepts": [cid for cid in raw["concept_ids"][raw["core_count"]:]],
            "assumed_prerequisites": [{"id": p, "name": cmap[p]["name"]} for p in prereq],
            "recommended_question_targets": [],
            "coverage_purpose": "독립 세트" if raw["area"] != "융합" else "영역 간 전이 및 A급 개념 재노출",
        })

    by_id = {x["id"]: x for x in bundles}

    # A급은 적어도 두 세트에서 만나게 한다. 1회뿐인 개념의 재노출 위치는
    # 위의 수동 관계표에서 결정해 특정 세트로의 기계적 쏠림을 막는다.
    for c in concepts:
        cid = c["id"]
        if c["importance"] != "A" or len({p["set_id"] for p in placements[cid]}) >= 2:
            continue
        assert cid in A_REINFORCEMENT, f"A급 수동 재노출 위치 누락: {cid}"
        target = by_id[A_REINFORCEMENT[cid]]
        assert target["id"] not in {p["set_id"] for p in placements[cid]}, (cid, target["id"])
        target["recommended_question_targets"].append({
            "concept_id": cid,
            "name": c["name"],
            "role": "문항·보기 재노출",
            "reason": "A급 개념 최소 2회 노출 보장; 인과·적용·비교 관계가 자연스러운 세트로 수동 배정",
        })
        placements[cid].append({"set_id": target["id"], "area": target["area"], "role": "문항·보기 재노출"})

    # C급 중 심화 경제에서만 강화된 개념은 해설에서 기초 개념과의 연결을 명시한다.
    for c in concepts:
        cid = c["id"]
        if c["importance"] != "C" or c["stage"] < 3:
            continue
        home = placements[cid][0]["set_id"]
        by_id[home].setdefault("explanation_extensions", []).append({
            "concept_id": cid,
            "name": c["name"],
            "role": "해설 확장",
            "instruction": "본문의 기초·핵심 개념에서 이 심화 개념이 도출되는 이유를 해설에 2~4문장으로 연결",
        })
        placements[cid].append({"set_id": home, "area": by_id[home]["area"], "role": "해설 확장"})

    # 개념별 최종 배분표
    coverage = []
    for c in concepts:
        ps = placements[c["id"]]
        unique_sets = sorted({p["set_id"] for p in ps})
        role_counts = Counter(p["role"] for p in ps)
        target = 2 if c["importance"] == "A" else 1
        coverage.append({
            "concept_id": c["id"],
            "name": c["name"],
            "primary_domain": c["primary_domain"],
            "domains": c["domains"],
            "stage": c["stage"],
            "stage_label": c["stage_label"],
            "depth_band": c["depth_band"],
            "importance": c["importance"],
            "minimum_set_exposure": target,
            "actual_set_exposure": len(unique_sets),
            "placements": ps,
            "role_counts": dict(role_counts),
            "coverage_status": "충족" if len(unique_sets) >= target else "미달",
            "prerequisites": c.get("prerequisites", []),
            "distractor_candidates": c.get("distractor_boundaries", [])[:4],
        })

    # 검증
    violations = []
    for c in coverage:
        if c["coverage_status"] != "충족":
            violations.append({"type": "노출 횟수 미달", "concept_id": c["concept_id"]})
    for bundle in bundles:
        seq = bundle["learning_sequence"]
        if [x["stage"] for x in seq] != sorted(x["stage"] for x in seq):
            violations.append({"type": "묶음 내부 학습 단계 역전", "set_id": bundle["id"]})
        if not seq:
            violations.append({"type": "빈 묶음", "set_id": bundle["id"]})
    validation = {
        "status": "PASS" if not violations else "FAIL",
        "concept_count": len(concepts),
        "covered_concept_count": sum(bool(x["placements"]) for x in coverage),
        "omitted_concepts": omitted,
        "unknown_concepts": unknown,
        "set_count": len(bundles),
        "sets_by_area": dict(Counter(x["area"] for x in bundles)),
        "importance_distribution": dict(Counter(c["importance"] for c in concepts)),
        "stage_distribution": dict(Counter(c["stage_label"] for c in concepts)),
        "coverage_by_importance": {
            grade: {
                "concepts": sum(c["importance"] == grade for c in coverage),
                "minimum_exposures": 2 if grade == "A" else 1,
                "all_satisfied": all(c["coverage_status"] == "충족" for c in coverage if c["importance"] == grade),
                "total_placements": sum(c["actual_set_exposure"] for c in coverage if c["importance"] == grade),
            }
            for grade in ["A", "B", "C"]
        },
        "role_distribution": dict(Counter(p["role"] for c in coverage for p in c["placements"])),
        "bundles_with_external_prerequisites": sum(bool(x["assumed_prerequisites"]) for x in bundles),
        "violations": violations,
    }
    assert validation["status"] == "PASS", validation

    (OUT / "통합사회_출제용_개념묶음_지도.json").write_text(json.dumps(bundles, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "통합사회_전체범위_출제배분표.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "통합사회_출제배분_검증.json").write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding="utf-8")

    # 개념 묶음 지도 Markdown
    lines = [
        "# 통합사회 출제용 개념 묶음 지도", "",
        "> 교과서 목차 순서가 아니라 윤리·지리·사회문화·경제·법과 정치·역사·융합의 설명 구조로 174개 개념을 재편한 지문 설계 전 단계 자료이다.", "",
        "## 설계 원칙", "",
        "- 한 묶음은 한 지문에서 인과·조건·비교·과정 관계로 함께 설명할 수 있는 개념으로 구성한다.",
        "- 묶음 내부 순서는 기초(1) → 핵심(2) → 심화(3)를 지킨다.",
        "- ‘본문 중심’은 지문의 주된 설명 대상, ‘본문 연계’는 중심 개념을 설명·제한·확장하는 개념이다.",
        "- 융합형은 개별 영역 학습 이후 개념을 새로운 문제에 전이하고 A급 개념을 재노출하는 역할이다.",
        "- 50개는 전 범위용 후보 묶음 수다. 이후 실제 제작에서 두 묶음을 한 세트로 합칠 수 있지만, 합칠 때도 이 배분표의 개념 역할은 보존한다.",
        "- 외부 선행 개념은 반드시 앞 세트를 뜻하지 않는다. 독립 세트로 출제할 때 지문에서 짧게 재정의해야 하는 배경 개념이다.", "",
        f"## 전체 구성: {len(bundles)}개 묶음", "",
    ]
    for area in AREA_ORDER:
        subset = [x for x in bundles if x["area"] == area]
        lines += [f"## {area} — {len(subset)}개", ""]
        for x in subset:
            lines += [f"### {x['id']}｜{x['title']}", "", f"- 초점: {x['focus']}", f"- 난도 기반: {x['difficulty_band']}", f"- 권장 자료: {x['recommended_visual']}", "- 학습·설명 순서:"]
            for c in x["learning_sequence"]:
                lines.append(f"  {c['order']}. [{c['stage_label']}/{c['importance']}] **{c['name']}** — {c['role']}")
            if x["assumed_prerequisites"]:
                lines.append("- 독립 출제 시 재정의할 선행 개념: " + ", ".join(p["name"] for p in x["assumed_prerequisites"]))
            if x["recommended_question_targets"]:
                lines.append("- 문항·보기 재노출: " + ", ".join(p["name"] for p in x["recommended_question_targets"]))
            exts = x.get("explanation_extensions", [])
            if exts:
                lines.append("- 해설에서 연결할 심화 개념: " + ", ".join(p["name"] for p in exts))
            lines.append("")
    (OUT / "통합사회_출제용_개념묶음_지도.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # 전체 범위 배분표 Markdown
    lines = [
        "# 통합사회 전체 범위 출제 배분표", "",
        "> 174개 개념이 어느 세트의 본문·문항·해설에서 학습되는지를 추적하는 누락 방지표이다.", "",
        "## 배분 규칙", "",
        "- A급: 서로 다른 세트에서 최소 2회 노출", "- B급: 최소 1회 본문 노출", "- C급: 최소 1회 본문 노출하고, 3단계 심화 개념은 해설 연결 지시 추가", "- 같은 세트에서 본문과 해설에 반복되어도 세트 노출 횟수는 1회로 센다.", "",
        "## 요약", "",
        f"- 개념 {len(coverage)}개 전부 배정", f"- 세트 묶음 {len(bundles)}개: " + ", ".join(f"{k} {v}" for k, v in validation["sets_by_area"].items()),
        f"- 중요도: A {validation['importance_distribution']['A']} / B {validation['importance_distribution']['B']} / C {validation['importance_distribution']['C']}",
        f"- 검증: **{validation['status']}** — 누락 0, 노출 미달 0, 묶음 내부 단계 역전 0", "",
    ]
    for area in ["융합", "윤리", "지리", "사회문화", "경제", "법과 정치", "역사"]:
        subset = [c for c in coverage if c["primary_domain"] == area]
        if not subset:
            continue
        lines += [f"## 주 영역: {area}", "", "|단계|등급|개념|배치 세트와 역할|노출|상태|", "|---:|:---:|---|---|---:|:---:|"]
        for c in sorted(subset, key=lambda z: (z["stage"], -z["actual_set_exposure"], z["name"])):
            ps = "; ".join(f"{p['set_id']}({p['role']})" for p in c["placements"])
            lines.append(f"|{c['stage']} {c['stage_label']}|{c['importance']}|{c['name']}|{ps}|{c['actual_set_exposure']}/{c['minimum_set_exposure']}|{c['coverage_status']}|")
        lines.append("")
    (OUT / "통합사회_전체범위_출제배분표.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # 검증 Markdown
    lines = [
        "# 통합사회 출제 배분 검증", "", f"## 결과: {validation['status']}", "",
        f"- 원본 개념: {validation['concept_count']}", f"- 배정 개념: {validation['covered_concept_count']}", "- 누락 개념: 0", "- 알 수 없는 개념 ID: 0", f"- 출제 묶음: {validation['set_count']}", "- 묶음 내부 기초→핵심→심화 순서 역전: 0", "",
        "## 중요도별 노출", "",
    ]
    for grade in ["A", "B", "C"]:
        x = validation["coverage_by_importance"][grade]
        lines.append(f"- {grade}: {x['concepts']}개, 최소 {x['minimum_exposures']}세트, 실제 총 {x['total_placements']}세트 배치, 전부 충족={x['all_satisfied']}")
    lines += ["", "## 영역별 묶음", "", *[f"- {k}: {v}개" for k, v in validation["sets_by_area"].items()], "", "## 주의", "", "- 이 배분표는 지문·문항 생성 전의 범위 설계다. 실제 생성 이후에는 ‘계획상 배치’가 아니라 본문과 문항에 개념이 실현되었는지 다시 검사해야 한다."]
    (OUT / "통합사회_출제배분_검증.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps(validation, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
