import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import ROOT,OUT,write,sha
base='data/기본기_연구/prepared_backlog/blind_sources/'
p=base+'YQ.json';sp=base+'YQ_choice_table_supplement_20260919.json';im=base+'YQ_G156_official_choice_table.png'
d=json.loads((ROOT/p).read_text());s=json.loads((ROOT/sp).read_text())
assert not (OUT/'YQ_source_with_restored_choices.json').exists()
old=copy.deepcopy(d['choices'])
rr=s['rows_verbatim_and_cell_alignment'];assert [r['number'] for r in rr]==list('①②③④⑤')
d['choices']=[f"ⓐ: {r['ⓐ']} / ⓑ: {r['ⓑ']}" for r in rr]
d['blind_only']=False
d['backfill_source_derivation']={'operation':'기존 공식 선택표 PNG를 주 에이전트가 직접 보고 두 열 다섯 행을 보충 전사와 대조.사후 보완 사본에만 연결.','original_source':p,'original_sha256':sha(ROOT/p),'original_choices':old,'supplement_source':sp,'supplement_sha256':sha(ROOT/sp),'image_source':im,'image_sha256':sha(ROOT/im),'visual_observation':'①용이/근거,②유력/근거,③용이/의탁,④원활/의탁,⑤유력/기초.하단 다음 공통발문 표지 외 내용 없음.','exposure':'기존 최초풀이·정답 확인 후 사후 판독,신규 blind 아님'}
write('YQ_source_with_restored_choices.json',d)
ov=json.loads((OUT/'source_overrides.json').read_text());ov['U0138-Q04']=str((OUT/'YQ_source_with_restored_choices.json').relative_to(ROOT));write('source_overrides.json',ov)
print('YQ 공식 선택표 대조 사본 연결')
