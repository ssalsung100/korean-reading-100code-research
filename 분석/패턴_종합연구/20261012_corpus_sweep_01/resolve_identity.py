"""직접 확인한 세 legacy 수록 중복만 연결한다. 원 자료에는 쓰지 않는다."""
from corpus_io import ROOT,OUT,load,rows,write,jsonl,packet,norm
import re

if (OUT/'identity_resolution.json').exists():raise RuntimeError('이미 반영한 중복 연결이다.')
es=rows(str(OUT.relative_to(ROOT)/'manifest_analyses.jsonl'))
gs=rows(str(OUT.relative_to(ROOT)/'manifest_groups.jsonl'))
qs=rows(str(OUT.relative_to(ROOT)/'manifest_questions.jsonl'))
res=[]
for old,case in [('C','BOK'),('D','BQG'),('H','AXA')]:
    legacy=next(e for e in es if e['analysis_id']=='독립풀이_03:'+old)
    target=next(e for e in es if e['analysis_id']=='PREP:'+case)
    a=packet(legacy['source_path']);b=load(target['source_path'])
    def body(text):
        text=re.sub(r'\*\*P\d+\.\*\*','',text)
        text=re.sub(r'^\s*\[\d+\s*[~～]\s*\d+\]\s*','',text)
        text=re.sub(r'^\s*다음\s*글을\s*읽고\s*물음에\s*답하시오\.?\s*','',text)
        return norm(text)
    assert body(a['passage_text'])==body(b['passage_text'])
    assert norm(a['stem'])==norm(b['stem'])
    assert [norm(x) for x in a['choices']]==[norm(x) for x in b['choices']]
    res.append(dict(analysis_id=legacy['analysis_id'],old_group=legacy['unique_group'],new_group=target['unique_group'],
        old_question=legacy['unique_question'],new_question=target['unique_question'],
        verification='본문 차이는 작업용 P1 표지·문항 범위·읽기 지시문뿐. 이를 제거하면 본문·발문·5선지 일치. 시험·연도·형·번호도 같음.',source_paths=[legacy['source_path'],target['source_path']]))
for name in ['manifest_groups.jsonl','manifest_questions.jsonl','manifest_analyses.jsonl','corpus_counts.json']:
    (OUT/('identity_initial_'+name)).write_bytes((OUT/name).read_bytes())
for r in res:
    legacy=next(e for e in es if e['analysis_id']==r['analysis_id']);legacy['unique_group']=r['new_group'];legacy['unique_question']=r['new_question']
    targetg=next(g for g in gs if g['unique_group']==r['new_group'])
    oldg=next(g for g in gs if g['unique_group']==r['old_group'])
    targetg['analysis_ids']+=oldg['analysis_ids'];targetg['source_paths']=sorted(set(targetg['source_paths']+oldg['source_paths']))
    gs=[g for g in gs if g['unique_group']!=r['old_group']]
    tq=next(q for q in qs if q['unique_question']==r['new_question']);oq=next(q for q in qs if q['unique_question']==r['old_question'])
    tq['analysis_ids']+=oq['analysis_ids'];tq['completed_analysis_ids']+=oq['completed_analysis_ids']
    qs=[q for q in qs if q['unique_question']!=r['old_question']]
    with (OUT/'duplicate_relations.jsonl').open('a') as f:f.write(__import__('json').dumps(dict(relation='작업용 표지 차이의 동일 지문·문항',**r),ensure_ascii=False)+'\n')
jsonl('manifest_groups.jsonl',gs);jsonl('manifest_questions.jsonl',qs);jsonl('manifest_analyses.jsonl',es)
o=load(str(OUT.relative_to(ROOT)/'execution_order.json'));o['groups']=[g for g in o['groups'] if g not in {r['old_group'] for r in res}];write('execution_order.json',o)
c=load(str(OUT.relative_to(ROOT)/'corpus_counts.json'));c['identity_resolved_groups']=len(gs);c['eligible_groups']=sum(g['status']=='추출 대기' for g in gs)
c['identity_resolved_completed_questions']=sum(q['completed'] for q in qs);c['repeated_completed_analyses']=c['all_completed_analyses']-c['identity_resolved_completed_questions']
c['by_exam']={f:dict(groups=sum(g['exam_family']==f and g['status']=='추출 대기' for g in gs),questions=sum(q['exam_family']==f and q['completed'] for q in qs)) for f in ['KICE','LEET','MEET']}
write('corpus_counts.json',c)
write('identity_resolution.json',dict(date='2026-10-12',resolutions=res,previous_group_count=500,current_group_count=len(gs),
    previous_unique_completed_questions=1672,current_unique_completed_questions=c['identity_resolved_completed_questions'],
    interpretation='처음 연결 집합의 임시 수에서 legacy C/D/H 수록 중복을 추가 제거했다. 기존 완료 원장은 변경하지 않는다.',
    provenance_correction=dict(group='G160',unique_group='U0142',stored_academic_year=2025,actual_academic_year=2026,
        actual_exam='2026학년도 6월 모평',record_id='ZD-answer_check-20260920-02',
        scope='G160 Q1~3의 저장 학년도 오연결 정정. G162의 2025학년도6월 원문은 별도 지문 유지.')))
print('고유 지문',len(gs),'추출 대상',c['eligible_groups'],'완료 고유 문항',c['identity_resolved_completed_questions'],'반복 분석',c['repeated_completed_analyses'])
