"""허용된 기존 분석만 재사용하여 v0.2 파일을 생성한다. 정본·검증 내용·원장은 열지 않는다."""
import hashlib
import json
import re
from pathlib import Path

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
PILOT=OUT.parent/'20261009_pilot_01'
APP=OUT.parent/'20261010_application_01'
if (OUT/'freeze_manifest.json').exists():
    raise SystemExit('이미 동결된 실행이다. 수정은 새 버전·새 폴더에서 수행해야 한다.')
def read(p): return json.loads(p.read_text())
def rows(p): return [json.loads(s) for s in p.read_text().splitlines()]
def save(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def md(name,lines): (OUT/name).write_text('\n'.join(lines)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

events=rows(APP/'revised_events.jsonl')
old_events={e['event_id']:e for e in rows(PILOT/'pilot_events.jsonl')}
audits={a['event_id']:a for a in rows(APP/'citation_audit.jsonl')}
boundaries=read(APP/'boundary_links.json')
counts=read(PILOT/'pilot_counts.json')
selection=read(PILOT/'sample_manifest.json')
old_cards=(PILOT/'pattern_cards.md').read_text()
matrix=(APP/'02_패턴별_활용_매트릭스.md').read_text()

# 상위 원리, 적용 인정의 최소 증거, 인접 후보 구별, 실제 하위 조작을 사전 정의한다.
spec={
 'P01':{
  'principle':'술어·역할·관계의 귀속은 원문이 연결한 대상에 보존되어야 한다.',
  'minimum':['둘 이상의 대상과 각 대상의 역할 또는 주장에 대한 구별 가능한 근거','대상-술어 또는 관계 양 끝이 특정 선지에서 이동했거나 확인되는 위치','원래 연결과 선지 연결의 차이를 설명한 판단'],
  'distinction':'P02는 같은 대상 안의 판단 축 이동이다. S06은 대상 동일성 자체가 미확정이다. AQP의 평가 근거 부재는 단순 술어 교환과 별개 확장형으로 유지한다.',
  'subtypes':[
   ('attribution','단항 귀속 복원',['E007','E011','E036'],'선지의 주어와 술어를 나누고 같은 술어의 원문 담당자를 찾아 연결한다.'),
   ('cause_type','원인 종류와 보정 정보',['E016'],'왜곡 현상을 원인 종류에 연결한 뒤 그 원인을 보정하는 정보를 대조한다.'),
   ('relation_endpoints','관계의 양 끝 복원',['E033'],'무엇이 무엇을 위반했는지 두 대상을 모두 적고 원문의 위반 관계와 비교한다.'),
   ('evaluation_target','평가 대상 행동의 근거',['E040'],'평가받는 인물과 행동을 함께 특정하고 그 행동의 평가 근거가 본문에 있는지 찾는다.')],
  'hold':'핵심 단항 귀속과 원인·양항 관계·평가 근거 탐색 사이의 전이 미확인. 통합·분할 모두 유보.'},
 'P02':{
  'principle':'한 판단 축의 일치·변화는 연결 근거 없이 다른 축의 일치·변화로 전이되지 않는다.',
  'minimum':['서로 다른 질문으로 표현할 수 있는 두 판단 축','각 축의 답 또는 미확정 상태와 축 사이 연결 유무의 근거','선지가 어느 축의 결론을 어느 축으로 이동하는지 또는 같은 축끼리 비교하는지의 명시'],
  'distinction':'P01은 담당 대상 이동, P07은 시점·상태 이동이다. S05는 규범/실행이라는 특수 관계를 포함한다. AC처럼 정의가 축을 연결하면 무조건 독립으로 처리하지 않는다.',
  'subtypes':[
   ('responsibility_degree','책임자·정도·단계 구별',['E003'],'누가 무엇을 언제 입증하는지와 인정 정도를 따로 대조한다.'),
   ('viewpoint_axes','견해의 판단 축별 공통점',['E025','E026'],'과학성/진릿값 또는 구성/환원 가능성을 각각 질문으로 바꾸고 같은 질문의 답끼리 비교한다.')],
  'hold':'S05와 상위 행동의 중첩 유지. AB에는 시간 단계가 추가되므로 단순 2열 분리만으로 완전 설명했다고 하지 않는다.'},
 'P03':{
  'principle':'비교 결론은 대상·척도·고정 조건과 원문이 준 관계의 방향을 보존해야 한다.',
  'minimum':['비교할 두 대상 또는 전후 상태와 척도','증가·감소 또는 역순 비교를 허용하는 명시 관계와 고정 조건','선지의 비교 방향까지 이르는 중간 연결'],
  'distinction':'P07은 이미 제거되거나 남은 상태의 배치가 핵심이다. S01은 사전 차이에서 사후 차이의 필연성을 도출할 수 있는지 묻는다. BJ의 충분 문턱만으로 단조 증가를 인정하지 않는다.',
  'subtypes':[
   ('inverse_order','정의에 따른 역순 비교',['E004'],'수치 크기를 비교하고 정의가 정한 척도 방향으로 변환한다.'),
   ('conditional_chain','조건 고정 후 방향 연쇄',['E005'],'같은 계절·달 위치를 고정하고 이심률→거리→조차의 방향을 연결한다.'),
   ('relative_ratio','상대 크기의 전후 비교',['E018'],'그림의 거리와 방향을 확인하고 절대 크기와 두 대상의 비율 변화를 구별한다.')],
  'hold':'역순·연쇄·비율의 실제 하위 조작을 유지. 상위 질문 공유가 하나의 풀이 절차라는 증거는 아니다.'},
 'P04':{
  'principle':'특정 결과·권한·방법의 적용은 그 경로에 필요한 전제의 충족을 요구한다.',
  'minimum':['판단할 결과·권한·방법과 그 적용 범위의 특정','조건이 단지 유리하거나 충분한 것이 아니라 그 경로에 필요하다는 근거','사례에서 해당 조건의 충족/결손을 확인하고 결론 범위를 제한한 추론'],
  'distinction':'AA의 모두 충족 요건, GM의 신호 발생 기전, BK의 양도 범위는 전제를 찾는 근거가 다르다. AH는 행위 규칙이 없어 적용할 전제 자체가 제시되지 않는다. 한 경로의 필요조건을 전체 결과의 필요조건으로 확대하지 않는다.',
  'subtypes':[
   ('explicit_requirements','AA: 명시된 누적 요건',['E002'],'모두 충족 문구에서 요건을 회수하고 고의·과실 결손이 책임 성립 주장과 양립하는지 확인한다.'),
   ('measurement_mechanism','GM: 측정 기전의 전제',['E022'],'신호 발생자→신호→평가 방법의 연결을 복원하고 발생 전제 결손이 해당 방법에 미치는 범위만 판단한다.'),
   ('authority_scope','BK: 권한과 양도 범위',['E013'],'행사 가능한 권한의 범위와 생명의 양도 제외 근거를 결합하여 허용 여부를 판단한다.')],
  'hold':'세 하위 판단은 상위 묶음 안에 별도로 보존한다. 외부 표본 전이 전에 무조건 통합하거나 분할하지 않는다.'},
 'P05':{
  'principle':'문맥 결합은 의미 후보를 제한하지만 의미 선택 절차를 설명하는 것과 실제 선택 수행은 다르다.',
  'minimum':['의미 또는 용례를 달리할 수 있는 표현과 실제 문맥','후보 의미·치환어를 제한하는 주어·목적어·후속 동작의 근거','활용을 인정하려면 특정 선지에서 후보를 줄이거나 같은 뜻을 확인하는 조작이 실제로 연결되어야 함'],
  'distinction':'S04는 두 후보 적합/무적합이라는 유보 원인 구별이다. E028/ZE는 절차 설명이며 직접 어휘 선택을 수행하지 않는다. E030/ZF④·⑤는 보기 해석 확인의 보조 활용이다.',
  'subtypes':[
   ('lexical_comparison','문맥 용례·치환 비교',['E010','E015','E019'],'주어·목적어를 유지한 채 쉬운 풀이말이나 치환어를 대입하여 같은 의미인지 확인한다.'),
   ('contextual_confirmation','보기의 문맥 제약 확인',['E030'],'후속 동작과 각 해석 후보를 결합하여 과일·신체 부위 해석이 남는 근거를 설명한다.'),
   ('description_only','의미 선택 절차의 설명',['E028'],'절차 설명과 선지의 일치를 대조한다. 이 행동을 P05의 직접 수행으로 계수하지 않는다.')],
  'hold':'E028은 설명·경계 관계로만 활용 집계에서 제외한다. E030은 정답③ 직접 결정에 필수는 아니나 비정답 선지 검토의 활용이다.'},
 'P06':{
  'principle':'대책은 글이 지정한 문제·평가 관점과 원인 관계에 대응해야 한다.',
  'minimum':['평가 주체와 발문이 지정한 구체적 문제','본문이 문제 삼은 원인·결과 또는 목적 관계','제시된 대책이 그 관계의 어느 부분에 작용하는지에 대한 연결'],
  'distinction':'P07의 ANV는 과거 정책 시점 대조이며 새 대책 선택이 아니다. 정책이 좋아 보인다는 일반 평가만으로 적용하지 않는다.',
  'subtypes':[
   ('control_power','비대한 권력의 통제',['E037'],'마지막 문제를 권력 비대화로 고정하고 대책이 시민 감시를 늘리는지 국가 정당성을 강화하는지 구별한다.'),
   ('correct_dependence','통치 자기 교정을 막는 의존',['E039'],'글쓴이의 비판 관점을 유지하고 과도한 의존과 통치 실패를 바꿀 수단을 확인한다.')],
  'hold':'현재 LEET·MEET 근거만 연결됨. KICE 생성 규칙으로의 전이는 미확인.'},
 'P07':{
  'principle':'상태와 사건은 원문이 확보한 선후·시점에 배치되어야 한다.',
  'minimum':['명시 시간·처리 정의·인과 기전 가운데 적어도 하나로 지지되는 선후 관계','단계별로 발생·제거·잔존하는 상태 또는 사건','선지의 시점과 상태를 대입하여 확인할 차이'],
  'distinction':'P03의 AD는 같은 계절의 조건부 비교다. E032/AJP①의 명분/실태는 그 자체로 전후 관계가 아니다. E031/AJP②는 규정/실행의 별도 경계다.',
  'subtypes':[
   ('processing_state','중간 처리 상태',['E017'],'㉠→㉡→㉢에서 제거된 효과와 남은 효과를 구별하여 선지를 대입한다.'),
   ('causal_sequence','발생·감지의 기전 순서',['E021'],'자극→청세포 반응→소리 전달→감지 경로를 측정 위치와 결합한다.'),
   ('historical_placement','역사적 전후 배치',['E035'],'초기와 이후의 정책을 원문 시간 근거에 배치하고 선지가 옮긴 시점을 찾는다.')],
  'hold':'처리·기전·역사의 증거 유형과 조작 차이를 유지한다. GL④ 수식 미검증은 GL①에 대한 기존 근거 재사용과 별개로 남긴다.'},
 'S01':{
  'principle':'갱신 전 값의 차이만으로 갱신 후 값의 차이가 필연적이라고 할 수 없다.',
  'minimum':['갱신값을 정하는 규칙','사전값 차이와 조건부 갱신값에 대한 정보 범위','서로 다른 사전값과 같은 사후값이 규칙과 양립할 수 있다는 근거 또는 반모형'],
  'distinction':'P03은 주어진 비교 방향의 전파다. S04는 해석 후보 선택 유보다. E014/BK②는 약함/전무 구별이지 갱신이 아니다.',
  'subtypes':[('update_possibility','갱신값 동일 가능성',['E009'],'사후값 차이를 강제하는 정보가 있는지 확인하고 같은 사후값 가능성을 금지하는 단정을 검토한다.')],
  'hold':'일대일 갱신이 명시되면 차이 보존을 인정해야 한다. 수치 반모형을 언제나 필수로 요구하지 않는다.'},
 'S02':{
  'principle':'관측의 존재와 경쟁 설명을 가르는 근거 역할은 구별된다.',
  'minimum':['본문에 제시된 목표 설명과 대안 설명','두 설명의 관측 수용 차이 또는 그 차이에 대한 본문의 명시 설명','선지가 지지 근거로 기능하는 이유와 공통 관측이 불충분한 이유'],
  'distinction':'P02의 OZ는 견해 공통점/진릿값 판단이다. 대안을 외부 지식으로 발명하거나 대안 하나의 실패를 목표 설명의 유일한 참으로 확대하지 않는다.',
  'subtypes':[('discriminating_observation','공통·판별 관측 구별',['E020'],'관측이 어느 설명과 양립하는지 비교하거나 본문에 명시된 판별 근거를 회수한다.')],
  'hold':'GK는 명시 근거 회수만으로도 해결 가능하다. 경쟁 설명을 직접 생성하는 풀이가 필수라고 하지 않는다.'},
 'S03':{
  'principle':'복합 전개 선지의 모든 동작은 실제 문단 기능으로 뒷받침되어야 한다.',
  'minimum':['전개 동작이 둘 이상 연결된 선지','각 동작에 대응하는 문단 기능과 대응하지 않는 동작의 확인','앞절 일치와 뒷절의 새 이론 도출 등을 분리한 판단'],
  'distinction':'문학의 지각·서술 주체 판정인 E041/AVS와 같게 처리하지 않는다. 마지막 문장만 확인하는 요령으로 축소하지 않는다.',
  'subtypes':[('discourse_actions','전개 동사별 대응',['E023'],'선지의 동사를 나누고 실제 비판 검토·재해석·의의 평가와 하나씩 연결한다.')],
  'hold':'한 지문 잠정 후보이며 기존 100코드 주 판정의 유보도 해소하지 않는다.'},
 'S04':{
  'principle':'같은 판정 유보도 복수 적합과 무적합이라는 서로 다른 원인을 가질 수 있다.',
  'minimum':['구별 가능한 후보 목록','각 후보의 적합 여부 또는 남은 후보 수를 정하는 명시 근거','같은 유보 결과에 대한 원인을 선지가 바꾼 위치'],
  'distinction':'P05의 의미 후보 제한과 같은 문항에서 공존할 수 있으나 조작은 다르다. S01은 사람별 갱신값 차이 문제다.',
  'subtypes':[('remaining_candidates','유보 원인의 후보 수',['E029'],'적합 후보를 남겨 보고 둘 이상 남은 상태와 하나도 없는 상태를 구별한다.')],
  'hold':'단순히 모른다고 한 문장만으로 유보 원인을 임의 분류하지 않는다.'},
 'S05':{
  'principle':'규정의 존재와 그 규정의 이행은 서로 다른 판단이다.',
  'minimum':['규정의 내용·적용 범위','규정과 어긋난 실행 또는 미이행의 근거','선지가 실행의 실패를 규정 부재로 바꾸는 위치'],
  'distinction':'P02와 상위 축 보존은 닮았지만 규범의 효력·예외 판단이 추가될 수 있다. AB는 인정 정도·책임·반증 단계 구별이며 규정 위반 장면이 아니다.',
  'subtypes':[('norm_execution','규정 존재/이행 구별',['E031'],'규정이 있었는지와 지켜졌는지 각각 답하고 결여라는 선지 표현을 대조한다.')],
  'hold':'P02와 통합·분할 결론 유보. 규정 공백 또는 적법한 예외가 명시되면 위반으로 처리하지 않는다.'},
 'S06':{
  'principle':'시기별 집단의 동일성에는 명칭의 출현 순서 외에 연결 근거가 필요하다.',
  'minimum':['서로 다른 시기의 집단 표현','선지가 주장하는 동일성·재등장 관계','별칭·지칭·구성원 연속성 등의 연결 근거가 있는지 확인한 범위'],
  'distinction':'P01은 이미 구별된 대상 사이의 술어 귀속이고 P07의 ANV는 같은 국가의 명시적 정책 전후다. 이름 차이만으로 집단 차이를 확정하지 않는다.',
  'subtypes':[('group_identity','집단 동일성 연결 검사',['E038'],'각 집단의 시기·실제 서술을 적고 동일 집단이라는 연결 근거를 찾는다. 없으면 동일성 단정을 지지하지 않는다.')],
  'hold':'현재 MEET 한 지문 근거. 연결 근거 없음과 실제로 다른 집단임을 구별한다.'}
}

role_definitions={
 'structure_present':'해당 정보 구조가 존재하거나 명시적으로 설명됨. structure_mode로 구현/설명을 구별. 활용의 자동 증거가 아님.',
 'item_utilized':'지문 구조가 발문·보기·선지 판단에서 실제 조작으로 활용됨. 비정답 선지 검토와 보조 활용도 포함.',
 'solution_helpful':'기존 기록 또는 명시된 풀이에서 해당 행동이 유효한 판단 경로를 제공함. 모든 타당한 풀이에 필수라는 뜻 아님.',
 'explanatory_only':'패턴의 행동을 내용으로 설명하거나 예시하나 그 행동을 직접 수행한 증거는 아님.',
 'boundary_case':'적용 범위나 인접 후보의 구별을 보여 주는 경계·비해당 관계. 출현·활용 빈도에서 제외.',
 'unconfirmed':'관련 가능성은 있으나 자료·중간 추론이 부족하여 적용 여부 미확인. 비적용과 구별.',
 'unclassified':'판단 장면은 있으나 동결된 후보에 배속하지 않음. 13개 후보로 억지 통합하지 않음.'
}
cards=[]; subtype_for={}
for pid,s in spec.items():
    block=re.search(r'^## '+pid+r'\. (.*?)\n(.*?)(?=^## |\Z)',old_cards,re.M|re.S)
    assert block,pid
    name=block.group(1);body=block.group(2)
    def oldfield(label):
        return re.search(r'^- '+label+r': (.*)$',body,re.M).group(1)
    mb=re.search(r'^## '+pid+r' — .*?\n(.*?)(?=^## |\Z)',matrix,re.M|re.S).group(1)
    af={}
    for line in mb.splitlines():
        if re.match(r'\|[A-F] ',line):
            k,v=line.strip('|').split('|',1);af[k[0]]=v
    evaluation=next(l for l in matrix.splitlines() if l.startswith('|'+pid+'|')).strip('|').split('|')
    subtypes=[]
    for suffix,title,eids,action in s['subtypes']:
        sid=pid+'.'+suffix
        subtypes.append({'subtype_id':sid,'name':title,'anchor_events':eids,'student_operation':action,
                         'status':'상위 후보 내부의 조작 구별; 독립 신규 패턴 아님'})
        for eid in eids: subtype_for[(pid,eid)]=sid
    cards.append({
     'pattern_id':pid,'name':name,
     'status':'표본 내 반복 후보' if pid.startswith('P') else '단독 지문 잠정 후보',
     'upper_judgment_principle':s['principle'],'sub_operations':subtypes,
     'application_units':{
       'passage':{'allowed':True,'condition':'정보 구조 확인; 이것만으로 문항·풀이 활용을 인정하지 않음'},
       'question':{'allowed':True,'condition':'발문·보기·선지에 연결된 실제 활용 또는 설명 관계를 구별'},
       'choice':{'allowed':True,'condition':'선지 번호와 판단 차이를 특정; 내용 판정/정답 선택 분리'},
       'solution':{'allowed':True,'condition':'원문 근거→중간 조작→해당 판단의 경로를 제시; 표 작성은 강제하지 않음'}},
     'minimum_evidence':s['minimum'],'evidence_missing_decision':'unconfirmed; 비적용으로 간주하지 않음',
     'application_conditions':[oldfield('적용 조건')],
     'inherited_information_structure_examples':af['A'],
     'inherited_item_design_examples':af['B'],
     'non_application_conditions':[oldfield('적용하지 말 것')],
     'non_application_examples':[af['F']],
     'neighbor_distinctions':s['distinction'],'required_student_actions':[af['C']]+[x['student_operation'] for x in subtypes if not x['subtype_id'].endswith('description_only')],
     'alternative_valid_solutions':{'allowed':True,'necessity_claim':'유효한 경로와 유일·필수 경로를 구별한다.',
       'examples':'본문 직접 대조·문장 설명·표·기호 등 근거와 판단을 보존하는 다른 표현을 허용한다. S02는 명시된 근거 회수만으로도 가능하다.'},
     'pattern_relation_allowed':list(role_definitions),
     'frequency':{'scope':'발견용 목적 표본 12지문·39문항의 기존 연결 장면만','legacy_counts':counts['patterns'][pid],
                  'corpus_prevalence':None,'sampling_rate_inference_allowed':False},
     'value_assessments':{
       'lecture':{'assessment':evaluation[4],'evidence_status':'활용 매트릭스의 설계 판단; 학생 효과 관찰 없음'},
       'textbook':{'assessment':af['D'],'evidence_status':'설명·행동 설계 제안; 반복 빈도로 대체 평가하지 않음'},
       'original_item_creation':{'assessment':evaluation[5],'design_conditions':af['E'],'evidence_status':'설계 가능성 판단; 생성 품질 일반 보증 아님'}},
     'held_boundary':s['hold'],
     'boundary_anchors':[b for b in boundaries if b['pattern_id']==pid],
     'sources':[{'path':str(PILOT.relative_to(ROOT)/'pattern_cards.md'),'section':pid},
                {'path':str(APP.relative_to(ROOT)/'02_패턴별_활용_매트릭스.md'),'section':pid},
                {'path':str(APP.relative_to(ROOT)/'03_대표와_경계_사례.md'),'section':pid}],
     'verification':{'mode':'기존 분석·application 정정의 승계','canonical_original_reopened':False,
                     'semantic_quote_reverification':'이번 실행에서 정본 대조 재확인 미실시; 기존 검증 범위만 승계'}})

mapping=[]
for e in events:
    eid=e['event_id'];pe=old_events.get(eid,{})
    relations=[]
    for pid in e['pattern_ids']:
        description=eid=='E028' and pid=='P05'
        roles=['structure_present','explanatory_only'] if description else ['structure_present','item_utilized','solution_helpful']
        relations.append({'pattern_id':pid,'pattern_relation':roles,'decision':'confirmed_inherited',
                          'subtype_ids':[subtype_for[(pid,eid)]],
                          'choice_ids':[j['choice_id'] for j in e['judgments']],
                          'structure_mode':'설명된 구조' if description else '기존 카드의 구조 확인',
                          'item_utilization_mode':'비활용: 절차 설명 대조' if description else ('보조 선지 검토' if eid=='E030' else '국소 선지 판단 활용'),
                          'solution_necessity':'직접 행동 활용 아님' if description else pe.get('action_necessity','필수성 미확정'),
                          'basis':e['minimum_distinction'],'boundaries':[]})
    for b in [b for b in boundaries if b['event_id']==eid]:
        r=next((r for r in relations if r['pattern_id']==b['pattern_id']),None)
        if r is None:
            r={'pattern_id':b['pattern_id'],'pattern_relation':['boundary_case'],'decision':'non_applicable_inherited',
               'subtype_ids':[],'choice_ids':b['choice_ids'],'structure_mode':None,'item_utilization_mode':'비활용: 경계',
               'solution_necessity':'해당 후보의 활용 증거가 아님','basis':b['reason'],'boundaries':[]}
            relations.append(r)
        else: r['pattern_relation'].append('boundary_case')
        r['boundaries'].append({'choice_ids':b['choice_ids'],'reason':b['reason']})
    unclassified=not e['pattern_ids']
    if unclassified:
        relations.append({'pattern_id':None,'pattern_relation':['unclassified'],'decision':'unclassified',
                          'subtype_ids':[],'choice_ids':[j['choice_id'] for j in e['judgments']],
                          'basis':'application에서 후보 배속 없음. 정답 경로 보완 및 경계 관계가 있어도 새 배속을 만들지 않음.'})
    a=audits.get(eid)
    mapping.append({'sample_split':'discovery','event_id':eid,'case_id':e['case_id'],'passage_id':pe.get('resolved_passage_id',e['question_id'].rsplit('-Q',1)[0]),
                    'passage_group':e['passage_group'],'question_id':e['question_id'],'exam_family':e['exam_family'],
                    'legacy_pattern_ids':e['pattern_ids'],'legacy_unclassified':unclassified,
                    'judgments_reused':e['judgments'],'relations':relations,
                    'event_source':{'path':str(APP.relative_to(ROOT)/'revised_events.jsonl'),'event_id':eid},
                    'evidence_references':e.get('original_evidence_reused',[]) or [e.get('passage_support',{})],
                    'quotation_audit':{'source':str(APP.relative_to(ROOT)/'citation_audit.jsonl') if a else str(APP.relative_to(ROOT)/'revised_events.jsonl'),
                                       'event_id':eid,'inherited_status':a['old_quote_assessment'] if a else '기존 정답 경로 추가 추출',
                                       'corrected_support':a['corrected_support'] if a else [e['existing_support']],
                                       'canonical_original_rechecked_this_run':False,
                                       'current_semantic_verification':'미재검증; 정본 원문을 열지 않고 기존 분석의 교정 결과만 승계'},
                    'annotation_origin':'v0.2 역할 분리는 신규 명세; 내용·선지·코드 판단은 기존 결과 승계'})

codebook={'schema_version':'0.2','codebook_id':'pattern-application-v0.2','status':'외부 적용 전 동결 후보 코드북; 검증 완료 규칙 아님',
          'goals':['기출의 지문·문항·풀이 판단 패턴 발견','교재 제작','강의 시연·재현 가능한 학습 행동','독창적 지문·문항 설계'],
          'pattern_relation_definitions':role_definitions,
          'invariants':['후보 13개 상태 보존','한 사건에 복수 패턴·역할 허용','경계와 미확인·미분류는 출현·활용 계수에서 제외',
                        '내용 적절성과 정답 선택 분리','SDSS 태그·100코드 번호만으로 적용 판정 금지','기존 100코드 변경 없음'],
          'cards':cards}
save('codebook_v0.2.json',codebook)
(OUT/'event_mapping_v0.2.jsonl').write_text(''.join(json.dumps(m,ensure_ascii=False)+'\n' for m in mapping))

discovery=[{'passage_group':s['passage_group'],'case_ids':s['case_ids']} for s in selection['samples'] if s['split']=='discovery']
validation=[{'passage_group':s['passage_group'],'case_ids':s['case_ids']} for s in selection['samples'] if s['split']=='validation']
save('management_metadata.json',{
 'discovery':discovery,'validation_metadata_only':validation,'holds_preserved':['G024','G370'],
 'validation_content_applied':False,'new_passages_created':False,'other_models_called':False,
 'exposure_history':[{'group':'G095','case':'NM','prior_exposure':'기존 정답·코드 요약 노출 이력 승계; 값은 이 파일에 포함하지 않음',
                      'current_incident':'sample_annotations.json의 노출 이력 필드에 포함된 정답·코드 값이 메타데이터 확인 출력에서 재노출됨. 이번 범위 위반으로 기록.',
                      'source':'../20261009_pilot_01/sample_annotations.json#/validation_contamination/0',
                      'restriction':'현재 실행 주체는 G095의 미노출 독립 검토자로 사용할 수 없음. 미노출 독자 배정은 후속 작업의 별도 절차.',
                      'validation_body_opened':False}],
 'other_validation_groups':'이번 실행의 출력에서 내용·정답·예상 패턴을 확인하지 않음. 과거 학습 노출 부재까지 보증하지 않음',
 'guard':'다음 독립 검토자에게 원 sample_annotations.json을 그대로 전달하지 않고 이 값 제거본을 제공한다.'})

lines=['# 패턴 적용 코드북 v0.2', '',codebook['status'], '',
 '기존 13개 후보의 상태를 보존한 운영 명세다. 하위형은 실제 행동 차이를 기록하는 내부 식별자이며 새 패턴 후보가 아니다. 기존 분석을 다시 풀거나 정본과 재대조하지 않았다. 인용 의미의 검증은 application의 교정 범위만 승계하고 이번 정본 재검증 여부는 미확인으로 표시한다.', '',
 '기계 판독본: [codebook_v0.2.json](codebook_v0.2.json). 역할·계수: [계수 규칙](counting_rules.md). 사전 판정: [프로토콜](application_protocol.md).', '',
 '## 관계 필드', '', '|pattern_relation 값|뜻|','|---|---|']
for k,v in role_definitions.items():lines.append(f'|{k}|{v}|')
for c in cards:
    lines += ['',f"## {c['pattern_id']} {c['name']}",'',f"상태: {c['status']}",'',f"상위 판단 원리: {c['upper_judgment_principle']}",'',
              '### 실제 하위 조작','', '|하위형|기존 장면|학생의 행동|','|---|---|---|']
    for st in c['sub_operations']:lines.append(f"|{st['subtype_id']} — {st['name']}|{', '.join(st['anchor_events'])}|{st['student_operation']}|")
    lines += ['', '### 적용 명세', '', '**적용 단위:** 지문은 구조 확인, 문항은 활용·설명 구별, 선지는 내용 판정, 풀이는 실제 조작 경로의 확인이다. 단위 간 자동 승격은 없다.', '', '**최소 근거 — 모두 충족해야 함:**', '']
    lines += ['- '+x for x in c['minimum_evidence']]
    lines += ['', '**적용 조건:**', '']+['- '+x for x in c['application_conditions']]
    lines += ['', '**비적용 조건:**', '']+['- '+x for x in c['non_application_conditions']]
    lines += ['', '**기존 구조·문항 구현 예시(외부 표본에 같은 소재를 요구하는 조건 아님):** '+c['inherited_information_structure_examples']+' '+c['inherited_item_design_examples'],
              '', '**기존 비적용 예시:** '+c['non_application_examples'][0]]
    lines += ['', '**유사 패턴 구별:** '+c['neighbor_distinctions'], '', '**학생 행동:** '+c['required_student_actions'][0], '',
              '**다른 타당한 풀이 허용:** '+c['alternative_valid_solutions']['examples'], '', '**보류 경계:** '+c['held_boundary'], '',
              '### 빈도와 활용 가치의 분리', '',
              f"기존 연결 규모: 구조 {c['frequency']['legacy_counts']['observed_passages']}지문, 실제 활용 {c['frequency']['legacy_counts']['utilized_passages']}지문·{c['frequency']['legacy_counts']['utilized_questions']}문항. 목적 표본의 연결 수이며 원 코퍼스 발생률은 미산출.", '',
              '- 강의: '+c['value_assessments']['lecture']['assessment'],
              '- 교재: '+c['value_assessments']['textbook']['assessment'],
              '- 창작: '+c['value_assessments']['original_item_creation']['assessment'],
              '- 설계 조건: '+c['value_assessments']['original_item_creation']['design_conditions'], '',
              '세 가치 평가는 기존 매트릭스의 설계 판단이다. 학생의 학습 효과·오답 빈도는 미관찰이다.', '',
              f"근거: [pilot 카드](../20261009_pilot_01/pattern_cards.md), [application 매트릭스](../20261010_application_01/02_패턴별_활용_매트릭스.md), [사례집](../20261010_application_01/03_대표와_경계_사례.md)의 {c['pattern_id']} 절. 경계의 정확한 event·선지는 JSON의 boundary_anchors와 아래 매핑을 따른다."]
md('codebook_v0.2.md',lines)
ml=['# 기존 장면과 코드북 v0.2 매핑', '',
    '기존 46장면을 보존한다. 아래 같은 event가 여러 행에 나타나는 것은 복수 관계이며 추가 사건이 아니다. `legacy_pattern_ids`는 출처 보존용이고 계수에 사용하지 않는다.', '',
    '|event / case|선지|후보·하위형|pattern_relation|판정|','|---|---|---|---|---|']
for m in mapping:
    for r in m['relations']:
        ml.append(f"|{m['event_id']} / {m['case_id']}|{','.join(str(i) for i in r['choice_ids'])}|{r['pattern_id'] or '미분류'} / {', '.join(r['subtype_ids'])}|{', '.join(r['pattern_relation'])}|{r['decision']}|")
ml += ['', 'E028/ZE의 P05 연결은 구조 설명+explanatory_only+boundary_case이며 item_utilized·solution_helpful이 없다. E030/ZF④·⑤는 보조 선지 판단으로 item_utilized·solution_helpful을 유지한다.', '',
       'E044~E046은 기존 정답 경로를 보완한 장면이지만 후보 미분류를 유지한다. 다른 후보의 경계 사례라는 이유만으로 원래 미분류 상태를 삭제하지 않는다.', '',
       '인용은 `event_mapping_v0.2.jsonl`의 quotation_audit에 application의 교정 인용·정확한 원장 좌표를 승계했다. 이번에는 원장을 열거나 정본과 의미를 재대조하지 않았다.']
md('event_mapping_v0.2.md',ml)

inputs=['pattern_cards.md','pilot_events.jsonl','pilot_counts.json','sample_manifest.json']
inventory=[{'path':str((PILOT/f).relative_to(ROOT)),'sha256':sha(PILOT/f),'use':'표본 manifest는 식별·분할 메타데이터만, 나머지는 발견용 분석'} for f in inputs]
for f in ['README.md','01_수정_판정장면과_변경기록.md','02_패턴별_활용_매트릭스.md','03_대표와_경계_사례.md','revised_events.jsonl','citation_audit.jsonl','boundary_links.json']:
    inventory.append({'path':str((APP/f).relative_to(ROOT)),'sha256':sha(APP/f),'use':'발견용 분석·정정·활용 명세 재사용'})
inventory.append({'path':str((PILOT/'sample_annotations.json').relative_to(ROOT)),'sha256':sha(PILOT/'sample_annotations.json'),
                  'use':'관리 메타데이터 출력 중 G095 기존 정답·코드 재노출 발생; 값 없는 관리 파일로 분리'})
save('input_inventory.json',inventory)
print('코드북 카드',len(cards),'기존 장면',len(mapping),'생성 완료; 아직 동결 전')
