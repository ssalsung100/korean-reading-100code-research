"""선지·인용·답·범위 연결 및 창작 규칙의 반모형을 검사한다. 의미 검토를 대체하지 않는다."""
import itertools
import json
import re
from pathlib import Path

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
OLD=OUT.parent/'20261009_pilot_01'
def read(p): return json.loads(p.read_text())
def rows(p): return [json.loads(x) for x in p.read_text().splitlines()]
def pointer(obj, path):
    for part in path.strip('/').split('/'):
        obj=obj[int(part)] if isinstance(obj,list) else obj[part]
    return obj
def num(v):
    if str(v) in '①②③④⑤': return '①②③④⑤'.index(str(v))+1
    return int(v)

events=rows(OUT/'revised_events.jsonl'); audits=rows(OUT/'citation_audit.jsonl')
raw=(ROOT/'data/기본기_연구/astra_handoff_queue.jsonl').read_text().splitlines()
manifest=read(OLD/'sample_manifest.json')
discovery={c for s in manifest['samples'] if s['split']=='discovery' for c in s['case_ids']}
validation={c for s in manifest['samples'] if s['split']!='discovery' for c in s['case_ids']}
assert len(events)==46 and len({e['event_id'] for e in events})==46
assert {e['case_id'] for e in events}==discovery
assert not {e['case_id'] for e in events}&validation
assert not {e['passage_group'] for e in events}&{'G024','G370'}
checks=0
for e in events:
    src=read(ROOT/e['source_path'])
    assert src['stem']==e['stem']
    answer=json.loads(raw[e['answer_record_line']-1])
    assert answer['record_id']==e['answer_record_id']
    assert num(answer['payload']['official_answer'])==e['official_answer_reused']
    for j in e['judgments']:
        assert src['choices'][j['choice_id']-1]==j['text']
        assert (j['answer_action']=='정답으로 선택') == (j['choice_id']==e['official_answer_reused'])
        checks+=1
    for x in e.get('original_evidence_reused',[]):
        original=pointer(src,x['json_pointer'])
        assert original[x['char_start']:x['char_end']]==x['quote'],e['event_id']
    if 'existing_support' in e:
        s=e['existing_support'];record=json.loads(raw[s['raw_line']-1])
        assert pointer(record,s['json_pointer'])==s['quote']
        assert e['passage_support']['quote'] in src['passage_text']
for a in audits:
    record=json.loads(raw[a['raw_line']-1])
    assert record['record_id']==a['record_id']
    assert a['corrected_support']
    for q in a['old_quote_pointers']+a['corrected_support']:
        assert pointer(record,q['json_pointer'])==q['quote']
routes=read(OUT/'answer_route_audit.json')
assert len(routes)==39 and all(r['after_answer_events'] for r in routes)
assert {r['case_id'] for r in routes if not r['before_answer_events']}=={'AA','AH','AJP'}
boundaries=read(OUT/'boundary_links.json')
by_id={e['event_id']:e for e in events}
for b in boundaries:
    e=by_id[b['event_id']]
    assert b['case_id']==e['case_id']
    assert set(b['choice_ids']) <= {j['choice_id'] for j in e['judgments']}
assert any(b['pattern_id']=='P07' and b['event_id']=='E032' and b['choice_ids']==[1] for b in boundaries)
assert any(b['pattern_id']=='S01' and b['event_id']=='E014' and b['choice_ids']==[2] for b in boundaries)
matrix=(OUT/'02_패턴별_활용_매트릭스.md').read_text()
assert all(f'## {p} ' in matrix for p in [f'P{i:02d}' for i in range(1,8)]+[f'S{i:02d}' for i in range(1,7)])

# 직접 후보 하나와 교차 후보 한 쌍을 갖는 국소 모형이다.
# 경로의 필요조건을 전체 채택의 필요조건으로 잘못 확장하는 주장의 반모형을 찾는다.
models=[]
for S,T,I,M in itertools.product([False,True],repeat=4):
    D=S and T;C=I and M;A=D or C
    models.append(dict(S=S,T=T,I=I,M=M,D=D,C=C,A=A))
counterexamples={
 '시각대응이_없으면_최종채택_불가':[x for x in models if not x['T'] and x['A']],
 '출처만_확인되면_직접채택':[x for x in models if x['S'] and not x['D']],
 '내용일치면_교차채택':[x for x in models if x['M'] and not x['C']]
}
assert all(counterexamples.values())
def state(records,pairs):
    direct=any(s and t for s,t in records)
    cross=any(i and m for i,m in pairs)
    return [direct,cross,direct or cross]
cases={
 '갑_변경전':state([(True,True),(True,False)],[(True,True)]),
 '갑_변경후':state([(True,False),(True,False)],[(True,True)]),
 '을_변경전':state([(False,True),(False,True)],[(False,True)]),
 '을_변경후':state([(False,True),(False,True),(False,True)],[(False,True),(True,True)]),
 '병_변경후':state([(True,False)],[])
}
assert cases=={'갑_변경전':[True,True,True],'갑_변경후':[False,True,True],
               '을_변경전':[False,False,False],'을_변경후':[False,True,True],'병_변경후':[False,False,False]}
# 갑의 둘째 기록 출처와 을 새 기록의 시각 검사는 본문에 미지정이다.
# 가능한 모든 완성에서 결과가 같은지 확인한다. 위 대표 모형 값을 확정 사실로 오인하지 않는다.
for second_source,new_time in itertools.product([False,True],repeat=2):
    assert state([(True,False),(second_source,False)],[(True,True)])==[False,True,True]
    assert state([(False,True),(False,True),(False,new_time)],[(False,True),(True,True)])==[False,True,True]
mutations={
 '갑_독립성도_취소':state([(True,False),(False,False)],[(False,True)]),
 '을_새기록도_복사':state([(False,True)]*3,[(False,True)]*2),
 '병_시각대응_확인':state([(True,True)],[])
}
assert [v[2] for v in mutations.values()]==[False,False,True]
broken=[];link_count=0
for p in OUT.glob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        target=target.strip('<>')
        if '://' in target or target.startswith('#'): continue
        f=target.split('#')[0]
        if not f: continue
        link_count+=1
        if not (p.parent/f).exists(): broken.append([p.name,target])
assert not broken,broken
report={'passed':True,'revised_events':46,'citation_audits':43,'choice_links_checked':checks,
        'answer_routes_checked':39,'added_answer_events':3,'boundary_links_checked':len(boundaries),
        'patterns_with_A_to_F_analysis':13,'markdown_file_links_checked':link_count,
        'discovery_only':True,'validation_semantic_analysis':False,'other_models_called':False,
        'hold_groups_entered':[],'prototype_cases':cases,'prototype_unknown_fields_all_completions_checked':True,
        'prototype_counterexamples':counterexamples,'prototype_condition_mutations':mutations,
        'limitations':['문자열·좌표 점검은 인용의 의미적 충분성을 자동 보증하지 않음',
                      '창작 문항의 논리 모형은 제작자의 본문 해석에 기초함; 독립 독자·학생 검증 아님',
                      '보존 해시 검사는 preservation_report.json으로 별도 기록']}
(OUT/'validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('검증 통과:',checks,'선지 연결, 43 인용, 39 정답 경로, 22 경계 연결, 13 후보, 창작 조건 반모형 및 미지정 조건 완성 검사')
