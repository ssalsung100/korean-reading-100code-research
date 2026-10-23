import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write,refresh,validate
assert not any(x['audit_id']=='QBF01-AUDIT012' for x in rows(OUT/'semantic_sample_audits.jsonl'))
assert not any(x['development_id']=='QBF01-DEV040' for x in rows(OUT/'pattern_development.jsonl')),'부분 실행이면 잔여만 복구'
ss={s['event_id']:s for s in rows(OUT/'new_judgment_scenes.jsonl')}
qs={q['unique_question']:q for q in rows(OUT/'current_question_reviews.jsonl')}
fixes=[('QBF01-AMD029','QBF01-U0165-Q02-S02','AHE는공동규제의부분과담당자를확인한다.미흡시후속개입의조건은있으나이장면의판단은산출값을다음처리가사용하는계산·정보처리구조가아니다.단계구분D를단순사전/사후나제도분담전체로넓히지않고부분전체·관계귀속과구체진입조건을보존한다.'),('QBF01-AMD030','QBF01-U0165-Q03-S03','AHF의현재선지는사전플랫폼/조건부사후정부의주체·시점교환이다.명시된미흡조건을보존하되산출값사용이라는단계구분D의기존적용으로확정하지않고관계귀속을남긴다.'),('QBF01-AMD031','QBF01-U0167-Q02-S02','AHM의최종판단유보와주체적평가구별은평가의범위·확정수준차이이다.두단계간산출정보전달이현재장면의직접연산이아니므로단계구분연결만제거하고범위이동및구체판단을보존한다.')]
assert not {x[0] for x in fixes}&{x['amendment_id'] for x in rows(OUT/'scene_amendments.jsonl')}
append('scene_amendments.jsonl',[dict(amendment_id=aid,event_id=eid,reason=reason,changes=[dict(field_path='pattern_connections',old_value=ss[eid]['pattern_connections'],new_value=[p for p in ss[eid]['pattern_connections'] if p['pattern_id']!='단계구분'])]) for aid,eid,reason in fixes])
q=qs['U0167-Q02']
assert not any(x['amendment_id']=='QBF01-QAMD004' for x in rows(OUT/'question_amendments.jsonl'))
append('question_amendments.jsonl',[dict(amendment_id='QBF01-QAMD004',unique_question='U0167-Q02',reason='AHM②설명중읽기전완료판단이라는압축표현을원문에맞게완독전최종판단유보로명료화.정답·최초판단·장면추론불변.',changes=[dict(field_path='option_checks.1.reasoning',old_value=q['option_checks'][1]['reasoning'],new_value='② 글을 다 읽기 전까지 최종 판단을 유보할 필요가 있으므로,책을 다 읽은 후로 미룰 수 없다는 선지는 반대다.')])])
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV040','pattern_ids':['BFP011','하한정확값','집계정보손실','수치표상'],'evidence_event_ids':['QBF01-U0163-Q01-S01'],
 'finding':'AGV는방전중변화하는단자전압의평균을공칭전압으로정의한다.동일평균산정범위의변동개별값에서평균보다낮은값이가능함을판정하며정확시점전압은계산하지않는다.',
 'decision':'BFP011을단일KICE예시문항에근거한잠정후보로유지.명시하한과실제값구별인하한정확값,세부복원불가인집계정보손실과관련되나현재핵심은평균정의에서개별값의가능위치를긍정적으로얻음이다.그래프축판독은없다.평균산정방식·비상수조건을넘어확장하지않음.',
 'next_counterexample':'교육용가상자료:모든값이3이면평균3보다낮은값은없다.값2와4의평균3은하한이아니다.한구간평균을다른구간값과비교하면내부위치결론은보장되지않는다.기출의실측전압이나시계열을복원한값이아니다.',
 'educational_use':'평균의대상과산정범위·실제변동여부를먼저적는다.평균을최소나항상유지값으로바꾸는선지를만들되정확시점값까지요구하지않는다.'},
 {'development_id':'QBF01-DEV041','pattern_ids':['단계구분','관계귀속','부분전체','범위이동'],'evidence_event_ids':['QBF01-U0164-Q01-S01','QBF01-U0165-Q02-S02','QBF01-U0165-Q03-S03','QBF01-U0167-Q02-S01','QBF01-U0167-Q02-S02'],
 'finding':'AHA는이미읽고이해한내용을숙고의입력으로삼으며AHM S01은인물이해→자기성찰→그성찰에근거한인물이해심화라는정보의존을명시한다.반면AHE/AHF규제장면은역할·시점·진입조건을,AHM S02는평가와최종확정의범위를판정한다.',
 'decision':'AMD029~031로후자세장면의단계구분연결제거.전자는입력으로사용되는정보가실제명시되어있어유지한다.사전/사후라는이름만으로모두값처리단계로묶지않는다.원95정의불변.후속제도사례에서출력결과를실제다음판정의입력으로쓰는구조가직접중심연산이면다시검토한다.',
 'next_counterexample':'규제단계의측정된결과값이후속판정규칙에직접입력되는실제사례는단순담당자교환과다르다.반대로정보가여러시점에등장해도각시점사이사용관계가없으면단계구분을붙이지않는다.',
 'educational_use':'앞에서만든정보/뒤에서그정보를쓰는행동을각각한줄로쓸수있는지확인한다.시간이름만있으면주체·범위판정으로기록한다.'},
 {'development_id':'QBF01-DEV042','pattern_ids':['표현기능판독','함축기능대응','관계귀속','병치인과분리','사건서술시간분리'],'evidence_event_ids':['QBF01-U0169-Q01-S01','QBF01-U0169-Q01-S03','QBF01-U0171-Q03-S01','QBF01-U0174-Q02-S01','QBF01-U0174-Q03-S01','QBF01-U0174-Q03-S02','QBF01-U0175-Q03-S01'],
 'finding':'질문·부정·인격화·대비·가정이존재한다는확인과그기능판정은다르다.AHW의없을까는앞단정을되묻고,AIM의손님은축복과같은방향이며,AIN의실제대비는나무썩음/버섯생성이지버섯생성/고통멈춤이아니다.AIR의부재가정은담의존재가방해만한다는뜻이아니다.',
 'decision':'형식존재→지시대상및관계양항→주변평가와행동→기능판정의중간단계를사례별로보존한다.시간연속을인과로강화하지않고한장면내대비를장면간대립으로옮기지않는다.관계귀속과표현기능이겹치는경우독립작업이있는지기록하며새번호를억지로분리하지않는다.',
 'next_counterexample':'같은의문형이정보요청이나확정적반문으로쓰인실제문맥,동일인격화가비판에쓰인문맥에서는현재기능이바뀐다.현재기출의의미를표현형식만으로일반규칙화하지않는다.',
 'educational_use':'수사법명만맞는오답에기능방향·대립양항·가정의부정을바꾸되직접판단근거를본문에남긴다.수정한한절의오류해소와복합선지전체의정답화는구별한다.'},
 {'development_id':'QBF01-DEV043','pattern_ids':['관계귀속','범위이동','속성분리','정보경로복원'],'evidence_event_ids':['QBF01-U0173-Q02-S02','QBF01-U0176-Q01-S01','QBF01-U0176-Q01-S02','QBF01-U0178-Q01-S02','QBF01-U0178-Q02-S01','QBF01-U0178-Q02-S02'],
 'finding':'AII는관찰시간의증상부재,AIV는전달된비하발언과부득이한공박중단,AIY는인물의생각,AIZ는급조한거짓내력과호랑이의자기자랑을각각구별한다.모두기록된내용의범위와근거주체가핵심이나단순한사실/의견이분법으로합쳐지지않는다.',
 'decision':'인물의인식이있다는진술의참과그인식내용의객관적참,발화가제시됨과그발화내력의사실성,행동중단과감정회복,독자효과와인물자기평가를사례별로구별한다.기존관계귀속·범위·속성후보를활용하고별도후보는보류한다.',
 'next_counterexample':'신뢰할수있는서술자가인물주장내용을따로확인하거나화해·감정해소를명시하면해당추론제약은달라진다.현재본문미제시는현실의영원한불가능을뜻하지않는다.',
 'educational_use':'누가안것/누가말한것/서술자가확인한것을나누고목적·인식·행동·결과의수준을보존한다.'}
])
keys=['AGV','AGW','AHA','AHE','AHF','AHI','AHM','AHT','AHW','AIC','AII','AIN','AIR','AIU','AIY']
sample=[q for q in qs.values() if set(q['case_ids'])&set(keys)]
assert len(sample)==15 and sum(len(q['scenes']) for q in sample)==32
append('semantic_sample_audits.jsonl',[{'audit_id':'QBF01-AUDIT012','batch':12,'date':'2026-10-15','sample_case_ids':keys,'sample_questions':15,'sample_scenes':32,
 'method':'주에이전트가현행15문항32장면75선지와해당원문·기존최초/후속판정·작성시직접본시각범위를대조.후보D/E를직접검토.새blind·공식원전전수재검증아님.',
 'dimensions':{'중간추론':'AGV평균의산정범위·변동조건,AGW총량/전류세기,AHI반지름→압력차→공통외부압력하내부압력→이동방향,AHM이해→성찰→이해심화의명시연결확인.','모든선지':'75선지실제검토.AHF공유기본권/규제방식차이,AII제정/수용,AIR가정의부정·부분협력/사례열거,AIU대상별기억평가,AIY정체공개/질문순서와인물인식수준확인.','후보경계':'BFP011은평균위치의단일사례잠정후보.단계구분세연결AMD029~031로제거하고정보입력의존이있는AHA/AHM S01은유지.','원문과이력':'AGW복원5행과2022예시문항전재출처한계,AIN6괄호·AIR3괄호·AIC발화범위직접관찰및hold해소순서를보존.AIR본문[C]오배치를근거로채택하지않음.AHW작품친숙성·AIY수궁가친숙성가능성을신규blind로승격하지않음.','교육출제':'반례·조건변경은실제기출과분리.AHI공통외부압력은사후명시한문맥조건이며일반이동법칙에무조건흡수하지않음.복합선지한절수정으로전체정답화를보장하지않음.'},
 'findings':[{'case':'AHE/AHF/AHM','issue':'단계구분D보다넓은역할·시점연결','resolution':'AMD029~031로후보연결축소.정답·구체판단불변.'},{'case':'AHM','issue':'②설명의압축표현으로독전/완독전혼동우려','resolution':'QAMD004로완독전최종판단유보를명료화.원raw보존.'},{'case':'AGQ','issue':'기존근접어휘불확실성','resolution':'작성시명시한19번째문항유보유지.새로운보편적어휘배타규칙확정안함.'}],
 'decision':'12배치감사완료.중대한미해결차단오류없어481번부터계속.19문항유보유지하며표본외의미무오류를보장하지않음.','unresolved_blocking_error_count':0,'limitations':'공식답전사는기존대조활용.새정답표셀전수확인·모델비교·보호자산전수hash반복검사없음.'}])
refresh();validate()
write('batch_012_validation.json',json.loads((OUT/'validation_report.json').read_text()))
c=json.loads((OUT/'checkpoint.json').read_text());write('batch_012_checkpoint.json',c)
h=json.loads((OUT/'session_handoff_20261013.json').read_text())
h.update(batch_state='001~012각40문항저장·표본감사완료.12배치15문항32장면75선지감사.481번부터13배치계속.',next_author_suggestion='author_013a.py',resume_command='python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 481 5',validation='480문항757장면현행증거·offset·hash·선지수·ID검증.보호자산전수hash재검사없음.')
h['important_corrections']+=['12배치감사15문항32장면75선지.AMD029~031단계구분연결축소,QAMD004AHM②표현명료화.DEV040~043저장.19문항유보유지.']
write('session_handoff_20261013.json',h)
