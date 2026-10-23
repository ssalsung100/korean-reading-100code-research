import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,write,sha
p='data/기본기_연구/prepared_backlog/blind_sources/TK.json';sp='data/기본기_연구/prepared_backlog/blind_sources/TK_choice_table_supplement_20260919.json'
d=json.loads((ROOT/p).read_text());s=json.loads((ROOT/sp).read_text())
assert not (OUT/'TK_source_with_restored_choices.json').exists()
old=copy.deepcopy(d['choices']);assert all(not x.strip() for x in old)
assert s['columns']==['㉮','㉯']
d['choices']=['㉮: '+r['a']+' / ㉯: '+r['b'] for r in s['choices']];d['blind_only']=False
d['backfill_source_derivation']={'operation':'기존XML전사보충자료의㉮/㉯두열다섯행을사후보완사본에연결.원공란·hold불변.','original_source':p,'original_sha256':sha(ROOT/p),'original_choices':old,'supplement':sp,'supplement_sha256':sha(ROOT/sp),'xml_anchor':s['xml_anchor'],'exposure':'기존풀이·정답활용사후보완.원표신규시각검증아님'}
write('TK_source_with_restored_choices.json',d)
ov=json.loads((OUT/'source_overrides.json').read_text());ov['U0118-Q03']=str((OUT/'TK_source_with_restored_choices.json').relative_to(ROOT));write('source_overrides.json',ov)
ip='data/기본기_연구/prepared_backlog/blind_sources/TH_diagram.png'
assert not (OUT/'TH_visual_review.json').exists()
write('TH_visual_review.json',{'status':'주에이전트의사후원이미지직접열람','image_path':ip,'image_sha256':sha(ROOT/ip),'observations':['비콘1은왼쪽위,비콘2는오른쪽위,비콘3은아래쪽에배치되어있다.','그려진원반지름의크기는1<2<3이다.','P는위쪽에서세원경계가만나는점이다.','비콘1·2원은P및그아래쪽에서교차한다.','Q장애물은비콘3과비콘1·2의아래쪽교점사이에있다.','공통영역은비콘1·2사이에있으며비콘1중심과같지않다.'],'scope':'도식의정성배치·원경계·Q/P위치를확인했다.수치좌표·반지름측정이나공식정답표새검증아님.기존hold후유효최초풀이를활용하는사후보완이다.'})
print('TK원표복원사본·TH직접시각관찰저장')
