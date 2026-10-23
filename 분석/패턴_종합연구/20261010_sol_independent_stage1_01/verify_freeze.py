from pathlib import Path
import hashlib,json
RUN=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r=json.loads((RUN/'freeze_record.json').read_text())
m=json.loads((RUN/'freeze_manifest.json').read_text())
assert sha(RUN/'freeze_manifest.json')==r['freeze_manifest_sha256']
assert sha(RUN/'freeze_manifest.sha256')==r['freeze_sha256_list_sha256']
assert len(m['files'])==r['payload_file_count']
assert all(sha(RUN/x['path'])==x['sha256'] for x in m['files'])
expected={x['path'] for x in m['files']}
actual={str(p.relative_to(RUN)) for p in RUN.rglob('*') if p.is_file() and '__pycache__' not in p.parts
        and p.name not in {'freeze_record.json','freeze_manifest.json','freeze_manifest.sha256'}}
assert actual==expected
print(json.dumps({'status':'고정 후 파일별 해시 재검증 통과','payload_files':len(expected),
 'freeze_record_sha256':sha(RUN/'freeze_record.json')},ensure_ascii=False,indent=2))
