import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,write,sha
p='data/기본기_연구/prepared_backlog/blind_sources/OH.json'
sp='data/기본기_연구/prepared_backlog/blind_sources/OH_canonical_source_supplement.json'
d=json.loads((ROOT/p).read_text())
s=json.loads((ROOT/sp).read_text())
old=d['stem']
assert s['anchors']['equation_script']=='{B} over {A}'
assert old.count('측정하여 로')==1
assert not (OUT/'OH_source_with_restored_equation.json').exists()
d['stem']=old.replace('측정하여 로','측정하여 B/A로')
d['blind_only']=False
d['backfill_source_derivation']={
 'operation':'기존 보충파일의 equation {B} over {A}를 사후 분석용 사본의 누락 위치에 B/A로 표시. 원본·기존 보충파일 불변.',
 'original_source':p,'original_sha256':sha(ROOT/p),'equation_source':sp,
 'equation_source_sha256':sha(ROOT/sp),'original_stem':old,
 'equation_id':s['anchors']['equation_id'],
 'exposure':'기존 풀이·정답 활용 사후 보완. 신규 blind source 또는 신규 공식원문 검증 성과 아님'}
write('OH_source_with_restored_equation.json',d)
ov=json.loads((OUT/'source_overrides.json').read_text())
ov['U0098-Q03']=str((OUT/'OH_source_with_restored_equation.json').relative_to(ROOT))
write('source_overrides.json',ov)
print(d['stem'])
