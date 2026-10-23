from pathlib import Path
import json,hashlib
from datetime import datetime,timezone

RUN=Path(__file__).resolve().parent
ROOT=RUN.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read_jsonl(name):return [json.loads(s) for s in (RUN/name).read_text().splitlines() if s.strip()]
def dump(name,obj):(RUN/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

assert not (RUN/'freeze_record.json').exists(), '고정한 실행을 덮어쓰지 않음'
targets=json.loads((RUN/'targets.json').read_text())
qs=read_jsonl('independent_solutions.jsonl');ps=read_jsonl('passage_analyses.jsonl')
scenes=read_jsonl('decision_scenes.jsonl');anchors=read_jsonl('evidence_anchors.jsonl');links=read_jsonl('evidence_links.jsonl')
candidates=json.loads((RUN/'independent_candidates.json').read_text())['candidates']
expected={c for s in targets['samples'] for c in s['case_ids']}
assert {q['case_id'] for q in qs}==expected and len(qs)==21
assert len(ps)==6 and len(scenes)==126 and len(anchors)==75 and len(links)==254
assert len(candidates)==20
assert {q['case_id'] for q in qs if q['independent_answer'] is None}=={'RX'}
assert all(len(q['option_judgments'])==5 for q in qs)
assert all(q['independent_answer'] is None or 1<=q['independent_answer']<=5 for q in qs)
assert all(q['repeatable_action'] and q['applicable_when'] and q['do_not_apply_when'] and
           q['alternative_routes'] and q['production_implications'] for q in qs)
assert not {'G024','G370'} & {q['passage_group'] for q in qs}
assert all(not q['current_session_answer_or_pattern_exposure'] for q in qs)

for s in targets['samples']:
    texts=[json.loads((RUN/'sources'/f'{c}.json').read_text())['passage_text'] for c in s['case_ids']]
    assert len(set(texts))==1, s['passage_group']+'의 지문 사본 차이'
for a in anchors:
 for loc in a['locations']:
    p=RUN/loc['file'];text=p.read_text() if loc['field']=='whole_text' else json.loads(p.read_text())[loc['field']]
    assert text[loc['char_start']:loc['char_end']]==a['quote']
    assert text[loc['paragraph_context_start']:loc['paragraph_context_end']]==loc['paragraph_context']
assert len({a['evidence_id'] for a in anchors})==75
aid={a['evidence_id'] for a in anchors};sid={s['scene_id'] for s in scenes}
assert all(l['evidence_id'] in aid and l['scene_id'] in sid for l in links)
assert all(set(c['evidence_ids'])<=aid and set(c['decision_scene_ids'])<=sid for c in candidates)
assert all(set(c['cases'])<=expected for c in candidates)
for q in qs:
 src=json.loads((RUN/'sources'/f"{q['case_id']}.json").read_text())
 for o,t in zip(q['option_judgments'],src['choices']):
    scene=next(s for s in scenes if s['scene_id']==q['case_id']+'-option-'+str(o['option']))
    assert scene['source_option_text']==t
    assert bool(scene['full_option_available'])==(q['case_id']!='RX')

inventory=json.loads((RUN/'source_inventory.json').read_text())
assert all(x.get('model_content_viewed') for x in inventory if x.get('case_id'))
for x in inventory:
 assert (ROOT/x['path']).exists() and sha(ROOT/x['path'])==x['sha256']
 if x.get('copy'):assert sha(RUN/x['copy'])==x['copy_sha256']
baseline=json.loads((RUN/'preservation_baseline.json').read_text())
changed=[x['path'] for x in baseline if not (ROOT/x['path']).is_file() or sha(ROOT/x['path'])!=x['sha256']]
assert not changed, changed
dump('preservation_report.json',{'status':'통과','checked_files':len(baseline),'changed_files':changed,
 'scope':'기존 패턴 연구 3폴더·이번에 사용한 blind 원문 및 보충·RX 진단 정본. 저장소 전체 파일의 전후 해시 증명은 아님.',
 'hold_actions':{'G024':'읽기·재개·상태 변경 없음','G370':'읽기·재개·상태 변경 없음'},
 'old_files_modified_by_this_run':False})
dump('validation_report.json',{'status':'통과','checks':{
 '고정 6세트 21ID 일치':True,'지문 중복 사본 내용 동일':True,'모든 문항 5선지 슬롯 기록':True,
 'RX B열 결손과 번호 보류 명시':True,'20독립 선택·1보류':True,
 '75근거 원문 문자 위치 일치':True,'254판단-근거 연결 참조 유효':True,
 '126판단 장면 및 원문 선지 복사 일치':True,'20후보 근거와 장면 참조 유효':True,
 '원본·사본 해시 일치':True,'범위 내 기존 파일 보존':True},
 'semantic_limit':'기계적 일관성 검사이며 공식 정답 정확성·후보 타당성·완전 독립성을 자동 입증하지 않음.',
 'answer_check_performed':False,'codebook_comparison_performed':False})

excluded={'freeze_manifest.json','freeze_manifest.sha256','freeze_record.json'}
files=[p for p in sorted(RUN.rglob('*')) if p.is_file() and p.name not in excluded and '__pycache__' not in p.parts]
rows=[{'path':str(p.relative_to(RUN)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]
stamp=datetime.now(timezone.utc).isoformat()
dump('freeze_manifest.json',{'stage':'독립 검증 1단계','frozen_at_utc':stamp,'algorithm':'SHA-256','files':rows,
 'exclusions':['고정 메타데이터 3파일은 최종 freeze_record에서 별도 해시 연결','__pycache__: 파이썬 실행 캐시·연구 결과 아님'],
 'source_hashes':'source_inventory.json','preservation':'preservation_report.json','next_action':'작업 종료·기존 코드북/공식 정답 대조 없음'})
(RUN/'freeze_manifest.sha256').write_text(''.join(row['sha256']+'  '+row['path']+'\n' for row in rows))
dump('freeze_record.json',{'stage':'1단계 결과 고정 완료','frozen_at_utc':stamp,'payload_file_count':len(rows),
 'run_folder':str(RUN.relative_to(ROOT)),
 'freeze_manifest_sha256':sha(RUN/'freeze_manifest.json'),
 'freeze_sha256_list_sha256':sha(RUN/'freeze_manifest.sha256'),
 'result_report_sha256':sha(RUN/'00_1단계_결과.md'),
 'candidates_sha256':sha(RUN/'independent_candidates.json'),
 'solutions_sha256':sha(RUN/'independent_solutions.jsonl'),
 'summary':{'groups':6,'questions':21,'selected':20,'hold':['RX'],'historical_exposure_group':'G095','historical_exposure_count':5,'candidate_counts':[4,6,10]},
 'integrity_note':'이 기록 자체의 SHA-256을 최종 응답으로 제시해 manifest·결과·개별 파일의 해시 연결을 외부에 고정한다.',
 'stopped_before_comparison':True})
for row in rows:assert sha(RUN/row['path'])==row['sha256']
print(json.dumps({'status':'검증·고정 완료','file_count':len(rows),
 'preserved_files':len(baseline),'freeze_record_sha256':sha(RUN/'freeze_record.json'),
 'freeze_manifest_sha256':sha(RUN/'freeze_manifest.json'),
 'result_report_sha256':sha(RUN/'00_1단계_결과.md')},ensure_ascii=False,indent=2))
