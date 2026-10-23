import sys,copy,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write,refresh,validate,evidence,BYCASE

if any(r['audit_id']=='QBF01-AUDIT004' for r in rows(OUT/'semantic_sample_audits.jsonl')):
    raise RuntimeError('이미 저장된 감사. 재실행하지 않는다.')
if any(r['amendment_id']=='QBF01-QAMD003' for r in rows(OUT/'question_amendments.jsonl')):
    raise RuntimeError('수정은 저장됨. 감사의 잔여 단계만 별도로 복구해야 한다.')

r=next(r for r in rows(OUT/'raw_question_reviews.jsonl') if r['unique_question']=='U0067-Q03')
old=copy.deepcopy(r['scenes'])
a=copy.deepcopy(old[0]); b=copy.deepcopy(old[0]);q=BYCASE['JY']
a.update(title='같은 네 측정값에서 전체합·좌우차·전후좌우 합차를 각각 계산',
 student_start='전체 빛의 양, 트래킹 편차, 초점 편차가 같은 산식으로 판정되는지 확인한다.',
 passage_information_structure='네 출력의 총합은 총량, 좌−우는 트래킹 편차, (전+후)−(좌+우)는 초점 편차를 나타낸다.',
 item_information_operation='①은 총합 대소를 반전하고②③은 서로 다른 산식이 판정하는 구동 필요 여부를 뒤집는다.',
 option_numbers=[1,2,3,5],
 intermediate_inference_steps=['상태1은 총합8, 좌우차2, 초점합차0이다.','상태2는 총합16, 좌우차0, 초점합차4다.','따라서 상태1은 트래킹 편차만, 상태2는 초점 편차만 있다.','①②③은 이 결과와 어긋난다.⑤의 상태1 거리 조절 불필요는 맞지만 상태2의 보정 방향은 별도 단계에서 검사한다.'],
 conclusion='①②③ 배제.⑤의 구동 필요 여부는 지지되며 이동 방향은S02에서 검토.',
 original_observed_behavior='기존 JY 풀이의 세 지표 계산을 활용. 기존 보완S01에 함께 저장된 계산과 보정 방향을 이번 감사에서 분리함.')
a['option_evidence']=[evidence(q,{'quote':__import__('backfill_io').source(q)['choices'][i-1],'option':i}) for i in a['option_numbers']]
a['educational_production'].update(
 logical_invariants='동일한 원자료라도 목적에 따라 다른 집계식과0 기준을 적용한다.',
 answer_flipping_minimal_change='상태1의 좌3·우1을 좌2·우2로 바꾸면 총합8과 초점합차0은 유지되지만 트래킹 구동 필요는 사라진다. 복합 선지 전체의 정오 변화와 구별한다.',
 truth_preserving_changes='모든 출력에 동일 상수를 더하면 좌우차와 합차는 유지되지만 총합은 달라진다.',
 ambiguity_or_insufficient_evidence_risk='새 표는 어느 지표를 묻는지와 지표별 산식을 명시해야 한다. 한 지표 불변을 모든 판정 불변으로 확대하지 않는다.',
 teachable_reading_action='전체합·좌우차·초점합차를 별도 칸에 계산하고 각 값이 설명하는 상태를 적는다.')
b.update(event_id='QBF01-U0067-Q03-S02',title='편차의 현재 방향에서 그 편차를 줄이는 보정 방향으로 전환',
 student_start='④⑤에서 어디로 치우쳤는가와 어디로 움직여야 하는가를 다른 질문으로 읽는다.',
 passage_information_structure='좌영역 우세는 왼쪽 치우침이므로 오른쪽으로 보정한다. 전후합 우세는 렌즈가 너무 가까운 상태이므로 거리를 늘린다.',
 item_information_operation='④는 오른쪽 보정 방향을 현재 광선의 오른쪽 치우침으로 잘못 옮긴다.',
 intermediate_inference_steps=['상태1 좌우차가 양수이므로 현재 광선은 왼쪽으로 치우쳤다.','오른쪽 이동은 그 편차를 고치는 조치이지 현재 편향의 위치가 아니다.','상태2의 전후합 우세는 렌즈와 기록면의 거리가 너무 가깝다는 신호다.','그 상태를 정상으로 되돌리려면 거리를 늘려야 하므로⑤가 맞는다.'],
 option_numbers=[4,5],conclusion='④는 현재 상태와 보정 방향을 혼동하며⑤는 올바른 거리 보정이다.',
 non_applicable_conditions='모든 제어가 무조건 반대 방향인 것은 아니다. 본문이 제시한 지표와 거리·위치 변화의 대응을 먼저 확인한다.',
 pattern_connections=[{'pattern_id':'조건부방향','case_specific_fit':'출력 부호→현재 편차→정상 상태로 되돌릴 조치의 방향을 연결한다.','definition_source':'분석/패턴_종합연구/20261012_corpus_sweep_01/pattern_candidates.json','definition_reused':True}],
 original_observed_behavior='JY 최초풀이의 현재 편향/보정 방향 구별을 재사용한다. 이번S02 분리는 사후 기록 구조 보완이며 새로운 blind 발견이 아니다.')
b['passage_evidence']=[evidence(q,t) for t in ['좌측으로 치우치면','광 픽업 장치를 오른쪽으로 움직여서 편차를 보정','거리가 가까워져 광선의 초점이 맞지 않으면']]
b['option_evidence']=[evidence(q,{'quote':__import__('backfill_io').source(q)['choices'][i-1],'option':i}) for i in b['option_numbers']]
b['educational_production'].update(
 logical_invariants='관측이 알려 주는 현재 상태와 그 상태를 바꾸기 위한 제어 명령은 다른 값이다.',
 answer_flipping_minimal_change='상태2 전후를3·3,좌우를5·5로 바꾸면 초점합차 부호가 바뀌어 거리를 줄여야 한다. 총합과 트래킹 무편차는 유지된다.',
 truth_preserving_changes='상태2의 모든 출력을 같은 양의 배율로 확대하면 초점합차의 부호가 같아 거리 증가 방향은 유지된다. 보정량까지 같다고 하지는 않는다.',
 ambiguity_or_insufficient_evidence_risk='새 제어 문항에서는 검출기 좌우와 조절 장치 좌우의 기준을 맞춰야 한다. 센서 설치 방향이 뒤집히면 대응을 새로 제공해야 한다.',
 teachable_reading_action='관측값→현재 편향→목표 상태→수정 방향을 순서대로 적고 마지막 방향을 현재 상태 자리에 넣지 않는다.')
append('question_amendments.jsonl',[{'amendment_id':'QBF01-QAMD003','unique_question':r['unique_question'],
 'reason':'4배치 표본 감사: 기존JY S01의 목적별 지표 계산과 편차 보정 방향 판단은 다른 조작이므로 두 장면으로 분리. 기존 raw·정답·최초풀이 불변.',
 'changes':[{'field_path':'scenes','old_value':old,'new_value':[a,b]}]}])

append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV011','pattern_ids':['BFP005','병렬경로','필요요건역전금지'],
  'evidence_event_ids':['QBF01-U0070-Q02-S03'],
  'finding':'KG는 복수 단서 중 귓바퀴 단서만 손상시킨 뒤 잔존 시간차로 전면 불능을 반박한다. 공통 원인에서 갈라지는 결과 사이의 인과 검사와는 다르다.',
  'decision':'대체 단서 잔존을BFP005 단일 문항 잠정 후보로 저장. 기존95정의는 수정하지 않으며 필요성 과장의 상위 계열과 통합할지는 추가 사례에서 판단한다.',
  'next_counterexample':'여러 단서가 실제로 모두 필수인 경우, 제거 조작이 공통 입력을 끊어 잔존 단서도 소실하는 경우, 단서가 남아도 문턱에 미달하는 경우를 대조.',
  'educational_use':'손상된 단서·남은 단서·전체 정확도의 세 칸을 분리하고 남았다는 사실에서 동일 정확도까지 주장하지 않게 한다.'},
 {'development_id':'QBF01-DEV012','pattern_ids':['수치표상','기준내부검사','누락연결전제'],
  'evidence_event_ids':['QBF01-U0068-Q03-S01','QBF01-U0072-Q03-S01','QBF01-U0070-Q01-S01'],
  'finding':'KB는 제시 A/C그래프의 기여비 모형으로 구간별 값을 합성한다. KP는 토양보다 낮다는 제약으로 후보를 검증하며 완전한 시간곡선을 도출하지 않는다. KF는 상위 변인의 의존을 하위 방향 축으로 옮길 근거가 부족하다.',
  'decision':'수치·그래프 문항을 동일 연산으로 통합하지 않는다. 주어진 모형으로 생성 가능한 결과와 제약으로 배제만 가능한 후보를 구분하며 KF유보를 해소된 기준으로 사용하지 않는다.',
  'next_counterexample':'동일 제약을 만족하는 그래프가 둘 이상인 자료, 방향과 거리 중 한 축만 정확도에 영향을 주는 자료를 제시하면 추가 근거 필요가 드러나는지 검토.',
  'educational_use':'각 추론에 본문 명시·보기 제공 모형·연구자 보강 가정 중 어느 것이 쓰였는지 붙인다.'},
 {'development_id':'QBF01-DEV013','pattern_ids':['수치표상','조건부방향','행위결과분리'],
  'evidence_event_ids':['QBF01-U0067-Q03-S01','QBF01-U0067-Q03-S02','QBF01-U0071-Q02-S01'],
  'finding':'JY의 현재 편차와 수정 방향, KK의 반증 시도와 가설의 실제 결과는 서로 다른 단계를 구별해야 한다. 둘 다 과정이라는 상위명만으로 동일 패턴은 아니다.',
  'decision':'JY는QAMD003으로 장면 분리. 산식 선택·부호 해석과 행동/결과의 증거 구별을 별도로 보존한다.',
  'next_counterexample':'같은 수정 명령이 다른 현재 상태에서 나온 경우, 반증 시도는 있으나 결과가 보고되지 않은 경우를 비교.',
  'educational_use':'현재 상태/목표/조치/결과를 필요에 따라 분리하되 해당 지문에서 실제 연결된 항만 채운다.'}
])

append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT004','batch':4,'date':'2026-10-13',
 'sample_case_ids':['IX','JY','KB','KF','KG','KK','KP','KT','KU'],'sample_questions':9,'sample_scenes':15,
 'method':'주 에이전트가 현행 수정 적용 분석과 기존 풀이·원문을 직접 비교. KB보기/5선지 및KP5선지를 직접 열람. 전수 재풀이·모델 비교·원배포PDF 전수대조는 하지 않음.',
 'dimensions':{
  '원문 연결':'IX의 복원②는 스트로슨의 의존방향을 반전한다.③은 양 입장을 한 선택지로 보존. JY표의상태1(2,2,3,1)·상태2(5,5,3,3)을 로컬 보충표와 대조. KB/KP한국어 그림 설명은 관찰전사임을 명시.',
  '중간 추론':'JY의합8/16·좌우차2/0·합차0/4와 보정방향을 확인. KB의s,1,3−s구간 합은 주어진 선형기여 모형 안에서 검토. KP는끝점 제약으로 선택하며 세부동역학은 유보.',
  '공통 정의와 사례 활용':'KG의대체 단서 잔존은 병렬경로의기존D에 억지로 포함하지 않고BFP005로잠정 분리. KT는비유 명칭과 실제 분류행동을 구별.각 활용은 해당 문항의변수·관계를 바꾸며 다른 기출 예시의이식은 표본에서 확인되지 않음.',
  '근거 이력':'IX최초 잘못 연결된선지 및이후QAMD002/AMD010·011을보존. KT최초 코드와후속depth 우선순위 변경을구별. KF추론한계는이번보완의 발견이며최초판정으로 소급하지 않음.',
  '다중 장면':'JY의계산과보정방향은QAMD003으로분리. KG3장면, KU2장면은정보종류·잔존단서·형태귀속·힘방향등판단대상 차이에 근거함.'},
 'findings':[
  {'case':'JY','issue':'하나의 장면에 지표 계산과 보정 방향 판단이 결합됨','resolution':'QBF01-QAMD003으로S01/S02분리, 원raw불변'},
  {'case':'KF','issue':'위치 의존으로부터 방향별 정확도 의존을 확정할 근거 부족','resolution':'기존 유보 유지. 공식답을 재판정한 것이 아니며 확정 생성규칙으로 채택하지 않음'},
  {'case':'KB/KP','issue':'실제 물리의 일반법칙이나 상세시간함수로 확대할 위험','resolution':'보기 모형과 제약 검사의 범위를 유지. 직접 시각 확인과 원배포PDF 검증은 구별'}],
 'decision':'장면 분리 반영 후161번부터 계속 진행 가능',
 'unresolved_blocking_error_count':0,
 'limitations':'9문항 의미 표본 감사다. KF 등의 명시된 근거 유보는 남아 있으며 표본 밖의 의미 무오류를 보증하지 않는다.'}])
refresh()
validate()
write('batch_004_validation.json',json.loads((OUT/'validation_report.json').read_text()))
write('batch_004_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
handoff=json.loads((OUT/'session_handoff_20261013.json').read_text())
cp=json.loads((OUT/'checkpoint.json').read_text())
handoff.update(status='재개·진행 중',reason='사용자 재개 지시 반영',reviewed_questions=cp['reviewed_questions'],new_scenes=cp['new_scene_count'],by_exam=cp['by_exam'],
 batch_state='001~004각40문항 저장·표본 감사 완료.004감사에서JY장면 분리.161번부터5배치 계속.',
 next_order=161,next_unique_question=cp['next_question'],next_case=cp['next_case_ids'][0],read_but_not_saved=[],
 last_saved_author='author_004h.py',next_author_suggestion='author_005a.py',
 resume_command='python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 161 5',
 validation='160문항205장면에서각증거 파일·offset·hash·선지수·장면ID 기계검증 통과.보호자산 전수hash 반복검사 생략.',
 current_session_delegation='이번 재개 세션에서보조모델 호출 없음. 심층판단·시각판독·의미감사 모두주에이전트 직접 수행.')
handoff['important_corrections'].append('JY는QAMD003으로 목적별 지표계산과현재편차→보정방향을2장면으로분리.기존raw불변.')
write('session_handoff_20261013.json',handoff)
