import sys,json
sys.dont_write_bytecode=True
import backfill_io as b
raw=b.rows(b.OUT/'raw_question_reviews.jsonl');cur=b.rows(b.OUT/'current_question_reviews.jsonl');target=b.rows(b.OUT/'target_manifest.jsonl')
errors=[];ids=[r['unique_question'] for r in raw]
if len(ids)!=len(set(ids)):errors.append('raw 고유문항 중복')
if set(ids)!={r['unique_question'] for r in target}:errors.append('대상/raw 불일치')
if {r['unique_question'] for r in cur}!=set(ids):errors.append('raw/current 대상 불일치')
if any(not r['scenes'] or len(r['option_checks'])!=5 or not r['all_options_actually_reviewed'] for r in cur):errors.append('빈 장면/선지 검토 누락')
cache={};supp=0;checked_answers=0;separate_answer_evidence=[]
def num(a):return '①②③④⑤'.index(a)+1 if isinstance(a,str) and a in '①②③④⑤' else int(a)
for r in cur:
 for e in r.get('supplementary_source_evidence',[]):
  p=e['path']
  if p not in cache:cache[p]=b.sha(b.ROOT/p)
  if cache[p]!=e['sha256']:errors.append(r['unique_question']+':부록해시')
  supp+=1
 a=r.get('effective_official_answer')
 if a is None and r.get('official_answer_values'):a=r['official_answer_values'][-1]
 if a is not None:
  checked_answers+=1
  if num(r['selected_answer'])!=num(a):errors.append(r['unique_question']+':현행공식답필드불일치')
 else:separate_answer_evidence.append({'unique_question':r['unique_question'],'case_ids':r['case_ids'],'status':r['official_answer_status']})
aud=json.loads((b.OUT/'current_semantic_sample_audits.json').read_text())['audits']
if sorted(a['batch'] for a in aud)!=list(range(1,28)):errors.append('감사번호누락중복')
for n in range(1,28):
 actual=[r for r in cur if r['batch_number']==n]
 if len(actual)!=(40 if n<27 else 37):errors.append(f'{n}:묶음문항수')
r={'scope':'전체대상/raw/current고유ID·5선지·장면존재·보유공식답필드·부록해시·감사1~27누락검사','target_questions':len(target),'raw_questions':len(raw),'current_questions':len(cur),'raw_scenes':sum(len(x['scenes']) for x in raw),'current_scenes':sum(len(x['scenes']) for x in cur),'scene_count_difference_explained':'기존question_amendment에의한현행장면추가1건;원raw불변','options':sum(len(x['option_checks']) for x in cur),'unresolved_questions':sum(bool(x['unresolved']) for x in cur),'supplement_references_checked':supp,'unique_supplement_files_checked':len(cache),'official_answer_fields_checked':checked_answers,'cases_requiring_separate_answer_evidence':separate_answer_evidence,'audit_count':len(aud),'sample_questions_total':sum(a['sample_questions'] for a in aud),'sample_scenes_total':sum(a['sample_scenes'] for a in aud),'sample_options_explicitly_recorded_total':sum(a.get('sample_options',0) for a in aud),'audits_without_explicit_option_count':[a['audit_id'] for a in aud if 'sample_options' not in a],'pending_backfill_raw':len(set(ids)-{r['unique_question'] for r in cur}),'errors':errors,'pass':not errors,'limits':'기존초기스키마는부록필드가없고일부별도풀이문항은공식답배열이없을수있다.없는필드는새로확인한것으로가정하지않고별도목록에보존.공식원문이미지·원정답표독립전수대조나의미유보해소를뜻하지않음.기본기rawqueue가아닌본보완원장반영상태.'}
b.write('final_integrity_20261016.json',r);print(json.dumps(r,ensure_ascii=False))
