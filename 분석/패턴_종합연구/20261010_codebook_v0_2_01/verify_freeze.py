"""동결 파일과 기존 입력의 해시·계수를 읽기 전용으로 확인한다."""
import hashlib
import json
import sys
from pathlib import Path
sys.dont_write_bytecode=True
from count_patterns import count_patterns

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((OUT/'freeze_manifest.json').read_text())
expected=(OUT/'freeze_manifest.sha256').read_text().split()[0]
assert sha(OUT/'freeze_manifest.json')==expected,'manifest 해시 불일치'
actual={str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file() and '__pycache__' not in p.parts
        and p.name not in {'freeze_manifest.json','freeze_manifest.sha256'}}
assert actual==set(manifest['files']),'동결 파일 목록의 추가·누락'
for name,item in manifest['files'].items():
    assert sha(OUT/name)==item['sha256'],name
    assert (OUT/name).stat().st_size==item['bytes'],name
protected=json.loads((OUT/'preservation_baseline.json').read_text())
assert all(sha(ROOT/p)==h for p,h in protected.items()),'기존 입력 변경'
cards=json.loads((OUT/'codebook_v0.2.json').read_text())['cards']
events=[json.loads(s) for s in (OUT/'event_mapping_v0.2.jsonl').read_text().splitlines()]
stored=json.loads((OUT/'count_reconciliation.json').read_text())['counts']
assert count_patterns(events,[c['pattern_id'] for c in cards])==stored,'계수 재현 실패'
print(json.dumps({'passed':True,'frozen_files':len(actual),'prior_files_unchanged':len(protected),
                  'manifest_sha256':expected,'codebook_sha256':manifest['files']['codebook_v0.2.json']['sha256']},ensure_ascii=False))
