"""이번 재개분 저장 확인. 과거 인계 파일은 보존하고 새 인계만 갱신한다."""
import json
from backfill_io import OUT, ROOT, rows, write, refresh, sha
from resume_support_20261015 import guard, prior

def finish(author, cases, notes=()):
    refresh()
    selected = [r for r in rows(OUT/'current_question_reviews.jsonl') if set(r['case_ids']) & set(cases)]
    assert len(selected) == len(cases)
    errors=[]; cache={}; ids=set()
    for r in selected:
        assert r['all_options_actually_reviewed']
        evs=[r['stem_evidence']]
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
            assert sha(ROOT/e['path']) == e['sha256']
    assert not errors, errors
    validation={'scope':'이번 작성 또는 감사 배치만 인용·근거 연결 검사; 보호 원장 전수 검사 없음','case_ids':cases,'questions':len(selected),'scenes':len(ids),'options':sum(len(r['option_checks']) for r in selected),'errors':errors,'pass':True}
    write(author.replace('.py','_validation.json'),validation)
    c=json.loads((OUT/'checkpoint.json').read_text())
    audits=rows(OUT/'semantic_sample_audits.jsonl')
    for a in rows(OUT/'audit_amendments.jsonl'):
        target=next(r for r in audits if r['audit_id']==a['audit_id'])
        for change in a['changes']:
            assert target[change['field']]==change['old_value']
            target[change['field']]=change['new_value']
    write('current_semantic_sample_audits.json',{'basis':'semantic_sample_audits.jsonl + audit_amendments.jsonl; 최초 감사 기록 보존','audits':audits})
    last=max(a['batch'] for a in audits)
    previous=json.loads((OUT/'continuous_research_progress.json').read_text())
    last_author=author if author.startswith('author_') else previous['last_saved_author']
    c.update(current_session_other_models_called=False,current_session_semantic_judgment='주 에이전트 직접 수행',last_saved_author=last_author,last_incremental_validation=author.replace('.py','_validation.json'),audited_batches=[a['batch'] for a in audits],audit_current_view='current_semantic_sample_audits.json',audit_amendments='audit_amendments.jsonl',last_saved_audit=f'audit_{last:03}.py',next_sample_audit_at=(last+1)*40,latest_session_progress='continuous_research_progress.json',latest_session_handoff='session_handoff_20261015_07.json',read_but_not_saved=[],continuation_policy='사용자 중단·실제 환경 한계까지 계속. 배치 완료 자체는 종료 사유 아님.')
    write('checkpoint.json',c)
    hpath=OUT/'session_handoff_20261015_07.json'
    h=json.loads((hpath if hpath.exists() else OUT/'session_handoff_20261015_06.json').read_text())
    for k in ['pause_request','pause_reason','pause_files','current_continuation_saved']: h.pop(k,None)
    completed=rows(OUT/'current_question_reviews.jsonl')
    lastq=completed[-1]
    current_batch=(c['next_order']-1)//40+1 if c['next_order'] else 27
    current=[r for r in completed if r['batch_number']==current_batch]
    h.update(status='연속 연구 중; 최신 저장점 자동 갱신',reviewed_questions=c['reviewed_questions'],new_scene_count=c['new_scene_count'],remaining_questions=c['target_count']-c['reviewed_questions'],by_exam=c['by_exam'],last_completed_question=lastq['unique_question'],last_completed_order=c['reviewed_questions'],last_completed_cases=lastq['case_ids'],last_saved_script=last_author,last_validation=author.replace('.py','_validation.json'),next_order=c['next_order'],next_question=c['next_question'],next_cases=c['next_case_ids'],last_audited_batch=last,next_sample_audit_at=c['next_sample_audit_at'],last_development=rows(OUT/'pattern_development.jsonl')[-1]['development_id'],unresolved_questions=sum(x['unresolved_questions'] for x in c['by_exam'].values()),read_but_not_saved=[],this_save_notes=list(notes),resume_command=f"python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet {c['next_order']} 3",next_procedure='기저장 author/audit 재실행 금지. 새 author 작성→preflight→한 번 저장→구간 검사. 40문항 경계 감사 후 계속.',continuation='현재 사용자가 재개함. 이전 일시중단 해제. 배치 완료를 종료 사유로 삼지 않음.',next_source_exposure='다음 문항 노출 상태는 read_but_not_saved와 이번 인계 세부 기록 참조.',current_batch={'batch':current_batch,'orders':[(current_batch-1)*40+1,min(current_batch*40,1077)],'saved_questions':len(current),'saved_scenes':sum(len(r['scenes']) for r in current),'next_audit_at':c['next_sample_audit_at']})
    h.setdefault('session_07_notes',[]).extend(notes)
    h['session_07_saved']={'start_reviewed':756,'start_scenes':1180,'added_questions':c['reviewed_questions']-756,'added_scenes':c['new_scene_count']-1180}
    write('session_handoff_20261015_07.json',h)
    write('continuous_research_progress.json',{'status':'계속 진행 중','start_reviewed':756,'start_scenes':1180,'current_reviewed':c['reviewed_questions'],'current_scenes':c['new_scene_count'],'added_questions':c['reviewed_questions']-756,'added_scenes':c['new_scene_count']-1180,'last_saved_author':last_author,'next_order':c['next_order'],'next_question':c['next_question'],'next_cases':c['next_case_ids'],'next_sample_audit_at':c['next_sample_audit_at'],'read_but_not_saved':[],'other_models_called':False})
    print(json.dumps(validation,ensure_ascii=False))
