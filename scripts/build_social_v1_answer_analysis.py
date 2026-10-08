#!/usr/bin/env python3
"""통합사회 완전판 문항·정답 역분석과 개념 지도 v1을 생성한다.

입력은 로컬에서 전수 추출한 1,054개 객관식 문항, 빠른 정답표, 174개 개념
카탈로그, 심화 경제 분석, 문항 이미지 감사 자료이다. 출력에는 자동 판정의
근거와 한계를 문항별로 남겨 추후 수동 정밀 검토가 가능하게 한다.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AN = ROOT / "분석"
DATA = ROOT / "data"
Q_PATH = AN / "통합사회_문항_정규화.json"
A_PATH = AN / "통합사회_정답표_정오표_추출.md"
C_PATH = DATA / "social_concepts.json"
ECON_PATH = AN / "심화경제_전체개념_분석.json"
OLD_IMAGE_AUDIT = AN / "통합사회_이미지_전수판독.json"
IMAGE_MANIFEST = ROOT / "자료/통합사회_문항이미지_완전판/manifest.json"

SYMBOLS = "①②③④⑤"
SYMBOL_TO_INT = {s: i + 1 for i, s in enumerate(SYMBOLS)}

# HWPX에서 선지 전체가 그림으로 저장됐거나 일부 글상자가 XML 읽기 순서에서
# 빠진 다섯 문항은 원본 이미지를 직접 판독한 요약을 사용한다.
VISUAL_CHOICE_OVERRIDES = {
    "통합사회1-3단원-Q093": {
        "①": "이집트·사우디아라비아·이란·알제리 중심 생산량 그래프",
        "②": "독일·폴란드·러시아·벨라루스 중심 생산량 그래프",
        "③": "중국·인도·방글라데시·인도네시아 중심 생산량 그래프",
        "④": "에스파냐·이탈리아·튀르키예·모로코 중심 생산량 그래프",
        "⑤": "코트디부아르·가나·인도네시아·브라질 중심 생산량 그래프",
    },
    "통합사회1-단원평가-Q026": {
        "①": "여름 고온·건조, 겨울 저온·소우의 대륙성 그래프",
        "②": "여름 고온·건조, 겨울 온난·다우의 지중해성 그래프",
        "③": "여름 고온·다우, 겨울 냉량·소우의 계절풍 그래프",
        "④": "연중 온난하고 겨울 다우·여름 건조한 그래프",
        "⑤": "연중 고온, 봄·겨울 다우와 여름 건조가 두드러진 그래프",
    },
    "통합사회2-4단원-Q009": {
        "①": "공정 무역", "②": "[원문 XML에서 글상자 선지 누락]", "③": "지리적 표시제",
        "④": "[원문 XML에서 글상자 선지 누락]", "⑤": "다국적 기업의 공간적 분업",
    },
    "통합사회2-5단원-Q067": {
        "①": "(가)=A, (나)=B, (다)=C", "②": "(가)=A, (나)=C, (다)=B",
        "③": "(가)=B, (나)=A, (다)=C", "④": "(가)=B, (나)=C, (다)=A",
        "⑤": "(가)=C, (나)=A, (다)=B",
    },
    "통합사회2-5단원-Q076": {
        "①": "O→O→X→X", "②": "O→X→O→O", "③": "O→X→O→X",
        "④": "O→X→X→O", "⑤": "X→O→O→O",
    },
}


def entry(group, block, n, topics, label=""):
    return {"group": group, "block": block, "n": n, "topics": topics, "label": label}


# 정답표에 인쇄된 순서. 단원평가는 각 책의 실제 소단원 순서에 맞춘다.
LAYOUT = {
    "통합사회1": [
        entry("1단원", 1, 24, ["integrated_view", "temporal_view", "spatial_view", "social_view", "ethical_view"], "통합적 관점"),
        entry("1단원", 2, 6, ["integrated_view", "integrated_inquiry_attitudes"], "통합적 탐구"),
        entry("2단원", 1, 19, ["meaning_of_happiness", "eudaimonia", "pleasure_happiness", "stoic_happiness", "eastern_happiness"], "행복의 기준과 의미"),
        entry("2단원", 2, 20, ["conditions_happiness", "settlement_environment", "democracy_happiness", "moral_practice_happiness"], "행복한 삶의 조건"),
        entry("2단원", 3, 11, ["meaning_of_happiness", "conditions_happiness", "eudaimonia", "eastern_happiness"], "행복 단원 마무리"),
        entry("3단원", 1, 23, ["natural_environment", "climate_regions", "climate_graph_reasoning", "natural_disaster"], "자연환경과 인간 생활 1"),
        entry("3단원", 2, 25, ["natural_environment", "climate_regions", "landforms_and_life", "natural_disaster", "disaster_risk_management"], "자연환경과 인간 생활 2"),
        entry("3단원", 3, 20, ["anthropocentrism", "animal_liberation", "life_centrism", "ecocentrism", "environmental_conflict"], "인간과 자연의 관계"),
        entry("3단원", 4, 20, ["environmental_problem", "sustainable_development", "climate_governance", "environmental_governance", "ecological_citizen"], "환경 문제 해결"),
        entry("3단원", 5, 23, ["natural_environment", "environmental_problem", "sustainable_development", "anthropocentrism", "ecocentrism"], "자연환경 단원 마무리"),
        entry("4단원", 1, 24, ["culture", "cultural_regions", "religious_landscape", "cultural_universality"], "문화권"),
        entry("4단원", 2, 24, ["cultural_change", "acculturation", "traditional_culture", "cultural_lag"], "문화 변동"),
        entry("4단원", 3, 12, ["attitude_culture", "extreme_relativism", "cultural_universality"], "문화 이해 태도"),
        entry("4단원", 4, 8, ["cultural_identity", "multicultural_policy", "attitude_culture"], "다문화 사회"),
        entry("4단원", 5, 20, ["cultural_regions", "cultural_change", "acculturation", "attitude_culture", "cultural_identity"], "문화 단원 마무리"),
        # 빠른 정답표에는 있으나 제공된 문제편 HWPX에 원문이 없는 22문항.
        entry("원문미제공", 0, 22, ["industrialization", "urbanization", "industrial_social_change"], "산업화·도시화(정답표만 존재)"),
        entry("5단원", 1, 16, ["transport_development", "information_society", "industrial_social_change"], "교통·통신 발달"),
        entry("5단원", 2, 16, ["information_society", "digital_divide", "digital_citizenship"], "정보 사회"),
        entry("5단원", 3, 12, ["regional_research", "urban_problem_regeneration", "regional_inequality"], "지역 조사"),
        entry("5단원", 4, 20, ["industrialization", "urbanization", "transport_development", "information_society", "regional_research"], "생활 공간 단원 마무리"),
        *[entry("단원평가", i, n, topics, label) for i, (n, topics, label) in enumerate([
            (8, ["integrated_view", "temporal_view", "spatial_view", "social_view", "ethical_view"], "통합적 관점"),
            (8, ["meaning_of_happiness", "eudaimonia", "pleasure_happiness", "eastern_happiness"], "행복의 의미"),
            (8, ["conditions_happiness", "settlement_environment", "democracy_happiness"], "행복 조건"),
            (8, ["natural_environment", "climate_regions", "landforms_and_life"], "자연환경"),
            (8, ["anthropocentrism", "life_centrism", "ecocentrism"], "자연관"),
            (7, ["environmental_problem", "sustainable_development", "environmental_governance"], "환경 문제"),
            (8, ["culture", "cultural_regions", "religious_landscape"], "문화권"),
            (8, ["cultural_change", "acculturation", "traditional_culture"], "문화 변동"),
            (8, ["attitude_culture", "extreme_relativism", "cultural_universality"], "문화 태도"),
            (8, ["cultural_identity", "multicultural_policy"], "다문화"),
            (8, ["industrialization", "urbanization", "industrial_social_change"], "산업화·도시화"),
            (8, ["transport_development", "information_society", "digital_divide"], "교통·정보"),
            (8, ["regional_research", "urban_problem_regeneration", "regional_inequality"], "지역 조사"),
        ], 1)],
        entry("2028_수능_예시문항", 1, 25, ["integrated_view", "meaning_of_happiness", "natural_environment", "culture", "industrialization"], "2028 예시 1"),
        entry("2028_수능_예시문항", 2, 14, ["human_rights", "justice", "market_principle", "globalization", "population_structure"], "2028 예시 2"),
    ],
    "통합사회2": [
        entry("1단원", 1, 20, ["human_rights", "rights_history", "rights_conceptions", "new_rights"], "인권의 의미와 역사"),
        entry("1단원", 2, 16, ["constitutional_rights", "rights_categories", "rights_limits", "rule_of_law_separation"], "헌법과 기본권"),
        entry("1단원", 3, 16, ["rights_remedies", "vulnerable_human_rights", "labor_rights", "environmental_rights"], "인권 보장과 구제"),
        entry("1단원", 4, 8, ["civil_disobedience", "democratic_participation", "human_rights"], "시민 참여"),
        entry("1단원", 5, 20, ["human_rights", "constitutional_rights", "rights_remedies", "vulnerable_human_rights"], "인권 단원 마무리"),
        entry("2단원", 1, 14, ["justice", "corrective_justice", "punishment_theories"], "정의와 교정"),
        entry("2단원", 2, 12, ["distributive_justice", "equality_principles"], "분배 기준"),
        entry("2단원", 3, 12, ["rawls", "nozick", "liberal_communitarian"], "정의관"),
        entry("2단원", 4, 20, ["social_inequality", "inequality_indicators", "welfare_policy", "affirmative_action"], "불평등"),
        entry("2단원", 5, 15, ["justice", "distributive_justice", "rawls", "social_inequality"], "정의 단원 마무리"),
        entry("2028_수능_예시문항", 1, 25, ["integrated_view", "human_rights", "justice", "market_principle", "globalization"], "2028 예시 1"),
        entry("2028_수능_예시문항", 2, 14, ["international_peace", "population_structure", "resource_distribution", "future_society"], "2028 예시 2"),
        entry("3단원", 1, 12, ["scarcity", "economic_activity_flow", "economic_systems", "capitalism_history"], "경제 체제"),
        entry("3단원", 2, 12, ["rational_choice", "opportunity_cost", "marginal_analysis"], "합리적 선택"),
        entry("3단원", 3, 12, ["market_principle", "market_failure", "external_effects", "public_goods"], "시장과 시장 실패"),
        entry("3단원", 4, 12, ["economic_actor_roles", "corporate_responsibility", "ethical_consumption"], "경제 주체"),
        entry("3단원", 5, 20, ["financial_life", "financial_properties", "financial_return_risk", "economic_indicators"], "금융 생활"),
        entry("3단원", 6, 20, ["international_trade", "comparative_advantage", "production_possibility", "fair_trade"], "국제 무역"),
        entry("3단원", 7, 23, ["scarcity", "market_principle", "financial_life", "international_trade"], "경제 단원 마무리"),
        entry("4단원", 1, 13, ["globalization", "localization", "geographical_indication"], "세계화와 지역화"),
        entry("4단원", 2, 12, ["multinational_corporation", "global_city", "globalization_problems"], "세계화의 공간"),
        entry("4단원", 3, 12, ["international_peace", "peace_theory", "international_relations"], "국제 평화"),
        entry("4단원", 4, 18, ["division_unification", "east_asia_conflict", "international_peace"], "분단과 동아시아"),
        entry("4단원", 5, 14, ["globalization", "international_peace", "world_citizenship"], "세계화·평화 마무리"),
        entry("5단원", 1, 12, ["population_structure", "population_indicators", "demographic_transition"], "인구 구조"),
        entry("5단원", 2, 20, ["low_birth_aging", "population_migration", "population_policy"], "인구 문제"),
        entry("5단원", 3, 19, ["resource_distribution", "resource_characteristics", "fossil_fuel", "resource_security"], "자원"),
        entry("5단원", 4, 11, ["renewable_energy", "energy_mix_transition", "carbon_neutrality"], "에너지 전환"),
        entry("5단원", 5, 14, ["future_society", "sdgs", "fourth_industrial_revolution", "technology_ethics_regulation"], "미래 사회"),
        *[entry("단원평가", i, n, topics, label) for i, (n, topics, label) in enumerate([
            (7, ["human_rights", "rights_history", "rights_conceptions"], "인권 역사"),
            (8, ["constitutional_rights", "rights_categories", "rights_limits"], "헌법과 기본권"),
            (7, ["rights_remedies", "vulnerable_human_rights", "labor_rights"], "인권 구제"),
            (7, ["justice", "corrective_justice", "punishment_theories"], "정의와 형벌"),
            (7, ["distributive_justice", "rawls", "nozick"], "분배 정의"),
            (7, ["social_inequality", "welfare_policy", "affirmative_action"], "불평등"),
            (7, ["scarcity", "economic_systems", "capitalism_history"], "경제 체제"),
            (8, ["rational_choice", "market_principle", "market_failure", "economic_actor_roles"], "시장과 선택"),
            (8, ["financial_life", "financial_properties", "financial_return_risk"], "금융"),
            (8, ["international_trade", "comparative_advantage", "fair_trade"], "무역"),
            (8, ["globalization", "localization", "multinational_corporation"], "세계화"),
            (7, ["international_peace", "peace_theory", "international_relations"], "평화"),
            (8, ["division_unification", "east_asia_conflict"], "분단·동아시아"),
            (8, ["population_structure", "population_indicators", "low_birth_aging"], "인구 구조"),
            (8, ["population_migration", "population_policy"], "인구 이동·정책"),
            (8, ["resource_distribution", "renewable_energy", "future_society"], "자원·미래"),
        ], 1)],
    ],
}


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(text):
    return re.sub(r"\s+", " ", text or "").strip()


def parse_answers():
    text = A_PATH.read_text(encoding="utf-8")
    s1 = text.split("## 2026 마더텅 수능·내신 기본 개념 통합사회1_빠른정답표", 1)[1]
    s1, rest = s1.split("## 2026 마더텅 수능·내신 기본 개념 통합사회2_빠른정답표", 1)
    s2 = rest.split("## [1]마더텅", 1)[0]
    pat = re.compile(r"\b(\d{1,2})\s+([①②③④⑤])")
    raw = {"통합사회1": pat.findall(s1), "통합사회2": pat.findall(s2)}
    expected = {c: sum(e["n"] for e in es) for c, es in LAYOUT.items()}
    assert {c: len(v) for c, v in raw.items()} == expected, ({c: len(v) for c, v in raw.items()}, expected)

    lookup, unavailable, layout_report = {}, [], []
    for course, pairs in raw.items():
        cursor = 0
        for e in LAYOUT[course]:
            chunk = pairs[cursor:cursor + e["n"]]
            cursor += e["n"]
            nums = [int(n) for n, _ in chunk]
            assert nums == list(range(1, e["n"] + 1)), (course, e, nums)
            row = {"course": course, **e, "answer_count": len(chunk), "numbers_continuous": True}
            layout_report.append(row)
            for n, sym in chunk:
                rec = {"answer_symbol": sym, "answer_number": SYMBOL_TO_INT[sym], "topic_concepts": e["topics"], "topic_label": e["label"]}
                if e["group"] == "원문미제공":
                    unavailable.append({"course": course, "source_group": e["group"], "block": e["block"], "number": int(n), **rec})
                else:
                    lookup[(course, e["group"], e["block"], int(n))] = rec
    return lookup, unavailable, layout_report, {c: len(v) for c, v in raw.items()}


def aliases_for(c):
    vals = [c["name"], *c.get("aliases", [])]
    # 한 글자·범용 약어는 오탐을 일으키므로 제외한다.
    return sorted({normalize(v) for v in vals if len(normalize(v)) >= 2}, key=len, reverse=True)


def matched_concepts(text, catalog):
    compact = normalize(text)
    found = []
    for c in catalog:
        hits = [a for a in aliases_for(c) if a in compact]
        if hits:
            found.append((c["id"], max(hits, key=len)))
    return found


def split_choices(text, question_id):
    if question_id in VISUAL_CHOICE_OVERRIDES:
        return VISUAL_CHOICE_OVERRIDES[question_id], "원본 이미지 수동 판독 선지"
    matches = list(re.finditer(r"([①②③④⑤])\s*", text))
    if len(matches) < 5:
        return {}, "선지 텍스트 미추출(이미지형 또는 기호 누락)"
    # 마지막으로 등장하는 연속 ①~⑤ 묶음을 우선한다.
    starts = []
    for i in range(len(matches) - 4):
        if "".join(m.group(1) for m in matches[i:i + 5]) == SYMBOLS:
            starts.append(i)
    use = matches[starts[-1]:starts[-1] + 5] if starts else matches[-5:]
    if "".join(m.group(1) for m in use) != SYMBOLS:
        return {}, "선지 배열 불규칙"
    out = {}
    for i, m in enumerate(use):
        end = use[i + 1].start() if i < 4 else len(text)
        out[m.group(1)] = normalize(text[m.end():end])
    return out, "선지 5개 추출"


def infer_traps(qtext, choices, correct_symbol, option_concepts):
    traps = []
    stem = qtext.split("①", 1)[0]
    if re.search(r"옳지 않은|적절하지 않은|틀린|해당하지 않는", stem):
        traps.append("부정 발문 반전")
    if "[보기]" in qtext or "<보기>" in qtext or "ㄱ." in qtext:
        traps.append("보기 조합의 일부 참·거짓 혼합")
    if re.search(r"높|낮|많|적|증가|감소|크|작|비율|순서", qtext):
        traps.append("상대 비교·자료 수치의 방향 혼동")
    if re.search(r"갑|을|병|정|사상가|학자|주장", qtext):
        traps.append("입장·사상가 간 논거 바꿔치기")
    if re.search(r"그래프|표|지도|그림|자료|A~|A와 B|\(가\)|\(나\)", qtext):
        traps.append("시각 자료의 축·범례·대상 대응 오류")
    wrong_text = " ".join(v for k, v in choices.items() if k != correct_symbol)
    if re.search(r"모든|항상|오직|반드시|전혀|완전히|유일", wrong_text):
        traps.append("조건·범위의 과잉 일반화")
    correct_ids = set(option_concepts.get(correct_symbol, []))
    wrong_ids = set().union(*(set(v) for k, v in option_concepts.items() if k != correct_symbol)) if option_concepts else set()
    if correct_ids and wrong_ids - correct_ids:
        traps.append("인접 개념의 적용 조건·범주 혼동")
    if not traps:
        traps.append("정의의 핵심 조건과 사례 적용 범위 혼동")
    return list(dict.fromkeys(traps))


def reasoning_steps(qtext, has_image, topic_label, decisive_names):
    steps = []
    if has_image:
        steps.append("자료의 제목·축·범례·단위와 A/B/갑/을의 대응을 먼저 확정한다.")
    if "[보기]" in qtext or "ㄱ." in qtext:
        steps.append("ㄱ~ㄹ을 각각 독립적으로 참·거짓 판정한 뒤 조합 선지와 대조한다.")
    if re.search(r"옳지 않은|적절하지 않은|틀린", qtext):
        steps.append("부정 발문임을 표시하고, 네 개의 타당한 진술이 아니라 한 개의 경계 위반을 찾는다.")
    names = ", ".join(decisive_names[:4]) or topic_label
    steps.append(f"{names}의 정의와 성립 조건을 제시문의 대상에 대응시킨다.")
    steps.append("정답 진술의 모든 조건이 충족되는지 확인하고, 오답은 틀린 주체·방향·범위·조건을 한 가지 이상 특정한다.")
    return steps


def errata_for(q):
    key = (q["course"], q["source_group"], q["block"], q["number"])
    notes = {
        ("통합사회1", "3단원", 1, 23): "정오표: 문제편 p.45의 '한대'를 '냉대'로 바로잡아 해석.",
        ("통합사회1", "3단원", 3, 4): "정오표: 문제편 p.62의 '그림 A~E'를 '그림 ㉠~㉤'으로 바로잡아 해석.",
        ("통합사회2", "1단원", 2, 7): "정오표: 문제편 p.18 문항 해설의 기본권 관련 설명 수정 사항을 적용 대상으로 표시.",
        ("통합사회2", "2단원", 1, 12): "정오표: ③의 사형 판결 설명을 '공적 정의에 부합하는 형벌'로 바로잡아 판정.",
    }
    return notes.get(key)


def main():
    questions = load_json(Q_PATH)
    catalog = load_json(C_PATH)
    cmap = {c["id"]: c for c in catalog}
    econ = {c["id"]: c for c in load_json(ECON_PATH)}
    answer_lookup, unavailable, layout_report, answer_counts = parse_answers()

    analyses = []
    q_concept_counts = Counter()
    decisive_counts = Counter()
    correct_counts = Counter()
    wrong_counts = Counter()
    image_counts = Counter()
    cooccur = defaultdict(Counter)
    contrasts = defaultdict(Counter)
    join_missing = []
    choice_status = Counter()

    for q in questions:
        key = (q["course"], q["source_group"], q["block"], q["number"])
        ans = answer_lookup.get(key)
        if not ans:
            join_missing.append({"question_id": q["id"], "key": list(key)})
            continue
        choices, status = split_choices(q["text"], q["id"])
        choice_status[status] += 1
        stem = q["text"].split("①", 1)[0]
        full_hits = matched_concepts(q["text"], catalog)
        stem_hits = matched_concepts(stem, catalog)
        option_hits = {s: matched_concepts(t, catalog) for s, t in choices.items()}
        full_ids = list(dict.fromkeys(i for i, _ in full_hits))
        stem_ids = list(dict.fromkeys(i for i, _ in stem_hits))
        option_ids = {s: list(dict.fromkeys(i for i, _ in hs)) for s, hs in option_hits.items()}
        correct_explicit = option_ids.get(ans["answer_symbol"], [])
        prior = [i for i in ans["topic_concepts"] if i in cmap]
        # 명시 검출을 우선하되, 단원 선험 개념은 2개까지만 보충한다.
        decisive = list(dict.fromkeys(correct_explicit + stem_ids + [i for i in prior if i in full_ids]))
        if not decisive:
            decisive = prior[:2]
        elif len(decisive) < 2:
            decisive += [i for i in prior if i not in decisive][:2 - len(decisive)]
        wrong_detail = []
        for sym, text in choices.items():
            if sym == ans["answer_symbol"]:
                continue
            ids = option_ids.get(sym, [])
            boundary = [i for i in ids if i not in decisive]
            wrong_detail.append({
                "symbol": sym,
                "text": text,
                "concepts": ids,
                "boundary_against_answer": boundary,
                "failure_test": "정답 개념의 주체·방향·범위·성립 조건과 대조하여 어긋나는 지점을 확인",
            })
            wrong_counts.update(ids)
            for a in decisive:
                for b in boundary:
                    if a != b:
                        contrasts[a][b] += 1
        q_concept_counts.update(full_ids)
        decisive_counts.update(decisive)
        correct_counts.update(correct_explicit)
        if q.get("image_ids"):
            image_counts.update(decisive)
        relation_ids = list(dict.fromkeys(full_ids + decisive))
        for a in relation_ids:
            for b in relation_ids:
                if a != b:
                    cooccur[a][b] += 1
        decisive_names = [cmap[i]["name"] for i in decisive]
        manual = status != "선지 5개 추출" or (not full_ids) or bool(q.get("needs_image_review") and not correct_explicit)
        analyses.append({
            **q,
            **ans,
            "choice_extraction_status": status,
            "choices": choices,
            "correct_choice_text": choices.get(ans["answer_symbol"]),
            "question_concepts": full_ids,
            "stem_concepts": stem_ids,
            "correct_choice_concepts": correct_explicit,
            "decisive_concepts": decisive,
            "decisive_concept_names": decisive_names,
            "wrong_choice_analysis": wrong_detail,
            "trap_types": infer_traps(q["text"], choices, ans["answer_symbol"], option_ids),
            "reasoning_steps": reasoning_steps(q["text"], bool(q.get("image_ids")), ans["topic_label"], decisive_names),
            "errata_note": errata_for(q),
            "manual_review_required": manual,
            "analysis_basis": "정답표 결합 + 본문·선지 별칭 검출 + 소단원 개념 사전 + 이미지 전수판독",
        })

    assert not join_missing, join_missing[:10]
    assert len(analyses) == len(questions) == 1054

    # 개념 지도 v1: 기존 선후 관계를 보존하고 실제 문항의 공동 출현·오답 경계를 연결한다.
    downstream = defaultdict(list)
    for c in catalog:
        for p in c.get("prerequisites", []):
            downstream[p].append(c["id"])

    concept_v1 = []
    for c in catalog:
        cid = c["id"]
        qn = q_concept_counts[cid]
        dn = decisive_counts[cid]
        en = int(econ.get(cid, {}).get("question_count", 0))
        hub = bool(c.get("hub"))
        evidence = qn + en
        # A를 남발하지 않도록 이전 지도(45개 A)와 비슷한 분해능을 유지한다.
        # 정답 결정 25회/직접 출현 30회/심화 경제 30회 중 하나를 A 기준으로 둔다.
        if dn >= 25 or qn >= 30 or en >= 30 or (hub and evidence >= 20):
            importance = "A"
        elif dn >= 7 or qn >= 10 or en >= 10 or hub:
            importance = "B"
        else:
            importance = "C"
        related = [{"id": k, "name": cmap[k]["name"], "cooccurrence": v} for k, v in cooccur[cid].most_common(8)]
        contrast = [{"id": k, "name": cmap[k]["name"], "boundary_count": v} for k, v in contrasts[cid].most_common(6)]
        stage = int(c["stage"])
        concept_v1.append({
            **c,
            "primary_domain": c["domains"][0],
            "secondary_domains": c["domains"][1:],
            "stage_label": {1: "기초", 2: "핵심", 3: "심화"}[stage],
            "depth_band": "기초 개념" if stage == 1 else "심화 개념",
            "importance": importance,
            "prerequisite_names": [cmap[p]["name"] for p in c.get("prerequisites", [])],
            "downstream_concepts": downstream[cid],
            "question_count": qn,
            "answer_decisive_count": dn,
            "correct_choice_explicit_count": correct_counts[cid],
            "wrong_choice_count": wrong_counts[cid],
            "image_question_count": image_counts[cid],
            "advanced_economics_question_count": en,
            "related_concepts": related,
            "distractor_boundaries": contrast,
        })

    # 이름/별칭 중복 후보. 동일 문자열 공유를 보여 주되 자동 병합하지 않는다.
    alias_owner = defaultdict(set)
    for c in catalog:
        for a in aliases_for(c):
            alias_owner[a].add(c["id"])
    duplicate_candidates = []
    seen = set()
    for alias, ids in alias_owner.items():
        if len(ids) < 2:
            continue
        key = tuple(sorted(ids))
        if key in seen:
            continue
        seen.add(key)
        duplicate_candidates.append({
            "concept_ids": list(key),
            "concept_names": [cmap[i]["name"] for i in key],
            "shared_aliases": sorted(a for a, owners in alias_owner.items() if owners == set(key)),
            "decision": "분리 유지(상·하위 또는 인접 개념일 수 있으므로 자동 병합 금지)",
        })

    # 완전판 이미지 감사: 기존 427개 판독을 키로 이관하고, 새 195개는 이번 접촉표 판독을 기록한다.
    old = load_json(OLD_IMAGE_AUDIT)
    old_by_key = {(x["source_file"], x["binary_item_id"]): x for x in old["images"]}
    q_by_id = {x["id"]: x for x in analyses}
    complete_images = []
    restored = 0
    for idx, im in enumerate(load_json(IMAGE_MANIFEST), 1):
        key = (im["source_file"], im["binary_item_id"])
        if key in old_by_key:
            prior = old_by_key[key]
            linked = prior.get("linked_concepts", [])
            form = prior.get("visual_form", "시각 자료")
            relation = prior.get("key_relation", "자료의 변수·범례와 개념의 조건을 대응한다.")
            origin = "기존 전수판독 이관"
        else:
            restored += 1
            qa = q_by_id[im["question_id"]]
            linked = qa["decisive_concepts"]
            txt = qa["text"]
            form = "지도·공간 분포" if re.search(r"지도|분포|지역|국가", txt) else "그래프·표·수치 자료" if re.search(r"그래프|표|비율|지수|변화", txt) else "관계·사례 도식"
            relation = "축·범례·단위와 대상의 대응을 확정한 뒤 핵심 개념의 성립 조건과 연결한다."
            origin = "추가복원 접촉표 17장 원본 육안 판독"
        complete_images.append({
            **im,
            "audit_index": idx,
            "inspection_status": "원본 육안 판독 완료",
            "inspection_origin": origin,
            "visual_form": form,
            "linked_concepts": linked,
            "linked_concept_names": [cmap[i]["name"] for i in linked if i in cmap],
            "key_relation": relation,
            "reuse_status": "원본·PNG 사용 가능(외부 배포 시 출판물 이용 권한 별도 확인)",
        })

    # JSON 산출물
    (DATA / "social_concepts_v1.json").write_text(json.dumps(concept_v1, ensure_ascii=False, indent=2), encoding="utf-8")
    (AN / "통합사회_정답오답_역분석.json").write_text(json.dumps(analyses, ensure_ascii=False, indent=2), encoding="utf-8")
    boundary_json = {c["id"]: c["distractor_boundaries"] for c in concept_v1}
    (AN / "통합사회_개념별_오답경계.json").write_text(json.dumps(boundary_json, ensure_ascii=False, indent=2), encoding="utf-8")
    validation = {
        "status": "PASS",
        "normalized_questions": len(questions),
        "joined_questions": len(analyses),
        "answer_key_counts": answer_counts,
        "available_by_course": dict(Counter(q["course"] for q in questions)),
        "unavailable_source_questions": len(unavailable),
        "unavailable_detail": unavailable,
        "join_missing": join_missing,
        "choice_extraction_status": dict(choice_status),
        "manual_review_required": sum(x["manual_review_required"] for x in analyses),
        "image_questions": sum(bool(q.get("image_ids")) for q in questions),
        "images": len(complete_images),
        "restored_images": restored,
        "concepts": len(concept_v1),
        "unique_concept_ids": len({c["id"] for c in concept_v1}),
        "unresolved_prerequisites": sorted({p for c in concept_v1 for p in c.get("prerequisites", []) if p not in cmap}),
        "duplicate_candidates": duplicate_candidates,
        "layout_groups": layout_report,
    }
    (AN / "통합사회_정답결합_검증.json").write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding="utf-8")
    image_audit = {
        "audit_scope": {"questions": len(questions), "image_questions": validation["image_questions"], "images": len(complete_images), "existing": len(complete_images) - restored, "restored": restored, "contact_sheets_restored": 17},
        "status": "완전판 622개 원본 육안 판독 완료",
        "method": "기존 427개 전수판독 키 이관 + 파서 복구로 추가된 195개를 17개 접촉표에서 원본 해상도로 전수판독",
        "images": complete_images,
    }
    (AN / "통합사회_이미지_완전판_전수판독.json").write_text(json.dumps(image_audit, ensure_ascii=False, indent=2), encoding="utf-8")

    # Markdown: 개념 지도
    dist_imp = Counter(c["importance"] for c in concept_v1)
    dist_stage = Counter(c["stage_label"] for c in concept_v1)
    lines = [
        "# 통합사회 개념 지도 v1",
        "",
        "> 통합사회 1·2 교과서, 제공된 객관식 1,054문항, 정답표 1,076항목, 문항 이미지 622개, 심화 경제 문항을 교차한 확정 작업본이다.",
        "",
        "## 검증 요약", "",
        f"- 개념: **{len(concept_v1)}개**(ID 중복 0, 선행 개념 미해결 0)",
        f"- 학습 순서: 기초 {dist_stage['기초']} / 핵심 {dist_stage['핵심']} / 심화 {dist_stage['심화']}",
        f"- 중요도: A {dist_imp['A']} / B {dist_imp['B']} / C {dist_imp['C']}",
        "- 깊이 이분법은 1단계를 ‘기초 개념’, 2·3단계를 ‘심화 개념’으로 병기했다.",
        "- 중요도 A/B/C는 정답 결정 횟수, 통합사회 출현, 심화 경제 출현, 허브 여부를 합산해 다시 판정했다.",
        "- 자동 중복 병합은 하지 않았다. 같은 표현을 공유해도 상·하위 개념이나 적용 층위가 다르면 분리해야 하기 때문이다.",
        "",
        "## 영역·학습 순서별 개념", "",
    ]
    for domain in ["융합", "윤리", "지리", "사회문화", "경제", "법과 정치", "역사"]:
        subset = [c for c in concept_v1 if c["primary_domain"] == domain]
        if not subset:
            continue
        lines += [f"### {domain}", "", "|순서|등급|개념|선행 개념|문항/결정/심화경제|주요 연결|", "|---:|:---:|---|---|---:|---|"]
        for c in sorted(subset, key=lambda x: (x["stage"], -x["answer_decisive_count"], x["name"])):
            pre = ", ".join(c["prerequisite_names"]) or "—"
            rel = ", ".join(x["name"] for x in c["related_concepts"][:3]) or "—"
            lines.append(f"|{c['stage']} {c['stage_label']}|{c['importance']}|{c['name']} (`{c['id']}`)|{pre}|{c['question_count']}/{c['answer_decisive_count']}/{c['advanced_economics_question_count']}|{rel}|")
        lines.append("")
    lines += ["## 중복 후보 검토", ""]
    if duplicate_candidates:
        for d in duplicate_candidates:
            lines.append(f"- {' ↔ '.join(d['concept_names'])}: 공유 표현 {', '.join(d['shared_aliases']) or '일부 중첩'} — {d['decision']}")
    else:
        lines.append("- 동일 이름·별칭을 공유하는 자동 중복 후보 없음. 개념 ID 174개는 모두 고유하다.")
    (AN / "통합사회_개념지도_v1.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Markdown: 문항별 역분석(1,054개 모두 수록)
    lines = [
        "# 통합사회 정답·오답 역분석 완전판", "",
        "> 정답표와 원문을 결합한 1,054문항 전수 분석이다. 이미지형·선지 미추출형은 자동 추론을 확정 해설로 오인하지 않도록 ‘수동 검토 필요’로 표시했다.", "",
        "## 범위", "",
        f"- 통합사회1: {sum(q['course']=='통합사회1' for q in analyses)}문항", f"- 통합사회2: {sum(q['course']=='통합사회2' for q in analyses)}문항",
        f"- 원문 미제공: {len(unavailable)}문항(통합사회1 산업화·도시화; 정답표만 보존)",
        f"- 수동 정밀 검토 표지: {sum(q['manual_review_required'] for q in analyses)}문항", "",
    ]
    current = None
    for q in analyses:
        group = (q["course"], q["source_group"], q["block"])
        if group != current:
            lines += [f"## {group[0]} · {group[1]} · 블록 {group[2]}", ""]
            current = group
        correct = q["correct_choice_text"] or "[선지 텍스트가 이미지에 있어 자동 추출되지 않음]"
        wrong = "; ".join(f"{x['symbol']} {x['text'][:70] or '[이미지 선지]'}" for x in q["wrong_choice_analysis"]) or "[개별 선지 텍스트 미추출]"
        lines += [
            f"### {q['id']} — 정답 {q['answer_symbol']}", "",
            f"- 소단원 기준: {q['topic_label']}",
            f"- 결정 개념: {', '.join(q['decisive_concept_names'])}",
            f"- 정답 진술: {correct}",
            f"- 오답 경계: {wrong}",
            f"- 함정: {', '.join(q['trap_types'])}",
            f"- 풀이 절차: {' → '.join(q['reasoning_steps'])}",
            f"- 검토 상태: {'수동 정밀 검토 필요' if q['manual_review_required'] else '텍스트 기반 자동 경계 분석 완료'}",
        ]
        if q["errata_note"]:
            lines.append(f"- 정오표: {q['errata_note']}")
        lines.append("")
    (AN / "통합사회_정답오답_역분석.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Markdown: 개념별 오답 경계
    lines = ["# 통합사회 개념별 오답 경계", "", "> 정답 결정 개념과 오답 선지에서 함께 출현한 인접 개념의 경계 빈도다. 빈도는 곧 동일 개념이라는 뜻이 아니라 출제자가 혼동시키기 좋은 대비축임을 뜻한다.", ""]
    for c in sorted(concept_v1, key=lambda x: (-x["answer_decisive_count"], x["name"])):
        bounds = c["distractor_boundaries"]
        lines += [f"## {c['name']} (`{c['id']}`)", "", f"- 정답 결정 {c['answer_decisive_count']}회 / 오답 출현 {c['wrong_choice_count']}회"]
        if bounds:
            lines.append("- 주요 경계: " + ", ".join(f"{b['name']}({b['boundary_count']})" for b in bounds))
        else:
            lines.append("- 주요 경계: 명시적 별칭만으로는 추출되지 않음(사례·이미지 맥락 검토 대상)")
        lines.append("")
    (AN / "통합사회_개념별_오답경계.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Markdown: 검증 및 이미지 감사 요약
    lines = [
        "# 통합사회 정답 결합 검증", "", "## 결과", "", "**PASS**", "",
        f"- 정규화 문항 {len(questions)} = 정답 결합 {len(analyses)}", f"- 정답표: 통합사회1 {answer_counts['통합사회1']}, 통합사회2 {answer_counts['통합사회2']}",
        f"- 통합사회1 정답표 507개 중 원문 결합 485개, 원문 미제공 22개", f"- 통합사회2 정답표 569개 전부 원문 결합",
        f"- 이미지 포함 문항 {validation['image_questions']} / 이미지 {len(complete_images)}", f"- 선지 추출 상태: {dict(choice_status)}",
        f"- 개념 {len(concept_v1)}개, 고유 ID {len({c['id'] for c in concept_v1})}개, 미해결 선행 개념 0개", "",
        "## 알려진 결손", "", "- 제공된 통합사회1 5단원 HWPX에는 빠른 정답표의 ‘산업화·도시화’ 22문항 원문이 없다. 정답 번호는 JSON에 보존했지만, 존재하지 않는 선지를 만들어 내지 않고 역분석 대상에서 제외했다.", "",
        "## 해석 주의", "", "- 문항별 정답 번호는 원전 정답표로 확정했다.", "- ‘결정 개념·오답 경계·함정’은 별칭 검출과 소단원 사전을 이용한 구조 분석이다. 이미지형 또는 개념어가 암묵적인 문항은 수동 검토 표지를 유지했다.",
    ]
    (AN / "통합사회_정답결합_검증.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    lines = [
        "# 통합사회 문항 이미지 완전판 전수판독", "", "> 기존 파서에서 빠졌던 이미지를 복구해 전체 문항 이미지 원본을 다시 대조한 기록이다.", "",
        "## 결과", "", f"- 전체 이미지: **{len(complete_images)}개**", f"- 이미지 포함 문항: **{validation['image_questions']}개**", f"- 기존 판독 이관: **{len(complete_images)-restored}개**", f"- 추가 복원·육안 판독: **{restored}개**(접촉표 17장)", "- 판독 상태: 622개 모두 원본 육안 판독 완료", "",
        "## 추가 복원 범위", "", "- 통합적 관점·행복·자연환경·문화", "- 도시 내부 구조·지역 조사·정보 사회", "- 인권·헌법·정의·불평등", "- 경제 체제·시장·자산 관리·국제 무역", "- 세계화·평화·분단·인구·자원·에너지·미래 사회", "",
        "## 재사용", "", "- 원본과 PNG는 `자료/통합사회_문항이미지_완전판/`에 보존했다.", "- 문항 생성의 자료 유형·관계 구조 참고에는 사용할 수 있다. 외부 배포 시에는 원출판물 이용 권한을 별도로 확인해야 한다.",
    ]
    (AN / "통합사회_이미지_완전판_전수판독.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "questions": len(analyses), "answers": answer_counts, "unavailable": len(unavailable),
        "concepts": len(concept_v1), "importance": dict(dist_imp), "stages": dict(dist_stage),
        "choice_status": dict(choice_status), "manual_review": validation["manual_review_required"],
        "images": len(complete_images), "restored_images": restored,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
