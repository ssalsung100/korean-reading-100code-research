import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write
from resume_support_20261015 import finish
assert not any(a['audit_id']=='QBF01-AUDIT015' for a in rows(OUT/'semantic_sample_audits.jsonl'))
assert not any(a['amendment_id'] in ['QBF01-AMD042','QBF01-AMD043'] for a in rows(OUT/'scene_amendments.jsonl')),'부분저장시잔여만복구'
qs=rows(OUT/'current_question_reviews.jsonl');ss={s['event_id']:s for s in rows(OUT/'new_judgment_scenes.jsonl')}
assert len([q for q in qs if q['batch_number']==15])==40
fixes=[('QBF01-AMD042','QBF01-U0306-Q01-S02','설명해상도','AXP의 구조 식별·재현 대상 인식·등장 이유의 설명은 과제의 목적어가 다르다. 원인 명명과 구체 작동 과정의 설명 깊이를 구별하는 기존 설명해상도 D/E와 완전히 같은 행동으로 계수하지 않는다. 관계귀속과 사례별 실제 설명은 유지한다.'),('QBF01-AMD043','QBF01-U0303-Q02-S01','대립가능성','AXG는 물이라는 명시 사례에 비이력과 과냉각이 공존함을 확인한다. 두 명제의 참/거짓 조합을 통해 대립 관계 전체를 분류하는 기존 대립가능성의 D/E와는 요구 연산이 다르다. 분류기준 연결과 공존 사례 설명을 유지한다.')]
am=[]
for aid,eid,pid,reason in fixes:
 old=ss[eid]['pattern_connections'];new=[p for p in old if p['pattern_id']!=pid]
 assert len(new)==len(old)-1
 am.append({'amendment_id':aid,'event_id':eid,'reason':reason,'changes':[{'field_path':'pattern_connections','old_value':old,'new_value':new}]})
append('scene_amendments.jsonl',am)
assert not any(d['development_id']=='QBF01-DEV052' for d in rows(OUT/'pattern_development.jsonl'))
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV052','pattern_ids':['관측합성','부분전체','비교변인','조건부방향','잔여량역산'],'evidence_event_ids':['QBF01-U0301-Q03-S02','QBF01-U0309-Q01-S02','QBF01-U0313-Q02-S01','QBF01-U0313-Q02-S02','QBF01-U0313-Q03-S01','QBF01-U0313-Q03-S02'],
 'finding':'평균 밀도 상승에서 층의 절대 두께,주파수 역비에서 안테나 길이비,부분 손실에서 순두께,한 유출항에서 유입속도를 얻으려면 서로 다른 추가 조건이 필요하다. 반면 C가 고정된D/(C+D)의 방향은 분모에도D가 있다는 이유만으로 유보할 필요가 없다.',
 'decision':'AXB의 부피·경계 자유도 유보,AXY의 같은 설계계수 조건,AYN의S/순두께 해석 구별을 유지한다. AYM의 표본 외삽 편향과 R 단조성은 명시된 고정 조건 아래 보존한다. 모두를 단일 미확정유지 후보로 합치지 않는다.',
 'verification_file':'audit_015_countermodel_checks.json','next_counterexample':'같은 평균 상승이어도 전체 부피가 줄면 고밀도 성분의 절대 두께는 줄 수 있다. 같은 역비라도 두 계수가 다르면 비율은 달라진다. 손실D가 커져도 유입이 더 크면E는 양수일 수 있다. 가상 모형이며 실제 관측값 아님.',
 'educational_use':'관측량의 이름 옆에 전체/부분·면적당/총량·현재/변화량을 쓰고 식에 들어가는 미지변수를 열거한다. 제작에서는 필요한 고정 조건을 추가하되 다른 관측 조건과 양립하는지 다시 확인한다.'},
 {'development_id':'QBF01-DEV053','pattern_ids':['경로의존','직전상태갱신','관계귀속'],'evidence_event_ids':['QBF01-U0303-Q02-S02','QBF01-U0303-Q03-S01','QBF01-U0317-Q01-S01','QBF01-U0317-Q02-S01'],
 'finding':'AXG/AXH는 현재 입력이 같아도 과거 상태와 접근 방향에 따라 상태 가지가 달라진다. AYX는 한 번의 기록에서B_next=NOT A_sampled이며 이후A가 재계산된다. AYY의 내부 저장 고리는 두 번 반전으로 상태를 유지하지만 외부 고리는 새 입력과 현재 상태로 다음 상태를 만든다.',
 'decision':'경로의존과 직전상태갱신은 관련되지만 각각 주어진 이력으로 가지를 고르는 행동과 전이 규칙에 따라 갱신하는 행동으로 구별한다. AYX 원기록의 반전 설명은 기록 직전A와 다음B로 한정한다. 피드백이라는 소재만으로 되먹임고리에 연결하지 않는다.',
 'next_counterexample':'AYX 예시에서C=1이면현재A와B는같고C=0이면반대이다. 따라서 항상같음도항상동시반대도성립하지않는다. AXH에서β바깥은단일가지지만α~β는이력이필요하므로모든입력에서복수상태를주장하지않는다.',
 'educational_use':'그림에는출발가지와이동방향을,전이식에는t와t+1을표시한다. 같은입력의다른결과와한입력이후의새상태를구별하는문항을쌍으로설계한다.'},
 {'development_id':'QBF01-DEV054','pattern_ids':['설명해상도','관계귀속','공통차별근거'],'evidence_event_ids':['QBF01-U0306-Q01-S02','QBF01-U0306-Q03-S01','QBF01-U0312-Q01-S02','QBF01-U0318-Q02-S02'],
 'finding':'음의 구성 식별과 선택 이유 해명,지성의 정점과 예술미의 정점,금지의 보호 효과와 법적 효력은 같은 평가어 아래 목적어 또는 기준이 다르다. 이를 모두 설명의 상세도 부족으로 묶으면 실제 문항 차이가 사라진다.',
 'decision':'AMD042로AXP의설명해상도연결을제거한다. 구체적인과제구별과교육·출제설명은보존한다. 새보편후보로즉시승격하지않고관계귀속이라는공통수준아래각사례의중간연산차이를남긴다.',
 'next_counterexample':'제목을몰라도다섯음을알아들을수있다. 유럽의지성적완성을주장하면서그리스의미적우월을말할수있다. 짧은경업금지는기업보호기간은짧게하지만제한의과도성도줄일수있다.',
 'educational_use':'이해·높다·효력이란말뒤의생략된목적어와판정기준을써보게한다. 오답은표면술어를유지한채목적어를바꾸는방식으로설계하되정답의유일성을다시점검한다.'},
 {'development_id':'QBF01-DEV055','pattern_ids':['분류기준','속성분리','관계귀속','대립가능성'],'evidence_event_ids':['QBF01-U0303-Q02-S01','QBF01-U0308-Q03-S01','QBF01-U0312-Q02-S01','QBF01-U0312-Q02-S02','QBF01-U0314-Q03-S01','QBF01-U0316-Q01-S01','QBF01-U0316-Q03-S02'],
 'finding':'분류할때이름·절차어·단일속성은지름길이될수도있지만잘못된기준을불러올수있다. 입증이라는단어보다입증대상,고전주의라는이름보다문명단계·장르,권한축소하나보다제도묶음,종이름보다인격속성이필요하다.',
 'decision':'같은분류기준후보에연결하더라도각입력속성과탈락조건을구체적으로보존한다. AYQ는빠진초기상태를공식렌더로복원했고유지칸의기준을명시한다. AMD043으로AXG의대립가능성연결을제거하여공존한사례와명제관계전체분류를구별한다.',
 'next_counterexample':'같은입증절차여도내심을입증하면의사주의일수있다. 같은권한축소여도기율과선거제가다르면미국식이아닐수있다. 같은동물범주여도유인원과물고기의인격속성은다르다.',
 'educational_use':'사례명칭을가린채속성표로먼저분류한다. 변경표는초기상태를대입해완성한다. 공존가능성문항을명제의모순·반대관계문항으로확장하려면추가진리조합을검토해야한다.'},
 {'development_id':'QBF01-DEV056','pattern_ids':['강도보존','지지방향','부분전체','포함반례'],'evidence_event_ids':['QBF01-U0311-Q01-S01','QBF01-U0311-Q02-S01','QBF01-U0313-Q03-S02','QBF01-U0318-Q02-S01','QBF01-U0318-Q03-S01'],
 'finding':'보장되지않음은불가능이아니고,악화가능성을보이는사례는모든상황의악화를뜻하지않으며,효력에부정적인사정은최종무효의충분조건이아니다. 중간효과와최종판정을구별해야할곳이경제·물리·법제문항에반복된다.',
 'decision':'AYE의조건수/전체효율,AYF의실제전후생산비,AZB의형량방향,AZC의자기결정제약을각각의근거로유지한다. 모든가능성제한을같은한줄설명으로복제하지않는다. 기존95후보정의와BFP001~013은수정하지않는다.',
 'next_counterexample':'AYF③의C최저와A/B양쪽고비용만으로A→B개선·악화모두구성가능하다. AZC의자기결정제약부재만으로기간·범위등다른요건을지운필연유효는도출되지않는다.',
 'educational_use':'판단요구가방향인지가능성인지최종확정인지먼저표시하고그강도를충족하는근거를찾는다. 선지하나의진릿값을바꾸는수정과문항전체의정답유일성보존을분리해검사한다.'}
])
cases=['AXB','AXG','AXH','AXP','AXR','AXY','AYE','AYF','AYI','AYK','AYM','AYN','AYQ','AYW','AYX','AYY','AZB','AZC']
sample=[q for q in qs if set(q['case_ids'])&set(cases)]
assert len(sample)==18 and sum(len(q['scenes']) for q in sample)==29
append('semantic_sample_audits.jsonl',[{'audit_id':'QBF01-AUDIT015','batch':15,'date':'2026-10-15','sample_case_ids':cases,'sample_questions':18,'sample_scenes':29,'sample_options':90,
 'method':'주 에이전트가 이번 작성분의 직접 원문·전체선지·기존풀이 열람과 선택한 이전배치내 문항의 재대조를 결합하여 표본 감사. AXB·AXG·AXH 원문과현재풀이·보기,AXP 전체선지를 다시 확인. AXH의 기존 파생 그래프 직접 판독. 후보D/E대조. 검산은선택한가상모형4종에한정.',
 'dimensions':{'중간추론':'평균/절대두께·공통계수·손실/순변화·전이시점·형량방향을집중점검.','모든선지':'표본90선지와해당보기각항목을확인. 조합선지는ㄱㄴㄷ의개별근거와조합오류를함께보존.','후보경계':'AMD042~043으로설명해상도·대립가능성의과잉연결2건제거. 새후보ID발급없음. 정의95개와기존후보13개불변.','원문과이력':'G348기호·분수와AYQ초기상태의신규복원은별도파일. AXHα/β는기존파생본사용. AYK/T는별도풀이둘을연결하고고유1회계수. 기존blind·hold·노출이력불변.','교육출제':'가상반례와공식관측분리. 개별선지진릿값변경과복수정답위험을표시. 실제법률·정책·윤리처방으로외삽하지않음.'},
 'findings':[{'case':'AXB','issue':'평균상승에서반지각절대두께의유일역산','resolution':'기존동심층모형의질량·정규관성·외곽관성·평균밀도수치를재계산하여유보유지. 공식③유지.'},{'case':'AXY','issue':'원문계수범위에서④약3배의비교조건','resolution':'같은k일때2.875,독립k범위에서는1.4375~5.75. 공식③유지·동일설계가정명시.'},{'case':'AYN','issue':'②의S해석과전체순두께해석차이','resolution':'바닥융해라는의도해석과공식②유지. 전체순두께로의일반화만유보.'},{'case':'AYX/AYY','issue':'피드백반전의위치·시점과저장/변경기능','resolution':'4상태표에서B_next=NOT A_sampled확인. 동시A/B는C에따라같거나반대이므로기존반전설명을시점관계로정밀화.'},{'case':'AXP/AXG','issue':'이름유사성에따른후보과잉연결','resolution':'AMD042~043. 실제추론·원raw·공식답유지.'}],
 'decision':'15배치40문항저장·표본감사·귀납완료. 중대한진행차단오류0. 유보28문항유지. 601번부터16배치계속.','unresolved_blocking_error_count':0,'limitations':'표본외의미무오류보장아님. 원문기호복원은선택한자료에한정. 보호원장전수hash·기존전체문항재분석·다른모델·Gitpush없음.'}])
finish('audit_015.py',cases,['15배치감사18문항29장면90선지·DEV052~056·AMD042~043 완료. AXB·AXY·AYN유보유지,AYX시점정밀화. 600문항960장면·601번재개.'])
c=json.loads((OUT/'checkpoint.json').read_text());c.update(last_saved_author='author_015n.py',last_saved_audit='audit_015.py',next_sample_audit_at=640,current_session_other_models_called=False);write('checkpoint.json',c);write('batch_015_checkpoint.json',c)
write('batch_015_validation.json',json.loads((OUT/'audit_015_validation.json').read_text()))
write('session_progress_20261015_03.json',{'start_reviewed':573,'start_scenes':922,'current_reviewed':600,'current_scenes':960,'new_questions':27,'new_scenes':38,'last_saved_author':'author_015n.py','last_audit':'audit_015.py','next':{'order':c['next_order'],'question':c['next_question'],'cases':c['next_case_ids']},'unresolved':28,'new_holds':['AXY','AYN'],'source_repairs':['G348_source_repair_history.json','AYQ_view_restored.json'],'new_candidates':[],'new_developments':['QBF01-DEV052','QBF01-DEV053','QBF01-DEV054','QBF01-DEV055','QBF01-DEV056'],'next_audit_at':640,'status':'연속진행중'})
