import sys,json,itertools
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write
from resume_support_20261016 import finish
assert not any(r['audit_id']=='QBF01-AUDIT022' for r in rows(OUT/'semantic_sample_audits.jsonl'))
c=json.loads((OUT/'checkpoint.json').read_text())
assert c['reviewed_questions']==880 and c['new_scene_count']==1376
allrows=rows(OUT/'current_question_reviews.jsonl')
batch=[r for r in allrows if r['batch_number']==22]
assert len(batch)==40 and sum(len(r['scenes']) for r in batch)==53
cases=['BRW','BRZ','BSM','BSR','BST','BSH','BSZ','BTI','BTJ','BTB','BTL','ALN','ALO','ALR','ALU','ALY']
sample=[r for r in batch if set(r['case_ids'])&set(cases)]
assert len(sample)==16 and sum(len(r['scenes']) for r in sample)==24
byid={s['event_id']:s for r in allrows for s in r['scenes']}
aln=next(r for r in allrows if r['unique_question']=='U0200-Q01')
old=aln['option_checks'][1]['reasoning']
assert '중심 기법' in old
assert not any(r['amendment_id']=='QBF01-QAMD007' for r in rows(OUT/'question_amendments.jsonl'))
new='② 칫솔·옷 등의 사물과 일부 속성은 나오지만,사물의 세밀한 묘사를 통해 애상적 정서를 강화한다는 연결을 뒷받침할 충분한 서술은 없다. 구체적으로 그려지는 눈물·얼굴·돌봄 행동의 대상을 사물로 바꾸지 않는다. 선지가 요구하지 않은 중심 기법 여부를 배제 기준으로 추가하지 않는다.'
truth=[]
for V,T in itertools.product([False,True],repeat=2):
 state={(False,False):'무관심',(False,True):'불안',(True,False):'안녕',(True,True):'위기'}[V,T]
 truth.append({'가치의식':V,'위협의식':T,'정의상태':state,'원무관심조건':not V and not T,'잘못된OR조건':not V or not T})
assert [r['정의상태'] for r in truth if r['잘못된OR조건'] and not r['원무관심조건']]==['불안','안녕']
devs=[
 {'development_id':'QBF01-DEV085','pattern_ids':['전개대상','기준내부검사','논거결론위계'],
  'evidence_event_ids':['QBF01-U0483-Q03-S01','QBF01-U0484-Q01-S01','QBF01-U0200-Q01-S01','QBF01-U0201-Q01-S01','QBF01-U0202-Q01-S01'],
  'finding':'LEET의감상기준적용·글전개판정과이번MEET의사물묘사기법·제목부제·역사서평가논점은소재등장과실제수행한서술행동을구별한다. ALN은사물등장≠세밀묘사,ALU는왕옹립사건≠정통성논증,ALR는소자제조≠회로설계이다.',
  'decision':'시험이달라도같은판단행동을국소적으로연결하되MEET5문항만으로시험전체의구현차이를일반화하지않는다. ALN의새보완초안에들어간중심기법이라는추가조건을QAMD007로삭제. 주제범위·기법근거·감상초점은각각보존하며KICE의생성근거우선순위는유지.',
  'next_counterexample':'사물의짧은색상정보하나가있다는사실과세밀묘사의충분근거는같지않다. 반대로어떤기법이주된것이아니어도실제로사용됐으면기법선지를무조건배제할수없다. ALR실용화를가능성으로고쳐도범위오류는남을수있다.',
  'educational_use':'기법·주제문항에서는발문이요구한기준만사용한다.명사소재·서술동사·논증기능·전체범위를구분하여출제조건을설계한다.'},
 {'development_id':'QBF01-DEV086','pattern_ids':['분류기준','문맥조작화','관계귀속'],
  'evidence_event_ids':['QBF01-U0484-Q03-S01','QBF01-U0484-Q03-S02','QBF01-U0488-Q03-S01','QBF01-U0488-Q03-S02','QBF01-U0203-Q02-S01'],
  'finding':'BRZ는명시된두인식축의AND조건을OR로약화한오류를반모형으로확인할수있다. BSM은행위요구와지위변경관계가다르고,ALY는자기선함/타인돌봄의설명초점에따른적합성판정이어서모든행위를배타적으로구획하지않는다.',
  'decision':'모든정의문항을동일한필요충분식또는배타적분류로취급하지않는다. BSM④·ALY②의기존국소해석제한을현행유보로승계하여51→53. 공식답유지·원raw불변.공동주후보16/15/37을단일번호로강제확정하지않음.',
  'next_counterexample':'BRZ의V참/T거짓은OR조건을만족하지만정의상안녕이다. BSM의행위비간섭의무와상대형성권부재는정의상다른축이다. ALY의대인돌봄이자기선함에도기여할가능성을전면부정할수없다.',
  'educational_use':'명시결합조건인지설명초점의비교인지먼저구별한다. 새문항에서범주중첩을금지할필요가있으면그조건을직접제시해야한다.'},
 {'development_id':'QBF01-DEV087','pattern_ids':['강도보존','누락연결전제','단계구분'],
  'evidence_event_ids':['QBF01-U0495-Q02-S01','QBF01-U0495-Q03-S01','QBF01-U0496-Q01-S02','QBF01-U0497-Q02-S01','QBF01-U0201-Q01-S02'],
  'finding':'BTI의어렵다는엄밀한불가능·유일필수조건보다약하다. BTJ는개별국민→추상일반인→전문가의단계완화,BTK는조건부가능성과완료성과,BTO는목적구속필연성부정과전면금지,ALR는연구가능성과실용화달성을나눈다.',
  'decision':'BTI의기존최초요약이선지보다강했던점을이번보완에서명시정밀화했다.반박을쉽게하려고선지를강화하지않는다.원blind·독립코드10이력·공식①불변.별도패턴추가나원코드경계의전역수정은하지않는다.',
  'next_counterexample':'없으면어렵다와없으면불가능하다는다른명제이며전자는유일해결책을뜻하지않는다. 실용화가확인되지않았다는것은실용화불가능을뜻하지않는다. 반드시참조할필요없음은참조금지가아니다.',
  'educational_use':'선지의정도·양태·시제를그대로옮겨검사한다. 가능성/필연성,곤란/불가능,제안/성과를출제시명확히구분한다.'},
 {'development_id':'QBF01-DEV088','pattern_ids':['정보신뢰','관계귀속','계기목적분리'],
  'evidence_event_ids':['QBF01-U0483-Q03-S01','QBF01-U0490-Q02-S01','QBF01-U0492-Q04-S02','QBF01-U0200-Q02-S01','QBF01-U0200-Q02-S02','QBF01-U0202-Q01-S02'],
  'finding':'BRW[B]는이번공식렌더에서마지막문단전체로사후확인했고BSR[A]는기존복원범위를재확인했다. BSZ는사용한근거와몰랐던것을구별하며ALO는음주행동보다화자의명시평가를우선하고추격에저지의도를추가하지않는다. ALU는명령/자발성차이를별도평가근거로쓴다.',
  'decision':'새원문확인을최초blind에소급하지않는다. ALU의오답번호정정은이미answer_check에있는수정이력으로승계한다. MEET원raw의strictblind=true와unique_primary_confirmed=false는그대로보존하되이번작업은모두사후보완으로계수한다.',
  'next_counterexample':'공식구간의확인은그구간의해석무오류를보장하지않는다. 음주만있고가장환한때라는평가가없으면ALO의인식판정근거는약해진다. 쫓아갔다는행동만으로출발저지라는목적은확정되지않는다.',
  'educational_use':'원관찰·인물평가·후행정보·사후복원·과거정정의출처를함께보존한다. 원문단서가새로확보된시점을연구성과와별도로남긴다.'},
 {'development_id':'QBF01-DEV089','pattern_ids':['비교축','중간시점','분류기준','관계귀속'],
  'evidence_event_ids':['QBF01-U0487-Q01-S01','QBF01-U0487-Q01-S02','QBF01-U0491-Q01-S01','QBF01-U0491-Q01-S02','QBF01-U0493-Q02-S01','QBF01-U0496-Q02-S01'],
  'finding':'BSH는같은이성우위의시작과끝사이에서도전과근거재해석을유지한다. BST는같은거래비용명칭의다른변수를분리한다. BTB는표리일체표현을대상별로분할하지않으며BTL은기준이다른동시지위를시간적전락으로바꾸지않는다.',
  'decision':'동일명칭·반대어·두항목의대칭배치만으로동일연산이나일대일대응을만들지않는다. 실제로같은변수·같은시점·같은대상·같은기준인지확인한뒤통합가능성을판단한다.이번새후보없음.',
  'next_counterexample':'정보비용감소와정치적변경비용증가는동시에성립할수있다. 지배계급소속이면서시장에서는피지배분파일수있다. 같은입장명칭으로끝나도논거와강도가달라지면무변화가아니다.',
  'educational_use':'명사마다대상·시점·측정기준을붙이고술어끼리의동일/대립/부분관계를확인한다. 서로다른변수의반대증감을형식모순으로출제하지않는다.'}
]
existing={r['development_id'] for r in rows(OUT/'pattern_development.jsonl')}
assert not any(d['development_id'] in existing for d in devs)
assert all(e in byid for d in devs for e in d['evidence_event_ids'])
append('question_amendments.jsonl',[{'amendment_id':'QBF01-QAMD007','unique_question':'U0200-Q01','reason':'22배치직접감사:발문은기법의사용여부를묻고중심기법일것을요구하지않는다.새보완초안의중심기법이라는추가조건을제거하고실제세밀묘사·정서강화의연결근거부족으로정밀화.정답·장면·인용근거불변.','changes':[{'field_path':'option_checks.1.reasoning','old_value':old,'new_value':new}]}])
write('audit_022_selected_checks.json',{
 'scope':'이번세션작성후직접의미감사.가상조건표는기출관측값아님.',
 'BRW':{'new_visual_resolution':'BRW_B_range_review_20261016.json','finding':'공식2009예비HWP렌더4쪽[B]괄호확인.이영화는호쾌한장면연출부터텍스트인것이다까지마지막문단전체.최초미보존은소급삭제하지않음.'},
 'BRZ':{'truth_table':truth,'finding':'가치/위협의주관적인식축.잘못된OR는불안·안녕을추가포함.확률계산성과아님.'},
 'BSM_ALY':'행위비간섭/지위면제와정의초점/전역배타성의경계는각기다르다.유보2문항승계.보기밖규칙을답에추가하지않음.',
 'BSR':'기존공식[A]페이지직접재확인.내용의격렬함·충격과서술의시간적긴박성을분리.⑤태도는장면한정.',
 'BST_BSH_BTB_BTL':'거래비용의서로다른변수,끝점/중간과정,표리일체표현,동시기준/시간변화검사.모순·일대일대응을표면어만으로구성하지않음.',
 'BSZ_ALO':'사용한근거를간과했다고바꾸지않음.화자의명시평가와행동단서를구별.추격→출발저지의미제시의도금지.',
 'BTI_BTJ':'어렵다는엄밀한필수관계보다약하다는수정명시.첫타협/재차완화로기준부담을판정하며전문가확대를무조건권고하지않음.',
 'ALN':'QAMD007:중심기법이라는미제시조건삭제.사물의짧은속성언급을전면부정하지않고실제세밀묘사·정서강화의근거를판정.',
 'ALR':'범위·성취수준두조건검사.실용화를가능성으로바꿔도트랜지스터한정의범위문제잔존.',
 'ALU':'기존오답필드5→1정정이력승계.옹립사건/정통성논지·자발/명령의평가기준구별.',
 'MEET_provenance':'5문항8장면은신규사후보완.기존strictblind·공동주후보미확정이력불변.이번공식정답원문전수재대조없음.',
 'new_amendments':['QBF01-QAMD007'],'holds_preserved':['BSM','ALY'],'pass':True})
append('pattern_development.jsonl',devs)
append('semantic_sample_audits.jsonl',[{
 'audit_id':'QBF01-AUDIT022','batch':22,'date':'2026-10-16','sample_case_ids':cases,'sample_questions':16,'sample_scenes':24,'sample_options':80,
 'method':'주에이전트직접감사.이번세션에서표본16문항전체원문·발문·5선지·기존풀이를직접읽어작성한뒤현행80선지와24장면의추론·경계·교육조건을재대조. BRW공식HWP4쪽과BSR공식[A]페이지직접확인증거사용.기계적인용·출처검사는22배치40문항에한정.',
 'dimensions':{'중간추론':'정의조건/설명초점·곤란/불가능·분류/서열·동시기준/시간변화·사용근거/간과검사.','전체선지':'표본80선지및BSM보기전체조건검토.','원문이력':'BRW[B]사후확인,BSR기존범위재확인.최초blind·노출·정정이력불변.','후보경계':'MEET공동주후보를단일코드로확정하지않음. ALNQAMD007으로추가조건철회. DEV085~089귀납.','활용':'LEET/MEET의국소반복연산만비교하고시험전체특징·생성기준가중치를소수사례로일반화하지않음.'},
 'findings':[{'cases':['ALN'],'issue':'기법판정에중심성추가조건이끼어든표현','resolution':'QAMD007로삭제.기법자체와정서효과연결근거검사로정밀화.정답·장면불변.'},{'cases':['BSM','ALY'],'issue':'사례의국소정의적용을전역배타성으로확대할위험','resolution':'기존제한을현행유보로승계.누적53.'},{'cases':['BTI'],'issue':'어렵다를유일필수조건으로요약한기존표현강도','resolution':'새보완에서조건부곤란의근거검사로정밀화.원raw보존.'},{'cases':['BRW','ALU'],'issue':'원문범위와과거기록정정의시점','resolution':'BRW사후직접확인과ALU기존answer_check정정을서로다른이력으로보존.'}],
 'decision':'22배치40문항53장면(LEET35문항45장면·MEET5문항8장면),표본16문항24장면80선지감사·DEV085~089귀납완료.누적880문항1376장면·유보53.미완료197문항모두MEET.881부터계속.',
 'unresolved_blocking_error_count':0,'limitations':'표본밖의미무오류·공식정답전수독립검증보증없음.이번MEET5건으로시험전체차이를확정하지않음.KICE생성근거우선순위유지.다른모델호출·Gitpush·보호원장전수해시없음.'}])
finish('audit_022.py',[next(c for c in r['case_ids'] if not c.startswith('BASIC-')) for r in batch],['22배치표본16문항24장면80선지감사·DEV085~089귀납. QAMD007 ALN미제시중심기법조건철회, BTI강도정밀화·BRW사후범위확인·MEET비배타성검토.누적880문항1376장면·유보53.881부터MEET계속.'])
write('batch_022_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
write('batch_022_validation.json',json.loads((OUT/'audit_022_validation.json').read_text()))
print('22배치감사완료.다음881.')
