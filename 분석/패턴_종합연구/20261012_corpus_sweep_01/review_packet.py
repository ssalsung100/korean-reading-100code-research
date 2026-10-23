"""선택한 기존 완성 풀이의 원문과 중간 추론 열람. 의미 판정·분류는 하지 않는다."""
import collections, json, sys
from corpus_io import ROOT, OUT, rows, get_source

analyses = rows(str(OUT.relative_to(ROOT) / 'manifest_analyses.jsonl'))
bycase = collections.defaultdict(list)
for line, record in enumerate(rows('data/기본기_연구/astra_handoff_queue.jsonl'), 1):
    bycase[record.get('case')].append((line, record))
seen = set()
for case in sys.argv[1:]:
    entry = next(e for e in analyses if e['case_id'] == case and e['origin'] == 'prepared')
    source = get_source(entry)
    print('\n###', entry['unique_group'], case)
    if entry['unique_group'] not in seen:
        print('본문', source.get('passage_text', ''))
        seen.add(entry['unique_group'])
    print('발문', source.get('stem'))
    print('선지', json.dumps(source.get('choices'), ensure_ascii=False))
    for line, record in bycase[case]:
        stage, payload = record['stage'], record['payload']
        if stage in ('blind', 'answer_check'):
            selected = {k: v for k, v in payload.items() if any(t in k for t in
                ('logic', 'intermediate', 'distractor', 'correction', 'refinement', 'discrepancy'))}
        elif stage in ('depth_backfill', 'boundary_revision'):
            selected = payload
        elif stage in ('independent_code', 'sdss_compare', 'sdss_disclosure'):
            selected = {k: v for k, v in payload.items() if any(t in k for t in
                ('refinement', 'semantic', 'correction', 'unresolved', 'code_free'))}
        else:
            continue
        if selected:
            print(stage, line, json.dumps(selected, ensure_ascii=False))
