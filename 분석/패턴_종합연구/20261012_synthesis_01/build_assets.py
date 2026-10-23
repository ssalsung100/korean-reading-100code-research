"""작업 C의 출처 인덱스·대응표 생성. 입력은 읽기 전용이며 전수 재분류하지 않는다."""
from pathlib import Path
import json, hashlib, collections

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BASE = ROOT / '분석/패턴_종합연구'
PILOT = BASE / '20261009_pilot_01'
APP = BASE / '20261010_application_01'
BOOK = BASE / '20261010_codebook_v0_2_01'
SOL = BASE / '20261010_sol_independent_stage1_01'
EXT = BASE / '20261010_codebook_external_application_01'

def read(p): return json.loads(p.read_text())
def rows(p): return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def rel(p): return str(p.relative_to(ROOT))
def dump(name, x): (OUT/name).write_text(json.dumps(x, ensure_ascii=False, indent=2)+'\n')
def jsonl(name, xs): (OUT/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in xs))
def ref(p, **kw): return {'path': rel(p), **kw}

manifest = read(PILOT/'sample_manifest.json')['samples']
events = rows(APP/'revised_events.jsonl')
exts = rows(EXT/'case_annotations.jsonl')
sols = rows(SOL/'independent_solutions.jsonl')
links = rows(EXT/'evidence_links.jsonl')
cases = {c:s for s in manifest for c in s['case_ids']}
answer_records = collections.defaultdict(list)
rawpath = ROOT/'data/기본기_연구/astra_handoff_queue.jsonl'
for line, s in enumerate(rawpath.open(), 1):
    d=json.loads(s)
    if d.get('case') in cases and d.get('stage')=='answer_check':
        answer_records[d['case']].append(ref(rawpath,line_1_based=line,record_id=d['record_id'],payload=d['payload']))

registry=[]
for case,s in cases.items():
    p=ROOT/f'data/기본기_연구/prepared_backlog/blind_sources/{case}.json'
    d=read(p)
    registry.append({
        'case_id':case,'passage_group':s['passage_group'],'passage_id':s['passage_id'],
        'identity_family':s['identity_family'],'question_id_from_manifest':s['question_ids'][s['case_ids'].index(case)],
        'exam_family':s['exam_family'],'academic_year':s['academic_year'],'sample_split':s['split'],
        'source':ref(p,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),passage_pointer='/passage_text',stem_pointer='/stem',choices_pointer='/choices',provenance=d.get('provenance')),
        'previous_application_events':[ref(APP/'revised_events.jsonl',line_1_based=i,event_id=e['event_id']) for i,e in enumerate(events,1) if e['case_id']==case],
        'sol_stage1':[ref(SOL/'independent_solutions.jsonl',line_1_based=i) for i,e in enumerate(sols,1) if e.get('case_id')==case],
        'external_application':[ref(EXT/'case_annotations.jsonl',line_1_based=i) for i,e in enumerate(exts,1) if e.get('case_id')==case],
        'external_exact_evidence':[ref(EXT/'evidence_links.jsonl',line_1_based=i,evidence_id=e['evidence_id']) for i,e in enumerate(links,1) if e.get('case_context')==case],
        'official_answer_history_reused':answer_records[case],
        'source_qualification':'기존 기출 연결 로컬 전사 및 기존 답 대조 승계. 작업 C에서 원 배포 지면·공식 정답표를 새로 전수 검수하지 않음.',
        'current_analysis_condition':'기존 분석 공개 후 심층 종합; 독립 blind 발견 실험 아님',
        'special_history':('G095 과거 정답·코드 노출. 세션별 미열람을 과거 미노출로 바꾸지 않음.' if s['passage_group']=='G095' else 'RX: 9월 결손/복원/보조 작업자 답필드 노출, Sol B열 미사용·번호보류, 외부적용 보강표 사용을 별도 보존.' if case=='RX' else 'G350: Sol 전사 사용과 외부적용 공식 이미지 확인 이력 구별.' if s['passage_group']=='G350' else None)
    })
jsonl('case_registry.jsonl',registry)

anchors=[]
for i,e in enumerate(events,1):
    for a in e.get('original_evidence_reused',[]) + ([e['passage_support']] if 'passage_support' in e else []):
        p=ROOT/e['source_path'];d=read(p);ptr=a['json_pointer'];txt=d[ptr.lstrip('/')];q=a['quote'];start=txt.find(q)
        assert start>=0,(e['event_id'],q)
        anchors.append({'evidence_id':f"C-{e['event_id']}-{len(anchors)+1}",'case_id':e['case_id'],'source_path':str(p.relative_to(ROOT)),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'json_pointer':ptr,'char_start':start,'char_end_exclusive':start+len(q),'exact_quote':q,'inherited_reference':ref(APP/'revised_events.jsonl',line_1_based=i,event_id=e['event_id']),'verification':'기존 인용의 문자 일치를 재검사; 의미상 충분성은 사례집의 중간 추론 참조'})
jsonl('evidence_anchors.jsonl',anchors)

counts={}
for split in ['discovery','validation']:
    counts[split]={}
    for family in ['KICE','LEET','MEET']:
        ss=[s for s in manifest if s['split']==split and s['exam_family']==family]
        counts[split][family]={'passages':len({s['identity_family'] for s in ss}),'questions':len({c for s in ss for c in s['case_ids']})}
dump('sample_accounting.json',{'scope':'기존 목적 표본만; 새 코퍼스 재분류 아님','by_original_split_and_exam':counts,'unique_passages':len({s['identity_family'] for s in manifest}),'unique_questions':len(cases),'independent_analysis_runs_are_not_new_cases':True,'corpus_prevalence':None})

md=['# 출처·분석 조건 인덱스','', '문항별 JSONL 좌표, 원문 경로·SHA-256·JSON pointer, 기존 정답 대조 record_id는 [case_registry.jsonl](case_registry.jsonl)에 있다. 아래 line은 그 인덱스의 행이다. 시험 표기는 기존 공통 manifest를 승계했다.','', '|case|시험 문항 식별자|원문|C 인덱스 행|기존 분석|','|---|---|---|---:|---|']
for i,r in enumerate(registry,1):
    prev=', '.join(e.get('event_id','') for e in r['previous_application_events']) or 'Sol 1단계 / 외부 적용'
    md.append(f"|{r['case_id']}|{r['question_id_from_manifest']}|[전사](../../../{r['source']['path']})|{i}|{prev}|")
(OUT/'00_출처와_분석조건.md').write_text('\n'.join(md)+'\n')

# 각 줄은 하나의 입력 후보. 화살표는 분류층을 구분한 대응이며 후보 개수의 합산표가 아니다.
maptext='''P01|부분 중첩|ACT-A·ACT-F; N01·N10·N11|AG BI AJQ ANW AQP JN RY ATN|이미 있는 술어의 담당자 복원은 유지. 정의 적용·새 동기 추가·지시 해소까지 한 연산으로 통합하지 않음.
P02|하위 유형|ACT-F 일부; ACT-E 일부; S05|AB OZ PA NK RV YS AJP|동일 질문끼리 비교하는 상위 원리. 규범/실행은 현 표본에서 특수 축으로 편입하되 규범 효력 판정은 별도 보존.
P03|하위 유형|ACT-H 일부; N05; R10|AC AD CA JO RX AYF|역순·연쇄·상대비·조건부 분모를 하위 조작으로 보존. 비교 정보 결손과 단조법칙 결손을 구분.
P04|부분 중첩|ACT-A·ACT-B·ACT-C 일부; N03|AA BK GM JN NM RV YS|경로 필요조건 검사 유지. 불필요 조건 추가와 실패 원인의 역추론은 분리.
P05|동일 원리|ACT-I; ASK-F는 문항층|AJ BL CB NO YU ZE ZF|문맥의 논항·방향·평가 성분을 보존하는 치환. ZE는 설명만, ZF는 보조 활용.
P06|근거 부족|N06; ACT-G의 목적 관련 일부|ANX AQO RY ATO|문제-수단 연결 상위 질문 유지. RY 오류 비용은 잠정 확장이고 ATO의 기존 대안 회수는 새 대책 적합성 판단과 분리.
P07|부분 중첩|ACT-F 일부; TXT-B 일부; N11|BZ GL ANV RW ATP NL|처리 잔존 상태·기전 선후·역사 배치를 유지. 정의 의존 순환은 제외. 지시 복원은 추가 연산.
S01|부분 중첩|ACT-B; N07·N08의 경계|AI YT AYE|입력 차이가 출력 차이를 보장하지 않는다는 상위 연결만 인정. 개인별 조건화·모형 역상·효율 비단조는 별도 연산.
S02|하위 유형|N04의 관측 판별 하위형|GK AYF NN|논증 역할 검사 아래 관측형으로 배치. 가상 반례 AYF와 같아졌다고 계수하지 않음.
S03|동일 원리|ASK-E; ACT-J의 YR 부분|OX YR AVS AYG|문단 기능과 선지 동작 대응은 OX/YR에서 반복. ACT-J 전체와의 동일성은 인정하지 않음.
S04|부분 중첩|ACT-D; N07|ZF YT RX|후보 집합을 보존하는 상위 연결. 복수/무적합 원인 구별과 전수 규칙 역상은 분리. 원문 결손은 바깥.
S05|하위 유형|P02의 규범-실행 축|AJP AB|현 AJP②는 규정 존재와 실행 두 질문으로 충분. 예외·효력·적용 범위가 쟁점인 새 사례에서는 별도 규범 연산 필요.
S06|부분 중첩|ACT-F; N11|AQN ATP ANV|집단 연속성 증거와 표현의 지시 해소를 구별. 이름 다름으로 집단 다름을 확정하지 않음.
TXT-A|별개의 원리|지문층 T1; N01·P04에 입력 제공|JN JO RV RW RY|분류→성립 조건→구체 사례의 제시 방식. 풀이 행동과 같은 후보로 합치지 않음.
TXT-B|별개의 원리|지문층 T2; P07·N05·N06|RV RW RX RY|장치 구조→결합→신호→판정→오류율의 층 이동. 동일 지문 내부 반복으로 한정.
TXT-C|별개의 원리|지문층 T3; P02·N02·N03·S03·N04|NK NL NN YR YS AYE AYG OX|이전 주장 유지/변경/비판/종합의 관계망. 시간표만으로 치환하지 않음.
TXT-D|하위 유형|지문층 T4 다중 발화; ACT-F·N11|ATN ATO ATP|정책 제안·반대·대안·회고의 복수 목소리. 논쟁형 조직의 역사 서술 하위형이나 반복성은 단일 지문.
ASK-A|부분 중첩|문항 조작 M1; P01·N01·N11|JO RV RW RY ATP|역할 교환과 성립 조건 삭제와 지시 대상 변경을 각각 기록. 표면 유사성은 공통 동기이지 동일 연산이 아님.
ASK-B|부분 중첩|문항 조작 M2; N01·P04·N03·N07|JO NM RY YT|새 사례 적용과 결과에서 조건 복원은 방향이 다르므로 분기.
ASK-C|부분 중첩|문항 조작 M3; N04|NN AYF AYG|반론·지지의 요구를 만드는 설계층. 학생 연산 ACT-G와 연결하되 후보 중복 계수 금지.
ASK-D|근거 부족|문항 조작 M1·M4·M5|JN NK NL YS ATN ATO|재서술은 너무 넓어 단일 풀이 원리로 확정 불가. 주체·범위·강도·동기·방향 변경을 원자 분해.
ASK-E|하위 유형|문항 조작 M6; S03|YR OX|전개 기능 대응을 요구하는 문항층. 전체 조직을 묻는 다른 모든 문항으로 자동 일반화하지 않음.
ASK-F|하위 유형|문항 조작 M7; P05·ACT-I|NO YU|문맥 치환 요구. 논증 내용 풀이와 별도 장면으로 보존.
ACT-A|부분 중첩|N01·P01·P04·P03|JN JO RW RY AYF|정의 조건을 새 사례에 대응하는 핵심 N01과 이미 정해진 귀속 복원, 비용 비교를 나눔.
ACT-B|부분 중첩|N09·P04·N03|JN JO NM RV ATN|양화·강도 점검은 공통 점검 행동. 필요조건 추가·모든 수정경로 부정·국소→전체 확대는 하위 차이 유지.
ACT-C|부분 중첩|N02·N03·P04·N08|NL NM AYE AYG|의존 입력 확인이라는 상위 질문 아래 정의 순환과 결합 예측을 분리. 조건 개수→효율은 추가 법칙의 문제.
ACT-D|동일 원리|N07·R08|YT|전수 조건표에서 출력의 역상을 계산하고 공통 성분만 확정. 단일 지문 반복 미검증.
ACT-E|부분 중첩|P02·N05·신호 해석 결합|RV RX RY|신호·판정·현실 분리와 조건부 분모는 별도 단계. 비율 없는 RV를 분모 연산 반복으로 세지 않음.
ACT-F|부분 중첩|P01·P02·P07·N11|NK YS ATN ATO ATP|화자 귀속, 시점 배치, 지시 복원, 평가 축을 분해. 한 표에 적을 수 있다고 같은 연산은 아님.
ACT-G|부분 중첩|N04·S02|NN AYF AYG ATO GK|실제 주장 충돌·판별 증거·담화 기능 세 하위형을 보존. 내용 참과 요구 역할 적합성을 분리.
ACT-H|부분 중첩|P03·N07·N08; 자료 상태|JO RX YT AYF ATN|정성 비교·부분 순서·역상·동기 미확정·소스 결손을 별개 이유로 보존. 모두 하나의 비교 패턴이 아님.
ACT-I|동일 원리|P05.lexical_comparison|NO YU AJ BL CB|문맥 대입의 입력·조작·결론이 동일. 방향·논항·평가 어조는 진단 요소로 추가.
ACT-J|부분 중첩|S03·N04; 판단 단위 점검|YR AYG|YR은 문단 기능, AYG는 증거 역할이다. 판단 수준을 맞추라는 메타 점검은 공유하나 실제 연산은 별개.
R01|동일 원리|N01; ACT-A 핵심|JN JO|대상 수·역할·동시성을 보존하는 정의 적용. N01의 KICE 대표 근거.
R02|별개의 원리|N02; ACT-C의 정의 분기|NL|정당화 의존의 순환은 기존 13카드에 없는 연산으로 보존. 한 문항과 G095 노출 제한 유지.
R03|별개의 원리|N03; ACT-C의 예측 분기|NM NK|필요 전제 찾기 다음의 실패 원인 비식별. P04의 단순 확장으로 소거하지 않음.
R04|부분 중첩|N04; ACT-G; S02|NN AYF AYG ATO GK|상위 목적 연결은 같지만 반론·반례 지지·경고/제안 구별을 분리해 보존.
R05|부분 중첩|P01·P02·P04·P07의 결합|RV RW RY|방식별 신호 해독은 복합 경로. 독립 원자 코드 승격 유보.
R06|하위 유형|N05; P03의 조건부 분모|RX|같은 조건 집합 내부의 여집합 비율 비교. 다른 표본 건수 비교는 비적용.
R07|근거 부족|N06; P06 잠정 확장|RY|후속 확인에서 제외되는 위음성과 추가 확인으로 이어지는 위양성의 경로 차이. 독립 반복과 비용 정량화 미확보.
R08|동일 원리|N07; ACT-D|YT YS|YT의 역상 조작에 한해 동일. YS 순방향 조건 대입은 별도 보조·경계.
R09|부분 중첩|N08; P03의 비적용 조건|AYE AYG BJ|불완전 최적 조건의 수는 효율 순서를 보장하지 않음. 문턱 사례와 상위 점검만 공유.
R10|하위 유형|P03의 부분 순서 미확정 경계|AYF|A>C 및 B>C로 A/B 서열을 만들 수 없음. 새 원자 후보를 중복 생성하지 않음.
R11a|하위 유형|N09; ACT-B|ATN BK|일부 변화→전부 소멸의 과잉 강도. 총량 불명과 실제 잔여값을 구분.
R11b|부분 중첩|N10; P01.evaluation_target 경계|ATN AVT AQP|행동에 제시되지 않은 동기·심리 성분 추가. 단항 귀속 교환과 분리하며 세 사례의 같은 심리 연산 여부는 유보.
R12|부분 중첩|N11; ACT-F·P07·S06|ATP AQN|어휘 뜻과 지시 대상을 분리. 역사 배치는 수단, 지시 해소는 별도 목표. 집단 동일성은 다른 하위형.''' 

book={x['pattern_id']:x for x in read(BOOK/'codebook_v0.2.json')['cards']}
sol={x['candidate_id']:x for x in read(SOL/'independent_candidates.json')['candidates']}
mapping=[]
for line in maptext.splitlines():
    cid,relation,target,cs,why=line.split('|')
    origin='Astra 코드북' if cid in book else 'Sol 독립 1단계' if cid in sol else '코드북 외부 적용 잔여'
    name=book[cid]['name'] if cid in book else sol[cid]['name'] if cid in sol else cid
    path=BOOK/'codebook_v0.2.json' if cid in book else SOL/'independent_candidates.json' if cid in sol else EXT/'pattern_residuals.md'
    pointer=('/cards/'+str(list(book).index(cid))) if cid in book else ('/candidates/'+str(list(sol).index(cid))) if cid in sol else None
    mapping.append({'candidate_id':cid,'name':name,'origin':origin,'candidate_source':ref(path,json_pointer=pointer,section=None if pointer else cid),'relation':relation,'target':target,'case_ids':cs.split(),'decision':why,'new_judgment':True,'scope':'현재 기출 장면의 종합 판단; 학습 전이 실증 아님'})
assert len(mapping)==46 and len({m['candidate_id'] for m in mapping})==46
jsonl('candidate_correspondence.jsonl',mapping)
md=['# 기존 후보와 잔여의 근거 기반 대응표','','13개 코드북·20개 Sol 후보·13개 잔여 행(R11을 a/b로 분리)의 출처를 모두 보존했다. 46은 입력 목록의 행 수이며 새 패턴 수가 아니다. 표의 동일성은 명시한 부분·장면에 한정된다. 지문층·문항층·풀이층 관계를 같은 종류의 통합으로 해석하지 않는다.','','관계: **동일 원리**는 입력·중간 연산·결론 제약이 같다. **하위 유형**은 상위 조건에 추가 조건을 붙인 경우다. **부분 중첩**은 공유 단계가 있으나 잔여 연산이 다르다. **별개의 원리**는 간선 의미 또는 판단 단위가 달라 서로 대체할 수 없다. **근거 부족**은 현 자료만으로 통합·반복성을 확정할 수 없다. N 식별자는 잠정 신설·확장 후보이며 [계층과 조건](03_패턴계층과_적용조건.md)에서 정의한다.','','|입력|관계|대응|기출 근거|판단|','|---|---|---|---|---|']
for m in mapping: md.append('|'+ '|'.join([m['candidate_id'],m['relation'],m['target'],' · '.join(m['case_ids']),m['decision']])+'|')
md+=['','출처의 정확한 JSON pointer는 [대응 원장](candidate_correspondence.jsonl), 문항별 시험·전사·분석 좌표는 [출처 인덱스](00_출처와_분석조건.md)를 따른다. 원본 R11은 외부 JSON에서 하나의 ID이지만 잔여 보고서는 두 오류를 분리했다. 본 표는 두 하위 ID의 출처를 R11과 함께 보존한다.']
(OUT/'01_후보대응표.md').write_text('\n'.join(md)+'\n')

dump('run_metadata.json',{'run_id':'20261012_synthesis_01','task':'작업 C: 기존 표본 심층 종합','requested_model':'GPT-6 Astra','requested_reasoning_effort':'high','runtime_exact_model_id':None,'runtime_effort_verified':False,'runtime_note':'현재 세션은 시스템상 GPT-6 기반 Codex. API 세부 모델·effort의 독립 확인 수단은 사용하지 못함. 모델 설정 준수를 검증했다고 주장하지 않음.','other_models_called':False,'new_blind_research':False,'new_corpus_classification':False,'original_files_edited':False,'git_push':False,'shared_queue_modified':False,'persistence':'이 폴더의 decision_raw.jsonl 및 종합 파일. 원 연구 queue/processed/CURRENT는 보존.','semantic_review':'주 세션의 직접 종합. 제2평가자 없음.'})
print(json.dumps({'cases':len(registry),'anchors':len(anchors),'candidate_rows':len(mapping),'counts':counts},ensure_ascii=False))
