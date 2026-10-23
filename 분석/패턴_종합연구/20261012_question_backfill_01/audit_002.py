from backfill_io import *
import collections,copy
candidate('BFP004','사건 성립 조건과 성립 후 처리 규칙 분리','어떤 사건이 성립한 뒤 결함·위반에 따라 발생하는 책임 또는 후속 처리를,그 사건 자체가 성립하기 위한 선행 필수조건으로 옮겼는지 검사한다.','본문이 사건 성립과 결함의 양립 사례 또는 명시적인 단계별 요건을 제공해야 한다.','단계구분의 산출값 전달과 다르고 요건순서의 필요한 조건 간 순서 비교와도 다르다. 후속 처리 규칙에서 앞 사건의 필수조건을 역산하는 오류를 좁게 묶는 잠정 후보. 단일 실제 문항이므로 독립 패턴 확정 아님.')
scenes=rows(OUT/'new_judgment_scenes.jsonl'); by={x['event_id']:x for x in scenes}
x=by['QBF01-U0037-Q02-S01'];old=x['pattern_connections'];new=copy.deepcopy(old)
for p in new:
 if p['pattern_id']=='단계구분':
  p.update(pattern_id='BFP004',case_specific_fit='체결 당시 값어치가 부족한 계약도 이미 체결된 것으로 전제하므로 담보 책임을 등가라는 계약 체결 요건으로 바꿀 수 없다.',definition_source=str(OUT.relative_to(ROOT)/'new_pattern_candidates.jsonl'))
append('scene_amendments.jsonl',[dict(amendment_id='QBF01-AMD005',event_id=x['event_id'],reason='기존 단계구분 정의의 산출값 전달과 다른 판단이므로 좁은 신규 잠정 후보로 연결을 분리한다.',changes=[dict(field_path='pattern_connections',old_value=old,new_value=new)])])
x=by['QBF01-U0027-Q01-S01'];old=x['pattern_connections'];new=[p for p in old if p['pattern_id']!='실행조건']
append('scene_amendments.jsonl',[dict(amendment_id='QBF01-AMD006',event_id=x['event_id'],reason='실행조건 공통 정의의 다른 규정과 허용 조건 대조까지 수행한 장면이 아니므로 과넓은 연결을 제거한다. 접근성/숙련의 속성분리는 유지한다.',changes=[dict(field_path='pattern_connections',old_value=old,new_value=new)])])
refresh()
scenes=rows(OUT/'new_judgment_scenes.jsonl'); reviewed=rows(OUT/'raw_question_reviews.jsonl'); batchq={r['unique_question'] for r in reviewed if r['batch_number']==2};batchsc=[s for s in scenes if s['unique_question'] in batchq]
common={v[k] for v in PATTERNS.values() for k in ['D','E','F']}
strings=[]
for s in batchsc:
 strings.extend([s[k] for k in ['student_start','passage_information_structure','item_information_operation','non_applicable_conditions']])
 strings.extend(s['educational_production'][k] for k in ['logical_invariants','answer_flipping_minimal_change','truth_preserving_changes','ambiguity_or_insufficient_evidence_risk','teachable_reading_action'])
exact=sum(s in common for s in strings)
prod=[s['educational_production'][k] for s in batchsc for k in ['logical_invariants','answer_flipping_minimal_change','truth_preserving_changes','ambiguity_or_insufficient_evidence_risk','teachable_reading_action']]
dup=[{'text':k,'count':n} for k,n in collections.Counter(prod).items() if n>1]
append('semantic_sample_audits.jsonl',[dict(audit_id='QBF01-AUDIT002',batch=2,date='2026-10-13',sample_case_ids=['ED','EX','BRN','FB','FC','FI','FK','GA'],sample_questions=8,sample_scenes=12,
 method='주 에이전트가 열람한 원문·기존 풀이·현재 저장 장면을 대조. 기존95후보 D정의도 연결 목록과 함께 확인함. 전 배치 원문 재풀이 아님.',
 dimensions={'원문 연결':'EX는 보기뿐 아니라 본문 참 보존 구간을 AMD002로 추가. BRN은 기존 시각 검증 완료 이력을 사용. FI는 누락 열을 기존 supplement 전체와 연결하며 원문 결손과 복원 단계를 분리.','공통 설명 복사':{'개별필드_기존DEF_완전일치':exact,'개별활용_완전중복':dup,'직접 표본 판정':'다른 기출의 제작 예시를 가져온 경우 없음. 완전일치 검사는 의미상 복사까지 자동 보증하지 않음.'},'중간 추론':'FC 일정비→동일 배율→기울기1,FB 생성열=발산열의 조건,FK 소유·통합 주체의 전제와 지각 이후 확정의 대비,GA 체결·하자 양립 사례의 반례 기능을 확인.','근거 상태':'기존 최초·정답 확인·depth·source hold payload 분리. BRN의 해소된 hold를 현재 미해결로 재등록하지 않음. FI의 로컬 표 복원을 공식 PDF 독립 확인으로 확대하지 않음.','제작 활용':'복합 선지의 한 절 수정과 선지 전체 정답화를 구별. 다른 정답 유지 시 복수정답 가능성 기록.'},
 findings=[{'case':'FI','issue':'두 빈칸의 동시 충족을 합산요건에 연결한 것이 기존 정의와 맞지 않음','resolution':'AMD004로 복수문턱 연결로 수정·원raw 보존'}, {'case':'ED','issue':'다른 규정과의 허용 조건 대조가 없는 장면을 실행조건에 연결함','resolution':'AMD006으로 과넓은 연결 제거'}, {'case':'GA','issue':'산출값 전달을 다루는 단계구분 정의만으로 책임/성립 요건 전환을 충분히 구별하지 못함','resolution':'AMD005·BFP004로 별도 잠정 후보 연결. 기존95정의 불변'}],
 decision='연결 수정과 근거 보완 반영 후 세 번째 배치 계속',unresolved_blocking_error_count=0,limitations='8문항의 의미 표본 감사. 모든 문항의 무오류를 뜻하지 않으며 후보의 통합·독립성은 추가 사례에서 검증한다.')])
append('pattern_development.jsonl',[
 dict(development_id='QBF01-DEV005',pattern_ids=['어휘행동','행위결과분리'],evidence_event_ids=['QBF01-U0030-Q04-S01','QBF01-U0031-Q05-S01','QBF01-U0035-Q06-S01','QBF01-U0036-Q05-S01'],finding='은폐/기만,주장 전개/전파는 행위가 낳을 수 있는 결과로 동의어를 판정할 수 없음을 보여 준다. 정착/의지 강화,숭상/믿음은 추상적인 말 사이에서도 변화·태도의 핵심 성분이 다르다.',decision='어휘행동 내부에 논항·행위/결과·변화 속성·평가 태도의 검토 축을 제안. 독립 패턴 분할은 미확정.',next_counterexample='핵심 성분 차이에도 문맥상 치환이 허용되는 CP류와 비교하여 사후 정답 정당화 여부 검증.',educational_use='단어만 표시하지 말고 목적어와 전후 상태 또는 태도 성분을 짧은 뜻풀이로 써서 비교한다.'),
 dict(development_id='QBF01-DEV006',pattern_ids=['속성분리','분류기준','포함반례'],evidence_event_ids=['QBF01-U0035-Q01-S01','QBF01-U0035-Q03-S01','QBF01-U0035-Q04-S01'],finding='법적/사회적 분류 층위,진입 기회/집단 위계,일부 허용/모든 이 허용은 서로 다른 질문이다. 진입 개방과 위계 유지가 양립하는 사례가 반복 확인된다.',decision='공통 하위 독해 행동은 비교축을 명명하는 것. 층위 혼동·속성 결합·전칭 반례는 근거 연산이 달라 하나의 패턴으로 즉시 합치지 않는다.',next_counterexample='진입 규칙 자체가 위계 해체를 수반하도록 설계된 사례에서 적용 경계 검증.',educational_use='지문을 새로 설계할 때 선발 기준,선발 대상 범위,진입 후 권한을 독립적으로 조정하여 다른 오답을 만들 수 있다.'),
 dict(development_id='QBF01-DEV007',pattern_ids=['BFP004','단계구분','요건순서'],evidence_event_ids=['QBF01-U0037-Q02-S01','QBF01-U0035-Q02-S01'],finding='FP는 단계별 수단 배치의 교환이고 GA는 이미 성립한 사건의 책임 조건을 성립 필요조건으로 옮긴다. 시간 어휘가 있다는 공통성만으로 같은 연산이라고 할 수 없다.',decision='GA를BFP004로 잠정 분리하고 기존 단계구분 정의는 유지한다.',next_counterexample='규정상 후속 책임이 성립 취소를 명시적으로 수반하는 사례에서는 결론이 달라지는지 확인.',educational_use='사건 성립과 결함이 함께 성립하는 사례를 준 뒤 책임 규칙을 성립조건으로 오독한 선택지를 검토하게 한다.')])
validate()
write('batch_002_validation.json',json.loads((OUT/'validation_report.json').read_text()))
write('batch_002_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
