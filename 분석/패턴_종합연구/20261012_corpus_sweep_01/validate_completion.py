"""최종 지문·문항·복수 장면·후속 과제·보존 집계를 검증한다. 의미 검증 아님."""
import ast, collections, hashlib, json
from corpus_io import ROOT, OUT, rows, load, write, sha
from candidates import P

prefix=str(OUT.relative_to(ROOT))+'/'
cp=load(prefix+'checkpoint.json')
summary=load(prefix+'final_scope_summary.json')
coverage=rows(prefix+'question_coverage.jsonl')
unextracted=rows(prefix+'unextracted_questions.jsonl')
depth=rows(prefix+'depth_followup_questions.jsonl')
history=rows(prefix+'group_extractions.jsonl')
scenes=[s for p in sorted(OUT.glob('batch_*_scenes.jsonl')) for s in rows(str(p.relative_to(ROOT)))]
base=load(prefix+'resume_verified_20261012.json')
original_events={s['event_id'] for s in scenes if s['unique_group'] in base['completed_groups']}
amendments=rows(prefix+'scene_amendments.jsonl')
for amendment in amendments:
    target=next(s for s in scenes if s['event_id']==amendment['event_id'])
    target.update(amendment['changes'])
    if amendment.get('audit_id')=='재개_의미경계_01': assert target['event_id'] not in original_events
assert len(original_events)==489
assert cp['next_group'] is None and cp['next_batch'] is None and cp['expected_remaining_groups']==0
assert len(cp['completed_groups'])==len(set(cp['completed_groups']))==len(history)==495
assert set(cp['completed_groups'])=={g['unique_group'] for g in history}
assert len({r['unique_question'] for r in coverage})==len(coverage)==1675
eligible=[r for r in coverage if r['eligible_for_sweep']]
with_scene=[r for r in eligible if r['scene_count']]
assert len(eligible)==1667 and len(with_scene)==590 and len(unextracted)==1077
assert {r['unique_question'] for r in unextracted}=={r['unique_question'] for r in eligible if not r['scene_count']}
assert not {r['unique_question'] for r in with_scene}&{r['unique_question'] for r in unextracted}
assert all(not r['scene_count'] and not r['group_first_pass_completed'] for r in coverage if not r['eligible_for_sweep'])
assert sum(r['scene_count'] for r in coverage)==len(scenes)==616
scenes_by_q=collections.defaultdict(list)
for scene in scenes:
    assert scene['pattern'] in P
    assert all(isinstance(scene[k],str) and scene[k].strip() for k in 'ABCDEF')
    scenes_by_q[scene['unique_question']].append(scene)
for r in with_scene:
    actual=scenes_by_q[r['unique_question']]
    assert set(r['event_ids'])=={s['event_id'] for s in actual}
    assert set(r['patterns'])=={s['pattern'] for s in actual}
counts=load(prefix+'pattern_counts.json')
cards=load(prefix+'pattern_candidates.json')
assert {r['pattern'] for r in counts}=={r['pattern'] for r in cards}=={s['pattern'] for s in scenes}
assert len(counts)==summary['judge_candidates']==95
assert sum(r['actual_solution_uses'] for r in counts)==616
assert len(depth)==summary['explicit_depth_followup_questions']==32
assert len({r['unique_question'] for r in depth})==32
assert all(r['unique_question'] in {q['unique_question'] for q in eligible} for r in depth)
assert sum(bool(r['event_ids']) for r in depth)==21
assert sum(not r['event_ids'] for r in depth)==11
raw=rows('data/기본기_연구/astra_handoff_queue.jsonl')
processed=rows('data/기본기_연구/astra_handoff_processed.jsonl')
pending={r['record_id'] for r in raw}-{r['source_record_id'] for r in processed if r.get('processed')}
assert len(raw)==len(processed)==7605 and not pending
for e in rows(prefix+'evidence_links.jsonl'):
    assert sha(ROOT/e['source_path'])==e['source_sha256']
    for r in e['solution_records']:
        stored=raw[r['line']-1]
        assert stored['record_id']==r['record_id'] and stored['payload']==r['payload']
for e in rows(prefix+'evidence_stage_supplements.jsonl'):
    assert e['event_id'] in {s['event_id'] for s in scenes}
    for r in e['supplemental_records']:
        stored=raw[r['line']-1]
        assert stored['record_id']==r['record_id'] and stored['payload']==r['payload'] and stored['stage']==r['stage']
for r in rows(prefix+'followup_evidence_index.jsonl'):
    assert raw[r['line']-1]['record_id']==r['record_id']
    assert all(raw[r['line']-1]['payload'][k]==v for k,v in r['fields'].items())
for name,old in base['existing_file_prefixes'].items():
    if name!='candidates.py': assert hashlib.sha256((OUT/name).read_bytes()[:old['bytes']]).hexdigest()==old['sha256'],name
# 신규 P 정의 블록만 제거하면 재개 전 candidates.py의 전체 바이트가 복원되어야 한다.
source=(OUT/'candidates.py').read_text();lines=source.splitlines(keepends=True);added=[]
for n in ast.parse(source).body:
    if isinstance(n,ast.Assign) and any(isinstance(t,ast.Subscript) and isinstance(t.value,ast.Name) and t.value.id=='P' for t in n.targets): added.append(n)
    elif isinstance(n,ast.Expr) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Attribute) and isinstance(n.value.func.value,ast.Name) and n.value.func.value.id=='P' and n.value.func.attr=='update': added.append(n)
for n in reversed(added): del lines[n.lineno-1:n.end_lineno+1]
assert hashlib.sha256(''.join(lines).encode()).hexdigest()==base['existing_file_prefixes']['candidates.py']['sha256']
preservation=load(prefix+'preservation_report.json')
assert preservation['unchanged_file_count']==9867
assert not preservation['changed_evidence_or_frozen_inputs'] and not preservation['missing_files']
assert len(preservation['changed_noninput_live_sibling_files'])==2
assert len(rows(prefix+'layer_candidates.jsonl'))==15
assert all(p['event_ids'] if p['layer'].startswith('B') else p['groups'] for p in rows(prefix+'layer_candidates.jsonl'))
report=dict(status='최종 저장·연결·범위 검사 통과',completed_first_pass_groups=495,eligible_questions=1667,scene_questions=590,scenes=616,unextracted_questions=1077,multiple_scene_questions=25,held_groups=2,held_questions=8,depth_followup_questions=32,depth_overlap_extracted=21,depth_overlap_unextracted=11,judge_candidates=95,pending_raw=0,old489scenes_bytes_preserved=True,old400groups_not_reprocessed=True,old_candidate_definitions_bytes_preserved=True,sdss_meaning_supplements_checked=True,semantic_validity_globally_completed=False,validation_scope='ID·集計·범위·추가 근거raw·이전 저장바이트·후보 정의 보존. 원문 의미의 전수 재검증 및 난도 검증 아님.')
report['validation_scope']=report['validation_scope'].replace('集計','집계')
write('completion_validation.json',report)
write('output_hashes.json',{p.name:sha(p) for p in OUT.iterdir() if p.is_file() and p.suffix in ('.json','.jsonl','.md','.py') and p.name!='output_hashes.json'})
for name,h in load(prefix+'output_hashes.json').items(): assert sha(OUT/name)==h
print('최종 검사 통과:495지문·590문항·616장면·미추출1077문항; 기존400지문/489장면·기존 후보 정의 보존; pending raw=0.')
