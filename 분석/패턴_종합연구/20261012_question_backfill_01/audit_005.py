import sys, json, copy
sys.dont_write_bytecode = True
from backfill_io import OUT, rows, append, write, refresh, validate

assert not any(r['audit_id']=='QBF01-AUDIT005' for r in rows(OUT/'semantic_sample_audits.jsonl')), '이미 저장된 감사'
assert not any(r['amendment_id']=='QBF01-AMD012' for r in rows(OUT/'scene_amendments.jsonl')), '수정 저장 후 잔여 단계만 복구할 것'
sc = next(s for s in rows(OUT/'new_judgment_scenes.jsonl') if s['event_id']=='QBF01-U0086-Q02-S01')
old = copy.deepcopy(sc['pattern_connections'])
append('scene_amendments.jsonl', [{
 'amendment_id':'QBF01-AMD012', 'event_id':sc['event_id'],
 'reason':'5배치 표본 감사: MM은 두 이론의 명제/감정 해석을 귀속하는 문항이며, 표현행위 후보 D의 단독/조건문 맥락별 내용과 수행 구별을 실제로 요구하지 않는다. 넓은 후보명만으로 연결한 항을 제거. 최초 raw와 기존 95후보 정의는 보존.',
 'changes':[{'field_path':'pattern_connections','old_value':old,'new_value':[p for p in old if p['pattern_id']!='표현행위']}]}])

append('pattern_development.jsonl', [
 {'development_id':'QBF01-DEV014','pattern_ids':['표현행위','관계귀속','문맥조작화','대립가능성'],
  'evidence_event_ids':['QBF01-U0084-Q03-S01','QBF01-U0086-Q02-S01','QBF01-U0086-Q04-S01'],
  'finding':'MF는 인과 식별의 어려움을 재진술하며 실제 원인을 선택하지 않는다. MM은 발화의 의미를 두 이론에 귀속하고, MO는 명제성을 인정하는 이론에서만 긍정/부정의 진리값을 검사한다. 소재와 실제 수행 연산은 별도다.',
  'decision':'MM의 표현행위 연결을 AMD012로 제거한다. 기존 후보의 명칭이 넓어도 D의 조건을 생략하지 않는다. 표현행위의 기존 사례 중 명령 이유와 외형의 구별은 D보다 넓어 보이므로 잠정 정의의 내적 이질성 검토 대상으로 남기되 이번 표본만으로 원95정의를 개정하지 않는다.',
  'next_counterexample':'같은 도덕 문장을 단독 발화/조건문 내포로 바꿔 내용과 수행을 비교하는 사례와, 동일 발화를 서로 다른 이론으로 해석하는 사례를 대조한다.',
  'educational_use':'학습자가 실제로 해야 하는 행동을 먼저 쓰고 인과·설명·감정 같은 소재명은 따로 기록한다.'},
 {'development_id':'QBF01-DEV015','pattern_ids':['지지방향','반박표적','강도보존','규범현실'],
  'evidence_event_ids':['QBF01-U0083-Q03-S01','QBF01-U0085-Q03-S01','QBF01-U0085-Q03-S03'],
  'finding':'MB의 비판 관점 재구성은 효용이 전혀 없다는 직접 증명과 같지 않다. MJ의 차등 평가 발생 인정도 차등 평가의 정당화와 같지 않다. 지지/비판의 방향과 문장의 주장 강도·규범 지위는 따로 검사해야 한다.',
  'decision':'MB의 ①⑤ 근거 강도 유보를 유지한다. MJ S03은 최초 풀이에 사용된 것으로 소급하지 않고 이번 사후 보완의 추가 연결로 보존한다. 방향이 맞는다는 이유로 모든 강화 표현을 허용하는 생성 규칙은 채택하지 않는다.',
  'next_counterexample':'목표를 충분히 달성하지 못하지만 일부 도움은 주는 방법, 차등 평가가 발생하지만 부당하다고 평가하는 관점을 대조한다.',
  'educational_use':'비판 대상·평가 목표·도움의 정도를 나누고, 현상 서술과 규범 승인을 별도 선지로 조작한다.'},
 {'development_id':'QBF01-DEV016','pattern_ids':['수치표상','공통차별근거','관측합성','사건서술시간분리'],
  'evidence_event_ids':['QBF01-U0078-Q02-S01','QBF01-U0078-Q02-S02','QBF01-U0087-Q03-S01','QBF01-U0089-Q02-S01','QBF01-U0089-Q02-S02','QBF01-U0090-Q01-S01'],
  'finding':'LK와 MY는 명시된 지수·고정 조건으로 배율을 계산한다. MX는 공통 구간과 차이 구간, 합성 관측과 변화 요인을 구분하지만 정확한 거리 함수를 산출하지 않는다. MS에서는 증거 발견 시점과 법률 상태 변화 시점의 구별이 결과를 결정한다.',
  'decision':'계산 가능한 수량, 순서만 비교 가능한 지표, 정성적 제약을 별도로 보존한다. 시점이나 숫자가 있다는 이유만으로 같은 연산으로 통합하지 않는다. 표·그림 복원과 최초 답 수정도 구별한다.',
  'next_counterexample':'형태가 바뀌어 비례상수가 달라지는 회전 물체, 같은 관측 곡선을 만드는 다른 요인 조합, 판결 뒤 발견한 옛 증거와 실제 뒤늦게 성립한 권리 변화를 대조한다.',
  'educational_use':'수식의 고정 조건과 그래프가 직접 알려 주는 수준을 적게 한다. 시간 문제에는 사건 발생·판결·발견의 세 줄을 분리한다.'}
])
sample=['KY','LK','LR','MB','MF','MJ','MM','MS','MX','MY']
selected=[r for r in rows(OUT/'current_question_reviews.jsonl') if set(r['case_ids']) & set(sample)]
append('semantic_sample_audits.jsonl', [{
 'audit_id':'QBF01-AUDIT005','batch':5,'date':'2026-10-15',
 'sample_case_ids':sample,'sample_questions':len(selected),'sample_scenes':sum(len(r['scenes']) for r in selected),
 'method':'주 에이전트가 작성 과정에서 직접 읽은 원문·기존 풀이·보충자료를 바탕으로 현행 10문항의 5선지·중간 추론·근거 이력을 재검토. LK의 정확 XML 표, LR의 [A] 이미지, MJ의 정답 연결 수정 기록, MX의 그래프 직접 판독 결과를 대조. 전수 재풀이·모델 비교·원배포 PDF 전수 대조는 수행하지 않음.',
 'dimensions':{
  '모든 선지':'KY의 소아 반례·범주 이동·상호 실현·불균형 실패를 분리하고, LK의 다섯 선지를 광도·절대등급·거리·겉보기등급에 각각 대응했다. MB의 직접 비판과 재구성 비판도 구분했다.',
  '중간 추론':'KY의 조화 충분조건을 단순 부정하지 않고 명시된 두 실패 경로를 합류시킨다. LK는 0.1²×10⁴=100과 등급차5를 확인. MY는 형태 고정 아래 속도2배→에너지4배. MX는 정성 모형만 사용한다.',
  '정의 적용':'MM의 표현행위 후보는 D의 단독/조건문 맥락 검사가 없어 제거한다. MF는 실제 인과 식별이 아니라 명시문 재진술이다.',
  '자료·수정 이력':'LR의 [A] 범위는 시각 판독으로 해소된 이력을 보존하고 공통감 문단을 포함하지 않는다. MJ의 최초①은 유지되며 준비 답②→공식형식 대응①은 출처 연결 수정이다. MF의 유일 주코드 유보도 최초 판정과 구별한다.',
  '다중 장면':'LK의 지수 계산/지표 선택, LR의 복수조건/형식 지식과 미감 판단, MJ의 평가 기준/고정변인/규범 구별, MX의 차별 근거/관측 합성을 별도 장면으로 유지한다.'},
 'findings':[
  {'case':'MM','issue':'넓은 후보명에 기대어 D보다 넓게 연결','resolution':'AMD012로 표현행위 연결만 제거. 관계귀속과 원래 추론·정답은 유지'},
  {'case':'MB','issue':'①⑤의 전면 부정이 보기 직접 함의보다 강함','resolution':'새 보완의 명시적 유보로 유지. 공식답③의 비판 방향 판단과 엄밀한 보편 함의를 구분'},
  {'case':'MJ/MF/LR','issue':'답 수정·코드 유보·자료 보강을 최초 풀이로 합칠 위험','resolution':'기존 이력별 지위를 확인하고 사후 보강을 별도 표시'}],
 'decision':'수정 반영 뒤 201번부터 계속 진행 가능',
 'unresolved_blocking_error_count':0,
 'limitations':'10문항 18장면 의미 표본 감사이며 표본 밖의 의미 무오류 보증은 아니다. MB 및 앞 배치의 근거 유보는 해소된 것으로 집계하지 않는다.'}])
refresh()
validate()
write('batch_005_validation.json',json.loads((OUT/'validation_report.json').read_text()))
cp=json.loads((OUT/'checkpoint.json').read_text())
write('batch_005_checkpoint.json',cp)
h=json.loads((OUT/'session_handoff_20261013.json').read_text())
h.update(date=cp['date'],reviewed_questions=cp['reviewed_questions'],new_scenes=cp['new_scene_count'],by_exam=cp['by_exam'],
 batch_state='001~005 각 40문항 저장·표본 감사 완료. 005감사에서 MM 후보 연결 수정. 201번부터 6배치 계속.',
 next_order=cp['next_order'],next_unique_question=cp['next_question'],next_case=cp['next_case_ids'][0],read_but_not_saved=[],
 last_saved_author='author_005k.py',next_author_suggestion='author_006a.py',
 resume_command='python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 201 5',
 validation='200문항263장면의 현행 증거·offset·hash·선지수·ID 검증 통과. 보호 자산 전수 hash 반복 검사는 생략.',
 current_session_delegation='이번 재개 세션에서 보조모델 호출 없음. 심층 판단·시각 판독·의미 감사 모두 주 에이전트 직접 수행.')
h['important_corrections'] += ['MM의 표현행위 연결은 AMD012로 제거. 후보 D의 단독/조건문 구별이 없으며 두 이론의 해석 귀속만 수행한다.', 'MB의 ①⑤ 부정 강도에 관한 직접 근거 한계는 새 사후 보완 유보로 유지한다.', 'author_005j.py는 MP/MQ 저장 후 MS 근거 필드 오류로 중단됐다. MS/MT만 author_005j_remaining.py로 저장 완료. 원 스크립트 재실행 금지.']
write('session_handoff_20261013.json',h)
