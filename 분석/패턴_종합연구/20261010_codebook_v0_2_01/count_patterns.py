"""pattern_ids가 아닌 관계·상태로 고유 단위 계수. 파일을 수정하지 않는다."""
import json
from pathlib import Path

POSITIVE={'structure_present','item_utilized','solution_helpful','explanatory_only'}
def accepted(relation):
    if relation['decision']=='confirmed_inherited':
        return True  # 기존 발견용 분석 승계 계수이며 신규 검증 통과가 아니다.
    if relation['decision']!='confirmed_new':
        return False
    evidence=relation.get('new_evidence',{})
    return (evidence.get('canonical_checked') is True
            and evidence.get('minimum_evidence_met') is True
            and bool(evidence.get('references'))
            and bool(evidence.get('reasoning')))

def count_patterns(events,pattern_ids):
    result={}
    for pid in pattern_ids:
        linked=[]
        for event in events:
            for relation in event['relations']:
                if relation['decision']=='confirmed_inherited' and event.get('sample_split')!='discovery':
                    continue
                if relation['pattern_id']==pid and accepted(relation):
                    linked.append((event,relation))
        def subset(role): return [(e,r) for e,r in linked if role in r['pattern_relation']]
        def unique(items,key):return len({e[key] for e,r in items})
        evidence=[(e,r) for e,r in linked if POSITIVE&set(r['pattern_relation'])]
        structure=subset('structure_present'); utilized=subset('item_utilized'); helpful=subset('solution_helpful')
        excluded_structure={e['event_id'] for e,r in structure if 'item_utilized' not in r['pattern_relation']}
        by_family={}
        for family in ['KICE','LEET','MEET']:
            part=[(e,r) for e,r in utilized if e['exam_family']==family]
            by_family[family]={'passages':unique(part,'passage_id'),'questions':unique(part,'question_id')}
        result[pid]={
          'evidence_events':unique(evidence,'event_id'),'observed_passages':unique(structure,'passage_id'),
          'utilized_passages':unique(utilized,'passage_id'),'utilized_questions':unique(utilized,'question_id'),
          'source_questions':unique(evidence,'question_id'),'structure_only_events':sorted(excluded_structure),
          'event_ids':sorted({e['event_id'] for e,r in evidence}),
          'utilized_events':unique(utilized,'event_id'),'solution_helpful_events':unique(helpful,'event_id'),
          'solution_helpful_questions':unique(helpful,'question_id'),
          'explanatory_events':unique(subset('explanatory_only'),'event_id'),'by_exam_family':by_family,
          'counts_are':'목적 표본의 연결 근거; 원 코퍼스 발생률 아님'}
    return result

if __name__=='__main__':
    base=Path(__file__).resolve().parent
    cards=json.loads((base/'codebook_v0.2.json').read_text())['cards']
    events=[json.loads(x) for x in (base/'event_mapping_v0.2.jsonl').read_text().splitlines()]
    print(json.dumps(count_patterns(events,[c['pattern_id'] for c in cards]),ensure_ascii=False,indent=2))
