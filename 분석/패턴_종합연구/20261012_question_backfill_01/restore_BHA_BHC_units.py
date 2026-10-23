import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,BYCASE,source,entry,write,sha
pairs=[('파장은 0.48이다','파장은 0.48μm이다'),('(0.4～0.7)','(0.4～0.7μm)'),('(0.7～1.2)','(0.7～1.2μm)'),('(1.2～3.0)','(1.2～3.0μm)'),('2.32, 2.58의','2.32, 2.58μm의'),('(3～14)','(3～14μm)'),('파장 3.62)','파장 3.62μm)'),('파장 9.67)','파장 9.67μm)'),('파장이 0.32인','파장이 0.32μm인'),('파장이 0.64인','파장이 0.64μm인'),('1.9, 2.7를','1.9, 2.7μm를'),('3～5와 8～14 대역','3～5μm와 8～14μm 대역')]
m=json.loads((OUT/'source_overrides.json').read_text())
for c in ['BHA','BHC']:
 q=BYCASE[c];assert q['unique_question'] not in m
 e=entry(q);s=copy.deepcopy(source(q))
 for a,b in pairs:
  assert a in s['passage_text'],a
  s['passage_text']=s['passage_text'].replace(a,b)
 s['backfill_source_derivation']={'original_source_path':e['source_path'],'original_sha256':sha(ROOT/e['source_path']),'evidence_paths':['자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2011/page_014.png','자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2011/page_015.png'],'method':'공식렌더직접판독하여누락μm단위만파생본문에복원. 과학서술의진위를외부지식으로교정하지않음.','changes':[{'old':a,'new':b} for a,b in pairs],'original_unchanged':True}
 n=c+'_source_with_restored_units.json';write(n,s);m[q['unique_question']]=str(OUT.relative_to(ROOT)/n)
write('source_overrides.json',m);print('BHA/BHC 단위 복원 파생본 저장')
