import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,rows,append,write,source,BYCASE,sha,source_module
from resume_support_20261016 import finish
assert not any(r['audit_id']=='QBF01-AUDIT027' for r in rows(OUT/'semantic_sample_audits.jsonl'))
c=json.loads((OUT/'checkpoint.json').read_text());assert c['reviewed_questions']==1077 and c['new_scene_count']==1586 and c['next_order'] is None
allrows=rows(OUT/'current_question_reviews.jsonl');batch=[r for r in allrows if r['batch_number']==27]
assert len(batch)==37 and sum(len(r['scenes']) for r in batch)==37
cases=['BCN','BCP','BCT','BCW','BCY','BDF','BDI','BDK','BDN','BDQ','BDU','BDV','BDY','BEB','BED','BEE','W','BRI','X','BRM']
sample=[r for r in batch if set(r['case_ids'])&set(cases)]
assert len(sample)==20 and sum(len(r['scenes']) for r in sample)==20
assert sum(bool(r['unresolved']) for r in sample)==18
byid={s['event_id']:s for r in allrows for s in r['scenes']}
def events(cs):return [s['event_id'] for r in batch if set(r['case_ids'])&set(cs) for s in r['scenes']]
for case in ['BDV','BRM']:assert sum(case in r['case_ids'] for r in allrows)==1
for case in ['W','X']:
 normalized=source(BYCASE[case]);der=normalized['backfill_source_derivation'];original=source_module.packet(der['original_source'])
 assert sha(ROOT/der['original_source'])==der['original_sha256']
 assert all(normalized[k]==original[k] for k in ['passage_text','stem','choices'])
devs=[
 {'development_id':'QBF01-DEV110','pattern_ids':['단계구분','관계귀속','분류기준'],'evidence_event_ids':events(['BCL','BCN','BCP','BCQ','BDL','BDR','BDT']),
 'finding':'BCL은소리반복이사건동일성을뜻하지않고BCN은장면의부차정보가별도부수스토리인것은아님을보인다.BCP/BCQ는임신순번·항원노출·항체생성주체를나누며BDL은합성/전환,BDR/BDT는응집전후·세포/시험관·보호주체를구별한다.',
 'decision':'같은외형행동이나명칭보다실제관계·순서·조건을우선한다.BCPㄱ기능유추는세균/혈구의분류동일성으로강화하지않는다.BDR대부분비가역과BDT세제후회복은조건이달라양립한다.',
 'next_counterexample':'외부주사라는조건만으로수동면역이아니다.첫임신도항원재노출일수있다.혼합에서안정해졌다면원래불안정했던표적을찾아야보호방향을정할수있다.',
 'educational_use':'순번·단계·주체·환경을별도열로써서중간단계삭제와조건전이를검사한다.'},
 {'development_id':'QBF01-DEV111','pattern_ids':['조건부방향','기준내부검사','강도보존'],'evidence_event_ids':events(['BDN','BEA','BEB','BEE','BCT']),
 'finding':'BDN의국소난소개선은뇌하수체·지방세포의전신순효과와다르다.BEB는내부3개에서실제감주r≥1이라는조건하에3-r≤2를얻는다.BEE는분포·전제·대안효율이보험설을다르게약화하며BCT도비판표적이항목마다다르다.',
 'decision':'BDN전신순효과·정답유일성,BEB보사용→실제감주조건,BEE통제없는ㄱ의완전반증은미해결/범위유보로유지.기존depth를해소완료로올리지않는다.국소개선이나비판관련성이전체충분성을보장하지않는다.',
 'next_counterexample':'BEB에서r=0을허용하면상한3배제는사라진다.BDN의기관선택성·경로크기정보가추가되기전에는한경로만으로총효과를정할수없다.BEE대안이있다는것과대안이더효율적이라는것도다르다.',
 'educational_use':'수학범위·인과방향·반박강도옆에그것을정당화하는조건을명시한다.'},
 {'development_id':'QBF01-DEV112','pattern_ids':['비교축','강도보존','표현기능판독'],'evidence_event_ids':events(['BCW','BCY','BDF','BDI','BDK','BDQ','BDU','BDY','BED','W','BRI','X']),
 'finding':'기획의전수성·선별반응·완전성지향·기준의가치·기사내확인·자연적가능성·주석경향·관점틀·제도합리성·규범구속력·숨은구조·특정관점귀속은각각다른해석범위를요구한다.',
 'decision':'27배치의18개기존한계/자격조건을현행유보로승계해전체93문항으로보존.문맥적수용을전역전칭·실측확인·엄밀동치로승격하지않음.유보수증가는정답변경건수가아니다.',
 'next_counterexample':'기사에근거가없어도현실에서검증가능할수있다.관점이구조→행위를부정하지않아도그관점에특정사례의그방향해석을귀속할근거는별도로필요하다.기준의전략효용이윤리적가치를자동보장하지않는다.',
 'educational_use':'의미를수용한범위와그범위를넘는강한명제를한쌍으로기록한다.'},
 {'development_id':'QBF01-DEV113','pattern_ids':['관계귀속','논거결론위계','반박표적','행위결과분리'],'evidence_event_ids':events(['BCU','BCW','BDD','BDV','BED','BEH','BEI','BRM']),
 'finding':'같은기록결론에도다른이유가있고같은제도지속에도다른설명기제가있다.원전표현과주석가동기해석,비판의어조와공격방향,외래방법과고유내용보존,행위결과만족과선행목적은서로구별된다.',
 'decision':'BED/BEE/X의74·75통합군과하위행동차이를유지한다.BRM별도55/78주판정및양상태그기각은역사적판정으로보존하며현재사이트의도·오류를확정하지않는다.',
 'next_counterexample':'같은결과를원한다고같은전제를갖는것은아니다.만족이생겨도만족때문에돕는것은아닐수있다.중국서술선례를따라도신라고유표현을보존할수있다.',
 'educational_use':'주체·논항·목표·동기·결과를명시하고공통결론에서공통전제를역추론하지않는다.'},
 {'development_id':'QBF01-DEV114','pattern_ids':['관계귀속','강도보존'],'evidence_event_ids':events(['BDV','W','X','BRM']),
 'finding':'BDV는기존F와동일문항이고태그·판정요약의사전노출이사후에식별되었다.W/X는독립풀이패킷에서읽는본문·발문·선지필드를문자열무변경JSON으로정규화했으며BRM은기존별도판정을포함한한고유문항이다.',
 'decision':'BDV엄격blind제외와초기unknown/후속정정모두보존.W/X원MD해시및필드동일성재검사.전체1077고유문항의사후추출을마쳤으나신규blind성과는0이며기존616장면/95후보의소급변환·동결코드북갱신은하지않음.',
 'next_counterexample':'태그일치나후속정답확인은최초독립성을되돌리지못한다.형식정규화는원문내용복원이아니며중복ID를새기출수로계수할수없다.',
 'educational_use':'자료정본·파생형식·노출시점·최초판정·후속수정·미해결상태를서로다른필드로관리한다.'}
]
existing={r['development_id'] for r in rows(OUT/'pattern_development.jsonl')}
assert not any(d['development_id'] in existing for d in devs)
assert all(e in byid for d in devs for e in d['evidence_event_ids'])
append('pattern_development.jsonl',devs)
write('audit_027_selected_checks.json',{'sample_case_ids':cases,'sample_questions':20,'sample_scenes':20,'sample_options':100,'new_amendments':[],'holds_in_sample':18,'new_candidates':[],'checks':{'BCN_BCP_BCQ':'스토리귀속·임신/노출순서·항체생성주체·기능유추범위확인.','BCT_BEE':'반박표적·약화/완전반증의효력분리.','BCW_BDF_BDI_BDK':'기획전칭·지향공통성·기준가치층위·기사내무근거범위유지.','BDN_BEB':'전신순효과와보사용의감주함축은미해결유지.','BDQ_BDU_BDY_BED':'자연적가능성·종합경향·지정관점틀·해당제도합리성의범위보존.','BDV_BRM':'별도판정·중복고유1회·BDV사후노출정정보존.','W_X':'MD파생JSON의본문/발문/선지동일성및원MD해시검사.규범구속력·귀속근거부족범위보존.','BRI':'숨은작용은유와영구인식불가능·저항절대불가구별.'},'pass':True})
append('semantic_sample_audits.jsonl',[{'audit_id':'QBF01-AUDIT027','batch':27,'date':'2026-10-16','partial_final_batch':True,'orders':[1041,1077],'batch_questions':37,'batch_scenes':37,'sample_case_ids':cases,'sample_questions':20,'sample_scenes':20,'sample_options':100,'method':'주에이전트직접감사.작성시읽은원문·발문·보기·전체선지·기존판정과현행표본20문항100선지20장면재대조.표본은마지막묶음의유보18문항전부와중복이력2문항을포함.기계검사는마지막37문항전체.','dimensions':{'추론':'단계·주체·목적·방향·공통성의추상도와반박강도검사.','전체선지':'20문항100선지와조합보기하위명제검토.','이력':'BDV=F사전노출후속정정,BRM별도판정고유1회,W/X필드무변경정규화확인.','후보':'기존정의범위에따른연결·74/75통합군유지.신규후보/의미amendment없음.','활용':'국소효과/전체충분성·문맥수용/전칭증명·출처확인/의미해결을구별.'},'findings':[{'cases':['BDN','BEB','BEE'],'issue':'전신순효과·실제감주조건·약화/결정반증의미해결범위','resolution':'구체화된장면은저장하되기존depth/추론유보해소완료로올리지않음.'},{'cases':['BDV','BRM'],'issue':'별도분석과동일원문중복','resolution':'고유문항각1회.원판정·노출정정불변.'},{'cases':['W','BRI','X'],'issue':'비유·규범·관점귀속의강도','resolution':'기존자격조건을현행유보로승계.'}],'decision':'최종부분묶음37문항37장면·표본20문항20장면100선지감사·DEV110~114완료.누적1077문항1586장면·유보93.전체인용·출처·보호파일최종검증대기.','unresolved_blocking_error_count':0,'limitations':'전건사후추출완료가유보93건의논증완전해결이나100코드최종확정을뜻하지않음.표본밖의미무오류보증없음.새blind0·다른모델호출·Gitpush없음.'}])
finish('audit_027.py',[next(c for c in r['case_ids'] if not c.startswith('BASIC-')) for r in batch],['최종37문항37장면·표본20문항20장면100선지감사·DEV110~114완료.전건1077/1586작성·유보93보존.전수출처/보호검증대기.'])
write('batch_027_checkpoint.json',json.loads((OUT/'checkpoint.json').read_text()))
write('batch_027_validation.json',json.loads((OUT/'audit_027_validation.json').read_text()))
print('27최종부분배치감사완료.전체검증대기.')
