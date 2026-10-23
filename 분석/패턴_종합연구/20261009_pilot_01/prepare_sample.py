import json, hashlib, re
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
def readj(p): return json.loads((ROOT / p).read_text())
def rows(p): return [json.loads(l) for l in (ROOT/p).read_text().splitlines() if l.strip()]
def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
idxpath='data/기본기_연구/research_data_index_enriched_v2.json'
idx=readj(idxpath)['case_to_group']
discovery=['G001','G002','G004','G010','G014','G039','G103','G160','G222','G260','G284','G329']
validation=['G064','G095','G119','G157','G350','G310']
def family_key(pid):
    return re.sub(r'-S.*$', '', (pid or '').replace(' ','_'))
selected=[]
for split,groups in [('discovery',discovery),('validation',validation)]:
    for group in groups:
        rr=[r for r in idx if r['passage_group']==group]
        assert rr and all(r['manifest_status']=='consumed_sdss' for r in rr)
        key=family_key(rr[0]['passage_id'])
        aliases=[r for r in idx if family_key(r.get('passage_id'))==key]
        selected.append(dict(split=split,passage_group=group,passage_id=rr[0]['passage_id'],
          identity_family=key,exam_family=rr[0]['exam_family'],academic_year=rr[0]['academic_year'],
          case_ids=[r['case_id'] for r in rr], question_ids=[r['question_id'] for r in rr],
          alias_case_ids=[r['case_id'] for r in aliases],alias_groups=sorted(set(r['passage_group'] for r in aliases)),
          source_paths=sorted(set(r['canonical_source_path'] for r in rr if r['canonical_source_path'])),
          blind_source_paths=[r['blind_source'] for r in rr],
          selection_metadata_only=True,validation_content_read=False))
assert len({r['identity_family'] for r in selected})==18
manifest=dict(schema_version=1,run_id=OUT.name,created_date='2026-10-09',frozen=True,
 common_manifest_for_future_models=True,prior_common_manifest_found=False,
 selection_method='완료 상태 및 시험 좌표의 메타데이터를 이용한 목적 표집. 발견 KICE 8/LEET 2/MEET 2, 검증 KICE 4/LEET 1/MEET 1. 정답·태그·코드 출현 수로 뽑지 않음. 최초 안내·인덱스 열람에서 노출된 앞부분 사례는 검증용에서 배제.',
 limitations=['통계적 충분성·대표성 보장 없음','독서 중심; 문학 및 시각자료 중심 문항 대표성 부족','범위 식별자가 다른 중복은 기존 식별자 연결에 의존. 코퍼스 전체 의미 유사도 중복검사는 수행하지 않음'],
 holds_excluded={'G024':['DR','DS','DT','DU'],'G370':['BAP','BAQ','BAR','BAS']},
 runtime={'model':'GPT-6 기반 Codex (런타임 지시에서 확인)','exact_model_id':None,'effort':None,'usage':None,'other_models_called':False},
 samples=selected)
target=OUT/'sample_manifest.json'
assert not target.exists(), '이미 고정한 표본을 재선정하지 않는다'
target.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
protected=['data/기본기_연구/astra_handoff_queue.jsonl','data/기본기_연구/astra_handoff_processed.jsonl','data/기본기_연구/prepared_backlog/manifest.jsonl','data/기본기_연구/meta_state.json',idxpath,'data/sdss_100codes_catalog.json','data/기본기_연구/코드군_통합가설_v1.json']
(OUT/'preservation_baseline.json').write_text(json.dumps({p:sha(p) for p in protected},ensure_ascii=False,indent=2)+'\n')
q=rows(protected[0]);p=rows(protected[1]);m=rows(protected[2])
stats=dict(queue_rows=len(q),queue_unique_ids=len({x['record_id'] for x in q}),processed_rows=len(p),
 pending=len({x['record_id'] for x in q}-{x['source_record_id'] for x in p}),
 stages=dict(Counter(r['stage'] for r in q)),manifest_rows=len(m),manifest_status=dict(Counter(r['status'] for r in m)),
 manifest_groups=len({r['passage_group'] for r in m}),index_cases=len(idx),
 index_nonnull_question_ids=len({r['question_id'] for r in idx if r.get('question_id')}),
 index_nonnull_passage_ids=len({r['passage_id'] for r in idx if r.get('passage_id')}),
 index_normalized_passage_families=len({family_key(r['passage_id']) for r in idx if r.get('passage_id')}),
 index_null_question_id_cases=sum(not r.get('question_id') for r in idx),
 index_null_passage_id_cases=sum(not r.get('passage_id') for r in idx),
 meta_state_reported={k:v for k,v in readj(protected[3]).items() if k in ['completed_passage_groups_total','completed_questions_total','meta_due','manual_parity_audit_due','depth_backfill_pending']})
(OUT/'corpus_counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(stats,ensure_ascii=False,indent=2))
print('고정된 표본',[(r['split'],r['passage_group'],r['alias_groups']) for r in selected])
