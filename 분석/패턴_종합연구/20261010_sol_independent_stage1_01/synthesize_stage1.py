"""확정된 독립 기록만 연결하며 외부 연구 파일을 열지 않는다."""
from pathlib import Path
import json
import hashlib
from datetime import datetime, timezone

RUN=Path(__file__).resolve().parent
ROOT=RUN.parents[2]
def dump(name,obj):
    (RUN/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def jsonl(name,rows):
    (RUN/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))

groups=[json.loads((RUN/'analysis'/f'{g}.json').read_text()) for g in ('G064','G095','G119','G157','G350','G310')]
sources={d['case_id']:d for p in (RUN/'sources').glob('*.json') if (d:=json.loads(p.read_text())).get('case_id')}
targets=json.loads((RUN/'targets.json').read_text())
case_metadata={case:{'passage_group':s['passage_group'],'question_id':qid,'source_path':src}
               for s in targets['samples'] for case,qid,src in zip(s['case_ids'],s['question_ids'],s['blind_source_paths'])}
passages=[];questions=[];evidence=[];scenes=[];links=[]
for g in groups:
    gid=g['passage_group'];p=g['passage_analysis']
    passages.append({'unit':'지문','passage_group':gid,**p})
    pool=[('sources/'+c+'.json','passage_text',sources[c]['passage_text']) for c in case_metadata if case_metadata[c]['passage_group']==gid]
    pool += [('sources/'+c+'.json','stem',sources[c]['stem']) for c in case_metadata if case_metadata[c]['passage_group']==gid]
    if gid=='G350':pool += [('sources/'+n,'whole_text',(RUN/'sources'/n).read_text()) for n in ('G350_visual01.md','G350_visual02.md')]
    for eid,quote in p['evidence'].items():
        matches=[]
        for path,field,text in pool:
            start=text.find(quote)
            if start>=0:
                context_start=text.rfind('\n\n',0,start)+2 if '\n\n' in text[:start] else 0
                context_end=text.find('\n\n',start+len(quote))
                if context_end<0:context_end=len(text)
                matches.append({'file':path,'field':field,'char_start':start,'char_end':start+len(quote),'line':text[:start].count('\n')+1,
                                'paragraph_context_start':context_start,'paragraph_context_end':context_end,
                                'paragraph_context':text[context_start:context_end]})
        assert matches, (eid,'원문 근거 불일치')
        evidence.append({'evidence_id':eid,'passage_group':gid,'quote':quote,'locations':matches})
    for a in g['questions']:
        case=a['case_id'];s=sources[case]
        questions.append({'unit':'문항·풀이 연결','passage_group':gid,**case_metadata[case],**a})
        scene_id=case+'-decision'
        scenes.append({'scene_id':scene_id,'unit':'풀이','case_id':case,'passage_group':gid,
                       'operation':a['repeatable_action'],'reasoning':a['reasoning_steps'],
                       'outcome':a['independent_answer'],'answer_status':a['answer_status'],
                       'evidence_ids':a['passage_features_used'],
                       'limit':a['do_not_apply_when'],'alternatives':a['alternative_routes']})
        for o,statement in zip(a['option_judgments'],s['choices']):
            sid=case+'-option-'+str(o['option'])
            scenes.append({'scene_id':sid,'unit':'선지 판독','case_id':case,'passage_group':gid,
                           'source_option_text':statement,'full_option_available':case!='RX',
                           **o,'is_independently_selected':o['option']==a['independent_answer']})
            for eid in o['evidence_ids']:
                links.append({'scene_id':sid,'case_id':case,'evidence_id':eid,'relation':'선지 지지·반박·미확정의 근거','reason':o['specific_reason']})
        for eid in a['passage_features_used']:links.append({'scene_id':scene_id,'case_id':case,'evidence_id':eid,'relation':'전체 풀이에 실제 활용'})
jsonl('passage_analyses.jsonl',passages);jsonl('independent_solutions.jsonl',questions)
jsonl('evidence_anchors.jsonl',evidence);jsonl('decision_scenes.jsonl',scenes);jsonl('evidence_links.jsonl',links)

def candidate(cid,unit,name,definition,cases,when,avoid,counter,applications,status='반복 관찰·잠정 후보'):
    qs=[a for a in questions if a['case_id'] in cases]
    return {'candidate_id':cid,'unit':unit,'name':name,'definition':definition,'cases':cases,
            'passage_groups':sorted({a['passage_group'] for a in qs}),
            'strict_unexposed_case_ids':[a['case_id'] for a in qs if a['passage_group']!='G095'],
            'historical_exposure_case_ids':[a['case_id'] for a in qs if a['passage_group']=='G095'],
            'evidence_ids':sorted({e for a in qs for e in a['passage_features_used']}),
            'decision_scene_ids':[a['case_id']+'-decision' for a in qs],
            'applicable_when':when,'do_not_apply_when':avoid,'sample_boundary_or_counterexample':counter,
            'applications':applications,'status':status,
            'count_warning':'후보 사례는 서로 중복될 수 있다. 해당 수는 빈도·배타적 분류·학습 효과의 측정값이 아니다.'}

candidates=[
candidate('TXT-A','지문','분류 뒤에 성립 조건과 작동 사례를 붙임',
 '상위 범주를 나눈 뒤 각 범주의 입력 조건·작동 차이·사례를 제공한다. 정의를 현상 판별에 쓸 수 있게 만든 조직이다.',
 ['JN','JO','RV','RW','RY'],'여러 하위 범주의 조건이 명시될 때.','범주 이름의 열거만 있고 판별 조건이 없을 때.',
 'G064의 시각 각도 설명은 존재하지만 JN/JO는 각도 계산을 요구하지 않는다. 지문 특징 전체를 문항 행동으로 세지 않는다.',
 '교재: 범주-조건-반례를 연결. 강의: 조건에 맞는 사례를 먼저 찾기. 창작: 표면이 닮고 성립 조건이 다른 현상을 설계.'),
candidate('TXT-B','지문','구조에서 기작·신호·판정으로 단계적으로 연결',
 '부품의 위치와 이동을 설명한 뒤 실제 결합, 표시 신호, 의미 판정, 오류율로 설명 층을 이동한다.',
 ['RV','RW','RX','RY'],'구조와 신호 의미가 명시적으로 연결된 설명일 때.','공간 배열만 보고 반응 관계와 신호 의미까지 보충할 때.',
 '표준선 발색은 정상 진행이고 목표 성분 존재의 보증이 아니다. RX에서는 결합 위치보다 실제 상태별 분모가 필요하다.',
 '교재: 설명 층을 분리한 도식. 강의: 단계마다 무엇을 알 수 있는지 점검. 창작: 정상 신호와 검출 신호를 독립시킴.',status='한 지문 내 여러 문항에서 관찰·지문 간 반복 미검증'),
candidate('TXT-C','지문','선행 주장에 대한 수정·비판·종합을 연결',
 '연구자나 입장의 목록을 나열하는 대신 앞선 설명의 한계, 변경한 가정, 후속 결론의 관계를 명시한다.',
 ['NK','NL','NN','YR','YS','AYE','AYG'],'앞뒤 입장의 관계를 본문이 직접 설명할 때.','연도·인명 존재만으로 비판·진전의 인과를 만들어 낼 때.',
 'G157의 마지막 의의 문장은 구체적 미해결 과제를 제시하지 않는다. G095의 공통 경험 시험은 입장 차이만 강조하면 사라진다.',
 '교재: 주장→문제→변경점 기록. 강의: 무엇을 유지하고 무엇을 바꿨는지 비교. 창작: 후속 입장이 실제 앞선 주장에 답하도록 구성.'),
candidate('TXT-D','지문','여러 발화자의 정책 논쟁과 사후 평가',
 '정책 제안·반대 이유·대안·회고 평가를 복수 인용 목소리로 조직하며 같은 어휘의 대상과 평가가 달라진다.',
 ['ATN','ATO','ATP'],'화자와 인용·회고 경계가 구분될 때.','복수 입장을 한 서술자의 승인된 사실로 합칠 때.',
 '작은 폐단과 왕의 폐단은 같은 기존 군역을 가리킬 수 있다. 같은 사건에 대한 평가 차이와 지시 대상 차이는 별개다.',
 '교재: 화자·정책·시점·평가의 분리. 강의: 발화 귀속. 창작: 같은 단어의 동일/상이 지시를 함께 구현.',status='한 지문에서 관찰·지문 간 반복 미검증'),
candidate('ASK-A','문항','닮은 말·신호·현상을 다른 역할로 바꾸어 제시',
 '본문의 표현을 표면적으로 유지하면서 관찰자/대상, 표지/항체, 검사/표준선, 기존/장래 폐단의 역할을 바꾼 선지를 만든다.',
 ['JO','RV','RW','RY','ATP'],'역할을 구별할 명시 조건이 있을 때.','소재가 같다는 이유만으로 대응한다고 볼 때.',
 'JO의 시간에 따른 공 크기 변화와 동시 집단 분포는 모두 크기가 변하지만 다른 단서다.',
 '교재: 혼동하기 쉬운 역할의 짝을 제시. 강의: 명칭보다 입력을 보기. 창작: 역할 한 개의 교환으로 오답 구성.'),
candidate('ASK-B','문항','본문 규칙을 새 사례나 관찰 결과로 옮김',
 '조건-결과 규칙을 보기에 적용하거나 결과에서 가능한 조건을 역으로 찾도록 설계한다. 순방향 적용과 역방향 복원은 구분한다.',
 ['JO','NM','RY','YT'],'필요 입력이 보기와 본문에 제공될 때.','불완전한 규칙의 결과만으로 단일 원인을 확정할 때.',
 'YT는 전수 네 조합과 규칙 부합 조건이 있어 역추론 가능하다. JO⑤의 실제 공포 반응은 단안 가능성만으로 필연 결과를 정할 수 없다.',
 '교재: 입력→결과와 결과→입력 과제 분리. 강의: 역추론 가능 근거 확인. 창작: 출력이 같은 복수 입력을 남김.'),
candidate('ASK-C','문항','주장의 지지·반론을 새로운 진술로 검사',
 '주장을 그대로 반복한 선지와 실제 반박·지지 사례를 구분시키며, 참인 비교도 해당 논증의 증거로 유효한지 묻는다.',
 ['NN','AYF','AYG'],'비판 대상·지지하려는 명제가 구체적일 때.','비판 어조나 두 상황의 차이만으로 논증 관계를 인정할 때.',
 'NN③은 상대가 채택하지 않은 수정 한정을 공격한다. AYG②는 최적/비최적 차이를 부분 조건 개수의 비단조성 증거로 잘못 쓴다.',
 '교재: 주장-증거 적합성 활동. 강의: 실제 상대 명제 확인. 창작: 사실은 맞아도 증거 역할이 어긋난 선지 설계.'),
candidate('ASK-D','문항','입장과 범위를 유지한 내용 재서술',
 '선지에 주체·필요 조건·정도·동기·방향을 재배치해 본문이 허용한 해석 범위를 검사한다.',
 ['JN','NK','NL','YS','ATN','ATO'],'발화자와 범위 표현을 추적할 수 있을 때.','모든 내용 일치 문항을 하나의 구체 행동이라고 단정할 때.',
 'ATN③은 감소를 소멸로 확대하고 명시되지 않은 동기를 부여한다. NK는 차이뿐 아니라 공통 경험 시험을 요구한다.',
 '교재: 선지에서 바뀐 요소 표시. 강의: 주체·조건·정도 먼저 확인. 창작: 단순 낱말 치환 대신 의미 범위의 변경을 설계.'),
candidate('ASK-E','문항','개별 사실에서 전체 글의 연결 방식으로 초점 이동',
 '본문 사실의 참거짓을 넘어서 문단 사이 관계와 끝맺음의 기능을 전체 전개 설명에 대응시킨다.',
 ['YR'],'전체 전개 방식이 발문의 직접 대상일 때.','비판·사회·후속이라는 어휘가 한 번 나왔다는 이유로 전체 조직을 결정할 때.',
 'G157에 위협-효능감 모형이 존재하지만 YR은 모형을 집단에 대입하는 행동을 사용하지 않는다.',
 '교재: 문단 요약 뒤 관계 동사. 강의: 부분 내용과 전체 기능 분리. 창작: 동일 소재라도 다른 연결 구조를 설계.',status='한 문항 관찰·반복 미검증'),
candidate('ASK-F','문항','논증 내용과 별도로 문맥 어휘의 호환을 검사',
 '동사 교체가 문장의 의미 방향·목적어 결합·평가 어조를 보존하는지 판단하게 한다.',
 ['NO','YU'],'표시어를 실제 문장에 대체하는 문항일 때.','동일 지문에 속한다는 이유로 철학 논증·심리 모형 풀이와 같은 행동으로 묶을 때.',
 'NO의 결과 도달은 원인 귀속과 다르며 YU의 영향은 긍정적 보탬인 기여와 다르다.',
 '교재: 문맥 대입 비교. 강의: 조사·방향·평가 어조. 창작: 사전적 관련성과 문맥 호환의 차이를 이용.'),
candidate('ACT-A','풀이','정의의 입력 조건에 사례 역할을 대응',
 '명칭을 붙이기 전에 대상 상태·관찰자·구성 물질·공급원 등 입력 역할을 고정해 성립 조건과 일치시킨다.',
 ['JN','JO','RW','RY','AYF'],'역할과 성립 조건이 명시될 때.','함께 움직임·같은 소재·같은 국가 묶음을 직접 결합 또는 비용 방향의 증거로 사용할 때.',
 'AYF③은 A·B가 모두 C보다 비싸지만 A-B 서열은 없다. JO④는 크기 변화라는 표면 공통점만으로 결 기울기가 아니다.',
 '교재: 역할 표 작성. 강의: 입력 조건 먼저 확인. 창작: 역할 한 개를 달리한 경계 사례.'),
candidate('ACT-B','풀이','필요·가능·전체 범위를 검사',
 '가능한 사실에 필요성을 덧붙였는지, 일부를 전부로 넓혔는지, 모든 수정 경로를 닫았는지 확인한다.',
 ['JN','JO','NM','RV','ATN'],'선지에 반드시·못함·없음·전체 등의 강한 범위가 들어갈 때.','약한 가능성 진술까지 동일 반박으로 배제할 때.',
 'JN④는 두 눈이 도움될 가능성이 아닌 두 눈의 필요성을 주장한다. NM⑤는 다른 지식 수정으로 가설을 유지하는 길을 부정한다.',
 '교재: 범위 표현 밑줄. 강의: 최소 반례 구성. 창작: 강도를 바꾼 선지와 그 반례를 함께 검증.'),
candidate('ACT-C','풀이','의존하는 전제를 분해해 단일 원인 단정을 막음',
 '결과를 만드는 가설·배경·조건 또는 가정의 결합을 분해하고, 실패·우열 주장의 입력에서 빠진 전제를 찾는다.',
 ['NL','NM','AYE','AYG'],'결과가 여러 전제에 의존하거나 설명이 정의에 다시 의존할 때.','관련된 모든 문장을 형식 논리의 같은 종류 화살표로 합칠 때.',
 'NL의 정의 의존 순환과 NM의 경험적 예측 실패는 서로 다른 논증 행동이다. 공통점은 의존 입력 확인이며 두 하위 행동을 유지한다.',
 '교재: 정의 의존과 예측 전제를 별도 도식. 강의: 무엇이 빠졌는지 질문. 창작: 숨은 가정을 명시한 뒤 변경.'),
candidate('ACT-D','풀이','전수 조건표에서 역추론하고 미확정 값을 남김',
 '가능한 입력을 모두 나열한 표에서 출력과 맞는 행을 찾고 같은 출력인 행들의 차이는 확정하지 않는다.',
 ['YT'],'전수 입력과 규칙 부합이 보장될 때.','일반 조건문을 대우나 역으로 임의 전환하거나 출력에 숨은 원인이 있을 때.',
 'YT 집단1·2의 위협은 낮다고 알지만 효능감은 어느 집단이 높은지 정할 수 없다. NM 예측 실패로 가설 하나를 탓하는 것은 이 조건을 충족하지 않는다.',
 '교재: 결정 가능/불가능 칸. 강의: 전수성 검증. 창작: 동일 출력의 복수 입력을 의도적으로 구성.',status='한 문항 직접 관찰·반복 미검증'),
candidate('ACT-E','풀이','표시·현실·오류 및 조건부 분모를 분리',
 '보이는 신호, 검사의 판정, 실제 상태를 각각 적고 지표의 분모가 어느 실제 상태 집단인지 고정한다.',
 ['RV','RX','RY'],'검사 판정과 현실이 어긋날 수 있고 조건부 지표가 정의될 때.','정상 검사 신호를 현실 상태의 참 보증으로 보거나 분모가 다른 절대 건수를 비교할 때.',
 'RX는 분모 해석까지 가능하지만 선지 B열 누락이 번호 확정을 막는다. RV는 비율 계산 없이 검사선/표준선 기능만으로 판단할 수 있다.',
 '교재: 실제×판정 표와 신호 칸 분리. 강의: 분모를 먼저 말하기. 창작: 표본 크기·비율 명시.',status='한 지문 내 반복 관찰·비율 연산은 RX 한 문항'),
candidate('ACT-F','풀이','발화자·시점·대상과 평가를 분리',
 '누가 어떤 정책·사건을 언제 말하는지 먼저 복원하고, 같은 대상의 다른 평가와 같은 어휘의 다른 대상을 구분한다.',
 ['NK','YS','ATN','ATO','ATP'],'복수 입장과 인용·회고가 문항 근거일 때.','왕·반대자·사관의 말을 합쳐 전체 글의 단일 입장으로 만들 때.',
 'ATP의 작다/크다는 평가가 새/기존 대상과 연결된다. ATN의 찬성 사실은 군포 완전 면제 기대를 명시하지 않는다.',
 '교재: 화자·시점·대상·평가 표. 강의: 발화 귀속. 창작: 동일 지시의 평가 차이 및 상이 지시의 동어 반복 구성.'),
candidate('ACT-G','풀이','사실과 논증의 증거 역할을 별도로 검사',
 '진술이 참일 수 있는지와 그것이 지정된 주장의 지지·비판으로 기능하는지를 나누어 판정한다.',
 ['NN','AYF','AYG','ATO'],'지지 사례·비판·대안의 담화 기능이 발문의 대상일 때.','비판적인 말투·관련 소재·두 상황의 차이만 보고 기능을 인정할 때.',
 'ATO의 청묘법은 정책 대안이 아니라 반대 유추다. AYG②는 최적 대비라는 차이가 핵심 비단조성의 증거가 되지 않는다.',
 '교재: 참인 사실이지만 관련 없는 증거 활동. 강의: 목표 주장 명시. 창작: 사실 일치와 증거 적합성이 갈라지는 사례.'),
candidate('ACT-H','풀이','비교 방향을 확정하되 정보 부족은 남김',
 '거리-속도·비용·위협-반응·변화량의 방향을 추적하고 주어진 비교로 결정되지 않는 순서·동기를 보류한다.',
 ['JO','RX','YT','AYF','ATN'],'비교 지표와 방향은 주어지지만 일부 연결 정보가 부족할 때.','누락 선지를 정답 기억으로 복원하거나 간접 서열에서 없는 직접 서열을 만들어 낼 때.',
 'AYF③의 A-B 비용, YT 집단1·2 효능감, RX④/⑤ B열은 각각 다른 이유로 미확정이다. 논리적 미확정과 원문 결손은 분리해서 기록한다.',
 '교재: 부족한 정보 적기. 강의: 보류 이유 분류. 창작: 불완전 정보 오답은 완전한 정답 선지와 구별되게 설계.'),
candidate('ACT-I','풀이','문맥 대입으로 의미 방향·논항·어조를 보존',
 '교체 어휘를 문장에 넣고 도착/원인 방향, 목적어와 조사, 중립/긍정 평가가 유지되는지 확인한다.',
 ['NO','YU'],'문맥상 어휘 호환을 직접 묻는 경우.','사전상 관련어라는 이유로 모든 문장에 동일 교체가 된다고 볼 때.',
 '기인한다는 도달한다의 방향을 보존하지 않고 기여는 아무 영향을 주지의 중립 의미와 결합을 보존하지 않는다.',
 '교재: 실제 문장 대입. 강의: 방향·조사·어조. 창작: 문맥 기능이 달라지는 관련어 선지.'),
candidate('ACT-J','풀이','국소 사실과 전체 조직의 판단 수준을 맞춤',
 '문단에 등장한 내용과 문단 사이 관계·전체 결론의 기능을 구분하여 발문이 요구한 수준만 판단한다.',
 ['YR','AYG'],'전체 전개 또는 사례의 주장 지지 기능을 묻는 경우.','본문의 복잡한 모형을 모든 문항에서 반드시 계산해야 한다고 볼 때.',
 'YR은 위티의 조건표를 사용하지 않는다. AYG의 표 판독은 필요하지만 그 다음에 비교의 논증 역할을 따로 검사한다.',
 '교재: 문항별 실제 사용 표시. 강의: 읽을 정보와 답을 가르는 정보 구분. 창작: 같은 지문에서 국소·전체 질문을 달리 설계.')
]
for c in candidates:
    c['count_warning']='후보 사례는 서로 중복될 수 있다. 해당 수는 빈도·배타적 분류·학습 효과의 측정값이 아니다.'
dump('independent_candidates.json',{'stage':'1단계·기존 체계 미대조', 'candidate_count':len(candidates),'candidates':candidates,
     'induction_note':'기존 정의·분류를 읽지 않고 이번 원문과 직접 작성한 풀이만 귀납. 유사한 후보는 분석 단위가 다르므로 연결하고, 풀이 후보 내부에서도 필요한 하위 행동을 보존함.'})

md=['# 문항별 독립 풀이 기록','', '공식 정답·기존 풀이·기존 패턴과 대조하지 않은 선택이다. RX는 선택 번호를 보류했다. G095는 과거 노출 이력으로 별도 집계한다.','']
for g in groups:
    p=g['passage_analysis'];md += ['## '+g['passage_group'],'',p['organization'],'', '실제 미활용 특징: '+' / '.join(p['features_present_but_not_required']),'']
    for a in g['questions']:
        case=a['case_id'];md += ['### '+case,'',f"독립 선택: {a['independent_answer'] if a['independent_answer'] is not None else '번호 보류'} · 확신: {a['confidence']} · {a['historical_exposure']}",'',a['question_design'],'']
        md += [str(i+1)+'. '+step for i,step in enumerate(a['reasoning_steps'])]+['']
        md += ['|선지|판단|구체 근거와 사고|','|---|---|---|']
        for o in a['option_judgments']:md += [f"|{o['option']}|{o['statement_status']}|{o['specific_reason']} ({', '.join(o['evidence_ids'])})|"]
        md += ['', '반복 행동: '+a['repeatable_action'],'','적용 조건: '+a['applicable_when'],'','금지 조건: '+a['do_not_apply_when'],'','대안 경로: '+' / '.join(a['alternative_routes']),'','제작 활용: '+a['production_implications'],'']
        if a['hold_reason']:md += ['보류 사유: '+a['hold_reason'],'']
(RUN/'문항별_독립풀이.md').write_text('\n'.join(md)+'\n')

md=['# 독립 후보 목록','','20개 후보: 지문 4, 문항 6, 풀이 10. 범주는 배타적이지 않으며 개수 자체를 연구 성과로 보지 않는다. 원문 특징과 문항의 실제 활용을 분리했다. 기존 체계와 의미상 겹칠 수 있으나 이번 단계에서는 비교하지 않는다.','']
for c in candidates:
    md += ['## '+c['candidate_id']+' · '+c['name'],'',c['unit']+' / '+c['status'],'',c['definition'],'','실제 사례: '+', '.join(c['cases']),'','적용: '+c['applicable_when'],'','제외: '+c['do_not_apply_when'],'','표본 경계·반례: '+c['sample_boundary_or_counterexample'],'','활용: '+c['applications'],'']
(RUN/'독립후보_목록.md').write_text('\n'.join(md)+'\n')

(RUN/'활용가능성_잠정분석.md').write_text('''# 교재·강의·창작 활용의 잠정 분석

원문에서 확인한 판단 행동을 학습 활동으로 바꾸는 제안이다. 학습 효과, 난도 조절 효과, 문항 타당도를 실제 학생 집단에서 검증한 결과는 아니다. 새 지문이나 문항은 제작하지 않았다.

|목적|잠정 활용 원리|근거 장면|조건·한계|
|---|---|---|---|
|교재의 읽기 활동|개념 이름 뒤에 성립 입력·배제 조건·사례 역할을 적게 한다.|JO, RW, RY, AYF|단순 유사어 찾기가 되지 않도록 누가 무엇을 언제 하는지를 포함한다.|
|교재의 문항 분석|지문 특징 목록 옆에 실제 선지 판정에 사용한 근거만 표시한다.|JN/JO, YR/YT, RV/RX|각도 정의·동호회 예시·나노 입자 이름의 존재를 모든 문항의 활용으로 세지 않는다.|
|강의의 비교 활동|화자·시점·지시 대상·평가를 따로 복원한다.|NK, YS, ATN, ATO, ATP|같은 대상의 다른 평가와 같은 어휘의 다른 지시를 나눈다.|
|강의의 조건 추론|순방향 적용과 전수 표를 통한 역추론을 나눈다.|JO, NM, YT|YT는 전수 조합·규칙 부합이 있고 NM은 실패 원인이 격리되지 않는다. 두 역추론을 하나로 지도하지 않는다.|
|강의의 논증 평가|진술의 참 가능성과 주장에 대한 증거 적합성을 별도로 확인한다.|NN, AYF, AYG|최적/비최적의 차이는 부분 조건 개수의 비단조성 증거가 아니다.|
|교재의 수치·판정 활동|보이는 표시, 판정, 실제 상태, 조건부 분모를 나눈다.|RV, RX, RY|RX의 번호는 원문 결손으로 보류되어 객관식 정답 예시로 사용하면 안 된다.|
|창작 설계 원리|역할·필요 조건·범위 중 하나를 바꾼 오답과 그 반례를 함께 설계한다.|JN, JO, RW, ATN|단순 표현 변형으로 오답이라고 간주하지 말고 조건 충돌을 확인한다.|
|창작 설계 원리|비교 정보가 충분한 사례와 불충분한 사례를 구분한다.|AYF②/③, YT 집단1·2|미확정 대상과 이유를 명시한다. 원문 누락인 RX와 논리적 미확정은 구별한다.|
|창작 설계 원리|본문의 동일 소재로 서로 다른 판단 수준을 요구하는 문항을 설계할 수 있다.|YR/YS/YT/YU, NK/NL/NM/NN/NO|내용 문항과 어휘 문항을 같은 행동으로 강제 분류하지 않는다.|

우선 교재에는 역할 대응·범위 검사·근거의 증거 적합성·보류 이유 표시의 네 활동을 작게 도입하는 것이 관찰 근거와 가장 가깝다. 조건표 역추론과 조건부 비율은 직접 사례가 각각 한 문항이므로 범용 핵심 행동으로 확정하기 전에 다른 지문에서 추가 독립 관찰이 필요하다. 정책의 오류 비용을 고려한 지표 선택은 RY 한 문항에 국한되어 별도의 반복 검증이 필요하다.

분류 체계는 텍스트 조직, 문항 변형, 실제 풀이 행동을 연결하는 자료 구조로 사용한다. 풀이가 짧은 직접 반박 경로와 전체 선지 검증 경로로 나뉘는 경우 둘을 보존한다. 하나의 정형 절차를 모든 학생에게 강요하면 원문이 허용한 효율적인 풀이를 지울 수 있다.
''')

summary={'passage_groups':6,'questions_analyzed':len(questions),'selected_answers':sum(a['independent_answer'] is not None for a in questions),
         'held_cases':[a['case_id'] for a in questions if a['independent_answer'] is None],
         'within_session_no_answer_or_pattern_values_viewed':21,'strict_unexposed_candidates':16,
         'historically_exposed_cases':['NK','NL','NM','NN','NO'],
         'strict_unexposed_selected':15,'strict_unexposed_held':1,
         'option_scenes':105,'holistic_scenes':21,'evidence_anchors':len(evidence),'evidence_links':len(links),
         'candidate_counts':{'지문':4,'문항':6,'풀이':10},'official_answers_checked':0,'codebook_comparisons':0,
         'all_candidates_provisional':True,'blind_absolute_guarantee':False,
         'source_completeness_issues':['RX: B열 전체 누락', 'G350: 시각자료 blind 전사 사용·원본 이미지 미대조·일부 텍스트 표지 누락'],
         'holds_preserved':['G024','G370'],'other_models_called':False,'new_passages_created':False,'git_push':False}
dump('analysis_summary.json',summary)
print(json.dumps(summary,ensure_ascii=False,indent=2))
