"""이 실행 폴더에만 기록하는 식별·근거·집계 보조 도구. 의미 판정은 하지 않는다."""
import collections, hashlib, html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BASE = ROOT / 'data/기본기_연구'

def load(path):
    return json.loads((ROOT / path).read_text())

def rows(path):
    return [json.loads(s) for s in (ROOT / path).read_text().splitlines() if s.strip()]

def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def jsonl(name, values):
    (OUT / name).write_text(''.join(json.dumps(v, ensure_ascii=False) + '\n' for v in values))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def norm(text):
    text = html.unescape(str(text or ''))
    text = re.sub(r'^- (?:원본|단원):.*$', '', text, flags=re.M)
    text = re.sub(r'\*\*P\d+\.\*\*', '', text)
    text = re.sub(r'다음 글을 읽고 물음에 답하시오\.', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    return re.sub(r'[^\w가-힣]', '', text)

def digest(text):
    return hashlib.sha256(norm(text).encode()).hexdigest()

def choice_texts(items):
    return [x.get('text',str(x)) if isinstance(x,dict) else x for x in (items or [])]

def packet(path):
    text = (ROOT / path).read_text()
    p = re.split(r'## (?:지문|제시문)\s*\n', text, maxsplit=1)[-1]
    p = re.split(r'## (?:문항|문제)\s*\n', p, maxsplit=1)
    passage = p[0]
    rest = p[1] if len(p) > 1 else ''
    s = re.split(r'## (?:선택지|선지)\s*\n', rest, maxsplit=1)
    choices = re.split(r'[①②③④⑤]\s*', s[1])[1:] if len(s) > 1 else []
    return dict(passage_text=passage.strip(), stem=s[0].strip(), choices=[x.strip() for x in choices])

def inventory():
    if (OUT / 'manifest_groups.jsonl').exists():
        raise RuntimeError('manifest가 이미 있다. 재선정하지 않고 재개한다.')
    idx = load('data/기본기_연구/research_data_index_enriched_v2.json')['case_to_group']
    queue = rows('data/기본기_연구/astra_handoff_queue.jsonl')
    processed = rows('data/기본기_연구/astra_handoff_processed.jsonl')
    bycase = collections.defaultdict(list)
    for line, r in enumerate(queue, 1):
        bycase[r.get('case')].append(dict(line=line, **r))
    qp, pp = {}, {}
    for family in ['kice', 'meet']:
        for line, q in enumerate(rows(f'data/{family}_questions.jsonl'), 1):
            qp[q['question_id']] = (q, f'data/{family}_questions.jsonl', line)
        for line, p in enumerate(rows(f'data/{family}_passages.jsonl'), 1):
            pp[p.get('passage_id',p.get('group_id'))] = (p, f'data/{family}_passages.jsonl', line)
    entries, evidence = [], []
    for r in idx:
        source = load(r['blind_source'])
        entries.append(dict(analysis_id='PREP:'+r['case_id'], case_id=r['case_id'],
            operational_group=r['passage_group'], origin='prepared', completed=r['manifest_status']=='consumed_sdss',
            exam_family=r['exam_family'], stored_passage_id=r['passage_id'], stored_question_id=r['question_id'],
            source_path=r['blind_source'], canonical_source_path=r.get('canonical_source_path'),
            source=source, raw_records=[dict(record_id=x['record_id'], stage=x['stage'], line=x['line']) for x in bycase[r['case_id']]],
            provenance_conflicts=r.get('provenance_conflicts'), academic_year=r.get('academic_year'), exam_type=r.get('exam_type')))
    legacy = []
    for folder, cases, seals in [
        ('독립풀이_03','ABCDEFGHIJKL',['봉인_연결.json','봉인_추가연결_JL.json']),
        ('독립풀이_04','MNOPQSTUVWXYZ',['봉인_KICE.json','봉인_LM.json'])]:
        ids = {}
        for f in seals:
            obj = load('data/기본기_연구/'+folder+'/'+f)
            ids.update(obj.get('cases', obj.get('records',obj)))
        for case in cases:
            info = ids.get(case,{})
            if not isinstance(info, dict): continue
            qid = info.get('sourceID',info.get('source_id',info.get('canonical_question_id')))
            doc = 'data/기본기_연구/'+folder+'/'+case+'_02_정답대조와_독립코드.md'
            if not qid:
                matches = re.findall(r'(?:KICE|LEET|MEET)-[^`\s]+-Q\d+', (ROOT/doc).read_text())
                qid = matches[0].rstrip('.,') if matches else None
            pid = info.get('passageID',info.get('passage_id',info.get('canonical_passage_id')))
            path = 'data/기본기_연구/'+folder+'/packets/'+case+'.md'
            src = packet(path)
            if qid in qp:
                q=qp[qid][0]; pid=q.get('passage_id',q.get('group_id'));p=pp[pid][0]
                canonical_text=p.get('passage_text',p.get('context_markdown'))
                if canonical_text:src=dict(passage_text=canonical_text,stem=q['stem'],choices=choice_texts(q['choices']))
            entry=dict(analysis_id=folder+':'+case,case_id=case, operational_group=folder+':'+case,origin=folder,
                completed=True, exam_family=(qid or '').split('-')[0] or info.get('exam_family'),
                stored_passage_id=pid,stored_question_id=qid,source_path=path,source=src,
                canonical_source_path=qp[qid][1] if qid in qp else info.get('source_path'),
                raw_records=[dict(record_id=x['record_id'],stage=x['stage'],line=x['line']) for x in bycase[case]] if folder.endswith('04') else [],
                solution_paths=[str(x.relative_to(ROOT)) for x in (BASE/folder).glob(case+'_0*.md')],
                independent_blind=True)
            entries.append(entry);legacy.append(entry['analysis_id'])
    review_counts = {}
    for f in ['code_reviews_01.jsonl','code_reviews_02.jsonl']:
        review_counts[f] = 0
        for line,r in enumerate(rows('data/기본기_연구/'+f),1):
            qid=r.get('local_question_id');pid=r.get('passage_id')
            src={}
            if qid in qp:
                q=qp[qid][0];pid=q.get('passage_id',q.get('group_id'));p=pp[pid][0]
                src=dict(passage_text=p.get('passage_text',p.get('context_markdown','')),stem=q['stem'],choices=choice_texts(q['choices']))
            entries.append(dict(analysis_id=f+':'+str(line),case_id=r['case_id'],origin=f,completed=True,
                operational_group=f+':'+str(line),exam_family=r['exam_family'],stored_passage_id=pid,stored_question_id=qid,
                source_path=qp[qid][1] if qid in qp else r.get('source_path'),canonical_source_path=r.get('source_path'),
                source=src,review_record=dict(path='data/기본기_연구/'+f,line=line),raw_records=[],
                independent_blind=False,source_status=r.get('source_status'),review_status=r.get('review_status')))
            review_counts[f]+=1
    # 同一 저장 ID의 부분 복원·표현 차이는 한 원문의 수록 변형으로 연결한다.
    # 같은 ID인데 본문이 크게 다른 경우는 자동 병합하지 않고 충돌로 보존한다.
    parent=list(range(len(entries)))
    def find(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    def union(i,j):
        a,b=find(i),find(j)
        if a!=b:parent[max(a,b)]=min(a,b)
    hash_seen={}; id_seen=collections.defaultdict(list);conflicts=[]
    import difflib
    for i,e in enumerate(entries):
        text=norm(e['source'].get('passage_text',''))
        e['passage_content_sha256']=digest(text) if text else None
        e['question_content_sha256']=digest(str(e['source'].get('stem',''))+'\n'+json.dumps(choice_texts(e['source'].get('choices',[])),ensure_ascii=False)) if e['source'].get('stem') else None
        if text:
            key=(e['exam_family'],e['passage_content_sha256'])
            if key in hash_seen:union(i,hash_seen[key])
            else:hash_seen[key]=i
        pid=e.get('stored_passage_id')
        if pid:
            for j in id_seen[(e['exam_family'],pid)]:
                other=norm(entries[j]['source'].get('passage_text',''))
                ratio=(1.0 if text==other else difflib.SequenceMatcher(None,text,other).ratio()) if text and other else None
                if not text or not other or ratio>=.96:union(i,j)
                elif not any(c['left']==entries[j]['analysis_id'] and c['right']==e['analysis_id'] for c in conflicts):
                    conflicts.append(dict(left=entries[j]['analysis_id'],right=e['analysis_id'],stored_passage_id=pid,similarity=ratio,status='본문 상이: 자동 병합 금지'))
            if not any(entries[j]['passage_content_sha256']==e['passage_content_sha256'] for j in id_seen[(e['exam_family'],pid)]):
                id_seen[(e['exam_family'],pid)].append(i)
    clusters=collections.defaultdict(list)
    for i,e in enumerate(entries):clusters[find(i)].append(e)
    groups=[]; question_rows=[];dups=[]
    for n,cluster in enumerate(clusters.values(),1):
        gid=f'U{n:04d}'
        qq=collections.defaultdict(list)
        for e in cluster:
            key=e.get('question_content_sha256') or e.get('stored_question_id') or e['analysis_id']
            # 동일 qID의 공백·선지 배열 형식 차이도 반복 분석으로 연결한다.
            existing=next((k for k,v in qq.items() if e.get('stored_question_id') and e['stored_question_id'] in [x.get('stored_question_id') for x in v]),None)
            qq[existing or key].append(e)
        qids=[]
        for k,es in qq.items():
            q=f'{gid}-Q{len(qids)+1:02d}';qids.append(q)
            for e in es:e['unique_group']=gid;e['unique_question']=q
            question_rows.append(dict(unique_question=q,unique_group=gid,exam_family=es[0]['exam_family'],
                stored_question_ids=sorted({e['stored_question_id'] for e in es if e.get('stored_question_id')}),
                analysis_ids=[e['analysis_id'] for e in es],completed_analysis_ids=[e['analysis_id'] for e in es if e['completed']],
                completed=any(e['completed'] for e in es)))
            if len(es)>1:dups.append(dict(relation='동일 원문 문항의 반복 분석/수록',unique_question=q,analysis_ids=[e['analysis_id'] for e in es]))
        op=sorted({e['operational_group'] for e in cluster if e['origin']=='prepared'})
        hold=any(g in ['G024','G370'] for g in op)
        groups.append(dict(unique_group=gid,exam_family=cluster[0]['exam_family'],
            operational_groups=op,analysis_ids=[e['analysis_id'] for e in cluster],
            stored_passage_ids=sorted({e['stored_passage_id'] for e in cluster if e.get('stored_passage_id')}),
            unique_questions=qids,completed_question_count=sum(any(e['completed'] for e in es) for es in qq.values()),
            status='기존 보류 승계' if hold else ('추출 대기' if any(e['completed'] for e in cluster) else '미완료'),
            source_paths=sorted({e['source_path'] for e in cluster if e.get('source_path')})))
        if len(op)>1:dups.append(dict(relation='동일 지문에 대한 복수 운영 그룹',unique_group=gid,operational_groups=op))
    jsonl('manifest_groups.jsonl',groups)
    jsonl('manifest_questions.jsonl',question_rows)
    jsonl('manifest_analyses.jsonl',[{k:v for k,v in e.items() if k!='source'} for e in entries])
    jsonl('duplicate_relations.jsonl',dups)
    jsonl('identifier_conflicts.jsonl',conflicts)
    # 내용 자체는 배치별로 필요한 단위만 표시한다. manifest에 전 코퍼스 본문을 복사하지 않는다.
    counts=dict(raw_records=len(queue),raw_unique_ids=len({r['record_id'] for r in queue}),
        raw_stages=dict(collections.Counter(r['stage'] for r in queue)),processed_records=len(processed),
        pending_raw=len({r['record_id'] for r in queue}-{r['source_record_id'] for r in processed}),
        prepared_cases=len(idx),prepared_completed_cases=sum(e['completed'] for e in entries if e['origin']=='prepared'),
        prepared_completed_operational_groups=len({e['operational_group'] for e in entries if e['origin']=='prepared' and e['completed']}),
        legacy_completed_analyses=len(legacy),review_counts=review_counts,all_completed_analyses=sum(e['completed'] for e in entries),
        identity_resolved_groups=len(groups),eligible_groups=sum(g['status']=='추출 대기' for g in groups),
        identity_resolved_completed_questions=sum(q['completed'] for q in question_rows),
        repeated_completed_analyses=sum(e['completed'] for e in entries)-sum(q['completed'] for q in question_rows),
        by_exam={f:dict(groups=sum(g['exam_family']==f and g['status']=='추출 대기' for g in groups),
              questions=sum(q['exam_family']==f and q['completed'] for q in question_rows)) for f in ['KICE','LEET','MEET']},
        identity_limit='본문 정규화 일치/저장ID와 본문 0.96 이상 일치의 연결 집합. 시험지 이미지 전수 대조에 의한 출제 이력 확정은 아님. 식별자 충돌과 unresolved source를 별도 보존.',
        holds={'G024':['DR','DS','DT','DU'],'G370':['BAP','BAQ','BAR','BAS']},
        complete_view_files=len(list((ROOT/'분석/기본기_연구/문항별_완성본').glob('*.md'))))
    write('corpus_counts.json',counts)
    protected=set()
    for folder in ['data/기본기_연구','분석/기본기_연구','분석/패턴_종합연구']:
        for p in (ROOT/folder).rglob('*'):
            if p.is_file() and OUT not in p.parents:protected.add(p)
    for e in entries:
        for key in ['canonical_source_path','source_path']:
            p=ROOT/(e.get(key) or 'NONEXISTENT')
            if p.is_file():protected.add(p)
    for path in ['data/kice_passages.jsonl','data/kice_questions.jsonl','data/meet_passages.jsonl','data/meet_questions.jsonl','data/sdss_100codes_catalog.json','AGENTS.md','DB_자산_인덱스.md','새대화용_평가원형_지문문항_생성_인수인계.md']:
        protected.add(ROOT/path)
    write('input_hashes.json',{str(p.relative_to(ROOT)):sha(p) for p in sorted(protected)})
    write('checkpoint.json',dict(run_id=OUT.name,date='2026-10-12',status='진행 중',
        requested_model='GPT-6.1 Sol',requested_effort='high',runtime_exact_model_verified=False,
        other_models_called=False,existing_files_written=False,git_push=False,
        completed_groups=[],last_completed_group=None,next_group=groups[0]['unique_group'],
        next_action='고유 지문 그룹 순서대로 기존 풀이 종합; 의미 판정은 직접 작성',batch_size=40,
        semantic_validity='잠정 귀납. 자동 검사는 식별자·근거 포인터·파일 무결성만 검증한다.'))
    print(json.dumps(counts,ensure_ascii=False,indent=2))

def get_source(e):
    if e['origin']=='prepared':return load(e['source_path'])
    if e['origin'].startswith('독립풀이'):return packet(e['source_path'])
    qid=e['stored_question_id']
    family=e['exam_family'].lower()
    if family in ['kice','meet']:
        q=next((r for r in rows(f'data/{family}_questions.jsonl') if r['question_id']==qid),None)
        if q:
            p=next(r for r in rows(f'data/{family}_passages.jsonl') if r.get('passage_id',r.get('group_id'))==q.get('passage_id',q.get('group_id')))
            return dict(passage_text=p.get('passage_text',p.get('context_markdown','')),stem=q['stem'],choices=choice_texts(q['choices']))
    return {}

def baseline():
    import subprocess
    paths=subprocess.check_output(['rg','--files','data/기본기_연구','분석/기본기_연구','분석/패턴_종합연구'],cwd=ROOT,text=True).splitlines()
    protected={ROOT/p for p in paths if OUT not in (ROOT/p).parents}
    for e in rows(str(OUT.relative_to(ROOT)/'manifest_analyses.jsonl')):
        for k in ['source_path','canonical_source_path']:
            p=ROOT/(e.get(k) or 'NONEXISTENT')
            if p.is_file():protected.add(p)
    for p in ['data/kice_passages.jsonl','data/kice_questions.jsonl','data/meet_passages.jsonl','data/meet_questions.jsonl','data/sdss_100codes_catalog.json','AGENTS.md','DB_자산_인덱스.md','새대화용_평가원형_지문문항_생성_인수인계.md']:
        protected.add(ROOT/p)
    if not (OUT/'input_hashes.json').exists():write('input_hashes.json',{str(p.relative_to(ROOT)):sha(p) for p in sorted(protected)})
    if not (OUT/'checkpoint.json').exists():write('checkpoint.json',dict(run_id=OUT.name,date='2026-10-12',status='진행 중',requested_model='GPT-6.1 Sol',requested_effort='high',runtime_exact_model_verified=False,other_models_called=False,existing_files_written=False,git_push=False,completed_groups=[],last_completed_group=None,next_group='U0001',next_action='고유 지문 그룹 순서대로 기존 풀이 종합; 의미 판정은 직접 작성',batch_size=40,semantic_validity='잠정 귀납; 자동 검사는 의미 타당성을 확정하지 않는다.'))
    print('읽기 전용 기준 파일',len(protected),'해시 저장')

def show(start,count):
    brief='brief' in sys.argv
    groups=rows(str(OUT.relative_to(ROOT)/'manifest_groups.jsonl'))
    entries=rows(str(OUT.relative_to(ROOT)/'manifest_analyses.jsonl'))
    byid={e['analysis_id']:e for e in entries}
    queue=rows('data/기본기_연구/astra_handoff_queue.jsonl');bycase=collections.defaultdict(list)
    for line,r in enumerate(queue,1):bycase[r.get('case')].append(dict(line=line,**r))
    for g in groups[start-1:start-1+count]:
        print('\n###',g['unique_group'],g['exam_family'],','.join(g['operational_groups']),g['status'])
        es=[byid[i] for i in g['analysis_ids'] if byid[i]['completed']]
        if not es:continue
        src=get_source(es[0]);pt=src.get('passage_text','')
        paras=[x.strip() for x in pt.split('\n\n') if x.strip()]
        print('문단 첫 문장',json.dumps([p.split('. ')[0][:70] for p in paras if not p.startswith('- ')][:8],ensure_ascii=False))
        for e in es:
            if e['origin']!='prepared':
                print('중복/초기분석',e['analysis_id'],e['unique_question'],e.get('solution_paths',e.get('review_record')))
                continue
            rr=bycase[e['case_id']];ss=get_source(e)
            print('CASE',e['case_id'],e['unique_question'],'발문',str(ss.get('stem'))[:90])
            for r in rr:
                p=r['payload']
                if r['stage']=='blind':
                    print('blind',r['line'],json.dumps({k:v for k,v in p.items() if any(t in k for t in (['logic','distractor'] if brief else ['logic','intermediate','distractor']))},ensure_ascii=False))
                elif r['stage']=='answer_check':
                    if p.get('match') is False or p.get('revision_needed') or p.get('discrepancy_analysis'):
                        print('확정/정정',r['line'],json.dumps({k:v for k,v in p.items() if k in ['code_free_logic','logic_frozen','logic','logic_without_codes_fixed','official_answer','match','correction','discrepancy_analysis']},ensure_ascii=False))
                elif r['stage'] in ['depth_backfill','boundary_revision']:
                    selected={k:v for k,v in p.items() if k in ['code_free_refinement','refinement','logic','scope_resolution','semantic_effect','boundary_or_generation_impact','evidence_additions']}
                    print('후속',r['stage'],r['line'],json.dumps(selected if brief else p,ensure_ascii=False)[:(950 if brief else 1400)])
        for op in g['operational_groups']:
            for r in bycase[op]:
                if r['stage']=='induction':
                    p=r['payload'];print('기존귀납',r['line'],json.dumps({k:v for k,v in p.items() if k in ['source_quality','counterexample_limit','kice_generation_candidate','generation_candidate','limits']},ensure_ascii=False))

if __name__=='__main__':
    if sys.argv[1]=='inventory':inventory()
    elif sys.argv[1]=='show':show(int(sys.argv[2]),int(sys.argv[3]))
    elif sys.argv[1]=='baseline':baseline()
