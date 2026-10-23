import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write,refresh,validate
assert not any(r['audit_id']=='QBF01-AUDIT007' for r in rows(OUT/'semantic_sample_audits.jsonl')),'감사 중복 실행 금지'
assert not any(r['development_id']=='QBF01-DEV020' for r in rows(OUT/'pattern_development.jsonl')),'부분 저장 뒤 잔여 단계만 복구할 것'
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV020','pattern_ids':['BFP007','BFP008','수치표상','하한정확값'],
 'evidence_event_ids':['QBF01-U0106-Q02-S02','QBF01-U0109-Q02-S01','QBF01-U0113-Q04-S01'],
 'finding':'PR은 한 분포 안의 최소 평균 비트 수를 고정한 뒤 여러 분포의 최소값끼리 최대를 비교한다. QR은 자리마다 허용한 두 값을 결합해2^n을 얻는다. SC는 수밀도→압력의 비례와 압력→진공도의 방향을 옮긴다.',
 'decision':'모두 수치를 다루지만 실제 연산은 극값 범위 중첩·조합 생성·정의된 비례 변환으로 다르다. BFP007·008은 각각 한 문항의 잠정 분리로 보존하며 확정 후보로 승격하지 않는다. BFP008의 선형 곱셈 금지는 n자리×자리당2값=2n이라는 오산을 뜻하며 자리별선택수의곱2×2×… 자체를 금지하는 뜻이 아니다.',
 'next_counterexample':'내부 최솟값과 외부 최대 비교가 없는 단순 범위 문제,자리 사이 제약으로 모든 조합이 허용되지 않는 문제,수밀도 대신 전체 분자 수만 주고 부피가 다른 문제를 대조한다.',
 'educational_use':'무엇을 고정하는지,무엇을 세는지,어떤 관계식을 적용하는지를 각 단계에 적게 한다. QR의 평탄화 수식은 새 지수 판독 성과로 표현하지 않는다.'},
 {'development_id':'QBF01-DEV021','pattern_ids':['부분전체','BFP005','관계귀속','실행조건','직전상태갱신','범위이동'],
 'evidence_event_ids':['QBF01-U0112-Q02-S03','QBF01-U0070-Q02-S03','QBF01-U0111-Q03-S02','QBF01-U0111-Q03-S03'],
 'finding':'RW에서 남는 표준선은 정상 진행이라는 다른 정보를 표시한다. KG에서 남는 시간 단서는 기존 방향 판별에 계속 기여한다. 둘 다 일부가 남지만 동일 판단의 대체 단서인지 다른 기능의 구성 부분인지 다르다. RS는 불능 급부에 일반 집행 절차를 적용할 수 없으며 반환 대상은 실제 지급 대금이다.',
 'decision':'RW를 부분전체에 두고 BFP005의 동일 목표에 대한 잔여 단서로 자동 통합하지 않는다. RS의 실행조건 연결은 다른 규정과의 충돌 검사라는 D에 미달하여 AMD015로 범위이동으로 바꾸었고,반복 입력 갱신이 없는 S03의 직전상태갱신은 AMD016으로 제거했다. 원95정의는 불변.',
 'next_counterexample':'남은 신호가 동일 판단을 대신하는 경우와 다른 기능만 표시하는 경우,필수행위가 별도 규정에 금지된 경우와 물리적으로 불가능한 경우,실제 순차 상태갱신과 단일 급부 귀속을 대조한다.',
 'educational_use':'남아 있는 요소의 수만 세지 말고 그 요소가 무엇을 알려 주는지 적는다. 후보 이름이 비슷하다는 이유만으로 연결하지 않는다.'},
 {'development_id':'QBF01-DEV022','pattern_ids':['대립가능성','강도보존','근거망복원','부분전체'],
 'evidence_event_ids':['QBF01-U0110-Q04-S01','QBF01-U0110-Q04-S02','QBF01-U0114-Q05-S03'],
 'finding':'QZ의 두 존재명제가 정확한 부정쌍이 아니라는 사실은 완결성의 직접 대입 문제를 지적하지만 적어도 하나 참이라는 약한 결론을 항상 거짓으로 만들지는 않는다. SH의 공식M기호 복원은 질량 표기 불일치를 해결하지만 구슬의 질량분포 적용 조건까지 명시해 주지는 않는다.',
 'decision':'공식답의 직접 근거,다른 선지의 배제 강도,원문 복원,모형 가정을 각각 구별한다. QZ의 기존 정답 후 상세 유보를 유지하고 SH⑤의 구슬 균질/구대칭 적용 조건은 사후 구체화한 유보로 저장한다. 문항 오류·복수정답 확정으로 승격하지 않는다.',
 'next_counterexample':'정확히하나/적어도하나를 명시한 양화문,빈 대상 집합 허용을 명시한 보기,균질구슬과 비대칭질량분포 구슬을 비교한다.',
 'educational_use':'새 문항에서는 양화 강도와 대상 존재 전제 및 등가모형의 분포 조건을 명시한다. 정답 일치와 모든 근거의 확정은 별개로 기록한다.'},
 {'development_id':'QBF01-DEV023','pattern_ids':['관계귀속','단계구분','요건순서'],
 'evidence_event_ids':['QBF01-U0107-Q03-S02','QBF01-U0107-Q03-S03','QBF01-U0111-Q02-S01','QBF01-U0114-Q05-S01'],
 'finding':'QJ는 순차 재사용과 동시 중복,자기 주소와 공통 참조 주소를 나눈다. RR은 같은 당사자여도 인도 의무와 반환 청구권의 대상·발생 원인이 다르다. SH는 같은 위치의 질점m을 쓰더라도 상대 천체를 바꾸면 같은 상호작용 쌍이 아님을 보인다.',
 'decision':'관계귀속을 도메인별 명칭으로 성급히 분리하지 않고,실제 판독할 좌표를 주체·상대방·대상·시점·발생 원인으로 사례별 명시한다. QJ의 과거10/12/22 유일주 유보를 이번 후보 연결로 해소했다고 하지 않는다.',
 'next_counterexample':'당사자는 그대로이고 방향만 역전한 관계,당사자 중 하나를 바꾼 관계,값은 같지만 참조 대상이나 시간 구간이 다른 관계를 대조한다.',
 'educational_use':'같다는 말을 평가할 때 무엇의 동일성인지 먼저 쓰게 하며 관계 그림의 끝점과 시간 구간을 보존한다.'}
])
keys=['PR','QJ','QQ','QR','QZ','RS','RW','SC','SD','SH']
qs=[q for q in rows(OUT/'current_question_reviews.jsonl') if set(q['case_ids']) & set(keys)]
eids={s['event_id'] for q in qs for s in q['scenes']}
ss=[s for s in rows(OUT/'new_judgment_scenes.jsonl') if s['event_id'] in eids]
append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT007','batch':7,'date':'2026-10-15','sample_case_ids':keys,'sample_questions':len(qs),'sample_scenes':len(ss),
 'method':'주 에이전트가 현행10문항26장면의 중간추론·선지 전체·후보D/E를 현재 작성에서 직접 읽은 원문 및 기존 풀이에 대조했다. SD는 기존 원표 5행 전사,SH는 기존 공식 문제지 crop을 직접 열람하고⑤M 및R+h를 확인했다. 신규blind·원배포정답표·전체코퍼스 재검증은 수행하지 않음.',
 'dimensions':{
 '중간추론':'PR에서고정분포내최소와분포간최대범위를구별. QR은2자리4경우를각각두갈래로확장하여8·16산출. SC는D/E압력·부착확률통제를확인한정성방향만사용. SH는mMe/d²와mMs/d²의서로다른상대질량및껍질환원후공통중심거리를검사.',
 '모든선지':'표본의50개선지검토와장면연결을확인. QQ의맞는결론/추가질량원인, QJ자기주소/공동참조주소, RW복합체성분/표지/두선기능을구분.',
 '후보경계':'RS의과잉연결을AMD015/016으로좁혔으며현행장면에반영확인. BFP007·008은각단일문항잠정후보. SH의공간기준은표면높이→중심거리라는명시기준변환범위로한정.',
 '원문과이력':'SD원표다섯행을정렬한사본과SH공식M사본만수정.기존번호hold·canonical기호hold·공식crop복원후유효최초답의순서를보존. QZ기존independent_code1948의유보사본을연결.',
 '교육출제':'PU의불명확한반전예시는이미AMD014로모든동음이의어선택이라는구체복수선택형수정. RW②수정예시에서는남은과달리까지함께제거해야함을명시. QZ양화강도및SH질량분포가정은새출제에서명시해야함.'},
 'findings':[
 {'case':'RS','issue':'실행조건·직전상태갱신의좁은D를넘은후보연결','resolution':'작성직후AMD015/016으로범위이동/관계귀속으로조정한현행값확인'},
 {'case':'QZ','issue':'③의정확히하나/적어도하나및학생존재전제','resolution':'기존유보유지·④직접근거와분리·문항오류확정아님'},
 {'case':'SH','issue':'공식M와canonicalm불일치및구슬분포조건','resolution':'전자는기존공식crop에근거한사본으로해소.후자는사후구체화한모형조건유보로유지'},
 {'case':'SD','issue':'첫행stem혼입·나머지행이동·빈⑤','resolution':'기존보충파일의정확한5행을사본에연결하고유효최초답이복원후임을보존'}],
 'decision':'명시유보를확정규칙으로사용하지않는조건에서281번부터계속진행가능','unresolved_blocking_error_count':0,
 'limitations':'표본밖의의미무오류보증이아니다.기존15문항유보는해소된것으로집계하지않는다.'}])
refresh();validate()
write('batch_007_validation.json',json.loads((OUT/'validation_report.json').read_text()))
cp=json.loads((OUT/'checkpoint.json').read_text());write('batch_007_checkpoint.json',cp)
h=json.loads((OUT/'session_handoff_20261013.json').read_text())
h.update(date=cp['date'],reviewed_questions=cp['reviewed_questions'],new_scenes=cp['new_scene_count'],by_exam=cp['by_exam'],batch_state='001~007 각40문항 저장·표본 감사 완료. 7배치10문항26장면 감사. 281번부터8배치 계속.',next_order=cp['next_order'],next_unique_question=cp['next_question'],next_case=cp['next_case_ids'][0],read_but_not_saved=[],last_saved_author='author_007i.py',next_author_suggestion='author_008a.py',resume_command='python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 281 5',validation='280문항402장면의현행증거·offset·hash·선지수·ID검증통과.보호자산전수hash반복검사생략.')
h['important_corrections'] += ['BFP007은분포내최소/분포간최대, BFP008은자리별선택결합의잠정후보.각단일문항근거이며확정아님.', 'RS후보연결을AMD015/016으로축소. QZ③의기존문언유보와SH⑤의사후모형조건유보를보존.', 'SD선택지행과SH⑤공식M는새폴더파생사본에연결. source_overrides.json사용. 원본불변.']
write('session_handoff_20261013.json',h)
