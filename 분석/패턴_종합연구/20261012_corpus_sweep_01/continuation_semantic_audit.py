"""재개 구간의 직접 판단에 대한 후보 경계 수정만 append한다. 재실행 금지."""
from candidates import P
from record_synthesis import append
from corpus_io import OUT
import json

changes=[
('U0163-S01','측정근사조건','역산의 설명 방향이 아니라 구간 대표값 근사의 정확 조건을 검사함.'),
('U0168-S01','경로길이분리','공통 원인의 두 결과 연결과 병렬 전달 경로의 직렬 합산은 다름.'),
('U0169-S01','병치인과분리','필수 전제 발문이 아니라 상태의 대비에 이동 인과를 추가한 오류.'),
('U0170-S01','표현기능판독','다른 소재들의 함축 비교가 아니라 단일 의문 표현의 기능 판독.'),
('U0174-S01','표현기능판독','단일 홀씨 소재의 생성 기능을 문맥 순서에서 확인함.'),
('U0175-S01','표현기능판독','동일 내용/주장 행위 분리와 반문의 긍정·반박 기능 판독을 구별함.'),
('U0177-S01','표현기능판독','글 전체 전개 방식이 아니라 사물 변형이라는 표현의 기능 판독.'),
('U0180-S01','정보경로복원','논증 근거의 합류가 아니라 수신·확인·발신과 내용 반영 경로임.'),
('U0485-S01','행위결과분리','과거 계기/미래 목적과 목적 시도/성공 결과는 다른 경계.'),
('U0492-S01','행위결과분리','설득 근거의 제시가 상대의 승복 결과를 입증하지 않음.'),
('U0443-S02','순변화','미측정 항 역산이 아니라 편익 증가500·비용 증가850의 순변화-350을 계산함.'),
('U0161-S01','공격대상변형','실제 부정한 신의 섭리를 수용한 입장으로 바꾸어 공격한 오류.'),
('U0176-S01','속성분리','감금 행위의 인정과 고의 동기의 부정을 분리하며 평가 기준의 공격이 아님.'),
('U0173-S01','어휘행동','수량 지표 환원이 아니라 변질이라는 말의 문맥 행동·평가 방향을 복원함.'),
('U0449-S01','어휘행동','자연의 제일법칙의 문맥 행동은 생존 선택이지 계급 순응이 아님.'),
('U0472-S02','어휘행동','수량화 오류가 아니라 초연의 두 문맥 의미를 분리함.'),
('U0460-S02','기준내부검사','규칙의 우선순위가 아니라 유일 적중 기준의 중복 금지를 적용함.'),
('U0490-S01','비교축','수단과 최종 목표의 위계보다 공동 목표와 이사 수단 이견을 비교함.'),
('U0464-S01','관측합성','설명의 성과 유지·추가 보완보다 같은 관련성에 얽힌 교란 경로를 분리함.'),
]
all_scenes=[json.loads(l) for p in sorted(OUT.glob('batch_*_scenes.jsonl')) for l in p.read_text().splitlines()]
existing=[json.loads(l) for l in (OUT/'scene_amendments.jsonl').read_text().splitlines()]
assert not any(r.get('audit_id')=='재개_의미경계_01' for r in existing), '수정 원장 재실행 금지'
for event,key,reason in changes:
    target=next(s for s in all_scenes if s['event_id']==event)
    assert target['batch']>=11
    _,D,E,F=P[key]
    if event=='U0443-S02':
        C='총편익은1000→1500으로500 늘고 보전 비용은500→1350으로850 늘어 순편익은350 줄어든다. 2021년 미회수 보상 잔여는500만원이며 후원금과 가격을 통한 회수를 구별한다.'
    else:C=target['C']
    if event=='U0464-S01': E+=' 여기서 합성은 통계적 교란 경로이며 원문이 기여 크기나 가중 합산식을 지정한 것은 아니다. 과거·현재 소득 지속성의 문맥 보충을 유지한다.'
    if event=='U0472-S02': E+=' 초연의 무관심/관조적 거리 두 독해는 미해결로 남긴다.'
    if event in ('U0180-S01','U0485-S01'): E+=' 후속 지정 범위·연결 검수는 기존 원장을 승계하며 이번 신규 시각 검수를 주장하지 않는다.'
    append('scene_amendments.jsonl',dict(event_id=event,changes=dict(pattern=key,C=C,D=D,E=E,F=F),reason=reason,audit_id='재개_의미경계_01',original_scene_preserved=True))
append('candidate_definition_revisions.jsonl',dict(revision_id='재개_후보경계_01',date='2026-10-12',new_candidates=['값대상수분리','좌표정렬','가중상쇄','행위결과분리','정보경로복원','측정근사조건','경로길이분리','표현기능판독','병치인과분리'],amended_new_event_ids=[x[0] for x in changes]+['U0429-S01'],scope='이번에 신규 작성한 장면만 수정. 재개 전400지문·489장면은 재처리하지 않음.',old_definitions_rewritten=False))
print('신규 장면 후보 경계',len(changes),'건 수정 원장에 저장')
