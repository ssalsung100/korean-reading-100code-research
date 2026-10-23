"""이 연구의 선택 표본·저장 순서·파생 사본·링크만 검사한다. 전체 원장 재감사가 아니다."""
import json
import re
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import unquote

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[2]
OUTPUT = Path(__file__).with_suffix('.json')

def jsonl(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]

errors = []
checks = {}

def check(name, ok, detail):
    checks[name] = {'pass': bool(ok), 'detail': detail}
    if not ok:
        errors.append(name)

# 출력 파일을 향한 README 링크도 첫 실행부터 실제로 검사한다.
OUTPUT.write_text(json.dumps({'status': '검증 진행 중'}, ensure_ascii=False))

required = []
for i in range(15):
    paths = list(BASE.glob(f'{i:02}_*'))
    check(f'산출물_{i:02}', len(paths) == 1 and (
        paths[0].is_dir() if i == 3 else paths[0].is_file() and paths[0].stat().st_size > 0
    ), [str(p.relative_to(BASE)) for p in paths])
    required.extend(paths)

samples = jsonl(BASE / '02_평가원지문_표본목록.jsonl')
raw = jsonl(BASE / '연구판단_raw.jsonl')
source = jsonl(ROOT / 'data/kice_passages.jsonl')
ids = [x['sample_id'] for x in samples]
check('표본_범위', ids == [f'PA{i:02}' for i in range(1, 23)],
      {'total': len(ids), 'derive': sum(x['role'] == '원리도출' for x in samples),
       'heldout': sum(x['role'] == '보류검증' for x in samples)})

copy_errors = []
sequence_errors = []
for s in samples:
    sid = s['sample_id']
    original = source[s['source_line'] - 1]
    copied = (BASE / s['passage_only_copy']).read_text()
    parts = re.split(r'^## P\d+\n\n', copied, flags=re.M)[1:]
    original_parts = [p.strip() for p in original['passage_text'].split('\n\n') if p.strip()]
    if ([p.strip() for p in parts] != original_parts or
            original['passage_id'] != s['passage_id'] or
            not (ROOT / s['source_markdown']).exists() or
            not (ROOT / '고3 기출' / s['source_hwpx']).exists()):
        copy_errors.append(sid)
    p1 = [i for i, r in enumerate(raw, 1) if r['stage'] == '지문자체분석_고정' and sid in r['sample_ids']]
    p2 = [i for i, r in enumerate(raw, 1) if r['stage'] == '문항연결' and sid in r['sample_ids']]
    if (len(p1) != 1 or len(p2) != 1 or not p1[0] < p2[0] or
            p1[0] != s['stage1_raw_line'] or p2[0] != s['stage2_raw_line']):
        sequence_errors.append(sid)
    if not (BASE / s['analysis_file']).exists():
        sequence_errors.append(f'{sid}:분석파일 없음')
check('선택22_전사사본과출처', not copy_errors, {'mismatch': copy_errors, 'scope': '선택한 22개 사본의 내용 비교. 공식 PDF 전수 대조 또는 전체 원장 해시 검증 아님.'})
check('지문_문항_저장순서', not sequence_errors, {'errors': sequence_errors, 'scope': '기록 순서 검사. 무노출 증명 아님. PA02 문항 동시 노출 예외 별도 기록.'})
freeze = next(i for i, r in enumerate(raw) if r['stage'].startswith('교차비교_후보v0'))
heldout = [i for i, r in enumerate(raw) if r['stage'] == '지문자체분석_고정' and any(s in r['sample_ids'] for s in ids[18:])]
check('보류표본_후보고정뒤기록', len(heldout) == 4 and freeze < min(heldout), {'freeze_raw_line': freeze + 1, 'heldout_raw_lines': [x + 1 for x in heldout], 'scope': '제목·첫 문장 표집 노출 및 과거 노출 가능성은 별개'})

keys = json.loads((BASE / '검증/문항_저장정답대조.json').read_text()) + json.loads((BASE / '검증/보류표본_저장정답대조.json').read_text())
recovered = json.loads((BASE / '검증/선택표_사후보완.json').read_text())
pairs = [(x['sample_id'], x['question']) for x in keys]
check('선택문항_최초기록', len(keys) == len(set(pairs)) == 44 and
      sum(x['matches'] is True for x in keys) == 41 and
      sum(x['initial_choice'] is None for x in keys) == 3,
      {'total': len(keys), 'initial_number_matches': 41, 'initial_deferred': 3, 'scope': '저장소 답 필드 대조. 독립 정답률·모든 선지 전수 판정 아님.'})
check('사후선택표_별도보존', len(recovered) == 2 and all(
    x['post_exposure'] and x['initial_choice'] is None and x['matches'] and (BASE / x['evidence']).exists() for x in recovered),
    {'recovered': 2, 'remaining_semantic_hold': 'PA04-49', 'initial_records_rewritten': False})

broken = []
links = 0
for path in BASE.rglob('*.md'):
    for m in re.finditer(r'(?<!!)\[[^\]\n]*\]\((<[^>]+>|[^)\n]+)\)', path.read_text()):
        target = m.group(1).strip().strip('<>')
        if '://' in target or target.startswith('#'):
            continue
        dest = unquote(target.split('#', 1)[0])
        links += 1
        if not (path.parent / dest).exists():
            broken.append({'file': str(path.relative_to(BASE)), 'target': target})
check('문서_로컬링크', not broken, {'count': links, 'broken': broken})

json_errors = []
for path in list(BASE.rglob('*.json')) + list(BASE.rglob('*.jsonl')):
    try:
        jsonl(path) if path.suffix == '.jsonl' else json.loads(path.read_text())
    except (ValueError, OSError) as e:
        json_errors.append({'file': str(path.relative_to(BASE)), 'error': str(e)})
check('신규폴더_JSON형식', not json_errors, json_errors)
math_result = json.loads((BASE / '검증/시험지문_수치검산.json').read_text())
check('시제품_검산결과', math_result['status'] == '산식·가상 사례 검산 통과', math_result['scope'])

result = {
    'at': datetime.now(timezone.utc).isoformat(),
    'status': '통과' if not errors else '확인 필요',
    'checks': checks,
    'errors': errors,
    'raw_records_at_validation': len(raw),
    'not_validated': ['학생 이해·독해 난도', '평가원 동등 품질', '전 표본 공식 PDF 문장별 대조', 'PA04-49 의미 판정', '기존 자산의 전수 불변 해시 감사'],
}
OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'status': result['status'], 'checks': len(checks), 'errors': errors,
                  'local_links': links, 'samples': len(samples)}, ensure_ascii=False))
raise SystemExit(bool(errors))
