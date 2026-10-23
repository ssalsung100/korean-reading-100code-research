import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write,refresh,validate,PATTERNS
assert not any(x['audit_id']=='QBF01-AUDIT011' for x in rows(OUT/'semantic_sample_audits.jsonl'))
assert not any(x['development_id']=='QBF01-DEV036' for x in rows(OUT/'pattern_development.jsonl')),'부분실행시잔여만복구'
ss={s['event_id']:s for s in rows(OUT/'new_judgment_scenes.jsonl')}
fixes=[('QBF01-AMD026','QBF01-U0162-Q02-S03','공간기준','AGM은미토막안팎의출발·도착귀속이며공간기준D/E의서로다른좌표계·측정값변환이아니다.관계귀속과구체적인정보출처/생산/사용처구별을유지하고공간기준연결만제거한다.'),('QBF01-AMD027','QBF01-U0159-Q04-S02','비교변인','AGA는한계약의두시점에서명시된고정조건과주체별변화를적용한다.두집단조작·환경비교라는기존D/E에자동확장하지않고조건부방향·관계귀속을남긴다.다른조건일정의중간추론은보존한다.')]
amds=rows(OUT/'scene_amendments.jsonl')
# 별도명시:집합연산우선순위에의존하지않는중복검사
assert not ({x[0] for x in fixes}|{'QBF01-AMD028'}) & {x['amendment_id'] for x in amds}
new=[]
for aid,eid,remove,reason in fixes:
 new.append(dict(amendment_id=aid,event_id=eid,reason=reason,changes=[dict(field_path='pattern_connections',old_value=ss[eid]['pattern_connections'],new_value=[p for p in ss[eid]['pattern_connections'] if p['pattern_id']!=remove])]))
eid='QBF01-U0153-Q03-S01'
new.append(dict(amendment_id='QBF01-AMD028',event_id=eid,reason='AEZ의전환율6/10계산에는실제그래프축·배율·기울기판독이없다.수치표상D를모든분수계산으로넓히지않고분자반응량/분모공급량의대상귀속으로연결한다.0.6계산과전환율/생성량구별은보존.',changes=[dict(field_path='pattern_connections',old_value=ss[eid]['pattern_connections'],new_value=[{'pattern_id':'관계귀속','case_specific_fit':'전환율의분자를반응한전체암모니아,분모를공급량에귀속하여6/10을계산한다.생성수소량을어느쪽에도대입하지않는다.','definition_source':ss[eid]['pattern_connections'][0]['definition_source'],'definition_reused':True}])]))
append('scene_amendments.jsonl',new)
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV036','pattern_ids':['BFP010','집계정보손실','범위이동'],'evidence_event_ids':['QBF01-U0156-Q03-S02'],
 'finding':'AGT는원RGB영상의정보와25개골격연결점에남는정보를구별한다.얼굴표정에해당하는세부점이없다는출력형식의제약이직접근거다.기존집계정보손실은여러특성을단일합계·거리·점수로합치는D를갖는다.',
 'decision':'입력정보가산출물에모두보존되지않는상위공통성은인정하되선택된다차원연결점출력을단일수치집계로기록하지않는다.BFP010을단일KICE사례잠정후보로분리하며원95정의불변.후속실제사례에서표상선택/집계의통합·하위분리를검토한다.',
 'next_counterexample':'교육용변형:표정차이를충분히구별하는눈·입연결점을추가하거나원영상을별도출력하면해당정보부재판정은다시검사해야한다.장치전체의얼굴처리불능으로확장하면안된다.새blind·실제장치실험아님.',
 'educational_use':'입력정보/처리방법/최종출력항목/현재물은정보를네칸으로대응한다.정보가사용되었다와출력에서복원가능하다를나눈다.'},
 {'development_id':'QBF01-DEV037','pattern_ids':['하한정확값','관계귀속','부분전체'],'evidence_event_ids':['QBF01-U0153-Q02-S01','QBF01-U0153-Q03-S02','QBF01-U0162-Q02-S03','QBF01-U0162-Q02-S04'],
 'finding':'AEY는추가수소최소6개>암모니아정확3개만으로충분하며외부분자식이필요없다.AEZ는거의부반응없음과상당부반응을반영한근사비교로정확생성량을확정하지않는다.AGM은정보출처≠생산장소,전체계승≠자동인과강도순위라는연결한계가있다.',
 'decision':'직접근거만으로충분한최소증명,지문이허용한근사비교,누락된연결전제를필요로하는의도해석을분리한다.AGM의공식④·최초④는유지하되두추론한계를유보한다.정답일치를모든중간전제의입증으로사용하지않는다.',
 'next_counterexample':'정보출처와생산위치를명시적으로분리한실제사례또는인과성강도순위를직접정의한사례와비교한다.이번에는외부번역·수송기구나인과강도공식을추가하지않는다.',
 'educational_use':'원문근거/중간해석/추가가정세표시를구별한다.AGM의외부합성·강도순위규칙추가는기출관측이아닌교육용보강으로만기록한다.'},
 {'development_id':'QBF01-DEV038','pattern_ids':['공간기준','비교변인','수치표상','관계귀속','조건부방향'],'evidence_event_ids':['QBF01-U0162-Q02-S03','QBF01-U0159-Q04-S02','QBF01-U0153-Q03-S01','QBF01-U0157-Q04-S01'],
 'finding':'막안팎이동은좌표계변환이아니고,한계약의시점별고정조건적용은두집단실험비교와다르며,전환율분수계산은그림축판독과다르다.AFO는실제시간축에서초기방향과최종기준선을읽으므로수치표상적용이확인된다.',
 'decision':'AMD026~028로현행후보연결만축소·교체.이름의넓은연상보다D/E를우선한다.개별행동과수치계산을버리지않고관계귀속·조건부방향에남긴다.원95정의불변.',
 'next_counterexample':'같은거리·속도를실제로다른좌표계에서비교하는경우,실제두집단조건을대조하는경우,같은비율이그래프의배율·기울기로표현되는경우와구별한다.',
 'educational_use':'패턴명을붙이기전무엇을어떤표상·단위·조건에서조작했는지문장으로쓴다.'},
 {'development_id':'QBF01-DEV039','pattern_ids':['속성분리','관계귀속','행위결과분리','규칙우선순위'],'evidence_event_ids':['QBF01-U0155-Q04-S02','QBF01-U0158-Q04-S01','QBF01-U0160-Q01-S03','QBF01-U0160-Q03-S01','QBF01-U0161-Q04-S01'],
 'finding':'AFI는기본음유지와음색변화,AFU는분포차이와통합주체,AGC/AGE는제재·효력·급부·반환,AGK는존재·위치·개입을각각구별한다.공통점하나에서모든속성동일성으로넘어가는오류를막지만각사례의조건은다르다.',
 'decision':'공통교육행동은속성별근거분리로남기되전역적으로모든축이독립이라는통계·형이상학명제를추가하지않는다.법적효과는명시된우선규정·예외에따라다시연결되므로그의존관계도보존한다.',
 'next_counterexample':'한속성의변화가다른속성변화를필연적으로함축하는규칙이직접주어진사례에서는그연결을적용한다.항상분리하여무관하다고하는반대오류를검사한다.',
 'educational_use':'무엇이같고무엇이다른지를명사와조건으로기록한다.반환청구가능을실제반환완료로,외부위치를외부영향으로바꾸지않는다.'}
])
keys=['ACU','AEY','AEZ','AFI','AGT','AFO','AFU','AGA','AGC','AGE','AGM','AGN','AGB']
qs=[q for q in rows(OUT/'current_question_reviews.jsonl') if set(q['case_ids'])&set(keys)]
assert len(qs)==13 and sum(len(q['scenes']) for q in qs)==28
append('semantic_sample_audits.jsonl',[{'audit_id':'QBF01-AUDIT011','batch':11,'date':'2026-10-15','sample_case_ids':keys,'sample_questions':13,'sample_scenes':28,
 'method':'주에이전트가현행13문항28장면65선지와원문·기존풀이·선택독립판정을대조.작성시직접읽은시각자료와저장관찰을활용하며새blind·전수원전재검증아님.',
 'dimensions':{'중간추론':'AEY의하한증명,AEZ의공통공급량·근사상한,AFI의최소진동수식별후세기비교,AFO의초기방향후장기기준선,AGA의2011.8비교기준·X/Z분리를확인.','모든선지':'65개실제검토.조합형AFU는4항및5행을검토하고긍정/부정두대안경로보존.ACU의실제상대입장왜곡,AGT의전체장치/골격출력범위구별확인.','후보경계':'BFP010은출력항목선택후보로단일수치집계와구별.AMD026~028적용.실제필요조건AGM③와단순역할/강도전도를구별.','원문과이력':'ACU·AFI·AGT·AFO시각관찰기록과기존hold→유효최초순서보존.AFU기존HWPX선택표전사연결을신규이미지판독으로기록하지않음.AGB근접어휘불확실성,AGM기존합성위치한계와사후구체화구별.','교육출제':'가상조건변경은기출관측과분리.정확값과하한,근사와엄밀한경계를구별.AFU조합항목변경시유일정답재설계필요.AGM연결전제추가를교육용보강으로표시.'},
 'findings':[{'case':'AGM/AGA/AEZ','issue':'후보이름과기존D/E의범위차이','resolution':'AMD026~028로연결수정.원raw·정답·구체추론보존.'},{'case':'AGB','issue':'최초①/③근접어휘유보','resolution':'현행유보추가.공식①유지·범용배타경계확정하지않음.'},{'case':'AGM','issue':'④막통과에필요한생산위치연결과⑤인과강도순위의명시근거한계','resolution':'직접근거와의도해석을분리한2유보저장.공식④·최초④유지.추론한계를숨기는중대한오류는해소했고범용규칙승격은보류.'},{'case':'AGL','issue':'author011h의인용에서또는세포내공생설누락으로검증중단','resolution':'436~437저장후미저장438~440만remaining스크립트로복구.중복없음.전체재실행금지.'}],
 'decision':'11배치감사완료.현행18문항유보를유지하며중대한미해결차단오류없어441번부터계속.표본외의미무오류를보장하지않음.','unresolved_blocking_error_count':0,'limitations':'기존정답전사를활용했으며공식답표독립전수대조가아니다.모델비교·보호자산전수hash반복검사없음.'}])
refresh();validate()
write('batch_011_validation.json',json.loads((OUT/'validation_report.json').read_text()))
c=json.loads((OUT/'checkpoint.json').read_text());write('batch_011_checkpoint.json',c)
h=json.loads((OUT/'session_handoff_20261013.json').read_text())
h.update(batch_state='001~011 각40문항저장·표본감사완료.11배치13문항28장면65선지감사.441번부터12배치계속.',next_author_suggestion='author_012a.py',resume_command='python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 441 5',validation='440문항686장면현행증거·offset·hash·선지수·ID검증.보호자산전수hash재검사없음.')
h['important_corrections']+=['11배치감사13문항28장면65선지완료.AMD026AGM공간기준제거,AMD027AGA비교변인제거,AMD028AEZ수치표상→관계귀속.DEV036~039저장.현행18문항유보.']
write('session_handoff_20261013.json',h)
