import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,BYCASE,entry,source,write,sha
q=BYCASE['BGQ'];e=entry(q);s=copy.deepcopy(source(q));m=json.loads((OUT/'source_overrides.json').read_text());assert q['unique_question'] not in m
v=(ROOT/'data/기본기_연구/prepared_backlog/blind_sources/G422_visual01.md').read_text()
for a,b in [('갈릴레오 낙하 법칙 은','갈릴레오 낙하 법칙 s=(1/2)gt²은'),('거리( )','거리(s)'),('시간( )','시간(t)'),('중력 가속도 는','중력 가속도 g는')]:
 assert a in v,a
 v=v.replace(a,b)
assert '[시각 자료 1]' in s['stem'];s['stem']=s['stem'].replace('[시각 자료 1]',v)
assert '상수가 아닌 를' in s['choices'][2];s['choices'][2]=s['choices'][2].replace('상수가 아닌 를','상수가 아닌 g를')
s['backfill_source_derivation']={'original_source_path':e['source_path'],'original_sha256':sha(ROOT/e['source_path']),'official_page':'자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2011/page_007.png','repaired_fields':['stem 보기의s=(1/2)gt²,s,t,g','choices.2의g'],'method':'공식17번보기·선지③직접판독. 상수근사조건은지구반지름대비작은낙하구간이라는원문문장으로확인.','original_unchanged':True,'history':'기존수식결손유보는이번사후원문복원에서해소. 최초원문노출상태는불변.'}
n='BGQ_source_with_restored_variables.json';write(n,s);m[q['unique_question']]=str(OUT.relative_to(ROOT)/n);write('source_overrides.json',m)
print('BGQ 공식17번 수식·변수 복원 저장')
