"""사람/주 모델이 직접 작성한 판단을 저장한다. 패턴 추론·자동 분류는 하지 않는다."""
import collections, json, sys
from pathlib import Path
from corpus_io import ROOT, OUT, rows, load, write, sha, get_source

ANALYSES=rows(str(OUT.relative_to(ROOT)/'manifest_analyses.jsonl'))
GROUPS=rows(str(OUT.relative_to(ROOT)/'manifest_groups.jsonl'))
RAW=rows('data/기본기_연구/astra_handoff_queue.jsonl')
BYCASE=collections.defaultdict(list)
for n,r in enumerate(RAW,1):BYCASE[r.get('case')].append(dict(line=n,**r))

def append(name,obj):
    with (OUT/name).open('a') as f:f.write(json.dumps(obj,ensure_ascii=False)+'\n');f.flush()

def record(spec):
    gid=spec['group']; g=next(g for g in GROUPS if g['unique_group']==gid)
    cp=load(str(OUT.relative_to(ROOT)/'checkpoint.json'))
    assert gid not in cp['completed_groups'],'중복 종합 금지'
    assert g['status']=='추출 대기','기존 hold/미완료 분석은 추출하지 않는다'
    es=[e for e in ANALYSES if e['unique_group']==gid and e['completed']]
    history=rows(str(OUT.relative_to(ROOT)/'group_extractions.jsonl')) if (OUT/'group_extractions.jsonl').exists() else []
    batch=max((g['batch'] for g in history),default=1)
    target=cp.get('batch_targets',{}).get(str(batch),40)
    if sum(g['batch']==batch for g in history)>=target:batch+=1
    # 모든 인용을 먼저 확인하여 뒤 장면의 인용 오류가 반쯤 저장된 그룹을 만들지 않게 한다.
    for s in spec['scenes']:
        if s.get('quote'):
            candidates=[e for e in es if e['case_id']==s['case']]
            e=next((e for e in candidates if e['origin']=='prepared'),candidates[0])
            src=get_source(e)
            assert any(s['quote'] in src.get(k,'') for k in ['passage_text','stem']),(gid,s['case'],s['quote'])
    for n,s in enumerate(spec['scenes'],1):
        candidates=[e for e in es if e['case_id']==s['case']]
        e=next((e for e in candidates if e['origin']=='prepared'),candidates[0])
        src=get_source(e);rr=BYCASE[e['case_id']]
        event=f'{gid}-S{n:02d}'
        needle=s.get('quote','');anchor=None
        if needle:
            for field in ['passage_text','stem']:
                pos=src.get(field,'').find(needle)
                if pos>=0:
                    anchor=dict(field=field,char_start=pos,char_end=pos+len(needle),quote=needle);break
            assert anchor is not None,(gid,s['case'],needle)
        refs=[dict(record_id=r['record_id'],line=r['line'],stage=r['stage'],payload=r['payload']) for r in rr if r['stage'] in ['blind','answer_check','independent_code','depth_backfill','boundary_revision']]
        ev=dict(event_id=event,unique_group=gid,unique_question=e['unique_question'],case_id=e['case_id'],
            stored_question_id=e['stored_question_id'],stored_passage_id=e['stored_passage_id'],
            source_path=e['source_path'],source_sha256=sha(ROOT/e['source_path']),source_anchor=anchor,
            stem_field='stem',stem=src.get('stem'),choices_field='choices',choices=src.get('choices'),
            original_source_links=dict(canonical_source_path=e.get('canonical_source_path'),provenance=src.get('provenance'),visual_supplements=src.get('visual_supplements')),
            existing_supplement_links=[dict(path=str(p.relative_to(ROOT)),sha256=sha(p)) for p in (ROOT/e['source_path']).parent.glob(e['case_id']+'_*') if p.is_file()],
            solution_path='data/기본기_연구/astra_handoff_queue.jsonl',solution_records=refs,
            legacy_solution_paths=e.get('solution_paths'),
            source_verification='기존 공식 원문 연결을 승계; 본문/선지 텍스트와 풀이의 의미 대조 범위는 개별 검토 주석을 따른다. 시험지 이미지 전수 재검수 아님')
        append('evidence_links.jsonl',ev)
        scene=dict(event_id=event,batch=batch,unique_group=gid,unique_question=e['unique_question'],exam_family=g['exam_family'],case_id=s['case'],
            pattern=s['pattern'],A=spec['A'],B=s['B'],C=s['C'],D=s['D'],E=s['E'],F=s['F'],
            use=s.get('use','실제 풀이 활용'),status=s.get('status','잠정 근거 연결'),
            source_check=s.get('source_check','기존 완성 풀이 종합; 모호한 논점을 새로 확정하지 않음'),
            evidence_id=event,not_a_new_blind_solution=True)
        append(f'batch_{batch:03d}_scenes.jsonl',scene)
    append('group_extractions.jsonl',dict(unique_group=gid,batch=batch,title=spec['title'],A=spec['A'],
        B_C_reviewed_cases=[e['case_id'] for e in es if e['origin']=='prepared'],
        non_prepared_analysis_ids=[e['analysis_id'] for e in es if e['origin']!='prepared'],
        extracted_scene_count=len(spec['scenes']),coverage='지문 그룹의 기존 풀이 1차 종합. 모든 선지 장면 전수 주석 완료는 아님',
        unclassified=spec.get('unclassified',[]),limitations=spec.get('limitations',[])))
    cp['completed_groups'].append(gid);cp['last_completed_group']=gid
    order=load(str(OUT.relative_to(ROOT)/'execution_order.json'))['groups'] if (OUT/'execution_order.json').exists() else [x['unique_group'] for x in GROUPS if x['status']=='추출 대기']
    pending=[x for x in order if x not in cp['completed_groups']]
    cp['next_group']=pending[0] if pending else None
    sizes=collections.Counter(g['batch'] for g in history);sizes[batch]+=1
    cp['completed_batches']=sum(n>=cp.get('batch_targets',{}).get(str(b),40) for b,n in sizes.items())
    cp['expected_remaining_groups']=len(pending)
    cp['next_batch']=batch+1 if sizes[batch]>=cp.get('batch_targets',{}).get(str(batch),40) else batch
    cp['semantic_validity']=f"{len(cp['completed_groups'])}그룹의 기존 풀이 1차 종합. 모든 선지 전수 주석·후보 일반 타당성 검증·전체 코퍼스 종합은 미완료."
    cp['status']='진행 중';write('checkpoint.json',cp)
    return gid

def aggregate():
    scenes=[]
    for p in sorted(OUT.glob('batch_*_scenes.jsonl')):scenes+=rows(str(p.relative_to(ROOT)))
    if (OUT/'scene_amendments.jsonl').exists():
        amendments=rows(str(OUT.relative_to(ROOT)/'scene_amendments.jsonl'))
        for a in amendments:
            target=next(s for s in scenes if s['event_id']==a['event_id'])
            target.update(a['changes'])
    counts=[]
    for key in sorted({s['pattern'] for s in scenes}):
        ss=[s for s in scenes if s['pattern']==key]
        counts.append(dict(pattern=key,unique_passages=len({s['unique_group'] for s in ss}),unique_questions=len({s['unique_question'] for s in ss}),
            actual_solution_uses=len([s for s in ss if s['use']=='실제 풀이 활용']),
            actual_solution_question_count=len({s['unique_question'] for s in ss if s['use']=='실제 풀이 활용'}),
            passage_structure_only=len({s['unique_group'] for s in ss if s['use']=='지문 구조만'}),
            by_exam={f:dict(passages=len({s['unique_group'] for s in ss if s['exam_family']==f}),questions=len({s['unique_question'] for s in ss if s['exam_family']==f}),
                uses=sum(s['exam_family']==f and s['use']=='실제 풀이 활용' for s in ss)) for f in ['KICE','LEET','MEET']},
            evidence_event_ids=[s['event_id'] for s in ss],frequency_scope='현재 직접 추출한 근거 장면만의 하한; 미처리 코퍼스의 빈도나 대표성 추정 아님'))
    write('pattern_counts.json',counts)
    cp=load(str(OUT.relative_to(ROOT)/'checkpoint.json'))
    write('processing_status.json',dict(completed_first_pass_groups=len(cp['completed_groups']),
        pending_groups=[g['unique_group'] for g in GROUPS if g['status']=='추출 대기' and g['unique_group'] not in cp['completed_groups']],
        held_groups=[g for g in GROUPS if g['status']=='기존 보류 승계'],
        extracted_scenes=len(scenes),extracted_unique_questions=len({s['unique_question'] for s in scenes}),
        by_exam={f:dict(processed_groups=sum(g['exam_family']==f and g['unique_group'] in cp['completed_groups'] for g in GROUPS),
            scene_questions=len({s['unique_question'] for s in scenes if s['exam_family']==f}),uses=sum(s['exam_family']==f and s['use']=='실제 풀이 활용' for s in scenes)) for f in ['KICE','LEET','MEET']}))
    print('직접 추출',len(cp['completed_groups']),'groups',len(scenes),'장면',len({s['unique_question'] for s in scenes}),'문항',len(counts),'후보')

if __name__=='__main__':
    if sys.argv[1]=='record':
        for spec in json.loads(Path(sys.argv[2]).read_text()):print(record(spec))
    elif sys.argv[1]=='aggregate':aggregate()
