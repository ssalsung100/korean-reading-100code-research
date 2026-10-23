import sys,json
from fractions import Fraction
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write
from resume_support_20261016 import finish
assert not any(r['audit_id']=='QBF01-AUDIT021' for r in rows(OUT/'semantic_sample_audits.jsonl'))
c=json.loads((OUT/'checkpoint.json').read_text())
assert c['reviewed_questions']==840 and c['new_scene_count']==1323
batch=[r for r in rows(OUT/'current_question_reviews.jsonl') if r['batch_number']==21]
assert len(batch)==40 and sum(len(r['scenes']) for r in batch)==68
cases=['BOY','BPJ','BPL','BPS','BPU','BPV','BPY','BQA','BQE','BQR','BQV','BQW','BRA','BRC','BRF','BRQ']
sample=[r for r in batch if set(r['case_ids'])&set(cases)]
assert len(sample)==16 and sum(len(r['scenes']) for r in sample)==29
allrows=rows(OUT/'current_question_reviews.jsonl')
byid={s['event_id']:s for r in allrows for s in r['scenes']}
sc=byid['QBF01-U0472-Q03-S01'];old=sc['pattern_connections']
new=[p for p in old if p['pattern_id']!='필요요건역전금지']
assert len(old)==3 and len(new)==2
assert not any(r['amendment_id']=='QBF01-AMD050' for r in rows(OUT/'scene_amendments.jsonl'))
# 아래 수치는 원문 관측값이 아닌 주 에이전트의 반모형 검산이다.
assert any([True,False]) and not all([True,False])
assert any([True,True]) and all([True,True])
x=[1,2,3];y=[9,5,4]
assert all(x[i]<x[i+1] and y[i]>y[i+1] for i in range(2))
assert len(set(a*b for a,b in zip(x,y)))==3
rho=Fraction(1+2,1)/Fraction(18,10)
assert rho!=Fraction(1+2,2)
f=lambda z:z//10
g=lambda z:z>=1
assert g(f(1))==g(f(2)) and g(f(2))!=g(f(12))
devs=[
 {'development_id':'QBF01-DEV080','pattern_ids':['강도보존','문맥조작화','누락연결전제'],
  'evidence_event_ids':['QBF01-U0463-Q02-S02','QBF01-U0464-Q01-S02','QBF01-U0471-Q02-S02','QBF01-U0473-Q01-S02','QBF01-U0476-Q02-S02'],
  'finding':'BPS의능력 존재 정의와 칸트 원칙 수용,BPU의질적 역방향 경향과 정확 역비례식,BQR의제도 통제와 영구 근절 불가능,BQW의억압 관행 비판과 지배계급 수혜 구체화,BRF의감상 유도와 실제 반응 순위는 추가 연결 없이 같아지지 않는다.',
  'decision':'5개 원판정의scope_limit을현행유보로승계했다. 이는공식정답을바꾸거나원문오류를확정한것이아니다. 문맥 수용과 논리적 필연·외부 실증을 분리한다. 유보46→51의 원인과 사례를 명시하며 신규 후보 없음.',
  'next_counterexample':'존재V와규범원칙거부의가상입장, x증가/y감소지만xy불변아닌수열,현재통제하지만미래제거가능한모형,특정계급귀속미확정인억압관행,공감과성찰의동시성은서로다른연결공백을드러낸다. 실제역사·관객통계의새확인아님.',
  'educational_use':'공식답 수용의 근거 옆에 문맥상 좁힘과 추가 전제를 별도로 적는다. 새 문항은 그 조건을 직접 제공하거나 결론 강도를 낮춘다.'},
 {'development_id':'QBF01-DEV081','pattern_ids':['단계구분','관계전이','기준내부검사','비율기준'],
  'evidence_event_ids':['QBF01-U0460-Q02-S01','QBF01-U0460-Q02-S02','QBF01-U0464-Q02-S01','QBF01-U0467-Q02-S01','QBF01-U0467-Q02-S02','QBF01-U0467-Q02-S03'],
  'finding':'BPJ는규칙수와동시적중수를구별하고간접경로존재를모든입력변화의출력변화로강화하지않는다. BPV는제도를우회하는경로가도구변수요건을깨는지검사한다. BQE는원용매부피/혼합전합/혼합후부피를분리하고비가산분모와단위를확인한다.',
  'decision':'경로의 존재·출력의 변화·식별 조건·비교 기준·차원 일치는 각각 다른 질문이다. BQE차원역산은현장면으로보존하고기존후보에억지연결하거나한사례로새후보를확정하지않는다.',
  'next_counterexample':'x→floor(x/10)→판정 경로는1과2입력에같은결과를낼수있다. 기술효과가모두제도에매개되면BPV의제도밖경로논거는달라진다.ρ1=1,ρ2=2,초기각부피1,최종1.8이면혼합밀도5/3으로산술평균1.5가아니다.모두가상검산.',
  'educational_use':'노드별 입력·출력과 고정 조건을 명시한다. 물리량 비교는 먼저 분모와 비교 기준을 적고 단위 일치를 확인한다.'},
 {'development_id':'QBF01-DEV082','pattern_ids':['관계귀속','반박표적','공격대상변형','정보경로복원'],
  'evidence_event_ids':['QBF01-U0456-Q02-S01','QBF01-U0456-Q02-S02','QBF01-U0465-Q02-S01','QBF01-U0465-Q02-S02','QBF01-U0473-Q01-S01','QBF01-U0475-Q02-S01'],
  'finding':'BOY는저술자/등장인물의동기와차별적증거평가를나누고,BPY는나중공개된동기로앞행동을설명하되고백사건을앞사건의원인으로만들지않는다. BQW는비판발신자/수신자교환,BRC는실제부족한것을과잉편중이라고공격하는표적변형이다.',
  'decision':'모든오귀속을공격대상변형으로합치지않는다. BRC는왜곡한표적을근거로비판하는추가구조가있어해당후보와연결한다. BPY의복선을기존56과전역동의어로만들지않고공개순서·설명기능을보존한다.',
  'next_counterexample':'저자기록이한해석만직접뒷받침하면BOY의비대칭평가를재검토할수있다. C가B의같은사건을다시서술하면BPY④관계가달라진다. 이름만틀린문장은자동으로허수아비논증이아니다.',
  'educational_use':'누가 누구의 무엇을 어떤 근거로 말하거나 비판하는지 복원한다. 사건 시점과 정보 공개 시점을 따로 표시한다.'},
 {'development_id':'QBF01-DEV083','pattern_ids':['비교축','규범현실','속성분리','수단목적층위'],
  'evidence_event_ids':['QBF01-U0461-Q01-S02','QBF01-U0471-Q02-S01','QBF01-U0474-Q02-S01','QBF01-U0474-Q02-S02','QBF01-U0476-Q02-S01','QBF01-U0481-Q03-S01','QBF01-U0481-Q03-S02'],
  'finding':'BPL의내재적/도구적가치,BQR의전체국가/한파벌규모,BRA의사건유형·국가·제안/시행사실,BRF의가족소재/가족평가,BRQ의협상력/노동시간과내부혜택/외부포용은서로다른축이다.',
  'decision':'공통단어·공통행동·일부성과로다른축의동일성을추정하지않는다. 특히장시간노동미해결을감소전무로확정하지않고,이익을위해제도를중시함을내재적가치부여와구별한다. 기존판정번호의국소중첩은허용하되장면중복계수는하지않는다.',
  'next_counterexample':'양쪽모두가족을다루더라도하나는규범에타협하고다른하나는억압을드러낼수있다. 노동시간이일부줄어도장시간문제는남을수있다. 같은판결파기라도이익충돌의사례와불성실변호의제안은다르다.',
  'educational_use':'주어·지표·대상범위·시점·진술지위를 채운 비교표를 사용한다. 개선과 해결,기회와 보장,현재 사실과 제안을 구분한다.'},
 {'development_id':'QBF01-DEV084','pattern_ids':['범위이동','강도보존','포함반례'],
  'evidence_event_ids':['QBF01-U0463-Q02-S01','QBF01-U0466-Q01-S01','QBF01-U0472-Q03-S01'],
  'finding':'BPS는존재명제를전칭으로강화한오류,BQA는책임→대안가능성의필요조건주장에책임있음/대안없음사례를대입하는반증,BQV는일부실현사례의공통속성을모든실현의필수조건으로만드는과잉이다.',
  'decision':'필요조건이라는말이공통되어도주어진필요조건을역전하는작업과필요조건자체를무근거로추가하는작업은다르다. BQV의필요요건역전금지연결을AMD050으로제거하고관계귀속·강도보존은유지한다. 원독립코드10을덮어쓰지않으며장면·정답불변.',
  'next_counterexample':'V인것과아닌것이하나씩있으면존재V는참·모든V는거짓이다. 모두V도존재V와양립하므로일부만을강제할수없다. BQA의한반례는모든대안부재상황의책임을입증하지않는다.',
  'educational_use':'필요조건을이미주었는지,그조건을새로부여했는지,조건에대한반례를제시했는지부터구별한다. 번호보다 실제 연산과 반모형을 기준으로 삼는다.'}
]
existing={r['development_id'] for r in rows(OUT/'pattern_development.jsonl')}
assert not any(d['development_id'] in existing for d in devs)
assert all(e in byid for d in devs for e in d['evidence_event_ids'])
append('scene_amendments.jsonl',[{'amendment_id':'QBF01-AMD050','event_id':sc['event_id'],'reason':'21배치 직접 감사: BQV는 일부 실현 사례에서 보편적 필요조건을 새로 부과한 오류이며 이미 주어진 필요조건의 역방향을 검사하는 필요요건역전금지의 정의와 다르다. 해당 연결만 철회하고 귀속·강도 판단과 원독립코드는 보존.','changes':[{'field_path':'pattern_connections','old_value':old,'new_value':new}]}])
write('audit_021_selected_checks.json',{
 'scope':'이번 세션 작성 후 직접 의미 감사. 가상 반모형 검산은 실제 관측자료가 아님.',
 'BPS':{'countermodels':{'some_not_all':[True,False],'all_also_some':[True,True]},'finding':'존재→전칭 강화와 존재→일부만 강화 모두 금지.①의 규범 전제 독립성 유보 유지.'},
 'BPU':{'hypothetical_x':x,'hypothetical_y':y,'products':[a*b for a,b in zip(x,y)],'finding':'반대 방향 경향은 곱 일정의 역비례를 보장하지 않음. 상관만으로 인과 존재/부재 확정 금지. 기존 한국어 정정 이력 보존.'},
 'BPJ':{'hypothetical_path':'x→floor(x/10)→중간값≥1','inputs':[1,2,12],'outputs':[g(f(z)) for z in [1,2,12]],'finding':'간접 경로가 있어도 모든 입력 변화가 최종출력을 바꾸는 것은 아님. 규칙수와 동시적중수 구별.'},
 'BQE':{'hypothetical_density':str(rho),'arithmetic_mean':'3/2','finding':'질량합과 비가산 분모를 분리. 원용매·혼합전합·혼합후값의 비교 기준 보존. 에너지/온도 차원 확인.'},
 'BOY_BPL':'해석의 근거 차이 미확인은 실제 확률 동등성 아님. 내재적/도구적 가치 차이 유지. BPL두ID고유문항1회·주4/39와주88이력보존.',
 'BPV':'제도 밖 기술 경로와 제도를 통해 작용하는 기술 경로를 구별. 기술 이전 실제 부재의 역사 판단 아님.',
 'BPY':{'direct_visual':'자료/LEET_언어이해/페이지/2026/2026_question_odd/page_010.png','finding':'이번 작성 때 공식 전체페이지에서A/B/C괄호 확인. A첫대사부터,B좌하→우상,C편지전체. 사전 오인·정정 이력 보존. 후행 해명/선행 원인 및 같은 사건 재서술을 분리.'},
 'BQA_BQV':'BQA는필요조건반례이며역전칭금지.BQV는무근거필수조건추가라AMD050연결철회.정답·장면·원독립판정불변.',
 'BQR_BQW_BRF':'BQR⑤본성의근절불가능,BQW①지배계급수혜구체화,BRF②실제관객엄격순위의공백을유보. 공식답변경이나 반대명제확정 없음.',
 'BRA_BRC':'제안/시행사실과변호유형을분리. BRC는실제로변형된표적을편중이라고공격하므로공격대상변형 연결을 유지.',
 'BRQ':'비용·자본·경험·시간을따로검사.노동문제미해결에서감소전무금지.내부협력이외부포용을보장하지않음.',
 'new_amendments':['QBF01-AMD050'],'holds_preserved':['BPS','BPU','BQR','BQW','BRF'],'pass':True})
append('pattern_development.jsonl',devs)
append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT021','batch':21,'date':'2026-10-16','sample_case_ids':cases,'sample_questions':16,'sample_scenes':29,'sample_options':80,
 'method':'주 에이전트 직접 감사. 이번 세션에서 표본16문항 전체 원문·발문·5선지·기존 풀이를 직접 읽어 작성한 뒤 현행80선지와29장면의 추론·적용 경계·후보 연결·교육/출제 조건을 재대조. BPY공식 페이지 및 BQR/BQV/BQW/BRC인라인 그림은 이번 작성 때 직접 확인한 증거를 사용. 기계적 인용·출처 검사는21배치40문항에 한정.',
 'dimensions':{'중간추론':'존재/전칭,필요조건반례/무근거필수조건,경로/실제변화,비가산분모,지표·주체·진술지위 검사.','전체선지':'표본80선지의 직접 근거·문맥 수용·추가 가정 구별.','원문이력':'BPY범위재확인,인라인주체·비판·비극적황홀확인. BPL/BPS별도판정과중복ID유지. G506/G507노출이력승계.','후보경계':'AMD050 BQV필요요건역전금지연결철회. 정의 없는 단위역산은 빈 후보로 보존. DEV080~084 귀납.','활용':'가상 반모형과 실제 기출 관측을 분리.필요조건·비교기준·유보를 출제 전제에 반영.'},
 'findings':[{'cases':['BPS','BPU','BQR','BQW','BRF'],'issue':'기존 scope_limit의 현행 유보 승계','resolution':'5문항을유보목록에명시.공식정답불변·해석제한보존.누적51.'},{'cases':['BQV'],'issue':'필수조건 추가와 필요조건 역전의 차이','resolution':'AMD050으로해당패턴연결만철회.'},{'cases':['BPJ','BPV','BQE'],'issue':'모형 경로와 성과·비교·차원의 충분성','resolution':'가상값 검산과 일반식·경로의 조건을 함께 확인.'},{'cases':['BOY','BPY','BRA','BRC','BRQ'],'issue':'근거 지위·발화·판단 층위 혼동 위험','resolution':'비교 기준과 문맥의 실제 귀속을 유지.'}],
 'decision':'21배치40문항68장면,표본16문항29장면80선지 감사 및DEV080~084 저장. 누적840문항1323장면·유보51. 신규후보없음,AMD050연결1건철회.841부터계속.',
 'unresolved_blocking_error_count':0,'limitations':'표본 외 의미 무오류·공식 정답 전수 독립검증 보증 없음. 기존 유보 해소 선언 없음. 다른 모델 호출·Git push·보호 원장 전수 해시 없음.'}])
finish('audit_021.py',[next(c for c in r['case_ids'] if not c.startswith('BASIC-')) for r in batch],['21배치 표본16문항29장면80선지 감사·DEV080~084 귀납. BPS/BPU/BQR/BQW/BRF 유보 승계 확인. AMD050 BQV 필요요건역전금지 연결 철회. 841부터 계속.'])
write('batch_021_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
write('batch_021_validation.json',json.loads((OUT/'audit_021_validation.json').read_text()))
print('21배치 감사 완료. 다음841')
