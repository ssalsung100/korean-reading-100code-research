"""실행 시작 때 기록한 기존 파일 해시를 대조한다. 원문 내용은 출력하지 않는다."""
import hashlib
import json
from pathlib import Path

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
baseline=json.loads((OUT/'preservation_baseline.json').read_text())
changed=[]
missing=[]
for i,(name,expected) in enumerate(baseline.items(),1):
    p=ROOT/name
    if not p.is_file():
        missing.append(name)
    elif hashlib.sha256(p.read_bytes()).hexdigest()!=expected:
        changed.append(name)
    if i%2000==0:
        print('보존 대조 진행',i,'/',len(baseline),flush=True)
report={'checked_files':len(baseline),'changed_files':changed,'missing_files':missing,
        'passed':not changed and not missing,
        'scope':'기존 pilot 전체, 기본기 연구 MD·데이터 트리 전체, 주요 원문 DB·원장·코드 카탈로그 및 초기 안내 파일. 검증용 본문은 해시만 계산하고 의미 분석하지 않음.',
        'hold_policy':'G024/G370 유지. hold 해제·원장 갱신·기존 manifest 수정 없음.'}
(OUT/'preservation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
assert report['passed']
