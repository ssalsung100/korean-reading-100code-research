"""직접 저장한 판단을 집계하고 문항별 추출 범위와 후속 대상을 기록한다.

새 풀이·의미 추론·기존 원장 변경은 하지 않는다. 후속 우선순위는 직접 작성한
아래 사례 목록이며 원장 유보 필드의 기계 색인과 구분한다.
"""
import collections, json, hashlib
from corpus_io import ROOT, OUT, rows, load, write, jsonl, sha

prefix = str(OUT.relative_to(ROOT)) + '/'
groups = rows(prefix+'manifest_groups.jsonl')
questions = rows(prefix+'manifest_questions.jsonl')
analyses = rows(prefix+'manifest_analyses.jsonl')
history = rows(prefix+'group_extractions.jsonl')
scenes = [s for p in sorted(OUT.glob('batch_*_scenes.jsonl')) for s in rows(str(p.relative_to(ROOT)))]
for amendment in rows(prefix+'scene_amendments.jsonl'):
    next(s for s in scenes if s['event_id']==amendment['event_id']).update(amendment['changes'])
events = {s['event_id']:s for s in scenes}
gmap = {g['unique_group']:g for g in groups}
amap = {a['analysis_id']:a for a in analyses}
case_map = {a['case_id']:a for a in analyses if a['origin']=='prepared'}
held = {g['unique_group'] for g in groups if g['status']=='기존 보류 승계'}
eligible = {g['unique_group'] for g in groups if g['status']=='추출 대기'}
assert {g['unique_group'] for g in history} == eligible and len(history)==495
by_question = collections.defaultdict(list)
for scene in scenes: by_question[scene['unique_question']].append(scene)
raw = rows('data/기본기_연구/astra_handoff_queue.jsonl')
raw_index = collections.defaultdict(list)
for line, record in enumerate(raw,1): raw_index[record.get('case')].append((line,record))

# 이미 검토한 새 구간에서 직접 지정한 A/B의 추가 근거. 자동 분류가 아니다.
layer_extensions = {
 'A01':['U0160','U0432','U0448','U0470','U0455'],
 'A02':['U0154','U0163','U0182','U0469'],
 'A03':['U0430','U0460','U0457'],
 'A05':['U0158','U0433','U0462','U0468','U0476','U0487','U0496'],
 'A06':['U0446','U0464','U0441'],
 'A07':['U0171','U0173','U0180','U0465','U0485','U0486','U0490','U0492'],
 'A08':['U0438','U0450'],
 'B01':['U0156-S01','U0158-S01','U0181-S01','U0452-S01','U0486-S01','U0488-S01'],
 'B02':['U0164-S01','U0434-S01','U0475-S01','U0490-S01'],
 'B03':['U0455-S01','U0493-S01','U0495-S01','U0485-S01','U0492-S01'],
 'B04':['U0430-S01','U0163-S03','U0462-S01','U0457-S01'],
 'B05':['U0155-S01','U0159-S01','U0159-S02','U0428-S01','U0166-S01','U0467-S01','U0467-S02'],
 'B07':['U0161-S01','U0161-S02','U0473-S01','U0466-S02'],
}
layer_records = rows(prefix+'layer_candidates.jsonl')
extension_records=[]
for card in layer_records:
    additions=layer_extensions.get(card['candidate_id'],[])
    if not additions: continue
    kind='groups' if card['layer'].startswith('A') else 'event_ids'
    existing=set(card[kind])
    for item in additions:
        if item in existing: continue
        card[kind].append(item)
        if kind=='groups':
            assert item in eligible
            card['evidence'].append(dict(unique_group=item,source='group_extractions.jsonl',field='A',links=gmap[item]['source_paths']))
        else:
            scene=events[item]
            card['evidence'].append(dict(event_id=item,B=scene['B'],C=scene['C'],link='evidence_links.jsonl'))
    if kind=='groups':
        card['count']=dict(unique_passages=len(card[kind]),unique_questions=0,actual_solution_uses=0,passage_structure_only=len(card[kind]),by_exam={f:sum(gmap[g]['exam_family']==f for g in card[kind]) for f in ['KICE','LEET','MEET']})
    else:
        selected=[events[x] for x in card[kind]]
        card['count']=dict(unique_passages=len({s['unique_group'] for s in selected}),unique_questions=len({s['unique_question'] for s in selected}),actual_solution_uses=len(selected),passage_structure_only=0,by_exam={f:dict(passages=len({s['unique_group'] for s in selected if s['exam_family']==f}),questions=len({s['unique_question'] for s in selected if s['exam_family']==f})) for f in ['KICE','LEET','MEET']})
    extension_records.append(dict(candidate_id=card['candidate_id'],layer=card['layer'],new_evidence=additions,decision='직접 검토한 재개 구간의 추가 근거. 이전 근거와 정의를 보존함.'))
jsonl('layer_evidence_extension.jsonl',extension_records)
jsonl('layer_candidates.jsonl',layer_records)
layer_md=['# 지문 전개·선지 변형의 층위별 후보','','A는 지문 배치의 근거만 세며 실제 풀이 사용은0이다. B는 연결된 장면의 근거 집합이다. 판단 행동 D와 합산하지 않는다. 빈도는 선별한 근거의 하한이다.','']
for r in layer_records:
    layer_md += ['## '+r['candidate_id']+' · '+r['name'],'',r.get('A',r.get('B')),'','조건: '+r['E'],'','제작 활용: '+r['F'],'','근거: '+', '.join(r.get('groups',r.get('event_ids'))),'','집계: '+json.dumps(r['count'],ensure_ascii=False),'']
(OUT/'지문_문항_층위별_후보.md').write_text('\n'.join(layer_md)+'\n')

# 아래는 원문과 기존 보강을 직접 읽고 정한 후속 작업이며 자동 유보 판정이 아니다.
depth_cases={
 'AX':'[A] 괄호 하단 범위의 원문 시각 확인',
 'BB':'[A]의 공식 시각 범위 확인',
 'HI':'비교 문장의 지정범위 포함 여부',
 'GL':'중복 첨자·누락 수식의 정본 연결',
 'GC':'②를 엄밀하게 배제하는 전제의 충분성',
 'HK':'끝 변위의 보조 기하 모형과 원문 조건 구별',
 'HD':'동일 감도·다른 도달 시간 그래프의 추가 장면',
 'BGQ':'누락 변수·수식과 상수 근사의 근거 범위',
 'BFX':'원선지 번호와 시각 자료05~09의 대응',
 'BCF':'간접 영향 허용 기준과ㄹ의 완전 배제',
 'BFP':'제소 가능성과 실체 성립의 구별·유일성',
 'BFQ':'부합의 양립/확률 지지 및 증거 합산 기준',
 'BGU':'선율-화음 복원의 범위·유일성·정량 비교',
 'BHG':'허용 범위와 투표 발생 규칙의 양방향 여부',
 'BHF':'거리의 원점/대상 간 해석 범위',
 'BEB':'보 사용을 실제 감주로 읽는 문맥 조건',
 'BEE':'약화 자료와 결정적 반증의 차이',
 'BLT':'원문만의 끝점 부등식·대칭 지점 도출 및 상한 동시 실현',
 'BMC':'겹침 인정에서 풍경 안 자각으로 가는 해석 강도',
 'BND':'ℓ≥2 문맥 조건과 ℓ=1 허용 시 반례',
 'BNG':'반응량에서 비용 변화 크기를 식별하는 추가 조건',
 'BNU':'문턱·포화 반응 아래 정확 생성량·생성량0의 식별',
 'BNW':'④의 도덕판단 문맥/정서 일반 범위',
 'BOG':'소거 선택과 붉은 소변 부재 직접 증명의 차이',
 'BOO':'문턱의 필요 요구와 최종 충분 정당화 해석',
 'BOS':'양의 초기값 범위·0고정점·수렴과 단조 격차 감소',
 'BPE':'행위-음향 동기화·메시지 우선과 대안 연출의 양립',
 'BPW':'상관 부호와 소득 지속성의 문맥 보충',
 'BQC':'두 책임 이전 연결 각각의 예측가능성',
 'BQI':'국제정세 활용과 국제적 고립의 범위·독점적 차이',
 'BQT':'초연의 두 의미와 특정 성취/일반 성공 범위',
 'BTH':'사전 인지 가능성과 실제 앎·지식 귀속 전제',
}
followups=[]
for case,task in depth_cases.items():
    assert case in case_map,case
    a=case_map[case];related=by_question.get(a['unique_question'],[])
    followups.append(dict(case_id=case,unique_group=a['unique_group'],unique_question=a['unique_question'],exam_family=a['exam_family'],task=task,priority='1 원문 충실도' if case in {'AX','BB','HI','GL','HD','BGQ','BFX'} else '2 추론·경계 조건',status='후속 검토 대상; 이번에 해소했다고 보고하지 않음',extraction_status='장면 있음' if related else '문항 장면 미추출',event_ids=[s['event_id'] for s in related],source_path=a['source_path'],existing_solution_record_ids=[r['record_id'] for _,r in raw_index[case]]))
jsonl('depth_followup_questions.jsonl',followups)
depth_by_q={r['unique_question']:r for r in followups}

coverage=[]
for question in questions:
    gid=question['unique_group'];qid=question['unique_question'];actual=by_question.get(qid,[])
    state='既存hold'.replace('既存','기존 ') if gid in held else ('판단 장면 추출' if actual else '지문 1차 종합 완료·문항 장면 미추출')
    linked=[amap[i] for i in question['analysis_ids']]
    coverage.append(dict(unique_question=qid,unique_group=gid,exam_family=question['exam_family'],operational_groups=gmap[gid]['operational_groups'],stored_question_ids=question['stored_question_ids'],analysis_ids=question['analysis_ids'],case_ids=sorted({a['case_id'] for a in linked}),eligible_for_sweep=gid in eligible,original_completed=question['completed'],group_first_pass_completed=gid in eligible,extraction_status=state,scene_count=len(actual),event_ids=[s['event_id'] for s in actual],patterns=sorted({s['pattern'] for s in actual}),source_paths=sorted({a['source_path'] for a in linked}),known_depth_followup=depth_by_q.get(qid),all_options_annotated=False,scope='지문 처리 완료와 문항·선지 전수 분석 완료를 구별한다. 미추출은 발생0·오답·미풀이를 뜻하지 않는다.'))
jsonl('question_coverage.jsonl',coverage)
unextracted=[r for r in coverage if r['eligible_for_sweep'] and not r['scene_count']]
jsonl('unextracted_questions.jsonl',unextracted)
jsonl('group_limitations.jsonl',[dict(unique_group=g['unique_group'],limitations=g['limitations'],source='group_extractions.jsonl',interpretation='원래 주석을 보존. 모든 항목이 미해결 심층 과제인 것은 아니다.') for g in history if g['limitations']])

# 원장에 담긴 유보·정정 필드를 인덱스로만 노출한다. 뒤 기록의 해소를 자동 판정하지 않는다.
notes=[]
for a in analyses:
    if a['origin']!='prepared' or a['unique_group'] not in eligible: continue
    for line,r in raw_index[a['case_id']]:
        fields={k:v for k,v in r['payload'].items() if any(t in k for t in ('unresolved','uncertainty','source_limit_resolution','source_correction','exposure_correction','next_review_target')) and v and v not in ('없음','none','None')}
        if fields: notes.append(dict(case_id=a['case_id'],unique_question=a['unique_question'],record_id=r['record_id'],line=line,stage=r['stage'],fields=fields,status='원장 필드 색인; 최신 의미 상태·해소 여부의 자동 판정 아님'))
jsonl('followup_evidence_index.jsonl',notes)
supplements=[]
for scene in scenes:
    extra=[dict(record_id=r['record_id'],line=line,stage=r['stage'],payload=r['payload']) for line,r in raw_index[scene['case_id']] if r['stage']=='sdss_compare']
    if extra: supplements.append(dict(event_id=scene['event_id'],solution_path='data/기본기_연구/astra_handoff_queue.jsonl',supplemental_records=extra,role='후속 의미 비교·유보 추적용. SDSS는 정답지가 아니며 장면 발생 횟수에 더하지 않음.'))
jsonl('evidence_stage_supplements.jsonl',supplements)

verified=load(prefix+'resume_verified_20261012.json')
prior=set(verified['completed_groups']);added=[g['unique_group'] for g in history if g['unique_group'] not in prior]
old_questions={s['unique_question'] for s in scenes if s['unique_group'] in prior}
multi=collections.Counter(s['unique_question'] for s in scenes)
stats=dict(eligible_groups=495,completed_first_pass_groups=len(history),pending_groups=0,eligible_questions=sum(r['eligible_for_sweep'] for r in coverage),extracted_unique_questions=len(by_question),extracted_scenes=len(scenes),unextracted_questions=len(unextracted),held_groups=len(held),held_questions=sum(r['unique_group'] in held for r in coverage),multiple_scene_questions=sum(n>1 for n in multi.values()),extra_scenes_beyond_one_per_question=sum(n-1 for n in multi.values()),judge_candidates=len({s['pattern'] for s in scenes}),passage_candidates=sum(r['layer'].startswith('A') for r in layer_records),item_candidates=sum(r['layer'].startswith('B') for r in layer_records),explicit_depth_followup_questions=len(followups),depth_followup_already_extracted=sum(bool(r['event_ids']) for r in followups),depth_followup_unextracted=sum(not r['event_ids'] for r in followups),candidate_boundary_pending=sum(not r.get('resolution') for r in rows(prefix+'unclassified_scenes.jsonl')),continuation_added_groups=len(added),continuation_added_scenes=sum(s['unique_group'] in set(added) for s in scenes),continuation_new_unique_questions=len(set(by_question)-old_questions),by_exam={f:dict(groups=sum(gmap[g]['exam_family']==f for g in eligible),eligible_questions=sum(r['eligible_for_sweep'] and r['exam_family']==f for r in coverage),extracted_questions=len({s['unique_question'] for s in scenes if s['exam_family']==f}),scenes=sum(s['exam_family']==f for s in scenes),unextracted_questions=sum(r['exam_family']==f for r in unextracted)) for f in ['KICE','LEET','MEET']})
assert stats['eligible_questions']==1667
assert stats['extracted_unique_questions']+stats['unextracted_questions']==1667
assert len(added)==95 and set(added).isdisjoint(prior)
preserved=[]
for name,baseline in verified['existing_file_prefixes'].items():
    if name=='candidates.py': continue # 새 정의만 추가. 기존 P 정의의 의미는 변경하지 않았다.
    content=(OUT/name).read_bytes()[:baseline['bytes']]
    assert hashlib.sha256(content).hexdigest()==baseline['sha256'], name
    preserved.append(name)
write('continuation_validation.json',dict(status='재개 구간 저장·집계 검사 통과',before_groups=400,before_scenes=489,after_groups=495,after_scenes=len(scenes),new_group_ids=added,duplicate_processed_groups=0,old_file_prefixes_preserved=preserved,old_group_judgments_reprocessed=0,new_scene_boundary_amendments=20,scope='재개 전 저장 바이트와 신규 지문 집합의 비중복 검사. 의미 타당성의 자동 검증 아님.'))
write('final_scope_summary.json',stats)
cp=load(prefix+'checkpoint.json')
cp.update(status='대상 지문 1차 종합 완료',completed_batches=13,next_batch=None,next_group=None,next_action='question_coverage.jsonl의 미추출 문항1077개와 depth_followup_questions.jsonl·미분류15개 기록의 후속 보완. 기존 완료 지문 재처리 금지.',last_completed_operational_groups=gmap[cp['last_completed_group']]['operational_groups'],next_operational_groups=[],expected_remaining_groups=0,context_handoff_reason='요청된495지문 1차 종합 완료. 지문 미처리는0이며 문항·선지 전수 주석과 일반 타당성 검증은 별도 후속 작업.',continuation_added_groups=len(added),continuation_added_scenes=stats['continuation_added_scenes'],continuation_notes=['전수완료_추가귀납.md','최종_진행보고.md'],semantic_validity='495지문 1차 종합 완료.590고유 문항616장면의 잠정 귀납.1077문항 장면 미추출·심층 보완·후보 일반 타당성 검증은 남아 있음.',completion_scope='지문별 1차 종합',question_coverage='question_coverage.jsonl',final_summary='final_scope_summary.json')
write('checkpoint.json',cp)
table=['|시험군|지문 1차 완료|대상 문항|장면 있는 문항|판단 장면|미추출 문항|','|---|---:|---:|---:|---:|---:|']
for f,x in stats['by_exam'].items():table.append(f"|{f}|{x['groups']}|{x['eligible_questions']}|{x['extracted_questions']}|{x['scenes']}|{x['unextracted_questions']}|")
md=['# 495지문 1차 분석 완료 보고','',f"실제 재개 확인 상태는400지문·489장면·489고유 문항·86판단 후보였다. 배치010까지 완결, 배치011에20지문 저장. U0427/G466 다음의 U0154/G193부터 저장된 실행 순서를 따랐다. 마지막은U0497/G537이다.",'',f"이번에 {stats['continuation_added_groups']}지문·{stats['continuation_added_scenes']}장면·{stats['continuation_new_unique_questions']}개 신규 고유 문항을 추가했다. 재개 전400지문은 재처리하지 않았다. 배치011의 남은20개, 배치012의40개, 배치013의35개를 완료했다.",'',f"최종 대상495지문 전부의1차 종합이 완료됐다. 실제 장면은 {stats['extracted_unique_questions']}고유 문항의{stats['extracted_scenes']}개다. 복수 장면 문항은{stats['multiple_scene_questions']}개이며 한 문항당1장면 기준보다{stats['extra_scenes_beyond_one_per_question']}개 많다. 모든 선지 전수 주석 완료라는 뜻은 아니다.",'',*table,'',f"판단 행동 후보{stats['judge_candidates']}개·지문 전개8개·발문 및 선지 변형7개를 별도 층위로 유지한다. 이 수는 최종100코드 수나 서로 독립적인 능력 수가 아니다. 신규9개 후보는 기존 후보에 억지로 넣지 않기 위한 잠정 분할이며 일반 타당성을 검증하지 않았다.",'','## 실제 분석 범위와 후속 작업','',f"`question_coverage.jsonl`은 hold8문항을 포함한 연결1675문항의 전체 목록이다. 대상1667문항 중590문항은 실제 장면이 있고1077문항은 지문1차 분석에 연결되었으나 판단 장면이 미추출이다. `unextracted_questions.jsonl`에1077문항의case ID·출처·기존 분석 경로를 저장했다. 미추출은 풀이 미완료나 해당 행동 빈도0을 뜻하지 않는다.",'',f"`depth_followup_questions.jsonl`에는 직접 지정한{len(followups)}개 심층 보완 문항을 기록했다. 장면 있는 문항{stats['depth_followup_already_extracted']}개와 미추출{stats['depth_followup_unextracted']}개가 겹치므로 미추출 수와 합산하지 않는다. 전체 심층 검토 필요 문항의 최종 개수로 단정하지 않는다. `followup_evidence_index.jsonl`은 원장 유보·정정 필드의 기계 색인이며 의미적 해소 여부를 자동 판정하지 않았다.",'','미분류·후보 경계 기록23개 중8개는 기존 수정으로 잠정 재분할,15개는 남아 있다. 후보 추상화·원문 도형 검수·실제 실패의 배제 근거를 별도 후속 범위로 유지한다. 모든 문항의 모든 장면을 세분화하는 일, 후보 간 중복·분리의 반례 검증, KICE 우선의 제작 규칙 검증·학생 난도 검증은 후속 작업이다.','','## 기록의 보존·검증','', '기존raw7605건과processed7605건은 변경하지 않았고pending raw=0을 승계·검증한다. G024/G370의8prepared hold와 연결 초기 완료2문항은 기존대로 유지한다. 기존Astra 동결 자료·원장·CURRENT는 읽기 전용으로 유지했다. 모든 신규 쓰기는 본 작업 폴더 안에만 수행했다.','','재개 전 배치001~010 및 배치011의 기존20개 장면, 원문 근거 연결, 지문 추출 원장의 저장 바이트를 비교하여 보존을 확인했다. 새 장면20개의 후보 수정은 최초 장면을 덮어쓰지 않고 `scene_amendments.jsonl`에 기록했다. `continuation_validation.json`이 비중복·보존 결과다.','','입력9869개 해시 기준 가운데9867개는 불변이며, 이번 근거로 쓰지 않은 이웃 폴더의2개 파일 변화는 `preservation_report.json`에 따로 보존한다. 사용 근거·동결 입력 변화0과 누락0을 확인한다. 모든 기준 파일이 불변이라고 과장하지 않는다. `validation_report.json`은 ID·raw행/내용·출처SHA·인용·집계 검사이며 의미 타당성의 전수 검증이 아니다.','','최초 실패(BMC·BNQ 등), 정본 연결 정정(BRU계열), 사전 노출 정정(BQZ), 추가 가정 아래 보강(BLT·BNG·BNU·BPW 등)을 소급 성공으로 만들지 않았다. 후속SDSS 의미 비교는 `evidence_stage_supplements.jsonl`에서 원장ID와payload를 추가 연결했다. 새blind 풀이·정답 재검증·외부 모델 호출·Git push는 수행하지 않았다.']
(OUT/'최종_진행보고.md').write_text('\n'.join(md)+'\n')
(OUT/'RESUME.md').write_text('# 후속 보완 인계\n\n495/495지문1차종합 완료. 지문 미처리0.590고유 문항·616장면.\n\n체크포인트에 다음 지문은 없으며 기존 author 파일을 재실행하지 않는다. `최종_진행보고.md`, `final_scope_summary.json`, `question_coverage.jsonl`부터 읽는다.\n\n후속은1077개 미추출 문항의 추가 장면, `depth_followup_questions.jsonl`의 지정 과제, 미분류15개 기록의 경계 검토다. 겹치는 대상을 합산하지 않는다. `followup_evidence_index.jsonl`의 유보 필드는 자동 해소 판정이 아니다.\n\n지문별 최초 추출은 immutable로 보존한다. 의미 수정은 `scene_amendments.jsonl`, 추가 선지 장면은 신규 별도 보완 원장에 저장해 기존 event ID와 중복되지 않게 한다. group_extractions를 다시 record하여 완료지문을 재처리하지 않는다. G024/G370 hold·기존 raw·processed·CURRENT·Astra 동결 자료는 변경하지 않는다.\n\n8A/7B 층위의 추가 근거는 `layer_evidence_extension.jsonl`까지 적용되어 있다. 원래 `layer_induction.py`만 재실행하면 추가 근거가 빠지므로 현재JSONL을 기준으로 삼는다. 집계 재생성은report.py, 파일·연결 검사는verify_outputs.py다. 모두 완료상태 next_group=null을 처리한다.\n')
(OUT/'README.md').write_text('# 완료 풀이 코퍼스 종합 · 실행01\n\n495/495개 고유 지문의1차 분석을 완료했다.590개 고유 문항에서616개 판단 장면을 저장했다. 이번 재개는 검증된400지문·489장면에서95지문·127장면을 추가했고, 이미 저장된 지문은 재처리하지 않았다.\n\n핵심 결과는 `최종_진행보고.md`, `전수완료_추가귀납.md`, `현재_결과.md`이다. 지문 배치A·선지 행동B·중간 추론C·판단 행동D·적용 조건E·제작 활용F를 보존한다. 후보95개는 판단 행동,8개는 지문 전개,7개는 발문·선지 변형이며 서로 다른 층위의 수를 더하지 않는다. 빈도는 실제 추출 근거의 하한이다.\n\n대상1667문항 중590문항은 장면이 있고1077문항은 미추출이다. 모든 문항·선지의 전수 주석 완료가 아니다. `question_coverage.jsonl`, `unextracted_questions.jsonl`, `depth_followup_questions.jsonl`을 함께 읽는다. 원장 유보·정정은 `followup_evidence_index.jsonl`에서 찾아 최신 의미 기록을 직접 확인한다.\n\n`manifest_groups.jsonl`·`manifest_questions.jsonl`·`manifest_analyses.jsonl`은 지문·문항·분석 단위를 구분한다. 완료·단일분석자검토1730건은 고유 문항1669개와 반복61건으로 연결되며, hold지문에 연결된 초기완료2문항을 추출에서 보류해495지문·1667문항이 대상이다. 단일분석자 검토42건의 독립 절차 완료를 주장하지 않는다. 고유ID는 재번호화하지 않았고 폐기alias U0498~U0500과 초기식별manifest는 보존한다. `identity_resolution.json`·`coordinate_aliases.jsonl`로 연결 과정을 추적한다. 시험지 이미지 전수 대조에 따른 출제 이력의 최종 검수는 아니다.\n\n`evidence_links.jsonl`은 sourceSHA·원문·발문·선지·기존 보충·풀이raw를 연결하고 `evidence_stage_supplements.jsonl`은 후속SDSS 의미 비교를 추가 연결한다. SDSS는 제3자 색인이며 정답지가 아니다. 의미 수정은append-only `scene_amendments.jsonl`에 두고 `pattern_counts.json`·`pattern_candidates.json`은 수정 적용 후 집계다.\n\n마지막 완료U0497/G537, 다음 지문없음. 배치011은40지문·50장면,012는40지문·53장면,013은35지문·44장면이다. `checkpoint.json`·`processing_status.json`을 상태 기준으로 삼으며 `RESUME.md`에서 후속 보완 절차를 읽는다. 기존author파일 재실행은 금지한다.\n\n원장·Astra동결·CURRENT·G024/G370 hold는 변경하지 않았다. `continuation_validation.json`은 이전400지문·489장면의 저장바이트 보존과95신규지문 비중복을 검증한다. `preservation_report.json`은9867개 기준파일 불변·미사용 이웃파일2개 변화·사용근거변화0을 구분한다. `validation_report.json`·`completion_validation.json`은 기계 연결 검사이며 모든 의미·난도·일반타당성을 검증하지 않는다. `output_hashes.json`이 최종 산출물 무결성 기준이다.\n')
print(json.dumps(stats,ensure_ascii=False,indent=2))
