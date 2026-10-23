import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write,refresh,validate
assert not any(r['audit_id']=='QBF01-AUDIT008' for r in rows(OUT/'semantic_sample_audits.jsonl')),'중복 감사 금지'
assert not any(r['amendment_id']=='QBF01-AMD017' for r in rows(OUT/'scene_amendments.jsonl')),'부분 완료 시 잔여 단계만 복구'
ss=rows(OUT/'new_judgment_scenes.jsonl')
s=next(s for s in ss if s['event_id']=='QBF01-U0120-Q01-S01')
old=copy.deepcopy(s['pattern_connections'])
new=old+[{'pattern_id':'설명해상도','case_specific_fit':'일정 조건의 존재를 언급한 수준과 그 인정 절차를 실제 설명한 수준을 대조한다.정보 부재를 현실 절차 부재로 바꾸지 않는다.','definition_source':'분석/패턴_종합연구/20261012_corpus_sweep_01/pattern_candidates.json','definition_reused':True}]
append('scene_amendments.jsonl',[{'amendment_id':'QBF01-AMD017','event_id':s['event_id'],'reason':'8배치 표본 감사: TU의 기존 추론에는 특허 절차의 주체 이전 방지와 조건 언급/절차 설명의 정보 수준 비교가 함께 있다.설명해상도 D/E에 맞는 두 번째 연결을 추가한다.원raw·최초풀이·정답·공통 정의 불변.','changes':[{'field_path':'pattern_connections','old_value':old,'new_value':new}]}])
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV024','pattern_ids':['설명해상도','관계귀속'],
 'evidence_event_ids':['QBF01-U0120-Q01-S01','QBF01-U0121-Q04-S02','QBF01-U0122-Q01-S01'],
 'finding':'TU는 조건이 존재한다는 언급에서 인정 절차를 얻을 수 없고,UC는 위임 사항의 대강 예측과 하위 규정의 구체 내용 확인을 구별한다.UE는 기제라는 공통어에도 화학제→병원체와 세균→사람이라는 다른 관계를 구별한다.',
 'decision':'관계의 대상 일치와 요구 정보 수준 충족을 별도 검사로 유지한다.TU에는 AMD017로 설명해상도를 추가 연결했다.원95정의의 수정이나 신규 후보 분리는 아직 필요하지 않다.',
 'next_counterexample':'같은 대상의 기능만 제시된 경우와 다른 대상의 상세 과정이 제시된 경우를 교차시켜,대상 일치만으로 답이 생기는지 또는 상세함만으로 답이 생기는지 검토한다.',
 'educational_use':'질문마다 무엇에 관해 어느 수준을 묻는가를 두 칸에 적는다.정보의 부재를 현실 존재의 부정으로 바꾸지 않는다.'},
 {'development_id':'QBF01-DEV025','pattern_ids':['단계구분','속성분리','관계귀속'],
 'evidence_event_ids':['QBF01-U0116-Q04-S02','QBF01-U0117-Q02-S01','QBF01-U0123-Q02-S02','QBF01-U0123-Q04-S03'],
 'finding':'SW는 후속 취득 가능성과 앞선 양도인의 소유권 보유가 다르고,TF는 오차 증가 결과가 맞아도 다른 장치의 원인을 붙이면 틀린다.UJ는 정확한 감지가 물리 보정 범위를 늘리지 않으며,UL은 아직 적용하지 않은 DIS의 실패로 현재 영상을 해석할 수 없다.',
 'decision':'같은 결과라는 공통점만으로 원인·발생 경로·성립 시점까지 같게 만드는 오류를 사례별 좌표로 설명한다.이를 모두 한 신규 후보로 합치거나 기존 100코드 유일주 판정으로 환원하지 않는다.TF의 기존46/56유보는 유지한다.',
 'next_counterexample':'동일 결과가 서로 다른 경로로 발생한 사례,정확한 입력에도 출력 범위가 제한되는 사례,처리 전·후 자료를 모두 주는 사례를 대조한다.',
 'educational_use':'결과 옆에 무엇으로/언제/어떤 조건에서라는 근거를 함께 적게 한다.'},
 {'development_id':'QBF01-DEV026','pattern_ids':['조건부방향','범위이동','강도보존'],
 'evidence_event_ids':['QBF01-U0117-Q04-S02','QBF01-U0117-Q04-S03','QBF01-U0120-Q04-S03','QBF01-U0124-Q03-S02'],
 'finding':'TH의 위치 변화는 현재 원 배치와 한 신호만 변한다는 조건에 의존한다.TX는 국가별 소득 경향을 S국의 소득 단계에 적용하는 문항 모형을 사용한다.UO는 다른 변기도 절차를 충족하면 될 수 있다는 조건부 가능성이다.',
 'decision':'도식의 국소 방향을 모든 배치·임의 변화량에,국가 간 경향을 개별 국가의 필연적 시간 경로에,조건부 가능성을 모든 대상의 현재 사실에 확대하지 않는다.TX 적용 가정은 사후 보완 사항으로 명시하며 새로운 관측 사실이나 확정 인과 법칙으로 사용하지 않는다.',
 'next_counterexample':'반지름 증가로 공통영역 변화가 포화되는 배치,국가 간 경향과 반대로 변화하는 개별 국가,같은 재료이지만 자격 수여 절차가 없는 대상을 비교한다.',
 'educational_use':'새 출제에서는 고정 변수·변화 구간·관계의 적용 가정을 명시한다.반전 예시가 원선지의 오류만 제거하는지 새 유일정답까지 보장하는지 구별한다.'}
])
keys=['SW','TF','TH','TK','TU','TX','UC','UJ','UL','UO']
qs=[q for q in rows(OUT/'current_question_reviews.jsonl') if set(q['case_ids'])&set(keys)]
eids={s['event_id'] for q in qs for s in q['scenes']}
assert len(qs)==10 and len(eids)==25
append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT008','batch':8,'date':'2026-10-15','sample_case_ids':keys,'sample_questions':10,'sample_scenes':25,
 'method':'주 에이전트가 현행10문항25장면의 전체50선지,중간추론,적용 한계,반전 예시를 작성 중 직접 읽은 원문·기존풀이 및 후보D/E와 대조했다.TK의5행 전사 복원,TH 도식과UL두프레임의 직접 열람 근거를 확인했다.기존 자료를 활용한 사후 감사이며 신규blind가 아니다.',
 'dimensions':{
 '중간추론':'SW에서 계약별 인도 방식과 독립 선의취득을 구별.TF에서 맞는 결과/틀린 원인을 분리.TH에서 신호→환산거리→도식 위치를 고정 조건 아래 연결.UL에서 회전→빈 영역→절단→크기·내용 손실을 연결.',
 '모든선지':'50개 선지의 실제 문언·검토 이유 확인.TK의 두 열5행에서 누락·오분류를 모두 확인.UC⑤는 현재 동일 광고물 규제에서 신고와 표시 방법을 함께 지키는 구조에 한정.',
 '후보경계':'TU의 조건 존재/절차 설명 차이를 설명해상도 D/E에 연결하는 AMD017 추가.관계귀속과 합치지 않고 두 검사 좌표를 보존.조건부방향을 통계적 경향의 필연적 인과로 사용하지 않음.',
 '원문과이력':'TK 빈 선택지는 기존 보충파일의 전사로 복원한 새폴더 사본.새 원표 시각 검증으로 표현하지 않음.UL 과거 그림 누락hold→복원 후 유효 최초답②를 보존하고 이번 직접 열람은 사후 확인으로 구분.TF 기존46/56유보 유지.',
 '교육출제':'TH의 비포화 조건 및 TX의 동일 경향 적용 가정을 남김.UO의 재현물 변경은 현재 오류 제거이지 모든 이론에서 예술성을 보증하는 수정이 아님.UR 정답 소멸과 새 유일정답 생성의 차이도 별도 경고.'},
 'findings':[
 {'case':'TU','issue':'이미 수행한 정보 수준 비교의 후보 연결 누락','resolution':'AMD017로 설명해상도 추가.기존 관계귀속 유지.'},
 {'case':'TX','issue':'국가 간 경향을 개별 국가의 시간 경로에 적용하는 전제','resolution':'사후 명시된 조건부 적용으로 유지.필연적 관측·인과로 확대하지 않음.'},
 {'case':'TH','issue':'도식 국소 방향을 임의 배치·무한 변화량까지 확대할 위험','resolution':'현재 배치·고정 변수·비포화 조건을 현행 장면에 명시한 상태 확인.'},
 {'case':'TF','issue':'기존 코드 유일주 경계 유보','resolution':'46/56유보를 후보 연결로 해결했다고 집계하지 않음.'}],
 'decision':'중대한 미해결 오류 없이321번부터 계속 진행 가능.명시한 적용 가정과 기존 유보 유지.',
 'unresolved_blocking_error_count':0,'limitations':'표본밖 의미 무오류 보증이 아니며 기존15문항 유보를 해소한 것으로 집계하지 않는다.'}])
refresh();validate()
write('batch_008_validation.json',json.loads((OUT/'validation_report.json').read_text()))
cp=json.loads((OUT/'checkpoint.json').read_text());write('batch_008_checkpoint.json',cp)
h=json.loads((OUT/'session_handoff_20261013.json').read_text())
h.update(date=cp['date'],reviewed_questions=cp['reviewed_questions'],new_scenes=cp['new_scene_count'],by_exam=cp['by_exam'],batch_state='001~008 각40문항 저장·표본 감사 완료.8배치10문항25장면 감사.321번부터9배치 계속.',next_order=cp['next_order'],next_unique_question=cp['next_question'],next_case=cp['next_case_ids'][0],read_but_not_saved=[],last_saved_author='author_008h.py',next_author_suggestion='author_009a.py',resume_command='python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 321 5',validation='320문항475장면 현행증거·offset·hash·선지수·ID검증.보호자산 전수hash 반복검사 생략.')
h['important_corrections'] += ['8배치TU에AMD017로설명해상도추가.원95정의불변.', 'TX의국가간경향→S시간경로적용은사후명시한가정.TH위치변화는현재배치와비포화조건한정.', 'TK는기존전사선택표를새폴더사본으로연결.UL두프레임직접확인.기존hold·유효최초답순서보존.']
write('session_handoff_20261013.json',h)
