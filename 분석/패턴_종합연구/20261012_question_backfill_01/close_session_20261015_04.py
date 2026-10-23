"""저장된 이번 연구분의 검증 결과를 모아 인계한다. 재실행 금지."""
import sys,json,collections
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,write,TARGETS
assert not (OUT/'session_handoff_20261015_04.json').exists(),'이미 인계 저장됨'
c=json.loads((OUT/'checkpoint.json').read_text())
assert c['reviewed_questions']==646 and c['new_scene_count']==1022 and c['next_order']==647
assert sum(x['unresolved_questions'] for x in c['by_exam'].values())==32
expected=[q['unique_question'] for q in TARGETS[618:646]]
selected=[r for r in rows(OUT/'raw_question_reviews.jsonl') if r['unique_question'] in set(expected)]
assert [r['unique_question'] for r in selected]==expected
assert len(selected)==28 and sum(len(r['scenes']) for r in selected)==36
assert sum(len(r['option_checks']) for r in selected)==140
assert all(v==1 for v in collections.Counter(r['unique_question'] for r in selected).values())
ids=[s['event_id'] for r in selected for s in r['scenes']];assert len(ids)==len(set(ids))
authors=['author_016'+x+'.py' for x in 'ghijklm']+['author_017a.py','author_017b.py']
vs=[json.loads((OUT/a.replace('.py','_validation.json')).read_text()) for a in authors]
assert all(v['pass'] and not v['errors'] for v in vs)
assert sum(v['questions'] for v in vs)==28 and sum(v['scenes'] for v in vs)==36
au=rows(OUT/'semantic_sample_audits.jsonl');assert au[-1]['batch']==16
av=json.loads((OUT/'audit_016_validation.json').read_text());assert av['pass']
validation={'scope':'이번619~646의저장ID·계수·선지수와각author의인용구간검증결과를확인. 전체원장SHA검증아님.','questions':28,'scenes':36,'options':140,'duplicate_questions':[],'duplicate_scene_ids':[],'author_validations':[a.replace('.py','_validation.json') for a in authors],'all_author_validations_passed':True,'sample_audit':{'batch':16,'questions':18,'scenes':27,'options':90,'validation':'audit_016_validation.json'},'partial_save_recovery':{'author':'author_016k.py','already_saved':['BEQ','BET'],'recovered_only':['BEU'],'script':'recover_016k.py','duplicates':0},'pass':True}
write('session_validation_20261015_04.json',validation)
reason='이번 응답의 컨텍스트·작성 작업 예산에 맞춘 중간 인계.16배치 완료 후 감사·귀납을 거쳐17배치6문항을 계속 분석했다. 구체 quota 잔여치와 runtime emergency 경고는 관측되지 않았으며 값을 추정하지 않는다.'
h={
 'date':'2026-10-15','run':'네 번째 이어서 실행','status':'진행 중·중간 인계 저장','stop_reason':reason,
 'authoritative_checkpoint':'checkpoint.json','previous_session_handoff':'session_handoff_20261015_03.json',
 'start':{'reviewed_questions':618,'scenes':986,'next_order':619,'next_question':'U0328-Q01','last_saved_author':'author_016f.py'},
 'session_completed':{'orders':[619,646],'questions_added':28,'scenes_added':36,'option_rows_checked':140,'exam':'LEET','new_raw_duplicates':0,'scripts':authors},
 'current':{'reviewed_questions':646,'target_questions':1077,'new_scenes':1022,'remaining_questions':431,'by_exam':c['by_exam'],'unresolved_questions':32},
 'last_saved_author':'author_017b.py','last_saved_question':'U0373-Q03','last_saved_case':'BFP','last_audit':'audit_016.py','audited_batches':list(range(1,17)),
 'audit_16':{'sample_questions':18,'sample_scenes':27,'sample_options':90,'amendments':['QBF01-AMD044','QBF01-AMD045'],'developments':['QBF01-DEV057','QBF01-DEV058','QBF01-DEV059','QBF01-DEV060'],'blocking_errors':0,'verification':'audit_016_selected_checks.json','anchor':'KICE NL은 BFP006의 기존 근거와 신규 BEX를 비교하는 데만 사용. 신규 분석·장면 계수 없음.'},
 'active_batch':{'number':17,'saved_questions':6,'semantic_sample_audit_complete':False,'next_audit_at_reviewed_questions':680},
 'candidate_update':{'new_ids':[],'BFP006':'기존KICE NL(U0094-Q02-S01)과신규LEET BEX(U0367-Q03-S01)의고유2문항에서정당화원점회귀를확인. DEV057이DEV017을supersede하며경계는보존. 원new_pattern_candidates정의와95후보는수정하지않음.','qualification':'반복구현의잠정근거이며최종분류·보편성확정아님. 독립외부근거가있는고리·상호정의·물리적되먹임·무한소급·절대종결과구별.'},
 'inherited_holds_added_to_backfill':[
 {'question':'U0364-Q01','case':'BEM','official_answer':5,'issue':'블록두배→주기두배는같은채널전송률조건이필요. 기존blind/answer의유보를승계.','verification':'BEM_rate_counterexample.json','next':'680감사에서조건누락사례와비교. r하한2배이상과동일률을구별.'},
 {'question':'U0371-Q03','case':'BFJ','official_answer':5,'issue':'세비교모두가설검증에관련되나외기·체격·대사통제가없으면유일한인과입증으로확대불가. 기존유보승계.','next':'실험관련성·예측방향·인과식별의조건을구별.'},
 {'question':'U0372-Q03','case':'BFM','official_answer':3,'issue':'②중국관사용의장소를조선으로제한해야풍기차이논거와연결. 선지장소생략유보승계.','next':'현행중국음일치와참된고대음의진실성을구별하고걱정/확신의목적어를고정.'},
 {'question':'U0373-Q03','case':'BFP','official_answer':1,'issue':'③제소허용의당위와공익보도의실체면책은독립된명제. 책임부정에서제소금지도출금지. 기존depth유보유지.','verification':'BFP_filing_liability_models.json','next':'①의직접지지와③의비유도성을구별.③을본문과정면모순이라단정하지않으며자연언어상적절성·유일성검토를남김.'}],
 'hold_count_note':'28→32는 새 문항에서 기존 원장이 남긴 유보4건을 보완 원장에 승계한 결과이다. 기존28문항 유보는 해소·삭제하지 않았다.',
 'source_repairs':[
 {'cases':['BAI','BAK','BAL'],'files':['BAI_source_with_restored_symbols.json','BAK_source_with_restored_symbols.json','BAL_source_with_restored_symbols.json'],'evidence':['data/기본기_연구/prepared_backlog/blind_sources/G368_restore_page13.png','data/기본기_연구/prepared_backlog/blind_sources/G368_restore_page14.png'],'repair':'기존공식렌더직접판독. 공통본문의온도·속도·분수·E1/E2/ΔE,BAI④0K,BAK보기의v/2v와음원off복원. 원본불변. 공식인쇄-273.16℃와기존물리서술을외부지식으로교정하지않음.'},
 {'cases':['BFE','BFF'],'files':['BFE_source_with_restored_target.json','BFF_source_with_restored_target.json','BFE_target_restoration_evidence.json'],'repair':'기존BFE boundary_revision이지정한공식2009 HWP_XML에서Text charshape-id=7의정당 수 산정두곳직접확인. BFE본문발문,BFF공통본문만복원. BFF보기는별도기존MD확인.'},
 {'case':'BFK','file':'BFK_visual01.png','repair':'G411_visual01.tif를RGB PNG로표시용변환해편경그림을직접판독. 내용추가·원본수정없음. 보기ㄱ~ㄹ는visual02.md.'}],
 'important_refinements':[
 'AMD044: AZS는새판정기준의해결기능을복원하는장면이므로구체적용결과와의일치검사인기준내부검사연결제거. 실제추론보존.',
 'AMD045: BET는대륙충돌이전의고압변성조건을다른경계에적용하는장면. 단계별계산값의처리와같다고보지않아단계구분연결제거. 실제과정복원보존.',
 'BFF: 선거후단순3·이항3,의회지수25/9. 미상3당득표합.1의제곱합≤.01이므로선거지수≥10/3으로의회지수와다름. 소수3당해산을이유로당시득표지수에서삭제하지않음. BFF_index_check.json 참조.',
 'BAL: 원자질량에따른p=mv와공명파장에따른광자운동량을구별. 실제흡수광자비교는동등한운동·도플러조건의해석을보존하며표의정지공명파장을실제광원설정과무조건동일시하지않음.',
 'BEK: 태그이식의키도난방지이득을부정하지않되불특정리더의직접판독차단과구별. 안전이라는말만으로대책목표를동일시하지않음.',
 'BEP: 재해관련예외지출부재와모든자연재해의전무를구별. BEU: 몇년전숫자와선후방향,인장력의추정강도를보존.',
 'BFH: 혈류의지속을전제로혈액냉각을설명하는이론과혈류공급의구동기제를설명하는이론을구별.',
 'BFP의두가상모형은현행법률판단이아닌기출명제관계검사. P→¬M에서제소당위S는결정되지않음.'
 ],
 'next':{'order':647,'unique_question':c['next_question'],'case_ids':c['next_case_ids'],'read_but_not_saved':False,'suggested_author':'author_017c.py','support_module':'resume_support_20261015_04','resume_command':'python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 647 2'},
 'save_state':{'read_but_not_saved':[],'authored_but_not_saved':[],'last_validation':'session_validation_20261015_04.json','original_new_author_validation':'author_017b_validation.json','verification_scope':'9개신규author각각의인용구간·해시·선지수·참조검증후새28문항ID·계수확인. 보호원장전수SHA검증없음.','execution_note':'author_016k는줄바꿈인용오류후BEQ/BET2문항만저장됐음을확인. 인용수정뒤recover_016k.py로BEU만저장하고3문항검증완료. author_016m의이중공백인용과author_017a의한/그인용오류는저장전preflight에서수정. 기저장author/audit재실행·중복append없음.'},
 'next_audit_focus':['680경계에서BFF부분분포상한과내각참여조건해석,BFH설명전제/대상,BFJ통제유보,BFM장소범위,BFP제소/실체유보를표본검토.','BFP006의두실제사례를유지하되같은고리표현으로모든순환·되먹임을통합하지않기.','LEET잔여229문항후MEET202문항진행. 기존KICE496문항재처리없음.'],
 'constraints':{'results_only_in_backfill_folder':True,'new_KICE_reviews':0,'KICE_anchor_only':['NL'],'original_assets_changed':False,'frozen_616_scenes_changed':False,'original_95_definitions_changed':False,'processed_CURRENT_changed':False,'other_models_called':False,'automatic_git_push':False,'holds_preserved':['G024','G370']},
 'legacy_metadata_note':'checkpoint의other_models_called=true는과거허용된Luna경로검색의역사기록. 이번에는다른모델호출없으며주에이전트가의미판단을직접수행.'
}
write('session_handoff_20261015_04.json',h)
c.update(latest_session_handoff='session_handoff_20261015_04.json',session_handoff_reason=reason,session_validation='session_validation_20261015_04.json',last_saved_author='author_017b.py',last_saved_audit='audit_016.py',next_sample_audit_at=680,current_session_other_models_called=False)
write('checkpoint.json',c)
write('session_progress_20261015_04.json',{'start_reviewed':618,'start_scenes':986,'current_reviewed':646,'current_scenes':1022,'new_questions':28,'new_scenes':36,'remaining':431,'unresolved':32,'last_saved_author':'author_017b.py','last_audit':'audit_016.py','active_batch':17,'active_batch_questions':6,'next':h['next'],'next_audit_at':680,'status':'중간인계저장·전체연구진행중','handoff':'session_handoff_20261015_04.json'})
legacy=json.loads((OUT/'session_handoff_20261013.json').read_text());legacy.update(latest_session_handoff='session_handoff_20261015_04.json',last_saved_author='author_017b.py',last_saved_audit='audit_016.py',batch_state='001~016 저장·표본감사완료.17배치6문항저장.646문항1022장면.다음647 BFR.',next_sample_audit_at=680);write('session_handoff_20261013.json',legacy)
print(json.dumps({'검토':646,'장면':1022,'이번문항':28,'이번장면':36,'남음':431,'유보':32,'다음':h['next'],'인계':'session_handoff_20261015_04.json','검증':True},ensure_ascii=False))
