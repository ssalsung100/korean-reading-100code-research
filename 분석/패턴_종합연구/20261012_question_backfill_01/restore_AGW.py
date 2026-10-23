import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import ROOT,OUT,write,sha
base='data/기본기_연구/prepared_backlog/blind_sources/'
p=base+'AGW.json';im=base+'AGW_Q31_official_crop_20260920.png'
d=json.loads((ROOT/p).read_text())
assert not (OUT/'AGW_source_with_restored_choices.json').exists()
old=copy.deepcopy(d['choices'])
d['choices']=['충전지에 표시된 전압보다 전원 전압이 높은 충전기를 사용해야 합니다.','충전지에 표시된 충전 허용 전류보다 충전 전류의 세기가 강하면 충전지의 수명이 줄어듭니다.','충전지의 온도가 과도하게 상승하면 충전을 중지해야 합니다.','충전지를 사용하다가 수시로 충전해도 무방합니다.','과도하게 방전시키면 충전지의 수명이 줄어듭니다.']
d['blind_only']=False
d['backfill_source_derivation']={'operation':'기존문제지전재본crop을주에이전트가직접보고5항목과①~⑤대응을새폴더사본에복원.지시문에는첫항목중복잔재를보존하고판단은복원choices를사용.','original_source':p,'original_sha256':sha(ROOT/p),'original_choices':old,'image_source':im,'image_sha256':sha(ROOT/im),'visual_observation':'①전원전압,②허용전류,③과온도,④수시충전,⑤과방전.원choices첫항목밀림과말미빈값을교정.','source_qualification':'2022학년도예시문항.기존raw2974의orbi.kr/download/united/40109864/1문제지전재본출처를보존.공식배포호스트직접검증·실제시행기출로승격하지않음.','exposure':'기존최초·정답노출후사후판독.신규blind아님.'}
write('AGW_source_with_restored_choices.json',d)
ov=json.loads((OUT/'source_overrides.json').read_text());ov['U0163-Q02']=str((OUT/'AGW_source_with_restored_choices.json').relative_to(ROOT));write('source_overrides.json',ov)
print('AGW5항목·번호대응새폴더사본연결')
