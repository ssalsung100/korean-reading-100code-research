import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write,candidate
from resume_support_20261016 import finish
assert not any(r['audit_id']=='QBF01-AUDIT025' for r in rows(OUT/'semantic_sample_audits.jsonl'))
c=json.loads((OUT/'checkpoint.json').read_text())
assert c['reviewed_questions']==1000 and c['new_scene_count']==1507
allrows=rows(OUT/'current_question_reviews.jsonl')
batch=[r for r in allrows if r['batch_number']==25]
assert len(batch)==40 and sum(len(r['scenes']) for r in batch)==42
cases=['ATC','ATD','ATJ','ATO','ATU','ATW','ATY','AUC','AUJ','AUK','AUN','AUZ','AVA','AVB','AVE','AVH','AVI','AVK']
sample=[r for r in batch if set(r['case_ids'])&set(cases)]
assert len(sample)==18 and sum(len(r['scenes']) for r in sample)==20
byid={s['event_id']:s for r in allrows for s in r['scenes']}
def events(cs):return [s['event_id'] for r in allrows if set(r['case_ids'])&set(cs) for s in r['scenes']]
changes=[]
for number,case,pid in [(51,'ATO','수단목적층위'),(52,'ATY','수단목적층위'),(53,'AVK','수단목적층위'),(54,'AVH','설명수준')]:
 r=next(r for r in batch if case in r['case_ids']);s=r['scenes'][0];old=s['pattern_connections'];assert any(x['pattern_id']==pid for x in old)
 new=[x for x in old if x['pattern_id']!=pid]
 if case=='AVH':new.append({'pattern_id':'BFP017','case_specific_fit':'표본채취의대표성을높이는조치와분말의물성차이를줄여실제분리를낮추는조치를구별한다.','definition_source':str(OUT.relative_to(OUT.parents[2])/'new_pattern_candidates.jsonl'),'definition_reused':True})
 changes.append({'amendment_id':f'QBF01-AMD{number:03}','event_id':s['event_id'],'reason':('25배치직접감사:수단목적층위의기존정의는중간조건/최종목표구별이다.이장면은일반수단목적대응또는서로다른목적구별로그특정연산이없으므로과잉연결만제거.정답·장면추론불변.' if case!='AVH' else '25배치직접감사:설명수준은사례·논거·원인의문장역할구별이다.측정정확성과대상실제개입의구별은동일연산이아니므로해당연결제거,BFP017단일잠정후보에연결.원raw·정답·장면추론불변.'),'changes':[{'field_path':'pattern_connections','old_value':old,'new_value':new}]})
existing_amd={r['amendment_id'] for r in rows(OUT/'scene_amendments.jsonl')}
assert not any(r['amendment_id'] in existing_amd for r in changes)
ave=next(r for r in batch if 'AVE' in r['case_ids'])
assert ave['selected_answer']==5
blind=next(s for s in ave['original_evidence_states'] if s['stage']=='blind')['payload']
answer=next(s for s in ave['original_evidence_states'] if s['stage']=='answer_check')['payload']
assert blind['selected_answer']==3 and blind['confidence']==0.91 and answer['official_answer']==5 and answer['match'] is False
assert sum('ATC' in r['case_ids'] for r in allrows)==1
candidate('BFP017','측정의 정확성 개선과 측정 대상의 실제 상태 개선을 구별','조치가관측표본·측정절차·정보갱신을바꾸는지,대상현상을일으키는변수를바꾸는지구별한다.더정확한진단이나대표성있는표본이곧대상상태의개선을뜻하지는않는다.',['측정대상과측정절차가분리되어제시되고,발문이어느쪽의개선을요구하는지확인할수있어야한다.','측정결과를이용한후속개입이나측정자체의물리효과가주어지면그경로를별도로검사한다.측정은언제나대상에무영향이라는전칭은금지.','현재AVH한문항에서직접확인한잠정후보.정밀측정과분체분리원인물성조절을구별한최초행동에근거.'],'설명수준은문장사이의사례·논거·원인역할구별,측정근사조건은대표값을구간에적용하는근사오차,조건부방향은원인변화의효과추적이다.여기서는조치의대상이관측절차인지실제현상인지먼저구별한다.다른후보와통합검토가능하며새대분류확정아님.')
devs=[
 {'development_id':'QBF01-DEV100','pattern_ids':['BFP011','BFP016'],'evidence_event_ids':['QBF01-U0163-Q01-S01','QBF01-U0267-Q03-S01'],
 'finding':'ATD는하위집단동일시율35%·12%가각각50%미만이므로전체도미만임을판정한다.기존AGV는변동하는시계열의평균을개별값하한으로읽을수없음을판정했다.둘다평균의내부성에관련된다.',
 'decision':'BFP016을한문항잠정후보로보존하되BFP011과같은평균경계원리의입력조건·추론방향이다른구현으로통합검토한다.번호차이만으로별개고급연산이나독립대분류를확정하지않는다.ATC/ATD과거소재노출도유지.',
 'next_counterexample':'ATD에서전체를덮지않는표본·중복집단·서로다른분자조건은결합근거를깨뜨린다.한집단이문턱위면집단크기에따라전체위치가달라진다.AGV는비상수조건이없으면평균과모든개별값이같을수있다.',
 'educational_use':'정확값계산과경계만필요한문제를구별한다.ATD의검산은(0.35×0.35+0.32×0.12)/0.67≈0.24015로과반비동일시를재확인할뿐필수아니다.'},
 {'development_id':'QBF01-DEV101','pattern_ids':['수단목적층위','설명수준','BFP017','비교축'],'evidence_event_ids':events(['ATO','ATY','AVH','AVK']),
 'finding':'ATO의대안수단,ATY의서로다른치료목적,AVK의유지조건/연결수단은중간조건과최종목표를구별하는기존수단목적층위의특정연산과다르다.AVH측정대표성/실제물성개입도설명수준의사례·논거·원인구별과다르다.',
 'decision':'AMD051~053으로수단목적층위세연결만제거.AMD054로AVH설명수준연결을BFP017단일후보로교체.원정답·원raw·추론·장면수불변.일반주제어가비슷하다고정의범위를늘리지않는다.',
 'next_counterexample':'수단이중간단계를실현하고그단계를최종목표로오인한경우라야수단목적층위의직접적용을재검토한다.측정뒤실제혼합제어가따라오면BFP017에서도측정조치와개입효과를추적해야한다.',
 'educational_use':'후보연결에는장면의주제어가아닌후보정의가요구하는실제연산을명시한다.적합한기존후보가없으면빈연결이나단일잠정후보를허용한다.'},
 {'development_id':'QBF01-DEV102','pattern_ids':['강도보존','표현기능판독','분류기준'],'evidence_event_ids':events(['ATU','AUN','AUZ','AVE']),
 'finding':'ATU①⑤는문맥수용과연역이달라지고,AUN⑤는보기전후와역사전칭이다르며,AUZ④는제시된수혜범위와실제공익가능성이다르다.AVE는상징적초월을물리적소멸로좁히면서후속불행에는미제시서사를허용한최초오답이다.',
 'decision':'네기존한계를현행유보승계하여누적67. AVE최초③확신0.91·공식⑤불일치·실패분석불변.공식정답으로③의모든조건초월을엄밀전칭증명했다고하지않음.',
 'next_counterexample':'정답일치만으로비정답선지의근거공백을메울수없다.미래추론이모두금지되는것이아니라불행이라는구체방향의근거가필요하다.특정집단수혜라는사실만으로항상사익이라고할수없다.',
 'educational_use':'공식답·최초성패·후속해석확신을따로보존하고사실층위/상징층위의적용을일관되게한다.'},
 {'development_id':'QBF01-DEV103','pattern_ids':['관계귀속','비교축','분류기준'],'evidence_event_ids':events(['ATC','ATW','AUC','AUJ','AUT','AUV','AVA','AVB','AVI']),
 'finding':'ATC입력단위/분류대상,ATW세포/산물/기능,AUC정의/외연,AUJ대명사지칭/인식사건,AUT인물인용/작가사상,AUV순환/발전,AVA부등식논항,AVB결과/원인,AVI표본수/채널수가각각교환되면오답이생긴다.',
 'decision':'공통상위행동은논항과비교축보존으로묶되각사례의구체대상과재분할조건을유지한다.숫자·상관·비유·비판이라는표면어만으로대표코드를결정하지않는다.',
 'next_counterexample':'서로다른단위라도표본크기의역할은대응할수있다.같은결과라도원인은다를수있고,한분야에서의주도관계가다른분야전체를규정하지않는다.필요부등식의방향을맞췄다고충분성이증명되지는않는다.',
 'educational_use':'주체·대상·범위·조건·기능을명시한뒤비교한다.선지한절이맞는것과연언전체가맞는것을구별한다.'},
 {'development_id':'QBF01-DEV104','pattern_ids':['강도보존','누락연결전제','공격대상변형','조건부방향','행위결과분리'],'evidence_event_ids':events(['ATJ','AUE','AUK','AVK']),
 'finding':'ATJ의세비판은적용범위·비용·인과식별을서로다르게제한하며ㄴ은실제기능을삭제한공격이다.AUE는검증요구와검증완료를나누고AUK는작은교정뒤의복귀동기를추적한다.AVK는유지할조건과바꿀조건을함께충족하는연결해결이다.',
 'decision':'비판의유효성을모든경우실패증명과같게보지않는다.교정·해결이라는행위명만으로최종효과를확정하지않는다.G326_visual01도판직접재확인은기존자료재확인으로기록.',
 'next_counterexample':'비용이이익보다크다면이라는조건은실제비용초과의보고가아니다.조금고쳤다는사실은이후행동에따라유지효과를낳을수있다.원통배치는그자체나쁜것이아니라한쪽제단을향하는현재목표와다르다.',
 'educational_use':'과제목표·조건·개입·중간행동·최종효과를나누어변형문항을설계한다.'}
]
existing={r['development_id'] for r in rows(OUT/'pattern_development.jsonl')}
assert not any(d['development_id'] in existing for d in devs)
assert all(e in byid for d in devs for e in d['evidence_event_ids'])
append('scene_amendments.jsonl',changes)
append('pattern_development.jsonl',devs)
write('audit_025_selected_checks.json',{'sample_case_ids':cases,'sample_questions':18,'sample_scenes':20,'sample_options':90,'scope':'주에이전트가이번작성에서직접읽은원문과현행기록의사후감사.외부현행사실검증아님.','new_candidates':['BFP016','BFP017'],'candidate_family_review':'BFP016/BFP011은평균내부성의다른방향구현으로통합검토;독립대분류확정아님.','amendments':[r['amendment_id'] for r in changes],'failure_preserved':{'case':'AVE','initial':3,'confidence':0.91,'official':5,'match':False},'holds_preserved':['ATU','AUN','AUZ','AVE'],'checks':{'ATD':'두하위집단각50%미만→전체미만.정확가중검산과필수판단분리.','ATJ':'범위·비용·교란비판과공격대상왜곡분리.','ATW_ATY':'세포별경로·촉진억제/억제억제·공통기전/목적대체구별.','AUC_AUE':'정의/외연·과학참/가치관련성·가능성/검증완료구별.','AUJ_AUK':'지시대상/인식사건·작은교정→복귀의국소경로.','AVA_AVB':'필요비교방향을동치로강화금지.공통결과를원인동일로확대금지.','AVE':'최초오답유지.상징의물리적환원과미제시후속불행을분리.','AVH_AVI':'측정개선/대상개선·표본수/채널수·역할대응/단위동일구별.','AVK':'기존펜덴티브도판직접재확인.사각본체와돔의동시요건.'},'pass':True})
append('semantic_sample_audits.jsonl',[{'audit_id':'QBF01-AUDIT025','batch':25,'date':'2026-10-16','sample_case_ids':cases,'sample_questions':18,'sample_scenes':20,'sample_options':90,'method':'주에이전트직접감사.작성시직접읽은원문·발문·선지·기존판정과현행18문항90선지20장면재대조.후보정의D/E에대조해AMD051~054적용.기계적인용·해시검사는25배치40문항.','dimensions':{'추론':'가중평균경계·비판의종류·관측/개입·귀속과비교축·상징/물리층위검사.','전체선지':'18문항90선지와조합보기하위명제검토.','이력':'ATC별도판정·중복1회,ATC/ATD사전노출,AVE최초오답0.91보존.','후보':'BFP016/BFP011통합검토·BFP017단일후보·AMD051~054과잉연결정밀화.','활용':'조건범위와변형시재판정조건을명시.기출의의학·법률내용을현행권고로확장하지않음.'},'findings':[{'cases':['ATO','ATY','AVK','AVH'],'issue':'기존후보의특정정의보다넓은주제어연결','resolution':'AMD051~054로정밀화.정답·원추론·장면수불변.'},{'cases':['ATD'],'issue':'가중비율문턱판정과기존평균후보의관계','resolution':'BFP016단일후보, BFP011과상위원리통합검토.'},{'cases':['ATU','AUN','AUZ','AVE'],'issue':'기존해석한계및최초성패보존','resolution':'네유보승계로누적67.AVE최초③/공식⑤불일치불변.'}],'decision':'25배치40문항42장면·표본18문항20장면90선지감사·DEV100~104완료.누적1000문항1507장면·유보67.잔여77문항을1001부터계속.','unresolved_blocking_error_count':0,'limitations':'표본밖의미무오류보증없음.기존AGV는BFP011정의와기저장장면의대조로이번새원문재분석이아님.보호원장전수해시·Gitpush·다른모델호출없음.'}])
finish('audit_025.py',[next(c for c in r['case_ids'] if not c.startswith('BASIC-')) for r in batch],['25배치표본18문항20장면90선지감사·DEV100~104완료.AMD051~054과잉연결수정,BFP016/BFP011통합검토,BFP017단일후보.누적1000/1507·유보67.1001부터계속.'])
write('batch_025_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
write('batch_025_validation.json',json.loads((OUT/'audit_025_validation.json').read_text()))
h=json.loads((OUT/'session_handoff_20261016_01.json').read_text())
h['current_session_new_candidates']=['BFP016:ATD하위집단공통문턱→전체문턱.단일후보,BFP011평균내부성과통합검토.','BFP017:AVH측정정확성개선/대상상태개선구별.단일후보.']
h['current_session_amendments']=['QBF01-AMD049','QBF01-AMD050','QBF01-QAMD007','QBF01-QAMD008','QBF01-AMD051','QBF01-AMD052','QBF01-AMD053','QBF01-AMD054']
h['latest_failure_review']='AVE최초③확신0.91/공식⑤불일치이력불변.상징/물리층위비대칭과미제시후속불행추가오류.③해석한계유보.'
write('session_handoff_20261016_01.json',h)
print('25배치감사완료.다음1001.')
