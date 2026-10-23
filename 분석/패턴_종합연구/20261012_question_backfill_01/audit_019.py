import sys,json,itertools
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write
from resume_support_20261015_07 import finish
assert not any(r['audit_id']=='QBF01-AUDIT019' for r in rows(OUT/'semantic_sample_audits.jsonl'))
c=json.loads((OUT/'checkpoint.json').read_text())
assert c['reviewed_questions']==760 and c['new_scene_count']==1188
batch=[r for r in rows(OUT/'current_question_reviews.jsonl') if r['batch_number']==19]
assert len(batch)==40
cases=['BKE','BKJ','BKP','BKR','BLC','BLH','BLI','BLR','BLU','BLW','BLZ','BMD','BMG','BMH','BMJ','BML']
sample=[r for r in batch if set(r['case_ids'])&set(cases)]
assert len(sample)==16
# 주 에이전트가 작성한 반모형의 진릿값만 검산. 의미 판단 자동 생성 아님.
assert {'a','b'}!={'a','c'} and {'a'}<={'a','b'} and {'a'}<={'a','c'}
models=[{'R':r,'S':s,'U':u} for r,s,u in itertools.product([False,True],repeat=3) if (not(r and s) or u) and not u]
assert any(not m['R'] and m['S'] for m in models)
assert all(not m['S'] for m in models if m['R'])
assert 8>0 and 12>8
write('audit_019_selected_checks.json',{
 'scope':'19배치 표본 직접 의미 감사의 보조 검산. 가상 수치·집합·진릿값은 실제 본문 관측값이 아님.',
 'BKE':{'direct_visuals':['G453_visual01.jpg','G453_visual02.jpg','2019/page_005.png'],'finding':'개별(나)그림의 눈금은 잘려 있지만 공식페이지에서는10nm 확인. (가)30nm와 두 점 분리의 범위 근거 확인. 배율과 전자 속력의 비율 동일시 금지. 기존 최초 판독 제한 보존.','scope':'본문의 장치 조절 모형 적용이며 영상만으로 전류의 유일 원인을 식별했다는 일반 주장 아님.'},
 'BKJ':{'hypothetical_utilities':{'무개입':0,'제거':8,'다른대안':12},'finding':'양의 증분 효용과 전역 최대는 다르다. 제거/무개입 비교의 문맥 수용 및 대안 집합 유보 유지.'},
 'BKP':{'finding':'성공 측의 기능 동일→빨간 온수 꼭지 사용이면 양쪽 모두 미사용 반박에 충분. 실패 측의 정확한 대체 행동은 미확정 유지.'},
 'BKR':{'finding':'Lite의 한 표현을Full도 표현하더라도 전체 표현력은 다를 수 있다. 모든A는B에서A⊆B이며 진포함이나 역포함까지 증명하지 않는다. 최대 표현력과 계산 보장의 선택 조건 분리.'},
 'BLC':{'countermodel':{'whole1':['a','b'],'whole2':['a','c'],'selected1':['a'],'selected2':['a']},'finding':'전체 차이만으로 선택된 일부의 차이 보장 불가. 이는 실제 종간 동일성의 증거가 아니며⑤는 별도 분화·조합 변화 근거로 지지.'},
 'BLH':{'finding':'거부 발화→입술 다뭄과 뒤의 마지못한 수령을 시점별로 구별. 사심으로 오해받았을까 하는 추측과 실제 사심 구별. 보기 전체 재독.'},
 'BLI':{'finding':'불로소득 과세/소유자 귀착→공정성과 초과부담 억제→효율성을 병렬로 유지. 효율성→공정성의 별도 인과는 미제시.'},
 'BLR':{'direct_visuals':['G467_visual01.jpg'],'restoration':'K=mv²/2,U=-GMm/r,E=K+U 기존 부록 승계','finding':'원궤도들 간 비교와 중력만 작용하는 구간 내 보존을 구별. 거리→중력 약화는 최초 풀이의 배경지식으로 명시되어 있고 공식 원문에 힘의 역제곱식이 있었다고 하지 않음. 감속→작은 타원→짧은 주기 연결 유지.'},
 'BLU':{'finding':'후대 유해물질 이동·잔류·미보정이 있어야 옛층의 형성시기와 노출시기를 혼동하는 경로 성립. 수분 양분 이동만으로 오차 필연성은 보장하지 않아 유보 유지.'},
 'BLW':{'rule':'R∧S→U','models_with_not_U':models,'finding':'관련성R이 추가되어야¬U로부터¬S 추론. 사용 사실→피해자 적극 대변은 도출되지 않음. 공식[B] 괄호 이미지와 보기 전체 재확인.'},
 'BLZ':{'finding':'불일치만으로 교정 대상을 확정하지 않음. 모델 시간정보 확장과 원로그 시각의 단순 차감 가능성을 구별. 보기의 정보보호 목적은 필수ID 삭제를 함축하지 않음.'},
 'BMD':{'countermodel':'A부류 모두1,B부류 모두2인 배분은 규칙 적용 일관성과 결과 차이가 양립함을 보여 줌. 실제 정당성 증명 아님.'},
 'BMG_BMH_BMJ_BML':{'finding':'이번 직접 작성분8장면의 전 선지·논항·조건·수정 제안 재확인. BMG 두 응보의 주체 차이, BMH 원칙과 전칭, BMJ 이름 하나 교환만으로 복합선지 전체 교정 불가, BML 설명/처방을 점검.'},
 'holds':['BKJ','BLU','BLW'],'new_amendments':[],'pass':True})
devs=[
 {'development_id':'QBF01-DEV070','pattern_ids':['포함반례','부분전체'],
  'evidence_event_ids':['QBF01-U0418-Q03-S02','QBF01-U0419-Q02-S01','QBF01-U0423-Q01-S02','QBF01-U0433-Q02-S02'],
  'finding':'BKP는 모두 명제의 한쪽 반례만으로 충분하고 BMH는 범주에 속하는 잔존 형벌 하나로 전체 소멸을 깨뜨린다. BKR는 서로 다른 전체 표현력의 언어가 한 온톨로지를 공유할 수 있음을, BLC는 서로 다른 전체에서 같은 부분이 선택될 수 있음을 보여 준다.',
  'decision':'포함반례와 부분전체를 통합하지 않는다. 전자는 이미 주장된 전칭을 실제 반례로 깨는 연산, 후자는 전체/부분의 동일성 귀속을 검사하는 연산이다. 미확정 잔여 정보를 억지로 채우지 않는다는 상위 지도 원리만 공통으로 남긴다. 신규 후보 등록 없음.',
  'next_counterexample':'모두를 일부로 바꾸면 단일 반례가 충분하지 않다. 전체 차이를 이루는 정보가 반드시 선택된다는 연결을 주면 BLC 반모형은 제한된다. 공통 부분이 존재할 가능성은 실제 동일성의 증명이 아니다.',
  'educational_use':'학생에게 결론에 필요한 최소 증거와 아직 모르는 정보를 따로 쓰게 한다. 출제자는 전칭 범위·반례 소속·부분 선택 규칙을 명시해야 한다.'},
 {'development_id':'QBF01-DEV071','pattern_ids':['필요요건역전금지','복수문턱','강도보존'],
  'evidence_event_ids':['QBF01-U0416-Q02-S01','QBF01-U0416-Q02-S02','QBF01-U0429-Q01-S03','QBF01-U0429-Q03-S02','QBF01-U0430-Q03-S02'],
  'finding':'BKJ의 실행 능력은 의무의 충분조건이 아니며, 양의 효용은 최대 효용을 보장하지 않는다. BLW는 결합 조건의 실패에서 신뢰성만 특정하려면 관련성이 필요하다. BLU의 이동 경로와 BLZ의 모델 확장 필요성도 각기 추가 조건과 분석 목적을 요구한다.',
  'decision':'부족한 연결을 하나의 필요조건 오류로 몰지 않는다. BKJ는 대안 집합, BLW는 다른 요건 충족, BLU는 물질 이동·잔류·미보정, BLZ는 모델 기반 분석이라는 범위를 따로 남긴다. BKJ/BLU/BLW 세 유보 유지, 공식답 불변.',
  'next_counterexample':'제거8·무개입0·다른 대안12, R거짓·S참·U거짓, 유해물질 비이동 또는 이동보정, 원로그의 시각 차감이 각각 다른 경계를 드러낸다.',
  'educational_use':'풀이자는 어떤 조건을 추가하면 추론이 성립하는지 명시한다. 신규 문항은 그 조건을 직접 제공하거나 결론 강도를 낮춰 복수정답을 방지한다.'},
 {'development_id':'QBF01-DEV072','pattern_ids':['관계귀속','설명수준','비교축'],
  'evidence_event_ids':['QBF01-U0424-Q03-S02','QBF01-U0433-Q01-S02','QBF01-U0434-Q01-S01','QBF01-U0434-Q03-S01','QBF01-U0434-Q03-S02'],
  'finding':'BLH의 불순한 사심은 오해에 대한 추측이고, BMG의 화복 응보 비판과 범죄자 처벌은 논항이 다르다. BMJ는 두 이론의 술어가 한 선지에 혼합되며 BML은 국가의 안전 명분을 푸코의 해법으로 옮긴다.',
  'decision':'관계귀속의 적용은 단순 인명 대조를 넘어 누가 어떤 상태를 사실·추측·평가·처방으로 말했는지까지 구체화하되 각 사례의 독립 연산을 보존한다. 생산적 권력의 생산을 좋은 결과라는 평가로 읽지 않는다. 기존95후보 정의 수정 없음.',
  'next_counterexample':'분석자가 실제로 해당 해법을 권고하는 문장을 추가하면 BML의 배제 근거가 달라진다. BMJ는 이름 하나를 바꾸면 다른 절이 다시 어긋나므로 모든 핵심 절을 검사해야 한다.',
  'educational_use':'행위자·분석자·추측자와 서술 내용의 지위를 함께 표기한다. 출제 시 어휘를 유지하면서 논항 또는 발화 행위 하나만 교환할 수 있으나 원래 관계는 분명히 제시해야 한다.'},
 {'development_id':'QBF01-DEV073','pattern_ids':['비교축','병치인과분리','속성분리'],
  'evidence_event_ids':['QBF01-U0425-Q01-S02','QBF01-U0432-Q01-S01','QBF01-U0433-Q01-S01','QBF01-U0434-Q01-S02'],
  'finding':'BLI의 공정성과 효율성은 각각 근거를 갖는 병렬 장점이다. BMD의 일관 적용과 내용 정당성, BMG의 엄격 집행과 과잉 처벌, BMJ의 상징적 단일성과 실제 공유는 서로 다른 기준의 판단이다.',
  'decision':'서로 다르다는 이유로 무조건 양립이라 하지 않는다. 각 술어의 대상·기준을 고정하고 본문이 인정한 관계를 확인한다. BLI의 인과 부재와 나머지의 차원 구별은 다른 연산으로 보존한다.',
  'next_counterexample':'같은 차원의 실제 권력 독점/공유는 다른 문제가 된다. 일관되게 적용한 규칙의 내용이 정당하다는 추가 근거가 있으면 BMD의 실질 평가도 달라진다.',
  'educational_use':'반대처럼 보이는 두 말에 각각 비교 기준을 붙이고, 함께 제시된 두 장점에는 각자의 근거를 붙인다. 이름의 유사성·반대성만으로 인과나 모순을 만들지 않는다.'},
 {'development_id':'QBF01-DEV074','pattern_ids':['조건부방향','관계귀속'],
  'evidence_event_ids':['QBF01-U0414-Q03-S01','QBF01-U0414-Q03-S02','QBF01-U0428-Q01-S01','QBF01-U0428-Q01-S02'],
  'finding':'BKE의 눈금은 물체 거리·배율의 근거이며 전자 속력 비가 아니다. BLR에서 복원한 에너지식과 최초 사용 배경지식은 출처가 다르다. 분사 순간의 속력 변화가 경로 변경 뒤의 주기를 그대로 결정하지 않는다.',
  'decision':'공식 페이지의10nm 재확인은 기존 판독 한계를 소급 삭제하지 않는다. BLR의 거리→중력 약화를 본문 직접 진술로 승격하지 않는다. 원궤도들 간 비교와 한 궤도 내 보존의 범위 유지.',
  'next_counterexample':'장치의 다른 조절 변수가 허용되면 영상 확대만으로 전류를 유일 역추정할 수 없다. 고정 길이 경로의 전구간 감속은 작은 타원 진입과 다른 모형이다.',
  'educational_use':'관측값·본문 관계·배경 전제·사후 복원을 구분해 근거 표를 작성한다. 신규 수치 문항에는 고정 변수와 변환식이 필요하다.'}
]
existing={r['development_id'] for r in rows(OUT/'pattern_development.jsonl')}
assert not any(d['development_id'] in existing for d in devs)
append('pattern_development.jsonl',devs)
bs=sum(len(r['scenes']) for r in batch);ss=sum(len(r['scenes']) for r in sample)
append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT019','batch':19,'date':'2026-10-15','sample_case_ids':cases,'sample_questions':len(sample),'sample_scenes':ss,'sample_options':len(sample)*5,
 'method':'주 에이전트 직접 감사. 표본16문항 전체 지문·발문·5선지·현행 중간 추론·적용 경계·교육/출제 조건 대조. BKJ/BKP/BKR/BLH/BLW/BLZ/BML 보기 전체 직접 재독. BKE 현행 두 영상과 공식2019p5, BLR 궤도 그림, BLW 공식[B] 괄호 직접 확인. 기계적 인용·출처 검사는19배치40문항만.',
 'dimensions':{'중간추론':'원칙/예외, 단일 반례, 부분/전체 동일성, 대안 집합, 결합요건 대우, 분석/처방의 연결 검사.','전체선지':'표본80선지와 조합 보기 하위 명제 직접 검토.','원문이력':'BKE10nm는 공식페이지에서 재확인; BLR식·BML발문은 기존 복원 승계. 원자료 불변.','후보경계':'DEV070~074에 상위 공통점과 서로 다른 연산을 함께 명시. 신규 후보 등록 없음.','활용':'필수 정보·정오 전환 조건·추가 가정·유일답 한계를 대조.'},
 'findings':[{'cases':['BKJ','BLU','BLW'],'issue':'공식답 유지와 별개인 추론 충분성의 공백','resolution':'기존 세 유보 유지. 근거가 없는 반대 명제의 확정 금지.'},{'cases':['BKE','BLR'],'issue':'시각 판독/배경 전제의 출처','resolution':'BKE 공식페이지10nm 직접 재확인. BLR 원문 수식과 배경지식 사용을 분리 보존.'},{'cases':['BKP','BKR','BLC','BMH'],'issue':'결론에 필요한 증거의 범위','resolution':'단일 반례의 충분성과 부분의 동일성 반모형을 별도 연산으로 유지.'},{'cases':['BLH','BMG','BMJ','BML'],'issue':'관계 주체와 진술 지위','resolution':'추측/실제 의도, 응보 논항, 복합 술어 귀속, 설명/처방 구별 확인.'}],
 'decision':f'19배치40문항{bs}장면 저장, 표본16문항{ss}장면80선지 감사 및DEV070~074 귀납 완료. 누적760문항1188장면,유보44. 진행 차단 오류0.761부터 계속.',
 'unresolved_blocking_error_count':0,'limitations':'표본 외 의미 무오류 또는 공식답 전수 독립검증을 보증하지 않는다. 기존 유보는 해소 선언하지 않음. 다른 모델 호출·Git push·보호원장 전수 해시 없음.'}])
finish('audit_019.py',[next(c for c in r['case_ids'] if not c.startswith('BASIC-')) for r in batch],['19배치 표본16문항 감사·DEV070~074 귀납. 기존유보44 유지. 신규후보·의미 amendment 없음.761부터20배치 계속.'])
write('batch_019_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
write('batch_019_validation.json',json.loads((OUT/'audit_019_validation.json').read_text()))
print(f'19배치{len(batch)}문항{bs}장면; 표본{len(sample)}문항{ss}장면80선지 감사 완료.')
