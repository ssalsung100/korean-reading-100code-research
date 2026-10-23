"""이번 재개분의 저장 확인과 인계 갱신. 의미 판단을 생성하지 않는다."""
import json
from backfill_io import OUT, ROOT, rows, write, refresh, sha, BYCASE, RAW

def guard(cases):
    saved = {r['unique_question'] for r in rows(OUT/'raw_question_reviews.jsonl')}
    assert not any(BYCASE[c]['unique_question'] in saved for c in cases), '기저장 문항 포함: 재실행 금지'

def prior(cases, name, extra=None):
    obj = {'date':'2026-10-15', 'prior_independent':{c:[r for r in RAW[c] if r['stage']=='independent_code'] for c in cases}}
    obj.update(extra or {})
    write(name, obj)
    return str(OUT.relative_to(ROOT)/name)

def finish(author, cases, notes=()):
    refresh()
    selected = [r for r in rows(OUT/'current_question_reviews.jsonl') if set(r['case_ids']) & set(cases)]
    assert len(selected) == len(cases)
    errors=[]; cache={}; ids=set()
    for r in selected:
        evs=[r['stem_evidence']]
        assert r['all_options_actually_reviewed']
        for o in r['option_checks']: evs += o['source_evidence']+[o['option_evidence']]
        for s in r['scenes']:
            assert s['event_id'] not in ids
            ids.add(s['event_id']); evs += s['passage_evidence']+s['option_evidence']
        for e in evs:
            p=e['source_path']
            if p not in cache: cache[p]=(json.loads((ROOT/p).read_text()),sha(ROOT/p))
            src,digest=cache[p]
            t=src[e['field']] if e['option_number'] is None else src['choices'][e['option_number']-1]
            if isinstance(t,dict): t=t['text']
            if digest != e['source_sha256'] or t[e['char_start']:e['char_end']] != e['quote']: errors.append(r['unique_question'])
        for e in r['supplementary_source_evidence']:
            assert (ROOT/e['path']).exists()
    assert not errors, errors
    validation={'scope':'이번 작성 문항만 검사; 보호 원장 전수 검증 없음','case_ids':cases,'questions':len(selected),'scenes':len(ids),'options':sum(len(r['option_checks']) for r in selected),'errors':errors,'pass':True}
    write(author.replace('.py','_validation.json'),validation)
    c=json.loads((OUT/'checkpoint.json').read_text())
    c['current_session_other_models_called']=False
    c['current_session_semantic_judgment']='주 에이전트 직접 수행'
    c['last_saved_author']=author
    c['last_incremental_validation']=author.replace('.py','_validation.json')
    c['audited_batches']=[a['batch'] for a in rows(OUT/'semantic_sample_audits.jsonl')]
    write('checkpoint.json',c)
    h=json.loads((OUT/'session_handoff_20261013.json').read_text())
    h.update(reviewed_questions=c['reviewed_questions'],new_scenes=c['new_scene_count'],by_exam=c['by_exam'],next_order=c['next_order'],next_unique_question=c['next_question'],next_case=c['next_case_ids'][0] if c['next_case_ids'] else None,read_but_not_saved=[],last_saved_author=author,next_author_suggestion='미처리 다음 순서에 맞는 새 author 파일 사용',batch_state=f"{c['reviewed_questions']}문항 저장. 표본 감사 완료 배치 {c['audited_batches']}. 다음 40문항 경계에서 감사.",resume_command=f"python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet {c['next_order']} 2",validation=f"{author.replace('.py','_validation.json')}에 신규 작성분만 구간·해시·참조 검증. 기존 전수 검증 반복 없음.")
    h['important_corrections']+=list(notes)
    h['current_session_delegation']='이번 재개 세션에서 다른 모델 호출 없음. 핵심 판단·도식 판독·의미 감사는 주 에이전트 직접 수행.'
    write('session_handoff_20261013.json',h)
    print(json.dumps(validation,ensure_ascii=False))
