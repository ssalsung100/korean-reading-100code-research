#!/usr/bin/env python3
"""Record the completed visual audit of all question-linked Economics images."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "자료/심화경제_문항이미지/manifest.json"
QUESTIONS = ROOT / "분석/심화경제_문항_정규화.json"
OUT_JSON = ROOT / "분석/심화경제_이미지_전수판독.json"
OUT_MD = ROOT / "분석/심화경제_이미지_전수판독.md"
REL_JSON = ROOT / "data/economics_detailed_relations.json"


RELATIONS = {
    "activity_types": ("경제 활동 유형", ["economic_activity_flow"], "생산은 부가 가치를 만들고, 분배는 생산 참여의 대가를 주고받으며, 소비는 효용을 얻는다."),
    "circular_flow": ("국민 경제 순환", ["economic_activity_flow", "economic_agent_objectives"], "가계·기업·정부와 생산물·생산 요소 시장 사이에서 실물 흐름과 화폐 흐름은 반대 방향으로 대응한다."),
    "choice_cost": ("합리적 선택의 계산", ["rational_choice", "opportunity_cost"], "선택의 기회비용은 명시적 비용과 포기한 대안의 순편익을 함께 반영하고, 순편익이 가장 큰 대안을 고른다."),
    "sunk_cost": ("매몰 비용 배제", ["rational_choice"], "이미 지출되어 회수할 수 없는 비용은 이후의 합리적 선택에서 제외한다."),
    "economic_system": ("경제 체제 비교", ["economic_systems"], "시장·계획·전통 경제는 자원 배분 기구, 소유권, 유인, 자유와 형평의 강조 정도로 구분한다."),
    "consumer_budget": ("예산 제약과 효용", ["consumer_choice_budget", "marginal_analysis"], "예산선 위 소비 조합 중 총효용이 가장 큰 조합을 선택하며 가격·소득 변화는 선택 가능 집합을 바꾼다."),
    "firm_optimum": ("생산량과 이윤 극대화", ["firm_production_cost", "marginal_analysis"], "총수입과 총비용의 차이가 최대인 생산량은 추가 수입과 추가 비용의 비교로 판정할 수 있다."),
    "tax_schedule": ("조세 함수와 부담률", ["tax_structure", "fiscal_balance"], "과세 표준에 따른 세액의 기울기와 평균 세율의 변화로 비례·누진·역진 구조를 판별한다."),
    "labor_market": ("노동 시장 균형", ["labor_market_wage", "demand_supply_shift"], "노동 수요·공급의 이동은 균형 임금과 고용량을 바꾸며 두 곡선이 함께 움직이면 한 결과가 불확정일 수 있다."),
    "market_shift": ("수요·공급 변동", ["demand_supply", "demand_supply_shift"], "곡선 자체의 이동과 곡선 위 이동을 구분하고, 균형 가격·거래량의 방향을 원인별로 추론한다."),
    "simultaneous_shift": ("수요·공급 동시 변동", ["simultaneous_market_shift"], "수요와 공급이 동시에 변하면 방향이 같은 변수만 확정되고 다른 변수는 이동 폭에 따라 달라진다."),
    "elasticity": ("탄력성과 총수입", ["elasticity"], "가격 변화율 대비 수량 변화율로 반응 정도를 비교하며 탄력성에 따라 가격 변화와 총수입의 관계가 달라진다."),
    "price_control": ("가격 규제", ["price_regulation", "economic_surplus_efficiency"], "균형 아래의 최고 가격은 초과 수요를, 균형 위의 최저 가격은 초과 공급을 만들고 실제 거래량은 짧은 쪽으로 제한된다."),
    "tax_subsidy_welfare": ("조세·보조금과 잉여", ["tax_subsidy_incidence", "economic_surplus_efficiency"], "조세·보조금은 소비자 지불 가격과 생산자 수취 가격의 쐐기를 만들며 잉여·재정 수입·후생 손실을 재배분한다."),
    "externality": ("외부 효과 교정", ["externality_correction"], "사적 곡선과 사회적 곡선의 차이로 과다·과소 생산을 판정하고 조세·보조금으로 사회적 최적에 접근한다."),
    "gdp_accounting": ("국민소득과 GDP", ["national_income_accounting"], "최종재 가치, 부가 가치, 생산·분배·지출 접근은 중복 계산을 피하면 동일한 국민소득을 가리킨다."),
    "nominal_real": ("명목·실질 지표 변환", ["nominal_real_indicators", "price_level_inflation"], "명목 GDP는 가격과 수량을 모두 반영하고 실질 GDP는 기준 연도 가격으로 수량 변화만 분리한다."),
    "employment": ("고용 지표의 분모", ["employment_indicators"], "실업률은 경제 활동 인구, 고용률은 15세 이상 인구를 분모로 하므로 동일한 인구 이동도 지표에 다르게 반영된다."),
    "discouraged_worker": ("실망 실업자 효과", ["discouraged_worker_effect"], "실업자가 구직을 포기해 비경제 활동 인구가 되면 고용이 개선되지 않아도 실업률이 하락할 수 있다."),
    "inflation": ("물가와 인플레이션", ["price_level_inflation", "inflation_types"], "총수요 증가는 물가와 실질 산출을 함께 높이고 총공급 감소는 물가 상승과 산출 감소를 함께 일으킬 수 있다."),
    "ad_as": ("총수요·총공급 균형", ["aggregate_demand_supply", "business_cycle"], "충격이 총수요와 총공급 중 어디에 작용하는지에 따라 물가와 실질 GDP의 조합이 달라진다."),
    "policy": ("경기 안정화 정책", ["fiscal_policy", "monetary_policy", "policy_mix"], "정부 지출·조세는 재정 경로로, 기준 금리·국공채는 통화 경로로 총수요에 영향을 주며 정책 조합은 강화·상쇄될 수 있다."),
    "ppf_trade": ("생산 가능 곡선과 무역", ["production_possibility", "comparative_advantage", "terms_of_trade"], "생산 가능 곡선의 기울기는 기회비용이며 교환 비율이 양국 기회비용 사이에 있어야 양국 모두 이익을 얻는다."),
    "trade_policy": ("국제 가격과 무역 정책", ["trade_policy_welfare"], "국제 가격과 국내 자급 균형 가격의 차이가 수출입 방향을 정하고 관세·보조금·수입 제한이 국내 가격과 잉여를 바꾼다."),
    "forex": ("외환 수요·공급과 환율", ["foreign_exchange_market", "exchange_rate_effects"], "외화 수요·공급의 이동은 환율과 외화 거래량을 바꾸며 통화 가치, 수출입 부담과 반대 방향으로 연결된다."),
    "cross_rate": ("교차 환율", ["cross_exchange_rate"], "공통 기준 통화에 대한 두 환율을 결합하여 제3국 통화 사이의 교환 비율과 가치 변화를 계산한다."),
    "balance_payments": ("국제수지 구성", ["balance_of_payments"], "상품·서비스·본원 소득·이전 소득 수지를 구분하고 거래의 방향에 따라 수입과 지급을 부호화한다."),
    "household_finance": ("가계 소득·지출", ["household_income_expenditure"], "경상·비경상 소득과 소비·비소비 지출을 구분하고 처분 가능 소득 및 저축을 계산한다."),
    "portfolio": ("금융 자산과 포트폴리오", ["financial_properties", "financial_return_risk"], "예금·채권·주식의 권리 구조와 안전성·수익성·유동성을 구분하고 자산 배분 변화를 해석한다."),
    "real_return": ("명목 수익과 실질 수익", ["real_interest_return", "time_value_of_money"], "명목 이자율에서 물가 상승의 효과를 제거해야 구매력 기준 실질 수익을 판단할 수 있다."),
}

AXES = {
    "activity_types": ("해당 없음", "해당 없음", "정의·사례의 분류"),
    "circular_flow": ("경제 주체·시장", "해당 없음", "실물 화살표와 화폐 화살표의 방향"),
    "choice_cost": ("대안·시점", "편익·명시적/암묵적 비용", "대안별 수치와 선택 결과"),
    "sunk_cost": ("선택 시점", "회수 가능성", "이미 지출한 비용과 앞으로의 편익·비용 분리"),
    "economic_system": ("시장 자율·형평 등 비교축", "강도·해당 여부", "국가·체제의 상대 위치와 분류 경로"),
    "consumer_budget": ("X재 수량", "Y재 수량", "예산선 위 소비 조합과 조합별 효용"),
    "firm_optimum": ("생산량·과세 대상 소득", "비용·수입·비율", "총량 곡선/점과 추가량의 변화"),
    "tax_schedule": ("과세 대상 소득", "세액·보조금", "구간별 기울기와 평균 부담률"),
    "labor_market": ("노동량", "임금", "노동 수요·공급 곡선 및 이동"),
    "market_shift": ("수량", "가격", "수요·공급 곡선 이동과 새 균형"),
    "simultaneous_shift": ("수량", "가격", "두 곡선의 동시 이동과 가능한 균형 영역"),
    "elasticity": ("수량·변화율", "가격·변화율", "가격 변화에 대한 수량 반응의 상대 크기"),
    "price_control": ("수량", "가격", "규제 가격선·수요량·공급량·실제 거래량"),
    "tax_subsidy_welfare": ("수량", "가격", "가격 쐐기와 소비자/생산자 잉여 영역"),
    "externality": ("수량", "가격·비용·편익", "사적 곡선과 사회적 곡선 및 시장/사회 최적점"),
    "gdp_accounting": ("경제 주체·재화 흐름", "부가 가치·소득", "GDP 포함 여부와 생산·분배·지출 대응"),
    "nominal_real": ("연도·실질 GDP", "명목 GDP·물가", "가격 효과와 수량 효과의 분해"),
    "employment": ("연도·경제 활동 참가율", "고용률·실업률·인구", "취업/실업/비경제 활동 상태와 서로 다른 분모"),
    "discouraged_worker": ("노동시장 상태 이동", "실업률", "실업자에서 비경제 활동 인구로의 이동"),
    "inflation": ("연도·실질 GDP 증가율", "물가 상승률", "물가와 산출의 동행·역행 조합"),
    "ad_as": ("실질 GDP", "물가", "총수요·총공급 곡선과 균형점 이동"),
    "policy": ("정부 지출·지급 준비율", "국공채·기준 금리", "정책 수단의 확대/긴축 방향과 조합"),
    "ppf_trade": ("X재 수량", "Y재 수량", "생산 가능선의 기울기·특화점·교역 후 소비점"),
    "trade_policy": ("국내 수량", "국내 가격·국제 가격", "국내 수요/공급, 수입·수출량, 관세·보조금 영역"),
    "forex": ("달러의 양", "원/달러 환율", "외화 수요·공급 이동과 환율·거래량"),
    "cross_rate": ("을국 통화량", "병국 통화량", "원점을 지나는 교환 비율선과 통화 가치"),
    "balance_payments": ("연도·상품 수출액", "수지·상품 수입액", "경상 수지 항목의 양·음과 거래 방향"),
    "household_finance": ("소득·지출 항목", "금액", "경상/비경상 소득과 소비/비소비 지출의 합계"),
    "portfolio": ("자산 유형·수익성", "비중·안전성·유동성", "금융 상품의 집합 관계와 포트폴리오 구성"),
    "real_return": ("연도", "명목 이자율·물가 상승률", "명목 수익에서 물가 효과를 제거한 구매력 변화"),
}


def relation_for(index: int) -> str:
    if index == 1: return "activity_types"
    if 2 <= index <= 14: return "circular_flow"
    if 15 <= index <= 18 or 20 <= index <= 24: return "choice_cost"
    if index == 19: return "sunk_cost"
    if 25 <= index <= 31: return "economic_system"
    if index == 32: return "consumer_budget"
    if 33 <= index <= 36: return "firm_optimum"
    if 37 <= index <= 39: return "tax_schedule"
    if 40 <= index <= 44 or index == 47: return "labor_market"
    if index in {45, 49, 50, 51, 54}: return "market_shift"
    if index == 46: return "elasticity"
    if index in {48, 52}: return "firm_optimum"
    if index == 53: return "simultaneous_shift"
    if index in {55, 57, 66, 67, 68, 69, 70, 72, 73, 74}: return "price_control"
    if index in {56, 71, 75}: return "tax_subsidy_welfare"
    if 58 <= index <= 65: return "externality"
    if index == 76: return "price_control"
    if 77 <= index <= 82: return "circular_flow"
    if index in {83, 84}: return "gdp_accounting"
    if index in {85, 86, 87, 88, 89}: return "nominal_real"
    if 90 <= index <= 93 or index == 95: return "employment"
    if index == 94: return "discouraged_worker"
    if index == 96: return "inflation"
    if index in {97, 98, 99, 100, 101}: return "inflation"
    if 102 <= index <= 109 or index == 111: return "ad_as"
    if index == 110 or 112 <= index <= 116: return "policy"
    if 117 <= index <= 122: return "ppf_trade"
    if 123 <= index <= 133: return "trade_policy"
    if 134 <= index <= 138 or 140 <= index <= 145: return "forex"
    if index == 139: return "cross_rate"
    if 146 <= index <= 148: return "balance_payments"
    if 149 <= index <= 150: return "household_finance"
    if 151 <= index <= 154 or index == 156: return "portfolio"
    if index == 155: return "real_return"
    raise ValueError(index)


def visual_form(index: int) -> str:
    if index in {1, 2, 3, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 28, 30, 31, 35, 36, 37, 47, 52, 76, 83, 84, 93, 94, 98, 100, 101, 112, 114, 115, 116, 144, 145, 149, 150, 151, 154, 156}:
        return "설명·분류 도식"
    if index in {4, 5, 6, 7, 8, 9, 10, 11, 12, 77, 78, 79, 80, 81, 82}:
        return "순환·흐름도"
    if index in {17, 26, 38, 39, 85, 86, 88, 91, 92, 96, 97, 117, 147, 148, 153}:
        return "표·막대·복합 자료"
    return "좌표·곡선 그래프"


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    questions = {q["id"]: q for q in json.loads(QUESTIONS.read_text(encoding="utf-8"))}
    audited = []
    for index, row in enumerate(manifest, 1):
        relation_id = relation_for(index)
        title, concepts, rule = RELATIONS[relation_id]
        x_axis, y_axis, encoding = AXES[relation_id]
        audited.append(
            {
                **row,
                "audit_index": index,
                "inspection_status": "원본 육안 판독 완료",
                "visual_form": visual_form(index),
                "relation_id": relation_id,
                "relation_name": title,
                "linked_concepts": concepts,
                "key_relation": rule,
                "x_axis_or_basis": x_axis,
                "y_axis_or_measure": y_axis,
                "visual_encoding": encoding,
                "generation_use": f"{title}의 원인→그래프 변화→결과를 묻는 자료 문항 또는 보기 적용 문항",
                "question_text_preview": questions[row["question_id"]]["text"][:180],
                "reuse_status": "원본·PNG 사용 가능(외부 배포 시 출판물 이용 권한 별도 확인)",
            }
        )

    payload = {
        "audit_scope": {"questions": len({x["question_id"] for x in audited}), "images": len(audited)},
        "status": "complete",
        "method": "13개 접촉표 전수 판독 후 세부 관계 분류; 문항 텍스트와 원본 PNG 교차 확인",
        "relations": [
            {"id": k, "name": v[0], "parent_concepts": v[1], "rule": v[2], "x_axis_or_basis": AXES[k][0], "y_axis_or_measure": AXES[k][1], "visual_encoding": AXES[k][2]}
            for k, v in RELATIONS.items()
        ],
        "images": audited,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REL_JSON.write_text(json.dumps(payload["relations"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# 심화 경제 이미지 전수 판독 장부",
        "",
        f"- 판독 문항: {payload['audit_scope']['questions']}개",
        f"- 판독 이미지: {payload['audit_scope']['images']}개",
        "- 상태: 원본 육안 판독 완료",
        "- 방법: 13개 접촉표로 전수 확인하고 문항 텍스트·원본 PNG와 교차 판정",
        "- 재사용: 자료실의 원본과 PNG를 문제 제작에 연결할 수 있다. 외부 배포물은 원 출판물 이용 권한을 별도로 확인한다.",
        "",
        "## 새로 확보한 세부 관계",
        "",
        "| 관계 | 상위 개념 | 판독 규칙 |",
        "|---|---|---|",
    ]
    for rid, (name, parents, rule) in RELATIONS.items():
        lines.append(f"| {name} | {', '.join(parents)} | {rule} |")
    lines += ["", "## 이미지별 판독", "", "| # | 문항 | 형식 | 판독 관계 | 원본 | PNG |", "|---:|---|---|---|---|---|"]
    for row in audited:
        lines.append(
            f"| {row['audit_index']} | {row['question_id']} | {row['visual_form']} | {row['relation_name']} | "
            f"[{Path(row['original_path']).name}](../{row['original_path']}) | "
            f"[{Path(row['png_path']).name}](../{row['png_path']}) |"
        )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"audited {len(audited)} images in {len({x['question_id'] for x in audited})} questions")


if __name__ == "__main__":
    main()
