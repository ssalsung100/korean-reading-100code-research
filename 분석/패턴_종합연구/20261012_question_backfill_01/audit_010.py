import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write,refresh,validate
assert not any(r['audit_id']=='QBF01-AUDIT010' for r in rows(OUT/'semantic_sample_audits.jsonl'))
assert not any(r['development_id']=='QBF01-DEV032' for r in rows(OUT/'pattern_development.jsonl')),'부분 실행 시 잔여만 복구'
sc={r['event_id']:r for r in rows(OUT/'new_judgment_scenes.jsonl')}
fixes=[
 ('QBF01-AMD023','QBF01-U0143-Q02-S01','필요요건역전금지','ZH는 엄밀한 단일 함축이 아니라 기억을 도울 수 있다는 경로를 필수 회상 요건으로 강화한다.필요요건역전금지 D/E의 실제 필요한 조건·역함축과 동일하다고 확정하지 않고 강도보존만 남긴다.도움/필수화의 구체 추론과 원raw는 보존.'),
 ('QBF01-AMD024','QBF01-U0150-Q02-S01','필요요건역전금지','ACL의 목표 상태를 참여 전 자격으로 전도한 조작은 실제 필요조건을 먼저 도출하고 역을 검사하는 D와 다르다.목표/선행 자격의 위치를 배정하는 관계귀속만 남긴다.원raw·개별 설명 불변.'),
 ('QBF01-AMD025','QBF01-U0151-Q03-S01','수치표상','ACQ S01은 실제 그래프·축·배율을 판독하는 장면이 아니라 정의의 측정 대상·기준점·원인 역할을 구별한다.작도는 교육용 보조이며 원자료의 표상 판독이 아니다.수치표상 연결만 제거하고 관계귀속 유지.전체 폭 추론은 별도S03의 BFP009로 남긴다.')]
amds=rows(OUT/'scene_amendments.jsonl');assert not {x[0] for x in fixes}&{a['amendment_id'] for a in amds}
append('scene_amendments.jsonl',[dict(amendment_id=aid,event_id=eid,reason=reason,changes=[dict(field_path='pattern_connections',old_value=sc[eid]['pattern_connections'],new_value=[p for p in sc[eid]['pattern_connections'] if p['pattern_id']!=remove])]) for aid,eid,remove,reason in fixes])
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV032','pattern_ids':['분류기준','분기망라','강도보존','필요요건역전금지','관계귀속','수치표상'],
 'evidence_event_ids':['QBF01-U0139-Q02-S01','QBF01-U0143-Q02-S01','QBF01-U0145-Q02-S02','QBF01-U0150-Q02-S01','QBF01-U0151-Q03-S01'],
 'finding':'조건별로 다른 반응을 분류하는 YS는 같은 결론에 이르는 경우 분석이 아니다.ZH의 도움→필수화와 ACL의 목표→선행 자격 전도는 실제 단일 함축의 역 검토와 다르다.ZN의 단순 대소 비교와 ACQ 정의의 대상 구별은 실제 축·배율 판독이 아니다.',
 'decision':'AMD021~025로 현재 연결을 축소했다.기존95후보의 이름이 넓게 읽혀도 D/E의 적용 조건을 임의 확장하지 않는다.도움의 필수화는 강도보존,목표 위치 교환은 관계귀속으로 남기고 필요하면 후속 사례에서 세분화한다.',
 'next_counterexample':'원문에 엄밀한 P→Q가 주어진 사례와 단지 도움이 될 수 있는 사례를 비교한다.서로 다른 분기의 결론이 실제로 같아지는 경우와 다른 경우를 구별한다.',
 'educational_use':'후보 이름을 붙이기 전에 어떤 전제와 어떤 변환이 실제로 있는지 한 문장으로 적게 한다.형식화를 위한 추가 가정은 원문 근거와 분리한다.'},
 {'development_id':'QBF01-DEV033','pattern_ids':['속성분리','조건부방향','관계귀속'],
 'evidence_event_ids':['QBF01-U0140-Q04-S02','QBF01-U0141-Q04-S05','QBF01-U0146-Q03-S03','QBF01-U0151-Q02-S02'],
 'finding':'YY는 낮은 활성이라는 비슷한 결과가 흡착량 부족과 과도 안정화라는 다른 원인에서 생긴다.ZC는 최종량이 같아도 도달 시간이 다르다.ZS는 서로 다른 공개·참여 수단이 정보 독점 완화를 돕고 ACP는 홈·이진수의 다른 표현이 같은 소리에 대응한다.',
 'decision':'같은 결과/다른 원인,같은 도착값/다른 시간,다른 수단/공통 효과,다른 표현/공통 대상은 각 사례의 연결로 분리한다.하나의 광범한 동일성 오류 후보로 합치지 않는다.',
 'next_counterexample':'최종량이 같다는 정보 외에 도달 시간도 같다고 명시하거나,유일한 원인·표현 형식을 정의한 사례에서 구분의 적용 한계를 점검한다.',
 'educational_use':'무엇의 같음인지 목적어를 붙이고 원인·시간·수단·표현까지 같다는 추가 결론이 나오는지 검사한다.YY에는 흡착 강도 전체 범위의 단조 증가를 부여하지 않는다.'},
 {'development_id':'QBF01-DEV034','pattern_ids':['BFP009','필요요건역전금지'],
 'evidence_event_ids':['QBF01-U0151-Q03-S03'],
 'finding':'ACQ는 대역 내부의 차폐음 주파수에서 다른 주파수까지의 거리가 대역 전체 폭을 넘으면 대역 밖임을 판단한다.전체 폭은 내부 두 점 거리의 상한이며 대칭성·기준점 중점 가정은 필요 없다.',
 'decision':'BFP009를 단일 KICE 문항 근거의 잠정 후보로 신설.기준점의 구간 내 위치를 적용 조건에 명시하고 거리 이하→구간 안 또는 차폐라는 역추론은 금지한다.원95정의 불변.',
 'next_counterexample':'설명용 가상 반례: 구간[0,10],내부 기준점1,대상10.5이면 거리9.5<전체폭10이어도 밖이다.구간[10,20]에서 기준점0은 내부가 아니므로 대상15와의 거리15>폭10이어도 대상은 안이다.이 수치는 기출 관측값이나 새 blind 사례가 아니라 조건 필요성을 보이는 사후 구성이다.',
 'educational_use':'구간 양 끝과 내부 기준점을 표시하고 전체 폭을 내부 최대 거리로 사용하는 이유를 쓰게 한다.대역 밖 배제의 충분조건과 실제 차폐의 다른 필요조건을 구별한다.'},
 {'development_id':'QBF01-DEV035','pattern_ids':['관계귀속','설명해상도','분류기준','범위이동'],
 'evidence_event_ids':['QBF01-U0144-Q02-S01','QBF01-U0148-Q03-S01','QBF01-U0149-Q04-S01','QBF01-U0150-Q01-S01'],
 'finding':'ZK의 자료 평가는 출처의 믿음과 목적 적합성을 구별한다.AAE의 같은 검색·생성 수단도 검토 목적이 다르다.AAI의 본문에 있는 참된 이유는 현재 사례에 그 조건이 있어야 적용된다.ACK의 전문화 역할 언급은 전문화 제도·절차 설명의 답이 아니다.',
 'decision':'말이나 수단이 등장한다는 사실과 현재 물음에 필요한 대상·목적·조건·상세 수준이 맞는지를 별도 검사한다.자료에 있다고 모두 현재 답의 근거가 되는 것은 아니라는 공통 교육 원리를 도출하되 각 후보의 논리 조건은 유지한다.',
 'next_counterexample':'같은 검색 수단으로 서로 다른 목적을 명시한 사례,동일 결과에 이르는 두 이유 중 하나만 현재 사례가 충족하는 경우,구체 절차를 실제 추가한 설명을 대조한다.',
 'educational_use':'근거 문장 옆에 무엇을 누구에게 왜 설명하는지 적고 발문의 요구와 대응하게 한다.다른 단계의 절차 설명으로 현재의 정보 공백을 임의 보충하지 않는다.'}
])
keys=['YQ','YS','YY','ZC','ZD','ZH','ZN','ZS','AAH','AAJ','ACN','ACQ','ACS']
qs=[q for q in rows(OUT/'current_question_reviews.jsonl') if set(q['case_ids'])&set(keys)]
eids={s['event_id'] for q in qs for s in q['scenes']}
assert len(qs)==13 and len(eids)==29
append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT010','batch':10,'date':'2026-10-15','sample_case_ids':keys,'sample_questions':13,'sample_scenes':29,
 'method':'주 에이전트가 현행13문항29장면의65개 선지,추론·적용 조건·교육 변형을 선택 대조.작성 때 읽은 기존 풀이·개별 판정과 원문을 활용. YQ 공식 선택표·YY 원그래프는 기존PNG 직접 판독.신규 blind나 전수 원전 재검증 아님.',
 'dimensions':{
 '중간추론':'ZC는 보정 대응·전체 질량·표면 처리 목적·공통 농도 비율·반응 시간을5장면으로 분리.ACQ는 내부 기준점·전체 폭·외부 판정의 중간 추론과 역추론 금지를 명시.AAJ는 개시 합의부터 실제 재판 경로를 선택.',
 '모든선지':'65개 각각의 실제 검토를 확인.YQ의 오답 행에서도 적합한 다른 열을 전면 부정하지 않는다.YS⑤ 정의 기준 구별을 현실 무상관 증명으로 강화하지 않음.ZS①은 미행사 가능성이지 모든 손실 회피 보장이 아님.',
 '후보경계':'AMD021/022 작성 직후 수정 확인,감사에서AMD023~025 추가.실제 단일 함축과 도움/목표의 필수화를 분리.실제 도표 축 해석과 개념 정의의 측정 대상 구별을 분리.BFP009는 단일 사례 잠정 후보.',
 '원문과이력':'YQ 파생 선택표 사본에만 복원하며 원빈셀·과거hold 보존.YY 그래프 상대 순위만 사용.ZD/ZE 연도·정답 오연결 후속 대조 이력 활용,수치 격차 추정 금지 보존.AAH/AAJ 사전답 노출 뒤 재구성·strict blind 제외 유지.',
 '교육출제':'YQ 단어 교체 후 두 정답이 생길 수 있어 유일 정답 재설계 필요.ACQ 가상 구간 반례는 기출값과 분리.ZC 같은 질량만으로 공통 농도를 가정하지 않고 보기의 공간·불변 조건을 사용.ACS 닮음/다름의 역할과 직접 표출/해석 가능을 구별.'},
 'findings':[
 {'case':'YS/ZN/ZH/ACL/ACQ','issue':'후보 이름의 넓은 해석과 기존D/E 차이','resolution':'AMD021~025 현행 연결 보정.추론·최초 기록·정답 불변.'},
 {'case':'ACN','issue':'기존 최초 분별/깨달음 근접 의미 유보가 정답 후에도 남음','resolution':'공식③ 유지하면서 사후 유보 항목으로 명시.범용 경계 확정만 유보하며 후속 진행 차단 아님.'},
 {'case':'ACL','issue':'author010g의 근거 인용에서 원문 조사 의 누락으로 검증 중단','resolution':'391~394 raw 저장 여부를 확인하고 ACL만 author010g_remaining으로 복구.원010g 전체 재실행 금지.중복 저장 없음.'},
 {'case':'AAJ','issue':'권리 행사·예외·절차를 한 덩어리로 적용할 위험','resolution':'갱신 사유와 증명,상한 초과와 기간 미정,조정 합의와 기능을3장면으로 나눔.'}],
 'decision':'중대한 미해결 오류 없이401번부터 계속.기존15문항 유보 유지 및 ACN의 기존 근접 의미 한계를 명시하여 현행16문항 유보.새 유보는 다음 연구를 차단하지 않는다.',
 'unresolved_blocking_error_count':0,'limitations':'표본외 의미 무오류 보장이 아니다.보호자산 전체hash·모델 비교 실험을 수행하지 않았다.'}])
refresh();validate()
write('batch_010_validation.json',json.loads((OUT/'validation_report.json').read_text()))
c=json.loads((OUT/'checkpoint.json').read_text());write('batch_010_checkpoint.json',c)
h=json.loads((OUT/'session_handoff_20261013.json').read_text())
h.update(reviewed_questions=c['reviewed_questions'],new_scenes=c['new_scene_count'],by_exam=c['by_exam'],batch_state='001~010 각40문항 저장·표본 감사 완료.10배치13문항29장면 감사.401번부터11배치 계속.',next_order=c['next_order'],next_unique_question=c['next_question'],next_case=c['next_case_ids'][0],read_but_not_saved=[],last_saved_author='author_010h.py',next_author_suggestion='author_011a.py',resume_command='python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 401 5',validation='400문항620장면의현행증거·offset·hash·선지수·ID검증.보호자산전수hash반복검사생략.')
h['important_corrections']+=['10배치감사13문항29장면65선지.AMD023~025로ZH/ACL필요요건역전금지·ACQ S01수치표상 연결 제거.DEV032~035저장.', 'BFP009는ACQ의구간내기준점에서전체폭초과거리로밖을판정하는단일사례잠정후보.대칭·중점가정불필요.가상반례와기출근거분리.', 'ACN의최초근접어휘불확실성을유보로명시.현행16문항유보.공식답③변경없음.', 'author010g는391~394저장후ACL인용누락으로중단.미저장ACL만author010g_remaining으로완료.전체재실행금지.']
write('session_handoff_20261013.json',h)
