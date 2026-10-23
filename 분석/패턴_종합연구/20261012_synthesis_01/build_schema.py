"""전체 코퍼스 후속 작업에 사용할 잠정 스키마와 현재 표본의 예시만 만든다."""
from pathlib import Path
import json, hashlib
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]

def obj(properties,required=None):
    return {'type':'object','properties':properties,'required':required or list(properties),'additionalProperties':False}
def arr(items):return {'type':'array','items':items}
def enum(values):return {'type':'string','enum':values}
S={'type':'string','minLength':1}; B={'type':'boolean'}; SS=arr(S)
nullable_string={'type':['string','null']}
evidence=obj({'evidence_id':S,'source_path':S,'source_sha256':{'type':'string','pattern':'^[0-9a-f]{64}$'},'json_pointer':S,'char_start':{'type':'integer','minimum':0},'char_end_exclusive':{'type':'integer','minimum':0},'exact_quote':S,'verification_level':enum(['문자좌표재검사','기존검수승계','원지면직접확인'])})
history=obj({'stage':S,'fact':S,'source_path':S,'locator':S,'inherits_to_current':B})
step=obj({'step_id':S,'input':SS,'operation':S,'edge_semantics':enum(['정의대입','귀속복원','정의의존','조건결합','역상','시점배치','비교','비율','논증역할','문맥치환','범위검사','근거탐색']),'output':S,'evidence_ids':SS})
pattern=obj({'pattern_id':S,'relation':enum(['구조존재','문항활용','풀이유용','설명만','경계','미확인','미분류']),'subtype_id':nullable_string,'basis':S,'evidence_ids':SS,'necessary_for_all_routes':enum(['예','아니오','미확인'])})
schema={
 '$schema':'https://json-schema.org/draft/2020-12/schema',
 '$id':'urn:korean-pattern-synthesis:analysis-event:0.3-draft',
 'title':'기출 판단 장면 잠정 스키마 v0.3-draft',
 **obj({
 'schema_version':{'const':'0.3-draft'},'record_id':S,
 'source_identity':obj({'case_id':S,'passage_group':S,'passage_id':S,'identity_family':S,'question_id':S,'exam_family':enum(['KICE','LEET','MEET','미확인']),'sample_split':enum(['discovery','validation','future_corpus']),'choice_ids':arr({'type':'integer','minimum':1,'maximum':5})}),
 'analysis_condition':obj({'phase':enum(['기존개별연구','Sol독립1단계','코드북외부적용','작업C종합','후속검증']),'codebook_seen_before_judgment':B,'prior_solutions_seen_before_judgment':B,'strict_blind_claim':B,'historical_exposure':enum(['확인노출','이력미확인','해당세션미열람만확인']),'history':arr(history),'reasoning_is_reconstructed':B,'student_process_observed':B}),
 'source_state':obj({'completeness':enum(['판단에충분','일부결손','원문결손으로번호불가','시각전사만','보강자료사용']),'supplements':SS,'source_limit':S}),
 'text_structure':arr(obj({'structure_id':S,'kind':S,'scope':S,'claim':S,'evidence_ids':SS,'actually_used_here':B})),
 'item_manipulation':arr(obj({'operation_id':S,'target':S,'kept':S,'changed_or_required':S,'evidence_ids':SS})),
 'reasoning_steps':arr(step),
 'judgment':obj({'content_status':enum(['지지','반박','근거부족','논리적미확정','자료결손','내용자체미판정']),'task_role_status':enum(['적합','부적합','판단보류','해당없음']),'stem_polarity':enum(['긍정선택','부정선택','짝짓기','기타']),'answer_action':enum(['선택','비선택','번호보류','해당선지판정만']),'selected_answer_in_this_record':{'type':['integer','null'],'minimum':1,'maximum':5},'official_answer_reused':{'type':['integer','null'],'minimum':1,'maximum':5},'answer_reference':nullable_string,'rationale':S}),
 'pattern_links':arr(pattern),'evidence':arr(evidence),
 'boundary':obj({'applicable_if':SS,'do_not_apply_if':SS,'counterexample_kind':enum(['없음','실제경계','강한기출반례','창작반모형']),'counterexample':nullable_string,'alternative_valid_route':nullable_string}),
 'uncertainty':arr(obj({'kind':enum(['원문결손','논리적미확정','반복미검증','노출제한','원지면미대조','의미판정유보','학생효과미관찰']),'note':S})),
 'teaching_and_design':obj({'repeatable_action':S,'design_constraint':S,'student_effect_verified':B}),
 'lineage':obj({'original_candidate_ids':SS,'prior_record_refs':SS,'supersedes':SS,'revision_reason':nullable_string,'created_in_run':S})
 })}
(OUT/'corpus_event.schema.json').write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n')

registry={d['case_id']:d for d in [json.loads(l) for l in (OUT/'case_registry.jsonl').read_text().splitlines()]}
examples=[]
def make(case,choice,content,role,action,selected,pattern,operation,edge,conclusion,quote,limit,counter=None):
 r=registry[case];p=ROOT/r['source']['path'];d=json.loads(p.read_text());i=d['passage_text'].find(quote);assert i>=0,(case,quote)
 ev={'evidence_id':f'EX-{case}-{choice}','source_path':r['source']['path'],'source_sha256':r['source']['sha256'],'json_pointer':'/passage_text','char_start':i,'char_end_exclusive':i+len(quote),'exact_quote':quote,'verification_level':'문자좌표재검사'}
 a=r['official_answer_history_reused'][-1];h=[]
 if case in ['NL','NM','NN','NK','NO']:
  h=[{'stage':'pilot 이후','fact':'G095의 NM 정답·코드 요약 노출 이력. 다섯 문항의 엄격 미노출 실적 제외.','source_path':'분석/패턴_종합연구/20261009_pilot_01/pilot_review.md','locator':'출처·검증 제한 및 우발 노출','inherits_to_current':True}]
 x={'schema_version':'0.3-draft','record_id':f'C-EX-{case}-{choice}',
 'source_identity':{'case_id':case,'passage_group':r['passage_group'],'passage_id':r['passage_id'],'identity_family':r['identity_family'],'question_id':r['question_id_from_manifest'],'exam_family':r['exam_family'],'sample_split':r['sample_split'],'choice_ids':[choice]},
 'analysis_condition':{'phase':'작업C종합','codebook_seen_before_judgment':True,'prior_solutions_seen_before_judgment':True,'strict_blind_claim':False,'historical_exposure':'확인노출' if h else '이력미확인','history':h,'reasoning_is_reconstructed':True,'student_process_observed':False},
 'source_state':{'completeness':'판단에충분','supplements':[],'source_limit':limit},
 'text_structure':[{'structure_id':'T-local','kind':'본문 관계','scope':'해당 선지에 실제 쓰인 부분','claim':quote,'evidence_ids':[ev['evidence_id']],'actually_used_here':True}],
 'item_manipulation':[{'operation_id':'M-local','target':f'{choice}번 선지','kept':'본문의 핵심 용어·대상','changed_or_required':operation,'evidence_ids':[ev['evidence_id']]}],
 'reasoning_steps':[{'step_id':'A1','input':[quote],'operation':operation,'edge_semantics':edge,'output':conclusion,'evidence_ids':[ev['evidence_id']]}],
 'judgment':{'content_status':content,'task_role_status':role,'stem_polarity':'부정선택' if case in ['JN','YT','ATN','AYG'] else '긍정선택','answer_action':action,'selected_answer_in_this_record':selected,'official_answer_reused':a['payload'].get('official_answer'),'answer_reference':f"{a['path']}#record_id={a['record_id']};line={a['line_1_based']}",'rationale':conclusion},
 'pattern_links':[{'pattern_id':pattern,'relation':'풀이유용','subtype_id':None,'basis':operation,'evidence_ids':[ev['evidence_id']],'necessary_for_all_routes':'아니오'}],
 'evidence':[ev],
 'boundary':{'applicable_if':['해당 본문 관계와 선지 범위가 확인됨'],'do_not_apply_if':[limit],'counterexample_kind':'창작반모형' if counter else '실제경계','counterexample':counter,'alternative_valid_route':'관련 선지 전체를 검토하지 않고 정답 선지의 결정 근거를 직접 회수할 수도 있음'},
 'uncertainty':[{'kind':'학생효과미관찰','note':'논리 경로의 재구성이며 실제 학생 행동 관찰이 아님'}],
 'teaching_and_design':{'repeatable_action':operation,'design_constraint':limit,'student_effect_verified':False},
 'lineage':{'original_candidate_ids':[pattern],'prior_record_refs':[f"{v['path']}#line={v['line_1_based']}" for v in r['external_application']+r['sol_stage1']],'supersedes':[],'revision_reason':None,'created_in_run':'20261012_synthesis_01'}}
 examples.append(x);return x

make('JN',4,'반박','부적합','선택',4,'N09','단안으로 가능한 경로에 양안 필수를 추가했는지 검사','범위검사','단안 단서인 직선 원근은 두 눈의 조합을 필요로 하지 않으므로 ④를 선택한다.','사람은 단안 단서만으로도 이전의 경험으로부터 추론에 의하여 세계를 3차원으로 인식할 수 있다.','양안이 도움이 될 가능성까지 부정하지 않는다.')
make('YT',1,'지지','적합','비선택',None,'N07','무반응의 가능한 두 입력 행에서 공통 위협 값만 확정','역상','집단1의 위협은 낮음이 확정되나 효능감은 미확정이다. ①은 부적절한 선지가 아니다.','효능감의 수준에 관계없이 공포 소구에 대한 반응이 없게 된다.','모형의 전수성과 관측 부합이 없으면 동일 역추론을 하지 않는다.')
make('AYF',3,'논리적미확정','부적합','비선택',None,'P03','A>C와 B>C가 허가하는 부분 순서만 남김','비교','A/B 비용 순서가 없으므로 감소 가능성의 판별 사례로 사용하기 부족하다.','생산비용이 낮은 국가에서 생산비용이 높은 국가로 바꾸는 것이므로 효율이 감소한다.','미확정이 A=B 또는 A<B를 확정한다는 뜻은 아니다.','A=12,B=10,C=5와 A=10,B=12,C=5는 동일 전제를 만족하며 A→B의 부호가 반대다.')
make('AYG',2,'내용자체미판정','부적합','선택',2,'N04','비교하는 상태가 목표 주장 적용 영역에 들어가는지 확인','논증역할','완전 최적/비최적 차이 자체를 거짓이라고 할 필요 없이 차선 상태 간 비단조성의 증거 역할을 부정한다.','하나 이상의 효율성 조건이 이미 파괴되어 있는 상태에서는','표의 조건 수를 효율 점수로 환산하지 않는다.')
make('ATN',3,'근거부족','부적합','선택',3,'N10','찬성 사실과 추가된 면제 기대라는 동기를 나누어 근거 검사','근거탐색','한 필 감축과 편의 찬성으로 무부담 기대 및 그것이 찬성 이유라는 연결을 보장하지 못한다.','호전이 편하다고 하는 자가 많았다.','총량 부재에서 실제 잔여가 반드시 양수라는 반대 단정도 하지 않는다.')

# 같은 case의 다른 단계는 덮어쓰지 않고 서로 다른 예시 record로 저장한다.
rx=make('RX',4,'자료결손','판단보류','번호보류',None,'N05','분모를 고정해 A/B 의미를 정하고 번호 정보의 결손을 따로 남김','비율','A=위음성, B=진음성이지만 원 입력에 B열이 없어 ④/⑤를 구별할 수 없다.','민감도는 시료에 목표 성분이 존재하는 경우에 대해 키트가 이를 양성으로 판정한 비율이다.','다른 집단의 오류 절대 건수를 비교하지 않는다.')
rx['record_id']='C-EX-RX-stage1-history';rx['analysis_condition'].update(phase='Sol독립1단계',codebook_seen_before_judgment=False,prior_solutions_seen_before_judgment=False,historical_exposure='해당세션미열람만확인')
rx['analysis_condition']['history']=[{'stage':'9월 기존 개별연구','fact':'보조 작업자 답필드 우발 노출 기록이 있으나 주 Astra에게 값 미전달이라고 기록. Sol 해당 세션 미열람 주장과 별도.','source_path':'data/기본기_연구/astra_handoff_queue.jsonl','locator':'RX-blind-20260919-01;1978행','inherits_to_current':True}]
rx['source_state'].update(completeness='원문결손으로번호불가',source_limit='Sol snapshot의 B열 누락. 보강 자산의 과거 존재와 해당 단계의 미사용을 구별.')
rx['judgment'].update(stem_polarity='짝짓기',official_answer_reused=None,answer_reference=None)
rx['uncertainty'].append({'kind':'원문결손','note':'B열 누락은 논리적 미확정이 아님'})
rx['lineage']['revision_reason']='작업 C가 과거 상태를 보존하는 예시; Sol 원기록 수정 아님'
p=ROOT/'분석/패턴_종합연구/20261010_sol_independent_stage1_01/sources/RX.json';d=json.loads(p.read_text());q=rx['evidence'][0]['exact_quote'];i=d['passage_text'].find(q)
rx['evidence'][0].update(source_path=str(p.relative_to(ROOT)),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),char_start=i,char_end_exclusive=i+len(q))
rx2=json.loads(json.dumps(rx,ensure_ascii=False));rx2['record_id']='C-EX-RX-external-history';rx2['analysis_condition'].update(phase='코드북외부적용',codebook_seen_before_judgment=True,historical_exposure='이력미확인')
rx2['source_state'].update(completeness='보강자료사용',supplements=['data/기본기_연구/prepared_backlog/blind_sources/RX_choice_table.md'],source_limit='외부 적용은 보강표 사용. 표 원본 스캔 독립 재검수는 하지 않았다고 보고.')
rx2['judgment'].update(content_status='지지',task_role_status='적합',answer_action='선택',selected_answer_in_this_record=4,rationale='같은 분모에서 A=위음성/B=진음성. 보강표 ④와 연결. 해당 외부 적용 단계의 공식답 미대조 상태를 유지.')
rx2['reasoning_steps'][0]['output']='분모를 고정한 A/B 의미와 보강표 ④를 연결한다.'
rx2['uncertainty']=[{'kind':'원지면미대조','note':'외부 적용의 보강표 원스캔 미재검수 한계 승계'},{'kind':'학생효과미관찰','note':'실제 학생 관찰 없음'}]
rx2['lineage']['revision_reason']='후속 입력 사용 차이 보존; stage1 번호 null을 소급 변경하지 않음'
examples.append(rx2)
for x in examples:
 case=x['source_identity']['case_id']
 source=ROOT/registry[case]['source']['path']
 if x['record_id']=='C-EX-RX-stage1-history':source=ROOT/'분석/패턴_종합연구/20261010_sol_independent_stage1_01/sources/RX.json'
 d=json.loads(source.read_text());sha=hashlib.sha256(source.read_bytes()).hexdigest()
 if x['record_id']=='C-EX-RX-external-history':
  x['evidence'][0].update(source_path=str(source.relative_to(ROOT)),source_sha256=sha)
 more={
  'JN':['또 다른 단안 단서로는 ‘직선 원근’이 있다.'],
  'AYF':['관세동맹이 세계 경제의 효율성을 떨어뜨릴 수 있음을 지적하였다.'],
  'ATN':['과인이 이미 군포 한 필을 감하겠노라고 말을 하였으니'],
  'RX':['특이도는 시료에 목표 성분이 없는 경우에 대해 키트가 이를 음성으로 판정한 비율이다.','이 경우 실제로 목표 성분이 없다면 진음성, 목표 성분이 있다면 위음성이라고 한다.']
 }
 for j,q in enumerate(more.get(case,[]),1):
  i=d['passage_text'].index(q);eid=x['record_id']+'-premise-'+str(j)
  x['evidence'].append({'evidence_id':eid,'source_path':str(source.relative_to(ROOT)),'source_sha256':sha,'json_pointer':'/passage_text','char_start':i,'char_end_exclusive':i+len(q),'exact_quote':q,'verification_level':'문자좌표재검사'})
  x['reasoning_steps'][0]['evidence_ids'].append(eid)
 for ptr,txt in [('/stem',d['stem'])]+[(f'/choices/{c-1}',d['choices'][c-1]) for c in x['source_identity']['choice_ids']]:
  eid=x['record_id']+'-'+ptr.replace('/','-')
  x['evidence'].append({'evidence_id':eid,'source_path':str(source.relative_to(ROOT)),'source_sha256':sha,'json_pointer':ptr,'char_start':0,'char_end_exclusive':len(txt),'exact_quote':txt,'verification_level':'문자좌표재검사'})
  x['item_manipulation'][0]['evidence_ids'].append(eid)
  x['reasoning_steps'][0]['evidence_ids'].append(eid)
 if case=='AYG':
  p=ROOT/'data/기본기_연구/prepared_backlog/blind_sources/G350_visual02.md';txt=p.read_text();q='X ⇔ Y X ⇔ L Y ⇔ L | X ⇎ Y X ⇎ L Y ⇔ L | X ⇔ Y X ⇎ L Y ⇎ L | X ⇎ Y X ⇎ L Y ⇎ L';i=txt.index(q);eid='EX-AYG-table'
  x['evidence'].append({'evidence_id':eid,'source_path':str(p.relative_to(ROOT)),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'json_pointer':'/text','char_start':i,'char_end_exclusive':i+len(q),'exact_quote':q,'verification_level':'문자좌표재검사'})
  x['reasoning_steps'][0]['evidence_ids'].append(eid)
  x['source_state'].update(completeness='보강자료사용',supplements=[str(p.relative_to(ROOT))],source_limit='기존 외부 적용의 공식 이미지 검수와 표 전사를 승계. 작업 C 신규 원지면 대조 아님.')
 if x['record_id']=='C-EX-RX-external-history':
  p=ROOT/'data/기본기_연구/prepared_backlog/blind_sources/RX_choice_table.md';txt=p.read_text();q='| ④ | 위음성 | 진음성 |';i=txt.index(q);eid='EX-RX-supplement-4'
  x['evidence'].append({'evidence_id':eid,'source_path':str(p.relative_to(ROOT)),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'json_pointer':'/text','char_start':i,'char_end_exclusive':i+len(q),'exact_quote':q,'verification_level':'문자좌표재검사'})
  x['reasoning_steps'][0]['evidence_ids'].append(eid)
(OUT/'schema_examples.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in examples))
print('스키마와 예시',len(examples),'건 저장')
