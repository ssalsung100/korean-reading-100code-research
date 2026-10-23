"""발견용 기존 43장면의 수동 재검토 결과를 직렬화한다. 기존 파일에는 쓰지 않는다."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
OLD = OUT.parent / '20261009_pilot_01'
def read(p):
    return json.loads(p.read_text())
def dump(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
def jsonl(name, rows):
    (OUT / name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))

events = [json.loads(s) for s in (OLD / 'pilot_events.jsonl').read_text().splitlines()]
coverage = read(OLD / 'reading_coverage.json')
cov = {r['case']: r for r in coverage}
manifest = read(OLD / 'sample_manifest.json')
allowed = {c for s in manifest['samples'] if s['split'] == 'discovery' for c in s['case_ids']}
assert set(cov) == allowed
sources = {c: read(ROOT / cov[c]['source']['blind_source']) for c in allowed}
raw_lines = (ROOT / 'data/기본기_연구/astra_handoff_queue.jsonl').read_text().splitlines()
def raw(e):
    r = json.loads(raw_lines[e['existing_analysis_source']['line'] - 1])
    assert r['record_id'] == e['existing_analysis_id']
    return r
def leaves(obj, pointer=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from leaves(v, pointer + '/' + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from leaves(v, pointer + '/' + str(i))
    elif isinstance(obj, str):
        yield pointer, obj
def answer_number(v):
    s = str(v)
    for i, ch in enumerate('①②③④⑤', 1):
        if ch in s:
            return i
    return int(s)

# 내용이 본문과 양립하는지 / 발문의 판단 대상에 적합한지는 별도로 수동 확인했다.
verdicts = {
 'E001': ['부적절'], 'E002': ['부적절'], 'E003': ['부적절','적절'],
 'E004': ['부적절'], 'E005': ['적절','부적절'], 'E006': ['본문에서 답을 찾을 수 없음'],
 'E007': ['부적절','적절'], 'E008': ['부적절'], 'E009': ['부적절'],
 'E010': ['문맥 의미 일치','문맥 의미 불일치'], 'E011': ['부적절'], 'E012': ['부적절'],
 'E013': ['적절'], 'E014': ['부적절'], 'E015': ['치환 부적절'],
 'E016': ['부적절','적절'], 'E017': ['적절','부적절','부적절'], 'E018': ['부적절','적절'],
 'E019': ['문맥 의미 일치','문맥 의미 불일치'],
 'E020': ['관측 사실은 본문과 양립하나 능동 발생의 판별 근거로 불충분','능동 발생을 지지하는 근거로 적절'],
 'E021': ['부적절'], 'E022': ['해당 기술로 청력을 평가하기 어려운 사례'],
 'E023': ['부적절','적절'], 'E024': ['적절','부적절'], 'E025': ['적절','부적절'],
 'E026': ['부적절','적절'], 'E027': ['부적절'], 'E028': ['적절'], 'E029': ['부적절'],
 'E030': ['적절','적절'], 'E031': ['부적절'], 'E032': ['부적절'], 'E033': ['비판 근거로 부적절'],
 'E034': ['부적절'], 'E035': ['부적절'], 'E036': ['부적절'], 'E037': ['대책으로 적절','지정된 문제에 대한 대책으로 부적절'],
 'E038': ['동일 집단이라는 근거 없음'], 'E039': ['대책으로 적절','대책으로 부적절'],
 'E040': ['평가 요소를 본문에서 찾을 수 없음','평가 요소를 본문에서 찾을 수 있음'],
 'E041': ['서술 방식으로 적절','서술 방식으로 부적절'], 'E042': ['애정 성분의 근거 부족','적절'], 'E043': ['부적절']
}
wrong_quote = {'E001','E002','E008','E014','E030','E031','E032'}
partial_quote = {'E003','E005','E007','E010','E016','E017','E018','E019','E020','E023','E024','E026','E037','E039','E040','E042'}
negative = {'AB','AC','AF','AG','AI','BI','BJ','BL','GL','GM','ZD','ZF','AJQ','AJR','ANV','ANW','AQN','AQP','AVS','AVT','AVU'}
audit = []
revised = []
for e in events:
    case = e['case_id']; src = sources[case]; r = raw(e)
    ans = answer_number(cov[case]['official_answer_reused'])
    oldquote = e['existing_analysis_source']['quote']
    all_leaves = list(leaves(r['payload'], '/payload'))
    exact = [{'json_pointer': p, 'quote': s} for p, s in all_leaves if s == oldquote]
    assert exact, (e['event_id'], '기존 인용을 원장에서 찾지 못함')
    supplemental = []
    for p, s in all_leaves:
        if e['event_id'] in wrong_quote and 'minimal_logic' in p:
            continue  # 다른 선지의 정답 요약은 이 장면의 교정 근거에 섞지 않는다.
        if 'intermediate' in p or 'minimal_logic' in p or 'exact_error' in p or '/error' in p:
            if 'minimal_logic' in p or any('①②③④⑤'[i-1] in s for i in e['choice_ids']):
                supplemental.append({'json_pointer': p, 'quote': s})
    a = {'event_id': e['event_id'], 'case_id': case,
         'old_quote_assessment': ('다른 선지의 판단 근거; 원 인용만으로 불충분' if e['event_id'] in wrong_quote else
                                  '일부 선지만 직접 뒷받침; 나머지 선지별 근거 보충' if e['event_id'] in partial_quote else
                                  '해당 핵심 판단을 뒷받침'),
         'old_quote': oldquote, 'old_quote_pointers': exact,
         'record_id': r['record_id'], 'raw_path': e['existing_analysis_source']['path'],
         'raw_line': e['existing_analysis_source']['line'], 'corrected_support': supplemental,
         'interpretation_origin': '선지별 판단은 기존 최초 풀이의 중간 추론에서 회수. 새 해석으로 소급하지 않음.',
         'new_interpretation': '내용 판정과 발문에 따른 선택을 분리한 사건 스키마 및 교육·출제 활용은 이번 실행의 새 분석.'}
    audit.append(a)
    choices = []
    for i, verdict in zip(e['choice_ids'], verdicts[e['event_id']]):
        choices.append({'choice_id': i, 'text': src['choices'][i-1], 'content_or_task_fit': verdict,
                        'answer_action': '정답으로 선택' if i == ans else '정답 후보에서 제외',
                        'role': '정답 결정 근거' if i == ans else '비정답 선지 검토'})
    revised.append({'event_id': e['event_id'], 'revision_of': e['event_id'], 'case_id': case,
                    'passage_group': e['passage_group'], 'question_id': cov[case]['resolved_question_id'],
                    'exam_family': cov[case]['resolved_question_id'].split('-')[0],
                    'stem': src['stem'], 'selection_request': '부정 대상 선택' if case in negative else '긍정 대상 선택',
                    'official_answer_reused': ans, 'answer_record_id': cov[case]['answer_record_id'],
                    'answer_record_line': cov[case]['answer_record_line'],
                    'judgments': choices, 'pattern_ids': e['pattern_ids'],
                    'source_path': cov[case]['source']['blind_source'], 'source_provenance': cov[case]['source'],
                    'original_evidence_reused': e['original_evidence'],
                    'minimum_distinction': e['decisive_difference'],
                    'inherited_code_reference': e['original_codes_after_candidate'],
                    'interpretation_origin': a['interpretation_origin'],
                    'new_interpretation': a['new_interpretation'],
                    'citation_audit_event': e['event_id'], 'strict_blind': False})

additions = [
 ('E044','AA',1,'입증의 용이성 차이 → 부담을 쉬운 쪽에 배분하는 형평 고려 → ①의 원리 설명과 일치',
  '이런 형평성을 고려하여 특정한 사실의 발생을 주장하는 이에게 그 사실의 존재에 대한 입증 책임을 지도록 하였다.'),
 ('E045','AH',4,'복수 명제를 동시에 새롭게 알아도 적용됨 → 참/거짓 정보를 함께 아는 사례도 적용 범위 안 → ④',
  '조건화 원리는 새롭게 알게 된 명제가 동시에 둘 이상인 경우에도 마찬가지로 적용된다.'),
 ('E046','AJP',3,'국가의 단속·수용과 복지기관의 규율, 국가보조금 지원을 결합 → 정책 수행상 협력 관계 → ③',
  '국가는 부랑인으로 규정된 개개의 국민을 경찰력을 동원해 단속·수용하고 복지기관을 통해 규율했을 뿐만 아니라')
]
for eid, case, choice, logic, quote in additions:
    parent = next(e for e in events if e['case_id'] == case); r = raw(parent); src = sources[case]
    ptr, support = next((p,s) for p,s in leaves(r['payload'], '/payload') if 'minimal_logic' in p)
    assert quote in src['passage_text']
    revised.append({'event_id': eid, 'revision_of': None, 'case_id': case,
                    'passage_group': cov[case]['passage_group'], 'question_id': cov[case]['resolved_question_id'],
                    'exam_family': cov[case]['resolved_question_id'].split('-')[0],
                    'stem': src['stem'], 'selection_request': '긍정 대상 선택',
                    'official_answer_reused': choice, 'answer_record_id': cov[case]['answer_record_id'],
                    'answer_record_line': cov[case]['answer_record_line'],
                    'judgments': [{'choice_id':choice, 'text':src['choices'][choice-1], 'content_or_task_fit':'적절',
                                  'answer_action':'정답으로 선택', 'role':'정답 결정 근거'}],
                    'pattern_ids': [], 'classification_status':'미분류 유지; 13후보에 억지 배속하지 않음',
                    'source_path': cov[case]['source']['blind_source'], 'source_provenance':cov[case]['source'],
                    'minimum_distinction':logic,
                    'passage_support':{'json_pointer':'/passage_text','quote':quote,'char_start':src['passage_text'].index(quote)},
                    'existing_support':{'record_id':r['record_id'],'raw_path':parent['existing_analysis_source']['path'],
                                        'raw_line':parent['existing_analysis_source']['line'],'json_pointer':ptr,'quote':support},
                    'interpretation_origin':'기존 최초 풀이의 정답 경로 재사용; 사건 단위 추출만 신규',
                    'new_interpretation':'이번에 독립된 정답 결정 이벤트로 추가. 신규 패턴 발견 수로 세지 않음.',
                    'strict_blind':False})

routes=[]
for case in [c['case'] for c in coverage]:
    ans=answer_number(cov[case]['official_answer_reused'])
    before=[e['event_id'] for e in events if e['case_id']==case and ans in e['choice_ids']]
    after=[e['event_id'] for e in revised if e['case_id']==case and any(j['answer_action']=='정답으로 선택' for j in e['judgments'])]
    routes.append({'case_id':case,'question_id':cov[case]['resolved_question_id'],'answer':ans,
                   'before_answer_events':before,'after_answer_events':after,
                   'status':'기존 정답 장면 있음' if before else '정답 장면 누락 보완'})
assert len(routes)==39 and all(r['after_answer_events'] for r in routes)
jsonl('revised_events.jsonl',revised); jsonl('citation_audit.jsonl',audit);dump('answer_route_audit.json',routes)

report=['# 수정된 판정 장면·인용 대조 기록', '',
        '기존 43장면을 유지하여 교정하고 정답 결정 장면 3개를 덧붙였다. 기존 원장·코드 판정은 변경하지 않았다. 이 작업은 노출된 발견용 표본의 재검토이며 신규 blind 풀이가 아니다.', '',
        '내용 판정은 선지의 주장 또는 발문이 지정한 역할에 대한 판정이다. 정답 선택은 그 판정과 발문의 긍정/부정 요구를 결합한 결과다. GK①처럼 사실인 관측도 요구된 근거로 불충분할 수 있고, GM⑤ 같은 명사구는 참/거짓 진술로 바꾸지 않는다.', '',
        '|event|case·선지|내용/역할 판정|정답 선택|원 풀이 인용 점검|', '|---|---|---|---|---|']
for e in revised:
    a=next((a for a in audit if a['event_id']==e['event_id']),None)
    for j in e['judgments']:
        report.append(f"|{e['event_id']}|{e['case_id']} {'①②③④⑤'[j['choice_id']-1]}|{j['content_or_task_fit']}|{j['answer_action']}|{a['old_quote_assessment'] if a else '기존 최초 풀이에서 정답 경로 추가 추출'}|")
report += ['', '## 핵심 변경', '',
 '- E004/AC②: 원형에 더 가깝다는 내용은 부적절하다. 부적절한 것을 고르는 발문이므로 **②를 정답으로 선택**한다.',
 '- E022/GM⑤: 청세포 신호로 해당 사례의 청력을 평가하기 어렵다. 활용하기 어려운 사례를 고르므로 **⑤를 정답으로 선택**한다. 듣지 못한다고 결론내리지 않는다.',
 '- E003·E007·E009·E011·E021 등에도 같은 분리를 적용했다. 이는 공식 정답 변경이 아니라 행동 표현의 모호성 수정이다.',
 '- E001·E002는 AA 정답①의 minimal_logic 대신 각각 intermediate_inference[1]·[3]을 연결했다. E008은 AH②의 intermediate_inference[1], E014는 BK②의 intermediate_inference[1]로 연결했다.',
 '- E030은 ZF④·⑤의 intermediate_reasoning[2]·[3], E031·E032는 AJP②·①의 intermediate_inferences[1]·[0]을 연결했다. 원 인용의 실제 존재와 그 인용의 논증 적합성은 별개다.',
 '- 39문항의 정답 선지 포함 여부를 모두 점검했다. 누락은 AA·AH·AJP 3문항이며 E044·E045·E046으로 보완했다. 새 해석을 기존 기록인 것처럼 소급하지 않았다.',
 '- P07의 명분/실태 경계는 E031/AJP②가 아니라 **E032/AJP①**이다. E031/AJP②는 규정/실행 구별(S05)의 별도 경계로만 유지한다.',
 '- S01의 약함/없음 경계는 E013/BK④가 아니라 **E014/BK②**이다. E013/BK④는 양도 범위·권한의 필요 전제(P04)이며 해당 설명의 근거가 아니다.',
 '', '## 근거를 여는 방법', '',
 '`revised_events.jsonl`의 source_path와 source_provenance가 선지 원문과 정본 좌표를 연결한다. `citation_audit.jsonl`은 원 인용, 평가, 보충 인용의 정확한 raw line·record_id·JSON pointer를 보존한다. 원장 기록 자체는 수정하지 않았다. `answer_route_audit.json`은 39문항의 보완 전후 정답 경로를 표시한다.',
 '', '기존 직접 판단이 발견된 인용 오류 7건은 새 해석이 아니라 잘못 선택한 인용의 교정이다. 사건 분리, 적용 한계의 정식화, 교육·출제 설계, 창작 반례는 이번 실행의 새 분석이다. 원 배포 지면의 신규 전수 대조는 하지 않았고 GL④의 수식 검증 유보를 승계한다.']
(OUT/'01_수정_판정장면과_변경기록.md').write_text('\n'.join(report)+'\n')
print('수정 장면',len(revised),'인용 대조',len(audit),'정답 경로',len(routes))
