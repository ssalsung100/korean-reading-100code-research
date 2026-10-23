"""교정 이벤트와 기존 근거를 읽어 대표·경계 사례의 추적 가능한 열람본을 만든다."""
import json
from pathlib import Path

OUT=Path(__file__).resolve().parent
OLD=OUT.parent/'20261009_pilot_01'
events={r['event_id']:r for r in map(json.loads,(OUT/'revised_events.jsonl').read_text().splitlines())}
audit={r['event_id']:r for r in map(json.loads,(OUT/'citation_audit.jsonl').read_text().splitlines())}
counts=json.loads((OLD/'pilot_counts.json').read_text())['patterns']
boundaries={
 'P01':[('E042',[1],'애정 성분의 근거 부족; 단순 귀속 교환만으로 설명하지 않는다.'),('E024',[5],'운동의 원인과 방해를 구별하는 추가 관계 판단이 필요하다.')],
 'P02':[('E004',[2],'정의가 두 척도를 연결하므로 무조건 별개 축으로 분리하면 안 된다.'),('E036',[3],'기관의 귀속 교환이 핵심이며 동일 주체 안의 판단 축 이동이 아니다.')],
 'P03':[('E012',[5],'충분한 문턱을 무제한 단조 증가로 바꾸는 것은 관계의 과잉 추정이다.'),('E017',[2],'중간 단계에 남은 효과 확인이 핵심이다.')],
 'P04':[('E012',[5],'유리한 수준·충분한 문턱을 필요조건으로 역전하지 않는다.'),('E008',[2],'행위 규칙 자체가 주어지지 않아 필요조건 적용 문제로 처리하지 않는다.')],
 'P05':[('E029',[3],'후보 수로 유보의 원인을 구별한다.'),('E028',[5],'절차 설명의 일치 판정이며 어휘 후보를 직접 좁힌 수행 증거가 아니다.')],
 'P06':[('E035',[5],'해결책이 아닌 과거 사실의 시점이다.'),('E012',[5],'강도를 높이면 대책이 항상 좋아진다고 가정할 수 없다.')],
 'P07':[('E032',[1],'명분/실태를 시간 전환으로 바꾸지 않는다. pilot의 E031 연결을 교정.'),('E005',[4,5],'동일 계절의 이심률 변화 전후 비교다.'),('E031',[2],'규정/실행 구별의 별도 경계로만 보존한다.')],
 'S01':[('E005',[4,5],'주어진 방향 관계의 적용이며 사전값만으로 사후값 차이를 확정하는 문제가 아니다.'),('E014',[2],'상대적 약함과 전무함의 구별. pilot의 E013 연결을 교정.')],
 'S02':[('E025',[2,5],'견해 공통점과 진릿값 판단이다. 관측의 설명 판별력은 쟁점이 아니다.')],
 'S03':[('E041',[4,5],'문학의 지각 주체와 서술 방식 판정은 문단 전개 동사 대조와 다르다.')],
 'S04':[('E009',[5],'사후값 동일 가능성이지 복수 의미 선택 유보가 아니다.')],
 'S05':[('E003',[4,5],'인정 정도와 책임자·반증 단계 구분; 규정 위반과 부재의 구분은 아니다.')],
 'S06':[('E035',[5],'동일 국가의 명시적 전후 정책 변화이며 집단 동일성의 근거 부재 문제가 아니다.')]
}
lines=['# 패턴별 대표·경계 사례', '',
 '발견용 12지문·39문항만 재검토했다. 아래 인용은 본문/선지와 기존 풀이를 구분한다. 경계 사례는 적용 조건을 벗어난 실제 기출이며, 조건을 모두 만족하는데도 규칙이 실패하는 강한 반례를 확보했다는 뜻은 아니다. 창작 반례는 강의 시제품에서 별도로 표시한다.', '',
 '출처 좌표는 학년도·시험·문항 번호를 포함한 resolved_question_id를 사용한다. KICE의 로컬 전사는 공식 기출의 내용에 연결되어 있으나 원 배포 PDF를 이번에 새로 전수 검수한 것이 아니다. LEET 2011은 공식 HWP 추출 텍스트 수준, LEET 2022와 MEET는 기존 검수 정본 수준을 승계한다. GL④ 수식 표기 검증은 유보한다.', '']
boundary_rows=[]
def details(e, selected=None):
    rows=[f"**{e['event_id']} / {e['case_id']} / {e['question_id']}**", '',
          f"발문: {e['stem'].splitlines()[0]}", '',
          f"원문·선지: [발견용 원문](../../../{e['source_path']}) · 공식답 재사용: {e['official_answer_reused']}번 (`{e['answer_record_id']}`).", '']
    for j in e['judgments']:
        if selected and j['choice_id'] not in selected: continue
        rows += [f"- {'①②③④⑤'[j['choice_id']-1]} {j['text']}",
                 f"  - 내용/역할: {j['content_or_task_fit']}. 발문에 따른 행동: **{j['answer_action']}**."]
    rows+=['']
    for x in e.get('original_evidence_reused',[]):
        rows += [f"원문 근거: “{x['quote']}” — [{x['canonical_path']}:{x['canonical_line']}](../../../{x['canonical_path']}#L{x['canonical_line']}); {x['json_pointer']}, 문자 {x['char_start']}~{x['char_end']}.", '']
    a=audit[e['event_id']]
    rows += [f"판단 차이: {e['minimum_distinction']}", '',
             f"기존 풀이: [{a['record_id']}](../../../{a['raw_path']}#L{a['raw_line']}). 기존 인용 상태: {a['old_quote_assessment']}.", '']
    for q in a['corrected_support']:
        rows += [f"- `{q['json_pointer']}`: “{q['quote']}”"]
    return rows+['']

for pid, count in counts.items():
    lines += [f'## {pid}', '', '### 대표·활용 근거', '']
    for eid in count['event_ids']:
        lines += details(events[eid])
    lines += ['### 경계·비해당', '']
    for eid, choices, why in boundaries[pid]:
        e=events[eid]
        chosen=[j for j in e['judgments'] if j['choice_id'] in choices]
        lines += [f"- **{eid} / {e['case_id']} / {e['question_id']} / {'·'.join('①②③④⑤'[c-1] for c in choices)}**: {why}",
                  f"  - [해당 원문·선지](../../../{e['source_path']})"]
        for j in chosen:
            lines += [f"  - 선지: “{j['text']}” → {j['content_or_task_fit']}; {j['answer_action']}."]
        boundary_rows.append({'pattern_id':pid,'event_id':eid,'case_id':e['case_id'],'choice_ids':choices,'reason':why})
    lines += ['']
lines += ['## 추가된 정답 결정 장면', '']
for eid in ['E044','E045','E046']:
    e=events[eid];s=e['existing_support'];j=e['judgments'][0]
    lines += [f"### {eid} / {e['case_id']} / {e['question_id']}", '',
              f"- {'①②③④⑤'[j['choice_id']-1]} {j['text']}",f"- 원문: “{e['passage_support']['quote']}”",f"- 판단: {e['minimum_distinction']}",
              f"- [원문](../../../{e['source_path']}) / [기존 정답 풀이](../../../{s['raw_path']}#L{s['raw_line']}) `{s['record_id']}` `{s['json_pointer']}`: “{s['quote']}”", '',
              '기존 해석을 재사용하여 사건을 추가했다. 13개 패턴의 빈도나 새로운 100코드 판정으로 편입하지 않았다.', '']
(OUT/'03_대표와_경계_사례.md').write_text('\n'.join(lines)+'\n')
(OUT/'boundary_links.json').write_text(json.dumps(boundary_rows,ensure_ascii=False,indent=2)+'\n')
print('사례집 생성; 경계 연결',len(boundary_rows))
