import json, collections, re
from corpus_io import ROOT,OUT,load,rows,write,jsonl
from record_synthesis import aggregate
from candidates import P

aggregate()
counts=load(str(OUT.relative_to(ROOT)/'pattern_counts.json'))
status=load(str(OUT.relative_to(ROOT)/'processing_status.json'))
cp=load(str(OUT.relative_to(ROOT)/'checkpoint.json'))
inventory=load(str(OUT.relative_to(ROOT)/'corpus_counts.json'))
scenes=[]
for path in sorted(OUT.glob('batch_*_scenes.jsonl')):scenes+=rows(str(path.relative_to(ROOT)))
if (OUT/'scene_amendments.jsonl').exists():
    for a in rows(str(OUT.relative_to(ROOT)/'scene_amendments.jsonl')):next(s for s in scenes if s['event_id']==a['event_id']).update(a['changes'])
groups=rows(str(OUT.relative_to(ROOT)/'group_extractions.jsonl'))
manifest=rows(str(OUT.relative_to(ROOT)/'manifest_groups.jsonl'))
questions=rows(str(OUT.relative_to(ROOT)/'manifest_questions.jsonl'))
held={g['unique_group'] for g in manifest if g['status']=='기존 보류 승계'}
inventory['held_linked_completed_questions']=sum(q['completed'] and q['unique_group'] in held for q in questions)
inventory['eligible_completed_unique_questions']=sum(q['completed'] and q['unique_group'] not in held for q in questions)
write('corpus_counts.json',inventory)
cards=[]
for c in counts:
    key=c['pattern'];name,D,E,F=P[key]
    ss=[s for s in scenes if s['pattern']==key]
    cards.append(dict(pattern=key,name=name,D=D,E=E,F=F,
        status='복수 실제 사례의 잠정 공통' if c['unique_passages']>1 else '단일 실제 사례의 새 후보',
        counts=c,concrete_examples=[dict(event_id=s['event_id'],B=s['B'],C=s['C'],A=s['A']) for s in ss[:6]],
        distinctions='100코드/기존 13후보의 재명명으로 확정하지 않음. 아래 경계·반례 문서에서 인접 후보 관계를 검토한다.'))
write('pattern_candidates.json',cards)
md=['# 코퍼스 종합 연구의 현재 결과','',
    f"고유 지문 그룹 {status['completed_first_pass_groups']}/{inventory['eligible_groups']}개를 1차 종합하여 {status['extracted_scenes']}개 판단 장면, {status['extracted_unique_questions']}개 고유 문항에 직접 연결했다. " + ('대상 지문의 1차 종합은 완료했다. 문항·선지별 전수 장면 추출과 심층 보완은 남아 있다.' if not status['pending_groups'] else f"다음 그룹은 {cp['next_group']}이다."),'',
    f"원장 7,605건은 출제 문항 수가 아니다. 현재 연결 집합은 완료·단일분석자 검토 기록 1,730건, 이에 연결된 고유 문항 {inventory['identity_resolved_completed_questions']}개, 반복 분석 {inventory['repeated_completed_analyses']}건이다. 기존 보류 지문에 붙은 완료 초기 분석 {inventory['held_linked_completed_questions']}개 문항도 별도 보존하여 이번 추출의 대상 문항은 {inventory['eligible_completed_unique_questions']}개이다. 추출 대상 지문은 {inventory['eligible_groups']}개이고 보류 지문 2개를 합한 연결 지문은 {inventory['identity_resolved_groups']}개다.",'',
    '이 수는 본문 정규화와 식별자 연결로 확정한 저장소 단위 수다. 실제 시험지 이미지 전수 대조에 따른 출제 이력의 최종 확정은 아니다. 완료 표시는 원 연구의 완료 상태를 승계하며 의미 타당성의 전수 재검증을 뜻하지 않는다.','',
    '1,730건은 준비 코퍼스의 consumed_sdss 1,663건, 초기 연구03/04의 25건, 코드 검토01/02의 single_analyst_reviewed 42건이다. 마지막 42건의 독립 절차·추가 검수 완료를 주장하지 않는다. 최초 blind·공식 대조·독립 판정·후속 수정의 관계는 원장 ID와 문서 경로에 별도로 보존한다.','',
    '|시험군|전체 대상 지문|현재 종합 지문|근거 장면의 고유 문항|실제 풀이 장면|','|---|---:|---:|---:|---:|']
for f in ['KICE','LEET','MEET']:
    x=status['by_exam'][f];md.append(f"|{f}|{inventory['by_exam'][f]['groups']}|{x['processed_groups']}|{x['scene_questions']}|{x['uses']}|")
md+=['','빈도는 아래 근거 장면에서만 센 하한이다. 지문 전체에 구조가 있더라도 실제 정오 판단이 활용하지 않은 관계는 풀이 사용으로 세지 않는다. 현재 추출하지 않은 장면·문항은 빈도 0이 아니라 미처리이다.','',
    '원장, 초기 연구, 단계별 MD, 문항별 완성본의 관계는 manifest_analyses.jsonl에서 추적한다. 완성본의 MD 178개와 디렉터리 내 전체 파일 182개는 부분 뷰다. G024/G370은 전체 지문 추출에서 보류를 유지하며 준비된 8 cases를 완료로 바꾸지 않았다.','',
    '최초 실행의 요청 모델 메타데이터는 체크포인트에 보존한다. 이번 재개에서도 정확한 런타임 모델 ID와 effort를 별도 검증하지 않았다. 기존 원장·동결 자료를 수정하거나 Git push를 하지 않았다.','',
    '## 현재 후보와 실제 근거','']
for card in cards:
    c=card['counts'];md+=['### '+card['name'],'',card['D'],'','적용과 경계: '+card['E'],'',f"현재 근거: {c['unique_passages']} 지문 / {c['unique_questions']} 문항 / {c['actual_solution_uses']} 풀이 장면 / 구조만 {c['passage_structure_only']} 지문.",'']
    for ex in card['concrete_examples'][:3]:md+=[f"- `{ex['event_id']}`: {ex['B']} {ex['C']}"]
    md+=['','구성 활용: '+card['F'],'']
(OUT/'현재_결과.md').write_text('\n'.join(md)+'\n')
uses=['# 교재·강의·신규 제작에 활용할 실제 장면','',
    '빈도와 별도로 중간 추론의 분명함, 오답이 바꾸는 요소, 전이의 조건을 기준으로 다음 장면을 보존한다. 현재 학생 오답률이나 난도 효과를 검증한 결과는 아니다.','']
for s in scenes:
    uses+=[f"## {s['event_id']} · {s['exam_family']} · {s['case_id']}",'','지문 배치: '+s['A'],'','선지 행동: '+s['B'],'','중간 추론: '+s['C'],'','제작 활용: '+s['F'],'','적용 제한: '+s['E'],'']
(OUT/'교재_강의_제작장면.md').write_text('\n'.join(uses)+'\n')
resolutions=rows(str(OUT.relative_to(ROOT)/'unclassified_resolutions.jsonl')) if (OUT/'unclassified_resolutions.jsonl').exists() else []
unclassified=[]
for g in groups:
    for x in g['unclassified']:
        r=next((r for r in reversed(resolutions) if r['unique_group']==g['unique_group'] and r['description']==x),None)
        unclassified.append(dict(unique_group=g['unique_group'],description=x,status=r['status'] if r else '후보 또는 미분류 보존',resolution=r))
jsonl('unclassified_scenes.jsonl',unclassified)
for b in sorted({s['batch'] for s in scenes}):
    gs=[g for g in groups if g['batch']==b];ss=[s for s in scenes if s['batch']==b]
    following=[g for g in groups if g['batch']>b]
    target=cp.get('batch_targets',{}).get(str(b),40)
    write(f'batch_{b:03d}_checkpoint.json',dict(batch=b,groups=[g['unique_group'] for g in gs],group_count=len(gs),scene_count=len(ss),
        last_group=gs[-1]['unique_group'],next_group=following[0]['unique_group'] if following else cp['next_group'],status=f'{target}개 지문 1차 종합 저장' if len(gs)==target else '배치 진행 중',
        files=f'batch_{b:03d}_scenes.jsonl',semantic_validity='근거 장면별 잠정 판정; 기계 검사를 의미 검증으로 간주하지 않음'))
print('집계·후보·활용 문서 갱신, 다음',cp['next_group'])
readme=OUT/'README.md'
if readme.exists():
    txt=readme.read_text();layer=rows(str(OUT.relative_to(ROOT)/'layer_candidates.jsonl')) if (OUT/'layer_candidates.jsonl').exists() else []
    ac=sum(r['layer'].startswith('A') for r in layer);bc=sum(r['layer'].startswith('B') for r in layer)
    sizes=collections.Counter(g['batch'] for g in groups)
    completed_sizes=[n for b,n in sorted(sizes.items()) if n==cp.get('batch_targets',{}).get(str(b),40)]
    lead=f"현재 **{len(cp['completed_groups'])}/{inventory['eligible_groups']}개 고유 지문 그룹을 1차 종합**, **{status['extracted_unique_questions']}개 고유 문항의 {len(scenes)}개 판단 장면**을 저장했다. 배치별 지문 수는 {'·'.join(map(str,completed_sizes))}개다. 판단 행동 후보 {len(cards)}개, 지문 전개 후보 {ac}개, 발문·선지 후보 {bc}개를 근거와 함께 보존했다. 서로 다른 층위의 후보 수를 더해 하나의 풀이 기본기 수로 해석하지 않는다."
    txt=re.sub(r'현재 \*\*\d+/\d+개 고유 지문 그룹.*?해석하지 않는다\.',lead,txt,flags=re.S,count=1)
    txt=re.sub(r'나머지 \*\*\d+개 지문\*\*',f"나머지 **{len(status['pending_groups'])}개 지문**",txt)
    prev=next(g for g in manifest if g['unique_group']==cp['last_completed_group'])
    if cp['next_group']:
        nxt=next(g for g in manifest if g['unique_group']==cp['next_group'])
        txt=re.sub(r'마지막 완료는 \*\*.*?\*\*, 다음은 \*\*.*?\*\*이다\.',f"마지막 완료는 **{cp['last_completed_group']} / {','.join(prev['operational_groups'])}**, 다음은 **{cp['next_group']} / {','.join(nxt['operational_groups'])}**이다.",txt)
        txt=re.sub(r'corpus_io\.py show \d+ 1',f"corpus_io.py show {int(cp['next_group'][1:])} 1",txt)
    overview=', '.join(f'`batch_{b:03d}_scenes.jsonl` {sum(s["batch"]==b for s in scenes)}장면' for b in sorted(sizes))
    txt=re.sub(r'`batch_001_scenes\.jsonl`.*?에 A~F를 분리했다\.',overview+'에 A~F를 분리했다.',txt,flags=re.S,count=1)
    if cp['next_batch'] is not None:
        txt=re.sub(r'새 파일 `author_\d+\.py`',f'새 파일 `author_{cp["next_batch"]:03d}.py`',txt)
    readme.write_text(txt)
