"""산식·가상 사례·분할 불변을 유리수로 검산한다. 문체·학습 효과 검사가 아니다."""
from fractions import Fraction as F
from pathlib import Path
import json

def gap(incomes, z=F(100)):
    return sum((max(z-y, F(0))/z for y in incomes), F(0))/len(incomes)

# 새 지문 P3: 실제로 가능한 두 소득 배열
x = [F(40), F(40), F(100), F(100)]
y = [F(60), F(60), F(60), F(100)]
assert gap(x) == gap(y) == F(3, 10)

# P5: 동일한 빈곤선과 비음수 소득으로 명시값이 실현됨
a = [F(60)]*100
b = [F(85)]*400
assert gap(a) == F(2, 5) and gap(b) == F(3, 20)
total = gap(a+b)
contrib_a = F(len(a),len(a+b))*gap(a)
contrib_b = F(len(b),len(a+b))*gap(b)
assert total == contrib_a+contrib_b == F(1, 5)
assert contrib_a == F(2,25) and contrib_b == F(3,25)

# P6: 을의 서로 다른 지수를 가진 두 하위 지역으로도 합산 불변
b1 = [F(100)]*200
b2 = [F(70)]*200
assert gap(b1+b2) == gap(b)
same_people_before_partition = gap(a+b1+b2)
same_people_after_partition = F(100,500)*gap(a)+F(200,500)*gap(b1)+F(200,500)*gap(b2)
assert same_people_before_partition == same_people_after_partition == total
# 원래 갑/을의 단순 평균과 갑/을1/을2의 단순 평균은 다름
assert (gap(a)+gap(b))/2 != (gap(a)+gap(b1)+gap(b2))/3

# 같은 전체 지수라도 지역 분포는 다를 수 있음
assert F(1,5)*F(4,5)+F(4,5)*F(1,20) == total

# 최초안·C안 검토에 쓰인 성질: 같은 총부족에서 제곱합은 달라짐
before = F(4,5)**2+F(1,5)**2
after = F(7,10)**2+F(3,10)**2
assert before == F(17,25) and after == F(29,50) and before > after

# 지원 우선순위를 기여분에서 도출하지 않음:
# 두 지역의 모든 수급자가 빈곤선 아래에 남으면 동일 총지급액의 G 감소는 동일.
assert (gap(a+b)-gap([F(70)]+a[1:]+b)) == (
    gap(a+b)-gap(a+[F(95)]+b[1:]))

result = {
    "status": "산식·가상 사례 검산 통과",
    "P3": {"두_지수": [str(gap(x)),str(gap(y))], "성립가능_개인자료": [list(map(str,x)),list(map(str,y))]},
    "P5": {"갑":str(gap(a)), "을":str(gap(b)), "전체":str(total),
           "갑_기여분":str(contrib_a),"을_기여분":str(contrib_b)},
    "P6": {"분할_전후_가중합":"동일", "단순평균_전":str((gap(a)+gap(b))/2),
           "단순평균_후":str((gap(a)+gap(b1)+gap(b2))/3)},
    "scope": "수치와 명시 모형의 관계만 검사. 실제 정책 효과·독자 이해·평가원 동등 품질 검증 아님.",
    "proof": "일반적 가법 분해는 학술근거.md의 대수 유도. 예시 검산을 일반 증명으로 대체하지 않음."
}
Path(__file__).with_name("시험지문_수치검산.json").write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
