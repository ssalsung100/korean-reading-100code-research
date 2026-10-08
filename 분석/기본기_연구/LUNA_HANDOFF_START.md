AGENTS.md와 `분석/기본기_연구/LUNA_HANDOFF.md`를 읽고 실행하라.

## 최신 session handoff — 2026-10-02 G426 partial sync·SDSS 대기

- Queue=processed=6,075 unique, pending=0, duplicate/orphan=0. G426의 BHA·BHB·BHC blind·answer_check·independent_code 9 raw를 반영했다.
- G426 최초답 ③·⑤·② 모두 공식답과 일치. 노출은 unknown이며 strict blind eligible=false라 엄격 blind 성과로 세지 않는다. 세 independent_code가 group 전체 저장됐으므로 SDSS 단계 barrier는 준비됐지만 `sdss_compare`와 induction은 아직 미완료다.
- `meta_state.py`: 385 groups·1,335 cases; meta/audit due=false, depth pending=[], semantic review=[]. Prepared manifest 333건(hold 포함), 다음 Excel-style ID BHD.
- 다음 Astra 작업은 G426 전체 SDSS 비교이며, 그 뒤 induction 상태를 처리하기 전 다음 group으로 넘어가지 않는다. blind packet source들은 blind-only이고 sealed 정답/SDSS 분리 확인을 유지한다.

## 이전 session handoff — 2026-10-02 G384 완료·G385 미열람

- Queue=processed=5,510 unique, pending=0, duplicate/orphan=0. Session hold는 응답·컨텍스트 예산 인계이며 quota emergency가 아니다. quota_status unavailable은 추정 없이 보존한다.
- G376~G384 9 groups·28 cases: group barrier 위반 0, 최초답 공식 일치 27/28(BCF), 선택답=매력 오답 중복 0/28, exact_error 누락/공백 0/28.
- `meta_state.py`: 344 groups·1,215 cases, META111 이후 1/4; meta/audit due=false, depth pending=[], semantic review=[].
- G385 frontier는 blind source·공식답·SDSS·기존 판정 모두 미노출. 새 Astra 세션에서 기본 상태 점검 후 G385 group blind부터 재개한다. BCF 실패/미해결 및 BBS 간접조건 유보를 그대로 보존한다.

미처리 Astra handoff record를 모두 기존 연구 자산에 반영하고,
Astra의 의미 판단을 변경하지 말고,
처리 원장과 CURRENT.md를 갱신하라.

hard usage limit으로 Astra가 먼저 종료된 경우에도 queue/processed 비교와 미처리 raw 후처리를 우선하라. 미완료 semantic stage 또는 SDSS compare를 추론해 채우지 말고 CURRENT에 남겨라.

의미적 재판단이 필요한 항목은 추측하지 말고 Astra 재검토 대상으로 남겨라.

처리가 끝나면 prepared backlog의 잔량과 다음 Excel-style case ID를 CURRENT에 기록한다. 잔량이 30개 미만이면 기존 후보 색인과 정본 자료를 이용한 기계적 준비를 수행한다. blind packet에는 공식 답·SDSS 태그·기존 해설·기존 코드 판정을 넣지 않고 sealed 파일에 분리한다. Luna는 코드 의미를 새로 판정하지 않는다.
