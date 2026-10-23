"""이미 실행한 인라인 amendment 명령의 보존본. 중복 실행은 guard에서 거부한다."""
import sys
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write
from resume_support_20261015_07 import finish
aid='QBF01-AMD048'
assert aid not in {a['amendment_id'] for a in rows(OUT/'scene_amendments.jsonl')},'이미 처리된 amendment: 재실행 금지'
r=next(r for r in rows(OUT/'current_question_reviews.jsonl') if 'BNV' in r['case_ids'])
sc=r['scenes'][1]
assert [p['pattern_id'] for p in sc['pattern_connections']]==['하한정확값']
append('scene_amendments.jsonl',[{'amendment_id':aid,'event_id':sc['event_id'],'reason':'기존 하한정확값은 최소값/실제값 구별과 차감 조건이다. BNV 상한100% 비교로 확대하지 않음. 추론·정답은 유지하고 후보 연결만 비움.','changes':[{'field_path':'pattern_connections','old_value':sc['pattern_connections'],'new_value':[]}]}])
write('BNV_upper_bound_pattern_review.json',{'amendment_id':aid,'scene':sc['event_id'],'decision':'후보 연결 비움. 상한 비교 행동 보존.','semantic_inference_changed':False})
finish('amend_BNV_upper_bound.py',['BNV'],['AMD048 BNV의 하한정확값 과잉 연결 제거. 원raw 보존.'])
