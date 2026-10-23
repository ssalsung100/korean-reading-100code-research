"""이번 산출물의 근거·계수·보존만 검증한다. 의미 판단을 자동 채점하지 않는다."""
import json,hashlib
from pathlib import Path
from collections import Counter
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
def j(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=j(OUT/'sample_manifest.json');a=j(OUT/'sample_annotations.json')
es=[json.loads(l) for l in (OUT/'pilot_events.jsonl').read_text().splitlines()]
coverage=j(OUT/'reading_coverage.json');counts=j(OUT/'pilot_counts.json')
baseline=j(OUT/'preservation_baseline.json')
checks={}
def check(name,val):checks[name]=bool(val)
check('manifest_immutable',sha(OUT/'sample_manifest.json')==a['manifest_sha256'])
check('split_12_6',Counter(s['split'] for s in m['samples'])=={'discovery':12,'validation':6})
ds=[s for s in m['samples'] if s['split']=='discovery'];vs=[s for s in m['samples'] if s['split']=='validation']
dc={c for s in ds for c in s['case_ids']};vc={c for s in vs for c in s['alias_case_ids']}
check('case_split_disjoint',not dc&vc)
check('identity_family_split_disjoint',not {s['identity_family'] for s in ds}&{s['identity_family'] for s in vs})
check('held_groups_excluded',not {'G024','G370'}&{s['passage_group'] for s in m['samples']})
check('all_discovery_cases_have_events',dc=={e['case_id'] for e in es})
check('no_validation_event',not vc&{e['case_id'] for e in es})
check('all_39_sources_normalized_parity',len(coverage)==39 and all(c['source']['passage_parity_normalized'] and c['source']['question_parity_normalized'] for c in coverage))
check('two_visuals_read',sum(c['diagram_read'] for c in coverage)==2)
check('event_ids_unique',len(es)==len({e['event_id'] for e in es}))
required=['passage_id','question_id','choice_ids','existing_analysis_id','existing_analysis_source','original_evidence','information_presentation','question_or_choice_operation','decisive_difference','solving_action','application_conditions','action_timing','action_necessity','reused_finding','new_interpretation','alternative_solution','disagreement_or_unverified']
check('all_11_requested_dimensions_present',all(all(e.get(k) for k in required) for e in es))
quote_ok=True;ref_ok=True
rawlines=(ROOT/'data/기본기_연구/astra_handoff_queue.jsonl').read_text().splitlines()
for e in es:
 for x in e['original_evidence']:
  b=j(ROOT/x['blind_path']);t=b[x['json_pointer'][1:]]
  quote_ok &= t[x['char_start']:x['char_end']]==x['quote']
 for o in e['option_quotes']:
  quote_ok &= j(ROOT/o['source_path'])['choices'][o['choice_id']-1]==o['text']
 old=e['existing_analysis_source'];r=json.loads(rawlines[old['line']-1])
 ref_ok &= r['record_id']==e['existing_analysis_id'] and r['case']==e['case_id'] and old['quote'] in json.dumps(r,ensure_ascii=False)
 ref_ok &= (ROOT/old['reflected_path']).exists()
check('exact_quote_and_choice_offsets',quote_ok);check('existing_analysis_record_refs',ref_ok)
for p,s in counts['patterns'].items():
 v=[e for e in es if p in e['pattern_ids']];u=[e for e in v if e['used_in_item']]
 check(p+'_unique_count',s['observed_passages']==len({e['resolved_passage_id'] for e in v}) and s['utilized_questions']==len({e['resolved_question_id'] for e in u}) and s['utilized_passages']==len({e['resolved_passage_id'] for e in u}))
check('7_repeated_6_singletons',sum(s['utilized_passages']>=2 for s in counts['patterns'].values())==7 and sum(s['utilized_passages']==1 for s in counts['patterns'].values())==6)
check('structure_only_not_counted_as_use',all(not e['used_in_item'] for e in es if e['case_id']=='ZE'))
check('G160_resolved_identity_preserved',all(c['resolved_passage_id']=='KICE-2026-6월_모평-Q01-03' for c in coverage if c['passage_group']=='G160'))
check('contamination_explicitly_recorded',a['validation_contamination'][0]['group']=='G095')
preserved={p:sha(ROOT/p)==h for p,h in baseline.items()}
check('all_protected_baseline_files_unchanged',all(preserved.values()))
report=dict(scope='출처 연결·고유 집계·표본 분할·파일 보존의 기계 점검. 의미 자동 검증 아님.',
 checks=checks,all_mechanical_checks_pass=all(checks.values()),protected_files=preserved,
 manual_limitations=['G095 한 문항의 과거 요약 우발 노출로 독립 검증 제한','검증용 적용 및 제2 의미 검토 미수행','GL 수식 원배포본 미검증 유지'],
 totals={k:v for k,v in counts.items() if k!='patterns'})
(OUT/'validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
assert all(checks.values()),[k for k,v in checks.items() if not v]
