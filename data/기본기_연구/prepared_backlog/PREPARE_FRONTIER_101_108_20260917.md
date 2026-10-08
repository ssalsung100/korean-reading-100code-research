# Prepared frontier report — G101~G108

- 시작 frontier: G101 ON
- 검사 범위: 기존 KICE canonical passage/question 색인, 기존 manifest·provenance mapping과의 중복 및 group variant 점검
- 새 READY group: 7개(G101, G102, G103, G104, G106, G107, G108)
- 새 READY cases: 34개(ON~PU)
- 제외 group: G105 — Q32 choice parse가 `incomplete_visual_or_table`이고 choices가 완전하지 않아 준비하지 않음
- visual/source 복원 asset: 없음. 선택된 7개 group은 passage/question의 visual placeholder가 없고 choices 5개·canonical link·공식답 기계 검증 필드를 통과함
- SDSS linkage: 0건. 의미적 유사성으로 태그를 추정하지 않고 sealed row의 site fields를 빈 값으로 유지함
- blind/sealed 분리: blind source에는 passage/stem/choices/provenance 역할만 저장하고 공식답은 sealed answer row에만 저장함
- G024 DR~DU 4건: 기존 prior-exposure hold를 유지하고 재blind·새 independent 판정을 만들지 않음
- semantic research: 수행하지 않음
- 다음 preparation frontier: G109
- Astra 즉시 연구 가능한 첫 READY group: G101 ON~OQ

검증 시 queue·processed·meta_state corpus 진행 수치는 변경하지 않았고, `record_id` pending raw는 0건이다. `scripts/verify_prepared_backlog.py`의 기존 source provenance 경고(IK, IO, IR, IW, IX, KS, LJ, LK, LN, LR, MX)와 기존 overlap 경고는 이번 신규 준비에서 발생한 오류가 아니다.
