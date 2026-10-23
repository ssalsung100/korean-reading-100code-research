"""집계·연결·불변성만 검사한다. 의미 타당성이나 정답률 검증이 아니다."""
import collections,json
from corpus_io import ROOT,OUT,load,rows,write,sha
cp=load(str(OUT.relative_to(ROOT)/'checkpoint.json'))
gs=rows(str(OUT.relative_to(ROOT)/'manifest_groups.jsonl'))
qs=rows(str(OUT.relative_to(ROOT)/'manifest_questions.jsonl'))
es=rows(str(OUT.relative_to(ROOT)/'manifest_analyses.jsonl'))
history=rows(str(OUT.relative_to(ROOT)/'group_extractions.jsonl'))
ev=rows(str(OUT.relative_to(ROOT)/'evidence_links.jsonl'))
sc=[]
for p in OUT.glob('batch_*_scenes.jsonl'):sc+=rows(str(p.relative_to(ROOT)))
raw=rows('data/기본기_연구/astra_handoff_queue.jsonl')
assert len(cp['completed_groups'])==len(set(cp['completed_groups']))==len(history)
assert set(cp['completed_groups'])=={h['unique_group'] for h in history}
assert not set(cp['completed_groups'])&{g['unique_group'] for g in gs if g['status']=='기존 보류 승계'}
assert len({s['event_id'] for s in sc})==len(sc)==len(ev)
assert {s['event_id'] for s in sc}=={e['event_id'] for e in ev}
assert len({q['unique_question'] for q in qs})==len(qs)
gset={g['unique_group'] for g in gs};qset={q['unique_question'] for q in qs}
assert all(e['unique_group'] in gset and e['unique_question'] in qset for e in es)
assert all(s['unique_group'] in cp['completed_groups'] and s['unique_question'] in qset for s in sc)
assert len({a['analysis_id'] for a in es})==len(es)
for e in ev:
    assert sha(ROOT/e['source_path'])==e['source_sha256']
    for r in e['solution_records']:
        assert raw[r['line']-1]['record_id']==r['record_id']
        assert raw[r['line']-1]['payload']==r['payload']
    if e['source_anchor']:
        src=load(e['source_path']);a=e['source_anchor'];assert src[a['field']][a['char_start']:a['char_end']]==a['quote']
baseline=load(str(OUT.relative_to(ROOT)/'input_hashes.json'))
changed=[];missing=[]
for p,h in baseline.items():
    f=ROOT/p
    if not f.exists():missing.append(p)
    elif sha(f)!=h:changed.append(p)
live_sibling_prefix='분석/패턴_종합연구/20261012_synthesis_01/'
changed_noninput_live=[p for p in changed if p.startswith(live_sibling_prefix)]
used_sources={e.get(k) for e in es for k in ['source_path','canonical_source_path']}
assert not set(changed_noninput_live)&used_sources
changed_inputs=[p for p in changed if p not in changed_noninput_live]
assert not changed_inputs and not missing,(changed_inputs,missing)
write('preservation_report.json',dict(baseline_file_count=len(baseline),unchanged_file_count=len(baseline)-len(changed),
    changed_evidence_or_frozen_inputs=changed_inputs,missing_files=missing,
    changed_noninput_live_sibling_files=[dict(path=p,before_sha256=baseline[p],current_sha256=sha(ROOT/p)) for p in changed_noninput_live],
    explanation='이웃 20261012_synthesis_01은 이번 판단 근거나 동결 근거 집합에 사용하지 않았다. 본 작업에서는 쓰지 않았다. 넓은 디렉터리 기준에 포함되어 해시 변화가 관측되었으므로 별도 기록하며 모든 파일 불변으로 보고하지 않는다.'))
order=load(str(OUT.relative_to(ROOT)/'execution_order.json'))['groups'];remaining=[g for g in order if g not in cp['completed_groups']]
assert cp['next_group']==(remaining[0] if remaining else None)
counts=load(str(OUT.relative_to(ROOT)/'corpus_counts.json'))
assert counts['identity_resolved_groups']==len(gs)
assert counts['identity_resolved_completed_questions']==sum(q['completed'] for q in qs)
assert counts['repeated_completed_analyses']==sum(e['completed'] for e in es)-sum(q['completed'] for q in qs)
write('validation_report.json',dict(status='기계 검사 통과',
    baseline_files=len(baseline),changed_input_files=changed_inputs,missing_input_files=missing,
    changed_noninput_live_sibling_files=changed_noninput_live,
    processed_groups=len(history),scenes=len(sc),evidence_records=len(ev),pending_groups=len(remaining),next_group=remaining[0] if remaining else None,
    original_raw_records=len(raw),raw_pending=counts['pending_raw'],
    source_anchors_present=sum(bool(e['source_anchor']) for e in ev),
    semantic_validation_completed=False,scope='ID·중복·raw행/내용·출처 SHA·인용 위치·집계·입력 불변성만 검사. 모든 원문 선지의 의미나 후보의 일반 타당성은 검사하지 않음.'))
write('output_hashes.json',{p.name:sha(p) for p in OUT.iterdir() if p.is_file() and p.suffix in ['.json','.jsonl','.md'] and p.name not in ['output_hashes.json','validation_report.json']})
print('기계 연결 검사 통과:',len(baseline)-len(changed),'기준 파일 불변;',len(changed_noninput_live),'미사용 이웃 파일 변화 별도 기록;',len(history),'지문;',len(sc),'장면;',len(remaining),'지문 대기. 의미 타당성 확정 아님.')
