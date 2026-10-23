"""허용된 기존 분석만 대조하며 검증용 원문은 열지 않는다. 동결 뒤에는 재작성하지 않는다."""
import copy
import hashlib
import json
import sys
from pathlib import Path
sys.dont_write_bytecode=True
from count_patterns import count_patterns

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
if (OUT/'freeze_manifest.json').exists():raise SystemExit('동결 후 재작성 금지. verify_freeze.py를 사용한다.')
def read(p):return json.loads(p.read_text())
def save(name,obj):(OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
cards=read(OUT/'codebook_v0.2.json')['cards']
schema=read(OUT/'annotation_schema.json')
template=read(OUT/'external_annotation_template.json')
assert schema['type']=='object'
assert set(schema['required'])<=set(template)
assert template['template_only'] and template['relations'][0]['decision']=='unconfirmed'
events=[json.loads(s) for s in (OUT/'event_mapping_v0.2.jsonl').read_text().splitlines()]
legacy=read(OUT.parent/'20261009_pilot_01/pilot_counts.json')
ids=[c['pattern_id'] for c in cards]
assert ids==[f'P{i:02}' for i in range(1,8)]+[f'S{i:02}' for i in range(1,7)]
required=['name','status','upper_judgment_principle','sub_operations','application_units','minimum_evidence',
          'application_conditions','non_application_conditions','neighbor_distinctions','required_student_actions',
          'alternative_valid_solutions','frequency','value_assessments','held_boundary','verification']
for c in cards:
    assert all(c.get(k) for k in required),c['pattern_id']
    assert set(c['application_units'])=={'passage','question','choice','solution'}
    assert set(c['value_assessments'])=={'lecture','textbook','original_item_creation'}
    assert c['frequency']['corpus_prevalence'] is None
    assert c['alternative_valid_solutions']['allowed'] is True
    assert c['verification']['canonical_original_reopened'] is False
valid_roles=set(read(OUT/'codebook_v0.2.json')['pattern_relation_definitions'])
for e in events:
    for r in e['relations']:
        assert set(r['pattern_relation'])<=valid_roles
        assert not ('explanatory_only' in r['pattern_relation'] and {'item_utilized','solution_helpful'}&set(r['pattern_relation']))
        if 'unclassified' in r['pattern_relation']:assert r['pattern_id'] is None
        else:assert r['pattern_id'] in ids
        for sid in r['subtype_ids']:
            assert sid in {s['subtype_id'] for c in cards for s in c['sub_operations']}
computed=count_patterns(events,ids)
diffs=[]
for pid in ids:
    for k,v in legacy['patterns'][pid].items():
        if computed[pid][k]!=v:diffs.append({'pattern':pid,'field':k,'old':v,'new':computed[pid][k]})
assert not diffs,diffs
matrix=(OUT.parent/'20261010_application_01/02_패턴별_활용_매트릭스.md').read_text()
for pid in ids:
    row=next(l for l in matrix.splitlines() if l.startswith('|'+pid+'|')).strip('|').split('|')
    for family,cell in zip(['KICE','LEET','MEET'],row[1:4]):
        passages,questions=map(int,cell.split('/'))
        assert computed[pid]['by_exam_family'][family]=={'passages':passages,'questions':questions}
assert computed['P05']['evidence_events']==5 and computed['P05']['source_questions']==5
assert computed['P05']['utilized_questions']==4 and computed['P05']['observed_passages']==4
assert computed['P05']['structure_only_events']==['E028']
assert count_patterns(events+copy.deepcopy(events),ids)==computed
stale=copy.deepcopy(events)
for e in stale:e['legacy_pattern_ids']=ids
assert count_patterns(stale,ids)==computed  # 태그만 많아져도 실제 계수는 불변
unconfirmed=copy.deepcopy(events)
for e in unconfirmed:
    for r in e['relations']:r['decision']='unconfirmed'
assert all(x['evidence_events']==0 for x in count_patterns(unconfirmed,ids).values())
fake_new=copy.deepcopy(events)
for e in fake_new:
    for r in e['relations']:r['decision']='confirmed_new'
assert all(x['evidence_events']==0 for x in count_patterns(fake_new,ids).values())
fake_external=copy.deepcopy(events)
for e in fake_external:e['sample_split']='external'
assert all(x['evidence_events']==0 for x in count_patterns(fake_external,ids).values())
assert {s['subtype_id'] for c in cards if c['pattern_id']=='P04' for s in c['sub_operations']}=={
    'P04.explicit_requirements','P04.measurement_mechanism','P04.authority_scope'}
assert len(events)==46 and sum(e['legacy_unclassified'] for e in events)==15
metadata=read(OUT/'management_metadata.json')
assert len(metadata['discovery'])==12 and sum(len(s['case_ids']) for s in metadata['discovery'])==39
assert len(metadata['validation_metadata_only'])==6 and sum(len(s['case_ids']) for s in metadata['validation_metadata_only'])==21
assert not {e['passage_group'] for e in events}&{s['passage_group'] for s in metadata['validation_metadata_only']}
assert not {e['passage_group'] for e in events}&{'G024','G370'}
protected=read(OUT/'preservation_baseline.json')
changed=[p for p,h in protected.items() if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]
assert not changed,changed
save('count_reconciliation.json',{'scope':'발견용 기존 분석 재사용','legacy_source':'../20261009_pilot_01/pilot_counts.json',
    'counts':computed,'legacy_differences':diffs,'application_family_matrix_matches':True,
    'direct_utilized_unique_questions':len({e['question_id'] for e in events for r in e['relations'] if 'item_utilized' in r['pattern_relation']}),
    'unclassified_events':15,'corpus_prevalence':None})
lines=['# 기존 수치와 v0.2 계수 대조','',
       'pattern_relation과 관계의 근거 상태만으로 재계산했다. 발견용 기존 분석의 수치를 재현한 것이며 외부 검증 결과가 아니다. 기존 카드의 모든 계수 필드 및 application의 시험별 활용 수와 일치했다.', '',
       '|후보|연결 장면|구조 지문|출처 문항|실제 활용 지문/문항|도움 풀이 장면|설명 장면|기존 수치 차이|',
       '|---|---:|---:|---:|---|---:|---:|---|']
for pid,c in computed.items():
    lines.append(f"|{pid}|{c['evidence_events']}|{c['observed_passages']}|{c['source_questions']}|{c['utilized_passages']}/{c['utilized_questions']}|{c['solution_helpful_events']}|{c['explanatory_events']}|없음|")
lines+=['','E028/ZE는 P05 설명 장면 1개에 포함하지만 실제 활용에는 포함하지 않는다. E030/ZF④·⑤는 보조 활용을 유지한다. P02의 OZ·PA는 두 문항이지만 같은 지문 하나다.', '',
        '46장면 중 기존 미분류 12개와 정답 경로 추가 3개를 합한 15개는 배속하지 않았다. 경계 사례로 쓰인 미분류 장면도 이 상태를 유지한다.', '',
        '중복 행 추가, legacy_pattern_ids를 임의로 늘리는 입력, 미확인 관계, 근거 없는 confirmed_new 입력이 실제 활용 수를 부풀리지 않는지 검사했다.']
(OUT/'count_reconciliation.md').write_text('\n'.join(lines)+'\n')
save('validation_report.json',{'passed':True,'cards':13,'events':46,'legacy_count_differences':diffs,
     'family_counts_match':True,'E028_excluded_from_utilization':True,'duplicate_and_tag_pollution_tests_passed':True,
     'unconfirmed_and_unsupported_new_excluded':True,'protected_prior_run_files':len(protected),'changed_prior_files':changed,
     'validation_applied':False,'G095_metadata_redisclosure_recorded':True,'holds_preserved':['G024','G370'],
     'canonical_quote_semantics_reverified':False,'json_schema_library_validation_run':False,
     'schema_check_scope':'JSON 구문·주요 필수 필드·역할/상태 제약을 로컬 assertion으로 검사. 별도 JSON Schema 엔진은 미실행.',
     'interpretation':'구조·계수·보존 점검이며 의미·교육효과·외부전이 검증 아님'})
print('검증 통과: 13카드·46장면, 기존 계수와 시험별 수치 일치, E028 제외, 중복/태그 오염 방지, 기존 37파일 불변')
