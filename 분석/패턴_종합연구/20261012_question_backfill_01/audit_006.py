import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write,refresh,validate
assert not any(r['audit_id']=='QBF01-AUDIT006' for r in rows(OUT/'semantic_sample_audits.jsonl')), '감사 중복 실행 금지'
assert not any(r['amendment_id']=='QBF01-AMD013' for r in rows(OUT/'scene_amendments.jsonl')), '수정 이후의 잔여 단계만 복구할 것'
s=next(s for s in rows(OUT/'new_judgment_scenes.jsonl') if s['event_id']=='QBF01-U0094-Q02-S02')
append('scene_amendments.jsonl',[{
 'amendment_id':'QBF01-AMD013','event_id':s['event_id'],
 'reason':'6배치 표본 감사: NL S02는 여러 이론의 판별 기준을 해당 입장에 귀속하는 검토다. 기준내부검사 E의 글쓴이 수용 조건이 이 비판적 소개문에서 직접 확보되지 않으므로 해당 연결을 제거하고 관계귀속으로 조정한다. 실제 중간 추론·정답·원raw와 동결 정의는 불변.',
 'changes':[{'field_path':'pattern_connections','old_value':copy.deepcopy(s['pattern_connections']),
 'new_value':[{'pattern_id':'관계귀속','case_specific_fit':'분석/종합 구별과 동의적 대체 조건을 누가 주장하고 누가 비판하는지 보존하여 선지의 귀속을 검사한다. 글쓴이가 각 기준을 최종 수용한다고 추정하지 않는다.','definition_source':'분석/패턴_종합연구/20261012_corpus_sweep_01/pattern_candidates.json','definition_reused':True}]}]}])
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV017','pattern_ids':['BFP006','근거망복원','되먹임고리'],
  'evidence_event_ids':['QBF01-U0094-Q02-S01','QBF01-U0099-Q02-S03','QBF01-U0100-Q01-S02'],
  'finding':'NL은 분석명제→동의성→필연성→분석명제라는 정당화 의존의 원점 회귀다. OK는 산성화→L생장→젖산→산성화라는 실제 강화 경로이고 ON은 현재 출력의 오차로 다음 가중치를 고치는 시간적 학습 경로다.',
  'decision':'NL을 BFP006 단일 문항 잠정 후보로 보존한다. 고리 그림이 같아도 정당화의 독립성 검사와 실제 변수 변화의 되먹임을 통합하지 않는다. 근거망복원과의 상위 통합 가능성은 열어 둔다.',
  'next_counterexample':'원점으로 돌아오지만 독립된 외부 근거도 있는 논증,단순 재진술만 반복한 설명,시간 순서만 원형으로 제시되고 인과가 없는 자료를 대조한다.',
  'educational_use':'화살표가 정당화 의존인지 인과 변화인지 먼저 쓰게 하고,원점 회귀의 결함과 강화·조정 효과를 별도로 묻는다.'},
 {'development_id':'QBF01-DEV018','pattern_ids':['기준내부검사','관계귀속','단계구분','수치표상'],
  'evidence_event_ids':['QBF01-U0094-Q02-S02','QBF01-U0092-Q03-S02','QBF01-U0096-Q03-S01','QBF01-U0098-Q03-S01'],
  'finding':'후보의 적용 조건과 수식의 고정 조건을 생략하면 실제 근거보다 넓은 결론이 된다. NL은 입장별 기준 적용이지만 글쓴이의 수용까지 보장하지 않는다. NF는 같은 세기를 같은 광자 수로 연결하는 조건이 미명시다. NW는 확률 고정이,OH는 환산 상수와100%미만 조건이 명시된다.',
  'decision':'NL은 AMD013으로 좁은 귀속 연결로 수정한다. 기준내부검사의 E를 글쓴이 수용뿐 아니라 발문이 지정한 관점 안의 가정적 수용까지 넓힐지는 별도 경계 검토 대상으로 남긴다. NF의 유보를 유지하며 외부 물리식으로 답을 재판정하지 않는다.',
  'next_counterexample':'글쓴이가 거부하는 이론의 내부 규칙만 적용하라고 명시한 문항,같은 세기이되 입력 수가 달라지는 자료,확률이 변하는 보험 비교를 대조한다.',
  'educational_use':'각 화살표에 필요한 관점·단위·고정량을 표시하고 명시/보기 제공/연구자 가정으로 구별한다.'},
 {'development_id':'QBF01-DEV019','pattern_ids':['단계구분','요건순서','필요요건역전금지','속성분리'],
  'evidence_event_ids':['QBF01-U0096-Q05-S01','QBF01-U0096-Q05-S02','QBF01-U0100-Q03-S01','QBF01-U0103-Q01-S01'],
  'finding':'NY는 해지권과 지급 책임의 다른 제한 및 계약 전 고지 시점을 구별한다. PB는 앞 단계 산출을 다음 단계에서 다시 선별하므로 선행 요건을 보존한다. OP는 특징을 다른 단자로 넣는 공간적 분리를 데이터 사례의 분할과 구별한다.',
  'decision':'단계라는 이름만으로 절차의 선후·효과의 분리·자료 단위의 분할을 통합하지 않는다. PB의 선행 조건은 필요한 것이지 그것만으로 최종 수록을 보장하는 충분조건이 아니다. NY의 미고지에 고의/중과실을 덧붙이지 않는다.',
  'next_counterexample':'중간 단계를 건너뛰는 별도 허용 경로,다른 단계가 독립 자료를 받는 절차,동일 사례의 특징 분리와 실제 사례 분할을 대조한다.',
  'educational_use':'단계별 입력 집합·출력 집합·성립 요건을 쓰고 효과별 예외는 별도 칸에 기록한다.'}
])
keys=['NF','NL','NS','NW','NY','OH','OK','ON','OP','PB']
sample=[r for r in rows(OUT/'current_question_reviews.jsonl') if set(r['case_ids']) & set(keys)]
append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT006','batch':6,'date':'2026-10-15',
 'sample_case_ids':keys,'sample_questions':len(sample),'sample_scenes':sum(len(r['scenes']) for r in sample),
 'method':'주 에이전트가 이번 작성에서 읽은 원문·기존 개별 풀이·복원 보충자료에 비추어 10문항19장면의 중간 추론·다섯 선지·후보 조건을 재검토. NS/OH는 기존 복원 앵커와 새 사본을 대조. 신규 blind나 원배포 PDF 전수 검증은 수행하지 않음.',
 'dimensions':{
  '원문 복원':'NS의 헤더ⓐⓑⓒ와5행㉮㉯㉱/㉮㉰㉯/㉱㉮㉰/㉱㉯㉰/㉱㉰㉯를 보충파일 문단에 대조. 보기 cell주소와 선택지 문단을 구별. OH는 equation {B} over {A} 및 앞뒤 앵커를 확인. 새 사본에만 보강했으며 원본 누락과 당시 hold 이력은 유지.',
  '중간 추론':'NW에서 보험료=기댓값=p×보험금과A/B확률1:2를 각 가정별 적용. OH는 B<kA→B/A<k로 단위를 보존. OK에서5.0이하는F5.8이하 및S5.5미만 한계를 모두 통과하며S의 초기 증가와 최종 사멸을 구분.',
  '후보 조건':'NL의 정당화 순환은BFP006으로 잠정 분리. S02의 기준내부검사 E를 확인한 뒤 AMD013으로 관계귀속만 연결. 원95정의 수정 없이 경계 검토 사항은DEV018에 저장.',
  '다중 장면':'NY의 효과별 예외/시점,ON의 고정 기준/오차 되먹임,OP의 데이터 단위/레이블 설정,PB의 순차 요건/규정 미개정을 별도로 보존.',
  '이력과 가정':'NF⑤의 광자 수 고정 연결 유보를 유지. NS/OH 최초 보류→자료 복원→유효 최초 답의 순서를 사후 성과와 구별. NY 미고지에 정신적 요건을 임의 보강하지 않음. OP의 표기 변경은 처음부터 일관된 학습 설정이며 기존 가중치 재해석 성과가 아님.'},
 'findings':[
  {'case':'NL','issue':'기준내부검사 E의 글쓴이 수용 조건이 확보되지 않은 이론별 기준 검토','resolution':'AMD013으로 관계귀속에 연결. 후보 E 확장 가능성은DEV018의 잠정 경계 문제로 분리'},
  {'case':'NF','issue':'같은 세기와 같은 광자 수의 연결이 파장 변경에도 유지되는지 미명시','resolution':'공식답③과 기존 정성⑤ 적용을 보존하되 입력량 유보 유지. 확정 생성 규칙으로 일반화하지 않음'},
  {'case':'NS/OH','issue':'원본의 일부 선택지 열·비율식 누락','resolution':'기존 복원파일을 근거로 새 폴더 사본만 보강. 원본·최초 hold 이력 불변'}],
 'decision':'후보 연결 수정 반영 후 241번부터 계속 진행 가능','unresolved_blocking_error_count':0,
 'limitations':'표본 밖 의미 무오류 보증이 아니다. NF와 이전 배치의 명시 유보는 해소된 것으로 집계하지 않는다.'}])
refresh()
validate()
write('batch_006_validation.json',json.loads((OUT/'validation_report.json').read_text()))
cp=json.loads((OUT/'checkpoint.json').read_text())
write('batch_006_checkpoint.json',cp)
h=json.loads((OUT/'session_handoff_20261013.json').read_text())
h.update(date=cp['date'],reviewed_questions=cp['reviewed_questions'],new_scenes=cp['new_scene_count'],by_exam=cp['by_exam'],
 batch_state='001~006 각40문항 저장·표본 감사 완료. 006감사에서 NL S02 후보 연결 조정. 241번부터7배치 계속.',
 next_order=cp['next_order'],next_unique_question=cp['next_question'],next_case=cp['next_case_ids'][0],read_but_not_saved=[],
 last_saved_author='author_006h.py',next_author_suggestion='author_007a.py',
 resume_command='python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 241 5',
 validation='240문항326장면의 현행 증거·offset·hash·선지수·ID 검증 통과. 보호 자산 전수 hash 반복 검사 생략.')
h['important_corrections'] += ['NL S02는 AMD013으로 기준내부검사 대신 관계귀속 연결. BFP006 정당화 순환은 단일 문항 잠정 후보다.', 'NS 선택지와OH 비율식은 기존 복원 보충자료를 새 폴더 사본에 연결했다. source_overrides.json의 경로를 사용하며 기존 원문은 불변.', 'NF⑤의 같은 세기→같은 광자 수 연결은 미확인 조건으로 유보. 최초 한계의 사후 구체화이며 공식답③ 변경 없음.']
write('session_handoff_20261013.json',h)
