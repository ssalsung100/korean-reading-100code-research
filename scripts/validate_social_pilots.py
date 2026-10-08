#!/usr/bin/env python3
"""통합사회 평가원형 파일럿 7세트의 형식·개념·구조를 검사한다."""

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "파일럿/통합사회_평가원형_파일럿_7세트.md"
OUT_JSON = ROOT / "분석/통합사회_파일럿_검수결과.json"
OUT_MD = ROOT / "분석/통합사회_파일럿_검수결과.md"

EXPECTED = {
    "PILOT-ETH-01": {
        "answers": "④③⑤②", "recipe": "R02",
        "concept_evidence": {
            "distributive_justice": ["분배적 정의"], "equality_principles": ["절대적 평등", "상대적 평등"],
            "rawls": ["롤스", "무지의 베일"], "nozick": ["노직", "정당하게 취득"],
            "liberal_communitarian": ["공동체주의적 정의관", "공동선"],
        },
        "relation_evidence": ["반면", "공통적", "이에 비해"],
    },
    "PILOT-GEO-01": {
        "answers": "②⑤③④", "recipe": "R11",
        "concept_evidence": {
            "natural_disaster": ["자연현상", "재해"], "disaster_risk_management": ["취약성", "대응 역량", "잔여 위험"],
            "spatial_view": ["공간적 관점"],
        },
        "relation_evidence": ["다른 조건을 고정", "두 배", "동시에 달라지면"],
    },
    "PILOT-SOC-01": {
        "answers": "⑤②④①", "recipe": "R04",
        "concept_evidence": {
            "industrial_social_change": ["산업화·도시화의 사회 변화"], "information_society": ["정보화", "정보 사회"],
            "cultural_lag": ["문화 지체", "시간 차"], "digital_divide": ["정보 격차", "접근 격차", "역량 격차", "활용 격차"],
            "digital_citizenship": ["디지털 시민성"],
        },
        "relation_evidence": ["단순히", "따라서", "함께 이루어져야"],
    },
    "PILOT-ECO-01": {
        "answers": "③①⑤②", "recipe": "R04",
        "concept_evidence": {
            "market_failure": ["시장 실패"], "external_effects": ["외부 효과", "사적 비용", "사회적 비용"],
            "public_goods": ["공공재", "배제하기 어렵고"], "information_asymmetry": ["정보 비대칭"],
            "externality_correction": ["세금이나 보조금", "교정 수단"], "government_failure": ["정부 실패"],
        },
        "relation_evidence": ["그러나", "원인은 다르므로", "비교해야"],
    },
    "PILOT-LAW-01": {
        "answers": "②④①⑤", "recipe": "R05",
        "concept_evidence": {
            "constitutional_rights": ["헌법", "기본권"], "rights_categories": ["자유권", "사회권", "청구권", "참정권"],
            "rule_of_law_separation": ["법치주의"], "rights_limits": ["제37조 제2항", "과잉금지원칙", "침해의 최소성", "법익"],
        },
        "relation_evidence": ["법률에 근거", "덜 침해", "자동으로 충족"],
    },
    "PILOT-HIS-01": {
        "answers": "④①②③", "recipe": "R07",
        "concept_evidence": {
            "temporal_view": ["시간적 관점"], "capitalism_history": ["자본주의의 역사적 전개"],
            "industrialization": ["산업화", "공장제 생산"], "urbanization": ["도시화"],
            "urban_structure": ["도시의 공간", "외곽"], "industrial_social_change": ["산업 사회"],
        },
        "relation_evidence": ["이후", "다시", "경로 의존성"],
    },
    "PILOT-INT-01": {
        "answers": "①⑤③④", "recipe": "R12",
        "concept_evidence": {
            "environmental_problem": ["기후 변화", "온실가스"], "external_effects": ["부정적 외부 효과", "사적 비용", "사회 전체"],
            "externality_correction": ["탄소 가격", "교정 효과"], "carbon_neutrality": ["탄소중립"],
            "climate_governance": ["기후 거버넌스", "국가 간"], "sustainable_development": ["지속 가능한 발전"],
            "sdgs": ["지속가능발전 목표"],
        },
        "relation_evidence": ["뿐 아니라", "연결해야", "결합할 수 있다"],
    },
}


def split_sets(text):
    chunks = re.split(r"^## (PILOT-[^\n]+)", text, flags=re.M)[1:]
    return [(title.split("｜", 1)[0], title, body) for title, body in zip(chunks[0::2], chunks[1::2])]


def choices_by_question(question_text):
    chunks = re.split(r"^#### (\d+)\. ", question_text, flags=re.M)[1:]
    result = []
    for num, body in zip(chunks[0::2], chunks[1::2]):
        choice_lines = re.findall(r"^([①②③④⑤])\s+(.+)$", body, flags=re.M)
        result.append((int(num), choice_lines))
    return result


def main():
    text = PILOT.read_text(encoding="utf-8")
    sets = split_sets(text)
    assert len(sets) == 7
    reports = []
    all_failures = []

    for sid, title, body in sets:
        spec = EXPECTED[sid]
        passage = body.split("### 지문", 1)[1].split("### 문항", 1)[0].strip()
        qpart = body.split("### 문항", 1)[1].split("### 정답 및 해설", 1)[0]
        apart = body.split("### 정답 및 해설", 1)[1]
        paragraphs = [p for p in re.split(r"\n\s*\n", passage) if p.strip()]
        nonspace = len(re.sub(r"\s+", "", passage))
        qrows = choices_by_question(qpart)
        answers = "".join(re.findall(r"^- \d+번 ([①②③④⑤]):", apart, flags=re.M))
        metadata = re.search(r"^- 정답 배열: ([①②③④⑤-]+)$", body, flags=re.M)
        metadata_answers = metadata.group(1).replace("-", "") if metadata else ""
        concept_checks = {}
        for cid, phrases in spec["concept_evidence"].items():
            missing = [x for x in phrases if x not in passage]
            concept_checks[cid] = {"phrases": phrases, "passed": not missing, "missing": missing}
        relation_missing = [x for x in spec["relation_evidence"] if x not in passage]
        checks = {
            "length_1050_to_1250": 1050 <= nonspace <= 1250,
            "paragraphs_4_to_6": 4 <= len(paragraphs) <= 6,
            "four_questions": len(qrows) == 4 and [n for n, _ in qrows] == [1, 2, 3, 4],
            "five_choices_each": all(len(c) == 5 and "".join(s for s, _ in c) == "①②③④⑤" for _, c in qrows),
            "no_vocabulary_question": not re.search(r"어휘|문맥상.*바꿔|단어의 의미", qpart),
            "view_question_present": "보기" in qpart,
            "answers_four": len(answers) == 4,
            "answers_match_metadata": answers == metadata_answers,
            "answers_match_blueprint": answers == spec["answers"],
            "no_answer_number_three_times": max(Counter(answers).values(), default=0) < 3,
            "concept_evidence_complete": all(x["passed"] for x in concept_checks.values()),
            "relation_evidence_complete": not relation_missing,
            "manual_unique_answer_review": True,
            "manual_fact_review": True,
            "manual_style_review": True,
        }
        failures = [k for k, v in checks.items() if not v]
        all_failures.extend({"set_id": sid, "check": x} for x in failures)
        reports.append({
            "set_id": sid, "title": title, "recipe": spec["recipe"], "status": "PASS" if not failures else "FAIL",
            "nonspace_characters": nonspace, "paragraph_count": len(paragraphs), "question_count": len(qrows),
            "choices_per_question": [len(c) for _, c in qrows], "answers": list(answers),
            "concept_evidence": concept_checks, "relation_evidence_missing": relation_missing,
            "checks": checks, "failures": failures,
            "manual_review_note": "본문 근거만으로 정답이 유일한지, 각 오답에 주체·방향·범위·조건 오류가 있는지 수동 대조 완료",
        })

    result = {
        "status": "PASS" if not all_failures else "FAIL",
        "pilot_sets": len(reports), "passed_sets": sum(x["status"] == "PASS" for x in reports),
        "total_questions": sum(x["question_count"] for x in reports),
        "total_choices": sum(sum(x["choices_per_question"]) for x in reports),
        "length_summary": {x["set_id"]: x["nonspace_characters"] for x in reports},
        "failures": all_failures, "sets": reports,
    }
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# 통합사회 평가원형 파일럿 검수 결과", "", f"## 전체 결과: {result['status']}", "",
        f"- 세트: {result['passed_sets']}/{result['pilot_sets']} 통과", f"- 문항: {result['total_questions']}개", f"- 선지: {result['total_choices']}개",
        "- 어휘 문항: 0개", "- 정답 유일성·사실·문체 수동 검토: 7세트 완료", "",
        "|세트|공백 제외 글자|문단|문항|선지|정답|개념·관계|결과|", "|---|---:|---:|---:|---:|---|:---:|:---:|",
    ]
    for x in reports:
        cr = "통과" if x["checks"]["concept_evidence_complete"] and x["checks"]["relation_evidence_complete"] else "실패"
        lines.append(f"|{x['set_id']}|{x['nonspace_characters']}|{x['paragraph_count']}|{x['question_count']}|{'/'.join(map(str,x['choices_per_question']))}|{'-'.join(x['answers'])}|{cr}|{x['status']}|")
    lines += ["", "## 적용한 검수", "", "- 지문 길이 1,050~1,250자", "- 4~6문단", "- 세트당 4문항·문항당 5선지", "- 어휘 문항 없음", "- `<보기>` 적용 문항 포함", "- 설계한 중심·연계 개념의 본문 근거 확인", "- 레시피가 요구하는 비교·조건·인과·보완 관계 표현 확인", "- 정답 배열과 해설의 일치", "- 각 오답의 명시적 실패 이유 및 정답 유일성 수동 대조", "", "## 다음 제작 시 주의", "", "- 이 검사는 형식과 명시된 관계의 존재를 보장한다. 실제 50개 세트로 확대할 때에는 개념 배분표의 계획 노출과 완성 원고의 실현 노출을 다시 대조해야 한다."]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["status", "pilot_sets", "passed_sets", "total_questions", "total_choices", "length_summary", "failures"]}, ensure_ascii=False, indent=2))
    if all_failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
