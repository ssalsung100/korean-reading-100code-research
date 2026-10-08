"""이번 사후 감사의 고정 대상만 기록하며, 실제 파일 변경은 apply_patch로 한다."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DATA = ROOT / 'data/기본기_연구'
QUEUE = DATA / 'astra_handoff_queue.jsonl'
IDS = 'DV GA DZ EO EP EJ AB BZ CT GC FH FN FT GJ ET FF FL FX EF FD EI'.split()
BASE = HERE / 'audit_baseline.json'

def digest(b):
    return hashlib.sha256(b).hexdigest()

def patch(s):
    subprocess.run(['apply_patch'], input=s, text=True, check=True, cwd=HERE)

def capture():
    paths = [QUEUE, DATA/'astra_handoff_processed.jsonl', DATA/'prepared_backlog/manifest.jsonl', DATA/'meta_state.json', ROOT/'분석/기본기_연구/CURRENT.md']
    for case in IDS:
        paths.extend(sorted((DATA/'prepared_backlog/blind_sources').glob(case+'*')))
    files = {}
    for p in paths:
        if p.is_file():
            b = p.read_bytes()
            files[str(p.relative_to(ROOT))] = {'bytes': len(b), 'sha256': digest(b)}
    q = [json.loads(x) for x in QUEUE.read_text().splitlines()]
    result = {'case_ids': IDS, 'queue_count': len(q), 'queue_last_record_id': q[-1]['record_id'], 'files': files}
    assert not BASE.exists(), '기존 snapshot 덮어쓰기 금지'
    s = json.dumps(result, ensure_ascii=False, indent=2)+'\n'
    patch('*** Begin Patch\n*** Add File: audit_baseline.json\n'+''.join('+'+line+'\n' for line in s.splitlines())+'*** End Patch\n')

def verify():
    baseline = json.loads(BASE.read_text())
    for name, info in baseline['files'].items():
        b = (ROOT/name).read_bytes()
        if ROOT/name == QUEUE:
            b = b[:info['bytes']]
        assert len(b) == info['bytes'] and digest(b) == info['sha256'], name
    rows = [json.loads(x) for x in QUEUE.read_text().splitlines()]
    assert len({r['record_id'] for r in rows}) == len(rows)
    added = rows[baseline['queue_count']:]
    staged = [json.loads(p.read_text()) for p in sorted((HERE/'raw_batches').glob('*.json'))]
    by_id = {r['record_id']: r for r in rows}
    persisted = [r for r in staged if r['record_id'] in by_id]
    assert all(by_id[r['record_id']] == r for r in persisted)
    manifest = [json.loads(x) for x in (DATA/'prepared_backlog/manifest.jsonl').read_text().splitlines()]
    groups = {x['case_id']: x['passage_group'] for x in manifest}
    covered = []
    for r in added:
        for ref in r['payload'].get('source_record_ids', []):
            assert ref in by_id, ref
        for item in r['payload'].get('evidence_additions', []):
            if 'case' not in item:
                continue
            case = item['case']
            assert case in IDS and groups[case] == item['passage_group']
            for key in ('task', 'target', 'evidence_location', 'evidence_type', 'existing_code_layers', 'strongest_competitor', 'competitor_relation'):
                assert item.get(key), (case, key)
            assert (ROOT/item['source']).is_file(), item['source']
            covered.append(case)
    assert len(covered) == len(set(covered)), '사례별 근거 중복'
    processed = [json.loads(x) for x in (DATA/'astra_handoff_processed.jsonl').read_text().splitlines()]
    processed_ids = {r.get('source_record_id', r.get('record_id')) for r in processed}
    pending = sorted(set(by_id)-processed_ids)
    if len(persisted) == 8:
        assert set(covered) == set(IDS)
        assert set(pending) == {r['record_id'] for r in added}
        assert len(added) == 8
        for case in IDS:
            for stage in ('blind', 'answer_check', 'independent_code', 'sdss_compare'):
                assert any(r.get('case') == case and r['stage'] == stage and r['status'] == 'done' for r in rows[:baseline['queue_count']]), (case,stage)
    print(json.dumps({'original_queue_prefix_unchanged': True, 'other_captured_files_unchanged': True, 'captured_file_count':len(baseline['files']), 'queue_count':len(rows), 'processed_count':len(processed), 'pending_raw_count':len(pending), 'persisted_batch_files_match':len(persisted), 'covered_cases':len(covered), 'covered_passage_groups':len({groups[c] for c in covered}), 'appended_ids':[r['record_id'] for r in added]}, ensure_ascii=False))

def append(name):
    source = (HERE/name).resolve()
    assert source.parent == HERE/'raw_batches'
    record = json.loads(source.read_text())
    assert record['stage'] in ('depth_backfill', 'boundary_revision')
    assert record['payload']['original_blind_preserved'] is True
    before = QUEUE.read_bytes()
    rows = [json.loads(x) for x in before.decode().splitlines()]
    existing = [r for r in rows if r['record_id'] == record['record_id']]
    if existing:
        assert existing == [record]
        print('이미 동일 record가 저장됨: '+record['record_id'])
        return
    assert before.endswith(b'\n')
    last = before.decode().splitlines()[-1]
    line = json.dumps(record, ensure_ascii=False, separators=(',', ':'))
    assert QUEUE.read_bytes() == before
    patch('*** Begin Patch\n*** Update File: '+str(QUEUE)+'\n@@\n '+last+'\n+'+line+'\n*** End Patch\n')
    after = QUEUE.read_bytes()
    assert after == before+(line+'\n').encode(), 'append 결과 byte 검증 실패'
    print('append 완료: '+record['record_id'])
    verify()

if __name__ == '__main__':
    if sys.argv[1] == 'capture': capture()
    elif sys.argv[1] == 'append': append(sys.argv[2])
    elif sys.argv[1] == 'verify': verify()
    else: raise SystemExit('capture | append raw_batches/파일.json | verify')
