import sys
sys.dont_write_bytecode=True
from backfill_io import *
import collections,copy
scenes=rows(OUT/'new_judgment_scenes.jsonl');by={s['event_id']:s for s in scenes}
for aid,eid,pid,replacement,reason in [
 ('QBF01-AMD007','QBF01-U0050-Q02-S01','직전상태갱신',None,'기존 정의는 입력마다 상태 유지/반전을 계산한다. SSTF의 다값 위치 재설정·남은 요청 재비교는 그 정의보다 넓으므로 연결을 제거하고 기준내부검사를 유지한다.'),
 ('QBF01-AMD008','QBF01-U0048-Q03-S02','직전상태갱신',('표현기능판독','조바꿈 뒤 현재 다장조와 기쁨의 표현 기능을 대응한다. 상태 재설정이라는 하위 행동은 별도 귀납 대상으로 남긴다.'),'라단조→다장조의 명시적 조바꿈은 기존 유지/반전 계산과 동일하지 않다. 정의를 임의 확장하지 않고 현재 표현 기능과 연결한다.'),
 ('QBF01-AMD009','QBF01-U0037-Q04-S01','관계전이',None,'주채무와 보증채무의 소멸 규칙은 본문에 직접 명시되어 있다. 매개를 거친 관계 전이의 타당성 검사를 별도 수행한 장면으로 확대하지 않는다. 속성분리를 유지한다.')]:
 s=by[eid];old=s['pattern_connections'];new=[copy.deepcopy(p) for p in old if p['pattern_id']!=pid]
 if replacement:
  new.append(dict(pattern_id=replacement[0],case_specific_fit=replacement[1],definition_source='분석/패턴_종합연구/20261012_corpus_sweep_01/pattern_candidates.json',definition_reused=True))
 append('scene_amendments.jsonl',[dict(amendment_id=aid,event_id=eid,reason=reason,changes=[dict(field_path='pattern_connections',old_value=old,new_value=new)])])
refresh()
scenes=rows(OUT/'new_judgment_scenes.jsonl');rr=rows(OUT/'raw_question_reviews.jsonl');bq={r['unique_question'] for r in rr if r['batch_number']==3};bs=[s for s in scenes if s['unique_question'] in bq]
common={v[k] for v in PATTERNS.values() for k in ['D','E','F']};texts=[];prod=[]
for s in bs:
 texts.extend(s[k] for k in ['student_start','passage_information_structure','item_information_operation','non_applicable_conditions'])
 prod.extend(v for k,v in s['educational_production'].items() if k!='status')
texts+=prod
append('semantic_sample_audits.jsonl',[dict(audit_id='QBF01-AUDIT003',batch=3,date='2026-10-13',sample_case_ids=['GC','GL','GZ','HD','HL','HQ','HT','HW','HP'],sample_questions=9,sample_scenes=12,
 method='원문과 기존 풀이·직접 판독한 그림을 사용한 저장 분석을 재검토. HD/HL 문장과 조건을 다시 대조하고 공통 패턴의 정의도 확인. 모든 원배포 PDF를 대조한 것은 아님.',
 dimensions={'원문 연결':'GL의 자극·응답 왕복 경로, GZ의 움직이는 기준/고정 기준, HD의 공통 시작·끝값, HL의 외부 방해 없음 정의를 확인. HQ/GZ의 복원 선택지는 원본 불변 파생 source와 보조 자료에 연결됨.','공통 설명 복사':{'기존DEF_완전일치':sum(t in common for t in texts),'제작필드_완전중복':[{'text':t,'count':n} for t,n in collections.Counter(prod).items() if n>1],'한계':'문자열 일치 검사는 의미상 독창성 보증이 아니며 표본은 사례별 근거 연결로 판단함.'},'구체 추론':'HD는 기준값에서 변화량의 50/90% 높이를 정하고 시간 비교. HL은 접촉 정지와 자유 변형 완료의 끝 사건 구별. HT는 두 출력의 반대 방향 및 하한/실제값 분리. HW는 첫 선택과 요청 끝/물리 끝에서 규칙을 구별함.','근거 이력':'GZ의 최초①·잘못 연결한 공식⑤·동일 시험형① 대조 해소를 모두 보존. GL 수식 정규화와 원표기 미검증, HL 그림 미확보는 현재 유보로 유지.','제작 활용':'도착 검출기 위치, 두 센서의 서로 다른 기준값, SCAN/LOOK의 같은 경로가 나오는 입력 등 적용 실패 조건이 개별 장면과 연결됨.'},
 findings=[{'case':'HW/HP','issue':'유지/반전이라는 기존 정의보다 넓은 다값 재설정을 직전상태갱신으로 연결','resolution':'AMD007/008로 과넓은 연결 수정. 두 행동의 상위 통합 여부는 DEV010에서 유보.'},{'case':'GC','issue':'직접 명시된 소멸 규칙의 사용을 매개 관계 전이 검사로 확대','resolution':'AMD009로 중복 연결 제거·속성분리 유지'}],
 decision='수정 후 네 번째 배치 계속',unresolved_blocking_error_count=0,limitations='표본 밖 의미 오류의 부재를 보증하지 않으며 현재 9문항의 일부 근거 유보는 완료 처리와 구별한다.')])
append('pattern_development.jsonl',[
 dict(development_id='QBF01-DEV008',pattern_ids=['수치표상','속성분리','기준내부검사'],evidence_event_ids=['QBF01-U0044-Q03-S01','QBF01-U0047-Q03-S02','QBF01-U0042-Q03-S01'],finding='최종 변화의 비율, 그 비율까지의 도달 시간, 관찰 정지와 정의상 완료는 다른 양이다. GV의 민감도와 가격 수준 구별도 비교량 명명의 필요성을 보여 준다.',decision='공통 교육 행동은 지표의 산식·시작 사건·끝 사건 명시. 그래프 좌표 비교와 종료조건 충족 검사는 별개 연산으로 보존한다.',next_counterexample='시작·끝값이 다른 센서 또는 접촉 없이 멈춘 장치에서 기존 판단이 달라지는지 검토.',educational_use='새 자료는 기준값 차이와 종료 원인을 독립 변인으로 설계하여 숫자만 바꾼 복제를 피한다.'),
 dict(development_id='QBF01-DEV009',pattern_ids=['기준내부검사','어휘행동'],evidence_event_ids=['QBF01-U0045-Q01-S01','QBF01-U0045-Q02-S01','QBF01-U0049-Q04-S01'],finding='HF의 판정 가능성과 참임, HG의 유의미성 기준과 기준을 설명하는 문장, HU의 측정 의미와 실제 성공·정확성은 서로 다른 층위다.',decision='진리성·의미·수행 결과를 한 축으로 통합하지 않는다. 문장에 어떤 기준을 적용하는지 먼저 특정하는 교육 절차로 연결한다.',next_counterexample='실제 성공을 어휘 정의의 필수 성분으로 삼는 행위어에서는 실패한 수행의 포함 여부를 다시 검토한다.',educational_use='성공/실패 여부만으로 행위어 뜻을 판정하지 않게 하되 결과가 정의의 일부인 경우도 함께 비교한다.'),
 dict(development_id='QBF01-DEV010',pattern_ids=['직전상태갱신','기준내부검사','표현기능판독'],evidence_event_ids=['QBF01-U0048-Q03-S02','QBF01-U0050-Q02-S01'],finding='조바꿈은 적용할 의미 대응표의 현재 값 변경이고 SSTF는 위치·잔여 요청 갱신 후 거리 재비교다. 기존 유지/반전 정의와 모두 상태를 갱신한다는 상위 행동을 공유하지만 실제 연산은 다르다.',decision='기존 후보 정의 불변. 두 문항의 직전상태갱신 연결 제거 후 넓은 상태 갱신 계열의 상위화 또는 분리 여부는 잠정 검토 대상으로 보존.',next_counterexample='초기 상태 참조가 여전히 유효한 규칙, 전체 이력이 필요한 규칙과 비교해 현재값만 유지하는 절차의 경계를 확인한다.',educational_use='현재값과 누적 이력을 별도 칸에 기록하고 다음 판단에 필요한 쪽만 참조하게 한다.')])
# 귀납의 event ID를 저장된 장면에 대조한다.
known={s['event_id'] for s in scenes}
for d in rows(OUT/'pattern_development.jsonl')[-3:]:
 for eid in d['evidence_event_ids']:
  if eid not in known:raise ValueError('없는 귀납 근거 '+eid)
validate()
write('batch_003_validation.json',json.loads((OUT/'validation_report.json').read_text()))
write('batch_003_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
