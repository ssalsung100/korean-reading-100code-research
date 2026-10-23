"""이 폴더 안의 저장·원문 연결·집계만 담당한다. 의미 판단은 직접 입력한다."""
import collections, copy, hashlib, importlib.util, json, os, sys
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
sys.dont_write_bytecode = True

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
OLD = OUT.parent / '20261012_corpus_sweep_01'

def rows(path):
    return [json.loads(x) for x in Path(path).read_text().splitlines() if x.strip()]

def write(name, obj):
    path = OUT / name
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    os.replace(temp, path)

def jsonl(name, data):
    path = OUT / name
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in data))
    os.replace(temp, path)

def append(name, data):
    with (OUT / name).open('a') as f:
        for x in data:
            f.write(json.dumps(x, ensure_ascii=False) + '\n')
        f.flush()
        os.fsync(f.fileno())

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

spec = importlib.util.spec_from_file_location('sweep_source', OLD / 'corpus_io.py')
source_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source_module)
ANALYSES = {x['analysis_id']: x for x in rows(OLD / 'manifest_analyses.jsonl')}
TARGETS = sorted(rows(OLD / 'unextracted_questions.jsonl'),
                 key=lambda x: ({'KICE': 0, 'LEET': 1, 'MEET': 2}[x['exam_family']], x['unique_question']))
BYQ = {x['unique_question']: x for x in TARGETS}
BYCASE = {c: x for x in TARGETS for c in x['case_ids']}
RAW = collections.defaultdict(list)
for line, x in enumerate(rows(ROOT / 'data/기본기_연구/astra_handoff_queue.jsonl'), 1):
    RAW[x.get('case')].append({'line': line, **x})
PATTERNS = {x['pattern']: x for x in json.loads((OLD / 'pattern_candidates.json').read_text())}

def entry(q):
    entries = [ANALYSES[a] for a in q['analysis_ids']]
    selected = dict(next((x for x in entries if x['origin'] == 'prepared'), entries[0]))
    overrides = OUT / 'source_overrides.json'
    mapping = json.loads(overrides.read_text()) if overrides.exists() else {}
    if q['unique_question'] in mapping:
        selected['source_path'] = mapping[q['unique_question']]
        selected['origin'] = 'prepared'
    return selected

def source(q):
    return source_module.get_source(entry(q))

def init():
    if (OUT / 'target_manifest.jsonl').exists():
        raise RuntimeError('대상 manifest가 이미 있다. 재선정 금지.')
    jsonl('target_manifest.jsonl', [dict(order=n, **q) for n, q in enumerate(TARGETS, 1)])
    paths = set(OLD.rglob('*'))
    for folder in ['data/기본기_연구', '분석/기본기_연구']:
        paths.update((ROOT / folder).rglob('*'))
    for name in ['data/kice_questions.jsonl', 'data/kice_passages.jsonl', 'data/meet_questions.jsonl', 'data/meet_passages.jsonl', 'data/sdss_100codes_catalog.json', 'AGENTS.md']:
        paths.add(ROOT / name)
    write('protected_input_hashes.json', {str(p.relative_to(ROOT)): sha(p) for p in sorted(paths) if p.is_file()})
    jsonl('raw_question_reviews.jsonl', [])
    jsonl('new_pattern_candidates.jsonl', [])
    refresh()
    print('대상', len(TARGETS), collections.Counter(q['exam_family'] for q in TARGETS))

def packet(start, count):
    seen = set()
    for n, q in enumerate(TARGETS[start - 1:start - 1 + count], start):
        e = entry(q); s = source(q)
        print('\n대상', n, q['unique_question'], q['case_ids'])
        if q['unique_group'] not in seen:
            print('전체 지문:', s.get('passage_text', ''))
            seen.add(q['unique_group'])
        print('발문:', s.get('stem', ''))
        for k, opt in enumerate(s.get('choices', []), 1):
            print(k, opt.get('text', opt) if isinstance(opt, dict) else opt)
        for c in q['case_ids']:
            for r in RAW[c]:
                if r['stage'] in ['blind', 'answer_check', 'depth_backfill', 'boundary_revision', 'hold']:
                    print('기존 근거', c, r['line'], r['stage'], json.dumps(r['payload'], ensure_ascii=False))
        print('기존 별도풀이:', [{k: x.get(k) for k in ['analysis_id', 'source_path', 'solution_paths', 'review_record']} for x in [ANALYSES[a] for a in q['analysis_ids']] if x['origin'] != 'prepared'])
        if q.get('known_depth_followup'):
            print('미해결 depth:', q['known_depth_followup'])

def evidence(q, quote, field='passage_text', option=None):
    if isinstance(quote, dict):
        return evidence(q, quote['quote'], quote.get('field', 'passage_text'), quote.get('option'))
    e = entry(q); s = source(q)
    text = s[field] if option is None else s['choices'][option - 1]
    if isinstance(text, dict):
        text = text['text']
    pos = text.find(quote)
    if pos < 0:
        raise ValueError(f'{q["unique_question"]} 원문 불일치: {quote}')
    return dict(source_path=e['source_path'], source_sha256=sha(ROOT / e['source_path']),
                field='choices' if option is not None else field, option_number=option,
                char_start=pos, char_end=pos + len(quote), quote=quote,
                paragraph_number=text[:pos].count('\n\n') + 1 if option is None and field == 'passage_text' else None)

def supplement_record(p):
    path = ROOT / p
    rec = dict(path=p, sha256=sha(path))
    if path.suffix == '.json': rec['full_record'] = json.loads(path.read_text())
    elif path.suffix in ['.md', '.txt']: rec['full_text'] = path.read_text()
    else: rec['kind'] = '이미지·시각 판독 내용은 문항 기록 참조'
    return rec

def candidate(cid, name, definition, conditions, boundary):
    existing = rows(OUT / 'new_pattern_candidates.jsonl')
    if cid in {x['candidate_id'] for x in existing}:
        return
    append('new_pattern_candidates.jsonl', [dict(candidate_id=cid, name=name, definition=definition,
        conditions=conditions, adjacent_boundary=boundary, status='보완 연구의 잠정 후보·최종 분류 아님')])

def scene(title, quotes, options, trigger, structure, operation, steps, conclusion, boundary,
          patterns, invariant, flip, neutral, risk, teaching, alternative=None, observed=None):
    return dict(title=title, evidence_quotes=quotes, option_numbers=options, student_start=trigger,
                passage_information_structure=structure, item_information_operation=operation,
                intermediate_inference_steps=steps, conclusion=conclusion,
                non_applicable_conditions=boundary, pattern_connections=patterns,
                original_observed_behavior=observed,
                alternative_valid_solution=alternative,
                educational_production=dict(status='해당 기출의 판단 구조에서 도출',
                    logical_invariants=invariant, answer_flipping_minimal_change=flip,
                    truth_preserving_changes=neutral, ambiguity_or_insufficient_evidence_risk=risk,
                    teachable_reading_action=teaching))

def add(key, answer, checks, scenes, alternative=None, unresolved=None, source_status='원문 텍스트 확인', note=None, supplementary_sources=None):
    q = BYCASE.get(key, BYQ.get(key))
    if q is None:
        raise KeyError(key)
    saved = rows(OUT / 'raw_question_reviews.jsonl')
    if q['unique_question'] in {x['unique_question'] for x in saved}:
        raise RuntimeError('불변 raw의 중복 저장 금지: ' + key)
    s = source(q); e = entry(q)
    if len(checks) != len(s.get('choices', [])):
        raise ValueError('전체 선지 검토 수 불일치')
    option_checks = []
    for n, (status, quote, reasoning) in enumerate(checks, 1):
        option_checks.append(dict(option_number=n, actual_review=True, statement_relation=status,
            source_evidence=[evidence(q, quote)] if quote else [], reasoning=reasoning,
            option_evidence=evidence(q, s['choices'][n - 1], option=n)))
    official = []
    states = []
    for c in q['case_ids']:
        for r in RAW[c]:
            if r['stage'] in ['blind', 'answer_check', 'depth_backfill', 'boundary_revision', 'hold']:
                states.append(dict(case_id=c, record_id=r['record_id'], stage=r['stage'], source_line=r['line'],
                                   source_path='data/기본기_연구/astra_handoff_queue.jsonl', payload=r['payload']))
                if r['stage'] == 'answer_check' and r['payload'].get('official_answer') is not None:
                    official.append(r['payload']['official_answer'])
    def answer_number(value):
        return '①②③④⑤'.index(value) + 1 if isinstance(value, str) and value in '①②③④⑤' else int(value)
    answer_records = [r for r in states if r['stage']=='answer_check' and r['payload'].get('official_answer') is not None]
    effective_official = official[-1] if official else None
    if len({answer_number(a) for a in official}) > 1:
        last = answer_records[-1]['payload']
        referenced = last.get('original_mismatch_record_preserved')
        if not last.get('resolution') or referenced not in {r['record_id'] for r in answer_records[:-1]}:
            raise ValueError('상이한 정답 기록의 명시적 해소 연결이 필요함')
    if official and answer_number(effective_official) != answer_number(answer):
        raise ValueError(f'공식답 재검토 필요: 입력 {answer}, 현행 {effective_official}, 이력 {official}')
    finalized = []
    for n, sc in enumerate(scenes, 1):
        sc = dict(sc)
        sc['event_id'] = f'QBF01-{q["unique_question"]}-S{n:02}'
        sc['passage_evidence'] = [evidence(q, t) for t in sc.pop('evidence_quotes')]
        sc['option_evidence'] = [evidence(q, s['choices'][i - 1], option=i) for i in sc['option_numbers']]
        for link in sc['pattern_connections']:
            pid = link['pattern_id']
            if pid in PATTERNS:
                link['definition_source'] = '분석/패턴_종합연구/20261012_corpus_sweep_01/pattern_candidates.json'
                link['definition_reused'] = True
            else:
                if pid not in {x['candidate_id'] for x in rows(OUT / 'new_pattern_candidates.jsonl')}:
                    raise ValueError('정의 없는 신규 후보: ' + pid)
                link['definition_source'] = str(OUT.relative_to(ROOT) / 'new_pattern_candidates.jsonl')
                link['definition_reused'] = True
        sc['reasoning_evidence_state'] = '이번 사후 보완의 복원 추론; 최초 실제 사용 여부는 original_observed_behavior와 별도'
        finalized.append(sc)
    rec = dict(record_id='QBF01-' + q['unique_question'] + '-review', unique_question=q['unique_question'],
        unique_group=q['unique_group'], exam_family=q['exam_family'], case_ids=q['case_ids'],
        batch_number=(next(i for i, t in enumerate(TARGETS) if t['unique_question'] == q['unique_question']) // 40) + 1,
        source_status=source_status, source_entry=e['analysis_id'], source_path=e['source_path'],
        supplementary_source_evidence=[supplement_record(p) for p in supplementary_sources or []],
        source_derivation=s.get('backfill_source_derivation'),
        source_sha256=sha(ROOT / e['source_path']), stem_evidence=evidence(q, s['stem'], field='stem'),
        exposure='기존 원문·기존 최초풀이·정답대조를 열람한 사후 보완; 신규 blind 실적 아님',
        selected_answer=answer, official_answer_values=official,
        effective_official_answer=effective_official, effective_answer_source_record_id=answer_records[-1]['record_id'] if answer_records else None,
        answer_history_resolution=answer_records[-1]['payload'].get('resolution') if answer_records else None,
        official_answer_status='기존 정답대조 raw 확인' if official else '기존 별도풀이 정답 근거의 추가 확인 필요',
        original_evidence_states=states, original_evidence_immutable=True,
        original_alternative_solution_paths=[ANALYSES[a].get('solution_paths') for a in q['analysis_ids'] if ANALYSES[a].get('solution_paths')],
        all_options_actually_reviewed=all(x['actual_review'] for x in option_checks), option_checks=option_checks,
        scenes=finalized, alternative_valid_solution=alternative,
        unresolved=unresolved or [], additional_note=note,
        processing_status='심층 추출 완료·일부 근거 유보' if unresolved else '심층 추출 완료')
    append('raw_question_reviews.jsonl', [rec])
    print(q['unique_question'], '저장', len(finalized), '장면')

def refresh():
    raw_saved = rows(OUT / 'raw_question_reviews.jsonl') if (OUT / 'raw_question_reviews.jsonl').exists() else []
    saved = copy.deepcopy(raw_saved)
    corrections = OUT / 'question_amendments.jsonl'
    for amendment in rows(corrections) if corrections.exists() else []:
        rec = next(r for r in saved if r['unique_question'] == amendment['unique_question'])
        for change in amendment['changes']:
            parts = change['field_path'].split('.')
            obj = rec
            for part in parts[:-1]: obj = obj[int(part)] if isinstance(obj, list) else obj[part]
            key = int(parts[-1]) if isinstance(obj, list) else parts[-1]
            if obj[key] != change['old_value']: raise ValueError('문항 수정 전 값 불일치')
            obj[key] = change['new_value']
    done = {x['unique_question']: x for x in saved}
    statuses = []
    for n, q in enumerate(TARGETS, 1):
        r = done.get(q['unique_question'])
        statuses.append(dict(order=n, unique_question=q['unique_question'], exam_family=q['exam_family'],
            case_ids=q['case_ids'], status=r['processing_status'] if r else '미처리',
        source_status=r['source_status'] if r else '미검토',
            deep_extraction=bool(r and r['scenes']), all_options_actually_reviewed=bool(r and r['all_options_actually_reviewed']),
            unresolved=bool(r and r['unresolved']), event_ids=[s['event_id'] for s in r['scenes']] if r else []))
    jsonl('question_review_status.jsonl', statuses)
    scenes = [dict(unique_question=r['unique_question'], unique_group=r['unique_group'], exam_family=r['exam_family'], **copy.deepcopy(sc)) for r in saved for sc in r['scenes']]
    amendments_path = OUT / 'scene_amendments.jsonl'
    by_event = {s['event_id']: s for s in scenes}
    for amendment in rows(amendments_path) if amendments_path.exists() else []:
        sc = by_event[amendment['event_id']]
        for change in amendment['changes']:
            parts = change['field_path'].split('.')
            obj = sc
            for part in parts[:-1]: obj = obj[part]
            if obj[parts[-1]] != change['old_value']:
                raise ValueError('수정 전 값 불일치: ' + amendment['amendment_id'])
            obj[parts[-1]] = change['new_value']
        sc.setdefault('applied_amendment_ids', []).append(amendment['amendment_id'])
    dev_path = OUT / 'pattern_development.jsonl'
    if dev_path.exists():
        devs = rows(dev_path)
        superseded = {d['supersedes'] for d in devs if d.get('supersedes')}
        current_devs = [d for d in devs if d['development_id'] not in superseded]
        for d in current_devs:
            for eid in d.get('evidence_event_ids', []):
                if eid not in by_event: raise ValueError('귀납 근거 ID 없음: ' + eid)
        jsonl('pattern_development_current.jsonl', current_devs)
    current_reviews = copy.deepcopy(saved)
    for rec in current_reviews:
        rec['scenes'] = [by_event[sc['event_id']] for sc in rec['scenes']]
    jsonl('current_question_reviews.jsonl', current_reviews)
    jsonl('new_judgment_scenes.jsonl', scenes)
    jsonl('pattern_links.jsonl', [dict(unique_question=s['unique_question'], exam_family=s['exam_family'], event_id=s['event_id'], **p) for s in scenes for p in s['pattern_connections']])
    jsonl('educational_production_ideas.jsonl', [dict(unique_question=s['unique_question'], event_id=s['event_id'], **s['educational_production']) for s in scenes])
    jsonl('unresolved_cases.jsonl', [dict(unique_question=r['unique_question'], case_ids=r['case_ids'], issues=r['unresolved']) for r in saved if r['unresolved']])
    for batch in sorted({r['batch_number'] for r in saved}):
        jsonl(f'batch_{batch:03}_question_reviews.jsonl', [r for r in raw_saved if r['batch_number'] == batch])
    families = {}
    for f in ['KICE', 'LEET', 'MEET']:
        rs = [r for r in saved if r['exam_family'] == f]
        families[f] = dict(target=sum(q['exam_family'] == f for q in TARGETS), reviewed=len(rs),
            deeply_extracted=sum(bool(r['scenes']) for r in rs), scenes=sum(len(r['scenes']) for r in rs),
            unresolved_questions=sum(bool(r['unresolved']) for r in rs), remaining=sum(q['exam_family'] == f for q in TARGETS) - len(rs))
    counts = {}
    for pid in {p['pattern_id'] for s in scenes for p in s['pattern_connections']}:
        counts[pid] = {f: len({s['unique_question'] for s in scenes if s['exam_family'] == f and any(p['pattern_id'] == pid for p in s['pattern_connections'])}) for f in ['KICE', 'LEET', 'MEET']}
    write('pattern_question_counts.json', dict(counting_unit='시험별 고유 문항; 동일 문항의 동일 패턴 반복 장면은 1회', counts=counts))
    pending = next((q for q in TARGETS if q['unique_question'] not in done), None)
    write('checkpoint.json', dict(run_id=OUT.name, date=datetime.now(ZoneInfo('Asia/Seoul')).date().isoformat(), status='진행 중',
        scope='기존 1차 탐색 미추출 1077문항의 사후 심층 보완', target_count=1077,
        reviewed_questions=len(saved), new_scene_count=len(scenes), by_exam=families,
        next_question=pending['unique_question'] if pending else None,
        next_case_ids=pending['case_ids'] if pending else [],
        next_order=next((n for n, q in enumerate(TARGETS, 1) if q['unique_question'] not in done), None),
        completed_batches=[b for b in sorted({r['batch_number'] for r in saved}) if sum(r['batch_number'] == b for r in saved) == 40],
        batch_size=40, other_models_called=True,
        delegation={'model':'gpt-6-luna','scope':'사용자 후속 지시로 허용된 기존 풀이 경로 검색만','semantic_judgment_delegated':False},
        git_push=False, frozen_assets_written=False,
        holds_preserved=['G024', 'G370'], quota_status='runtime에 구체 잔여치 미노출·추정하지 않음',
        first_batch_semantic_sample_audit='semantic_sample_audits.jsonl',
        resume_command='python3 backfill_io.py packet <next_order> 5',
        provenance_limit='기존 source 텍스트와 정답대조 raw에 대한 사후 분석. 공식 시험지 이미지 독립 전수 대조 아님.'))
    print(json.dumps({'검토문항': len(saved), '신규장면': len(scenes), '다음': pending['unique_question'] if pending else None}, ensure_ascii=False))

def validate(check_protection=False):
    saved = rows(OUT / 'current_question_reviews.jsonl')
    errors = []
    source_cache = {}
    eids = set()
    for r in saved:
        q = BYQ[r['unique_question']]
        if len(r['option_checks']) != len(source(q)['choices']):
            errors.append(r['unique_question'] + ': 선지수')
        evs = [r['stem_evidence']] + [e for o in r['option_checks'] for e in o['source_evidence'] + [o['option_evidence']]]
        for sc in r['scenes']:
            if sc['event_id'] in eids:
                errors.append('장면 ID 중복')
            eids.add(sc['event_id'])
            evs += sc['passage_evidence'] + sc['option_evidence']
        for ev in evs:
            ev_path = ev['source_path']
            if ev_path not in source_cache:
                source_cache[ev_path] = (json.loads((ROOT / ev_path).read_text()), sha(ROOT / ev_path))
            s, digest = source_cache[ev_path]
            if digest != ev['source_sha256']: errors.append(r['unique_question'] + ': 근거 파일 해시')
            text = s[ev['field']] if ev['option_number'] is None else s['choices'][ev['option_number'] - 1]
            if text[ev['char_start']:ev['char_end']] != ev['quote']:
                errors.append(r['unique_question'] + ': 원문 offset')
    changed = []
    if check_protection:
        for name, digest in json.loads((OUT / 'protected_input_hashes.json').read_text()).items():
            if sha(ROOT / name) != digest:
                changed.append(name)
    report = dict(reviewed_questions=len(saved), scenes=len(eids), mechanical_errors=errors,
        protected_input_changes=changed, protection_checked=check_protection,
        interpretation='현행 amendment 적용 문항·장면에서 각 증거가 지정한 파일의 구간·해시·선지수·ID를 검사. 의미 타당성은 별도 직접 표본 감사.',
        pass_mechanical=not errors and not changed)
    write('validation_report.json', report)
    print(json.dumps(report, ensure_ascii=False))

if __name__ == '__main__':
    command = sys.argv[1]
    if command == 'init': init()
    elif command == 'packet': packet(int(sys.argv[2]), int(sys.argv[3]))
    elif command == 'refresh': refresh()
    elif command == 'validate': validate('--protection' in sys.argv)
    elif command == 'patterns': print('\n'.join(f'{p}: {v["D"]}' for p, v in PATTERNS.items()))
