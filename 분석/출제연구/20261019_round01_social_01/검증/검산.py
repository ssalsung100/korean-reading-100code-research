"""이번 창작의 가상 수치만 검사한다. 기출 원장과 v1은 읽거나 수정하지 않는다."""
from fractions import Fraction as F
from pathlib import Path
import json


def indices(incomes, z=100):
    n = len(incomes)
    gaps = [max(F(0), (F(z) - y) / z) for y in incomes]
    return {
        "빈곤율": F(sum(y < z for y in incomes), n),
        "빈곤갭지수": sum(gaps) / n,
        "제곱빈곤갭지수": sum(g * g for g in gaps) / n,
        "부족액_합": sum(gaps) * z,
    }


def output(row):
    return {k: {"정확값": str(v), "소수": float(v)} for k, v in row.items()}


def main():
    # 정수 조건을 학생에게 추가하지 않는다. 두 반모형은 실수 영역에서도 유효하다.
    witnesses = [[30, 90, 120, 160], [60, 60, 120, 160]]
    for x in witnesses:
        r = indices(x)
        assert r["빈곤율"] == F(1, 2)
        assert r["빈곤갭지수"] == F(1, 5)
        assert sum(y for y in x if y < 100) == 120
        assert r["빈곤갭지수"] / r["빈곤율"] == F(2, 5)
    assert [sum(y < 50 for y in x) for x in witnesses] == [1, 0]

    # 두 빈곤층 소득 합 120, 각 소득 100 미만. 가능한 정렬쌍은 (t,120-t), 20<t<=60.
    # 유리수 격자 검사는 보조이고, 전체 실수 영역의 논증은 해설에 따로 쓴다.
    grid = [F(i, 10) for i in range(201, 601)]
    states = [indices([t, 120-t, 120, 160]) for t in grid]
    assert min(s["제곱빈곤갭지수"] for s in states) == F(2, 25)
    assert all(s["제곱빈곤갭지수"] > F(1, 25) for s in states)
    assert all(s["부족액_합"] == 80 for s in states)

    incomes = {
        "지급_전": [20, 80, 100, 160],
        "갑": [20, 100, 100, 160],
        "을": [40, 80, 100, 160],
        "병": [25, 85, 105, 165],
    }
    rows = {k: indices(v) for k, v in incomes.items()}
    assert [rows[k]["빈곤율"] for k in incomes] == [F(1,2), F(1,4), F(1,2), F(1,2)]
    assert [rows[k]["빈곤갭지수"] for k in incomes] == [F(1,4), F(1,5), F(1,5), F(9,40)]
    assert [rows[k]["제곱빈곤갭지수"] for k in incomes] == [F(17,100), F(4,25), F(1,10), F(117,800)]
    assert all(sum(incomes[k]) - sum(incomes["지급_전"]) == 20 for k in ["갑","을","병"])
    assert min(["갑","을","병"], key=lambda k:rows[k]["빈곤율"]) == "갑"
    assert min(["갑","을","병"], key=lambda k:rows[k]["제곱빈곤갭지수"]) == "을"
    assert rows["갑"]["부족액_합"] == rows["을"]["부족액_합"] == 80
    wrong_calc = {
        "2번①_부족액을_소득합으로": 80,
        "2번③_전체평균을_빈곤층평균으로": 0.2,
        "2번⑤_평균을_먼저_제곱": float(F(1,5)**2),
        "3번①_경계포함": sum(y <= 100 for y in incomes["갑"]) / 4,
        "3번②_개인소득배율을_전체지수로": float(rows["지급_전"]["빈곤갭지수"] / 2),
        "3번③_모든지급액을_부족감소로": float(rows["지급_전"]["빈곤갭지수"] - F(20,400)),
    }
    result = {
        "범위": "창작 2·3번의 수치, 반모형, 의도한 오계산. 자연어 해석·문체·학생 난도는 자동 검증하지 않음.",
        "계산": "유리수 정확 계산",
        "2번_반모형": [{"소득": x, "지표": output(indices(x)), "50미만인원":sum(y<50 for y in x)} for x in witnesses],
        "2번_보조격자": {"개수":len(grid),"범위":"20<t<=60, 0.1 간격","한계":"실수 전수 검증 아님; 해설의 대수적 증명을 보조"},
        "3번": {k:{"소득":incomes[k],"지표":output(v)} for k,v in rows.items()},
        "오계산_실행": wrong_calc,
        "상태": "모든 assert 통과",
    }
    out = Path(__file__).with_name("수치검산.json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
