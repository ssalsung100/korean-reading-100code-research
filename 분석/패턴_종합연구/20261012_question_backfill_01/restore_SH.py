import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,write,sha
p='data/기본기_연구/prepared_backlog/blind_sources/SH.json'
sp='data/기본기_연구/prepared_backlog/blind_sources/SH_official_question_supplement_20260919.json'
ap='data/기본기_연구/prepared_backlog/blind_sources/SH_symbol_A_supplement_20260919.json'
ip='data/기본기_연구/prepared_backlog/blind_sources/SH_G121_2019KICE_Q31_choice5.png'
d=json.loads((ROOT/p).read_text());s=json.loads((ROOT/sp).read_text());a=json.loads((ROOT/ap).read_text())
assert not (OUT/'SH_source_with_official_mass.json').exists()
old=copy.deepcopy(d['choices'][4]);assert '질량이 m인 지구' in old
new=s['mechanical_transcription']['choice_5_verbatim_from_official_crop'].removeprefix('⑤ ')
assert old.replace('질량이 m인 지구','질량이 M인 지구')==new
assert a['A_text'] in d['passage_text']
d['choices'][4]=new;d['blind_only']=False
d['backfill_source_derivation']={'operation':'기존 공식 문제지 crop과 보강 전사를 대조해 사후 보완용 사본의⑤지구 질량만m→M.원canonical 오류와hold이력불변.','original_source':p,'original_sha256':sha(ROOT/p),'original_choice5':old,'official_supplement':sp,'official_supplement_sha256':sha(ROOT/sp),'image_path':ip,'image_sha256':sha(ROOT/ip),'A_scope_supplement':ap,'A_scope_sha256':sha(ROOT/ap),'current_visual_observation':'주에이전트가기존저장crop직접열람:⑤지구대문자M,구슬소문자m,등가질점M,m,R+h확인.현재header와정답표새시각검증은수행하지않음.','exposure':'사후보완·신규blind아님'}
write('SH_source_with_official_mass.json',d)
ov=json.loads((OUT/'source_overrides.json').read_text());ov['U0114-Q05']=str((OUT/'SH_source_with_official_mass.json').relative_to(ROOT));write('source_overrides.json',ov)
print('SH⑤공식M 파생사본 연결')
