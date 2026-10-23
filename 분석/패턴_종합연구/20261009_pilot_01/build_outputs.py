import json,re,hashlib,html
from pathlib import Path
from collections import Counter
from event_specs import EVENTS
from card_specs import CARDS
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
def read(p): return (ROOT/p).read_text()
def j(p): return json.loads(read(p))
def rows(p): return [(i,json.loads(l)) for i,l in enumerate(read(p).splitlines(),1) if l.strip()]
def save(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def norm(s): return re.sub(r'[^\w]', '', re.sub(r'<[^>]+>','',html.unescape(s)))
def relink(p,line=None):
    return f'[{p}'+(f':{line}' if line else '')+'](<../../../'+p+(f'#L{line}' if line else '')+'>)'
manifest=j(str(OUT.relative_to(ROOT)/'sample_manifest.json'))
samples=[s for s in manifest['samples'] if s['split']=='discovery']
cases={c:s for s in samples for c in s['case_ids']}
idx={r['case_id']:r for r in j('data/기본기_연구/research_data_index_enriched_v2.json')['case_to_group']}
queuepath='data/기본기_연구/astra_handoff_queue.jsonl'
raw={}
for ln,r in rows(queuepath):
    if r.get('case') in cases:
        raw.setdefault(r['case'],{}).setdefault(r['stage'],[]).append((ln,r))
kps={r['passage_id']:(ln,r) for ln,r in rows('data/kice_passages.jsonl')}
kqs={r['question_id']:(ln,r) for ln,r in rows('data/kice_questions.jsonl')}
mps={r['group_id']:(ln,r) for ln,r in rows('data/meet_passages.jsonl')}
mqs={r['question_id']:(ln,r) for ln,r in rows('data/meet_questions.jsonl')}
coverage=[]; blind={}; src={}
for c,s in cases.items():
    bpath=f'data/기본기_연구/prepared_backlog/blind_sources/{c}.json'
    b=j(bpath);blind[c]=b;rr=idx[c];qid=rr['question_id'];pid=rr['passage_id']
    if rr['exam_family']=='KICE':
        pl,p=kps[pid];ql,q=kqs[qid]
        source=dict(passage_file='data/kice_passages.jsonl',passage_line=pl,passage_field='passage_text',question_file='data/kice_questions.jsonl',question_line=ql,source_container='고3 기출/'+p['source_hwpx'],source_markdown=p['source_markdown'],level='정본 JSONL/편집 HWPX 연결 전사 대조; 원 배포 지면 신규 전수 대조 아님')
        passage_match=norm(p['passage_text'])==norm(b['passage_text'])
        question_match=norm(q['stem'])==norm(b['stem']) and all(norm(a)==norm(z) for a,z in zip(q['choices'],b['choices'])) and len(q['choices'])==len(b['choices'])
    elif rr['exam_family']=='MEET':
        pl,p=mps[pid];ql,q=mqs[qid]
        source=dict(passage_file='data/meet_passages.jsonl',passage_line=pl,passage_field='context_markdown',question_file='data/meet_questions.jsonl',question_line=ql,source_markdown=p['source']['canonical_markdown'],official_pages=p['source']['official_pages'],level='공식 지면 검수 완료 정본 전사 재사용; 이번에는 전사 텍스트 연결 대조')
        passage_match=norm(b['passage_text']) in norm(p['context_markdown'])
        question_match=norm(b['stem']) in norm(q['question_markdown']) and all(norm(z) in norm(q['question_markdown']) for z in b['choices'])
    else:
        sp=rr['canonical_source_path'];text=read(sp)
        source=dict(passage_file=sp,passage_line=10 if c in ['AJP','AJQ','AJR'] else 364,passage_field='본문',question_file=sp,question_line=None,source_markdown=sp,level='공식 검수 전사' if s['passage_group']=='G222' else '기존 공식 HWP 추출 텍스트; 이번 지면 재검수 없음')
        if s['passage_group']=='G260': text='\n'.join(text.splitlines()[361:393])
        passage_match=norm(b['passage_text']) in norm(text)
        question_match=norm(b['stem']) in norm(text) and all(norm(z) in norm(text) for z in b['choices'])
    if s['passage_group']=='G160':
        resolved_pid='KICE-2026-6월_모평-Q01-03';resolved_qid=f'{resolved_pid}-Q{rr["question_number"]:02d}'
        source['identity_correction']='원장 2620~2622행의 2026학년도6월 후속 대조를 승계. 저장소 원 식별자와 정답 필드는 변경하지 않음.'
    else:
        resolved_pid=re.sub(r'-S.*$','',pid);resolved_qid=resolved_pid+f'-Q{rr["question_number"]:02d}'
    source.update(blind_source=bpath,passage_parity_normalized=passage_match,question_parity_normalized=question_match)
    src[c]=source
    last=raw[c]['answer_check'][-1]
    answer=last[1]['payload'].get('official_answer')
    coverage.append(dict(case=c,passage_group=s['passage_group'],passage_id=pid,question_id=qid,
        resolved_passage_id=resolved_pid,resolved_question_id=resolved_qid,
        full_passage_read=True,full_stem_and_all_choices_read=True,choice_count=len(b['choices']),
        source=source,official_answer_reused=answer,answer_record_id=last[1]['record_id'],answer_record_line=last[0],
        analysis_records=[dict(stage=st,line=ln,record_id=r['record_id']) for st,rs in raw[c].items() for ln,r in rs],
        diagram_read=c in ['CA','GL'],verification_limit='원문 배포본 전수 재검증·재풀이는 하지 않았으며 기존 검증 범위를 승계'))
cover={r['case']:r for r in coverage}
save('reading_coverage.json',coverage)

def evidence(c,quote,field):
    b=blind[c];txt=b[field]
    assert quote in txt,(c,quote,'원문 인용 불일치')
    offset=txt.index(quote)
    source=src[c]
    original_file=source['passage_file'] if field=='passage_text' else source['question_file']
    line=source['passage_line'] if field=='passage_text' else source['question_line']
    ev=dict(quote=quote,blind_path=source['blind_source'],json_pointer='/'+field,
        char_start=offset,char_end=offset+len(quote),
        text_line=txt[:offset].count('\n')+1,
        paragraph_by_blank_line=len(re.split(r'\n\s*\n',txt[:offset])),
        canonical_path=original_file,canonical_line=line,canonical_field=source['passage_field'] if field=='passage_text' else 'stem / question_markdown / 해당 문항',
        verification_level=source['level'])
    if original_file.endswith('.md'):
        candidates=[i for i,l in enumerate(read(original_file).splitlines(),1) if norm(quote) in norm(l)]
        ev['canonical_matching_lines']=candidates
        if candidates:ev['canonical_line']=candidates[0]
        assert candidates,(c,quote,'원본 MD 인용 미확인')
    else:
        d=json.loads(read(original_file).splitlines()[line-1])
        assert norm(quote) in norm(json.dumps(d,ensure_ascii=False)),(c,quote,'정본 JSONL 인용 미확인')
    return ev

events=[]
preview={
'G001':'입증 요건, 책임 주체, 인정 정도, 인과관계 인정 뒤 반증의 순서를 구분해 둘 수 있다.',
'G002':'이심률의 정의와 원형성·거리·각지름의 방향 관계를 정리할 수 있다. 조차는 보기를 본 뒤에 연결된다.',
'G004':'전통적 인식론/베이즈주의의 표현 방식, 갱신 조건, 무관 정보 유지 규칙을 분리할 수 있다.',
'G010':'형벌권의 위탁 범위, 예방 목적, 피해와 처벌의 비례, 강도와 지속 효과를 나눌 수 있다.',
'G014':'내부/외부 왜곡과 원근 효과를 나누고 왜곡 보정→시점 변환→합성을 정리할 수 있다. A/B 비교는 그림 열람 뒤에 가능하다.',
'G039':'능동 발생 주장의 근거, 청세포 신호의 발생·전달 경로, 손상 시 신호 소멸을 정리할 수 있다.',
'G103':'주장자를 구분하고 과학성·진릿값·물질 구성·환원 가능성을 각각 표시하며 문단의 논증 역할을 정리할 수 있다.',
'G160':'고빈도 의미의 우선 확인과 최종 채택을 구별하고 문맥 제약에 따른 후보 제거·유보 절차를 이해할 수 있다.',
'G222':'상위법/훈령과 상급/하급 기관, 정책 명분/운영 실태, 역사적 변화를 각각 구분할 수 있다.',
'G260':'초기/이후의 국가 역할, 입법부/행정부의 대표 기능, 마지막 국가 비대화 문제를 표시할 수 있다.',
'G284':'시기별 인물 집단, 평가 주체의 긍정·비판 이유, 인사·재정·직언·통치 문제를 나눌 수 있다.',
'G329':'지각·추정의 중심이 자영임을 추적하고 인물-대상별 감정과 방·팔·노란 선의 장면 기능을 읽을 수 있다.'}
for n,spec in enumerate(EVENTS,1):
    c=spec['case'];rr=cover[c];b=blind[c];bl=raw[c]['blind'][-1]
    bp=bl[1]['payload']; logic=next((bp[k] for k in ['minimal_logic_without_codes','minimal_logic'] if k in bp),None)
    assert logic is not None
    ic=raw[c]['independent_code'][-1]
    ev=dict(event_id=f'E{n:03d}',split='discovery',passage_id=rr['passage_id'],question_id=rr['question_id'],
      resolved_passage_id=rr['resolved_passage_id'],resolved_question_id=rr['resolved_question_id'],
      passage_group=rr['passage_group'],case_id=c,choice_ids=spec['choice_ids'],
      option_quotes=[dict(choice_id=i,text=b['choices'][i-1],source_path=src[c]['blind_source'],json_pointer=f'/choices/{i-1}') for i in spec['choice_ids']],
      existing_analysis_id=bl[1]['record_id'],existing_analysis_source=dict(path=queuepath,line=bl[0],field='payload',quote=logic,
        reflected_path=f'data/기본기_연구/독립풀이_04/{c}_01_최초풀이.md'),
      original_evidence=[evidence(c,spec['quote'],spec['quote_field'])],
      information_presentation=spec['information_structure'],question_or_choice_operation=spec['option_operation'],
      decisive_difference=spec['decisive_difference'],solving_action=spec['action'],
      application_conditions=[CARDS[p]['condition'] for p in spec['patterns']] or ['기록된 발문·선지와 명시된 원문 관계에 한정; 일반 규칙 미확정'],
      action_timing=dict(during_passage=preview[rr['passage_group']]+' 특정 선지의 오류 판정은 아직 불가.',after_question=spec['action']),
      action_necessity=spec['necessity'],
      reused_finding=logic,new_interpretation=spec['new_interpretation'] or '이번에는 이 국소 조작을 다른 지문의 같은 조건·행동과 비교하는 사건 단위로 추출했다.',
      alternative_solution=spec['alternatives'],
      disagreement_or_unverified=['학생 실제 오답·수행 자료 없음; 행동의 교육 효과와 실제 사용 빈도는 미확인','별도 검증 표본 적용 전'],
      pattern_ids=spec['patterns'],classification_status='candidate' if spec['patterns'] else 'unclassified_preserved',
      feature_in_passage=True,used_in_item=c!='ZE',
      utilization_role='절차 설명의 내용 대조만 확인; 패턴 행동 직접 수행 아님' if c=='ZE' else spec['necessity'],
      answer_record_id=rr['answer_record_id'],answer=rr['official_answer_reused'],
      original_codes_after_candidate=dict(record_id=ic[1]['record_id'],path=queuepath,line=ic[0],
        roles={k:v for k,v in ic[1]['payload'].items() if k in ['primary','primary_candidates','auxiliary','surface','primary_status']},
        site_original_codes=idx[c].get('site_original_codes'),site_status=idx[c].get('sdss_applicability'),mapping_status='기존 판정과 사후 대응; 이번 신규 100코드 판정 아님'))
    if c=='GL':ev['disagreement_or_unverified'].append('④ 수식 중복첨자 원 배포본 검증은 기존 유보 유지. 이 사건은 ① 선후만 사용.')
    if c=='GK':ev['disagreement_or_unverified'].append('GK-depth_backfill-20260915-audit12-01 (queue:926)의 대안 풀이·필수성 제한 승계')
    if c in ['ZD','ZE','ZF']:ev['disagreement_or_unverified'].append('원 식별자 2025/최초 답 오연결, 후속 2026학년도6월 정정 기록 우선')
    events.append(ev)
(OUT/'pilot_events.jsonl').write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n' for e in events))
assert set(cases)=={e['case_id'] for e in events}
stats={}
for p in CARDS:
    es=[e for e in events if p in e['pattern_ids']];use=[e for e in es if e['used_in_item']]
    stats[p]=dict(evidence_events=len(es),observed_passages=len({e['resolved_passage_id'] for e in es}),
       utilized_passages=len({e['resolved_passage_id'] for e in use}),utilized_questions=len({e['resolved_question_id'] for e in use}),
       source_questions=len({e['resolved_question_id'] for e in es}),
       structure_only_events=[e['event_id'] for e in es if not e['used_in_item']],event_ids=[e['event_id'] for e in es])
summary=dict(discovery_passages=len({e['resolved_passage_id'] for e in events}),discovery_questions=len({e['resolved_question_id'] for e in events}),
    events=len(events),unclassified_events=sum(not e['pattern_ids'] for e in events),
    classified_unique_questions=len({e['resolved_question_id'] for e in events if e['pattern_ids'] and e['used_in_item']}),patterns=stats)
save('pilot_counts.json',summary)

md=['# 발견용 표본에서 얻은 패턴 후보', '',
    '정본 지문·발문·모든 선지를 읽은 뒤 판정 장면을 먼저 작성하고 기존 코드 대응을 확인했다. 반복 후보는 독립된 검증을 통과한 확정 규칙이 아니다. 아래 수치는 발견용 12세트·39문항 중 **연결된 장면에서 확인한 수**이며 표본 내 모든 가능한 활용을 전수 분류한 빈도도, 전체 기출의 빈도도 아니다.', '',
    '‘필수’는 해당 선지의 의미를 정확히 판단하는 데 필요한 구별을 뜻한다. 특정 표 작성이나 전 문항 공통 행동의 강제, 실제 학생 수행의 관찰을 뜻하지 않는다. 원문 인용은 원장의 풀이 문구와 별도 필드로 저장했다. 정확한 JSON 필드·문단·문자 위치 및 모든 관련 선지 전문은 `pilot_events.jsonl`을 따른다.','',
    '|후보|상태|지문 구조 확인|문항 활용 지문|고유 활용 문항|장면|','|---|---|---:|---:|---:|---:|']
for p,c in CARDS.items():
    t=stats[p];status='표본 내 반복 후보' if t['utilized_passages']>=2 else '단독 지문 잠정 후보'
    md.append(f'|{p} {c["name"]}|{status}|{t["observed_passages"]}|{t["utilized_passages"]}|{t["utilized_questions"]}|{t["evidence_events"]}|')
for p,c in CARDS.items():
    t=stats[p];es=[e for e in events if p in e['pattern_ids']]
    md.extend(['',f'## {p}. {c["name"]}','',f'**규칙:** {c["rule"]}','',f'- 적용 조건: {c["condition"]}',f'- 적용하지 말 것: {c["avoid"]}',f'- 연결 구조: {c["chain"]}',f'- 통합·구분 근거: {c["relation"]}',f'- 근거 규모: 구조 확인 {t["observed_passages"]}개 고유 지문, 실제 문항 활용 {t["utilized_passages"]}개 고유 지문·{t["utilized_questions"]}개 고유 문항. {t["evidence_events"]}개 장면. 동일 문항의 여러 장면은 문항 수 1로 계산.',f'- 100코드 사후 대응: {c["mapping"]}',f'- 검증 상태: {"다른 소재에서 반복 관찰했으나 검증용 미적용" if t["utilized_passages"]>=2 else "한 지문에만 확인되어 반복 패턴으로 확정하지 않음"}. 학생 오류율·교육 효과 미확인.',f'- 다음 검증: {c["test"]}','', '근거 장면:', ''])
    for e in es:
        a=e['original_evidence'][0];old=e['existing_analysis_source']
        md.extend([f'- **{e["event_id"]} / {e["case_id"]} / {e["resolved_question_id"]} / 선지 {e["choice_ids"]}**: “{a["quote"]}”. 출처 {relink(a["canonical_path"],a["canonical_line"])}; 원본 필드 {a["canonical_field"]}, source의 빈 줄 기준 문단 {a["paragraph_by_blank_line"]}.',f'  {e["decisive_difference"]} → {e["solving_action"]} 기존 풀이: {relink(old["path"],old["line"])} (`{e["existing_analysis_id"]}`). 역할: {e["action_necessity"]}.'])
    md.extend(['','경계·비해당 사례:',''])
    for bc in c['boundary']:
        bes=[e for e in events if e['case_id']==bc]
        e=bes[0];a=e['original_evidence'][0]
        md.append(f'- {bc} / {e["event_id"]}: {e["decisive_difference"]} ({relink(a["canonical_path"],a["canonical_line"])}). 위 적용 제외·통합 기준으로 판별하며 같은 문항의 다른 장면에는 적용될 수 있다.')
    md.append('\n반례의 범위: 위 항목은 실제 기출의 경계 사례다. 같은 적용 조건을 모두 만족하면서 규칙이 실패하는 강한 반례는 아직 미확보다.')
(OUT/'pattern_cards.md').write_text('\n'.join(md)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
print('연결 점검',[(r['case'],r['source']['passage_parity_normalized'],r['source']['question_parity_normalized']) for r in coverage])
