import sys,json,math
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write
from resume_support_20261015 import finish
assert not any(a['audit_id']=='QBF01-AUDIT014' for a in rows(OUT/'semantic_sample_audits.jsonl'))
assert not any(a['amendment_id']=='QBF01-AMD038' for a in rows(OUT/'scene_amendments.jsonl')),'부분 실행 시 잔여만 복구'
ss={s['event_id']:s for s in rows(OUT/'new_judgment_scenes.jsonl')}
qs=rows(OUT/'current_question_reviews.jsonl')
def link(pid,fit):return {'pattern_id':pid,'case_specific_fit':fit,'definition_source':'분석/패턴_종합연구/20261012_corpus_sweep_01/pattern_candidates.json','definition_reused':True}
fixes=[
 ('QBF01-AMD038','QBF01-U0218-Q01-S01','정보경로복원',link('관계귀속','공시 원천·가격 매개·투자자의 직접 입력을 다른 역할로 구별한다.'),'ANM은 공시의 가격 반영과 투자 판단의 매개 모형이다. 기존 정보경로복원 D/E의 동일 행위자 수신·방문 확인·후속 발신 내용 반영과 동일한 행동으로 확정하지 않는다. 가격 매개 설명 자체는 보존하고 관계귀속으로 제한.'),
 ('QBF01-AMD039','QBF01-U0298-Q01-S01','정보경로복원',None,'AWQ의 프레온 배출·수송·축적은 물질 이동이다. 인간의 정보 수신·확인·후속 발신이라는 기존 D/E에 해당하지 않아 연결을 제거한다. 물질 경로와 생성/파괴의 실제 설명은 관계귀속 및 사례 내용에 보존.'),
 ('QBF01-AMD040','QBF01-U0299-Q03-S01','조건수렴',link('분류기준','최적통화지역의 충격 대칭성·대체 조정 가능성 조건을 각 국가쌍에 적용한다.'),'AWV는 서로 다른 국가쌍에 조건을 적용하는 분류이다. 동일 시작 상태에 서로 다른 규칙을 적용해 경로가 수렴하는 기존 조건수렴 D/E와 다르므로 후보 연결을 변경. 보완 조건과 실제 채택/최적성 구별은 유지.'),
 ('QBF01-AMD041','QBF01-U0297-Q03-S02','설명해상도',link('범위이동','고통이라는 결과 하나의 확인을 논리적 정당화·모순까지 포함한 해석 전체의 확인으로 확대하지 않는다.'),'AWPⓒ의 문제는 단순 설명 대 세부 메커니즘의 해상도 차이라기보다 복합 해석의 일부만 확인됨이다. 기존 설명해상도 D/E를 모든 근거 부족에 확대하지 않고 범위이동으로 한정한다.')]
am=[]
for aid,eid,pid,replacement,reason in fixes:
 old=ss[eid]['pattern_connections'];new=[p for p in old if p['pattern_id']!=pid]
 assert len(new)==len(old)-1
 if replacement:new.append(replacement)
 am.append({'amendment_id':aid,'event_id':eid,'reason':reason,'changes':[{'field_path':'pattern_connections','old_value':old,'new_value':new}]})
append('scene_amendments.jsonl',am)
counter=[]
for b in [1,0.25]:
 t=3/math.sqrt(b)-1;x=b*t;y=9/(1+t)
 assert 0<t<6
 assert abs(b-9/(1+t)**2)<1e-12
 counter.append({'b':b,'t_opt':t,'x_opt':x,'y_opt':y,'total':x+y,'F_prime':b-9/(1+t)**2,'F_second':18/(1+t)**3})
assert counter[1]['t_opt']>counter[0]['t_opt'] and counter[1]['x_opt']<counter[0]['x_opt']
write('AWI_countermodel_verification.json',{'status':'가상 수학 반례·기출 관측값 아님','domain':'0≤t≤6, b>0','definitions':{'D':'x=b*t','U':'y=9/(1+t)','curve':'y=9*b/(b+x)','total_derivative':'F_t=b-9/(1+t)^2','total_second_derivative':'18/(1+t)^3>0','curve_second_derivative':'18*b/(b+x)^3>0'},'cases':counter,'conclusion':'같은 개입t에서 독재 비용을 낮추는b감소는 최적t증가와 실제x감소를 동시에 낳을 수 있다. 개입 순서와 비용좌표는 다른 함수 사이에서 동일시할 수 없다.','scope':'공식③ 변경 없음. 선지의 왼쪽을 개입이 적은 제도의 순서로 읽는 기존 해석과 실제 가로좌표를 읽는 해석의 차이를 드러낸다.'})
assert not any(d['development_id']=='QBF01-DEV048' for d in rows(OUT/'pattern_development.jsonl'))
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV048','pattern_ids':['BFP013','규칙우선순위','채택근거','논거결론위계','분류기준'],'evidence_event_ids':['QBF01-U0220-Q01-S01','QBF01-U0220-Q02-S01'],
 'finding':'ANS는 같은 행동 내용이어도 실제 채택한 이유가 다를 수 있음을 묻고, ANT는 개별 행위 이유를 비교하는 저울의 사용을 상위 근거가 차단하는지 묻는다. 강한 의무·외부 명령·이유의 언급 자체는 그 차이를 결정하지 않는다.',
 'decision':'BFP013을 ANT 단일 실제 문항의 잠정 후보로 유지한다. ANS를 추가 독립 검증으로 계수하지 않는다. 규칙우선순위는 명시된 우선·보충 규정을 선택하고, 채택근거는 사용한 근거의 귀속을 확인하며, 논거결론위계는 지지 관계의 층위를 구별하므로 ANT의 사용 배제와 우선 완전 통합하지 않는다.',
 'next_counterexample':'교육용 가상 대비: 약속의 이익이 손해보다 크면 지킨다는 판단은 이유 비교이며, 아무리 손해여도 약속을 지킨다는 제시 규칙은 손해가 결정을 바꾸지 못하게 한다. 매우 큰 가중치와 이유 배제를 구별할 조건 변경 사례가 필요하다.',
 'educational_use':'같은 최종 행동을 주되 실제 판단 규칙을 바꿔 분류하게 한다. 비교할 이유와 비교 사용을 허용·차단하는 상위 조건을 별도 층으로 제시한다.'},
 {'development_id':'QBF01-DEV049','pattern_ids':['수치표상','비교변인','기준내부검사','범위이동'],'evidence_event_ids':['QBF01-U0295-Q02-S01','QBF01-U0295-Q02-S02','QBF01-U0295-Q02-S03','QBF01-U0295-Q03-S01'],
 'finding':'AWI의 축은 독재 비용이고 제도 순서는 개입 정도이다. 한 곡선 안의 단조 순서를 언론 감시로 비용 함수가 바뀌는 사회 간 실제좌표 비교로 자동 확대할 수 없다. AWJ에서도 곡선의 악화와 그 위에서 새 제도를 고르는 개선은 서로 다르다.',
 'decision':'AWI 새 좌표 유보를 유지한다. 가상 반례의 최적점은 엄격볼록 모형 안에서 검산했으며 공식답③ 변경 근거로 사용하지 않는다. 제도 순서의 의도된 읽기와 비용 좌표의 엄밀 읽기를 구별한다. 같은 사회 내부 최적과 사회 간 절대 비용, 약볼록성과 유일 최소의 차이도 보존한다.',
 'verification_file':'AWI_countermodel_verification.json',
 'next_counterexample':'D_b(t)=bt,U(t)=9/(1+t),0≤t≤6에서b=1이면t*=2,x*=2이고b=1/4이면t*=5,x*=1.25이다. 비용 감소가 더 많은 개입과 더 작은x를 동시에 허용한다. 실제 정책 수치나 기출 실험 결과가 아니다.',
 'educational_use':'개입량과 비용을 다른 기호로 정의하고 곡선 내부 이동/함수 변화/곡선 전체 위치 이동을 구별한다. 실제 좌표 방향을 유일하게 묻는다면 비용함수 조건을 추가하며①처럼 엄격 우열이 필요하면 유일 최소도 확보한다.'},
 {'development_id':'QBF01-DEV050','pattern_ids':['관측합성','강도보존','지지방향','설명보완','조건부방향'],'evidence_event_ids':['QBF01-U0218-Q02-S01','QBF01-U0226-Q02-S02','QBF01-U0294-Q01-S02','QBF01-U0294-Q02-S01','QBF01-U0296-Q02-S01','QBF01-U0296-Q03-S01','QBF01-U0296-Q03-S02'],
 'finding':'ANN의 비약화는 충분 입증이 아니고 AOL의 상대적 영향은 배타적 원인이 아니다. AWE/AWF의 식별 한계는 모든 방향 추론 금지가 아니며 AWL/AWM의 잡음 감소·신호대잡음비·역수 민감도는 다른 지표이다.',
 'decision':'관측이 지지하는 범위와 필요한 추가 조건을 사례별로 남긴다. AWM 질량·출력은 적절한 조율이 가능한 조합으로 읽으며 아무 증가량이나 성능 개선을 보장하지 않는다. 투과율 증가를 다른 조절로 상쇄할 수 있음과 그 항목이 개선에 기여함은 별개이다.',
 'next_counterexample':'출력 증가에 비해 질량 증가가 부족하면 저진동수 개선이 보장되지 않는다. 모든 코호트가 같은 크기로 변한다는 추가 명제는 AWF의 기간 효과 가능성보다 강하다. 평균 차이만으로 AOL의 단독 인과·통계적 유의성이 나오지 않는다.',
 'educational_use':'관측값/지표 정의/예상 방향/증거가 허용하는 강도/조율 조건을 분리한다. 실험형·그래프형·이론 비교형의 표면 차이보다 실제 필요한 중간 추론을 대응하되 동일 패턴으로 무리하게 합치지 않는다.'},
 {'development_id':'QBF01-DEV051','pattern_ids':['정보경로복원','조건수렴','설명해상도','관계귀속','분류기준','범위이동'],'evidence_event_ids':['QBF01-U0218-Q01-S01','QBF01-U0297-Q03-S02','QBF01-U0298-Q01-S01','QBF01-U0298-Q02-S01','QBF01-U0299-Q03-S01'],
 'finding':'경로라는 이름만으로 정보의 수신·확인·후속 발신, 가격을 통한 정보 영향, 물질의 수송·축적을 동일 후보로 계수하면 기존 정의가 흐려진다. 조건표를 쓴다는 사실만으로 모든 분류가 조건수렴인 것도 아니고 근거 부족이 모두 설명해상도인 것도 아니다.',
 'decision':'AMD038~041로4개 연결을 축소·교체한다. ANM 가격매개·AWQ 물질수송·AWV 조건분기·AWP 복합해석 검증의 실제 판단은 보존한다. 기존95정의 수정 없음. AWR의 지연은 실제 축과 변화 시작 형태를 읽는 것이므로 수치표상 연결은 유지하되 기울기·정확 변화율 계산으로 확대하지 않는다.',
 'next_counterexample':'후속 실제 사례에 같은 행위자가 정보를 듣고 확인해 후속 전언에 반영하는 내용 제약이 등장하면 정보경로복원 연결을 재검토한다. 단순 물질 이동에는 적용하지 않는다. 동일 입력에 여러 규칙을 적용해 같은 경로인지 묻는 경우라야 조건수렴을 검토한다.',
 'educational_use':'공통 이름보다 입력·판단 연산·출력·실패 조건을 먼저 비교한다. 정의에 맞지 않은 구체 기출 설명도 삭제하지 않고 사례별 교육·제작 자료로 남긴다.'}
])
cases=['ANT','ANM','AOA','AOL','AWE','AWF','AWI','AWJ','AWL','AWM','AWP','AWQ','AWR','AWV']
sample=[q for q in qs if set(q['case_ids'])&set(cases)]
assert len(sample)==14 and sum(len(q['scenes']) for q in sample)==25
append('semantic_sample_audits.jsonl',[{'audit_id':'QBF01-AUDIT014','batch':14,'date':'2026-10-15','sample_case_ids':cases,'sample_questions':14,'sample_scenes':25,'sample_options':70,
 'method':'주 에이전트가 현행14문항25장면70선지와 이번 및 직전 작성에서 직접 읽은 원문·기존 풀이·선택 독립 판정을 대조. 후보 D/E/기존 사례와 BFP013을 직접 비교. 신규 공식 도식 직접 판독 기록을 활용. KICE 재분석 없음.',
 'dimensions':{'중간추론':'AWI 비용축/개입량 반례 검산, AWF 고정 변수·관측 방향, AWM 역수축·복합 개입 조율, AWR 시간 척도·지연, AWV 충격과 조정 수단 분기를 확인.','모든선지':'70선택행 실제 확인. AWL/AWM/AWF/AWV는 보기 각 조건·항목도 검토. AWP 기존MD보기5개 내용을 직접 읽고 연결.','후보경계':'BFP013 단일 문항 잠정 유지. AMD038~041로 정보경로복원·조건수렴·설명해상도 과잉 연결 보정.','원문과이력':'AWE 기존 BASIC 별도판정 연결과 고유문항1회 집계. 원전 이미지 직접 판독과 기존MD전사 활용을 구별. AOA 최초 존재 명시성 유보·AWI 새 좌표 유보 보존.','교육출제':'가상 반례는 실측값과 분리. AWM 임의 증가량 보장 금지·AWV 비용0의 단순화 모형 범위·AWR 미표시 시작 연도 추정 금지 확인.'},
 'findings':[{'case':'ANM/AWQ/AWV/AWP','issue':'기존 정의보다 넓은 연결4건','resolution':'AMD038~041. 구체 풀이·공식답·원raw 불변.'},{'case':'AWI','issue':'비용 가로축과 제도 개입 순서 혼동 가능성','resolution':'가상 엄격볼록 반례를 검산·별도 저장. 공식③ 보존·좌표 일반화 유보.'},{'case':'ANT','issue':'상위 근거 후보와 기존 우선규칙·채택근거의 경계','resolution':'BFP013을 ANT 단일사례 잠정 후보로 유지.'},{'case':'AOA','issue':'② 존재 진술의 최초 명시성 한계','resolution':'현행 유보 유지. 공식④ 변경 없음.'}],
 'decision':'14배치 저장·표본 감사·귀납 완료. 진행 차단 오류 없음.561번부터15배치 계속.25문항 유보 유지.','unresolved_blocking_error_count':0,'limitations':'표본 외 의미 무오류나 공식 답표 독립 전수 대조를 보장하지 않음. 보호 원장 전수 해시·모델 비교·Git push 없음.'}])
finish('audit_014.py',cases,['14배치 감사14문항25장면70선지·DEV048~051 완료. AMD038~041 연결4건 보정. BFP013 단일 사례 잠정 유지. AWI 비용함수 반례 검산·공식③ 유지. 총25문항 유보.561부터15배치 계속.'])
c=json.loads((OUT/'checkpoint.json').read_text());c.update(last_saved_author='author_014n.py',last_saved_audit='audit_014.py',next_sample_audit_at=600);write('checkpoint.json',c);write('batch_014_checkpoint.json',c)
write('batch_014_validation.json',json.loads((OUT/'audit_014_validation.json').read_text()))
h=json.loads((OUT/'session_handoff_20261013.json').read_text());h.update(last_saved_author='author_014n.py',last_saved_audit='audit_014.py',next_author_suggestion='author_015a.py',batch_state='001~014 저장·표본 감사 완료.560문항899장면.561부터15배치 계속.');write('session_handoff_20261013.json',h)
