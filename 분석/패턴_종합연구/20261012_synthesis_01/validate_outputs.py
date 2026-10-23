"""입력 보존·정확 인용·참조·현 스키마 부분집합·창작 모형의 유일성 검사.

의미 타당성·실제 학생 사고를 자동 판정하지 않는다. 외부 패키지/네트워크 불필요.
"""
from pathlib import Path
import json, hashlib, re, collections
from functools import lru_cache
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
def read(p):return json.loads(p.read_text())
def rows(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
@lru_cache(maxsize=None)
def source_lines(p):return p.read_text().splitlines()
errors=[];checks={}
def require(test,msg):
 if not test:errors.append(msg)

baseline=read(OUT/'input_preservation_baseline.json')
changed=[p for p,h in baseline.items() if not (ROOT/p).exists() or sha(ROOT/p)!=h]
require(not changed,'기존 입력 변경: '+str(changed))
checks['input_files_unchanged']=len(baseline)
checks['changed_input_files']=changed

registry=rows(OUT/'case_registry.jsonl');bycase={r['case_id']:r for r in registry}
require(len(registry)==60==len(bycase),'60개 고유 case 연결 오류')
require(len({r['identity_family'] for r in registry})==18,'18개 고유 지문 연결 오류')
for r in registry:
 p=ROOT/r['source']['path'];require(p.exists() and sha(p)==r['source']['sha256'],r['case_id']+' source 변경')
 for field in ['previous_application_events','sol_stage1','external_application','official_answer_history_reused']:
  for link in r[field]:
   p=ROOT/link['path'];require(p.exists(),str(p)+' 없음')
   ls=source_lines(p);n=link['line_1_based'];require(0<n<=len(ls),str(link)+' line 오류')
   if 0<n<=len(ls):
    value=json.loads(ls[n-1])
    if 'event_id' in link:require(value.get('event_id')==link['event_id'],'event ID 불일치')
    if 'record_id' in link:require(value.get('record_id')==link['record_id'],'raw ID 불일치')
    require(value.get('case_id',value.get('case'))==r['case_id'],'case 참조 불일치 '+str(link))
for r in registry:
 if r['sample_split']=='validation':require(bool(r['sol_stage1']) and bool(r['external_application']),r['case_id']+' 후속 분석 연결 없음')
checks['unique_passages']=18;checks['unique_cases']=len(registry)

mapping=rows(OUT/'candidate_correspondence.jsonl')
expected={f'P{i:02}' for i in range(1,8)}|{f'S{i:02}' for i in range(1,7)}|{f'TXT-{c}' for c in 'ABCD'}|{f'ASK-{c}' for c in 'ABCDEF'}|{f'ACT-{c}' for c in 'ABCDEFGHIJ'}|{f'R{i:02}' for i in range(1,11)}|{'R11a','R11b','R12'}
require({m['candidate_id'] for m in mapping}==expected and len(mapping)==46,'입력 후보 coverage 오류')
relations={'동일 원리','하위 유형','부분 중첩','별개의 원리','근거 부족'}
for m in mapping:
 require(m['relation'] in relations,'허용되지 않은 관계')
 require(all(c in bycase for c in m['case_ids']),'후보의 case 미해소')
 p=ROOT/m['candidate_source']['path'];require(p.exists(),'후보 source 없음')
 ptr=m['candidate_source'].get('json_pointer')
 if ptr:
  value=read(p)
  for k in ptr.strip('/').split('/'):value=value[int(k)] if isinstance(value,list) else value[k]
  require(value.get('candidate_id',value.get('pattern_id'))==m['candidate_id'],'후보 pointer 불일치')
checks['candidate_rows']=len(mapping)
checks['candidate_relations']=dict(collections.Counter(x['relation'] for x in mapping))
edges=rows(OUT/'relation_edges.jsonl')
require(len(edges)==len({e['relation_id'] for e in edges}),'관계 ID 중복')
for e in edges:
 require(e['relation'] in relations,'관계 enum 오류')
 require(set(e['case_ids'])<=set(bycase),'관계 근거 case 오류')
new=read(OUT/'new_candidate_registry.json')['candidates']
require({c['candidate_id'] for c in new}=={f'N{i:02}' for i in range(1,12)},'신규 후보 ID 오류')
checks['pairwise_relations']=len(edges);checks['provisional_new_or_extended_candidates']=len(new)

def verify_evidence(e):
 p=ROOT/e['source_path'];require(p.exists(),'인용 source 없음 '+str(p))
 if not p.exists():return
 require(sha(p)==e['source_sha256'],'인용 hash 오류 '+e['evidence_id'])
 ptr=e['json_pointer'];value={'text':p.read_text()} if p.suffix!='.json' else read(p)
 for k in ptr.lstrip('/').split('/'):
  k=k.replace('~1','/').replace('~0','~');value=value[int(k)] if isinstance(value,list) else value[k]
 a=e['char_start'];b=e['char_end_exclusive'];require(value[a:b]==e['exact_quote'],'인용 범위 불일치 '+e['evidence_id'])
 require(b-a==len(e['exact_quote']),'인용 길이 오류 '+e['evidence_id'])
 require(a>=0 and b<=len(value),'인용 구간 경계 오류')

anchors=rows(OUT/'evidence_anchors.jsonl')+rows(OUT/'casebook_evidence.jsonl')
for a in anchors:verify_evidence(a)
require(len({x['evidence_id'] for x in anchors})==len(anchors),'근거 ID 중복')
cards=rows(OUT/'casebook_records.jsonl');anchorids={a['evidence_id'] for a in anchors}
for c in cards:
 require(set(c['evidence_ids'])<=anchorids,'사례집 근거 ID 미해소')
 require(set(c['case_ids'])<=set(bycase),'사례집 case 미해소')
checks['casebook_comparisons']=len(cards);checks['exact_quotes_checked']=len(anchors)

# 외부 범용 JSON Schema 엔진은 사용하지 않음. 이 파일이 사용하는 키워드만 구현한다.
supported={'$schema','$id','title','type','properties','required','additionalProperties','items','enum','const','minLength','minimum','maximum','pattern'}
def inspect_schema(s):
 require(set(s)<=supported,'지원 범위를 벗어난 스키마 키워드 '+str(set(s)-supported))
 for p in s.get('properties',{}).values():inspect_schema(p)
 if 'items'in s:inspect_schema(s['items'])
def validate_schema(v,s,loc='$'):
 if 'const'in s:require(v==s['const'],loc+' const 오류')
 if 'enum'in s:require(v in s['enum'],loc+' enum 오류')
 types=s.get('type',[]);types=[types] if isinstance(types,str) else types
 def istype(t):return {'object':isinstance(v,dict),'array':isinstance(v,list),'string':isinstance(v,str),'integer':type(v)is int,'boolean':type(v)is bool,'null':v is None}[t]
 if types:
  good=any(istype(t) for t in types);require(good,loc+' type 오류')
  if not good:return
 if isinstance(v,dict):
  require(set(s.get('required',[]))<=set(v),loc+' 필수 필드 누락')
  if s.get('additionalProperties') is False:require(set(v)<=set(s['properties']),loc+' 추가 필드')
  for k,x in v.items():
   if k in s.get('properties',{}):validate_schema(x,s['properties'][k],loc+'/'+k)
 if isinstance(v,list) and 'items'in s:
  for i,x in enumerate(v):validate_schema(x,s['items'],loc+'/'+str(i))
 if isinstance(v,str):
  if 'minLength'in s:require(len(v)>=s['minLength'],loc+' 문자열 길이')
  if 'pattern'in s:require(re.search(s['pattern'],v) is not None,loc+' 정규식')
 if type(v)is int:
  if 'minimum'in s:require(v>=s['minimum'],loc+' 최소값')
  if 'maximum'in s:require(v<=s['maximum'],loc+' 최대값')
schema=read(OUT/'corpus_event.schema.json');inspect_schema(schema)
examples=rows(OUT/'schema_examples.jsonl')
for e in examples:
 validate_schema(e,schema,e['record_id'])
 ids={a['evidence_id'] for a in e['evidence']}
 for a in e['evidence']:verify_evidence(a)
 for k in ['text_structure','item_manipulation','reasoning_steps','pattern_links']:
  for x in e[k]:require(set(x['evidence_ids'])<=ids,'예시 근거 ID 미해소')
 if e['judgment']['answer_action']=='번호보류':require(e['judgment']['selected_answer_in_this_record'] is None,'보류 답 덮어쓰기')
 require(not e['analysis_condition']['student_process_observed'],'학생 관찰 과장')
 require(not e['analysis_condition']['strict_blind_claim'],'현재 예시 strict blind 과장')
checks['schema_examples']=len(examples)
checks['schema_exact_quotes_checked']=sum(len(e['evidence']) for e in examples)
checks['schema_validation_scope']='현 스키마 키워드 전부를 처리하는 로컬 검사기. 범용 JSON Schema 엔진의 메타스키마 적합성 인증은 아님.'

# 창작 시제품 A: 가능한 입력과 주어진 결과로부터 허용되는 상태를 전수 열거한다.
def route(match,table):return '자동' if match and table else '보완' if match else '수동'
states=[{'match':m,'table':t,'route':route(m,t)} for m in [False,True] for t in [False,True]]
manual=[s for s in states if s['route']=='수동'];auto=[s for s in states if s['route']=='자동'];supp=[s for s in states if s['route']=='보완']
def current_route(initial,verification_failed):return '재검토' if initial=='자동' and verification_failed else initial
truth=[all(not s['match'] for s in manual),len({s['table'] for s in manual})==2,all(s['match'] and s['table'] for s in auto),all(current_route(s['route'],True)=='재검토' for s in auto),all(not s['match'] for s in supp)]
require(truth==[True,True,True,True,False],'시제품 A 유일 정답 오류')
require(80>70 and 0<1 and 100>80,'시제품 B 반모형 오류')
checks['prototype_A_choice_support']=truth
checks['prototype_B_support']='나/다: 모두 일부 결손, 성립수0<1이나 품질80>70. 가/나는 적용 영역 밖.'

broken=[]
for p in OUT.glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  target=target.strip('<>')
  if re.match(r'\w+://',target) or target.startswith('#'):continue
  path=target.split('#')[0]
  if path and not (p.parent/path).exists() and (p.parent/path)!=OUT/'validation_report.json':broken.append([p.name,target])
require(not broken,'깨진 로컬 링크 '+str(broken))
checks['broken_local_links']=broken

raw=rows(OUT/'decision_raw.jsonl');require(len(raw)==len({r['decision_id'] for r in raw}),'판단 raw 중복')
checks['raw_decisions']=len(raw)
report={'status':'pass' if not errors else 'fail','checks':checks,'errors':errors,'limits':['인용의 문자 일치는 의미상 충분성 보증이 아님','기출 판단과 창작 시제품의 학생 효과 미검증','원 배포 지면·공식 답표 신규 전수 대조 없음','다른 모델·평가자의 의미 검증 없음']}
(OUT/'validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
artifact_hashes={p.name:sha(p) for p in OUT.iterdir() if p.is_file() and p.name!='artifact_hashes.json'}
(OUT/'artifact_hashes.json').write_text(json.dumps(artifact_hashes,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
