import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,rows,append,write,sha
from resume_support_20261016 import finish
assert not any(r['audit_id']=='QBF01-AUDIT026' for r in rows(OUT/'semantic_sample_audits.jsonl'))
c=json.loads((OUT/'checkpoint.json').read_text());assert c['reviewed_questions']==1040 and c['new_scene_count']==1549
allrows=rows(OUT/'current_question_reviews.jsonl');batch=[r for r in allrows if r['batch_number']==26]
assert len(batch)==40 and sum(len(r['scenes']) for r in batch)==42
cases=['AVL','AVR','AVV','AVX','AWD','BAT','BAX','BBC','BBJ','BBN','BBO','BBQ','BBX','BBZ','BCC','BCE','BCF','BCI','BCJ']
sample=[r for r in batch if set(r['case_ids'])&set(cases)]
assert len(sample)==19 and sum(len(r['scenes']) for r in sample)==21
byid={s['event_id']:s for r in allrows for s in r['scenes']}
def events(cs):return [s['event_id'] for r in batch if set(r['case_ids'])&set(cs) for s in r['scenes']]
bbo=next(r for r in batch if 'BBO' in r['case_ids']);s=bbo['scenes'][0]
old_reason=bbo['option_checks'][0]['reasoning'];assert '항상' in old_reason
old_inv=s['educational_production']['logical_invariants'];assert '필요조건이나' in old_inv
amds=[{'amendment_id':'QBF01-AMD055','event_id':s['event_id'],'reason':'26배치감사:공유기호에여러주체가참여함이단일의미확정의충분조건이아니라는것만필요하다.필요조건까지부정한불필요한일반명제를삭제.정답·추론불변.','changes':[{'field_path':'educational_production.logical_invariants','old_value':old_inv,'new_value':'동일한기호를여러주체가공유한다는사실만으로그들이동일한의미에합의하거나확정함이보장되지않는다.'}]}]
for num,case,scene_idx,pid,reason in [(56,'BCF',1,'정보신뢰','정보신뢰의정의는정보전달주체의접근·기억·확신조건검사이다.이장면은정답출처확인과해석충분성이라는연구검증층위의구별이므로동일한문항풀이연산으로과잉계수하지않고연결제거.'),(57,'BBN',0,'누락연결전제','누락연결전제는이유와결론사이추가로필요한가치·효과연결을찾는정의이다.이문항은본문에제시된두이론의공통일반화가정을추상화하는과업이므로그특정누락연결연산을확정하지않고연결제거.원58판정은별도이력유지.')]:
 r=next(r for r in batch if case in r['case_ids']);sc=r['scenes'][scene_idx];old=sc['pattern_connections'];assert any(l['pattern_id']==pid for l in old)
 amds.append({'amendment_id':f'QBF01-AMD{num:03}','event_id':sc['event_id'],'reason':'26배치직접감사:'+reason,'changes':[{'field_path':'pattern_connections','old_value':old,'new_value':[l for l in old if l['pattern_id']!=pid]}]})
assert not ({a['amendment_id'] for a in amds}&{a['amendment_id'] for a in rows(OUT/'scene_amendments.jsonl')})
assert not any(a['amendment_id']=='QBF01-QAMD009' for a in rows(OUT/'question_amendments.jsonl'))
proof=json.loads((OUT/'BCF_official_source_review_20261016.json').read_text())
a=proof['answer_original'];assert a['answer']=='②' and a['question_number']==34 and sha(ROOT/a['path'])==a['sha256']
bcf=next(r for r in batch if 'BCF' in r['case_ids'])
b=next(r['payload'] for r in bcf['original_evidence_states'] if r['stage']=='blind')
assert b['selected_answer']==3 and b['confidence']==0.86 and bcf['selected_answer']==2 and proof['needs_astra_review']
assert sum('BCF' in r['case_ids'] for r in allrows)==1
append('question_amendments.jsonl',[{'amendment_id':'QBF01-QAMD009','unique_question':bbo['unique_question'],'reason':'26배치감사:①원선지에없는항상을풀이에서추가하지않도록삭제.연출가중심변화가텍스트/오브제중요도서열을보장하지않는다는국소판정유지.','changes':[{'field_path':'option_checks.0.reasoning','old_value':old_reason,'new_value':'① 연출가중심화에서텍스트보다오브제가더중요하게되었다는서열변화까지도출할근거는없다.원선지에없는항상이라는전칭을추가하지않는다.'}]}])
append('scene_amendments.jsonl',amds)
devs=[
 {'development_id':'QBF01-DEV105','pattern_ids':['비교축','관계귀속','기준내부검사'],'evidence_event_ids':events(['AVL','AVR','AVV','AVX','BAX']),
 'finding':'AVL경계구획/외부차단,AVR투영면/보존성질과투영중심/원중심,AVV표현변환/정보삽입,AVX부분절단/성분삭제,BAX탐구대상/이용매개를분리해야한다.',
 'decision':'AVR의a와1/a는본문방향별국소축척의보정표현이지반경500km영역의정확적분결과가아니다.곱보존을가중합상쇄로연결하지않음.AVX의분산잔존을서로다른단서대체BFP005와자동통합하지않음.',
 'next_counterexample':'창호가차단기능을가져도차단우선목적이되는것은아니다.북극중심거리보존으로북위38도원모양을보장할수없다.원본고주파질감이삭제된식별자를복원해주지않는다.',
 'educational_use':'보존대상·조작대상·고정기준·시점과범위를명시하여닮은표현사이의역할교환을막는다.'},
 {'development_id':'QBF01-DEV106','pattern_ids':['강도보존','조건부방향'],'evidence_event_ids':events(['BBJ','BCE','BAT','BBC','BBZ']),
 'finding':'BBJ는방향관계에서출력의가속을도출할수없다.가상a=exp(t),T=exp(-t)는a쌍미분양수·T일미분음수·T쌍미분양수여서입력가속과출력감속감소가양립한다.BCE는P(강함|인공)에서P(인공|강도)의단조성을자동도출하지못한다.',
 'decision':'BBJ/BCE의기존유보를수학반모형·조건부확률방향으로구체화했다.실제우주법칙·실측신호분포로주장하지않음.BAT하위유형/전체,BBC현재장치한계/영구불가능,BBZ개체군/종외연한계도유지.',
 'next_counterexample':'변화방향이반대여도변화율의변화방향은다를수있다.강한자연신호가많아지는분포에서는강도증가가인공발신가능성증가로이어지지않을수있다.근거없음을항상무관으로뒤집지않는다.',
 'educational_use':'방향·속도·가속,원인조건확률·역조건확률,하위범위·전체범위의층위를따로적는다.'},
 {'development_id':'QBF01-DEV107','pattern_ids':['표현기능판독','정보신뢰','어휘행동'],'evidence_event_ids':events(['AWD','BCC','BCG','BCI','BCJ']),
 'finding':'AWD는온기주제와역설방식의두요건, BCC는꿈내용/꿈보고/신뢰의세층위, BCG는배경사실/주제해석, BCI는태도변화/변화이유, BCJ는부정적태도공통/취득행위차이를검사한다.',
 'decision':'BCC②엄니호칭과⑤죄의식해석한계유지.사회·의학적외부사실검증으로확대하지않는다.BCI산전수전다는관용적노련함으로,BCJ는사전전문검증과문맥판정을구별한다.',
 'next_counterexample':'꿈속사건이비현실적이어도그꿈을꿨다는말이거짓인것은아니다.타인말의영향을받아도독자적반성·제안이있으면무소신으로환원할수없다.주제일치만으로역설요건이충족되지않는다.',
 'educational_use':'상징·관용의미와문자적양화의층위를일관되게적용한다.발문에없는중심성·전칭조건을추가하지않는다.'},
 {'development_id':'QBF01-DEV108','pattern_ids':['비교축','강도보존'],'evidence_event_ids':events(['BBN','BBO','BBQ','BBX']),
 'finding':'BBN은본문의공통가정을추상화하고BBO는공유기호와해석결과를나눈다.BBQ는양쪽인형의시간구현근거를따로확인하며BBX는적응/생성/멸종을억지이분하지않는다.',
 'decision':'AMD057로BBN누락연결전제의특정정의과잉연결제거.원58/77판정불변.QAMD009는BBO①에추가한항상삭제,AMD055는필요조건까지불필요부정한일반문구를공유만으로합의가보장되지않는다는국소충분성으로수정.',
 'next_counterexample':'같은도구는같은기능을보장하지않고서로다른논점은항상정반대주제를뜻하지않는다.전제내용이일반화라고그전제를복원하는행동자체가새귀납인것도아니다.',
 'educational_use':'같은주제어보다후보정의가요구하는행동을검사한다.주장의내용·논증역할·문항과제를구별하여중복계수하지않는다.'},
 {'development_id':'QBF01-DEV109','pattern_ids':['관계귀속','강도보존'],'evidence_event_ids':events(['BCF','AVV','BCE']),
 'finding':'BCF의공식원문보기와원HWP홀수형34번②를이번직접확인했다.하지만ㄷ의간접영향을허용하며ㄹ을충분배제하는기준은여전히확정하지못했다.정답확인과의미충분성은다른상태이다.',
 'decision':'BCF최초③0.86·공식②불일치와needs_astra_review및기존depth미해결유지.고유문항1회.새확인은공식페이지시각대조+원HWP표셀추출이며렌더이미지확인은아님.AMD056으로연구메타검증을정보신뢰후보의문항연산으로계수한연결만제거.',
 'next_counterexample':'더권위있는정답표를반복확인해도ㄹ의무관성논거가생기지는않는다.은하성분과행성재료가다른단위라는사실만으로간접의존이전무하다고증명할수없다.',
 'educational_use':'출처정본성·최초성패·후속추론·미해결조건을독립필드로보존한다.정답맞춤형으로논증의공백을메우지않는다.'}
]
existing={r['development_id'] for r in rows(OUT/'pattern_development.jsonl')}
assert not any(d['development_id'] in existing for d in devs)
assert all(e in byid for d in devs for e in d['evidence_event_ids'])
append('pattern_development.jsonl',devs)
write('audit_026_selected_checks.json',{'sample_case_ids':cases,'sample_questions':19,'sample_scenes':21,'sample_options':95,'amendments':['QBF01-QAMD009','QBF01-AMD055','QBF01-AMD056','QBF01-AMD057'],'holds_preserved':['AVV','BAT','BBC','BBJ','BBZ','BCC','BCE','BCF'],'BCF_source_review':'BCF_official_source_review_20261016.json','BCF_semantic_resolved':False,'BCF_initial_preserved':{'answer':3,'confidence':0.86,'official':2},'BBJ_countermodel':'a=exp(t),T=exp(-t):a이차미분>0,T일차미분<0,T이차미분>0.가상반모형이며실제우주식아님.','visuals':'G326정자,G327사진/조각,G328투영2도판,G330질감,G332흑백회화직접재확인.색상판독은본문서술과구별.','checks':'중심/형상·변환/추가정보·대상/매개·관점귀속·복수요건·가속강도·조건부확률방향·상징/문자·전칭추가금지검토.','pass':True})
append('semantic_sample_audits.jsonl',[{'audit_id':'QBF01-AUDIT026','batch':26,'date':'2026-10-16','sample_case_ids':cases,'sample_questions':19,'sample_scenes':21,'sample_options':95,'method':'주에이전트가작성시직접읽은원문·발문·선지·기존판정과현행표본19문항95선지21장면을재대조.도판직접확인·BCF원문/원HWP추가대조.기계적인용·해시검사는26배치40문항.','dimensions':{'추론':'비교축·의존방향·가속변화율·역조건확률·목표대상/매개·상징과신뢰층위검토.','전체선지':'19문항95선지와조합보기하위명제대조.','이력':'BCF최초오답과별도판정·고유1회계수.추가출처확인과미해결의미를분리.','후보':'AMD055~057/QAMD009정밀화·DEV105~109귀납.신규후보추가없음.','활용':'본문의정성관계·현행과거사실·실제실측·가상반모형을구별해기록.'},'findings':[{'cases':['BBO'],'issue':'원선지에없는항상및불필요필요조건부정','resolution':'QAMD009/AMD055로국소명제에한정.'},{'cases':['BBN','BCF'],'issue':'기존후보정의와다른추론행동연결','resolution':'AMD056/057해당연결만제거.원판정·추론보존.'},{'cases':['BCF'],'issue':'공식답대조와ㄹ배제논거의별도공백','resolution':'원HWP표셀②직접확인.의미미해결과최초③0.86유지.'},{'cases':['AVV','BAT','BBC','BBJ','BBZ','BCC','BCE','BCF'],'issue':'기존해석강도·범위·추론한계','resolution':'현행유보승계로누적75.'}],'decision':'26배치40문항42장면·표본19문항21장면95선지감사·DEV105~109완료.누적1040문항1549장면·유보75.잔여37문항을1041부터계속.','unresolved_blocking_error_count':0,'limitations':'BCF의의미미해결을해결완료로보고하지않음.표본밖의미무오류·현행외부사실보증없음.다른모델호출·Gitpush·보호원장전수해시없음.'}])
finish('audit_026.py',[next(c for c in r['case_ids'] if not c.startswith('BASIC-')) for r in batch],['26배치표본19문항21장면95선지감사·DEV105~109.AMD055~057/QAMD009정밀화.BCF공식원HWP②추가확인과의미미해결분리.누적1040/1549·유보75.1041부터계속.'])
write('batch_026_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
write('batch_026_validation.json',json.loads((OUT/'audit_026_validation.json').read_text()))
h=json.loads((OUT/'session_handoff_20261016_01.json').read_text())
h['current_session_amendments']=['QBF01-AMD049','QBF01-AMD050','QBF01-QAMD007','QBF01-QAMD008','QBF01-AMD051','QBF01-AMD052','QBF01-AMD053','QBF01-AMD054','QBF01-QAMD009','QBF01-AMD055','QBF01-AMD056','QBF01-AMD057']
h['BCF_followup']={'official_source_review':'BCF_official_source_review_20261016.json','official_answer':2,'initial_answer':3,'initial_confidence':0.86,'source_rechecked':True,'semantic_resolved':False,'remaining':'ㄷ간접영향허용과ㄹ완전배제의일관된충분기준','needs_astra_review':True}
write('session_handoff_20261016_01.json',h)
print('26배치감사완료.다음1041.')
