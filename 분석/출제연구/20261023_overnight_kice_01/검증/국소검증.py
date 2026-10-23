"""창작 수치·경계·산출물 구조 검증. 자연어 정오를 자동 증명하는 도구가 아니다."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def poverty(incomes, line=100):
    gaps = [max(F(line) - F(y), F(0)) / line for y in incomes]
    poor = [g for g in gaps if g > 0]
    return {
        "인구": len(incomes),
        "빈곤인구": len(poor),
        "부족비율합": sum(gaps),
        "빈곤율": F(len(poor), len(incomes)),
        "빈곤층평균": sum(poor) / len(poor) if poor else None,
        "지수": sum(gaps) / len(incomes),
    }


def serial(x):
    if isinstance(x, F):
        return {"분수": str(x), "소수": float(x)}
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [serial(v) for v in x]
    return x


def verify_poverty():
    # 표의 평균식을 다시 곱하는 것과 별도로, 실현 가능한 개인 소득으로 복원한다.
    regions = [([60] * 100 + [100] * 100),
               ([50] * 120 + [100] * 180),
               ([40] * 100 + [100] * 400)]
    stats = [poverty(a) for a in regions]
    total = poverty(sum(regions, []))
    contributions = [s["부족비율합"] / total["인구"] for s in stats]
    assert [s["지수"] for s in stats] == [F(1, 5), F(1, 5), F(3, 25)]
    assert contributions == [F(1, 25), F(3, 50), F(3, 50)]
    assert total["지수"] == F(4, 25)
    assert total["빈곤층평균"] == F(1, 2)
    assert contributions[2] / total["지수"] == F(3, 8)
    q2_truth = [stats[0]["지수"] > stats[1]["지수"],
                sum(s["지수"] for s in stats) / 3 == total["지수"],
                stats[1]["지수"] != stats[2]["지수"] and contributions[1] == contributions[2],
                stats[1]["빈곤층평균"] < total["빈곤층평균"],
                stats[2]["부족비율합"] / total["부족비율합"] == F(6, 100)]
    assert q2_truth == [False, False, True, False, False]

    base = [0, 90, 60, 60] + [100] * 96
    after_a = [30, 120, 60, 60] + [100] * 96
    after_b = [0, 90, 90, 90] + [100] * 96
    initial, real_a, real_b = [poverty(a)["지수"] for a in [base, after_a, after_b]]
    estimate = (sum(max(100-y, 0) for y in base) - 60) / F(100 * len(base))
    overcorrected = (190 - (60-30)) / F(10000)
    assert [initial, real_a, real_b, estimate] == [F(19,1000), F(15,1000), F(13,1000), F(13,1000)]
    q3_truth = [estimate > real_a,
                estimate < real_a and estimate == real_b,
                estimate == initial,
                (initial-real_a) > (initial-real_b),
                overcorrected == real_a]
    assert q3_truth == [False, True, False, False, False]

    # 대안 B: 지역별 개인 소득으로 현재 빈곤층을 다시 선정한다.
    old_a, new_a = poverty([0,90]+[100]*48), poverty([30,120]+[100]*48)
    stale = old_a["빈곤율"] * new_a["빈곤층평균"]
    assert stale == F(28,1000) and new_a["지수"] == F(14,1000)
    assert new_a["빈곤층평균"] > old_a["빈곤층평균"]
    assert new_a["지수"] < old_a["지수"] < stale

    # 정의의 경계와 일반화의 반례: 무빈곤층·빈곤선 동일·초과 지급.
    assert poverty([100,120])["빈곤층평균"] is None
    assert poverty([100,120])["지수"] == 0
    reductions = {}
    for y, t in [(0,30), (90,30), (60,30), (90,10), (100,30)]:
        by_definition = max(100-y,0)-max(100-y-t,0)
        by_cap = min(t, max(100-y,0))
        assert by_definition == by_cap
        reductions[f"소득{y}_지급{t}"] = by_definition
    # 동일 예산 10이라도 두 사람 모두 미달 범위에 있으면 같은 감소.
    assert sum(min(5,max(100-y,0)) for y in [0,90]) == sum(min(5,max(100-y,0)) for y in [60,60])
    return {"2번_개인소득복원": stats, "2번_전체": total, "2번_기여분": contributions,
            "2번_진리값": q2_truth, "3번_지수": {"지원전":initial, "실제갑":real_a, "실제을":real_b, "조사자":estimate},
            "3번_진리값":q3_truth, "대안B_혼합시점산출":stale, "경계_부족액감소":reductions}


def verify_signal():
    # 후속 본문에 명시한 고장 시 정액1회 모형의 예상비용 실현 가능성.
    payment=F(100)
    costs={"고품질":F(1,5)*payment, "저품질":F(1,2)*payment}
    assert costs=={"고품질":F(20),"저품질":F(50)}
    # 반복 지급으로 달리 읽으면 고장 경험 확률만으로 비용 순서를 정할 수 없다.
    repeat_countermodel={"H":F(1,10)*3*payment,"L":F(1,5)*payment}
    assert repeat_countermodel['H']>repeat_countermodel['L']
    result = {}
    for kind, cost in [("고품질",20),("저품질",50)]:
        for policy, with_aid, without_aid in [("지원전",0,0),("가",15,15),("나",15,0)]:
            with_warranty = 40-cost+with_aid
            without_warranty = without_aid
            difference = with_warranty-without_warranty
            # 정책이 보증 선택에 붙이는 순지원만으로 계산한 별도 경로와 비교.
            assert difference == (40-cost)+(with_aid-without_aid)
            result[kind+policy] = {"보증":with_warranty,"무보증":without_warranty,"차이":difference}
    assert result['저품질가']['차이'] == -10
    assert result['저품질나']['차이'] == 5
    assert result['고품질가']['차이'] == 20
    assert result['고품질나']['차이'] == 35
    chosen = {policy: tuple(kind for kind in ['고품질','저품질']
                           if result[kind+policy]['차이'] > 0) for policy in ['가','나']}
    predictions = [(('고품질',),('고품질',)),
                   (('고품질',),('고품질','저품질')),
                   (('고품질','저품질'),('고품질',)),
                   (('고품질','저품질'),('고품질','저품질')),
                   ((),('고품질',))]
    q3_truth = [(a,b)==(chosen['가'],chosen['나']) for a,b in predictions]
    assert q3_truth == [False,True,False,False,False]
    # 분리조건의 실제 경계. 낮은 비용만으로 충분하지 않음.
    choices = {benefit:[benefit>20, benefit>50] for benefit in [10,40,60]}
    assert choices == {10:[False,False],40:[True,False],60:[True,True]}
    threshold = {aid:40-50+aid for aid in [9,10,11,15]}
    assert threshold == {9:-1,10:0,11:1,15:5}
    return {"지원안_선택차이": result, "3번_진리값":q3_truth,
            "정액1회_예상비용":costs, "반복지급_범위반례":repeat_countermodel,
            "추가수입별_두유형선택":choices, "조건부지원_저품질경계":threshold,
            "한계":"구매자 기대·새 시장가격은 자연어 논리로 검토; 새 균형 가격을 자동 산출하지 않음"}


def verify_files():
    student_files = [ROOT/'A_지역빈곤/03_학생용_최종후보.md',
                     ROOT/'B_품질보증/03_학생용_최종후보.md',
                     ROOT/'C_공유자원/03_학생용_최종후보.md']
    results = []
    for path in student_files:
        s = path.read_text()
        headings = re.findall(r'^## ([123])\.',s,re.M)
        assert headings == ['1','2','3'], (path,headings)
        for block in re.split(r'^## [123]\.',s,flags=re.M)[1:]:
            for symbol in '①②③④⑤':
                assert block.count(symbol) == 1, (path,symbol)
        assert not re.search(r'정답\s*[:은]|설계 의도|연구 기록|기출 대응|교사용',s)
        passage=s.split('---')[0]
        results.append({'파일':str(path.relative_to(ROOT)), '문항':3,'선지':15,
                        '본문_공백포함문자':len(passage),'주의':'길이는 편집 정보이며 품질 점수가 아님'})
    return results


def main():
    output = {"검증시각":datetime.now().astimezone().isoformat(),
              "지역빈곤":verify_poverty(), "품질보증":verify_signal(),
              "파일구조":verify_files(),
              "자동검증의한계":["자연어 선지의 참거짓과 기출 대응은 교사용·대응표의 수동 근거가 필요",
                               "공유자원의 권리 분류는 수치 검산 대상이 아니며 전 선지 수동 판독",
                               "학생 난도·오답률·외부 독립 검토를 검증하지 않음"]}
    path=ROOT/'검증/국소검증_결과.json'
    path.write_text(json.dumps(serial(output),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'상태':'통과','수치':'지역 빈곤·품질 보증의 정의 기반 수치와 경계',
                      '구조':'학생용 3세트·9문항·45선지','결과':str(path)},ensure_ascii=False))


if __name__=='__main__':
    main()
