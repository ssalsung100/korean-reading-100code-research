import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,write,sha
p='data/기본기_연구/prepared_backlog/blind_sources/XS.json';sp='data/기본기_연구/prepared_backlog/blind_sources/XS_choice_table_supplement_20260919.json'
d=json.loads((ROOT/p).read_text());s=json.loads((ROOT/sp).read_text())
assert not (OUT/'XS_source_with_restored_choices.json').exists()
old=copy.deepcopy(d['choices'])
assert [r['choice'] for r in s['choices']]==list('①②③④⑤')
d['choices']=[f"ⓐ: {r['a']} / ⓑ: {r['b']} / ⓒ: {r['c']}" for r in s['choices']]
d['blind_only']=False
d['backfill_source_derivation']={'operation':'기존 보충자료 3열5행을 사후 분석용 사본에 연결.신규 시각 원표 판독 아님.','original_source':p,'original_sha256':sha(ROOT/p),'original_choices':old,'supplement_source':sp,'supplement_sha256':sha(ROOT/sp),'xml_anchor':s['xml_anchor'],'exposure':'기존 풀이·정답 활용 사후 보완'}
write('XS_source_with_restored_choices.json',d)
ov=json.loads((OUT/'source_overrides.json').read_text());ov['U0132-Q01']=str((OUT/'XS_source_with_restored_choices.json').relative_to(ROOT));write('source_overrides.json',ov)
print('XS 3열5행 복원 사본 연결')
