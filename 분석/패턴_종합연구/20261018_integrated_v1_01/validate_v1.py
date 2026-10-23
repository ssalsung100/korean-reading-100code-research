"""새 산출물의 국소 무결성·연결 및 카드 명시 모형만 검사한다."""
from pathlib import Path
import json, re, hashlib, itertools, collections
from urllib.parse import unquote
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
BASE=ROOT/'분석/패턴_종합연구'
SRC=BASE/'20261016_integrated_research_01'
errors=[];passed=[]
def readj(p): return json.loads(p.read_text())
def rows(p): return [json.loads(s) for s in p.read_text().splitlines() if s.strip()]
def check(ok,label):
    (passed if ok else errors).append(label)
def dump(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

required=['연구원리체계_v1.md','원리계층과관계.json','판단장면_원리연결.jsonl','대표경계사례_인덱스.md','미분류와후속검토.md','교재학습단위_v1.md','강의설계원칙_v1.md','출제설계원칙_v1.md','다중AI_출제입력카드.md','연구자관점_반영방법.md','v1_검증범위와사용제한.md','README.md']
check(all((OUT/n).is_file() and (OUT/n).stat().st_size>100 for n in required),'필수12파일의 비어 있지 않은 저장')
json_counts={}
for f in OUT.iterdir():
    if f.suffix not in ['.json','.jsonl']:continue
    try:
        d=rows(f) if f.suffix=='.jsonl' else readj(f)
        json_counts[f.name]=len(d) if isinstance(d,list) else '객체'
    except Exception as e:errors.append(f'{f.name}: {e}')
check(not errors,'현재 JSON/JSONL 구문 파싱')
graph=readj(OUT/'원리계층과관계.json');nodes=graph['principles'];pids={p['principle_id'] for p in nodes}
original_p={p['principle_id']:p for p in rows(SRC/'principles_current.jsonl')}
check(len(nodes)==len(pids)==63 and pids==set(original_p),'63원리 ID 집합 일치·비중복')
check(all(n['definition']==original_p[n['principle_id']]['definition'] and n['limits']==original_p[n['principle_id']]['limits'] and n['integration_status_v1']==original_p[n['principle_id']]['integration_status_v1'] for n in nodes),'기존 정의·한계·상태의 보존')
fields=['required_inputs','trigger','decisive_intermediate_inference','result','application_conditions','non_application_and_boundaries','representative_sources','v1_relation_ids']
check(all(n.get(k) for n in nodes for k in fields),'63원리의 실행 필드·대표 출처·관계 공란 없음')
check(all(e['from'] in pids and e['to'] in pids for e in graph['relations']),'원리 관계 끝점 유효')
dids={d['decision_id'] for d in rows(SRC/'integration_decisions.jsonl')}
check(all(d in dids for e in graph['relations'] for d in e['evidence_decision_ids']),'52관계의 기존 결정 참조 유효')
members=[p for g in graph['organizers'] for p in g['members']]
check(len(members)==63 and set(members)==pids,'7상위 조직의63원리 비중복 소속')

mapping=rows(OUT/'판단장면_원리연결.jsonl');eids={x['event_id'] for x in mapping}
source_files=list((BASE/'20261012_corpus_sweep_01').glob('batch_*_scenes.jsonl'))+[BASE/'20261012_question_backfill_01/new_judgment_scenes.jsonl']
old_ids={x['event_id'] for f in source_files for x in rows(f)}
check(len(mapping)==len(eids)==2202 and eids==old_ids,'원2202장면 집합 정확 일치·누락/중복 없음')
check(len({x['source']['unique_question'] for x in mapping})==1667,'고유1667문항 유지')
check(all(l['principle_id'] in pids for x in mapping for l in x['principle_links']),'장면의 원리 참조 유효')
check(all((ROOT/x['source']['source_path']).is_file() and (ROOT/x['source_record']['path']).is_file() for x in mapping),'2202장면의 원문·장면 원본 경로 존재; 내용 전수 재검증 아님')
direct=rows(OUT/'대표대조_검토기록.jsonl');rids={r['review_id'] for r in direct}
prior={e for r in rows(SRC/'source_registry.jsonl') for e in r.get('compared_event_ids',[])}
check(len(direct)==len(rids)==21 and {r['event_id'] for r in direct}<=prior,'직접21장면은 기존191의 부분집합·신규 표본 아님')
check(all(x['current_v1_review_id'] in rids for x in mapping if x['current_v1_review_id']),'직접검토 기록 참조 유효')
check(all(l['verification'] in ['M0','I1','V2'] and l.get('role') for x in mapping for l in x['principle_links']),'장면 연결의 검증 등급·역할 분리')
unmapped=rows(OUT/'미분류장면_후속목록.jsonl')
check(len(unmapped)==215 and {x['event_id'] for x in unmapped}=={x['event_id'] for x in mapping if not x['principle_links']},'215미연결 장면의 후속 목록 정확 일치')
cs=rows(OUT/'기존후보_보존연결.jsonl');old_cs=rows(SRC/'기존후보_통합상태표.jsonl')
check(len(cs)==112 and all(all(c.get(k)==old.get(k) for k in old) for c,old in zip(cs,old_cs)),'112후보의 모든 기존 필드 보존')
effects=rows(OUT/'출제변형효과_300건_분류.jsonl');old_effects=rows(SRC/'production_effects.jsonl');fxids={r['effect_id'] for r in effects}
check(len(effects)==len(fxids)==300 and all(e['original']==o for e,o in zip(effects,old_effects)),'300효과 비중복·원효과 모든 필드 보존')
check(all(len(e['axes'])==5 and e['required_information_relation'] for e in effects),'300효과의5축과 필요한 관계 공란 없음')
cards=readj(OUT/'다중AI_출제입력카드.json')['cards']
check(len(cards)>=3 and len({c['card_id'] for c in cards})==len(cards),'서로 다른 제작 카드4종 저장')
card_fields=['operation','boundary','new_subject_conditions','independent_exposition','information_design','paragraph_progression','item_inferences','distractor_operations','truth_and_effects','logical_constraints','anti_copy','unverified']
check(all(c.get(k) for c in cards for k in card_fields),'제작 카드의 필수 내용 공란 없음')
check(all(p in pids for c in cards for p in c['principle_ids']),'카드 원리 참조 유효')
check(all(e in eids for c in cards for e in c['evidence']['event_ids']),'카드 장면 참조 유효')
check(all(d in dids for c in cards for d in c['evidence']['decision_ids']),'카드 기존 결정 참조 유효')
check(all(e in fxids for c in cards for e in c['evidence']['effect_ids']),'카드 효과 참조 유효')
check(all(r in rids for c in cards for r in c['evidence']['review_ids']),'카드 직접검토 참조 유효')
text=(OUT/'교재학습단위_v1.md').read_text()
check(len(re.findall(r'^## LU\d+',text,re.M))==12,'잠정 학습 단위12개')
check(set(re.findall(r'P\d{3}',text))>={p[3:] for p in pids},'교육 단위에63원리 전부 연결; 교육 효과 검증 아님')

# 카드의 설계 가정만 확인하는 좁은 수학 검산.
solutions=[(a,b,c) for a,b,c in itertools.product(range(7),repeat=3) if a+b+c==6 and b+2*c==6]
z_solutions=[x for x in solutions if x[0]+x[2]==4]
d_solutions=[x for x in solutions if x[0]-x[2]==0]
check(len(solutions)==4 and z_solutions==[(2,2,2)] and d_solutions==solutions,'C01: 같은 요약의4입력·독립Z의 복원·종속D의 무기여')
baseline=100+(8-10)*1+(8-12)*2
changed=100+(9-10)*1+(11-12)*2
changed13=100+(9-10)*1+(13-12)*2
check((baseline,changed,changed13)==(90,97,101),'C02: 기준90·변경97·추가변형101 L, 개선7과 절대감소3 구별')
truth=[]
for L,X,U,E in itertools.product([False,True],repeat=4):
    C=L and not X;F=C and U and not E;A=L
    truth.append({'L':L,'X':X,'U':U,'E':E,'C':C,'F':F,'A':A})
base=[r for r in truth if r['L'] and not r['X'] and r['E']]
without=[r for r in truth if r['L'] and not r['X'] and not r['E']]
check(all(r['C'] and not r['F'] and r['A'] for r in base) and {r['F'] for r in without}=={False,True},'C03: 통지오류 예외에서 취소/기록 유지·비용금지, 예외 제거만으로 비용 미확정')
dump('카드_국소검산.json',{'scope':'가상 설계의 명시 수치·규약 검산. 완성 문항/실제 사실/교육 효과 검증 아님',
    'C01':{'T6_W6_allowed_inputs':solutions,'with_Z4':z_solutions,'with_D0':d_solutions,'domain':'0이상 정수; T=0 평균 제외'},
    'C02':{'baseline_final':baseline,'modified_final':changed,'modified_second_inflow13_final':changed13,'comparison_gain':changed-baseline,'absolute_change':changed-100,'intermediate_stocks':[98,90,99,97,99,101],'unit':'L'},
    'C03':{'scope':'현재 유예 시각의 규약만. 사전 연장 뒤 새 시각의 결과는 포함 안 함','truth_table':truth,'base_case_U_unknown':base,'without_E_U_unknown':without},
    'C04':{'check_type':'명제 역할의 수동 대조','P':'특정 작성자','Q':'분류표 신뢰','T':'시대','finding':'P←Q←P에서 B→T가 추가되어도 T→P의 충분 관계는 주어지지 않는다. 독립C→P가 명시될 때만 별도 정당화 경로가 생긴다.','not_claimed':'실제 유물 진위, 외부 검사 신뢰, 완성 선지 유일성 미검증'}})

snapshot=readj(OUT/'기준입력상태.json')
changed_inputs=[]
for r in snapshot['selected_inputs']:
    f=ROOT/r['path']
    if hashlib.sha256(f.read_bytes()).hexdigest()!=r['sha256']:changed_inputs.append(r['path'])
check(not changed_inputs,'주요 기준 입력13파일의 저장바이트 보존; 전체 저장소 검증 아님')

# 생성되는 보고서/검산 경로까지 만든 후 Markdown 링크를 확인한다.
dump('검증보고서.json',{'status':'검사 중'})
broken=[];link_count=0
for f in OUT.glob('*.md'):
    for target in re.findall(r'\]\(([^\n]+?)\)',f.read_text()):
        t=unquote(target.strip().strip('<>')).split('#',1)[0]
        if not t or re.match(r'^[a-z]+://',t):continue
        link_count+=1
        if not (f.parent/t).exists():broken.append({'file':f.name,'target':t})
check(not broken,'Markdown 로컬 링크 대상 존재')
report={'date':'2026-10-18','status':'통과' if not errors else '실패','checks_passed':passed,'errors':errors,
    'json_parsed':json_counts,'markdown_local_links_checked':link_count,'broken_links':broken,
    'changed_selected_inputs':changed_inputs,'counts':readj(OUT/'v1_집계.json'),
    'verification_limit':'원본 전체 hash/audit, 모든 장면의 새 의미 판정, 완성 문항 유일성, 학생/다른 모델 검증은 수행하지 않음'}
dump('검증보고서.json',report)
print(json.dumps({'status':report['status'],'passed':len(passed),'errors':errors,'broken_links':broken,'local_links':link_count},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
