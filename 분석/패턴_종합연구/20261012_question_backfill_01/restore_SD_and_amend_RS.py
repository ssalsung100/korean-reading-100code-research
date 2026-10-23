import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,write,sha,rows,append,refresh
p='data/기본기_연구/prepared_backlog/blind_sources/SD.json'
sp='data/기본기_연구/prepared_backlog/blind_sources/SD_choice_table_supplement_20260919.json'
d=json.loads((ROOT/p).read_text());s=json.loads((ROOT/sp).read_text())
assert not (OUT/'SD_source_with_restored_choices.json').exists()
oldstem=d['stem'];oldchoices=copy.deepcopy(d['choices'])
d['stem']=s['stem']+'\n\n◦읽기 계획 : 1문단을 훑어보면서 뒷부분을 예측하고 질문 만들기를 한 후, 글을 읽고 점검하기'
d['choices']=[r['prompt']+'\n'+r['result'] for r in s['choice_table_rows']]
assert len(d['choices'])==5
assert [r['choice'] for r in s['choice_table_rows']]==list('①②③④⑤')
d['blind_only']=False
d['backfill_source_derivation']={'operation':'기존 원표 보충자료의 다섯 행과 선택번호를 사후 분석용 사본에 연결. 원본의 첫 행 stem 혼입·이후행 한칸 이동·빈⑤ 불변.','original_source':p,'original_sha256':sha(ROOT/p),'original_stem':oldstem,'original_choices':oldchoices,'supplement_source':sp,'supplement_sha256':sha(ROOT/sp),'xml_anchor':s['xml_anchor'],'exposure':'기존 풀이·정답 활용 사후 보완. 신규 blind나 원표 신규 검증 성과 아님'}
write('SD_source_with_restored_choices.json',d)
ov=json.loads((OUT/'source_overrides.json').read_text());ov['U0114-Q01']=str((OUT/'SD_source_with_restored_choices.json').relative_to(ROOT));write('source_overrides.json',ov)
existing={r['amendment_id'] for r in rows(OUT/'scene_amendments.jsonl')}
assert not {'QBF01-AMD015','QBF01-AMD016'} & existing
ss={r['event_id']:r for r in rows(OUT/'new_judgment_scenes.jsonl')}
for aid,eid,new,reason in [
 ('QBF01-AMD015','QBF01-U0111-Q03-S02',[{'pattern_id':'범위이동','case_specific_fit':'채무 실현 제도의 일반 설명을 목적물이 이미 소실되어 불능인 상황까지 무조건 적용한 범위 이동을 검사한다.','definition_source':'분석/패턴_종합연구/20261012_corpus_sweep_01/pattern_candidates.json','definition_reused':True}], '실행조건 D는 다른 규정이 필수 수반 조건을 허용하는지 검사하는 좁은 구조다. RS는 특정 급부의 실제 불능이라는 범위 제한이므로 기존 정의를 확장하지 않고 범위이동에 연결한다.'),
 ('QBF01-AMD016','QBF01-U0111-Q03-S03',[x for x in ss['QBF01-U0111-Q03-S03']['pattern_connections'] if x['pattern_id']=='관계귀속'], '직전상태갱신 D의 반복 입력별 상태 유지/반전 계산이 실제 수행되지 않았다. 이미 지급된 급부를 반환 대상에 대응하는 관계귀속만 유지한다.')]:
 sc=ss[eid];append('scene_amendments.jsonl',[{'amendment_id':aid,'event_id':eid,'reason':'작성 직후 후보 정의 선택 대조: '+reason+' 원raw·정답·중간 추론·동결 정의 불변.','changes':[{'field_path':'pattern_connections','old_value':copy.deepcopy(sc['pattern_connections']),'new_value':new}]}])
refresh()
print('SD 다섯 선택지 복원 사본 연결·RS 후보 연결 AMD015/016 저장')
