import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write,refresh,validate
assert not any(r['audit_id']=='QBF01-AUDIT009' for r in rows(OUT/'semantic_sample_audits.jsonl')),'감사 중복 금지'
assert not any(r['development_id']=='QBF01-DEV028' for r in rows(OUT/'pattern_development.jsonl')),'부분 완료 시 잔여 단계만 복구'
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV028','pattern_ids':['관계귀속','속성분리','지지방향','범위이동'],
 'evidence_event_ids':['QBF01-U0125-Q04-S02','QBF01-U0125-Q06-S02','QBF01-U0132-Q06-S02','QBF01-U0135-Q03-S01'],
 'finding':'UV는 결론이 현실에 맞아도 사용한 원리가 그 근거에 적용되지 않으면 틀리다.UX는 반박받는 논증을 정확히 바꿔 쓸 수 있으며 그 논증 승인과 다르다.XX는 유익한 독서 계획이라도 작곡 노력의 답이 아니고,YG는 결론을 지지하는 근거라도 지정 관점의 근거가 아닐 수 있다.',
 'decision':'명제의 사실성·의미 보존·추론 타당성·과제 적합성·관점 일치를 다른 평가 축으로 기록한다.모두 그럴듯함이라는 하나의 오류로 합치지 않고 기존 후보와 사례별 검사 좌표를 유지한다.',
 'next_counterexample':'같은 선지를 문맥 대치/최종 타당성 문항에서 각각 평가하거나,지정 관점을 삭제했을 때 복수 정답이 생기는지 대조한다.',
 'educational_use':'먼저 발문이 요구하는 판단 종류를 적게 한다.YG의 관점 조건 삭제는①도 후보가 되므로 유일 정답을 다시 설계해야 한다.'},
 {'development_id':'QBF01-DEV029','pattern_ids':['되먹임고리','BFP006','관계귀속','단계구분'],
 'evidence_event_ids':['QBF01-U0130-Q03-S01','QBF01-U0137-Q03-S01','QBF01-U0137-Q03-S02','QBF01-U0090-Q02-S02'],
 'finding':'XB는 소비가 생산·소득을 거쳐 추가 소비로, YM은 독서 행위의 성공 결과가 다시 독서 동기로 돌아온다.둘 다 출발 변수를 강화하는 실제 설명 경로다.정당화 근거가 서로 의존하는 BFP006과는 화살표의 의미가 다르다.',
 'decision':'XB·YM은 되먹임고리의 추가 KICE 구현으로 연결한다.숫자 계산이나 원형 도식 자체를 필수 조건으로 삼지 않는다.YM에서는 이전 결과와 다음 목적을 회차별로 구분한다.BFP006은 정당화 의존의 잠정 후보로 유지하며 자동 통합하지 않는다.',
 'next_counterexample':'마지막 결과가 출발 변수로 돌아오지 않는 직선 경로,출발 변수로 돌아오지만 약화하는 고리,단지 명제들이 서로를 근거로 삼는 순환을 비교한다.',
 'educational_use':'화살표마다 실제 변화·동기 재생·정당화 중 어느 관계인지 쓰게 한다.XB의 정확 승수나YM의 영구 습관 보장은 주어지지 않았음을 명시한다.'},
 {'development_id':'QBF01-DEV030','pattern_ids':['속성분리','관계귀속','조건부방향','분류기준'],
 'evidence_event_ids':['QBF01-U0132-Q02-S01','QBF01-U0133-Q01-S02','QBF01-U0134-Q01-S03','QBF01-U0131-Q02-S01'],
 'finding':'XT·XY는 같은 음악·책에도 청자·독자 조건이 달라 결과가 달라질 수 있다.YB는 서로 다른 두 요인이 같은 관측 결과에 영향을 주어도 요인 사이 관계는 따로 주어져야 한다.XG는 같은 검출 결과를 낸다는 사실이 물질의 결합 상태 동일성을 보장하지 않는다.',
 'decision':'같은 입력/다른 처리 조건,다른 입력/공통 결과,공통 결과/다른 구현을 사례별 구조로 분리한다.단순히 조건 차이가 있다는 이유로 방향 변화 패턴을 적용한 XT 연결은 AMD018로 제거되어 현행 속성분리만 남는다.새 후보의 과도한 분리는 보류한다.',
 'next_counterexample':'입력·조건이 모두 같다고 명시한 경우,두 요인 사이 독립된 직접 관계가 추가된 경우,동일 출력이 반드시 같은 기제를 뜻하도록 정의한 경우를 대조한다.',
 'educational_use':'무엇이 같고 무엇이 다른지 입력·조건·과정·결과의 칸에 배치한다.관계가 미제시라는 판단을 현실에서 항상 무관하다는 주장으로 바꾸지 않는다.'}
])
keys=['UT','UZ','XB','XD','XG','XS','XT','YB','YG','YM']
qs=[q for q in rows(OUT/'current_question_reviews.jsonl') if set(q['case_ids'])&set(keys)]
eids={s['event_id'] for q in qs for s in q['scenes']}
assert len(qs)==10 and len(eids)==21
append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT009','batch':9,'date':'2026-10-15','sample_case_ids':keys,'sample_questions':10,'sample_scenes':21,
 'method':'주 에이전트가 현행10문항21장면의50개 선지 문언·중간추론·적용 한계·교육 반전 예시와 관련 후보D/E를 직접 대조했다.XS는 기존3열5행 전사를 연결한 사본,YM은 기존BMP와 정본 지정 자산의 동일성을 선택 확인한 뒤 무손실PNG를 직접 열람했다.신규blind나 전체 보호자산 전수검증 아님.',
 'dimensions':{
 '중간추론':'UT의 동일→같은 특성에서 역을 추가하지 않음.XB는 소비의 재투입 연결과 같은 소득 증가 비교를 사용.XG는 결합→분해→형광·소광 분리→발색을 구분.YM은 완료 경험n과 다음 행위n+1의 기대를 분리.',
 '모든선지':'50개 선지를 각각 읽고 검토했다.XD⑤는 추가된 자사 제품 탄력성 증가 조건을 원래 광고 목적보다 우선 적용하며 절대 가격 상한으로 읽지 않음.XS는5행의 모든 칸을 대조.XB⑤는 관련 완결 문장과 뒤의 무관 파편을 구분.',
 '후보경계':'AMD018~020 현행 반영 확인.XT의 비단조 조건 차이에 조건부방향을 붙이지 않고,UT는 정의 반례 대신 단일 함축,UZ는 목표 달성 검사가 아닌 당위/물리 사건 구별로 좁힘.YB①의 길다·짧다 방향은 실제 명시되어 XT와 다름.',
 '원문과이력':'XS 선택표 미비hold 뒤 복원 후 최초답②를 유지.YM의 누락hold와 잘못된anchor 검토hold 뒤 복원 최초답①를 유지.verified보충파일의 정본hash 한 글자 누락은 실제파일hash와 별도 기록.추출BMP는정본BinData/image7.bmp와정확일치.기존파일무수정.',
 '교육출제':'YG 관점 조건 삭제는 일반 지지 근거①도 허용할 수 있어 단일정답 재설계 필요.UT 역함축,XT 좋은 음악 평가와 세부 감정 동일성,YM 이전 결과와 다음 목적을 각각 분리하도록 구성.'},
 'findings':[
 {'case':'UT/UZ/XT','issue':'넓게 붙인 후보 이름과 좁은D/E 불일치','resolution':'작성 직후AMD018~020으로 연결 축소·교체하고 이번 감사에서 현행 반영 확인'},
 {'case':'YM','issue':'기존 verified 보충파일의 canonical hash 문자열 누락','resolution':'해당 정본과 지정 이미지 한 자산만 선택 대조.원BMP 동일·PNG픽셀동일 확인.기존값과실제값을새폴더YM_visual_source_review.json에 병기'},
 {'case':'XB','issue':'⑤ 뒤 집합 의례 무관 문장 파편','resolution':'기존풀이와 일치하는 완결 선지만 판정.파편 원문·기존 노출 보존.정본 신규복원 성과로 기록하지 않음'},
 {'case':'YG','issue':'일반적으로 맞는 근거와 지정 관점의 근거 혼동 위험','resolution':'결론 지지와 관점 일치를 별도 검사.①자체를 거짓이라고 고치지 않음'}],
 'decision':'중대한 미해결 오류 없이361번부터 계속 진행 가능.명시된 적용 가정과 기존15문항 유보 유지.',
 'unresolved_blocking_error_count':0,'limitations':'표본밖 의미 무오류 보증이 아니다.기존 유보 해소나 새blind 성과로 집계하지 않는다.'}])
refresh();validate()
write('batch_009_validation.json',json.loads((OUT/'validation_report.json').read_text()))
cp=json.loads((OUT/'checkpoint.json').read_text());write('batch_009_checkpoint.json',cp)
h=json.loads((OUT/'session_handoff_20261013.json').read_text())
h.update(date=cp['date'],reviewed_questions=cp['reviewed_questions'],new_scenes=cp['new_scene_count'],by_exam=cp['by_exam'],batch_state='001~009 각40문항 저장·표본 감사 완료.9배치10문항21장면 감사.361번부터10배치 계속.',next_order=cp['next_order'],next_unique_question=cp['next_question'],next_case=cp['next_case_ids'][0],read_but_not_saved=[],last_saved_author='author_009h.py',next_author_suggestion='author_010a.py',resume_command='python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 361 5',validation='360문항548장면 현행증거·offset·hash·선지수·ID검증.보호자산 전수hash 반복검사 생략.')
h['important_corrections'] += ['9배치감사10문항21장면.기존15문항유보유지.DEV028~030추가.', 'YM정본hash기재누락은새폴더검증기록에실제값병기.원BMP정본자산동일·무손실PNG직접열람.원본불변.', 'XB⑤뒤무관파편분석제외범위명시.XD⑤는상대가격결정력제약.UT역함축추가금지.YG관점조건삭제시유일정답재설계.']
write('session_handoff_20261013.json',h)
