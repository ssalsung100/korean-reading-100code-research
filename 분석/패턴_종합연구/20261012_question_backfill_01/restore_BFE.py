import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,BYCASE,source,entry,write,sha
q=BYCASE['BFE'];e=entry(q);s=copy.deepcopy(source(q));m=json.loads((OUT/'source_overrides.json').read_text());assert q['unique_question'] not in m
for k in ['passage_text','stem']:
 assert s[k].count('[시각 자료 1]')==1
 s[k]=s[k].replace('[시각 자료 1]','정당 수 산정')
s['backfill_source_derivation']={'original_source_path':e['source_path'],'original_sha256':sha(ROOT/e['source_path']),'evidence_path':'분석/패턴_종합연구/20261012_question_backfill_01/BFE_target_restoration_evidence.json','repair':'기존boundary_revision이지정한공식HWP_XML에서본문·발문Text(charshape-id=7) 정당 수 산정 두곳을직접확인. 원본문구의자리표시자만대체.','original_unchanged':True,'history':'최초조건부풀이와정답전복원후확정의구별유지.'}
n='BFE_source_with_restored_target.json';write(n,s);m[q['unique_question']]=str(OUT.relative_to(ROOT)/n);write('source_overrides.json',m)
print('BFE 본문·발문 표적의 파생 복원 저장')
