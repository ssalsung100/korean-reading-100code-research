import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write
from resume_support_20261015_04 import finish
assert not any(a['audit_id']=='QBF01-AUDIT016' for a in rows(OUT/'semantic_sample_audits.jsonl'))
assert not any(a['amendment_id'] in ['QBF01-AMD044','QBF01-AMD045'] for a in rows(OUT/'scene_amendments.jsonl'))
qs=rows(OUT/'current_question_reviews.jsonl');ss={s['event_id']:s for s in rows(OUT/'new_judgment_scenes.jsonl')}
assert sum(r['batch_number']==16 for r in qs)==40
fixes=[('QBF01-AMD044','QBF01-U0323-Q03-S01','기준내부검사','AZS는 이상적 욕구자라는 새 판정 기준이 어떤 문제를 해결하도록 고안되었는지 복원한다. 정해진 기준에 구체 적용 결과가 맞는지 검사하는 기존 D/E와 같은 행동으로 확정하지 않는다. 기준의 선별 기능 설명과 관계귀속은 보존한다.'),('QBF01-AMD045','QBF01-U0366-Q02-S01','단계구분','BET의 직접 연산은 전체 충돌 과정 이전에 변성의 고압 조건이 이미 충족됨을 찾아 다른 경계 유형에 적용하는 것이다. 단계별 처리 값과 다음 단계의 사용을 구별하는 기존 D/E에 단순 과정 구획만으로 배정하지 않는다. 발생 시점의 추론과 분류기준 연결은 유지한다.')]
am=[]
for aid,eid,pid,reason in fixes:
 old=ss[eid]['pattern_connections'];new=[p for p in old if p['pattern_id']!=pid];assert len(old)-len(new)==1
 am.append({'amendment_id':aid,'event_id':eid,'reason':reason,'changes':[{'field_path':'pattern_connections','old_value':old,'new_value':new}]})
append('scene_amendments.jsonl',am)
write('audit_016_selected_checks.json',{'scope':'선택한새분석의수치·구조검산. 실제측정아님.','BAK':{'base_shift':500-498,'g':[500,496],'n':[502,494],'d':[None,496],'answer':1},'BAL':{'resonant_photon_momentum_Li_over_Rb':780/670,'same_speed_atom_momentum_Li_over_Rb':6.94/85.47,'limit':'정지공명표의대응비율. 실제레이저설정파장의독립측정아님. 종간냉각비교는동등한운동·보정조건.'},'BEM':{'block_sizes':[1,2],'channel_rates':[2,4],'periods':[1/2,2/4],'both_at_least_twice_playback':True,'double_period':False,'inherited_hold':True},'BFP006':{'NL':'분석명제→동의성→필연성→분석명제','BEX':'개념확실성→신실재→개념확실성','shared_operation':'정당화의독립근거확보전원점회귀검사','distinct_unique_questions':2,'KICE_anchor_recounted':False},'pass':True})
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV057','pattern_ids':['BFP006','근거망복원','되먹임고리'],'evidence_event_ids':['QBF01-U0094-Q02-S01','QBF01-U0099-Q02-S03','QBF01-U0100-Q01-S02','QBF01-U0367-Q03-S01'],
 'finding':'NL은 분석명제→동의성→필연성→분석명제의 세 단계 회귀이고,BEX는 개념확실성→신실재→개념확실성의 두 단계 회귀다. 둘 다 실제 변화의 되먹임이 아니라 정당화 근거의 독립성 결여를 검사한다.',
 'decision':'BFP006은 기존KICE NL과 신규LEET BEX의 고유2문항에서 같은 연산이 확인된 잠정 후보로 연구 상태를 갱신한다. 원 후보 정의와95개 후보는 수정하지 않는다. 기존DEV017의OK/ON 대비,즉 인과 강화와 시간적 학습 고리는 정당화 회귀와 구별한다는 경계도 유지한다.',
 'next_counterexample':'원점으로 돌아오더라도 독립된 외부 근거가 있어 그 근거만으로 주장을 정당화할 수 있는 경우,상호 정의만 하는 경우,근거가 끝없이 늘거나 절대 명제에서 멈추는 경우를 분리해야 한다.',
 'educational_use':'명제 내용보다 무엇이 무엇을 정당화하는지 화살표로 적고 독립 근거를 얻기 전에 출발점이 재사용되는지 묻는다. 두 단계와 세 단계 변형을 제작하되 명제의 실제 거짓을 결론으로 요구하지 않는다.',
 'supersedes':'QBF01-DEV017','correction_reason':'단일NL사례라는이전상태를새LEET BEX직접대조에따라갱신. NL은근거anchor로만읽었고새문항·장면으로재계수하지않음.'},
 {'development_id':'QBF01-DEV058','pattern_ids':['비교변인','조건부방향','관계귀속'],'evidence_event_ids':['QBF01-U0309-Q01-S02','QBF01-U0364-Q01-S01','QBF01-U0329-Q03-S01','QBF01-U0329-Q04-S01','QBF01-U0329-Q04-S02'],
 'finding':'AXY의길이비와BEM의주기비는비례계수가동일해야단순역비·배수로결정된다. BAK는동일속력이어도방향과활성음원이달라지면감지값이다르며,BAL은원자운동량과광자운동량의입력자체가다르다.',
 'decision':'BEM의기존동일전송률유보를보완연구에승계한다. 2배이상의하한을같은2배로바꾸지않는다. BAL은공명표기준과같은운동조건의비교를유지하며임의의상이한속도·설정까지보편화하지않는다. 공통계수검사와서로다른물리량의식선택은구별한다.',
 'next_counterexample':'블록1/2와전송률2/4이면주기.5/.5로같다. BAK의v를2v로바꾸면편이는2에서4가되지만공명일치조건은오히려깨진다. 개선변수의증가가모든목표에유리한것은아니다.',
 'educational_use':'식에서소거하는항을표시하여동일조건을확인한다. 설정값·감지값·목표값은다른기호를사용하고조건변경후정답유일성을다시검사한다.'},
 {'development_id':'QBF01-DEV059','pattern_ids':['범위이동','강도보존','관계귀속','필요요건역전금지'],'evidence_event_ids':['QBF01-U0320-Q02-S01','QBF01-U0326-Q01-S01','QBF01-U0326-Q03-S02','QBF01-U0330-Q02-S01','QBF01-U0363-Q02-S01'],
 'finding':'특정입증요구를완화함은무입증과다르며,절차부재로규칙적용범위밖인경우는절차존재하예외와다르다. 원이론의충족충분성과비판자의충분성부정도분리해야한다. 위험의한경로를줄이는대책은모든노출차단과다르다.',
 'decision':'각사례의전건·예외·부정대상·출력강도를구체적으로보존한다. BAB의배제사유부재를최종배상확정으로전환하지않는다. BEK의이식에의한키도난방지이득은인정하되무차별판독의직접차단과구별한다.',
 'next_counterexample':'절차가실제로있고본인이이용하지않은사례로바꾸면BAB의범위밖논리는적용되지않는다. 선별정보제공이더라도인가된리더가정보를오용하는문제까지자동해결하지않는다.',
 'educational_use':'규칙의입구조건·적용뒤의예외·그후의최종요건을별도로쓴다. 같은결론표현을유지한채근거범위만바꾼오답을제작하고원문이허용한강도를명시한다.'},
 {'development_id':'QBF01-DEV060','pattern_ids':['기준내부검사','단계구분','분류기준','관계귀속'],'evidence_event_ids':['QBF01-U0323-Q03-S01','QBF01-U0366-Q02-S01','QBF01-U0322-Q03-S02','QBF01-U0322-Q04-S02','QBF01-U0368-Q03-S01','QBF01-U0369-Q02-S01'],
 'finding':'기준이무슨문제를해결하는지설명하는행동과기존기준에사례를대입하는행동은같지않다. 전체과정의최종사건보다앞서생기는결과를확인하는작업도모든단계별계산과동일하지않다. 소재·명칭의유사성보다실제판정행동을먼저보존해야한다.',
 'decision':'AMD044로AZS의기준내부검사,AMD045로BET의단계구분연결을제거한다. 구체추론은보존한다. AZO/AZP에서는같은실험의유효성과참여목표에서의한계를분리하고,BFA는한계소재보다그뒤태도로분류하며,BFC는미흡함의평가의제를고정한다.',
 'next_counterexample':'한계인정뒤에현실실천이아닌절망이따르면인물형이달라진다. 같은이론을미흡하다고말해도실용화·경험검증·가치정당화중무엇을묻는지에따라다른비판이다.',
 'educational_use':'후보이름이맞아보이더라도입력·중간추론·출력·실패조건을정의와대조한다. 맞지않는연결은지우되실제사례의설명과제작아이디어는남긴다.'}
])
cases=['AZH','AZO','AZP','AZS','AZU','AZV','AZZ','BAB','BAF','BAG','BAI','BAK','BAL','BEM','BEO','BET','BEX','BFE']
sample=[r for r in qs if set(r['case_ids'])&set(cases)]
count_s=sum(len(r['scenes']) for r in sample);assert len(sample)==18 and count_s==27
append('semantic_sample_audits.jsonl',[{'audit_id':'QBF01-AUDIT016','batch':16,'date':'2026-10-15','sample_case_ids':cases,'sample_questions':18,'sample_scenes':count_s,'sample_options':90,
 'method':'주에이전트가이번및직전작성에서직접열람한원문·보기·전체선지·기존풀이를표본기록과대조. 이전세션의AZH/AZO/AZP/AZS/AZU/AZV/AZZ/BAB현행기록도다시대조. BFP006은NL원문과기존장면을추가anchor로비교하되새분석·계수하지않음. 원문복원은기존공식렌더·공식XML에한정.',
 'dimensions':{'중간추론':'BEM전송률반례,BAK진동수편이,BAL대상별운동량,AZU/AZV역치·방향·또는,AZZ/BAB가능성과규칙범위확인.','전체선지':'90선지와각보기의하위명제를검사. 선택조합과개별진릿값을구별.','원문이력':'BAI/BAK의hold·복원후풀이와BFE조건부풀이·답공개전XML복원을보존. 새파생본문4개는원본과분리.','후보경계':'AMD044~045 연결2건축소. BFP006의새실제사례를확인하되원정의불변.','출제활용':'단순배수의동일률·공명목표일치·규칙입구조건을명시. 불일치결론을모든조건의반대명제로강화하지않음.'},
 'findings':[{'case':'BEM','issue':'상이한전송률에서⑤정확두배미보장','resolution':'기존유보승계·가상모형검산·공식⑤유지.'},{'case':'BEX/NL','issue':'정당화회귀의추가구현','resolution':'고유2문항의잠정반복근거로DEV057갱신. NL재계수없음.'},{'case':'AZS/BET','issue':'후보정의보다넓은연결','resolution':'AMD044~045. 실제추론과공식답불변.'},{'case':'BAI/BAK/BAL/BFE','issue':'본문·발문기호결손과기존복원이력','resolution':'새폴더파생복원과출처연결. 최초풀이의결손상태소급변경없음.'}],
 'decision':'16배치40문항저장·감사·귀납완료. 중대한진행차단오류0. 총29문항유보유지.641부터17배치진행.','unresolved_blocking_error_count':0,'limitations':'표본외의미무오류보장아님. 보호원장전수hash·모델호출·Gitpush없음. 공식기출의제시모형밖실제과학·법률검증아님.'}])
finish('audit_016.py',cases,['16배치표본18문항27장면90선지·DEV057~060·AMD044~045완료. BFP006고유2사례확인. BEM기존유보승계.'])
c=json.loads((OUT/'checkpoint.json').read_text());c.update(last_saved_author='author_016m.py',last_saved_audit='audit_016.py',next_sample_audit_at=680);write('checkpoint.json',c);write('batch_016_checkpoint.json',c)
write('batch_016_validation.json',json.loads((OUT/'audit_016_validation.json').read_text()))
print('16배치 감사 완료. 다음641. 유보29.')
