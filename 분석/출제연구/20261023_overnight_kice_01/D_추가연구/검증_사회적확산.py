"""창작 연결망의 동시 갱신과 연결 추가의 국소 경계만 검증한다."""
from pathlib import Path
from collections import deque
from fractions import Fraction
from itertools import product
import json
import re

ROOT=Path(__file__).resolve().parent
V=set('ABCDEF')
GRAPHS={
    'I': {v:set('DEF') if v in 'ABC' else set('ABC') for v in V},
    'II': {'A':set('BCD'),'B':set('ADE'),'C':set('AEF'),
           'D':set('ABF'),'E':set('BCF'),'F':set('CDE')},
}


def evolve(g, threshold=2):
    active=set('AB');steps=[active.copy()]
    while True:
        nxt=active | {v for v in V if len(g[v]&active)>=threshold}
        if nxt==active:
            return steps
        steps.append(nxt.copy());active=nxt


def first_step(steps,v):
    return next((i for i,group in enumerate(steps) if v in group),None)


def shortest(g,target):
    q=deque([(v,0) for v in 'AB']);seen=set('AB')
    while q:
        v,n=q.popleft()
        if v==target:return n
        for w in g[v]-seen:seen.add(w);q.append((w,n+1))


results={}
for name,g in GRAPHS.items():
    assert set(g)==V
    assert all(len(neighbors)==3 for neighbors in g.values())
    assert all(v in g[w] for v in V for w in g[v])
    steps=evolve(g)
    results[name]={'채택단계':[sorted(x) for x in steps],
                   '최초채택':{v:first_step(steps,v) for v in sorted(V)},
                   'C최단경로':shortest(g,'C'),
                   '마지막비채택자의_채택이웃수':{v:len(g[v]&steps[-1]) for v in V-steps[-1]}}
assert results['I']['최초채택']=={'A':0,'B':0,'C':2,'D':1,'E':1,'F':1}
assert results['II']['최초채택']=={'A':0,'B':0,'C':None,'D':1,'E':None,'F':None}
assert results['I']['C최단경로']==2 and results['II']['C최단경로']==1

# 별도의 새 연결 사례: II에서 기존 연결을 남기고 B-C만 추가한다.
added={v:n.copy() for v,n in GRAPHS['II'].items()}
added['B'].add('C');added['C'].add('B')
old_steps,new_steps=evolve(GRAPHS['II']),evolve(added)
for t in range(max(len(old_steps),len(new_steps))):
    assert old_steps[min(t,len(old_steps)-1)] <= new_steps[min(t,len(new_steps)-1)]
assert new_steps[-1]==V

# 관측에서 기준 후보 복원. 각 기준을 가정했을 때의 예측과 관찰을 대조한다.
observations={'갑':(3,2,True),'을':(5,2,False),'병':(5,3,True)}
criteria={'인원':lambda n,k:k>=2,'비율':lambda n,k:Fraction(k,n)>=Fraction(2,3)}
candidates={who:{name for name,rule in criteria.items() if rule(n,k)==observed}
            for who,(n,k,observed) in observations.items()}
assert candidates=={'갑':{'인원','비율'},'을':{'비율'},'병':{'인원'}}
assignments=list(product(*(candidates[who] for who in ['갑','을','병'])))
q2_truth=[len({a[0] for a in assignments})>1,
          all(a[1]=='비율' for a in assignments),
          all(a[2]=='인원' for a in assignments),
          any(a[0]==a[2] for a in assignments),
          all(a[1]==a[2] for a in assignments)]
assert q2_truth==[True,True,True,True,False]
# 닫힌 기준 범위를 없애면 원래의 역복원이 무너질 수 있음을 확인한다.
third=lambda n,k:k>=3
assert third(5,2)==False and third(5,3)==True
# 따라서 '세 명 기준'을 추가 허용하면 을·병의 서로 다른 반응도 같은 기준으로 설명 가능.

text=(ROOT/'04_사회적확산_학생용후보.md').read_text()
assert re.findall(r'^## ([123])\.',text,re.M)==['1','2','3']
for block in re.split(r'^## [123]\.',text,flags=re.M)[1:]:
    assert all(block.count(c)==1 for c in '①②③④⑤')
assert not re.search(r'정답\s*[:은]|교사용|설계 의도|기출 대응',text)
report={'모형':results,'II에BC추가': [sorted(x) for x in new_steps],
        '개정2번_기준후보':{k:sorted(v) for k,v in candidates.items()},
        '개정2번_선지진리값':q2_truth,
        '개정2번_한정반례':'세 명 기준을 추가하면 을·병이 같은 기준일 수 있음',
        '결론':'모형의 상태·정체·최단경로·국소 연결 추가 확인',
        '한계':'실제 행동 확률·실험 재현·기출 대응의 자동 증명 아님'}
(ROOT/'사회적확산_검증결과.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
