"""이번 재개분의 상태 연결만 보완. 의미 판단 생성 없음."""
import json
from backfill_io import OUT,rows,write
from resume_support_20261015 import guard,prior,finish as previous_finish

def finish(author,cases,notes=()):
    previous_finish(author,cases,notes)
    c=json.loads((OUT/'checkpoint.json').read_text())
    audits=rows(OUT/'semantic_sample_audits.jsonl')
    last=max(a['batch'] for a in audits)
    c.update(last_saved_audit=f'audit_{last:03}.py',next_sample_audit_at=(last+1)*40,latest_session_progress='session_progress_20261015_04.json')
    write('checkpoint.json',c)
    write('session_progress_20261015_04.json',{'start_reviewed':618,'start_scenes':986,'current_reviewed':c['reviewed_questions'],'current_scenes':c['new_scene_count'],'new_questions':c['reviewed_questions']-618,'new_scenes':c['new_scene_count']-986,'remaining':1077-c['reviewed_questions'],'last_saved_author':author,'last_audit':c['last_saved_audit'],'next_order':c['next_order'],'next_question':c['next_question'],'next_cases':c['next_case_ids'],'next_sample_audit_at':c['next_sample_audit_at'],'status':'진행 중','current_session_other_models_called':False})
