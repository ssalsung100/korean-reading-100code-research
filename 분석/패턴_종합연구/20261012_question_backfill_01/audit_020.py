import sys,json,itertools
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write
from resume_support_20261016 import finish
assert not any(r['audit_id']=='QBF01-AUDIT020' for r in rows(OUT/'semantic_sample_audits.jsonl'))
c=json.loads((OUT/'checkpoint.json').read_text())
assert c['reviewed_questions']==800 and c['new_scene_count']==1255
batch=[r for r in rows(OUT/'current_question_reviews.jsonl') if r['batch_number']==20]
assert len(batch)==40 and sum(len(r['scenes']) for r in batch)==67
cases=['BMM','BMV','BMW','BNB','BNC','BNR','BNV','BNX','BNZ','BOC','BOH','BOL','BOM','BOP','BOR','BOV']
sample=[r for r in batch if set(r['case_ids'])&set(cases)]
assert len(sample)==16
byid={s['event_id']:s for r in batch for s in r['scenes']}
bor=byid['QBF01-U0454-Q01-S01']
old=bor['pattern_connections'];new=[p for p in old if p['pattern_id']!='비교변인']
assert len(old)==2 and len(new)==1
assert not any(r['amendment_id']=='QBF01-AMD049' for r in rows(OUT/'scene_amendments.jsonl'))
# 실제 자료가 아닌 소규모 정수 모형으로 주 에이전트의 부등식 논증을 검산한다.
tested=0
for sizes in itertools.product(range(1,8),repeat=3):
 for before,after in itertools.product(range(1,9),repeat=2):
  a=[x for x in sizes if x>=before];b=[x for x in sizes if x>=after]
  if a and sum(b)>sum(a):
   assert after<before and min(b)<min(a)
   tested+=1
assert [x for x in [2,4,7] if x>=4]==[x for x in [2,4,7] if x>=3]
assert 2+2*3==8 and 36-2==34 and 38-2==36
assert all(x<=100 for x in range(101))
devs=[
 {'development_id':'QBF01-DEV075','pattern_ids':['단계구분','관계귀속'],
  'evidence_event_ids':['QBF01-U0438-Q01-S01','QBF01-U0438-Q01-S02','QBF01-U0438-Q02-S01','QBF01-U0450-Q03-S02'],
  'finding':'BMV의NAD+는 해당작용의 입력이면서 발효의 재생 산물이며 BOH의F는 앞 효소의 산물이자 뒤 효소의 기질이다. BMW의 직접ATP·조효소 전환·전체 수율은 합산 범위를 달리한다. 입력/출력 관계 복원 뒤에도 전체 보유량의 순변화는 별도 정보가 필요하다.',
  'decision':'물질의 역할을 단계에 붙이는 공통 행동을 확인하되 생성 경로 확인과 보유량 증감을 통합하지 않는다. BMV는 BFP014의 순유입 개선/초기 순유입 조건을 충족하지 않으므로 독립 반복으로 계수하지 않는다. 기존 후보 정의 수정 없음.',
  'next_counterexample':'생성=소비이면 생성 경로가 작동해도 보유량은 일정하다. 같은 물질이 앞 단계의 산물이므로 축적되지 않는다는 일반화를 BOH가 깨뜨린다. BMW에서 개수 비교를 에너지 환산으로 바꾸면 질문 자체가 달라진다.',
  'educational_use':'각 숫자와 물질에 과정·입력/출력·직접/환산·총량/순량을 붙인다. 새 문항에서 농도 변화를 요구하면 부피와 소비 항도 명시한다.'},
 {'development_id':'QBF01-DEV076','pattern_ids':['강도보존'],
  'evidence_event_ids':['QBF01-U0440-Q01-S02','QBF01-U0440-Q02-S01','QBF01-U0446-Q03-S02','QBF01-U0452-Q02-S02'],
  'finding':'BNB의지표 개선은 식별 위험의 엄격 증가를 보장하지 않는다. BNC는 실제 잔존율 증가와 고정 그룹 조건을 함께 써 새 집합 크기m<이전k≤이전 최소를 도출한다. BNV는정확값 대신100%상한으로 더 큼을 배제하며 BOM은정치적 제약 약화의 가능성 추론에 머문다.',
  'decision':'변화 방향이라는 표면 유사성으로 한 연산에 합치지 않는다. BNC는조건부 수학적 증명,BNV는경계값 배제,BNB는충분성 공백,BOM은본문 정치 모형의 경향 추론이다. BNV의AMD048 빈 후보 연결 유지. 신규 상한 후보를 한 문항만으로 만들지 않는다.',
  'next_counterexample':'k를낮춰도 새 통과 집합이 없으면 최소는 같다. 기존 잔존이0이면 이전 최소는 정의되지 않는다. BNV에서 비교 상대가60%이면100%상한만으로 더 큼을 배제할 수 없다. 유사도가 공통 속성 복원으로만 증가하면 식별 후보가 같을 수 있다.',
  'educational_use':'결론의 엄격 부등호를 지지하는 추가 정보가 무엇인지 표시한다. 비교에 충분한 상한·하한이 있으면 불필요한 정확값 계산을 요구하지 않는다.'},
 {'development_id':'QBF01-DEV077','pattern_ids':['범위이동','포함반례','문맥조작화'],
  'evidence_event_ids':['QBF01-U0435-Q01-S02','QBF01-U0448-Q01-S02','QBF01-U0451-Q01-S01','QBF01-U0455-Q02-S01','QBF01-U0455-Q02-S02'],
  'finding':'BMM의특별한 존재는 신성 인정이라는 문맥 제한이 있어야 수용된다. BNZ의반환재판 제한은 모든 재판의 영구 금지가 아니며 BOI의조건부 평가는 역할 전체의 정의가 아니다. BOV는주기·행위별 복합 제한을 읽은 뒤 결함 예외를 전칭에 대입한다.',
  'decision':'조건·시점·행위·대상을 보존하는 원리는 공유하지만 넓은 어휘의 문맥 한정과 실제 포함 반례의 발견을 같은 연산으로 합치지 않는다. BMM 유보를 해소하지 않으며 BNZ에서 변경 가능의 구체 요건을 새로 만들지 않는다.',
  'next_counterexample':'예외를 제외한 범위로 선지를 좁히면 BOV의단일 반례가 바로 적용되지 않는다. BMM의특별함을 일반 존경까지 넓히면 본문 근거가 부족하다. 한 절차에서 판단하지 않는다는 사실은 다른 절차의 특정 결론을 보장하지 않는다.',
  'educational_use':'전칭의 범위와 예외의 소속을 함께 표시한다. 제한 규칙을 새 문항으로 옮길 때 적용 주체·시점·행위를 삭제하지 않는다.'},
 {'development_id':'QBF01-DEV078','pattern_ids':['관계귀속','반박표적','표현행위'],
  'evidence_event_ids':['QBF01-U0445-Q02-S01','QBF01-U0445-Q02-S02','QBF01-U0447-Q02-S01','QBF01-U0452-Q02-S01','QBF01-U0453-Q02-S01','QBF01-U0453-Q02-S02'],
  'finding':'BNR는선택자/계승자 관계를 대응하고 알 수 없는 복제를 억지로 정하지 않는다. BNX는주관적 감정과 사실적 기술을 분리한다. BOM은무효화와 여론 추종이라는 반대 방향의 난제를 나누며 BOP는침해 옹호 논변이 넘는 문턱과 조건부 양보의 비판 방향을 확인한다.',
  'decision':'관계귀속을 붙이는 데 그치지 않고 누가 무엇을 사실·조건·평가로 진술하며 무엇을 문제 삼는지 기록한다. 비판 방향의 동조를 논거의 동치로, 입장 추론을 실제 개인의 단일한 심리로 확대하지 않는다.',
  'next_counterexample':'BNR의인명 하나만 교정해도 복합 선지의 적자 지위 입증이라는 잘못된 결론은 남는다. BOP의권리가 넘는 문턱으로 주체를 바꾸면 원래 논증 부담의 방향이 사라진다. 감정을 다룬다는 사실만으로 진릿값 가능성을 결정할 수 없다.',
  'educational_use':'논항과 문장 지위를 복원한 뒤 비판 대상과 결론을 검사한다. 설령이라는 양보를 실제 승인과 구분한다.'},
 {'development_id':'QBF01-DEV079','pattern_ids':['되먹임고리','중간시점','수치표상'],
  'evidence_event_ids':['QBF01-U0449-Q01-S02','QBF01-U0452-Q01-S01','QBF01-U0454-Q01-S01'],
  'finding':'BOC는운동M0→소설N→후속 운동M1로 시간차의 되먹임을 복원한다. BOL은초기 반발과 후기 수용을 다른 시점에 놓는다. BOR는증가하는 생산 수준과 감소하는 한계 증가폭을 구별하고 고정 모형 조건을 유지한다.',
  'decision':'시간별 상태가 다르다는 공통점만으로 되먹임과 단순 변화,한계효과를 통합하지 않는다. BOR의모형 고정 조건을 두 집단 비교 패턴인 비교변인에 연결한 과잉을AMD049로 철회. 한 단위 증가폭 판독이라는 수치표상 연결만 제한적으로 유지한다.',
  'next_counterexample':'후속 운동에 소설의 영향이 없다면 되먹임이 아니다. 반발 뒤 수용의 경향은 모든 사례의 필연적 수렴이 아니다. 생산 수준 증가와 한계 증가폭 감소는 모순이 아니며 정비례도 아니다.',
  'educational_use':'반복되는 명사에 시점을 붙이고 값·증가폭·인과 경로를 따로 표시한다. 모델의 고정 가정과 실험 비교의 통제는 다른 절차로 가르친다.'}
]
existing={r['development_id'] for r in rows(OUT/'pattern_development.jsonl')}
assert not any(d['development_id'] in existing for d in devs)
allids={s['event_id'] for r in rows(OUT/'current_question_reviews.jsonl') for s in r['scenes']}
assert all(e in allids for d in devs for e in d['evidence_event_ids'])
append('scene_amendments.jsonl',[{'amendment_id':'QBF01-AMD049','event_id':bor['event_id'],'reason':'20배치 직접 감사: 비교변인 후보는 두 집단의 조작·정보·환경을 나란히 놓는 정의다. BOR의 단일 모형에서 인구·기술 가정을 유지하는 행동까지 자동 확장하지 않는다. 추론과 정답·장면수는 보존하고 이 후보 연결만 철회.','changes':[{'field_path':'pattern_connections','old_value':old,'new_value':new}]}])
write('audit_020_selected_checks.json',{
 'scope':'주 에이전트의 직접 표본 의미 감사와 가상 반모형 검산. 실제 관측 자료나 기출 원문 수정 아님.',
 'BMM':'②를 신성 인정으로 좁힌 문맥 수용의 유보 유지.⑤의 개인 구원/스승 추종은 보완 관계이며 쇠락의 원인 연결은 별도 근거가 없다.',
 'BMV_BMW':{'finding':'NAD+ 재생/소비와 순량을 분리. BFP014 반복으로 계수하지 않음.2+2×3=8,36/38−2=34/36,ATP2와NADH2는 개수 비교. 산소는 필요조건이지 경로의 유일 선택 조건 아님.','hypothetical_countermodel':'일정 부피에서 재생10·소비10이면 보유량 일정. 실제 근육의 측정값이 아님.'},
 'BNB':'공통 속성의 복원만으로 유사도가 증가할 수 있는 가상 모형은 식별 가능성의 엄격 단조 보장 부재를 드러냄. 기존 유보·공식② 유지.',
 'BNC':{'proof':'고정 원본·전처리·그룹 및 이전 잔존 비공집합. 잔존율 실제 증가→새 통과 집합 존재→새m<이전k≤이전최소.','finite_checks':tested,'limit':'유한 검산이 일반 증명을 대체하지 않음. k완화만으로 엄격 변화는 보장되지 않음.'},
 'BNR':'선택자 문왕/인조,계승자 무왕/효종 대응. 태사 복제 미정 유지. 종통을 확고히 해야 한다는 당위어가 항상 현재 부재를 함축한다는 일반화 금지.',
 'BNV':{'finding':'녹색→X적색→Y활성산소의 간접 경로. Z50% 제거 뒤 양수이지만 사멸률50%는 미확정. XZ100%를 넘는 사멸률은 불가능.','candidate_link':'AMD048에 따라 상한 장면의 빈 후보 연결 유지. 정확한YZ 사멸률 미확정 허용.'},
 'BNX':'감정 내용의 주관성과 사실적 진술의 참/거짓 가능성을 분리.ㄱ의 공익 범위를 모든 개인적 쾌락으로 확대하지 않음.',
 'BNZ':'승소와 실행,반환과 본안 범위를 구별. 합의 경로에까지 승소 필요를 강제하지 않음.',
 'BOC':'M0→N→M1 시간차 되먹임. 같은 사건의 자기 선행 원인이나 소설의 유일 원인 주장이 아님.',
 'BOH':{'visual':'data/기본기_연구/prepared_backlog/blind_sources/BOH_official_table_crop.png','finding':'이번 직접 확인한㉣ 병합셀은 두 반응을 맡음. 생성 차단/이미 존재한 물질 소멸 분리. F의 앞 산물/뒤 기질 역할 동일성 확인. 기존 복원 승계.'},
 'BOL_BOM':'반응 수렴은 경향이며 기제 동일성 아님. 높은 관심과 무반응의 논리적 양립 가능성은 남김. 두 난제와 정치적 제약 약화는 문맥 모형으로 한정하고 개인 심리·위헌 필연성으로 확대하지 않음.',
 'BOP':'문턱을 넘는 주체는 침해 옹호 논변.③ 조건부 양보의 다른 비판 경로는 동조 가능성이지 논거 동치 아님.',
 'BOR':'명시 문장으로 판정. 그래프 새 판독·수식 복원 성과 없음. 고정 모형 조건/두 집단 비교를 분리하여AMD049로 비교변인 연결 철회.',
 'BOV':'한 주기의 상한·예정 이식 수·행위를 결합.착상 전/후 및 채취/수정 구별.결함 예외로⑤ 전칭 배제.',
 'new_amendments':['QBF01-AMD049'],'holds_preserved':['BMM','BNB'],'pass':True})
append('pattern_development.jsonl',devs)
ss=sum(len(r['scenes']) for r in sample)
append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT020','batch':20,'date':'2026-10-16','sample_case_ids':cases,'sample_questions':len(sample),'sample_scenes':ss,'sample_options':len(sample)*5,
 'method':'주 에이전트 직접 감사. 표본16문항의 전체 지문·발문·5선지와 현행 추론·적용 경계·교육/출제 조건을 대조. 이번 신규 BOH/BOL/BOM/BOP/BOR/BOV는 작성 때 직접 검토한 원문과 저장 결과를 재대조. BOH 공식 표 직접 시각 확인. 기존10문항은 감사에서 원문과 현행 추론을 직접 재독. 기계적 인용·출처 검사는20배치40문항에 한정.',
 'dimensions':{'중간추론':'순량/경로,엄격 증가,상한 비교,조건부 양보,논항·시점 범위 검사.','전체선지':'표본80선지와 BNX 보기ㄱㄴㄷ 직접 검토.','원문이력':'BOH 표 병합셀 재확인. BOR 수식 글리프 손상은 남고 결정 근거는 명시 문장. 기존 원문 복원과 이번 해석을 구분.','후보경계':'BFP014 독립 반복 미계수·AMD048 유지·AMD049 과잉 연결 철회. DEV075~079 귀납.','활용':'필수 전제·정오 전환·고정 조건·미확정값과 유보 보존.'},
 'findings':[{'cases':['BMM','BNB'],'issue':'문맥 범위 및 엄격 단조성의 충분성 한계','resolution':'기존 유보 유지. 공식답과 반대 명제 확정의 구별.'},{'cases':['BNC','BNV'],'issue':'정확값 대신 결론에 필요한 증거의 충분성','resolution':'실제 증가에서 새 집합 존재를 도출;100%상한으로 초과 비교 배제. 각자의 전제·경계 보존.'},{'cases':['BOR'],'issue':'후보 정의보다 넓은 연결','resolution':'AMD049로 비교변인 연결만 제거. 장면·정답·근거 불변.'},{'cases':['BNR','BNX','BNZ','BOM','BOP','BOV'],'issue':'논항·진술 지위·절차 범위·예외','resolution':'각 비교에 필요한 주체와 조건을 유지. 미정 내용을 임의 보충하지 않음.'}],
 'decision':f'20배치40문항67장면,표본16문항{ss}장면80선지 감사 및DEV075~079 저장. 누적800문항1255장면·유보46. 신규 후보 없음,AMD049 연결1건 철회.801부터 계속.',
 'unresolved_blocking_error_count':0,'limitations':'표본 밖의 의미 무오류나 공식답 전수 독립검증을 보증하지 않음. 기존 유보 해소 선언 없음. 다른 모델 호출·Git push·보호 원장 전수 해시 없음.'}])
finish('audit_020.py',[r['case_ids'][0] for r in batch],['20배치 표본16문항29장면80선지 감사·DEV075~079 귀납. BMM/BNB 유보 및AMD048 유지. AMD049 BOR 비교변인 연결 철회. 801부터21배치 계속.'])
write('batch_020_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
write('batch_020_validation.json',json.loads((OUT/'audit_020_validation.json').read_text()))
print('20배치 감사 완료',len(sample),ss,'다음801')
