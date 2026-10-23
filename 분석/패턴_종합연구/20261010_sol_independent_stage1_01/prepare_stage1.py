"""고정 표본에서 허용 필드만 분리. 정답·기존 판정 값은 출력하지 않는다."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
RUN = Path(__file__).resolve().parent

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write(name, value):
    (RUN / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

manifest_path = ROOT / '분석/패턴_종합연구/20261009_pilot_01/sample_manifest.json'
manifest = json.loads(manifest_path.read_text())
fields = ('split', 'passage_group', 'passage_id', 'exam_family', 'academic_year',
          'case_ids', 'question_ids', 'source_paths', 'blind_source_paths')
samples = [{k: row[k] for k in fields if k in row}
           for row in manifest['samples'] if row.get('split') == 'validation']
assert len(samples) == 6 and sum(len(s['case_ids']) for s in samples) == 21
assert not {'G024', 'G370'} & {s['passage_group'] for s in samples}

logs = []
sources = []
(RUN / 'sources').mkdir(exist_ok=True)
allowed = {'blind_only', 'passage_group', 'case_id', 'provenance', 'passage_text',
           'stem', 'choices', 'visual_supplements'}
for s in samples:
    for rel in s['blind_source_paths']:
        p = ROOT / rel
        d = json.loads(p.read_text())
        assert d['blind_only'] is True
        assert not set(d) - allowed, (rel, sorted(set(d) - allowed))
        assert len(d['choices']) == 5
        safe = {k: d[k] for k in ('passage_group', 'case_id', 'passage_text', 'stem', 'choices', 'visual_supplements') if k in d}
        target = 'sources/' + p.name
        write(target, safe)
        sources.append({'path': rel, 'sha256': digest(p), 'copy': target,
                        'copy_sha256': digest(RUN / target), 'case_id': d['case_id'],
                        'scope': '지문·발문·전체 선지·필수 시각자료 경로',
                        'model_content_viewed': False})

write('targets.json', {'samples': samples, 'question_count': 21, 'holds': ['G024', 'G370'],
    'fixed_manifest': str(manifest_path.relative_to(ROOT)), 'fixed_manifest_sha256': digest(manifest_path),
    'separation': '고정 표본 목록을 코드로 파싱해 허용 ID·출처 필드만 새 파일로 분리. 나머지 값은 모델에 출력하지 않음.',
    'G095': '이전 Astra의 정답·코드 노출 이력은 사용자 고지로만 인지. 상세 기록 열람 금지. 5문항 별도 집계.'})
write('source_inventory.json', sources)

protected = []
for directory in ('분석/패턴_종합연구/20261009_pilot_01',
                  '분석/패턴_종합연구/20261010_application_01',
                  '분석/패턴_종합연구/20261010_codebook_v0_2_01'):
    for p in sorted((ROOT / directory).rglob('*')):
        if p.is_file(): protected.append({'path': str(p.relative_to(ROOT)), 'sha256': digest(p)})
for s in sources:
    protected.append({'path': s['path'], 'sha256': s['sha256']})
write('preservation_baseline.json', protected)

write('read_history.json', {
    'requested_model': 'GPT-6.1 Sol', 'requested_effort': 'xhigh',
    'runtime_identity_verified': False,
    'runtime_note': '이번 실행은 주 세션에서만 수행. 외부 모델 호출·subagent·cx1m 호출 없음. API 모델 ID와 effort를 직접 검증하는 수단은 사용하지 않음.',
    'preloaded': ['사용자 제공 AGENTS.md 지침 전체', '사용자 최신 독립 검증 1단계 지시', '시스템·개발자 지침·스킬 목록·환경 정보'],
    'preloaded_impact': '연구 절차·G095 노출 이력·hold ID·기존 코드북 식별자만 제공됨. 기존 패턴 정의·적용 결과·정답은 제공되지 않음.',
    'events': [
        {'scope': 'pwd 및 rg --files', 'mode': '경로명 열거', 'content_exposure': '파일명만. 첫 검색은 출력 일부가 잘림. 문서 본문 미열람.'},
        {'path': '분석/패턴_종합연구/20261010_codebook_v0_2_01/independent_validation_inputs.md', 'mode': '기계적 필터', 'content_exposure': 'ID G095, 표 헤더(시점·필요 입력·제공·분리 기준), 행·열 수만. 본문 값 출력 없음.'},
        {'path': '분석/패턴_종합연구/20261010_codebook_v0_2_01/management_metadata.json', 'mode': '기계적 구조 검사', 'content_exposure': '최상위 키와 배열 길이·레코드 키만. 노출 기록 및 패턴 값 미출력.'},
        {'path': '분석/패턴_종합연구/20261010_codebook_v0_2_01/input_inventory.json', 'mode': '기계적 구조 검사', 'content_exposure': '최상위 타입 list만.'},
        {'path': str(manifest_path.relative_to(ROOT)), 'mode': '구조 검사 및 허용 필드 분리', 'content_exposure': '최상위·표본 레코드 키, 고정 검증 표본 6개의 ID·문항 ID·출처 경로만.'},
        {'paths': [s['path'] for s in sources], 'mode': '기계적 파싱·허용 필드 복사', 'content_exposure': '준비 단계에서는 6개 대표 blind 파일 키만 출력. 실제 본문 열람은 이후 events에 기록.'},
        {'scope': 'preservation_baseline.json에 열거한 파일', 'mode': '바이트 해시만 계산', 'content_exposure': '기존 보고·코드북 등을 hash 함수로 읽었으나 본문을 모델에 출력·해석하지 않음.'}
    ],
    'guarantee': '모델 세션에 표시된 자료와 코드로만 처리한 자료를 구분. 숨은 자동 파일 삽입 여부 및 사전학습 기출 기억은 완전히 검증할 수 없음.'
})
print(json.dumps({'run': str(RUN.relative_to(ROOT)), 'groups': 6, 'questions': 21, 'protected_files': len(protected)}, ensure_ascii=False))
