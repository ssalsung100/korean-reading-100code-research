<!-- 종료 gate D — 2026-10-05 -->
## 최신 상태 — 종료 gate D 판정 기록

- 연구 전체 완료·미완료 8 cases 완료 처리·제외를 뜻하지 않는다. 이번 연속 연구는 gate D에서 중단 판정되었으며 quota 중단이나 emergency가 아니다.
- Queue/processed=7,605 unique, pending=0, duplicate/orphan=0. 누계 497 groups·1,663 completed cases; meta=162, manual audit=162, meta/audit due=false, depth/semantic pending 없음.
- 남은 hold: G024 DR/DS/DT/DU 4건은 사전 SDSS 장벽 때문에 현재 절차상 independent 판단 불가. 재개에는 명시적 비독립 검토 절차가 필요하다. G370 BAP/BAQ/BAR/BAS 4건은 공식 원문 렌더 및 blind source에 본문이 없어 질문 전용 원문 복원이 필요하다. 현재 actionable=0.
- 최근 run G510~G537: 28 groups·78 cases, 기본 4단계 및 induction; META154~162, audits 156/159/162, depth backfill BQC/BQT/BRJ/BSA/BSD/BRN/BSP/BSL/BTH. 모두 strict-blind 실적에서 제외.

<!-- luna-sync:SESSION-hold-normal-quota-20261004-01-sync-20261004 -->
# Astra checkpoint — 정상 quota handoff·G502 SDSS 대기

- G502 9 stage raw와 hold 1건 반영. Queue=processed=7,128 unique, pending=0, duplicate/orphan=0.
- 최초 답 ②·③·③은 공식 답과 일치하나 strict blind eligible=false. G502 SDSS compare·induction 미완료, 다음 Astra는 SDSS부터 재개. 이번 run 완료 범위 G481~G501, BNQ 기존 제한 보존.
- `meta_state.py`: 461 groups·1,560 cases; META150 이후 1/3, meta/audit/depth/semantic pending 없음. 주간 remaining 7% 정상 handoff, primary 5h=null, runtime emergency 없음.

<!-- luna-sync:SESSION20261002-G411-G422-hold-20261002 -->
# Astra checkpoint — G411~G422 완료·응답예산 hold·G423 미열람

- 최종 hold raw까지 반영: Queue=processed=6,025 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G411~G422 12 groups·33 cases, 132 stage raw의 queue 줄 인덱스 barrier·답 일치·blind `exact_error`·경쟁 코드 2~4개·raw ID 중복 기계검증 오류 0건. 의미 판정 전수감사가 아니다.
- hold 사유는 응답예산 인계이며 quota unavailable이다. 실제 경고·임계 관측은 없고 연구 완료가 아니다. 다음 frontier G423은 미열람·미노출이다.

<!-- luna-sync:SESSION20261002-G422-META124-20261002 -->

- G422·META124까지 반영: Queue=processed=6,024 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G411~G422 12 groups·33 cases, 132 stage raw의 queue 줄 인덱스 barrier·답 일치·blind `exact_error`·경쟁 코드 2~4개·raw ID 중복 기계검증 오류 0건. 의미 판정 전수감사가 아니다.
- 다음 frontier G423은 미열람·미노출이다. BGO4③·BGP19·BGQ12 범위 유보를 보존한다.

<!-- luna-sync:SESSION20261002-hold-G399-G410-20261002 -->
# Astra checkpoint — G399~G410 완료·G411 미열람

- 최종 hold와 BACKFILL120-BFJ까지 반영했다. Queue=processed=5,873 unique, pending=0, duplicate=0, orphan=0. Hold 사유는 응답 작업예산이며 quota emergency/threshold 관측이 아니다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G399~G410 12 groups·36 cases의 실제 queue 줄 인덱스 장벽, 최초답=공식답, `exact_error`, record_id 중복을 기계 검증했다: stage barrier 위반 0, 답 불일치 0, exact_error 누락 0, 중복 0.
- 다음 frontier G411은 미열람·미노출이며 다음 blind 단계에서 시작한다. BEM 문맥 동일률 해석 유보와 기존 반모형 한정을 보존한다.

<!-- luna-sync:SESSION20261002-G385-G398-context-01 -->
## 이전 세션 인계 — G399 미열람 당시

- Hold raw `SESSION20261002-hold-G385-G398-context-01`까지 반영: Queue=processed=5,704 unique, pending=0. 인계 사유는 응답·컨텍스트 예산이며 quota 조회는 unavailable, runtime quota emergency는 관측되지 않았다.
- G385~G398은 14 groups·42 case 기록이다. 기계 검증에서 모든 case가 blind/answer_check/independent_code/sdss_compare 각 1건, group stage barrier 14/14 통과, 최초답-공식답 불일치 0, 최초답=매력 오답 0, exact_error 누락 0. 이 수치는 case 기록 수이며 고유 원문 전수 중복검증을 뜻하지 않는다.
- BDV는 MEET-2012-Q12, 기존 핵심8코드 기준 9장 F와 동일한 기노출 사례이므로 신규 고유 문항 및 strict-blind 성과로 세지 않는다. 나머지도 과거 노출 unknown인 경우 strict-blind 성과 확정에서 제외한다.
- BCT: ‘억압의 필연적 경로’ 설명은 원문의 가능성을 과강화한 오류로 철회. 최초 blind와 답⑤는 보존하며 ㄷ의 연역 타당성·공식답 유일성은 미해결. BDN: 전신 되먹임의 순효과·공식답 유일성 미해결. BDM⑤ 정량 방향 유보, BCP 기능 확장 한계·BDB 20 필수성·BDF 12 범위 미확정도 유지. 반모형은 논리 검사용이며 실제 생물 모형·치료 지침이 아니다.
- G398 BDX/BDY/BDZ는 후보 색인에 등재됐지만 matched_case_id=null이며 기존 연구 case 중복으로 확정하지 않는다.
- META116 완료; `meta_due=false`, `manual_parity_audit_due=false`, depth backfill=[], semantic_state_review=[]. Hold 처리 원장에는 `needs_astra_review`(미완료/hold 보존)로 남고, meta_state의 semantic_state_review에는 포함되지 않았다.
- 다음 frontier G399는 미열람·미노출이며 잠금 해제. 새 세션에서 AGENTS/CURRENT/ASTRA_START, meta_state/quota/pending을 점검한 뒤 G399 blind부터 시작한다.

# Astra checkpoint — G384 완료·G385 미열람

<!-- luna-sync:SESSION20261002-G384-G385-context-handoff -->
## 최신 Luna sync — G384 완료·응답/컨텍스트 인계·G385 미열람

- G384 induction 및 `SESSION20261002-hold-G376-G384-context-01` raw까지 반영했다. Queue=processed=5,510 unique, pending=0, duplicate=0, orphan=0. 인계 사유는 응답·컨텍스트 예산이며 quota emergency가 아니다. raw의 `quota_status=unavailable`은 unavailable 그대로 보존한다.
- G376~G384 9 groups·28 cases 기계검증: 모든 group에서 blind 전체 → 최초 answer_check 전체 → independent_code 전체 → SDSS compare 전체 순서 통과, barrier/coverage 위반 0. 최초답 공식 일치 27/28(BCF만 불일치), 선택답=매력 오답 중복 0/28, `exact_error` 누락·공백 0/28.
- `meta_state.py`: 완료 344 groups·1,215 research cases, META111 이후 1 group·4 cases; `meta_due=false`, `manual_parity_audit_due=false`, depth backfill=[], semantic review=[].
- 다음 frontier G385는 미열람·미노출(blind source/공식답/SDSS/기존 판정 모두 false). 다음 단계는 새 Astra 세션에서 AGENTS/CURRENT/ASTRA_START 확인 후 meta_state/quota/pending 점검, 이어 G385 group blind다. 미완료 semantic stage 없음.
- BCF 최초답 실패와 ㄹ 배제·공식 정답 유일성 미해결, BBS 간접조건 유보는 그대로 유지하며 사후에 최초 기록을 덮어쓰지 않는다.

# Astra checkpoint — G366~G375 완료·G376 미열람 frontier

## Luna sync 완료 — 2026-10-01 response/context handoff

- `SESSION20261001-hold-G366-G375-context-01` 반영. 응답·컨텍스트 예산 인계이며 quota emergency가 아니다. Queue=processed=5,381 unique, pending=0, duplicate/orphan=0.
- G366~G369·G371~G375: 9 groups·28 cases. G370 source-unavailable BAP~BAS 4건은 완료 분모에서 제외. Blind/answer_check/independent_code/sdss_compare 각각 28/28, group barrier 위반 0. 최초답 공식 일치 28/28; blind-answer 선택 불일치 0; 매력 오답=선택 답 중복 0; exact_error 누락 0.
- `meta_state.py`: 335 completed groups·1,187 cases, META108 이후 1/3; meta/audit due false; depth pending=[], semantic review=[].
- Manifest prepared 484/1,671; G024 historical hold 4 + G370 source hold 4 are non-actionable, actionable prepared=476. G376 manifest-only case IDs: BBI, BBJ, BBK; all source material remains unviewed.
- Preserve G368 restore provenance/strict blind limits; G370 hold; G372 BAW81/BAX44 limits and BACKFILL108; G373 tag100/BBB18 scope holds; G375 official diagram image provenance, transcription issue, and original hold.

# Astra checkpoint — G366~G375 완료·G376 미열람 frontier

## Luna sync 완료 — 2026-10-01 response/context handoff

- `SESSION20261001-hold-G366-G375-context-01` 반영. 응답·컨텍스트 예산 인계이며 quota emergency가 아니다. Queue=processed=5,381 unique, pending=0, duplicate/orphan=0.
- G366~G369·G371~G375: 9 groups·28 cases. G370 source-unavailable BAP~BAS 4건은 완료 분모에서 제외. Blind/answer_check/independent_code/sdss_compare 각각 28/28, group barrier 위반 0. 최초답 공식 일치 28/28; blind-answer 선택 불일치 0; 매력 오답=선택 답 중복 0; exact_error 누락 0.
- `meta_state.py`: 335 completed groups·1,187 cases, META108 이후 1/3; meta/audit due false; depth pending=[], semantic review=[].
- Manifest prepared 484/1,671; G024 historical hold 4 + G370 source hold 4 are non-actionable, actionable prepared=476. G376 manifest-only case IDs: BBI, BBJ, BBK; all source material remains unviewed.
- Preserve G368 restore provenance/strict blind limits; G370 hold; G372 BAW81/BAX44 limits and BACKFILL108; G373 tag100/BBB18 scope holds; G375 official diagram image provenance, transcription issue, and original hold.

# Astra checkpoint — BACKFILL108 반영·G375 frontier 개방

## Luna sync 완료 — 2026-10-01 G375 원문 도식 준비

- BACKFILL108은 기존 절차기록/processed에 반영됐다. `meta_state.py`: 334 groups·1,184 cases, meta/audit due false, depth pending=[], semantic review=[]. G375 gate 해제.
- BAX 후속 revision은 case detail의 payload-preserving reference 및 BACKFILL108 절차 raw를 통해 추적 가능하다. 최초 independent raw는 불변이다.
- G375 공식 원페이지는 `blind_sources/G375_official_question_page.png`에 전체 복사, 출처 metadata는 `G375_official_question_page.md`. 2006 MEET 공식 PDF p.50 연결 렌더와 hash 일치. 페이지에 해당 passage group의 문항 및 도식만 있고 정답·해설·다음 신규 지문은 없다.
- 마지막 점검 시 queue 5,373, processed 5,366, pending G375 raw 7건. G370 source hold4 prepared·completion 제외; G368 restoration provenance·strict 제한 보존.

# Astra checkpoint — AUDIT108 반영·BAT/BAX/BBC backfill 선행·G375 잠금

## Luna sync 완료 — 2026-10-01 AUDIT108

- AUDIT108 raw 반영 완료. Queue=processed=5,365 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 334 completed groups·1,184 cases, META108 이후 0/0; meta/audit due false; `depth_backfill_pending=["BAT", "BAX", "BBC"]`, semantic review=[].
- 다음은 Astra의 BAT·BAX·BBC depth_backfill raw 작성 후 Luna sync다. 해당 raw 반영 전까지 G375를 잠근다. Luna는 의미를 추가하지 않는다.
- G370 source hold4 prepared·미완료 유지, G368 restoration provenance·strict-blind 제한 보존.

# Astra checkpoint — META108 반영·AUDIT108 선행·G375 잠금

## Luna sync 완료 — 2026-10-01 META108

- META108 raw를 기존 절차 기록과 processed에 반영했다. Queue=processed=5,364 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 334 completed groups·1,184 cases, META108 이후 0/0; `meta_due=false`, `manual_parity_audit_due=true`, next audit remaining=0, depth pending=[], semantic review=[].
- 다음 허용 단계는 Astra의 AUDIT108 raw, audit가 요청하는 depth_backfill, 그 후 Luna sync다. 그 전까지 G375를 잠근다.
- G370 BAP~BAS source hold 4건은 prepared·미완료 유지, completion 분모 제외. G368 restoration provenance와 strict-blind 제한 보존.

# Astra checkpoint — G374 완료·META108/AUDIT108 선행·G375 잠금

## Luna sync 완료 — 2026-10-01 G374

- G374 BBC·BBD·BBE 전체 stage raw 12건과 induction 1건을 반영했다. Queue=processed=5,363 unique, pending=0, duplicate/orphan=0.
- 세 사례별 blind/answer_check/independent_code/sdss_compare 각 1건이며 두 group barrier 위반 0건.
- `meta_state.py`: 334 completed groups·1,184 cases, META107 이후 3/9; `meta_due=true`, `manual_parity_audit_due=false`(META108 반영 전), next audit까지 1회, depth pending=[], semantic review=[]. META108 및 META108에 따라 요구될 AUDIT108, 필요한 backfill/Luna sync 전까지 G375를 잠근다.
- Manifest prepared 487건(1,671 rows). G370 BAP~BAS source hold 4건은 prepared·미완료 상태이며 완료 분모에서 제외된다. 다음 frontier G375(잠금).

# Astra checkpoint — G373 완료·G374 frontier

## Luna sync 완료 — 2026-10-01 G373

- G373 BAZ·BBA·BBB 전체 stage raw 12건과 induction 1건을 반영했다. Queue=processed=5,350 unique, pending=0, duplicate/orphan=0.
- 세 사례별 blind/answer_check/independent_code/sdss_compare 각 1건이며 두 group barrier 위반 0건.
- 사이트 100 태그가 정답 아닌 ⑤ 또는 작품 전체를 가리킬 가능성은 미확정 상태로 둔다. BBB18 엄밀 명제 모순과 평가 기준 불일치의 범위도 유보한다.
- `meta_state.py`: 333 completed groups·1,181 cases, META107 이후 2/6; meta/audit due false, depth pending=[], semantic review=[]. Manifest prepared 490건. G370 source hold BAP~BAS 4건은 prepared·미완료로 완료 분모에서 제외된다. G368 restoration provenance와 strict-blind 제한 보존.
- 다음 frontier G374이며 meta gate상 잠금 해제 상태다.

# Astra checkpoint — G372 완료·G373 frontier

## Luna sync 완료 — 2026-10-01 G372

- G372 BAW·BAX·BAY 전체 stage raw 12건과 induction 1건을 반영했다. Queue=processed=5,337 unique, pending=0, duplicate/orphan=0.
- 세 사례 각각 blind/answer_check/independent_code/sdss_compare 1건, group barrier 위반 0건.
- BAW81은 단순 표면 유보로 한정하고 BAX44는 국소 용법 및 주 우선순위 유보를 보존했다. 기존 최초 판정과 코드 키는 raw대로 유지한다.
- `meta_state.py`: 332 completed groups·1,178 cases, META107 이후 1/3; meta/audit due false, depth pending=[], semantic review=[]. Prepared 493건. G370 source hold 4건은 prepared·미완료이며 완료 분모에서 제외된다. G368 restoration provenance와 strict-blind 제한 보존.
- 다음 frontier G373.

# Astra checkpoint — META107 반영·G372 frontier

## Luna sync 완료 — 2026-10-01 META107·잠금 해제

- META107 raw 반영 완료. Queue=processed=5,324 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 331 completed groups·1,175 cases, META107 이후 0/0; `meta_due=false`, `manual_parity_audit_due=false`, depth pending=[], semantic review=[]. G372 frontier가 열렸다.
- 마지막 manual audit 기준 META105, 이후 meta induction 2건이며 다음 audit까지 1회 남았다.
- G370 BAP·BAQ·BAR·BAS source hold 네 건은 prepared 상태로 유지하고 completion 분모에서 제외한다. G368 restored-source provenance 및 strict-blind/exposure 제한을 보존한다.
- 다음 frontier는 G372이며 원문 미열람이다.

# Astra checkpoint — G371 완료·META107 선행·G372 잠금

## Luna sync 완료 — 2026-10-01 G371·META107 gate

- G371 BAT·BAU·BAV 전체 stage raw 12건과 induction 1건을 반영했다. Queue=processed=5,323 unique, pending=0, duplicate/orphan=0.
- 세 사례별 blind/answer_check/independent_code/sdss_compare 각 1건, 두 group barrier 위반 0건.
- `meta_state.py`: 331 completed groups·1,175 research cases, META106 이후 3 groups·10 cases; `meta_due=true`, audit due=false, depth pending=[], semantic review=[]. META107 및 state gate에 따른 후속 Luna sync 전까지 G372를 잠근다.
- Manifest prepared 496건(전체 1,671). G370 BAP·BAQ·BAR·BAS source hold 네 건 prepared 상태이며 완료 분모에서 제외된다. 다음 frontier G372.

# Astra checkpoint — G370 hold·G371 frontier

## Luna sync 완료 — 2026-10-01 G370 source-unavailable

- G370 source-unavailable hold raw를 반영했다. Queue=processed=5,310 unique, pending=0, duplicate/orphan=0.
- G370은 미완료·hold로 유지한다. BAP·BAQ·BAR·BAS 네 manifest row는 `prepared`로 보존되며 consumed/excluded 처리하지 않았다. prepared 전체 499건(1,671 rows 중)에는 이 source hold 4건이 포함된다.
- `meta_state.py`: 330 completed groups·1,172 cases, META106 이후 2/7; meta/audit due false; depth pending=[], semantic review=[].
- 2017 LEET 홀수형·짝수형 question-only HWP의 [7–10] 지문 위치는 온라인 게시 불가 안내와 책 출처 표시로 대체되어 본문 복원 가능한 공식 question-only 원문이 확인되지 않았다. G371 frontier는 원문 미열람이다.

# Astra checkpoint — G369 완료·G370 frontier

## Luna sync 완료 — 2026-10-01 G369·G370 frontier

- G369 BAM·BAN·BAO 전체 stage raw 12건과 induction 1건을 payload 의미 변경 없이 반영했다. Queue=processed=5,308 unique, pending=0, duplicate/orphan=0.
- 세 사례 각각 blind/answer_check/independent_code/sdss_compare 1건씩, 두 group barrier 위반 0건. `primary`/`auxiliary`/`surface` 키와 최초 판정, 후속 보조 후보 인정, 주 우선순위 유보의 raw payload를 보존했다.
- `meta_state.py`: 330 completed groups·1,172 research cases, META106 이후 2/7; `meta_due=false`, `manual_parity_audit_due=false`, depth pending=[], semantic review=[]. Manifest prepared 499건.
- 다음 frontier는 G370이다.

# Astra checkpoint — G368 완료·G369 frontier

## Luna sync 완료 — 2026-10-01 G368·G369 frontier

- G368 BAI·BAJ·BAK·BAL 네 사례의 전체 stage raw 16건 및 G368 induction 1건을 기존 자산과 processed에 반영했다. 앞서 저장된 case hold 3건과 group-level crop hold 1건은 원기록으로 유지했다. Queue=processed=5,295 unique, pending=0, duplicate/orphan=0.
- 네 사례 각각 blind/answer_check/independent_code/sdss_compare 1건씩, all-group-blind-before-answer 및 all-group-independent-before-SDSS 위반 0건이다. `primary`/`auxiliary`/`surface` 키를 보존했다.
- Restored blind의 source-repair/original-hold provenance와 공식 source mapping을 반영했다. 전체 원문 render page 13·14가 blind_sources에 있고, 불완전 crop은 근거에서 제외했다.
- `meta_state.py`: 329 completed groups·1,169 cases, META106 이후 1/4; meta/audit due false, depth pending=[], semantic review=[]. Manifest prepared 502건, G368 네 case consumed_sdss. 다음 frontier G369.

# Astra checkpoint — G368 official source recovery held

## Luna sync 완료 — 2026-10-01 G368 복원 자료·미완료 barrier

- G368 BAI/BAJ/BAK 및 group-level hold 4건과 BAL blind 1건을 반영했다. Queue=processed=5,279 unique, pending=0, duplicate/orphan=0.
- G368 전체 blind barrier는 미완료다. BAI·BAJ·BAK hold, BAL blind 저장. `meta_state.py`: 328 completed groups·1,165 cases; META106 이후 0/0; due flags false; depth/semantic pending 없음. G368은 완료 집계 밖이다.
- 허용된 2016 LEET 홀수형 원 HWP 연결 렌더 인쇄면 13·14 전체 PNG를 blind_sources에 복사하고 manifest 해시와 동일함을 확인했다. 파일: `G368_restore_page13.png`, `G368_restore_page14.png`; `G368_restore_source.md`에 원본 경로·페이지·문항 mapping이 있다. 축소 열 crop 4개는 불완전으로 표시했다.
- 새 원문 범위는 공식 question HWP 및 question-only 렌더에 한정했다. 정답·해설·SDSS·sealed/candidate 자료를 열지 않았다. 다음 semantic 단계는 Astra 직접 검토 대기다.

# Astra checkpoint — META106 반영·G368 frontier

## Luna sync 완료 — 2026-10-01 META106·G368 잠금 해제

- META106 raw를 절차 기록과 processed 원장에 반영했다. Queue=processed=5,274 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 328 completed groups·1,165 research cases, META106 이후 0/0; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`. G368 frontier가 열렸다.
- BAF 후속 primary/auxiliary 수정 provenance marker와 지정 필드가 BAF SDSS 비교, G367 induction, META106 기록에 보존됐음을 기계 확인했다. 최초 independent raw는 불변이다.
- 신규 source/sealed/candidate 원문은 읽지 않았다.

# Astra checkpoint — G367 완료·META106 선행·G368 잠금

## Luna sync 완료 — 2026-10-01 G367·META106 gate

- G367 BAF·BAG·BAH의 전체 stage raw 12건과 G367 induction raw 1건을 원문 의미 변경 없이 반영했다. Queue=processed=5,273 unique, pending=0, duplicate/orphan=0.
- G367 세 사례에서 blind/answer_check/independent_code/sdss_compare 각 3건, group barrier 위반 0건이다. primary/auxiliary/surface 키를 보존하고 BAF 원 raw 판정 기록을 유지했다.
- `meta_state.py`: 328 completed groups·1,165 research cases, META105 이후 3 groups·9 cases; `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G368은 주 Astra의 META106 raw 저장과 Luna sync가 끝날 때까지 잠근다. Manifest prepared 506건이며 G024 historical HOLD 4건을 포함한다.
- 새 source/sealed/candidate 원문은 읽지 않았다.

# Astra checkpoint — G366 완료·G367 frontier

## Luna sync 완료 — 2026-10-01 G366·G367 frontier

- G366 BAC·BAD·BAE의 전체 네 단계 raw 12건과 G366 induction raw 1건을 기존 자산 및 processed 원장에 payload 의미 변경 없이 반영했다. Queue=processed=5,260 unique, pending=0, duplicate/orphan=0.
- 세 group case의 blind/answer_check/independent_code/sdss_compare는 각 3건씩이며 group barrier 2개 위반 0건이다. primary/auxiliary/surface 키 보존을 확인했다.
- `meta_state.py`: 327 completed groups·1,162 research cases, META105 이후 2 groups·6 cases; meta/audit due false, depth pending=[], semantic review=[].
- Manifest 1,671 rows 중 prepared 509건(기존 G024 historical HOLD 4건 포함), actionable prepared 505건이다. 다음 frontier는 G367이며 G366 induction sync가 완료됐다.
- 신규 source/sealed/candidate 자료는 열지 않았다. 연구 전체 완료가 아니다.

# Astra checkpoint — G347~G364 완료·G365 미열람 세션 인계

## Luna sync 완료 — 2026-09-28 세션 인계·재개 상태

- `SESSION20260928-hold-20260928-context-handoff-01`까지 반영했다. queue/processed 각 5,234 unique, pending0, duplicate/orphan0. 이번 중단은 response/context budget handoff이며 quota emergency 관측이 아니다.
- 이번 작업분 G347~G364: 18 groups·56 cases. Queue 순서 기준 네 stage 각각 56건이고, `all_group_blind_records_before_any_group_answer_check` 및 `all_group_independent_code_records_before_any_group_sdss_disclosure` 위반 0, group/case coverage 오류 0. 최초 선택 답 공식 일치 56/56.
- 누적 meta_state: 325 groups·1,156 research cases; META105 이후 0/0; meta/audit due false, depth pending=[], semantic review=[]. Research 1,156과 사이트 총계 1,147은 다른 분모다.
- Manifest `prepared` 24건(기존 G024 HOLD 4건, actionable 20건). G365는 AZZ가 첫 case ID이고 AZZ/BAA/BAB 모두 prepared다. G365 blind source, official answer, SDSS, prior judgment는 모두 미열람이다. Research complete=false.
- 재개: 새 세션에서 AGENTS.md/CURRENT.md/ASTRA_START.md를 읽고 meta_state/quota/pending을 확인한 뒤 G365 group blind부터 시작. Quota는 unavailable이며 이 인계는 quota emergency가 아니다.
- 보존: AYP/AZI 최초 오답 필드 오류와 사후 보충의 비소급, strict blind 미확정·AXH 제한·AVE/ATK 실패, AXW/AYE/AZO 원 hold 및 공식 복원 뒤 별도 blind, G348 안테나 분수계수 누락, 사이트 범위 미확정, G354 식별자 오기의 META102 정정.

<!-- luna-sync:TARGET-CROSSWALK-G282-G311-G312-PREFLIGHT-20260928 -->
## 현재 진행 상태 — crosswalk 갱신 완료·G312~G341 READY

- `research_completed_total = 994`; `target_completed = 457 / 1147`; `target_remaining = 690`. 두 진행률의 분모는 서로 다르며 994/1147로 합치지 않는다.
- G282~G311의 신규 91 consumed case를 exact `candidate_id`로 target crosswalk와 research-side crosswalk에 반영했다. 모두 `TARGET_MATCHED`; 기존 903 research row·366 완료 target row의 분류 및 4 HOLD·8 AMBIGUOUS 상태는 보존했다.
- Crosswalk 사전 검사: 1,147 target row, 994 research row, candidate/question/consumed-case 중복 0, 완료·HOLD·AMBIGUOUS overlap 0. Queue와 processed는 변경하지 않았다.
- Queue=processed=4,496, pending raw=0. G282~G311은 30 groups·91 cases, 네 semantic stage 각 91, group barrier 30/30이다. 최초 답 90/91 일치; ATK 최초④·공식②·확신도 .94 불일치를 보완풀이로 덮지 않았다. G306 3 cases는 핵심8코드 기준의 동일 소재 예시 사전노출로 strict blind 성과에서 제외했다. ARQ 원 hold와 resolved blind 모두 보존했다.
- META78~87, AUDIT78/81/84/87 및 관련 depth backfill 완료. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 신규 preparation dry-run 후 G312~G341, 30 groups·90 questions를 `READY_LOCAL_SOURCE`로 실제 기록했다. 첫 READY는 G312/ATT, family는 MEET/DEET 21 groups·LEET 9 groups·KICE 0. blind/sealed는 분리되었고 semantic research는 미착수다.
- Target-side crosswalk에는 이 90건이 여전히 `NOT_COMPLETED_READY_LOCAL_SOURCE`이므로 target 완료에 포함하지 않았다. 그 결과 target completed/remaining은 그대로 457/1,147 및 690이다. Manifest prepared 94건은 G312~G341 90 READY와 기존 G024 DR~DU 4 HOLD다. G024 HOLD는 미소비·미제외로 보존하며 다음 연구 frontier로 삼지 않는다.
- G312~G341 dry-run 검사: duplicate candidate/question, completed/HOLD/ambiguous overlap, blind answer/SDSS leakage, source provenance, passage-question linkage, empty stem, choice count, required visual, output conflict가 모두 0. 새 source·packet 90건 및 sealed provenance/answer 90건을 만들었다.
- 남은 사전준비 inventory: READY_LOCAL_SOURCE 244, NEEDS_RESTORE 335, SOURCE_MISSING 9, HOLD 4, AMBIGUOUS_COMPLETION 8. 다음 semantic frontier는 G312 ATT부터 strict passage barrier를 지켜 시작한다.
- `target_completion_crosswalk_v1.jsonl`과 `research_case_target_crosswalk_v1.jsonl`에는 G282~G311까지 반영했다. **이후 준비만 된 G312~G341은 research completion이 아니므로 crosswalk에는 아직 올리지 않았다.**
- Quota tool 결과는 계속 `unavailable`; 수치는 추정하지 않았다.

<!-- luna-sync:G282-G311-final-20260928 -->
## 현재 상태 — G282~G311 코호트 종료·다음 신규 blind 준비 필요

- Queue 4,496건·processed 4,496건·unique ID 각각 4,496건·pending 0건. G282~G311 신규 raw 413건(stage 364·induction 30·META 10·manual audit 4·depth_backfill 4·hold 1)을 반영했다.
- Queue SHA-256 `1fcc52188525f3b9d77d7c781cd9e6629bd6899774d328fc51884e2f39b9c6d9`. 기존 4,083행 prefix hash는 queue `e98e459b68fe52ae582fae7d213e550e4052930770ea8762ebc33e7769881624`, processed `f0fe43a1d5ceeb02b777b4a07a2ca1d2faeb948b594955ddf88bce9d8abde456`로 초기값과 일치한다.
- 신규 cohort: 30 groups·91 cases, blind/answer_check/independent_code/sdss_compare 각 91건, group barrier 30/30 통과. 최초 정답 일치 90/91이며 유일 불일치는 ATK 최초④·공식②, 확신도 0.94 실패다. 사후 보완은 최초 성과를 바꾸지 않는다.
- G306 세 사례는 사전노출로 `strict_blind_eligible=false`이며 정답·SDSS 선공개는 없었다. ARQ의 최초 hold는 불변 보존되고 정정 blind/resolved_hold로 해결됐다.
- meta_state: 272 groups·994 cases, META87·AUDIT87, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`. META78~87, AUDIT78/81/84/87 및 대응 depth_backfill 원장도 모두 반영됐다.
- Manifest: consumed_sdss 994·prepared 4. 나머지 네 건 G024 DR~DU는 기존 HOLD이며 actionable prepared 0이다. 임의 소비 금지.
- Crosswalk 미갱신: research crosswalk 903행·target crosswalk 1,147행은 신규 91건의 완료를 반영하지 않는다. 이번 작업에서는 crosswalk를 수정하지 않았다.
- 미해결 제한: AQW 경계 증거 unresolved, ASI site19 deferred, ATK 후보10 누락 및 법적 권리 자동박탈로 일반화 금지. 다음 연구는 새 blind source frontier를 준비한 뒤 시작한다.
- Quota unavailable이며 이는 quota 종료가 아니라 현재 actionable 준비목록 소진 상태다.

# Astra checkpoint — G252~G281 준비목록 소진·Luna sync 완료

## Luna sync 완료 — 2026-09-27 G252~G281 최종 준비목록 소진 checkpoint

- 이번 집계는 신규 G252~G281만 포함한다. 총 30 groups·86 cases·392 raw: blind 86, answer_check 88(최초 86 + ANI 보충 2), independent_code 86, sdss_compare 86, induction 30, META68~77 10, manual audit 3, depth_backfill 3건(총 6 cases). 이전 G232~G251은 제외했다.
- 30/30 group에서 최초 barrier인 전체 blind → 전체 최초 answer_check → 전체 independent_code → 전체 SDSS 순서를 통과했다. 최초 공식 대조 86건 중 85건 일치, ANI 최초 answer_check의 원장 필드 match=false를 불일치로 보존했다. ANI 보충 answer_check -02/-03은 최초 barrier 집계에서 분리했으며, ANG/ANH independent_code 뒤·ANI independent_code 앞에 append된 시점을 투명하게 기록한다.
- queue 4,083건·processed 4,083건·pending 0건. record_id 고유성과 모든 queue→processed ID 대응을 확인했다. 반영 스크립트는 queue 원장을 쓰지 않았다. 이전 baseline hash가 없어 세션 간 원문 payload hash 불변성은 별도 검증 불가다.
- meta_state.py: 242 groups·903 cases, META77, meta_due=false, manual_parity_audit_due=false(다음 audit까지 1회), depth_backfill_pending=[]·semantic_state_review=[]이다. manifest 907건은 consumed_sdss 903건과 prepared 4건으로, prepared 네 건 모두 G024 DR~DU hold다. 미소비·미제외로 보존하며 actionable prepared는 0이다.
- 이는 quota 종료가 아니라 현재 준비목록 소진 checkpoint다. quota unavailable 상태는 그대로 둔다. source/sealed를 읽지 않았다.

## Luna sync 완료 — 2026-09-21 G203~G221 최종 준비목록 소진 checkpoint

- G221 AJL~AJO 16단계 raw와 `G221-induction-20260921-01`을 반영했다. queue 3,295건·processed 3,295건·pending 0건이며 queue 원문은 불변이다.
- `meta_state.py`: 182 groups·730 cases, `meta_induction_count=57`, `last_manual_parity_audited_meta_count=57`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. META57과 최근 manual parity audit 2회, depth_backfill 11 cases의 상태를 반영했다.
- G203~G221은 19 groups·67 cases이며, queue/manifest 기계 점검에서 최종 유효 blind·independent_code barrier 누락은 각각 0건이었다. AIC·AIN·AIR·AIW의 과거 hold marker와 후속 해소 기록은 보존한다.
- manifest는 734건 중 `consumed_sdss` 730건·`prepared` 4건이다. 남은 DR~DU는 G024 SDSS 사전노출 hold이며 actionable READY는 0건이다. 이는 quota 종료나 전체 100코드 연구 완료가 아니라 현재 준비목록 소진 checkpoint다.
- 다음 작업은 새 canonical source 준비과 미확정 경계 반례 확보다. 기존 hold·후보/대표·최초 primary와 원문 출처 한계는 유지한다.

## Luna sync 완료 — 2026-09-15 G060 완료

- 이번 세션 시작 시점 실제 완료 집계 50 passage groups·206 cases에서 G052~G060 후속 raw와 META14·META15·META16, META15 audit, IO·IK depth_backfill을 반영해 최종 59 groups·232 cases가 되었다. G060 JB answer_check·independent_code·sdss_compare까지 처리했다.
- queue 1,111건·processed 1,111건·pending 0건. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. queue 원문은 불변이다.
- manifest prepared 4건은 모두 G024 DR~DU historical preexposure hold이며 actionable 잔량은 0건이다. 다음 Excel-style case `JC`는 미준비 상태이고, 추가 후보 준비·별도 비독립 검토는 후속 작업으로 남긴다.

## Luna sync 완료 — 2026-09-15 사용자 중지

- 직전 sync 이후 queue 미처리 32건을 원 payload 그대로 반영했다. queue 858건·processed 858건·pending 0건이며 queue 원문은 불변이다.
- `SESSION-hold-20260915-user-stop-01`을 마지막 hold로 processed에 기록했다. G042는 전체 단계 완료, G043은 GZ를 제외한 answer_check까지, G044는 answer_check까지 반영했다. G043/G044 independent_code·SDSS는 미착수로 보존한다.
- GZ blind ① 대 sealed 공식답 ⑤ 불일치는 `needs_astra_review`로 유지한다. 시험형 차이·정본 연결을 Luna가 추론하지 않았고, 성과상 정답 일치로 집계하지 않는다.
- 재개 시 첫 작업은 G043 GZ의 공식 답 번호·정본·시험형 대응 확인이다. G045/G046은 미열람이다. 사용자 중지 상태에서 Astra 연구를 재개하지 않는다.

```json
{
  "record_id": "SESSION-hold-20260915-user-stop-01",
  "case": "SESSION",
  "stage": "hold",
  "status": "done",
  "timestamp": "2026-09-15T05:22:17.374850+00:00",
  "payload": {
    "reason": "사용자가 현재까지 작업을 Luna 후처리한 뒤 정지하라고 지시함. quota threshold 또는 runtime emergency 중단이 아님.",
    "last_completed_atomic_record": "HD-answer_check-20260915-01",
    "last_regular_luna_sync": "SYNC-hold-20260915-three-groups-01",
    "completed_since_regular_sync": [
      "G042 blind/answer_check/independent_code/sdss_compare 전체"
    ],
    "G043": {
      "cases": [
        "GW",
        "GX",
        "GY",
        "GZ",
        "HA"
      ],
      "blind_done": [
        "GW",
        "GX",
        "GY",
        "GZ",
        "HA"
      ],
      "answer_check_done": [
        "GW",
        "GX",
        "GY",
        "HA"
      ],
      "answer_check_needs_astra_review": [
        "GZ"
      ],
      "independent_code_done": [],
      "sdss_compare_done": [],
      "sdss_disclosed": false
    },
    "G044": {
      "cases": [
        "HB",
        "HC",
        "HD"
      ],
      "blind_done": [
        "HB",
        "HC",
        "HD"
      ],
      "answer_check_done": [
        "HB",
        "HC",
        "HD"
      ],
      "independent_code_done": [],
      "sdss_compare_done": [],
      "sdss_disclosed": false
    },
    "GZ_unresolved": {
      "blind_selected_answer": 1,
      "sealed_official_answer": 5,
      "restored_source_form": "2011학년도 수능 언어영역 짝수형 질문 PDF",
      "restored_choice_1": "지구/회귀년/항성년",
      "judgment": "최초 의미 판단과 복원 선택지①은 대응하지만 sealed⑤와 번호 불일치. 시험형 차이 또는 정본 연결 문제인지 미확인. 후속 source read 전에 사용자 중지 지시를 받음.",
      "preserve": "최초 blind와 mismatch raw 모두 불변. 성과상 정답 일치로 집계 금지. Luna 추론으로 매핑 수정 금지."
    },
    "meta_state_last_sync": {
      "meta_induction_count": 10,
      "completed_groups_since_last_meta": 1,
      "completed_questions_since_last_meta": 3,
      "meta_due": false,
      "manual_parity_audit_due": false,
      "depth_backfill_pending": []
    },
    "next_work_if_resumed": "미처리 raw0 확인 후 G043 GZ 공식답 번호/정본·시험형 대응부터 직접 확인. G043 전체 answer_check가 유효 완료된 뒤 전체 independent_code→장벽 확인→SDSS. G044는 전체 independent_code부터. G042 비교 귀납은 향후 메타에서 포함. G045/G046 source·답·태그는 미열람.",
    "source_qualifications": [
      "GV/HD 그림 직접 판독 완료.",
      "GZ 선택지①~④ 및천체그림 직접 판독,⑤는 텍스트supplement 확인. [A] 하단 crop 경계 완전검증 미완료.",
      "기존 GL 수식·GR 사전 뜻·G024/DP/CZ/G032 등 유보 불변."
    ],
    "quota_status": "unavailable",
    "runtime_emergency_warning_observed": false,
    "new_semantic_work_after_stop": false,
    "luna_action": "신규 raw 차집합만 원 payload대로 기존 MD/JSONL 및processed에 반영. CURRENT/ASTRA_CHECKPOINT/handoff 최신화. 신규source/sealed/해설/코드판정 열람 및추론·backlog 준비 금지. GZ는needs_astra_review. queue원문불변. pending0 확인 보고 후 종료."
  }
}
```
<!-- luna-sync:SESSION20261002-hold-G399-G410-20261002 -->
# Astra checkpoint — G399~G410 완료·G411 미열람

- 최종 hold와 BACKFILL120-BFJ까지 반영했다. Queue=processed=5,873 unique, pending=0, duplicate=0, orphan=0. Hold 사유는 응답 작업예산이며 quota emergency/threshold 관측이 아니다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G399~G410 12 groups·36 cases의 실제 queue 줄 인덱스 장벽, 최초답=공식답, `exact_error`, record_id 중복을 기계 검증했다: stage barrier 위반 0, 답 불일치 0, exact_error 누락 0, 중복 0.
- 다음 frontier G411은 미열람·미노출이며 다음 blind 단계에서 시작한다. BEM 문맥 동일률 해석 유보와 기존 반모형 한정을 보존한다.
<!-- luna-sync:SESSION-hold-normal-quota-20261004-01-sync-20261004 -->
# Astra checkpoint — 정상 quota handoff·G502 SDSS 대기

- G502 BPR·BPS·BPT의 blind/answer_check/independent_code 9 raw와 정상 quota hold 1건까지 반영했다. Queue=processed=7,128 unique, pending=0, duplicate=0, orphan=0.
- 세 최초 답 ②·③·③은 공식 답과 일치한다. `past_exposure=unknown`, `strict_blind_eligible=false`를 보존한다. G502 전체 SDSS compare와 induction은 미완료이며 SDSS를 Luna가 열거나 보완하지 않았다.
- `meta_state.py`: 461 groups·1,560 cases, META150 이후 1/3, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 이번 run 완료 범위는 G481~G501이며 BNQ 최초 오답 기록의 기존 제한을 유지한다. 다음 Astra는 G502 전체 SDSS 공개·대조부터 재개하고 G503은 미열람이다. 연구 완료·backlog 소진이 아니다.
- hold 사유는 주간 remaining 7%(used 93%) 정상 threshold handoff, primary 5h=null이며 runtime emergency가 아니다.
