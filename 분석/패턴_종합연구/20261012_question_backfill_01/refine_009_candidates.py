import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,refresh,write
ids={'QBF01-AMD018','QBF01-AMD019','QBF01-AMD020'}
assert not ids & {r['amendment_id'] for r in rows(OUT/'scene_amendments.jsonl')}
sc={r['event_id']:r for r in rows(OUT/'new_judgment_scenes.jsonl')}
def link(p,r):return {'pattern_id':p,'case_specific_fit':r,'definition_source':'분석/패턴_종합연구/20261012_corpus_sweep_01/pattern_candidates.json','definition_reused':True}
changes=[
 ('QBF01-AMD018','QBF01-U0132-Q02-S01',[x for x in sc['QBF01-U0132-Q02-S01']['pattern_connections'] if x['pattern_id']!='조건부방향'],'XT는 청자 조건 차이에 따라 반응이 달라질 수 있다는 설명이며 입력→중간변수→결과의 증가·감소 방향을 이어 계산하지 않는다.조건부방향 D/E의 단조 방향 관계를 새로 만들지 않고 속성분리만 유지한다.'),
 ('QBF01-AMD019','QBF01-U0125-Q02-S03',[link('필요요건역전금지','동일하다면 같은 특성이라는 단일 함축을 유지하고 같은 특성에서 동일·상이 중 어느 쪽도 임의로 역추론하지 않는다.')],'UT④는 정의 대상/속성의 반례 배치가 아니라 단일 함축이 허용하지 않는 주장의 귀속 문제다.정의방향의 반례 구조를 억지 적용하지 않고 필요요건역전금지의 단일 함축·역방향 구별에 연결한다.'),
 ('QBF01-AMD020','QBF01-U0126-Q02-S02',[link('속성분리','처벌의 당위적 정당화 관계와 실제 처벌의 물리적 사건을 구별하고 하나의 설명을 다른 것으로 대체하지 않는다.')]+[x for x in sc['QBF01-U0126-Q02-S02']['pattern_connections'] if x['pattern_id']=='범위이동'],'UZ②에는 제도 목표의 실제 달성 여부를 검사하는 규범현실 D/E의 구조가 없다.당위적 연결과 물리적 사건을 구별한 실제 조작은 속성분리·범위이동으로 남기며 원95정의를 넓히지 않는다.')]
for aid,eid,new,reason in changes:
 append('scene_amendments.jsonl',[{'amendment_id':aid,'event_id':eid,'reason':'9배치 작성 직후 선택적 후보 정의 대조: '+reason+' 원raw·정답·최초풀이 불변.','changes':[{'field_path':'pattern_connections','old_value':copy.deepcopy(sc[eid]['pattern_connections']),'new_value':new}]}])
append('pattern_development.jsonl',[{'development_id':'QBF01-DEV027','pattern_ids':['조건부방향','정의방향','필요요건역전금지','규범현실','속성분리'],
 'evidence_event_ids':['QBF01-U0132-Q02-S01','QBF01-U0125-Q02-S03','QBF01-U0126-Q02-S02'],
 'finding':'XT의 청자별 반응 차이는 증가·감소 방향 사슬이 아니며,UT의 동일성 원리는 정의 반례의 배치가 아닌 단일 함축의 방향 검사이다.UZ의 처벌 당위는 목표가 현실에 구현되었는지 묻는 사례가 아니다.',
 'decision':'AMD018~020으로 넓게 붙인 후보 연결을 각각 축소·교체했다.조건이라는 말,정의처럼 보이는 원리,규범이라는 명칭만으로 가까운 후보를 적용하지 않는다.원95후보 정의 불변.',
 'next_counterexample':'동일 입력/상이한 조건에서 결과 차이만 있는 사례와 실제 단조 방향 사슬,분류 정의의 반례와 일반 단일 함축,당위/사실 구분과 제도 목표/현실 달성 검사를 서로 대조한다.',
 'educational_use':'수업의 넓은 설명 범주와 실제 연구 후보의 좁은 작동 정의를 분리한다.후보 이름이 아니라 D/E의 필요한 조작이 있었는지 적게 한다.'}])
refresh()
cp=json.loads((OUT/'checkpoint.json').read_text());h=json.loads((OUT/'session_handoff_20261013.json').read_text())
h.update(date=cp['date'],reviewed_questions=cp['reviewed_questions'],new_scenes=cp['new_scene_count'],by_exam=cp['by_exam'],batch_state='001~008 저장·표본 감사 완료.9배치321~350 저장.360번 저장 후9배치 감사 예정.',next_order=cp['next_order'],next_unique_question=cp['next_question'],next_case=cp['next_case_ids'][0],read_but_not_saved=[],last_saved_author='author_009f.py',next_author_suggestion='author_009g.py',resume_command='python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 351 5')
h['important_corrections']+=['9배치작성직후AMD018~020: XT조건부방향제거,UT정의방향→필요요건역전금지,UZ규범현실→속성분리.원95정의불변.DEV027저장.','XS기존3열5행전사새폴더사본연결.신규원표시각검증아님.']
write('session_handoff_20261013.json',h)
