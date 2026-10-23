"""현재2번과 미채택 대안의 자료를 읽어 세 가중 방식과 전 선지를 대조한다."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import re

ROOT=Path(__file__).resolve().parents[1]
current=(ROOT/'A_지역빈곤/03_학생용_최종후보.md').read_text().split('## 2.',1)[1].split('## 3.',1)[0]
draft=(ROOT/'A_지역빈곤/07_2번가중방식_대조와_유지.md').read_text().split('### 2.',1)[1].split('### 대안의 전 선지',1)[0]


def analyze(text, comparison):
    rows=re.findall(r'^\|\s*([갑을병])\s*\|([^|]+)\|([^|]+)\|([^|]+)\|\s*$',text,re.M)
    assert [r[0] for r in rows]==list('갑을병')
    ns=[int(r[1].strip().replace(',','').replace('명','')) for r in rows]
    hs=[F(r[2].strip().removesuffix('%'))/100 for r in rows]
    ins=[F(r[3].strip()) for r in rows]
    qs=[n*h for n,h in zip(ns,hs)]
    assert all(q.denominator==1 and q>0 for q in qs)
    assert all(0<i<=1 for i in ins)
    gs=[h*i for h,i in zip(hs,ins)]
    sums=[n*g for n,g in zip(ns,gs)]
    total_n=sum(ns);total_q=sum(qs);total_s=sum(sums)
    total_g=total_s/total_n;correct=total_s/total_q
    equal=sum(ins)/3;pop=sum(n*i for n,i in zip(ns,ins))/total_n
    cs=[s/total_n for s in sums];shares=[s/total_s for s in sums]
    compare=(lambda a,b:a<b) if comparison=='작다' else (lambda a,b:a>b)
    line=re.search(r'^⑤ (.+)$',text,re.M).group(1)
    declared_c=F(re.search(r'([0-9]+\.[0-9]+)',line).group(1))
    declared_share=F(re.search(r'([0-9]+)%',line).group(1))/100
    truth=[gs[0]>gs[1],sum(gs)/3==total_g,
           gs[1]!=gs[2] and cs[1]==cs[2],compare(ins[1],correct),
           cs[2]==declared_c and shares[2]==declared_share]
    assert truth==[False,False,True,False,False]
    # 각 지역의 빈곤층 소득을100*(1-I), 비빈곤층 소득을100으로 두어 실현 가능.
    incomes=[{'빈곤인구':int(q),'빈곤층소득':str(100*(1-i)),
              '비빈곤인구':n-int(q),'비빈곤층소득':'100'} for n,q,i in zip(ns,qs,ins)]
    return {'N':ns,'빈곤인구':[int(q) for q in qs],
            '지역G':list(map(str,gs)),'기여분':list(map(str,cs)),
            '전체G':str(total_g),'정의대로I':str(correct),
            '단순지역평균I':str(equal),'전체인구가중I':str(pop),
            '선지진리값':truth,
            '4번_방식별판정':{'빈곤인구가중':compare(ins[1],correct),
                              '지역단순평균':compare(ins[1],equal),
                              '전체인구가중':compare(ins[1],pop)},
            '빈곤선100의실현사례':incomes}


result={'시각':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),
        '현재':analyze(current,'작다'),'대안':analyze(draft,'크다'),
        '결정':'현재 학생용 유지. 대안은 전체 인구 가중치 전용 오류와 지역 단순 평균 오류 중 어떤 방식이④의 정오를 바꾸는지를 교환한다.',
        '한계':'선지의 의미·비교방향은 저자가 지정하고 수치만 검산. 실제 학생의 계산 방식·선택률을 측정한 것이 아니다.'}
assert result['현재']['4번_방식별판정']=={'빈곤인구가중':False,'지역단순평균':False,'전체인구가중':True}
assert result['대안']['4번_방식별판정']=={'빈곤인구가중':False,'지역단순평균':True,'전체인구가중':False}
(ROOT/'검증/빈곤2_가중방식_결과.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
