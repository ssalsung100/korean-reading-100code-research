"""신규 v1 파생 산출물만 작성. 원본·동결·기존 원장에는 쓰지 않는다."""
from pathlib import Path
import csv, json, copy, hashlib, collections

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
BASE = ROOT / '분석/패턴_종합연구'
SRC = BASE / '20261016_integrated_research_01'
SWEEP = BASE / '20261012_corpus_sweep_01'
BACK = BASE / '20261012_question_backfill_01'

def rows(p):
    return [json.loads(s) for s in p.read_text().splitlines() if s.strip()]
def write_json(name, obj):
    (OUT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
def write_rows(name, data):
    (OUT/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data))
def rel(p):
    return str(p.relative_to(ROOT))
def mdlink(path, label=None):
    import os
    return f'[{label or Path(path).name}](<{os.path.relpath(ROOT/path,OUT)}>)'
def tableval(x):
    return str(x).replace('|','／').replace('\n',' ')

principles = rows(SRC/'principles_current.jsonl')
candidates = rows(SRC/'기존후보_통합상태표.jsonl')
decisions = rows(SRC/'integration_decisions.jsonl')
effects = rows(SRC/'production_effects.jsonl')
registry = rows(SRC/'source_registry.jsonl')
reg_case = {r['case_id']:r for r in registry}
manifest = {r['unique_question']:r for r in rows(SWEEP/'manifest_questions.jsonl')}
evidence = {r['event_id']:r for r in rows(SWEEP/'evidence_links.jsonl')}
reviews = {r['unique_question']:r for r in rows(BACK/'current_question_reviews.jsonl')}
scope = json.loads((SRC/'v1_입력범위.json').read_text())
manual = list(csv.DictReader((OUT/'연산명세_편집입력.tsv').open(),delimiter='\t'))
checks = list(csv.DictReader((OUT/'대표대조_편집입력.tsv').open(),delimiter='\t'))
assert len(manual)==63 and len({x['번호'] for x in manual})==63

# 탐색 장면은 수정 원장을 순서대로 적용한 파생 뷰를 만든다.
# 보완 장면은 이미 applied_amendment_ids를 갖춘 현행 파일이므로 재적용하지 않는다.
scenes=[]
scene_files=sorted(SWEEP.glob('batch_*_scenes.jsonl'))+[BACK/'new_judgment_scenes.jsonl']
for f in scene_files:
    for line,r in enumerate(rows(f),1):
        r=copy.deepcopy(r);r['_source_record']={'path':rel(f),'line':line,'record_id':r['event_id']};scenes.append(r)
scene_by={r['event_id']:r for r in scenes}
assert len(scenes)==len(scene_by)==2202
for line,a in enumerate(rows(SWEEP/'scene_amendments.jsonl'),1):
    r=scene_by[a['event_id']];r.update(a['changes'])
    r.setdefault('_sweep_amendments',[]).append({'path':rel(SWEEP/'scene_amendments.jsonl'),'line':line,'reason':a['reason']})
candidate_by={r['candidate_id']:r for r in candidates}
prior_compared={e for r in registry for e in r.get('compared_event_ids',[])}
prior_meta={e for r in registry for e in r.get('metadata_reviewed_event_ids',[])}
reg_event={e:r for r in registry for e in r.get('compared_event_ids',[])+r.get('metadata_reviewed_event_ids',[])}

def source_for(s):
    q=s['unique_question'];e=s['event_id'];rv=reviews.get(q);ev=evidence.get(e);rg=reg_event.get(e)
    p=rv.get('source_path') if rv else ev.get('source_path') if ev else None
    case_ids=rv.get('case_ids',[]) if rv else [s.get('case_id')] if s.get('case_id') else []
    if rg:
        p=rg.get('primary_source_read_path') or rg.get('source_path') or p
    return {'case_ids':case_ids,'unique_question':q,'unique_group':s['unique_group'],'exam_family':s['exam_family'],
        'stored_question_ids':manifest.get(q,{}).get('stored_question_ids',[]),
        'source_path':p,
        'analysis_ref':{'path':rel(BACK/'current_question_reviews.jsonl'),'record_id':rv['record_id']} if rv else {'path':rel(SWEEP/'evidence_links.jsonl'),'event_id':e},
        'source_evidence_status':rv.get('source_status') if rv else ev.get('source_verification') if ev else '기존 색인 참조',
        'anchors':s.get('passage_evidence',[]) if rv else [ev.get('source_anchor')] if ev else [],
        'unresolved_in_prior_review':rv.get('unresolved',[]) if rv else rg.get('source_unresolved',[]) if rg else []}

direct=[]
for n,c in enumerate(checks,1):
    r=scene_by[c['장면']];rg=reg_case[c['사례']]
    direct.append({'review_id':f'V1-R{n:03d}','event_id':c['장면'],'case_id':c['사례'],
        'principle_ids':c['원리'].split(','),'role':c['역할'],
        'intermediate_inference':c['이번검토의중간추론'],'source_location':c['근거위치'],
        'remaining_limit':c['남는제한'],'source_path':rg.get('primary_source_read_path') or rg['source_path'],
        'prior_analysis_ref':source_for(r)['analysis_ref'],
        'epistemic_layer':'이번 v1의 대표·경계 사후 직접 대조','new_blind':False,
        'all_options_newly_solved':False,'original_pdf_reverified':False,
        'source_of_claim':'기출 로컬 정본/전사와 기존 추론을 읽은 주 에이전트의 제한된 대조',
        'researcher_feedback_received':False})
write_rows('대표대조_검토기록.jsonl',direct)
direct_by={r['event_id']:r for r in direct}

def links_for(e):
    out=[]
    for p in principles:
        for field,role in [('evidence_event_ids','적용'),('contrast_event_ids','대조'),('boundary_evidence_event_ids','경계')]:
            if e in p.get(field,[]):
                out.append({'principle_id':p['principle_id'],'verification':'I1','role':role,
                    'basis':{'path':rel(SRC/'principles_current.jsonl'),'record_id':p['principle_id'],'field':field},
                    'note':'기존 작성자의 장면ID별 의미 연결 승계. 이번 원문 직접 대조와 구별'})
    for d in decisions:
        for pid,eids in d.get('principle_evidence_mapping',{}).items():
            if e in eids and not any(x['principle_id']==pid for x in out):
                out.append({'principle_id':pid,'verification':'I1','role':'적용','basis':{'path':rel(SRC/'integration_decisions.jsonl'),'record_id':d['decision_id']},'note':'원 결정의 원리별 개별 장면 매핑만 승계; 결정 내 모든 원리×장면 교차연결 금지'})
    if e in direct_by:
        d=direct_by[e]
        for pid in d['principle_ids']:
            out=[x for x in out if x['principle_id']!=pid]
            out.append({'principle_id':pid,'verification':'V2','role':d['role'],
                'basis':{'path':rel(OUT/'대표대조_검토기록.jsonl'),'record_id':d['review_id']},
                'note':d['intermediate_inference'],'limit':d['remaining_limit']})
    return out

linked=[]
for s in scenes:
    e=s['event_id']
    patterns=[s['pattern']] if 'pattern' in s else [x['pattern_id'] for x in s.get('pattern_connections',[])]
    routes=[];links=links_for(e)
    for cid in patterns:
        c=candidate_by.get(cid)
        routes.append({'candidate_id':cid,'classification':c['classification'] if c else None,
            'route_principle_ids':c['ir_ids'] if c else [],'verification':'M0',
            'basis':{'path':rel(SRC/'기존후보_통합상태표.jsonl'),'record_id':c['record_id']} if c else None,
            'meaning':'후보명 경유 탐색 연결. C는 별도 잠정 유지, D는 부분 중첩/유보. 이 장면의 모든 연산을 해당 IR로 승인하지 않음'})
        if c:
            for pid in c['ir_ids']:
                if not any(x['principle_id']==pid for x in links):
                    links.append({'principle_id':pid,'verification':'M0','role':'후보 경유 가능 연결' if c['classification'] in ['A','B'] else '중첩 검토 경로',
                        'basis':{'candidate_id':cid,'record_id':c['record_id']},'note':'의미 검증 미실시; 원 후보 전체와 원리의 동치 아님'})
    levels={x['verification'] for x in links}
    status='V2 포함' if 'V2' in levels else 'I1 포함' if 'I1' in levels else 'M0만' if links else 'IR 미연결·후보 보존' if patterns else '미분류'
    linked.append({'event_id':e,'source_record':s['_source_record'],'source':source_for(s),
        'effective_amendments':s.get('_sweep_amendments',s.get('applied_amendment_ids',[])),
        'original_candidate_ids_effective':patterns,'candidate_routes':routes,'principle_links':links,
        'mapping_status':status,'prior_integrated_direct_comparison':e in prior_compared,
        'research_meta_or_mixed':e in prior_meta,
        'inference_ref':{'path':s['_source_record']['path'],'event_id':e,'field':'C' if 'C' in s else 'intermediate_inference_steps'},
        'current_v1_review_id':direct_by[e]['review_id'] if e in direct_by else None,
        'unclassified_reason':None if links else '현행 IR의 개별 장면 연결 및 후보 경유 IR 없음. 미연결이 기존 풀이 미완료를 뜻하지 않음',
        'not_a_new_blind_solution':True})
write_rows('판단장면_원리연결.jsonl',linked)
preserved_candidates=[]
for c in candidates:
    n=dict(c, v1_source_ref={'path':rel(SRC/'기존후보_통합상태표.jsonl'),'record_id':c['record_id']},v1_status_changed=False)
    if c['candidate_id']=='대립가능성':
        n['v1_reconciliation_note']='기존 판정 문구의 우선 직접 비교는 이력으로 보존한다. QZ/KK의 실제 비교는 IR-D094·사례76에서 완료했으며, 남은 것은③의 문언·존재 전제 유보다. 새 사례집을 우선 추가하라는 현행 지시로 읽지 않는다.'
    preserved_candidates.append(n)
write_rows('기존후보_보존연결.jsonl',preserved_candidates)
write_json('사용제외_적용목록.json',scope['excluded_applications'])

FAMILIES=[
('R1','표현·문장·서술의 역할','말이 나타내는 관계와 실제 서술 행동을 평가 과제에 맞춰 복원한다.'),
('R2','주체·견해·목적의 귀속','같은 말이나 결과를 다른 주체·설명 역할·의도에 옮기지 않는다.'),
('R3','기준·적용 범위·효과','규칙의 입력 영역과 요건을 고정하고 어느 효과까지 이어지는지 구별한다.'),
('R4','근거의 방향과 설명 강도','근거 간 의존, 비교 연결, 반박 표적을 확인하여 결론의 강도를 제한한다.'),
('R5','수량의 정의와 비교','단위·분모·시간·고정 조건을 갖춘 뒤 계산·경계·역산을 수행한다.'),
('R6','정보의 식별과 보존','주어진 입력·변환·출력에서 무엇이 구별되며 무엇이 남는지 확인한다.'),
('R7','경로·개입·복수 목표','전달 경로와 목표별 효과를 복원하여 개입·대체·검사 생략의 조건을 확인한다.')]

# 아래 관계는 범위를 명시한 v1 편집 판단. 그룹 소속만으로 동일 연산을 주장하지 않는다.
RELATIONS='''002|022|부분 중첩|평균의 경계와 평균에서 절대 구조 역산은 입력·출력이 다르다.|IR-D020
002|036|적용 전제 대조|단위가 맞아도 분모 비가산이면 평균식을 쓸 수 없다.|IR-D030
003|004|독립 연산·교육 대조|같은 목표의 남은 단서와 다른 기능의 신호를 나눈다.|IR-D003
003|046|독립 연산·교육 대조|별도 단서 대체와 동일 정보의 분산 잔존은 다르다.|IR-D040
005|016|선행 결합 가능|BEX는 정당화 의존을 복원한 뒤 정의에 분류한다. 모든 기준 적용이 순환 검사는 아니다.|IR-D004
006|016|교육 대조|사실 묘사와 내면성 공존은 분야 간 경계 점검이며 같은 분류법은 아니다.|IR-D016
006|039|부분 중첩|표현의 존재·대상을 확인하되 문학적 기능 귀속의 해석 강도는 따로 남긴다.|IR-D033
007|020|교육 대조|실제 목표와 관측, 조건부 작용과 전후 결과는 다른 비교 기준이다.|IR-D019
008|001|평가 과제 대조|질문의 전제 적합성과 대체어의 문맥 보존은 다른 출력이다.|IR-D024
009|010|독립 연산·상위 점검 공유|결합 실패의 책임 미식별과 완결 입력의 역상 교집합은 다르다.|IR-D009
010|030|부분 중첩|역상 공통 성분 복원과 산술 종속 변수의 효과 분리 한계를 구별한다.|IR-D026
010|063|부분 중첩|공통 성분을 얻는 역추론과 출력이 지운 차이를 증명하는 과제는 다르다.|IR-D096
011|012|선행 결합|이동 양끝 비교가 가능한지 확인한 뒤 그 이동의 증거 역할을 판정한다.|IR-D009
012|031|한정 하위 연산|예상과 관측의 차이가 추가 설명을 지지하는 경우. 모든 지지가 이 방식은 아니다.|IR-D026
013|012|선후 결합|조건 수와 성과를 읽은 뒤 그 비교가 주장을 시험하는지 판단한다.|IR-D013
014|015|독립 연산·교육 대조|규칙이 같은 출력을 지시함과 간접 경로의 존재는 다르다.|IR-D014
015|025|부분 중첩|경로 복원이 검사 간 함의 증명을 대신하지 않는다.|IR-D029
016|026|재분류 후보|새 전략을 규칙의 대상에 넣는 행동은 기준 적용 하위형일 수 있으나 P026을 삭제하지 않는다.|IR-D024
012|027|재분류 후보|절차의 상위 요약 지지는 증거 역할의 하위형 가능성이 있다.|IR-D024
037|027|재분류 후보|실제 수행 행위를 상위 서술로 요약하는 과제를 보존한다.|IR-D024
050|034|재분류 후보|입장별 필수 요건의 귀속은 P050의 하위형 가능성이 있으나 필요/불충분 차이는 남긴다.|IR-D028
017|018|독립 연산·교육 대조|가중 미소 변화합0과 축척 곱 보존은 같은 상쇄 연산이 아니다.|IR-D017
019|021|부분 중첩|미지 분자에 따른 방향 미정과 공통 계수의 소거 조건을 나눈다.|IR-D020
020|024|부분 중첩|전후 비교 기준은 공유하지만 곱의 동시 변화와 초기 수지 부호는 다르다.|IR-D021
021|032|대안 또는 선행 결합|LK에서 지수 배율 계산과 등급 비교는 각각 충분한 경로일 수 있다.|IR-D083
023|024|같은 지문·독립 연산|표본 외삽 편향과 유입/유출 수지는 다른 식을 쓴다.|IR-D021
024|048|부분 중첩|수지 합성은 공유하지만 기관별 경로 크기 미정은 별도 식별 공백이다.|IR-D043
025|003|교육 대조|검사가 논리적으로 함축됨과 남은 단서가 기여함은 증명 강도가 다르다.|IR-D023
028|029|같은 문항·독립 연산|소실 급부의 실현 제한과 실제 이행 급부의 반환 대응을 나눈다.|IR-D025
030|031|독립 연산·교육 대조|정확 효과량을 분리 못해도 방향의 증거가 전부 사라지는 것은 아니다.|IR-D026
032|033|선행 결합|역수축의 개선 방향을 해석한 뒤 보완 조합을 평가한다.|IR-D027
032|057|선후 결합|지표에서 현재 상태를 읽은 뒤 장치 법칙으로 수정 방향을 결정한다.|IR-D064
035|015|부분 중첩|우회 경로의 존재에 방법의 허용 요건 검사가 추가된다.|IR-D029
037|038|교육 대조|글의 실제 서술 행동과 선지가 수행한 감상 행동은 대상이 다르다.|IR-D032
039|052|경계 대조|행동 목적의 해석적 근거와 명시적 목적 부정을 같은 강도로 가르치지 않는다.|IR-D050
040|050|부분 중첩|태도 대상 전이와 견해 귀속의 미지원은 다른 입력을 가진다.|IR-D034
041|037|부분 중첩|인용/대안 역할과 글의 전개 행동은 공유 준비 행동만 있다.|IR-D035
042|003|교육 대조|역할 전체 대체와 한 목표의 잔여 단서 기여는 충분성 범위가 다르다.|IR-D036
043|044|같은 지문·독립 연산|유지/변경 설계 조건과 설치 목적의 우선성 판단을 분리한다.|IR-D037
045|063|적용 경계|가역 표현 변환은 정보 손실을 함의하지 않는다. 실제 조작을 확인한다.|IR-D096
046|063|교육 대조|남은 동일 정보의 복원과 출력에서 사라진 차이의 비식별을 대조한다.|IR-D096
049|002|교육 대조|상한은 가능값 전체 목록이 아니며 더 느슨한 상한을 반박하지 않는다.|IR-D045
050|054|선행 결합|각 견해의 근거를 회수한 뒤 공통 관계만 추출한다.|IR-D056
050|060|부분 중첩|현상의 발생을 인정하는 주체와 규범적으로 승인하는 주체를 분리한다.|IR-D081
051|058|독립 연산·교육 대조|경향의 예외와 전칭 집합 안의 명시 제외를 구별한다.|IR-D068
052|044|부분 중첩|결과와 목적, 기능 존재와 목적 우선성은 귀속 근거의 종류가 다르다.|IR-D050
053|050|부분 중첩|객관적 인상/구성 과정과 견해 귀속은 같은 주체 확인으로 끝나지 않는다.|IR-D053
001|056|평가 과제 대조|문장 치환과 낱말의 부분 의미 포함은 요구하는 보존 수준이 다르다.|IR-D061
059|062|독립 연산·교육 대조|성립/책임 구별과 예외의 효과별 범위는 다른 추론이다.|IR-D088
061|062|독립 연산·교육 대조|시점상 새로움과 여러 효과 중 예외의 표적을 혼동하지 않는다.|IR-D088
047|045|독립 연산·교육 대조|탐구 대상/이용 매개의 역할과 표현 변환/정보 조작의 단계는 다른 관계이다.|IR-D041
055|054|독립 연산·교육 대조|자연적 가능 영역과 현재 결핍의 적용은 두 설명의 공통 지향을 추출하는 과제와 다르다.|IR-D058'''
edges=[]
for i,line in enumerate(RELATIONS.splitlines(),1):
    a,b,kind,reason,did=line.split('|')
    edges.append({'relation_id':f'V1-REL{i:03d}','from':'IR-P'+a,'to':'IR-P'+b,'relation':kind,'rationale':reason,
        'evidence_decision_ids':[did],'epistemic_layer':'AI의 v1 조직 제안·기존 결정의 범위 한정 계승','final_merge':False})

by_pid={p['principle_id']:p for p in principles}
mapped_by_event={s['event_id']:s for s in linked}
nodes=[]
for m,p in zip(manual,principles):
    assert m['번호']==p['principle_id'][-3:]
    pid=p['principle_id'];n=copy.deepcopy(p)
    n.update({'organizer_id':m['조직군'],'required_inputs':m['필요입력'],'trigger':m['시작단서'],
        'decisive_intermediate_inference':m['결정적중간추론'],'result':m['판단결과'],'application_conditions':m['적용조건'],
        'non_application_and_boundaries':p['limits'],'verification_level':p['integration_status_v1'],
        'node_role':'상위 원리와 복수 하위 연산' if p.get('subtypes') else '독립 유지 중인 연산; 상태와 사용 범위는 별도',
        'v1_relation_ids':[e['relation_id'] for e in edges if pid in [e['from'],e['to']]],
        'legacy_candidate_ids':[c['candidate_id'] for c in candidates if pid in c['ir_ids']],
        'representative_sources':[dict(event_id=e,source=mapped_by_event[e]['source']) for e in p.get('evidence_event_ids',[]) if e in mapped_by_event],
        'current_v1_review_ids':[r['review_id'] for r in direct if pid in r['principle_ids']],
        'field_provenance':{'definition_limits_status':'기존 통합 원리 원문 승계','inputs_trigger_inference_result_conditions':'이번 AI의 조작적 명세; 학생 효과 미검증','source_information':'기존 출처 연결; V2 지정 부분만 이번 직접 열람','researcher_view':'새 내용 의견 수신 없음'},
        'source_ref':{'path':rel(SRC/'principles_current.jsonl'),'record_id':pid}})
    nodes.append(n)
graph={'schema_version':'1.0','date':'2026-10-18','principle_count':len(nodes),
    'organizers':[{'organizer_id':a,'name':b,'purpose':c,'status':'탐색용 상위 조직; 새로 검증한 독립 원리 수에 더하지 않음','members':[n['principle_id'] for n in nodes if n['organizer_id']==a]} for a,b,c in FAMILIES],
    'relation_types':'독립 유지/범위 한정 하위/선후 결합/부분 중첩/교육 대조/재분류 후보를 구별. 관계는 전체 동치가 아니며 방향 없는 대조의 from/to는 저장 편의.',
    'principles':nodes,'relations':edges,
    'legacy_candidates_ref':'기존후보_보존연결.jsonl','excluded_applications_ref':'사용제외_적용목록.json',
    'epistemic_layers':{'S':'기출 로컬 정본·전사 정보','A':'기존 풀이의 분석 결과','H':'AI의 귀납/설계 제안','R':'연구자 직접 견해: 수신 기록이 있는 경우에만','U':'미해결 유보','L':'출제 때 준수할 논리 조건'},
    'mapping_levels':{'M0':'기존 후보명 경유 기계 연결','I1':'기존 원리 원장의 장면ID별 의미 연결 승계','V2':'이번 지정 구간 원문·기존 중간 추론 직접 대조'}}
write_json('원리계층과관계.json',graph)

intro='''# 연구 원리 체계 v1

2026-10-18. 이 체계는 **지문에서 필요한 관계를 복원하고, 선지가 요구한 판단에 맞춰 중간 추론을 실행하는 도구**다. 100코드 번호나 소재 이름을 맞히는 체계가 아니다. 연구 원리63개를 유지하면서 입력·판단 단서·추론·출력·경계를 조작 가능한 형태로 묶었다. 잠정 안정화26·단독 잠정29·추가 비교5·재분류3이며, 모두 연구자의 내용 검토 및 학생 재현성 검증은 별도다.

## 사용하는 순서

1. 발문이 요구하는 결과를 정한다. 문맥 치환, 실제 발생, 관점 귀속, 정량 비교는 다른 과제다.
2. 주체·대상·시점·관점·출력 범위를 고정한다. 이 확인만으로 풀이가 끝난 것은 아니다.
3. 필요한 정보 관계를 회수한다. 평균에는 가산 분모, 배율에는 공통계수, 목적에는 선택 동기의 증거가 필요하다.
4. 아래 카드의 중간 추론을 실행한다. 조건이 빠졌으면 미지원과 반대 명제의 참을 구별한다.
5. 정답에 필요한 경로와 다른 선지 판단·대안 풀이·연구용 검산을 구분한다.

한 문항에는 여러 원리가 들어간다. AGT의 출력 정보 보존은④의 적절성 판단이며 정답①의 전부가 아니다. LK의 광도 배율과 절대등급 차는 같은 답에 이르는 대안 경로다. 학생에게 둘을 모두 필수로 수행시키지 않는다. 미지 어휘의 관습적 뜻이나 문학적 해석의 경계를 몇 개의 형식 연산으로 완전히 제거할 수 있다고 주장하지 않는다.

## 조직과 계층

상위 조직7개는 찾기 위한 묶음이며 검증된 새 원리7개가 아니다. 실제 상하위 관계는 입력·중간 추론을 보존하는 범위에서만 허용한다. P002는 평균의 두 방향, P024는 부분량/역산/개선과 절대증가, P063은 집계/선택 표상을 하위로 남긴다. 반면 가중합 상쇄 P017과 축척 보정 P018, 정당화 순환 P005와 상태 되먹임 후보는 합치지 않는다.

P026은 P016, P027은 P012/P037, P034는 P050의 하위형일 가능성을 관계로 표시했으나 기존ID를 폐기하지 않았다. 112개 이전 후보의 A12/B17/C58/D25는 원리63개와 다른 단위다. C58을 새 확정 원리58개로 합산하지 않는다. [후보 보존 연결](기존후보_보존연결.jsonl)에 정의·조건·근거·유보를 모두 남겼다.

## 핵심 경계

|비교|공유되는 준비 행동|끝까지 남겨야 할 차이|
|---|---|---|
|P003/P004/P046/P063|남은 정보 확인|같은 목표의 다른 단서 / 다른 기능의 신호 / 동일 정보의 분산 / 출력 구별 보존|
|P002/P022/P036|수량 관계 회수|평균 경계 / 구조 역산 / 단위 검사. 어느 것도 나머지의 충분조건 아님|
|P020/P021/P024|고정 조건과 비교 기준|실제 전후 결과 / 계수 소거 배율 / 초기 수지와 순변화|
|P005/되먹임고리/직전상태갱신|연결 추적|근거 의존 / 인과 영향 / 시간별 입력 갱신|
|P016/P050|관점과 속성 대응|지정 기준 적용에는 필자의 수용 불필요; 견해 귀속에는 해당 주체의 근거 필요|
|P039/P052|행동과 목적 근거 회수|문학적 기능의 해석적 귀속과 본문의 적극적 목적 부정을 같은 강도로 만들지 않음|
|P059/P061/P062|사건과 규칙 정리|성립과 책임 / 사실과 발견의 시점 / 예외가 바꾸는 효과|

## 원리별 실행 카드

정의·한계·상태는 기존 통합 원장, 입력·단서·중간 추론·결과는 그 범위 안에서 작성한 이번 AI의 v1 명세다. 각 원리의 전체 대표 출처·하위형·관계는 [기계 판독본](원리계층과관계.json)에 있다. 아래 대표 링크는 신규 원문 전수 검증 표시가 아니다. 이번 직접 대조는 [검토기록](대표대조_검토기록.jsonl)의 지정 장면에만 해당한다.
'''
parts=[intro]
for fid,title,purpose in FAMILIES:
    parts.append(f'### {fid} {title}\n\n{purpose}\n')
    for n in nodes:
        if n['organizer_id']!=fid: continue
        parts.append(f"#### {n['principle_id']} {n['name']}\n\n**상태: {n['integration_status_v1']['status']}** · {n['node_role']}\n\n{n['definition']}\n\n")
        for label,field in [('필요 입력','required_inputs'),('시작 단서','trigger'),('결정적 중간 추론','decisive_intermediate_inference'),('판단 결과','result'),('적용 조건','application_conditions'),('비적용·경계','non_application_and_boundaries')]:
            parts.append(f'- {label}: {n[field]}\n')
        refs=n['representative_sources'][:2]
        parts.append('- 대표 근거: '+'; '.join(f"{x['event_id']} — {mdlink(x['source']['source_path'], '/'.join(x['source']['case_ids']) or x['source']['unique_question'])}" for x in refs)+'\n')
        es=[e for e in edges if n['principle_id'] in [e['from'],e['to']]]
        parts.append('- 관계: '+'; '.join(e['from']+' ↔ '+e['to']+' '+e['relation']+' — '+e['rationale'] for e in es[:3])+'\n')
        if n.get('subtypes'): parts.append('- 보존할 하위 연산: '+ '; '.join(x if isinstance(x,str) else x.get('operation',str(x)) for x in n['subtypes'])+'\n')
        parts.append('- 사용 수준: '+n['integration_status_v1']['production_use']+' 연구자 의견을 받았다고 간주하지 않는다.\n\n')
(OUT/'연구원리체계_v1.md').write_text(''.join(parts))

# 변형 효과 전건은 원장 판정을 읽어 아래 주효과를 지정했다.
# T 국소 정오, P 풀이/근거 경로, G 평가 목표, U 미확정/부분 보완,
# M 모형 정합성 파괴, K 판정 유지, B 새 경계 사례/적용 영역 변경.
EFFECT_MAIN='''
T P U G U T U U U T G T U T U P P T M P U P P T U T G M T U U T P U T G U G T T U G P G U T G U U T U U T G T U T G U U T K T G U U T G U T U T T U U T T U P P P U P U U T T U P T U U U T T P T K T M
T T U G G T U U T G T P M T U P K K U K U T T M P U U U K G B T B T T P M T K T K M K K T G T K T K U K T K T T T K T G B U U U U K T K U U U P U T K T M B K T T K B T B K B T B G B T U T P U U M K M
U U K P P U T K T G T T P T T U U M T T P T U T T T U U T T U M P P T K T T T K K P T K T K T T T U K U M M U T K T K U P T K B T T P T T U K T U T T U T T K T U T K G K P T M G T U P T U T K P T G B
'''.split()
assert len(EFFECT_MAIN)==300,len(EFFECT_MAIN)
# 정합적으로 새 그래프/답을 만드는 E198을 모형 훼손과 구별한다.
EFFECT_MAIN[197]='T'
normalized=[]
MAIN_NAME={'T':'국소 정오 변경','P':'풀이·근거 경로 변경; 정오 유지 범위 별도','G':'평가 대상 변경','U':'미확정·근거 부분 변경','M':'모형·문항 정합성 재설계 필요','K':'현재 판정 유지','B':'새 경계 또는 적용 조건 사례'}
effect_relations={
 2:'핵심 집단50%·주변 집단12%·두 집단의 양의 비중과 전체 분할을 유지한다. 나머지 집계값도 수정 값과 일치해야 한다.',
 3:'50%초과 집단의 실제 값과 비중을 주고 다른 집단과의 가중 평균을 계산한다. 정확한50% 경계 전후를 따로 확인한다.',
 5:'널리 유행함이 해당 문장의 상태·정도·주체를 보존하는지 대입한다. 기존 적절한③과의 중복을 검사한다.',
 6:'원문이 나타내는 상태 하락과 대체어의 논항·방향을 보존한다. 부적절한 선지가 하나 이상 남는지는 별도 검사한다.',
 7:'실제 변동을 보장하는 모든 문장이 제거되었는지 확인한다. 상수 함수 가능성과 원명제의 거짓을 구별한다.',
 8:'검사선·표준선의 역할, 정상 작동, 충분 농도와 경쟁 방식의 미발색 조건을 모두 명시한다.',
 9:'관측 결과를 모형에 대입할 자격과 허용 입력 조합의 완결성을 제공한다. 삭제 뒤에도 별도 부합 조건이 남는지 확인한다.',
10:'A→B 비교의 양끝과 같은 생산량/비용 기준을 고정한다. B의 더 큰 비용이라는 추가 정보가 다른 비교와 충돌하지 않아야 한다.',
11:'충분 입증을 묻는다면 가설의 범위·경쟁 설명·자료의 지지 강도가 그 결론을 감당해야 한다. 단순 비약화 자료로는 대체하지 않는다.',
12:'무관 명제라는 입력 범주와 이전 믿음의 값을 유지하라는 규칙을 함께 보존한다. 규칙 부재와 같은 출력은 별개다.'}
pure_path={2,16,17,20,22,23,79,89,96,112,116,125,136,172,195,204,205,213,221,233,234,242,261,267,286,292,297}
for i,(r,main) in enumerate(zip(effects,EFFECT_MAIN),1):
    assert r['effect_id']==f'IR-E{i:03d}'
    cls=r.get('effect_class',[])
    t=(r.get('whole_item_status') or '')+' '+(r.get('local_result') or '')+' '+(cls if isinstance(cls,str) else ' '.join(cls))
    multi='명시된 위험' if any(x in t for x in ['복수','둘 다','2개','두 개','①·④ 최소']) else '원장에 명시되지 않음·부재 미검증'
    impossible='모형/선지 재설계 필요; 불능·충돌의 범위는 원장 판정 참조' if main=='M' else '판단 근거 부족 또는 상실 위험' if main=='U' and any(x in t for x in ['부족','소실','없','미확정','미정','불가','비식별']) else '원장에 명시되지 않음·부재 미검증'
    normalized.append({'effect_id':r['effect_id'],'source_ref':{'path':rel(SRC/'production_effects.jsonl'),'record_id':r['effect_id']},
        'original':r,'v1_primary_effect':MAIN_NAME[main],
        'axes':{'선지정오변경':'국소 변경; 전 선지 정답과 구별' if main=='T' else '유지 범위 명시' if main=='K' else '정오 유지 여부는 원장 local_result·whole_item_status의 범위에 한정' if main=='P' else '조건부/미확정 또는 별도 과제',
            '풀이경로만변경':'국소 판정 유지 범위에서 해당. 전체 유일성은 원장 whole_item_status의 미검토/유지 구별을 따름' if main=='P' and i in pure_path else '경로 보완/변경은 있으나 정오 유지가 미확정이므로 경로만 변화로 확정하지 않음' if main=='P' else '단독 효과로 확정하지 않음',
            '발문평가대상변경':'해당' if main=='G' else '명시 주효과 아님',
            '판단불가능':impossible,'복수정답위험':multi},
        'answer_loss_risk':'명시' if any(x in t for x in ['정답 소실','정답소실','정답 없음','정답없음','모두 적절','모두적절','모두 부적절']) else '미판정',
        'required_information_relation':r.get('constraints') or effect_relations[i],
        'epistemic_layer':'기존 AI의 변형 분석을 이번에 읽어 5축으로 정규화. 전300건의 원문/수정 전선지 신규 직접 검증은 아님',
        'new_item_ready':False})
write_rows('출제변형효과_300건_분류.jsonl',normalized)

counts={'principles':len(nodes),'principle_states':dict(collections.Counter(n['integration_status_v1']['status'] for n in nodes)),
    'candidate_states':dict(collections.Counter(c['classification'] for c in candidates)),
    'scenes':len(linked),'unique_questions':len({s['source']['unique_question'] for s in linked}),
    'mapping_status':dict(collections.Counter(s['mapping_status'] for s in linked)),
    'link_levels':dict(collections.Counter(x['verification'] for s in linked for x in s['principle_links'])),
    'current_direct_scenes':len(direct),'current_direct_questions':len({scene_by[r['event_id']]['unique_question'] for r in direct}),
    'current_direct_groups':len({scene_by[r['event_id']]['unique_group'] for r in direct}),
    'prior_integrated_compared_scenes':len(prior_compared),'prior_meta_scenes':len(prior_meta),
    'effects':len(normalized),'effect_primary_counts':dict(collections.Counter(r['v1_primary_effect'] for r in normalized)),
    'relations':len(edges)}
write_json('v1_집계.json',counts)

# 주요 입력만 기록한다. 전체 원장·전체 PDF 재검증은 수행하지 않는다.
snapshot=[]
for name in ['1차통합_완료준비도.md','기존후보_통합상태_읽기표.md','기존후보_통합상태표.jsonl','잠정안정화_원리목록.md','핵심미해결쟁점_우선순위.md','v1구축_전제조건과잔여작업.md','재개기록_20261018_사례집78_v1전환.md','principles_current.jsonl','integration_decisions.jsonl','production_effects.jsonl','원리별_v1상태.jsonl','source_registry.jsonl','v1_입력범위.json']:
    f=SRC/name;b=f.read_bytes();snapshot.append({'path':rel(f),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
snapshot_object={'date':'2026-10-18','source_directory':rel(SRC),'selected_inputs':snapshot,'counts':counts,
    'scene_source_files':[{'path':rel(f),'records':len(rows(f))} for f in scene_files],
    'amendment_policy':'sweep 수정원장35행을 읽어 파생 뷰에 적용. backfill 현행1586장면의 applied_amendment_ids를 그대로 사용하여 중복 적용 안 함.',
    'preserved_reservations':'기존 원유보93건·G024/G370 hold·BCF 메타·시제품 미검증 상태 불변. 새 산출물은 기존 파일을 수정하지 않음.',
    'model_identity':'요청: GPT-6 Astra xhigh. 별도 모델 호출/전환 없음. 런타임 모델 정체성은 도구로 별도 확인하지 않음.'}
if not (OUT/'기준입력상태.json').exists():
    write_json('기준입력상태.json',snapshot_object)
else:
    saved=json.loads((OUT/'기준입력상태.json').read_text())
    assert saved['selected_inputs']==snapshot,'입력이 최초 v1 스냅샷에서 변경됨. 확인 없이 기준점을 덮어쓰지 않는다.'

# 대표·경계 색인은 직접 대조와 승계 목록을 분리한다.
case_index=[]
for r in registry:
    ss=[s for s in linked if r['case_id'] in s['source']['case_ids']]
    case_index.append({'case_id':r['case_id'],'unique_question':r['unique_question'],'exam_family':r['exam_family'],
        'stored_question_ids':manifest.get(r['unique_question'],{}).get('stored_question_ids',[]),
        'source_path':r.get('primary_source_read_path') or r['source_path'],
        'prior_casebooks':[rel(SRC/x) for x in r.get('casebooks',[])],
        'prior_compared_event_ids':r.get('compared_event_ids',[]),
        'current_review_ids':[x['review_id'] for x in direct if x['case_id']==r['case_id']],
        'source_limits':r.get('source_unresolved',[]),'new_official_answer_verification':False})
write_rows('기출사례_출처색인.jsonl',case_index)
idx=['# 대표·경계 사례 인덱스\n\n이번 직접 대조21장면과 기존 원리63개의 대표 연결을 분리한다. 전자는16문항·15지문군이며 기존 직접 비교191장면에 더하는 신규 표본이 아니다. 모든 사례ID의 공식 저장 식별자·로컬 원문·기존 사례집은 [기출사례 출처색인](기출사례_출처색인.jsonl)에 있다.\n\n## 이번 지정 구간 직접 대조\n\n|검토ID/사례|장면·원리·역할|회수한 중간 추론|한계|\n|---|---|---|---|\n']
for r in direct:
    idx.append('|'+f"{r['review_id']} / {mdlink(r['source_path'],r['case_id'])}"+'|'+r['event_id']+' / '+','.join(r['principle_ids'])+' / '+r['role']+'|'+tableval(r['intermediate_inference'])+'|'+tableval(r['remaining_limit'])+'|\n')
idx.append('\nAGT의 골격, BFV의 거리 계통수와 분기론 그림을 직접 판독했다. AXY는 기존 복원본, BEX·AYN·BHM은 별도 보기 전사를 함께 사용했다. 공식답은 기존 대조를 승계했다. 원문·그림·보기의 구체 위치는 [직접 검토 기록](대표대조_검토기록.jsonl)에 있다.\n\n## 기존 원리별 대표와 관계 경계\n\n아래 표의 존재만으로 이번 직접 검증을 주장하지 않는다. 대표를 연결한 원장 필드와 전 근거 목록은 [원리 관계 JSON](원리계층과관계.json)의 representative_sources에 있다.\n\n|원리|대표 장면과 사례|직접 검토 기록|경계/대조를 볼 위치|\n|---|---|---|---|\n')
for n in nodes:
    rr=n['representative_sources'][:2]
    rep='; '.join(x['event_id']+' '+mdlink(x['source']['source_path'],'/'.join(x['source']['case_ids'])) for x in rr)
    books=[n.get('casebook')]+n.get('additional_casebooks',[])
    idx.append('|'+n['principle_id']+' '+n['name']+'|'+rep+'|'+(', '.join(n['current_v1_review_ids']) or '이번 신규 대조 없음')+'|'+', '.join(mdlink(rel(SRC/b),b) for b in books if b)+'|\n')
idx.append('\n## 역할별 읽기\n\n정답 결정은 BFV③·LK③·NL④·GA④·NY④ 등에 연결된다. AGT④·BQE①⑤는 다른 선지 판단이다. LK의 등급 경로는 대안 풀이, BHM의 음수 수지 예와 BFV의 동일 거리 행렬은 사후 검산이다. ASN은 목적 해석의 강도 유보, AXY는 공통계수 조건의 경계다. 단지 같은 문항에 나온다는 이유로 모든 선지에 한 원리를 붙이지 않는다.\n')
(OUT/'대표경계사례_인덱스.md').write_text(''.join(idx))

proposals={
 'QBF01-U0438-Q01-S02':('IR-P024','생성·소비의 수지가 P024의 같은 연산인지 원문 부호·기간을 대조. 현행은 미분류 유지.'),
 'QBF01-U0419-Q02-S02':('정의방향 후보','전칭의 포함 방향과 정의의 필요/충분 방향을 같은 행동으로 볼 범위를 확인. 역방향을 추가하지 않음.'),
 'QBF01-U0423-Q01-S02':('IR-P063','다른 전체에서 같은 일부 선택이 가능함과 출력 비식별의 입력 영역을 대조. 동일 원리로 미리 확정하지 않음.'),
 'QBF01-U0430-Q03-S01':('IR-P009','모형/실제 불일치의 책임 분기와 결합 전제 실패의 비식별을 비교. 입력 구조 차이 보존.'),
 'QBF01-U0409-Q03-S01':('IR-P016','평가어 적용 영역과 MO 명제성 선행 조건을 비교하되 윤리 평가를 진리값과 같은 연산으로 강제하지 않음.'),
 'QBF01-U0446-Q03-S02':('IR-P049','정확값 없이 상한으로 배제하는 것과 가능한 값 목록의 해석을 분리하여 비교.')}
unmapped=[]
for r in linked:
    if r['mapping_status'] not in ['미분류','IR 미연결·후보 보존']:continue
    s=scene_by[r['event_id']];p=proposals.get(r['event_id'])
    unmapped.append({'event_id':r['event_id'],'mapping_status':r['mapping_status'],'source':r['source'],'source_record':r['source_record'],
        'title':s.get('title',s.get('D','')),'existing_inference':s.get('intermediate_inference_steps',s.get('C')),
        'preserved_candidate_ids':r['original_candidate_ids_effective'],
        'followup_hypothesis':{'compare_with':p[0],'action':p[1],'status':'AI의 후속 비교 제안·연결 승인 아님'} if p else None})
write_rows('미분류장면_후속목록.jsonl',unmapped)
u=['# 미분류와 후속 검토\n\n2,202개 장면 중195개는 기존 후보를 보존하되 현행 IR로 연결하지 않았고,20개는 현행 후보 연결도 없는 장면이다. 이215개는 [전체 후속 목록](미분류장면_후속목록.jsonl)에 ID·출처·기존 추론을 보존했다. 앞의1,847개 M0 장면도 의미적으로 검증된 연결은 아니므로 사용 전 해당 추론을 확인해야 한다.\n\n## 원리와 후보의 유보\n\nP006·022·039·048·049는 추가 비교, P026·027·034는 재분류 검토다. 단독 잠정29개를 삭제하거나 안정화로 승격하지 않았다. 후보 C58·D25는 서로 다른 처리 단위이며 원리의37개와 합산하지 않는다. 후보112개 모두의 원정의·조건·기출·판정은 [보존 연결](기존후보_보존연결.jsonl)에 있다.\n\n현재 v1은 P058을 일반 반례 규칙으로 넓히지 않으며 AKX의 충분성 적용을 제외한다. 따라서 이 확장 연구가 끝나기 전에도 좁은 체계를 사용할 수 있다.\n\n## 후속 연구 우선순위\n\n|우선|과제|완료 판단 기준|범위|\n|---|---|---|---|\n|1|제작 카드 한 개를 실제 설명문·문항으로 구현|지문 설명의 완결성, 전 선지 근거와 유일성, 중복 연산 여부를 각각 기록|이번에는 입력 카드까지 완료. 모델 호출은 별도 요청 때|\n|2|교수 설명의 재현성 관찰|대표와 경계에서 학생이 실제로 쓴 단서·중간 발화를 확보|강의 제안과 학습 효과를 분리|\n|3|AKX의 충분 방향 근거|추가 충분성 근거가 있으면 범위 명시, 없으면 제외 유지|정답 오류 확정을 목표로 삼지 않음|\n|4|BKP/BMH와 P058 비교|명시 제외와 실제 포함 반례의 동일/상이 연산 설명|P058 확장이 필요한 경우에만|\n|5|미분류의 유망 연결|아래 가설을 원문·기존 추론으로 대조해 범위 한정 연결 또는 독립 유지|가설을 M0 이상의 검증으로 세지 않음|\n|6|재분류3개|P026/027/034의 하위형 여부를 입력·중간 추론 기준으로 설명|기존ID와 분리 조건 보존|\n\nDEV053의 경로의존/직전상태갱신, U0428의 값/대상 수 구별, DEV023의 QJ·RR 잔여도 원자료의 유보로 유지한다. 전체 미사용 DEV나2,202장면을 다시 풀어야 다음 작업을 시작할 수 있는 것은 아니다.\n\n## 후보 연결도 없는20장면\n\n아래 제목과 추론은 기존 사후 분석의 승계다. 이번에는 새 원문 의미 검증을 하지 않았다. 비교 제안은 새 확정 원리 등록이 아니다.\n\n|장면/사례|기존 연산 제목|후속 행동|\n|---|---|---|\n']
for r in unmapped:
    if r['mapping_status']!='미분류':continue
    p=r['followup_hypothesis'];src=r['source']
    action=p['action'] if p else '기존 중간 추론과 적용 조건을 먼저 읽고, 동일 연산이 확인될 때만 연결한다. 현재는 미분류 보존.'
    u.append('|'+r['event_id']+' '+mdlink(src['source_path'],'/'.join(src['case_ids']))+'|'+tableval(r['title'])+'|'+action+'|\n')
u.append('\n## 후보는 있으나 IR을 부여하지 않은 범위\n\n195장면의 원후보 이름은 제거하지 않았다. 선행 검증 경로 PB(D089), 학습 데이터 구성 단위 OP(D090), 중첩 극값 PR의 BFP007, 자리별 결합 QR의 BFP008 같은 판단은 개별 연구의 지위를 유지한다. 모든 후보를 가장 가까운 상위 원리로 이동하면 다른 중간 연산이 지워지므로 전체 목록의 source_record와 기존후보_보존연결을 함께 읽는다.\n\nBCF의 공식 정답 확인은 의미 충분성 해결이 아니다. 메타/혼합 장면2개는 장면 모집단에서 삭제하지 않았고 직접 출현 빈도로 계산하지 않았다. 기존 원유보93건과 G024/G370 hold도 변경하지 않았다.\n')
(OUT/'미분류와후속검토.md').write_text(''.join(u))

readme='''# 국어 독해·풀이·출제 원리 체계 v1

2026-10-18. 기존 통합 연구를 교재·강의·신규 제작에 쓰기 위한 실제 본문과 입력 카드로 조직했다. 기존 원본·원장·완료 풀이·사례집78개는 수정하지 않았다. 새 사례집이나 신규 blind는 추가하지 않았다.

## 먼저 읽을 것

1. [연구 원리 체계](연구원리체계_v1.md): 상위 조직, 주요 경계,63개 원리의 실행 카드.
2. [교재 학습 단위](교재학습단위_v1.md)와 [강의 설계](강의설계원칙_v1.md): 연구 원리와 구분한12개 잠정 단위, 실제 학생 행동과 대안 풀이.
3. [출제 설계 원칙](출제설계원칙_v1.md)과 [제작 입력 카드4종](다중AI_출제입력카드.md): 설명문 요구·개념 관계·문단·문항 추론·오답·유일성 조건.
4. [검증 범위와 사용 제한](v1_검증범위와사용제한.md): 직접 확인과 승계·자동 연결·미검증의 구별.

## 현재 규모와 의미

|단위|상태|
|---|---|
|연구 원리63|잠정 안정화26·단독 잠정29·추가 비교5·재분류3|
|상위 조직7·관계52|탐색/계층/중첩/선후/대조 관계. 새 확정 원리 수에 합산하지 않음|
|기존 후보112|A12·B17·C58·D25의 정의·조건·근거·유보 보존|
|장면2,202 / 문항1,667|원 장면ID와 출처 전건 연결, 전건 새 의미 검증 아님|
|이번 직접 대조21장면|16문항·15지문군, 원리 연결23건. 기존191장면의 일부를 재대조|
|승계119장면 / 기계 연결만1,847장면|I1 기존 명시 연결과 M0 후보명 경유를 구별|
|IR 미연결 후보195 / 미분류20|기존 추론과 후속 제안 보존|
|변형 효과300|원문 보존+다섯 효과 축 정리. 실제 수정 문항300개 제작 아님|
|학습 단위12·제작 카드4|잠정 교육안과 실제 제작 입력. 학생 효과·완성 문항 미검증|

제작 카드는 관측 자료의 두 요약값과 복원, 두 운전 구간 저장조의 수지, 예약의 취소·비용·이력 규칙, 기록물 인증의 독립 근거를 다룬다. 가상 수치·기관·논증은 설계 가정이며 실제 기출 정보와 구별된다.

## 파일 계약

|파일|용도|
|---|---|
|[원리계층과관계.json](원리계층과관계.json)|63노드의 입력/단서/중간 추론/출력/조건/경계/출처/상태와52관계|
|[판단장면_원리연결.jsonl](판단장면_원리연결.jsonl)|장면당1행. source_record와source로 출처 추적; principle_links의 검증 등급과 역할을 반드시 함께 읽음|
|[대표경계사례_인덱스.md](대표경계사례_인덱스.md)|이번 직접 대조와 기존 원리별 근거 분리|
|[미분류와후속검토.md](미분류와후속검토.md)|유보·215미연결 장면·후속 우선순위|
|[다중AI_출제입력카드.json](다중AI_출제입력카드.json)|Markdown과 같은4카드, 모델 중립 입출력 계약과 S/A/H/R/U/L 층위|
|[출제변형효과_300건_분류.jsonl](출제변형효과_300건_분류.jsonl)|원효과·주효과·정오/경로/목표/불능/복수 위험; 명시 안 됨은 위험 없음이 아님|
|[연구자관점_반영방법.md](연구자관점_반영방법.md)|수시 의견·수업 관찰·의미 수정의 반영. 별도 최종 승인 대기 없음|
|[기준입력상태.json](기준입력상태.json)|입력 지점·주요13파일의 저장 상태·원 모집단 기록|
|[v1_집계.json](v1_집계.json)|현재 파생본의 정확한 계수. 초기 기준 스냅샷의 집계보다 우선|
|[검증보고서.json](검증보고서.json)|파일·ID·참조·장면 집합·주요 입력 보존의 국소 검사|
|[checkpoint.json](checkpoint.json)|완료 범위와 다음 실행 위치|

M0는 후보명 경유 탐색, I1은 기존 원장에 명시된 장면별 의미 연결 승계, V2는 이번 지정 구간 원문/기존 추론 직접 대조다. 하나의 장면에 등급이 다른 여러 연결이 있을 수 있다. V2 포함 장면이라고 그 안의 모든 M0 연결까지 검증된 것은 아니다. 경계 연결은 긍정 적용의 반복 출현으로 세지 않는다. 후보 경유9,890건을 풀이 연산 빈도로 사용하지 않는다.

보조 데이터는 [기존 후보 보존](기존후보_보존연결.jsonl), [기출 출처색인](기출사례_출처색인.jsonl), [직접 대조 기록](대표대조_검토기록.jsonl), [미분류 후속 목록](미분류장면_후속목록.jsonl), [사용 제외 적용](사용제외_적용목록.json)에 있다. 기계 판독 경로는 저장소 루트 기준, Markdown 링크는 각 파일 기준이다. ID를 모델별 이름으로 재번호화하지 않는다.

## 다음 작업

대표 카드 하나를 골라 사실 자료와 독립 설명문을 작성한 뒤 실제 문항의 전 선지 근거·유일성·추론 중복을 검토한다. 별도 요청이 있으면 독립 AI 제작/비판 계약을 실행할 수 있으나 이번에는 모델 호출·비교 실험을 하지 않았다. 연구 확장이 필요하면 AKX의 충분 방향, BKP/BMH와 P058, 제안된 미분류 연산부터 좁게 검토한다. 학생 반응과 연구자 관점은 수시로 반영한다.

## 편집 재개

`build_v1.py`는 이번의 연산명세/대표대조 TSV와 기존 입력을 읽어 파생 JSON·색인을 만든다. `write_cards.py`는 실제 카드 데이터에서 MD/JSON을 함께 만든다. 본문 교육·강의·설계 원칙은 직접 편집 파일이다. 스크립트 실행은 원장 재분석이 아니며 입력이 기준 스냅샷에서 바뀌면 중단한다. 후속 수정 때는 먼저 변경 목적과 상태를 checkpoint에 남기고 관계·장면·카드 참조를 함께 확인한다. 기존 연구의 author/audit 스크립트 재실행이나 Git push는 필요하지 않다.
'''
(OUT/'README.md').write_text(readme)
print(json.dumps(counts,ensure_ascii=False,indent=2))
