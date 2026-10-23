import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,BYCASE,entry,source,write,sha
mapping=json.loads((OUT/'source_overrides.json').read_text())
changes=[]
for c in ['AXY','AYA']:
 q=BYCASE[c];assert q['unique_question'] not in mapping
 e=entry(q);s=copy.deepcopy(source(q));old=s['passage_text']
 replacements=[('빛의 속도()','빛의 속도(c)'),('주파수()','주파수(f)'),('파장()','파장(λ)'),('수치()','수치(c＝fλ)'),('파장의 ～ 정도인데','파장의 1/2～1/4 정도인데')]
 for a,b in replacements:
  assert a in s['passage_text'],a
  s['passage_text']=s['passage_text'].replace(a,b)
 s['backfill_source_derivation']={'original_source_path':e['source_path'],'original_sha256':sha(ROOT/e['source_path']),'repair_date':'2026-10-15','method':'주 에이전트가 공식 HWP 페이지 렌더를 직접 보고 누락 기호·분수만 복원','evidence_paths':['자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2014/page_014.png','자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2014/page_015.png'],'changes':[{'old':a,'new':b} for a,b in replacements],'original_unchanged':True,'scope':'기존 최초풀이의 결손 이력은 보존. 이번 사후 파생본 보강이며 신규 blind 아님.'}
 name=c+'_source_with_restored_formula.json';write(name,s)
 mapping[q['unique_question']]=str(OUT.relative_to(ROOT)/name)
 changes.append({'case':c,'question':q['unique_question'],'derived_source':name,**s['backfill_source_derivation']})
write('source_overrides.json',mapping)
write('G348_source_repair_history.json',changes)
write('AXY_antenna_ratio_verification.json',{'status':'원문범위의 수학적 확인·기출 실제 장치 측정 아님','formula':'L=k*c/f; k in [1/4,1/2]','common_coefficient_ratio':2300/800,'independent_coefficient_ratio_range':[(.25/.5)*(2300/800),(.5/.25)*(2300/800)],'interpretation':'④의약3배는k800=k2300인동일설계비교에서성립. 범위만으로 서로다른k를배제할수없음. 공식③유지.','official_answer':3})
print('G348 누락기호·분수 파생본2개와 비교조건 기록 저장. 원본 불변.')
