import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write
from resume_support_20261016 import finish
assert not any(r['audit_id']=='QBF01-AUDIT023' for r in rows(OUT/'semantic_sample_audits.jsonl'))
c=json.loads((OUT/'checkpoint.json').read_text())
assert c['reviewed_questions']==920 and c['new_scene_count']==1420
allrows=rows(OUT/'current_question_reviews.jsonl')
batch=[r for r in allrows if r['batch_number']==23]
assert len(batch)==40 and sum(len(r['scenes']) for r in batch)==44
cases=['AMG','AMT','AOU','AOW','AOX','AOY','APB','APL','APQ','APU','APV','APX','APZ','AQA','AQE','AQI']
sample=[r for r in batch if set(r['case_ids'])&set(cases)]
assert len(sample)==16 and sum(len(r['scenes']) for r in sample)==18
byid={s['event_id']:s for r in allrows for s in r['scenes']}
apx=next(r for r in allrows if r['unique_question']=='U0239-Q03')
old=apx['option_checks'][0]['reasoning']
assert '경우에야' in old
new='① ㄱ은 실재론의 옹호 방향이다. ㄴ의 실패 이론이 많다는 사실만으로는,이 글이 성공한 이론의 설명력에 근거해 제시한 참됨·실재 믿음의 연결을 직접 반박하지 못한다. 비판이 가능할 모든 조건을 단 하나로 한정하지 않는다.'
assert not any(r['amendment_id']=='QBF01-QAMD008' for r in rows(OUT/'question_amendments.jsonl'))
graph=json.loads((OUT/'APB_official_graph_review_20261016.json').read_text())
edges={tuple(e) for e in graph['observed_edges']}
assert ('B','신경근증') in edges and ('B','D') not in edges
assert {a for a,b in edges if b=='D'}=={'분절 불안정성','C'}
assert graph['node_solution']=={'A':'추간판 변성','B':'추간판 탈출','C':'골극 성장','D':'추간공 협착'}
for r in allrows:
 if set(r['case_ids'])&{'AOU','APB','APZ'}: assert sum(x['unique_question']==r['unique_question'] for x in allrows)==1
devs=[
 {'development_id':'QBF01-DEV090','pattern_ids':['강도보존','설명수준','누락연결전제'],
  'evidence_event_ids':['QBF01-U0206-Q02-S02','QBF01-U0207-Q01-S01','QBF01-U0238-Q03-S01','QBF01-U0239-Q01-S01','QBF01-U0239-Q03-S01','QBF01-U0242-Q01-S01'],
  'finding':'AMG는설명가정없이는이해하기어렵다는말을발생불가능증명과구별한다. AMI/APV/APX는대안옹호·믿을이유·약화를완전증명이나논리모순과구별한다. APU는규범이불이익가능성만요구하며AQE의지정모형은필연도출을요구한다.',
  'decision':'모든과제에같은강도를부여하지않는다.발문·모형이요구한가능/필연/합리적근거를각각보존한다. AMG⑤의새충분성유보와②의범위제한을유지.공식답불변. APX의경우에야라는불필요한배타적서술은QAMD008로완화.',
  'next_counterexample':'동등설명력이있어도이론들이자동모순인것은아니다.설명이어렵다는것은그현상이불가능하다는말이아니다.규범이가능성만으로발동하면항상불이익이라는더강한전제가필요없다.',
  'educational_use':'답의강도를맞추기전에과제가요구하는추론양태를확인한다.선지를쉽게반박하려고강도를올리는오류를금지한다.'},
 {'development_id':'QBF01-DEV091','pattern_ids':['비교변인','기준내부검사','근거망복원'],
  'evidence_event_ids':['QBF01-U0230-Q01-S01','QBF01-U0230-Q03-S01','QBF01-U0232-Q02-S01'],
  'finding':'AOU는공통질문지와실제조작변인을나누고,AOW는같은설계의관측표와제임스이론의예측표를나눈다.APB는분기·합류·직접경로를보존해야시작원인과매개단계를맞출수있다.',
  'decision':'실험에등장한절차는그효과가분리측정됐다는뜻이아니며관측값을경쟁이론예측으로복사하지않는다.APB공식도판의B→신경근증직접선을이번사후확인했음을출처와함께보존.세과제의연결표상이비슷해도실험설계·가설예측·인과망배치는다른행동이다.',
  'next_counterexample':'질문지내용만바꾼집단이추가되면AOU④를검토할수있다.A/B각성조건이다르면AOW동일예측근거는사라진다.APB의직접선을없애면A/B구별단서가약해진다.',
  'educational_use':'조작표·관측표·이론예측표·인과도를구별하여작성한다.효과가없음과효과를분리검증하지않음을혼동하지않는다.'},
 {'development_id':'QBF01-DEV092','pattern_ids':['분류기준','비교축','기능유추'],
  'evidence_event_ids':['QBF01-U0209-Q01-S01','QBF01-U0210-Q01-S01','QBF01-U0231-Q01-S01','QBF01-U0231-Q02-S01','QBF01-U0240-Q02-S01','QBF01-U0240-Q02-S02','QBF01-U0240-Q03-S01'],
  'finding':'AMO는기능분리와해부학적국재화를나누고AMR은망의대상과이동행위를맞춘다.AOX는유추방향과역응용을구별한다.AOY는통상운동의공간배치조건을검사하며APZ/AQA는관계의존재·강도·구체효과·대체정보기능을구별한다.',
  'decision':'역할의유사성을수치단위동일성·전체정의동일성으로확대하지않는다.AOY의공간배치대표코드미확정을유지하고원운동전면금지규칙을만들지않는다.APZ의사회적보증은연결망효과의한형태,AQA대체는정보기능범위이다.',
  'next_counterexample':'편지받는사람을클릭에대응하면대상과행동이엇갈린다.약한연결은없음이아니고정보효과가항상약한것도아니다.전체몸을고리안에넣는놀이는통상의허리훌라후프와다른활동이다.',
  'educational_use':'대상·관계·행위·기능·수치단위와공간의자유도를분리하여사례의조건을설계한다.기존100코드번호때문에독립행동차이를억지로만들지않는다.'},
 {'development_id':'QBF01-DEV093','pattern_ids':['강도보존','기준내부검사','정보신뢰'],
  'evidence_event_ids':['QBF01-U0211-Q01-S01','QBF01-U0235-Q04-S01','QBF01-U0237-Q02-S01','QBF01-U0241-Q01-S01','QBF01-U0241-Q02-S01','QBF01-U0243-Q03-S01'],
  'finding':'AMT③의만,APQㄷ의항상,APL②의필연법칙은원선지의직접표현이아니다. AQB는실제로성립하는반례라도핵심비판이아닐수있음을명시하고AQC는가장의전체구성을특정가식표정의필수성으로좁히지않는다. AQI는해석적반례와명시반례의근거강도가다르다.',
  'decision':'정답을유지하기위해선지에없는한정어를추가하지않는정밀화를확인했다.AQI기존독립판정의보조반례확신0.78을현행유보로승계.명시성·문맥적부합·가장중요함·가장가까움을한검사로합치지않는다.',
  'next_counterexample':'AQB에서큰문제아님이핵심문제로바뀌면③의순위가달라진다.AQI의사랑그림을긍정이라고직접평가하는문장이추가되면반례의증거강도는높아질수있다.최선요약과전칭반증의과제는같지않다.',
  'educational_use':'발문이최적답을묻는지진위·필수성을묻는지먼저표시한다.원문에없는항상·오직·반드시를보충한뒤반박하는풀이를교정한다.'},
 {'development_id':'QBF01-DEV094','pattern_ids':['관계귀속','논거결론위계','반박표적'],
  'evidence_event_ids':['QBF01-U0232-Q02-S01','QBF01-U0235-Q01-S01','QBF01-U0238-Q02-S01','QBF01-U0239-Q01-S01','QBF01-U0240-Q02-S01','QBF01-U0243-Q02-S01','QBF01-U0244-Q01-S01'],
  'finding':'API는정통의담당자교체와중심기준해체,APT는권리해석과뇌사기준,APV는관점의내용과옹호이유,AQH는꿈그림의출전과욕망의근원,AQK는역할준비와평소동경을나눈다. APB공식그림확인과APZ태그기각이력은각각다른출처층위이다.',
  'decision':'같은명사주변에있다는이유로논항·목적·평가기준을옮기지않는다.AOU/APB/APZ중복ID는고유문항1회로확인.APZ조건문태그의과거기각을현재사이트오류·작성의도확정으로강화하지않고과거독립검토를보존한다.',
  'next_counterexample':'판결이바뀌었다고의학기준도바뀐것은아니다.기자역을연구했다고기자직을동경한것은아니다.두문헌안의단어가비슷해도자료기능·사실·평가의대상은따로확인해야한다.',
  'educational_use':'판단기록에무엇을언제어떤출처로직접확인했는지붙인다.공식이미지의사후확인을최초blind에소급하지않고태그는제3자색인이라는지위를유지한다.'}
]
existing={r['development_id'] for r in rows(OUT/'pattern_development.jsonl')}
assert not any(d['development_id'] in existing for d in devs)
assert all(e in byid for d in devs for e in d['evidence_event_ids'])
append('question_amendments.jsonl',[{'amendment_id':'QBF01-QAMD008','unique_question':'U0239-Q03','reason':'23배치직접감사:ㄴ이직접반례가되는경우를모든실패이론도참이라고주장한경우에야로배타한정한문구가불필요하게강했다.이글의실제논거와직접충돌하지않는다는국소판정으로정밀화.공식⑤·장면·인용근거불변.','changes':[{'field_path':'option_checks.0.reasoning','old_value':old,'new_value':new}]}])
write('audit_023_selected_checks.json',{
 'scope':'작성시직접읽은전체원문·표·그림과현행기록의사후감사.실제과학·법률이론의외부전수검증아님.',
 'AMG':'설명가정의필요와현상발생필수조건을구별.⑤가설의존유보유지.②도본문피진환경어린이로한정.',
 'AMT_APL_APQ':'원선지에없는만·필연·항상표현을직접인용또는강화한조건으로추가하지않는지확인.최선요약·문맥적전제·부적절성의과제를구별.',
 'AOU_AOW':'약물/정보/협력자태도와공통질문지절차를분리.질문지효과분리검증없음≠효과0.무주사대조까지수행한것으로확장금지.실제B/C무반응과제임스의A/B동일예측구별.',
 'AOX_AOY':'유추에역응용이불필요하다는것은역응용불가능이아님.G270그림2개직접재확인.통상훌라후프의공간배치만판정하고모든원운동금지안함.대표번호미확정보존.',
 'APB':{'source':'APB_official_graph_review_20261016.json','direct_edge_verified':['B','신경근증'],'not_edge':['B','D'],'merge_inputs_to_D':['분절 불안정성','C'],'finding':'공식7쪽의노드명·모든화살표·선지표이번직접확인.최초blind문자도식/글자없는PNG의출처한계는불변.'},
 'APU_APV_APX':'불이익가능성이면규범발동.실재론내용과믿을이유구별.동등설명력≠모순·모든이론거짓. QAMD008로불필요한경우에야한정완화.',
 'APZ_AQA':'사람/관계/행동/효과·약함/없음·정보기능대체/전체관계대체·사용량/승인태도구별.별도태그기각이력보존.',
 'AQE':'법칙·초기조건·필연성이라는지정모형의요건검사.과학소재만으로형식적합성보장금지.모형자체비판과사례부합을분리.',
 'AQI':'비로소의필수성근거부족과사랑그림긍정성의해석적반례를분리.기존보조확신0.78승계.공식⑤유지.',
 'new_amendments':['QBF01-QAMD008'],'holds_preserved':['AMG','AQI'],'pass':True})
append('pattern_development.jsonl',devs)
append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT023','batch':23,'date':'2026-10-16','sample_case_ids':cases,'sample_questions':16,'sample_scenes':18,'sample_options':80,
 'method':'주에이전트직접감사.이번세션에서표본16문항의전체원문·발문·선지·기존풀이를읽어작성한뒤현행80선지와18장면의추론·경계·최소수정·후보연결을재대조. APB공식전체페이지·G270몸그림·G269표전사는이번직접확인증거사용.기계적인용·출처검사는23배치40문항만.',
 'dimensions':{'중간추론':'설명/발생필수성·관측/예측·직접/매개경로·약함/부재·역할/동기·문구강도검사.','전체선지':'표본80선지및해당조합보기의하위명제까지직접검토.','원문이력':'APB도판사후확인과최초제한보존. AOU/APB/APZ별도판정·중복ID1회계수확인.','후보경계':'AOY대표번호미확정·APZ태그기각이력유지. QAMD008국소정밀화. DEV090~094귀납.','활용':'명시반례/해석적보조·최적답/필연검사를나누어신규문항의추가전제위험을기록.'},
 'findings':[{'cases':['AMG'],'issue':'설명곤란과발생불가능의강도차이','resolution':'새충분성유보유지.선천성가설을조건으로판독.'},{'cases':['AQI'],'issue':'해석적반례의명시성부족','resolution':'기존0.78보조확신제한을현행유보승계.누적유보55.'},{'cases':['APX'],'issue':'비판가능조건에불필요한배타한정','resolution':'QAMD008로이글의국소논거검사로완화.'},{'cases':['APB'],'issue':'최초도판의노드표기출처한계','resolution':'이번공식페이지에서직접노드·화살표확인.최초blind에소급하지않음.'}],
 'decision':'23배치MEET40문항44장면,표본16문항18장면80선지감사·DEV090~094완료.누적920문항1420장면·유보55.정답변경없음.미완료157문항.921부터계속.',
 'unresolved_blocking_error_count':0,'limitations':'표본밖의미무오류·공식정답전수독립검증보증없음.직접읽은자료의과학·법·철학서술을현행외부사실로검증한것아님.다른모델호출·Gitpush·보호원장전수해시없음.'}])
finish('audit_023.py',[next(c for c in r['case_ids'] if not c.startswith('BASIC-')) for r in batch],['23배치표본16문항18장면80선지감사·DEV090~094귀납. QAMD008 APX불필요배타한정정밀화, AMG새유보·AQI기존해석적반례한계승계, APB공식도판사후확인.누적920문항1420장면·유보55.921부터계속.'])
write('batch_023_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
write('batch_023_validation.json',json.loads((OUT/'audit_023_validation.json').read_text()))
h=json.loads((OUT/'session_handoff_20261016_01.json').read_text())
h.update(execution='주에이전트직접의미판단·감사.다른모델호출·Gitpush없음.실제quota관측은quota_observation_20261016.json참조.5시간미확인·마지막관측주간잔여62%.runtime emergency관측없음.',quota_observation_file='quota_observation_20261016.json',new_visual_reviews=['BRW_B_range_review_20261016.json','APB_official_graph_review_20261016.json'],current_session_amendments=['QBF01-AMD049','QBF01-AMD050','QBF01-QAMD007','QBF01-QAMD008'],current_session_scope_refinements=['BTI의어렵다/유일필수조건구별','AMT③에만추가금지','APL②에필연법칙직접명시했다고강화금지','APQㄷ에항상직접명시했다고기록금지'],current_session_new_or_carried_holds=['BPS','BPU','BQR','BQW','BRF','BSM','ALY','AMG','AQI'])
write('session_handoff_20261016_01.json',h)
print('23배치감사완료.다음921.')
