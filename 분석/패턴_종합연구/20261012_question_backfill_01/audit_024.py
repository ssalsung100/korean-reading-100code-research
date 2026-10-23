import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write
from resume_support_20261016 import finish
assert not any(r['audit_id']=='QBF01-AUDIT024' for r in rows(OUT/'semantic_sample_audits.jsonl'))
c=json.loads((OUT/'checkpoint.json').read_text())
assert c['reviewed_questions']==960 and c['new_scene_count']==1465
allrows=rows(OUT/'current_question_reviews.jsonl')
batch=[r for r in allrows if r['batch_number']==24]
assert len(batch)==40 and sum(len(r['scenes']) for r in batch)==45
cases=['AQM','AQQ','ARH','ARI','ARJ','ARO','ARQ','ART','ASB','ASD','ASF','ASJ','ASN','ASS','ASZ','ATA']
sample=[r for r in batch if set(r['case_ids'])&set(cases)]
assert len(sample)==16 and sum(len(r['scenes']) for r in sample)==19
byid={s['event_id']:s for r in allrows for s in r['scenes']}
def events(cs):return [s['event_id'] for r in batch if set(r['case_ids'])&set(cs) for s in r['scenes']]
devs=[
 {'development_id':'QBF01-DEV095','pattern_ids':['표현기능판독','전개대상','관계귀속'],'evidence_event_ids':events(['AQM','AQQ','ASN','ASW']),
 'finding':'AQM의장치기능과작품전체주제,AQQ의현실소재와서술방식,ASN의국소행동기능과인물전체정서,ASW의비동조와적극환영은판단층위가다르다.',
 'decision':'AQQ에중심기법이라는미제시조건을추가하지않고비유존재만으로모든사실적묘사를부정하지않는다.ASN의전반적두려움가능성과국소전략적관찰은양립가능.정답불변.',
 'next_counterexample':'몸짓이두려움완화를위한것이라는직접지시가추가되면ASN①을재검토한다.비판비동조에승진환영내면이추가되면ASW②의근거상태가달라진다.',
 'educational_use':'행동·장치·서술방식의직접근거와작품전체해석을분리해서기록한다.'},
 {'development_id':'QBF01-DEV096','pattern_ids':['강도보존','비교축','후보설명비교'],'evidence_event_ids':events(['ARH','ARI','ARJ','ART','ASB','ASJ']),
 'finding':'ARH는가장가까운입장의추론,ARI는보유/거래와신규조달비중,ARJ는장기수준과경로,ART는한요인제거와전체편차,ASB는추구강도와이성적선택,ASJ는어려움과불가능을구별한다.',
 'decision':'여섯사례의유보를유지하며서로다른누락근거를하나의보편오류로뭉개지않는다.ARI②의충분성유보는이번새점검이고나머지의기존불확실성은현행에승계.공식답변경없음.',
 'next_counterexample':'보유주식의유통거래만확대되는상황은기업신규조달증가와동일하지않다.장기소득수준이높아도전환기성장률은낮을수있다.이탈확률이낮아도0이라고증명된것은아니다.',
 'educational_use':'명제의범위·비교기준·가능성강도·생략된보조조건을각각표시한다.'},
 {'development_id':'QBF01-DEV097','pattern_ids':['이론부분유지','분류기준','비교축','기능유추'],'evidence_event_ids':events(['ARO','ARQ','ASD','ASF','ASS']),
 'finding':'ARO는역학모형의폐기와장실재유지,ARQ는연속체역학과입자론,ASD는발화귀속과변화축,ASF는부분부합과전체동일,ASS는비동일과배타를구별한다.',
 'decision':'자료에등장하는부분/전체또는역학이라는단어만으로대표연산을정하지않는다.원번호판정을보존하며실제선지의귀속·분류·비교행동을따로기술. ARO의매질용어·시기제한유지.',
 'next_counterexample':'역학적으로설명했다고반드시입자적원격작용모형인것은아니다.공유구조가있다고역사적이론전체가현대이론과같지는않다.원인이모두강제는아니라고해서강제가원인밖에있는것도아니다.',
 'educational_use':'유지한속성·폐기한속성·공유한비교축을나누고범주관계를그린다.'},
 {'development_id':'QBF01-DEV098','pattern_ids':['비교변인','기준내부검사','병치인과분리','강도보존'],'evidence_event_ids':events(['ART','ASZ','ATA']),
 'finding':'ART는원인하나의제거에따른문항내추정,ASZ는가설참조건의두분리비교,ATA는실제보고된군별결과와관찰편향의적용이다.세과제의근거지위가다르다.',
 'decision':'ASZ의성분/경로변경은비교변인후보에맞지만한요인부재인ART를완전통제실험으로확대하지않는다.ATA는군간차이없음을개인별안전이나금기부재로바꾸지않음.',
 'next_counterexample':'관찰군의혈압이낮다는동반만으로치료가혈압을낮췄다고할수없다.가설참의조건부예측을추가연구의실제관측이라고기록해서도안된다.',
 'educational_use':'가설·설계·관측·해석의열을분리하여조건부예측과확인된결과를구별한다.'},
 {'development_id':'QBF01-DEV099','pattern_ids':['정보신뢰','관계귀속','비교축'],'evidence_event_ids':events(['ARQ','ASZ','ASX','ASP','ASR']),
 'finding':'ARQ의그림누락오판후정정은새복원이아니며ASZ의별도49/43·prepared46판정은동일문항의이력이다.ASX평가가치·ASP공통규범·ASR비판대상도누가무엇을어떤근거로판단했는지유지해야한다.',
 'decision':'ARQ기존hold/정정raw를함께보존.ASZ고유문항1회와별도판정전문보존.역사적판정·이번사후해석·공식자료의지위를서로대체하지않음.신규blind0.',
 'next_counterexample':'한사람만말한규범이상식적으로옳아도두사람의공통견해가되지는않는다.직무를알고도수행하지않는사람을직무를모르는사람으로평가할수없다.',
 'educational_use':'내용판단과그판단의주체·시점·출처를함께기록하고후속확인을최초풀이에소급하지않는다.'}
]
existing={r['development_id'] for r in rows(OUT/'pattern_development.jsonl')}
assert not any(d['development_id'] in existing for d in devs)
assert all(e in byid for d in devs for e in d['evidence_event_ids'])
assert sum('ASZ' in r['case_ids'] for r in allrows)==1
write('audit_024_selected_checks.json',{'scope':'이번세션직접읽은원문·5선지·기존판정에대한사후표본감사.외부의학·법률·과학사실의현행검증아님.','sample_case_ids':cases,'sample_questions':16,'sample_scenes':19,'sample_options':80,'checks':{'AQM_AQQ_ASN':'직접기능/전체해석·현실소재/사실적서술·국소행동/전체정서구별.미제시중심성조건추가금지.','ARH_ARI_ARJ':'가장가까운입장과명시규정,보유거래와신규조달,장기수준과전기간성장률구별.','ARO_ARQ':'초기매질모형/후기장개념구별.그림은기존제공자료로이번신규복원아님.','ART_ASB_ASJ':'원인한개제거/전체편차·행동강도/이성적선택·어려움/불가능의유보유지.','ASD_ASF_ASS':'주체귀속·부분부합·전체동일·비동일/배타구별.','ASZ_ATA':'성분/경로와질환대응,가설참예측/실제결과,확률/전원발병,관찰특성/치료효과구별.별도판정불변·중복1회.'},'new_amendments':[],'holds_preserved':['ARH','ARI','ARJ','ARO','ART','ASB','ASJ','ASN'],'pass':True})
append('pattern_development.jsonl',devs)
append('semantic_sample_audits.jsonl',[{'audit_id':'QBF01-AUDIT024','batch':24,'date':'2026-10-16','sample_case_ids':cases,'sample_questions':16,'sample_scenes':19,'sample_options':80,'method':'주에이전트직접감사.작성시직접읽은원문·발문·선지·기존풀이와현행표본80선지/19장면의추론·경계·후보연결을재대조.기계적인용·해시검사는24배치40문항.','dimensions':{'중간추론':'직접기능/전체해석,보유/조달,장기수준/성장경로,한요인/완전통제,부분부합/동일성,가설/관측구별.','전체선지':'16문항80선지및조합보기하위명제검토.','원문이력':'ARQ그림누락오판후정정이력보존.ASZ별도판정과고유문항1회확인.','후보경계':'DEV095~099귀납.번호만으로분리하지않고실제판단연산과제한기록.','활용':'논항·양태·범위·주체·시점을명시하여변형문항의추가전제위험제어.'},'findings':[{'cases':['ARI'],'issue':'국제주식보유에서자금조달의존비중직접도출불가','resolution':'이번새충분성유보유지.공식⑤불변.'},{'cases':['ARH','ARJ','ARO','ART','ASB','ASJ','ASN'],'issue':'기존풀이의문맥적해석·범위제한','resolution':'현행유보승계.누적63.'},{'cases':['ARQ','ASZ'],'issue':'자료확인·판정출처이력혼동위험','resolution':'사후확인을최초풀이에소급하지않고별도판정병존보존.'}],'decision':'24배치40문항45장면·표본16문항19장면80선지감사및DEV095~099완료.누적960문항1465장면·유보63.미완료117문항을961부터계속.','unresolved_blocking_error_count':0,'limitations':'표본밖의의미무오류보증없음.외부사실의현행전수검증없음.다른모델호출·Gitpush·보호원장전수해시없음.'}])
finish('audit_024.py',[next(c for c in r['case_ids'] if not c.startswith('BASIC-')) for r in batch],['24배치40문항45장면·표본16문항19장면80선지감사·DEV095~099.유보63·정답불변.961부터계속.'])
write('batch_024_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
write('batch_024_validation.json',json.loads((OUT/'audit_024_validation.json').read_text()))
print('24배치감사완료.다음961.')
