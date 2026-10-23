"""배치의 저장·근거 연결 검사. 의미 타당성 검증은 아니다."""
import sys,json,collections
from corpus_io import ROOT,OUT,rows,load,write,sha
b=int(sys.argv[1]);prefix=str(OUT.relative_to(ROOT))+'/'
gg=rows(prefix+'group_extractions.jsonl');ss=rows(prefix+f'batch_{b:03d}_scenes.jsonl');ee=rows(prefix+'evidence_links.jsonl')
assert len({g['unique_group'] for g in gg})==len(gg)
allss=[s for p in OUT.glob('batch_*_scenes.jsonl') for s in rows(str(p.relative_to(ROOT)))]
assert len({s['event_id'] for s in allss})==len(allss)
idx={e['event_id']:e for e in ee};raw={r['record_id']:r for r in rows('data/기본기_연구/astra_handoff_queue.jsonl')}
for s in ss:
    e=idx[s['event_id']];assert e['unique_question']==s['unique_question']
    assert sha(ROOT/e['source_path'])==e['source_sha256']
    for r in e['solution_records']:assert raw[r['record_id']]['payload']==r['payload']
cp=load(prefix+'checkpoint.json');manifest=rows(prefix+'manifest_groups.jsonl')
for g in manifest:
    assert g['unique_group'] not in cp['completed_groups'] or g['status']=='추출 대기'
    g['extraction_status']='1차 종합 완료' if g['unique_group'] in cp['completed_groups'] else ('기존 보류 승계' if g['status']=='기존 보류 승계' else '미처리')
from corpus_io import jsonl
jsonl('manifest_groups.jsonl',manifest)
write(f'batch_{b:03d}_validation.json',dict(batch=b,groups=sum(g['batch']==b for g in gg),scenes=len(ss),evidence_links_checked=len(ss),source_hash_changed=0,raw_payload_changed=0,duplicate_event_ids=0,hold_extraction=0,full_input_hash_scan_performed=False,semantic_validation_completed=False,meaning='저장·근거 연결 검사만 통과. 의미 판정은 실제 장면·경계 주석을 따른다.'))
print('배치',b,'근거 연결',len(ss),'통과. 남은 지문',cp['expected_remaining_groups'])
