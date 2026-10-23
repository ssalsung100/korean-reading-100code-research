"""이번 재개분의 저장 상태를 묶는다. 이미 실행했다면 재실행하지 않는다."""
import sys,json,collections
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,write,append,refresh,TARGETS
assert not (OUT/'session_handoff_20261015_03.json').exists(),'이미 인계 저장됨: 재실행 금지'
assert not any(x['amendment_id']=='QBF01-QAMD006' for x in rows(OUT/'question_amendments.jsonl')),'부분실행이면남은저장만복구'
current=rows(OUT/'current_question_reviews.jsonl')
r=next(x for x in current if x['unique_question']=='U0313-Q03')
old=r['option_checks'][0]['statement_relation'];assert old=='지역 장르 귀속 반대'
append('question_amendments.jsonl',[{'amendment_id':'QBF01-QAMD006','unique_question':'U0313-Q03','reason':'AYN① 판정 표제의 장르를 빙붕 규모로 정정. 추론·정답·유보·근거 불변.','changes':[{'field_path':'option_checks.0.statement_relation','old_value':old,'new_value':'지역별 빙붕 규모의 귀속 반대'}]}])
refresh()
c=json.loads((OUT/'checkpoint.json').read_text())
assert c['reviewed_questions']==618 and c['new_scene_count']==986 and c['next_order']==619
assert sum(x['unresolved_questions'] for x in c['by_exam'].values())==28
raw=rows(OUT/'raw_question_reviews.jsonl')
expected=[q['unique_question'] for q in TARGETS[573:618]]
selected=[r for r in raw if r['unique_question'] in set(expected)]
assert len(selected)==45 and [r['unique_question'] for r in selected]==expected
assert all(n==1 for n in collections.Counter(r['unique_question'] for r in selected).values())
assert sum(len(r['scenes']) for r in selected)==64
assert sum(len(r['option_checks']) for r in selected)==225
ids=[s['event_id'] for r in selected for s in r['scenes']];assert len(ids)==len(set(ids))
authors=['author_015'+x+'.py' for x in 'fghijklmn']+['author_016'+x+'.py' for x in 'abcdef']
validations=[json.loads((OUT/a.replace('.py','_validation.json')).read_text()) for a in authors]
assert all(v['pass'] and not v['errors'] for v in validations)
assert sum(v['questions'] for v in validations)==45
assert sum(v['scenes'] for v in validations)==64
au=rows(OUT/'semantic_sample_audits.jsonl');assert au[-1]['batch']==15
validation={'scope':'574~618 신규45문항의저장메타데이터·ID·전선지수와15개author의개별인용검증결과확인. 원문구간·해시는각author저장시검증했으며이단계에서보호원장전수해시를재실행하지않음.','range':[574,618],'questions':45,'scenes':64,'options':225,'duplicate_questions':[],'duplicate_scene_ids':[],'author_validations':[a.replace('.py','_validation.json') for a in authors],'all_author_validations_passed':True,'audited_batch':15,'sample':{'questions':18,'scenes':29,'options':90},'final_label_correction':'QBF01-QAMD006','pass':True}
write('session_validation_20261015_03.json',validation)
reason='이번 응답의 컨텍스트·작성 작업 예산에 맞춘 중간 인계. 연구 또는 배치 완료를 종료 사유로 삼지 않았으며,15배치 감사 후16배치18문항을 추가 진행했다. 구체 quota 잔여치·runtime emergency 경고는 관측되지 않았고 한도값을 추정하지 않는다.'
c.update(last_saved_author='author_016f.py',last_incremental_validation='author_016f_validation.json',last_saved_audit='audit_015.py',audited_batches=[x['batch'] for x in au],next_sample_audit_at=640,latest_session_handoff='session_handoff_20261015_03.json',current_session_other_models_called=False,current_session_semantic_judgment='주 에이전트 직접 수행',session_handoff_reason=reason,session_validation='session_validation_20261015_03.json')
write('checkpoint.json',c)
h={
 'date':'2026-10-15','run':'세 번째 이어서 실행','status':'진행 중·중간 인계 저장','stop_reason':reason,
 'authoritative_checkpoint':'checkpoint.json','previous_session_handoff':'session_handoff_20261015_02.json',
 'start':{'reviewed_questions':573,'scenes':922,'next_order':574,'next_question':'U0306-Q03','last_saved_author':'author_015e.py'},
 'session_completed':{'orders':[574,618],'questions_added':45,'scenes_added':64,'exam':'LEET','option_rows_checked':225,'new_raw_duplicates':0,'scripts':authors},
 'current':{'reviewed_questions':618,'target_questions':1077,'new_scenes':986,'remaining_questions':459,'by_exam':c['by_exam'],'unresolved_questions':28},
 'last_saved_author':'author_016f.py','last_saved_question':'U0327-Q03','last_saved_case':'BAE','last_audit':'audit_015.py','audited_batches':list(range(1,16)),
 'audit_15':{'sample_questions':18,'sample_scenes':29,'sample_options':90,'amendments':['QBF01-AMD042','QBF01-AMD043'],'developments':['QBF01-DEV052','QBF01-DEV053','QBF01-DEV054','QBF01-DEV055','QBF01-DEV056'],'blocking_errors':0,'verification':'audit_015_countermodel_checks.json'},
 'active_batch':{'number':16,'saved_questions':18,'semantic_sample_audit_complete':False,'next_audit_at_reviewed_questions':640},
 'new_candidates':{'new_ids':[],'decision':'이번 새 원리·구별은 개별장면과DEV052~056에 보존. 단일 사례를 반복 후보로 승격하거나 기존95정의에 강제 배정하지 않음. BFP001~013 정의 불변.'},
 'new_unresolved':[
 {'question':'U0309-Q01','case':'AXY','official_answer':3,'issue':'④의 약3배는 두 안테나의 유효길이/파장 비례계수k가 같을 때 성립. 원문1/4~1/2범위만으로독립k를배제할수없음.','verification':'AXY_antenna_ratio_verification.json','next':'동일설계계수 조건과 범위값을 후속 실제 비교문항에 대조. 공식③ 유지.'},
 {'question':'U0313-Q03','case':'AYN','official_answer':2,'issue':'②의두께감소속도는의도상S(바닥융해)로해석. 전체순두께의감소로확대하려면A,B,C·면적조건이추가로필요.','verification':'AYN_flux_interpretation_check.json','next':'제작문구를바닥에서녹는단위면적당두께로명료화. 실제아문센해두께증가주장아님. 공식②유지.'}],
 'prior_unresolved_review':{'AXB':'15배치감사에서동심층모형의질량·정규관성·외곽관성·밀도를재계산하여기존유보유지. 공식③변경없음.','AWI':'기존14배치비용축/개입량유보그대로보존. 이번전수재검증안함.'},
 'source_repairs':[
 {'cases':['AXY','AYA'],'files':['AXY_source_with_restored_formula.json','AYA_source_with_restored_formula.json','G348_source_repair_history.json'],'repair':'c,f,λ,c=fλ 및안테나분수1/2~1/4를공식2014렌더14·15쪽에서직접확인하여파생본에복원. source_overrides.json은이두대상만추가. 원본불변.'},
 {'case':'AYQ','file':'AYQ_view_restored.json','repair':'기존보충은변경표만있었음. 공식2015렌더7쪽에서A국의강한입법권한·강한기율·의회단순다수·대통령결선이라는초기상태문단복원. 기존source불변·보충근거로연결.'},
 {'case':'AXH','file':'AXH_source_with_restored_greek.json','repair':'이전세션α·β복원파생본을감사에서그대로사용. 원본과복원·노출이력구별유지.'}],
 'important_refinements':[
 'AYX: B_next=NOT A_sampled. 피드백뒤A가재계산되므로같은시점A와B가항상반대라는강한명제는금지. C=1이면동시A=B,C=0이면A=NOT B. AYX_timing_review.json과감사검산참조.',
 'AMD042: AXP의설명해상도연결제거. 구조식별/등장이유의과제구별은관계귀속과개별설명에보존.',
 'AMD043: AXG의대립가능성연결제거. 물의비이력/과냉각공존사례와두명제의진리조합전체분류를구별.',
 'QAMD006: AYN①표제의장르를빙붕규모로단순정정. 원raw·실제추론불변.',
 'AYK/T 동일문항의기존최초풀이및정답대조MD둘을연결. 매력적오답AYK①/T②이력보존·고유1회계수.',
 'BAB: 절차부재는규칙의적용범위밖이며,절차존재하법관귀책으로미이용한명시예외와다름. 배제사유부재를최종배상확정으로전환하지않음.',
 'AZV: 서로다른Wg농도에서mRNA동일이보장되지않는다는말을모든mRNA가반드시상이하다고강화하지않음. 또는로제시된수용체/소낭경로를동시필수로바꾸지않음.'
 ],
 'next':{'order':619,'unique_question':c['next_question'],'case_ids':c['next_case_ids'],'read_but_not_saved':False,'suggested_author':'author_016g.py','resume_command':'python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 619 2'},
 'save_state':{'read_but_not_saved':[],'authored_but_not_saved':[],'last_validation':'session_validation_20261015_03.json','original_new_author_validation':'author_016f_validation.json','verification_scope':'각새author의원문구간·참조·선지수검증및새45문항ID·계수확인. 전체보호원장SHA검사없음.','execution_note':'author_015f첫preflight에서인용한곳의어순불일치를저장전에수정. 같은파일의문맥조작화연결도정의불일치로저장전에제거. 그외새author와audit는저장1회. yield된저장프로세스는poll후확인했으며재실행없음.'},
 'next_audit_focus':['16배치640경계에서AZH의입증완화/무입증,AZO/AZP의실험유효성/실천한계,AZU/AZV의역치·방향·대안가설,AZZ/BAB의가능경로·규칙범위밖/예외를표본에포함.','이번새후보강제배정없음. 기준내부검사·범위이동·관계귀속의연결이너무넓지않은지실제D/E와후속사례를대조.','LEET잔여257문항후MEET202문항으로진행. KICE재분석금지.'],
 'constraints':{'results_only_in_backfill_folder':True,'KICE_reanalysis':False,'original_assets_changed':False,'frozen_616_scenes_changed':False,'original_95_definitions_changed':False,'processed_CURRENT_changed':False,'other_models_called':False,'automatic_git_push':False,'holds_preserved':['G024','G370']},
 'legacy_metadata_note':'checkpoint의other_models_called=true와Luna경로검색기록은이전연구의역사적메타데이터다. 이번세션은current_session_other_models_called=false이며다른모델호출없음.'
}
write('session_handoff_20261015_03.json',h)
write('session_progress_20261015_03.json',{'start_reviewed':573,'start_scenes':922,'current_reviewed':618,'current_scenes':986,'new_questions':45,'new_scenes':64,'remaining':459,'unresolved':28,'last_saved_author':'author_016f.py','last_audit':'audit_015.py','active_batch':16,'active_batch_questions':18,'next':h['next'],'next_audit_at':640,'status':'중간인계저장·전체연구진행중','handoff':'session_handoff_20261015_03.json'})
legacy=json.loads((OUT/'session_handoff_20261013.json').read_text());legacy.update(latest_session_handoff='session_handoff_20261015_03.json',last_saved_author='author_016f.py',last_saved_audit='audit_015.py',batch_state='001~015 저장·표본감사완료.16배치18문항저장.618문항986장면.다음619 BAF.',next_sample_audit_at=640);write('session_handoff_20261013.json',legacy)
print(json.dumps({'검토':618,'장면':986,'이번문항':45,'이번장면':64,'남음':459,'유보':28,'다음':h['next'],'인계':'session_handoff_20261015_03.json','검증':True},ensure_ascii=False))
