"""재개 순서의 소규모 원문·완성풀이 열람. 의미 분류는 수행하지 않는다."""
import json,re,sys,collections
from corpus_io import ROOT,OUT,rows,load,get_source
gs={g['unique_group']:g for g in rows(str(OUT.relative_to(ROOT)/'manifest_groups.jsonl'))}
aa={a['analysis_id']:a for a in rows(str(OUT.relative_to(ROOT)/'manifest_analyses.jsonl'))}
rr=collections.defaultdict(list)
for n,r in enumerate(rows('data/기본기_연구/astra_handoff_queue.jsonl'),1):
    rr[r.get('case')].append(dict(line=n,**r))
cp=load(str(OUT.relative_to(ROOT)/'checkpoint.json'))
order=load(str(OUT.relative_to(ROOT)/'execution_order.json'))['groups']
ids=sys.argv[1:]
if len(ids)==1 and ids[0].isdigit():ids=[x for x in order if x not in cp['completed_groups']][:int(ids[0])]
for gid in ids:
    g=gs[gid];es=[aa[x] for x in g['analysis_ids'] if aa[x]['completed']]
    print('\n###',gid,g['exam_family'],','.join(g['operational_groups']))
    src=get_source(es[0]);text=src.get('passage_text','')
    ps=[p.strip() for p in text.split('\n\n') if p.strip() and not p.startswith('- ')]
    if len(ps)<3:
        ss=re.split(r'(?<=다\.)\s+',text)
        ps=[ss[0],*ss[1::max(1,len(ss)//6)],ss[-1]] if ss else []
    selected=ps if len(ps)<=3 else [ps[0],ps[len(ps)//2],ps[-1]]
    print('원문 전개표지',json.dumps([p[:65] for p in selected],ensure_ascii=False))
    for e in es:
        if e['origin']!='prepared':
            print('별도 기존기록',e['analysis_id'],e.get('solution_paths',e.get('review_record')));continue
        case=e['case_id'];s=get_source(e)
        print(case,'발문',str(s.get('stem',''))[:80])
        for r in rr[case]:
            p=r['payload'];st=r['stage']
            if st=='blind':
                v={k:v for k,v in p.items() if 'logic' in k}
            elif st=='answer_check':
                v={k:v for k,v in p.items() if any(t in k for t in ['correction','discrepancy','unresolved','refinement']) and v}
                v={k:x for k,x in v.items() if x not in ['없음',None]}
                if p.get('match') is False:
                    v.update(match=False,official_answer=p.get('official_answer'))
                    v.update({k:v for k,v in p.items() if 'logic' in k})
            elif st in ['depth_backfill','boundary_revision']:
                v={k:v for k,v in p.items() if any(t in k for t in ['refinement','logic','resolution','semantic','evidence','boundary','unresolved'])}
                if not v:v=p
            elif st=='independent_code':
                v={k:v for k,v in p.items() if k=='unresolved' and v}
            else:continue
            if v:print(st,r['line'],json.dumps(v,ensure_ascii=False))
