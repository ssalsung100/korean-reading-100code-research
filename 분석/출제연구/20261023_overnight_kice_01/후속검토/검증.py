"""미실시 후속 확인 자료의 수치·후보 집합·빈 기록란을 국소 검증한다."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
from zoneinfo import ZoneInfo
import re
import json

ROOT=Path(__file__).resolve().parent
student=(ROOT/'학생용_응답기록지.md').read_text()
record_rows=re.findall(r'^\|(?:지역의 빈곤과 전체의 빈곤|품질을 알리는 보증|공유자원과 권리의 묶음|관계의 연결과 행동의 확산)\|[123]\|([^|]*)\|([^|]*)\|$',student,re.M)
assert len(record_rows)==12 and all(not a.strip() and not b.strip() for a,b in record_rows)

a_rows=re.findall(r'^\|([갑을병])\|([\d,]+)명\|([\d.]+)%\|([\d.]+)\|$',student,re.M)
assert [r[0] for r in a_rows]==list('갑을병')
ns=[int(r[1].replace(',','')) for r in a_rows]
hs=[F(r[2])/100 for r in a_rows];ins=[F(r[3]) for r in a_rows]
qs=[n*h for n,h in zip(ns,hs)];gs=[h*i for h,i in zip(hs,ins)]
sums=[q*i for q,i in zip(qs,ins)];whole_g=sum(sums)/sum(ns)
correct_i=sum(sums)/sum(qs);equal_i=sum(ins)/3;wrong_n_i=sum(n*i for n,i in zip(ns,ins))/sum(ns)
assert (correct_i,equal_i,wrong_n_i)==(F(14,27),F(1,2),F(53,100))
cs=[s/sum(ns) for s in sums];shares=[s/sum(sums) for s in sums]
# 현재 지역 빈곤2의 다섯 진술을 이 새 표에 그대로 붙이면 어떻게 되는가.
old_claims=[gs[0]>gs[1],sum(gs)/3==whole_g,gs[1]!=gs[2] and cs[1]==cs[2],
            ins[1]<correct_i,cs[2]==F('0.060') and shares[2]==F(6,100)]
assert old_claims==[False,True,True,True,False]

b=student.split('## 추가 확인 B',1)[1]
assert '세 명 이상' in b and '3분의2 이상' in b
b_rows=re.findall(r'^\|([XYZ])\|(\d+)명\|(\d+)명\|채택함\|$',b,re.M)
assert [r[0] for r in b_rows]==list('XYZ')
candidates={}
for who,nt,kt in b_rows:
    n,k=int(nt),int(kt)
    predicted={'인원':k>=3,'비율':F(k,n)>=F(2,3)}
    candidates[who]=[name for name,value in predicted.items() if value]
assert candidates=={'X':['인원','비율'],'Y':['비율'],'Z':['인원']}

report={'시각':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),
        '빈기록란':len(record_rows),'추가A':{'빈곤인구':list(map(str,qs)),
        '정의대로I':str(correct_i),'지역단순평균I':str(equal_i),'전체인구가중I':str(wrong_n_i),
        '기존5선지를붙였을때진리값':old_claims,'참인선지':['②','③','④'],
        '결론':'서술형 계산 확인으로만 사용. 현재5지선다의 표만 바꾸면 복수정답.'},
        '추가B_가능기준':candidates,'실제학생응답수':0,
        '한계':'자료의 수치와 모형만 확인. 학생에게 실시한 결과나 측정 도구의 타당도 검증 아님.','통과':True}
(ROOT/'검증결과.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
