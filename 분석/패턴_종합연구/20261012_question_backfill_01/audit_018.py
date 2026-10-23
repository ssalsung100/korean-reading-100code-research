import sys,json
sys.dont_write_bytecode=True
from fractions import Fraction
from backfill_io import OUT,rows,append,write
from resume_support_live import finish
assert not any(r['audit_id']=='QBF01-AUDIT018' for r in rows(OUT/'semantic_sample_audits.jsonl'))
qs=rows(OUT/'current_question_reviews.jsonl')
batch=[r for r in qs if r['batch_number']==18]
assert len(batch)==40
cases=['BIA','BID','BII','BIK','BIN','BIQ','BIU','BIX','BJE','BJF','BJL','BJN','BJR','BJU','BJX','BJY','BJZ','BKB']
sample=[r for r in batch if set(r['case_ids'])&set(cases)]
assert len(sample)==len(cases)
sample_scenes=sum(len(r['scenes']) for r in sample)
batch_scenes=sum(len(r['scenes']) for r in batch)
sample_options=sum(len(r['option_checks']) for r in sample)
# 직접 판독한 그림의 간선에서 설명용 경로만 검산. 원문 추출이나 의미 판정 자동화가 아님.
edges=[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4)]
paths=[]
def walk(p):
 if p[-1]==4: paths.append(p);return
 for a,b in edges:
  if a==p[-1]:walk(p+[b])
walk([0])
assert paths==[[0,1,2,3,4],[0,1,3,4],[0,2,3,4]]
assert all(set(p)==set(range(5)) for p in paths if len(p)==5)
counter=[0,1,2,1,4]
assert len(counter)==5 and counter[0]==0 and counter[-1]==4 and 3 not in counter
write('audit_018_selected_checks.json',{
 'scope':'18배치 표본의 명제·수치 및 시각자료 점검. 가상 수치는 실제 관측값이 아님.',
 'BID':{'ratio_before':str(Fraction(10,2)),'ratio_after':str(Fraction(4,1)),'denominator_decreased':True,'ratio_increase_guaranteed':False,'zero_denominator':'유한 비율 미정의','hold':'공식⑤ 유지,④의 비유도와 반대 방향 필연성 구별'},
 'BII':{'before':100*0.8,'after':150*0.6,'same_after_value_without_cut':150*0.8,'scope':'동일 담보에서 정책 효과 감소와 전후 한도 증가 양립. 실제 차입량과도 구별.'},
 'BIK':{'visual':'G438_visual01/02 직접 재확인','A':'대칭의 깊고 얕은 골,ⓐ는 얕은 골이므로 밝은 별이 앞','B':'빠른 상승·느린 하강,ⓒ주기는 고유 밝기 추정 입력','normalization':'100%가 절대 측광값이 아니지만 주기가 겉보기 밝기 측정의 필수조건이 되는 것은 아님'},
 'BIU':{'visual':'G442_visual01 직접 재확인','finding':'소낭의 원줄기세포·이동 후손·분화한 상피세포의 유형을 구별. 분화의 정확한 공간 경계는 주어지지 않음.'},
 'BJE':{'visual':'G445_visual02 직접 재확인','edges':edges,'all_paths_0_to_4':paths,'only_length5':[p for p in paths if len(p)==5],'countermodel_walk':counter,'scope':'현재 비순환 구조가 중복 검사를 만듦. 다른 순환 그래프 반모형이며 원그림의 경로로 오인하지 않음. 1·2검사가 각각 최소 필수라고 주장하지 않음.'},
 'BJY':{'equal_child_statutory_share':str(Fraction(1,2)),'equal_reserved_amount_ratio_to_estate':str(Fraction(1,2)*Fraction(1,2)),'alternative':'정확한 비율을 계산하지 않아도 같은 법정분에 같은 비율을 적용하여 동일성 판단 가능'},
 'holds':['BIA 수정허용이 모든 거래 증가 가능성을 배제하지 않음','BID 분자 변화 조건과0분모','BIN 자손 제재와 본인 유죄·형벌의 별도 범위'],
 'current_record_amendments':[],'pass':True})
devs=[
 {'development_id':'QBF01-DEV065','pattern_ids':['BFP015','전제포함','복수문턱'],'evidence_event_ids':['QBF01-U0406-Q03-S01'],
 'finding':'BJE는 오류 없음만으로3검사를 생략한 것이 아니다. 그림의 번호 증가 간선→재방문 불가→길이5는 서로 다른5정점→전체 포함의 중간 증명이 필요하다. 현재0→4경로는01234,0134,0234이고 길이5는 첫 경로뿐이다.',
 'decision':'author_018h에서 등록한 BFP015를 단일 기출 후보로 유지한다. 전제의 단순 재표현과 구별하여 구조 제약이 서로 다른 검사 조건 사이 함의를 만드는 연산을 기록한다. 기존95후보 정의는 수정하지 않으며 기존 META132와 이번 보완은 같은 BJE의 재검토라 독립 반복으로 세지 않는다.',
 'next_counterexample':'비순환성을 제거한0→1→2→1→4는 시작·끝·길이를 만족하지만3을 누락한다. 순환 존재만으로 언제나 실패가 생긴다는 역일반화도 금지한다. 다른 기출에서 구조 제약 아래 검사의 함축이 재현되는지 찾는다.',
 'educational_use':'앞 검사를 통과하고 뒤 검사에 실패하는 후보를 구성하게 한다. 새 문항은 방문 횟수와 서로 다른 정점 수를 구별해 쓰고, 생략의 충분 조건과 최소 필요 검사 집합을 별도로 묻는다.'},
 {'development_id':'QBF01-DEV066','pattern_ids':['조건부방향','BFP014'],'evidence_event_ids':['QBF01-U0397-Q02-S02','QBF01-U0398-Q04-S02','QBF01-U0410-Q03-S01'],
 'finding':'BID에서 분모 감소는 분자의 변화가 미정이면 비율 증가를 보장하지 않는다. BII에서 동일 담보의 한도비율 인하 효과와 담보가치도 오른 전후 실제 한도는 다른 비교이다. BJR에서 특수성이 만든 위험과 대응 후 실제 위험도 다른 기준이다.',
 'decision':'세 사례를 변화 방향이라는 말만으로 단일 연산으로 확정하지 않는다. BID는 비율식의 미지 입력, BII는 고정 조건의 효과와 관측 전후 변화, BJR은 원래 위험과 대책 후 결과의 구별이다. BII를 재고·순유입 관계의 BFP014 반복 사례로 계수하지 않는다.',
 'next_counterexample':'BID는10/2→4/1, BII는100×.8→150×.6과150×.8의 비교가 각각 다른 추론 공백을 드러낸다. 두 항의 단조성만으로 정확 함수나 단일 효과 크기를 추가하지 않는다.',
 'educational_use':'증가·감소 앞에 무엇을 고정하고 무엇과 비교하는지 적는다. 비율 문항은 분자 조건과0분모를, 정책 문항은 비교 기준 시점과 동일 조건 여부를 명시한다.'},
 {'development_id':'QBF01-DEV067','pattern_ids':['필요요건역전금지','강도보존','속성분리'],'evidence_event_ids':['QBF01-U0404-Q01-S01','QBF01-U0404-Q01-S02','QBF01-U0407-Q01-S02','QBF01-U0409-Q01-S02','QBF01-U0409-Q03-S01','QBF01-U0412-Q03-S01'],
 'finding':'BIX는 정당성의 필요조건과 약한 적용/미적용을 구별한다. BJF는 별도 정당화 필요와 불가능을, BJL은 정당화 부담과 그 충족을, BJN은 평가 적용 자격 결여와 중립값 부여를, BJY는 권리자격과 계산 집합을 구별한다.',
 'decision':'모두 조건 확인이라는 한 문장으로 합치지 않는다. 성공에 필요한 내용, 별도 심사 요구, 실제 충족 여부, 평가어의 정의 가능성, 집계 대상 자격은 입력과 출력이 다르다. BJN과BJL 두 번째 장면은 좁은 기존 후보에 억지 배정하지 않은 상태를 유지한다.',
 'next_counterexample':'BIX에서 인권취지에 부합해도 다른 정당성 조건이 부족할 수 있다. BJN에 경험 주체가 생겨도 곧바로 특정 가치가 정해지지는 않는다. BJY는 권리 상실에도1804계산에는 남아 있다.',
 'educational_use':'조건이 무엇을 가능하게 하는지 먼저 명시한다. 적용 여부·정도·정당화 부담·충족 사실·집계 포함을 별도 질문으로 제시하여 학생이 자동 치환하지 않게 한다.'},
 {'development_id':'QBF01-DEV068','pattern_ids':['관계귀속','비교축','분류기준'],'evidence_event_ids':['QBF01-U0401-Q03-S01','QBF01-U0411-Q02-S01','QBF01-U0412-Q02-S02','QBF01-U0413-Q01-S01','QBF01-U0413-Q03-S01','QBF01-U0413-Q03-S02'],
 'finding':'BIQ는 차별 배제와 국가관 전환의 각각 다른 공통점을 비교한다. BJU는 이익 대표의 중앙 집약과 정부 권력 집중을 구별한다. BJX는 같은 혁명기의 사회 관념/입법자 태도를, BJZ는 정책 실행자의 목적/관찰자의 해석을 구별한다. BKB는 태도 유사성을 동시대나 공통 혈통으로 올리지 않는다.',
 'decision':'같은 이름·같은 시기·같은 어휘의 공유와 실제 관계 동일성을 분리한다. 비교축 후보의 상위 공통성은 유지하되 각 기출에서 비교하는 항목을 개별적으로 작성한다. 해석 불일치를 실제 인물 생몰연대의 외부 사실로 보강하지 않는다.',
 'next_counterexample':'공통 가치가 특정 시대에만 허용된다는 연결이나 실제 연대가 추가되면 BKB의 판단 근거가 달라진다. 정책 주체가 보편 시민을 의식적 목표로 삼았다고 주어지면 BJZ⑤도 재검토 대상이다.',
 'educational_use':'시기 표 안에 주체를 나누고, 같은 주체에 붙은 대상·목적·평가 축을 표시한다. 출제 시 표면어를 보존하면서 주체나 비교 관계 하나를 바꿔 오류의 위치를 명확히 만들 수 있다.'},
 {'development_id':'QBF01-DEV069','pattern_ids':['관계귀속','강도보존'],'evidence_event_ids':['QBF01-U0396-Q02-S01','QBF01-U0397-Q02-S02','QBF01-U0400-Q03-S02','QBF01-U0403-Q01-S01','QBF01-U0408-Q01-S01'],
 'finding':'BIA의 상대적 제도 예측은 거래 증가의 모든 가능성을 닫지 않는다. BID의 비율 방향과 BIN의 여성 본인 형벌은 각각 추가 전제가 남는다. BIU는 분열 후손의 분화이지 줄기세포가 절대 움직이지 않는다는 설명이 아니다. BJI 최초 해설의 앞/뒤 호르몬 표현은 실제③의 테스토스테론→항뮐러관인자 방향으로 보완했다.',
 'decision':'BIA·BID·BIN 유보41누적 중 해당 세 건 유지. BJI 정답은 불변이고 원 blind 문장을 덮어쓰지 않으며 BJF_BJH_BJI_prior_review.json에 표현 보완 이력을 남긴다. BJA/BJF/BJR/BJX와 BIQ의 인라인·범위는 기존 복원 승계이며 이번 신규 원문 복원 성과로 계수하지 않는다.',
 'next_counterexample':'본인 형벌의 규정이나 분자 변화 조건이 추가되면 현재 유보 범위를 재검토할 수 있다. 원문을 확인했다는 사실만으로 문장 사이의 의미 공백까지 자동 해소된 것은 아니다.',
 'educational_use':'공식답 선택의 직접 근거, 나머지 선지의 비유도성, 반대 명제의 증명 여부를 별도로 설명한다. 수정 이력을 교재 제작 단계까지 보존한다.'}
]
existing={r['development_id'] for r in rows(OUT/'pattern_development.jsonl')}
assert not any(r['development_id'] in existing for r in devs)
append('pattern_development.jsonl',devs)
c=json.loads((OUT/'checkpoint.json').read_text())
assert c['reviewed_questions']==720 and c['new_scene_count']==1120
holds=sum(x['unresolved_questions'] for x in c['by_exam'].values())
append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT018','batch':18,'date':'2026-10-15','sample_case_ids':cases,'sample_questions':len(sample),'sample_scenes':sample_scenes,'sample_options':sample_options,
 'method':'주 에이전트 직접 감사. 표본18문항의 현행 전체 선지 근거·추론·후보 연결 확인. BIA/BID/BII/BIN/BIK/BIQ/BIU/BIX는 지문 전체·전체 선지를 다시 읽고 관련 보기와 유보 보조자료를 대조. BIK A/B그래프·BIU도식·BJE그래프 직접 재확인. 나머지 표본은 이번 연속 작성에서 직접 읽은 원문·보기·최초풀이 및 현행 기록을 다시 대조. 기계적 구간·출처 검사는18배치40문항만 수행.',
 'dimensions':{'중간추론':'분모 조건, 동일 담보의 효과, 고유/겉보기 밝기의 입력, 비순환성의 검사 함축, 자격과 계산 집합을 점검.','전체선지':f'표본{sample_options}선지의 채택·배제 근거. 보기의 하위 명제와 조합 선지를 구별.','원문이력':'BIQ 범위와 BJA/BJF/BJR/BJX 인라인은 기존 복원 승계.4n 지수서식은 BJC/BJE 판단에 사용하지 않음. 원문 무수정.','후보경계':'BFP015 단일 후보, BFP014와BII의 비동일성, BJN/BJL 일부 장면 빈 연결 유지. 후보 D/E/F의 사례 복사 없음.','활용':'구조 조건·분자 조건·평가어 적용 조건·비교 주체를 출제 조건에 명시하여 유일성 검토.'},
 'findings':[{'cases':['BIA','BID','BIN'],'issue':'공식답과 추가 전제의 공백','resolution':'기존/추가 유보 유지. 반대 명제의 일괄 확정 금지.'},{'cases':['BJE'],'issue':'특정 입력에서 검사 중복','resolution':'BFP015 단일 후보 승인, 현재 그래프와 별도 순환 반모형 구별.'},{'cases':['BIK','BIU'],'issue':'시각 자료의 정보 범위','resolution':'A/B유형·얕은 골·정규화 및 세포 위치/유형 구별 직접 대조.'},{'cases':['BJI'],'issue':'기존 해설의 호르몬 방향 표현','resolution':'author018i의 구체 방향 보완 확인. 정답·원기록 불변. 표본 외 별도 표현 이력 확인.'}],
 'decision':f'18배치{len(batch)}문항·{batch_scenes}장면 저장과 표본{len(sample)}문항·{sample_scenes}장면 감사·귀납 완료. 누적720문항1120장면,유보{holds}문항. 중대한 진행 차단 오류0.721부터19배치 계속.',
 'unresolved_blocking_error_count':0,'limitations':'표본 외 의미 무오류 보장이나 공식 정답표 독립 전수 검증 아님. 보호 원장 전수 해시·다른 모델 호출·Git push 없음.'}])
finish('audit_018.py',[r['case_ids'][0] for r in batch],['18배치 표본18문항30장면90선지 감사. DEV065~069. BFP015 단일 후보. 유보41 유지.721부터 계속.'])
c=json.loads((OUT/'checkpoint.json').read_text())
c.update(last_saved_author='author_018m.py',last_saved_audit='audit_018.py',next_sample_audit_at=760)
write('checkpoint.json',c);write('batch_018_checkpoint.json',c)
write('batch_018_validation.json',json.loads((OUT/'audit_018_validation.json').read_text()))
for name in ['continuous_research_progress.json','session_handoff_20261015_05.json']:
 x=json.loads((OUT/name).read_text())
 x.update(last_saved_author='author_018m.py',last_saved_audit='audit_018.py',next_sample_audit_at=760)
 if name.startswith('session_'):
  x['last_saved_script']='author_018m.py';x['last_validation']='audit_018_validation.json';x['last_development']='QBF01-DEV069'
 write(name,x)
print(f'18배치 감사 완료:{len(batch)}문항{batch_scenes}장면.표본{len(sample)}문항{sample_scenes}장면{sample_options}선지.유보{holds}.721부터 계속.')
