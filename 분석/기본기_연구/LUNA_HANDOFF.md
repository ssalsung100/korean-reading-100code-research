<!-- 종료 gate D — 2026-10-05 -->
## 최신 상태 — 종료 gate D 판정 기록

- 연구 전체 완료·미완료 8 cases 완료 처리·제외를 뜻하지 않는다. 이번 연속 연구는 gate D에서 중단 판정되었으며 quota 중단이나 emergency가 아니다.
- Queue/processed=7,605 unique, pending=0, duplicate/orphan=0. 누계 497 groups·1,663 completed cases; meta=162, manual audit=162, meta/audit due=false, depth/semantic pending 없음.
- 남은 hold: G024 DR/DS/DT/DU 4건은 사전 SDSS 장벽 때문에 현재 절차상 independent 판단 불가. 재개에는 명시적 비독립 검토 절차가 필요하다. G370 BAP/BAQ/BAR/BAS 4건은 공식 원문 렌더 및 blind source에 본문이 없어 질문 전용 원문 복원이 필요하다. 현재 actionable=0.
- 최근 run G510~G537: 28 groups·78 cases, 기본 4단계 및 induction; META154~162, audits 156/159/162, depth backfill BQC/BQT/BRJ/BSA/BSD/BRN/BSP/BSL/BTH. 모두 strict-blind 실적에서 제외.

<!-- luna-sync:SESSION20261005-G537-induction-sync-20261005 -->
## 최신 Luna sync — G537 induction 반영·G024/G370 hold 검토 대기

- G537 induction raw 1건을 기존 기록에 의미 변경 없이 반영했다.
- Queue=processed=7,602 unique, pending=0, duplicate/orphan=0. `meta_state.py`: latest META162, 497 groups·1,663 cases, META162 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Prepared manifest의 마지막 ID까지 기본 단계가 저장되었지만 G024·G370의 최소 hold 기록 2 groups·8 cases가 남아 있다. 주 Astra가 hold raw를 직접 검토해 다음 단계와 범위를 결정할 때까지 완료·종료로 표시하지 않는다.
<!-- luna-sync:SESSION20261005-BQC-G510-sync-20261005 -->
## 최신 Luna sync — G510 induction 반영·G511 frontier

- BQC depth_backfill과 G510 전체 raw를 기존 자산에 의미 변경 없이 반영했다. 원raw의 `同じ` 입력 표기는 보존하고, 가독성 주석에서만 `같은`으로 풀어 적었다. 이미 processed인 BQI backfill은 재반영·재연구하지 않았다.
- Queue=processed=7,252 unique, pending=0, duplicate/orphan=0. `meta_state.py`: 470 groups·1,588 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`. Manifest=1,671 cases.
- 다음 frontier G511: BQT — `data/기본기_연구/prepared_backlog/blind_sources/BQT.json` (prepared, 존재); BQU — `data/기본기_연구/prepared_backlog/blind_sources/BQU.json` (prepared, 존재); BQV — `data/기본기_연구/prepared_backlog/blind_sources/BQV.json` (prepared, 존재). 이번은 정상 연구 중 sync이며 종료/hold가 아니다.

<!-- luna-sync:SESSION-hold-normal-quota-20261004-01-sync-20261004 -->
## 최신 Luna sync — 정상 quota handoff·G502 SDSS 대기

- G502 BPR·BPS·BPT 9 raw와 hold 1건 반영. Queue=processed=7,128 unique, pending=0, duplicate/orphan=0.
- 최초 답 ②·③·③은 공식 답과 일치하지만 strict blind eligible=false. SDSS compare·induction 미완료이며 G503 미열람이다.
- `meta_state.py`: 461 groups·1,560 cases, META150 이후 1/3; due/depth/semantic review 없음. 이번 run G481~G501 완료 및 BNQ 최초 오답 제한 보존.
- 주간 used 93%/remaining 7% 정상 handoff, primary 5h=null, runtime emergency 없음. 다음 Astra는 G502 SDSS부터 재개한다.

<!-- luna-sync:SESSION20261002-G426-partial-sync-20261002 -->
## 최신 Luna sync — G426 9 raw 반영·SDSS 대기

- BHA·BHB·BHC blind·answer_check·independent_code 총 9 raw를 반영했다. Queue=processed=6,075 unique, pending=0, duplicate=0, orphan=0. G426의 SDSS 공개·대조와 induction은 아직 queue에 없으므로 미완료 상태다.
- 세 최초 답 ③·⑤·②는 각 공식 답과 일치한다. `past_exposure=unknown`, `strict_blind_eligible=false`를 보존하고 엄격 blind 성과로 계산하지 않는다. 세 blind source 모두 `blind_only=true`이며 공식답·SDSS·기존 판정 필드가 없다.
- `meta_state.py` 동기화: 완료 385 groups·1,335 cases, `meta_due=false`, `manual_parity_audit_due=false`, depth backfill=[], semantic review=[]. Manifest prepared 333건(hold 포함), 다음 ID BHD; 최소 임계치 미만이 아니므로 기계적 후보 준비 불필요.
- 다음 허용 Astra 단계는 G426 전체 independent-code barrier 확인 후 SDSS 공개·대조다. 그 다음 induction 단계가 해결되기 전 신규 group을 시작하지 않는다.

<!-- luna-sync:SESSION20261002-G384-G385-context-handoff -->
## 최신 Luna sync — G384 완료·응답/컨텍스트 인계·G385 미열람

- G384 induction 및 `SESSION20261002-hold-G376-G384-context-01` raw까지 반영했다. Queue=processed=5,510 unique, pending=0, duplicate=0, orphan=0. 인계 사유는 응답·컨텍스트 예산이며 quota emergency가 아니다. raw의 `quota_status=unavailable`은 unavailable 그대로 보존한다.
- G376~G384 9 groups·28 cases 기계검증: 모든 group에서 blind 전체 → 최초 answer_check 전체 → independent_code 전체 → SDSS compare 전체 순서 통과, barrier/coverage 위반 0. 최초답 공식 일치 27/28(BCF만 불일치), 선택답=매력 오답 중복 0/28, `exact_error` 누락·공백 0/28.
- `meta_state.py`: 완료 344 groups·1,215 research cases, META111 이후 1 group·4 cases; `meta_due=false`, `manual_parity_audit_due=false`, depth backfill=[], semantic review=[].
- 다음 frontier G385는 미열람·미노출(blind source/공식답/SDSS/기존 판정 모두 false). 다음 단계는 새 Astra 세션에서 AGENTS/CURRENT/ASTRA_START 확인 후 meta_state/quota/pending 점검, 이어 G385 group blind다. 미완료 semantic stage 없음.
- BCF 최초답 실패와 ㄹ 배제·공식 정답 유일성 미해결, BBS 간접조건 유보는 그대로 유지하며 사후에 최초 기록을 덮어쓰지 않는다.

# 최신 Luna sync — G366~G375 마감·G376 미열람 frontier

- Session hold까지 반영. 응답·컨텍스트 예산 인계, quota emergency 아님. Queue=processed=5,381 unique, pending=0, duplicate/orphan=0.
- G366~G369·G371~G375 9 groups·28 cases: 네 stage 28/28, barriers 0 위반, 최초답 일치 28/28, blind-answer 불일치 0, 매력 오답=선택 답 중복 0, exact_error 누락 0. G370 BAP~BAS hold 4건은 완료분모 제외.
- `meta_state.py`: 335 groups·1,187 cases; META108 이후 1/3; meta/audit due false, depth/semantic pending 없음.
- Manifest prepared 484/1,671; actionable 476 (G024 hold4, G370 source hold4 제외). G376 manifest-only IDs BBI·BBJ·BBK; source 미열람.
- G368 restoration/strict limits, G370 source hold, G372 BAW81/BAX44 및 BACKFILL108, G373 tag100/BBB18 유보, G375 official diagram provenance/source-quality hold를 보존.

# Luna handoff
<!-- luna-sync:SESSION-G347-G364-G365-resume-20260928 -->
## 최신 Luna handoff — G347~G364 검증·G365 새 세션 재개

- Session hold raw까지 반영: queue=processed=5,234 unique, pending0, duplicate/orphan0. 응답·컨텍스트 예산 인계이며 quota emergency가 아니다.
- Queue-order audit: 18 groups·56 cases; 각 blind/answer_check/independent_code/sdss_compare 56건, 두 group stage barrier 위반 0, coverage 오류 0. 이번 최초답 공식 일치 56/56.
- `meta_state.py`: 325 groups·1,156 research cases; META105 이후 0/0; meta/audit due false, depth pending=[], semantic review=[]. 사이트 전체 1,147과 research 1,156은 다른 분모.
- Prepared 24건(기존 G024 HOLD 4건, actionable 20건). G365 첫 case AZZ; group blind source와 정답/SDSS/기존판정 미열람. 새 세션 초기 확인 후 G365 group blind부터 재개한다. 연구 완료 아님.
- AYP/AZI 오답 기록 품질 제한, 기존 hold·실패·노출 및 분수계수 전사 유보를 유지한다.

<!-- luna-sync:AUDIT105-AZW-backfill-lock-20260928 -->
## 최신 Luna sync — AUDIT105 반영·AZW backfill 선행·G365 잠금

- AUDIT105 raw 1건을 반영했다. Queue=processed=5,232 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 325 groups·1,156 cases, META105 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["AZW"]`, `semantic_state_review=[]`.
- AZW depth_backfill 반영 및 sync 전까지 G365는 잠긴다.
- AYP·AZI irreversible 품질 제한과 기존 site/code range, hold, exposure 유보를 유지한다.

<!-- luna-sync:META105-AUDIT105-lock-20260928 -->
## 최신 Luna sync — META105 반영·AUDIT105 선행·G365 잠금

- META105와 G364 induction raw 각 1건을 반영했다. Queue=processed=5,231 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 325 groups·1,156 cases, META105 이후 0/0, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- AUDIT105 및 지정 backfill의 raw 저장과 sync 전까지 G365는 잠긴다.
- 기존 사이트·코드 범위 유보와 품질·hold·exposure 제한을 유지한다.

<!-- luna-sync:G364-META105-lock-20260928 -->
## 최신 Luna sync — G364 반영·META105 선행·G365 잠금

- G364 전체 stage raw 12건과 G363 induction 1건을 반영했다. Queue=processed=5,229 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 325 groups·1,156 cases, META104 이후 3/9, `meta_due=true`, `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Astra 보고상 최초 답 ③·②·①은 공식 답과 일치한다. G364 induction/META105, AUDIT105, 필요한 backfill sync 전까지 G365는 잠긴다.
- 사이트·코드 범위 유보와 기존 품질·exposure 제한을 그대로 보존한다.

<!-- luna-sync:G363-G364-frontier-20260928 -->
## 최신 Luna sync — G363 반영·G364 frontier

- G363 전체 stage raw 12건과 G362 induction 1건을 반영했다. Queue=processed=5,216 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 324 groups·1,153 cases, META104 이후 2/6, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Astra 보고상 최초 답 ⑤·①·⑤는 공식 답과 일치한다. 그림 3개 JPG 직접 확인 이력을 보존한다. 사이트 87은 공간 농도 그래프 범위 후보이며 기울기 수치 계산으로 판단하지 않는다.
- 다음 frontier는 G364이며 G363 induction raw 추가 대기다.

<!-- luna-sync:G362-G363-frontier-20260928 -->
## 최신 Luna sync — G362 반영·G363 frontier

- G362 전체 stage raw 12건을 반영했다. Queue=processed=5,203 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 323 groups·1,150 cases, META104 이후 1/3, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Astra 보고상 최초 답 ④·⑤·④는 공식 답과 일치한다. AZS95는 기준 필요성과 특정 해결 방법의 유일 필요성을 구별해 유보한다.
- 다음 frontier는 G363이며 G362 induction raw는 Astra 추가 대기다. 서로 다른 분모의 research/site totals를 혼합하지 않는다.

<!-- luna-sync:META104-G362-frontier-20260928 -->
## 최신 Luna sync — META104 반영·G362 frontier

- G361 induction 및 META104 raw 각 1건을 반영했다. Queue=processed=5,191 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 322 groups·1,147 research cases, META104 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G362다. Research cases 1,147과 사이트 전체 1,147은 서로 다른 분모다.
- AZO 원 hold, AYP·AZI 품질 제한 및 기존 전사·범위·노출 유보를 보존한다.

<!-- luna-sync:G361-META104-lock-20260928 -->
## 최신 Luna sync — G361 반영·META104 선행·G362 잠금

- G361 네 사례 전체 stage raw 16건, AZO hold, G360 induction 1건을 반영했다. Queue=processed=5,189 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 322 groups·1,147 cases, META103 이후 3/10, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Astra 보고상 최초 답 ①·⑤·①·④는 공식 답과 일치한다. G361 induction/META104 저장과 sync 전까지 G362는 잠긴다.
- AZO 원 hold는 보존한다. 복원 blind의 provenance는 공식 강조구 보충파일 범위이며 기존 유보·품질·노출 제한을 유지한다.

<!-- luna-sync:G360-G361-frontier-20260928 -->
## 최신 Luna sync — G360 반영·G361 frontier

- G360 전체 stage raw 12건과 G359 induction 1건을 반영했다. Queue=processed=5,171 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 321 groups·1,143 cases, META103 이후 2/6, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Astra 보고상 G360 최초 답 ①·③·④는 공식 답과 일치한다. 근거는 신채호 논설의 문항 내 해석이며 외부 역사 사실 검증이 아니고, 사이트 범위 미확정은 보존한다.
- 다음 frontier는 G361, G360 induction raw는 Astra 추가 대기다.

<!-- luna-sync:G359-G360-frontier-20260928 -->
## 최신 Luna sync — G359 반영·G360 frontier

- G359 전체 stage raw 12건을 반영했다. Queue=processed=5,158 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 320 groups·1,140 cases, META103 이후 1/3, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- AZI blind 매력 오답 번호가 선택 답④로 잘못 입력되어 answer_check에서 사후 보충된 제한을 기록했다. 선택 답 정확성과 최초 오답 분석 완비 여부는 분리하고, AYP와 함께 최초 오답 분석 완비 성과에서 제외한다. 원blind는 수정하지 않는다.
- 다음 frontier는 G360이며 G359 induction raw는 Astra 추가 대기다.

<!-- luna-sync:META103-G359-frontier-20260928 -->
## 최신 Luna sync — META103 반영·G359 frontier

- G358 induction과 META103 raw 각 1건을 반영했다. Queue=processed=5,146 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 319 groups·1,137 cases, META103 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G359다. 사이트 범위 미확정과 기존 quality/hold/exposure 제한을 raw대로 보존한다.

<!-- luna-sync:G358-META103-lock-20260928 -->
## 최신 Luna sync — G358 반영·META103 선행·G359 잠금

- G358 전체 stage raw 12건과 G357 induction 1건을 반영했다. Queue=processed=5,144 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 319 groups·1,137 cases, META102 이후 3/9, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G358 induction/META103 raw 저장과 sync 전까지 G359는 잠긴다.
- 사이트 범위 미확정은 raw대로 보존한다. AZC19 유보와 기존 AYP 품질 제한·hold·exposure 이력도 유지한다.

<!-- luna-sync:G357-G358-frontier-20260928 -->
## 최신 Luna sync — G357 반영·G358 frontier

- G357 전체 stage raw 12건과 G356 induction 1건을 반영했다. Queue=processed=5,131 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 318 groups·1,134 cases, META102 이후 2/6, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Astra 보고상 최초 답 ②·①·①은 공식 답과 일치한다. 다음 frontier는 G358이며, AZC 사이트 19 범위 유보를 유지한다.
- G357 induction raw는 Astra 추가 대기다. 기존 source hold·노출·성과 제한을 보존한다.

<!-- luna-sync:G356-G357-frontier-20260928 -->
## 최신 Luna sync — G356 반영·G357 frontier

- G356 세 사례의 전체 stage raw 12건을 반영했다. Queue=processed=5,118 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 317 groups·1,131 cases, META102 이후 1/3, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Astra 보고상 최초 답 ③·④·④는 공식 답과 일치한다. Blind raw 기록대로 Astra가 원 TIFF의 RGB PNG 변환본을 확인했으며, 원 TIFF와 노출 기록을 유지한다. 외부 source 열람은 없었다.
- G356 induction raw는 Astra 추가 대기다. 다음 frontier는 G357이다.

<!-- luna-sync:BACKFILL102-G356-frontier-20260928 -->
## 최신 Luna sync — BACKFILL102 반영·G356 frontier

- `BACKFILL102-depth_backfill-20260928-01` 1건을 반영했다. Queue=processed=5,106 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 316 groups·1,128 cases, META102 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- AYQ·AYT 지정 backfill 반영이 끝나 G356 잠금이 해제됐다. 다음 frontier는 G356이다.
- AYP 품질 제한 및 AYE hold·복원 blind 등 기존 원기록·유보를 보존한다.

<!-- luna-sync:AUDIT102-AYQ-AYT-backfill-lock-20260928 -->
## 최신 Luna sync — AUDIT102 반영·AYQ/AYT backfill 선행·G356 잠금

- AUDIT102 raw 1건을 반영했다. Queue=processed=5,105 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 316 groups·1,128 cases, META102 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["AYQ", "AYT"]`, `semantic_state_review=[]`.
- AYQ·AYT depth_backfill sync 전까지 G356은 잠긴다. Astra가 depth raw를 작성한다.
- AYP 최초 오답 분석 품질 제한은 irreversible로 유지한다. G354 raw의 AYU/AXU 정정 연결도 원raw를 고치지 않는다.

<!-- luna-sync:G355-META102-AUDIT102-lock-20260928 -->
## 최신 Luna sync — G355 반영·META102/AUDIT102 선행·G356 잠금

- G355 전체 stage raw 12건과 G354 induction 1건을 반영했다. Queue=processed=5,102 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 316 groups·1,128 cases, META101 이후 3/9, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- META102·AUDIT102와 필요한 backfill의 sync 전까지 G356은 잠긴다.
- G354 induction의 `AYU의 59/80`은 Astra가 `AXU`로 정정할 예정인 typo다. raw 원문은 보존하고, Luna는 해석상 보정하지 않는다. AYP blind 사후 보충의 성과 비소급 제한도 유지한다.

<!-- luna-sync:G354-G355-frontier-20260928 -->
## 최신 Luna sync — G354 반영·G355 frontier

- G354 전체 stage raw 12건과 G353 induction 1건을 반영했다. Queue=processed=5,089 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 315 groups·1,125 cases, META101 이후 2/6, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G355이며 G354 induction은 Astra 추가 대기다.
- AYP blind 오류의 사후 보충 및 원blind 불변·성과 비소급 제한을 유지한다.

<!-- luna-sync:G353-G354-frontier-20260928 -->
## 최신 Luna sync — G353 반영·G354 frontier

- G353 AYO·AYP·AYQ 전체 stage raw 12건을 반영했다. Queue=processed=5,076 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 314 groups·1,122 cases, META101 이후 1/3, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Astra 보고상 최초 선택 답 3건은 공식 답과 일치한다. AYP blind의 매력 오답 필드에 선택 답②가 잘못 입력되어 answer_check에서 사후 보충된 품질 제한을 보존한다. 원blind는 수정하지 않고 최초 오답 분석 성과로 소급하지 않는다.
- 다음 frontier는 G354다.

<!-- luna-sync:META101-G353-frontier-20260928 -->
## 최신 Luna sync — META101 반영·G353 frontier

- G352 induction 및 META101 raw 각 1건을 반영했다. Queue=processed=5,064 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 313 groups·1,119 cases, META101 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G353이다. 기존 AYE hold·복원 blind 기록 및 G348 전사 한계를 유지한다.

<!-- luna-sync:G352-META101-lock-20260928 -->
## 최신 Luna sync — G352 반영·META101 선행·G353 잠금

- G352 AYL·AYM·AYN stage raw 12건을 기존 스크립트로 반영했다. Queue=processed=5,062 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 313 groups·1,119 cases, META100 이후 3/10, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Astra 보고상 G352 최초 답 ④·⑤·②는 공식 답과 일치한다. 다음은 Astra의 G352 induction 및 META101 raw이며, sync 전까지 G353은 잠근다.
- AYE source hold와 복원 blind 기록, G348 안테나 분수계수 전사 누락 한계를 보존한다.

<!-- luna-sync:G350-G351-G352-frontier-20260928 -->
## 최신 Luna sync — G350·G351 반영·G352 frontier

- G350 AYE·AYF·AYG, G351 AYH·AYI·AYJ·AYK의 전체 단계 28건, AYE source hold 1건, G350·G351 induction 각 1건을 반영했다. Queue=processed=5,050 unique, pending0, duplicate/orphan0.
- `meta_state.py`: 312 groups·1,116 cases, META100 이후 2/7, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 일곱 사례는 모두 manifest상 `consumed_sdss`; 두 induction도 반영됐다. 다음 frontier는 G352 AYL~AYN이다.
- AYE 원 source hold와 복원 blind raw를 각각 보존하며, 사이트와 독립 판정 차이·미확정은 raw대로 유지한다. 세 번째 group 완료 때 due 단계의 sync를 우선한다.

<!-- luna-sync:BACKFILL99-G347-frontier-20260928 -->
## 최신 Luna sync — BACKFILL99 반영·G347 AXV frontier

- `BACKFILL99-depth_backfill-20260928-01`을 독립연구 진행 기록과 processed 원장에 원문 의미 변경 없이 반영했다. AXU 주코드 변경 제안 75→59 및 최초 주75 보존을 함께 기록했다.
- Queue=processed=4,978 unique, pending raw=0, duplicate/orphan 0이다. `meta_state.py`: 307 groups·1,100 cases, META99 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 manifest상 prepared인 G347 AXV다. AUDIT99 지정 backfill 완료로 G347 잠금이 해제됐다.

<!-- luna-sync:G342-crosswalk-frontier-20260928 -->
## 최신 Luna sync — crosswalk 반영·G342~G370 READY

- Research complete 1,084. Target crosswalk 547/1,147 complete·600 remaining; research crosswalk 1,084 rows(547 TARGET_MATCHED, 537 NON_TARGET_RESEARCH). G312~G341 90 cases는 전부 TARGET_MATCHED. duplicates 0, HOLD/AMBIGUOUS overlap 0.
- Queue=processed=4,903 unique, pending0. G312~G341 barrier 30/30. 신규90 최초89/90; AVE 최초③·공식⑤·.91 실패 및 strict 미확정 불변.
- Manifest consumed_sdss 1,084·prepared 96: G342~G370 29 groups·92 LEET READY(첫 AXF), G024 DR/DS/DT/DU HOLD4. 신규 READY 이 cohort 바깥 추가분 0.
- Target remaining categories: READY244, NEEDS_RESTORE335, SOURCE_MISSING9, HOLD4, AMBIGUOUS8. Categories and research total are different views; no merged rate.
- Preflight report: `prepared_backlog/LUNA_FRONTIER_PREFLIGHT_20260928_G342.md`. meta/audit/backfill due false; depth_backfill_pending=[], semantic_state_review=[].

<!-- luna-sync:G312-G341-final-sync-20260928 -->
## 최종 Luna sync — 90 cases 반영·actionable prepared 0

- 전체 연구 1,084 cases. G312~G341의 90 cases stage barrier 30/30 통과, queue=processed 4,903 unique, pending0, duplicate0.
- 이번 90 최초 답 89/90; AVE ③/공식⑤/.91 최초 실패 불변. 노출 이력 미확인으로 strict 성과 확정하지 않는다.
- Manifest consumed_sdss 1,084·prepared 4. 남은 네 건은 G024 DR~DU HOLD라 actionable prepared 0.
- Target/research crosswalk는 이 cohort 미반영 상태(기존 1,147/994 rows); crosswalk 분모와 연구 완료 수를 합산하지 않는다.
- META88~97, AUDIT90/93/96, BACKFILL90/93/96 보존. due false, depth_backfill_pending=[], semantic_state_review=[].

<!-- luna-sync:META97-G341-frontier-20260928 -->
## 최신 Luna 정기 sync — G340·META97 반영·G341 frontier

- G340 hold·stage·induction 및 META97을 반영했다. Queue=processed=4,890, unique ID 4,890, pending raw 0이다.
- meta_state: 301 groups·1,081 cases, META97 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`(다음 2회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- AXB hold raw 보존과 `resolved_hold` blind 연결, 공식 문제 표18 복원 provenance를 유지한다. 신규87 최초86/87은 strict 미확정이며 기존 AVE 실패도 보존한다.

<!-- luna-sync:G339-state-20260928 -->
## 최신 Luna 정기 sync — G339 반영·G340 frontier

- G339 stage raw 12건과 induction 1건을 반영했다. Queue=processed=4,875, unique ID 4,875, pending raw 0이다.
- meta_state: 300 groups·1,078 cases, META96 이후 2/6, `meta_due=false`, `manual_parity_audit_due=false`(다음 3회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 G340이다. AWW93 범위 유보, 신규84 최초83/84 strict 미확정 및 AVE 최초 실패를 보존한다.

<!-- luna-sync:G338-state-20260928 -->
## 최신 Luna 정기 sync — G338 반영·G339 frontier

- G338 stage raw 12건과 induction 1건을 반영했다. Queue=processed=4,862, unique ID 4,862, pending raw 0이다.
- meta_state: 299 groups·1,075 cases, META96 이후 1/3, `meta_due=false`, `manual_parity_audit_due=false`(다음 3회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 G339이다. AWT98/AWU42 후보 누락, AWV48 유보, 신규81 최초80/81 strict 미확정을 보존한다.

<!-- luna-sync:BACKFILL96-G338-frontier-20260928 -->
## 최신 Luna 정기 sync — AUDIT96 backfill 완료·G338 frontier

- AUDIT96와 BACKFILL96을 반영했다. Queue=processed=4,849, unique ID 4,849, pending raw 0이다.
- meta_state: `meta_due=false`, `manual_parity_audit_due=false`(다음 3회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- G338 gate가 열렸다. 미확정 경계를 강제 해소하지 않고 최초 판정을 유지한다. 신규78 최초77/78 strict 미확정 및 TIFF 원본 불변/PNG 직접 확인을 보존한다.

<!-- luna-sync:META96-AUDIT96-due-20260928 -->
## 최신 Luna 정기 sync — META96 반영·AUDIT96 선행

- G337 stages·induction과 META96을 처리했다. Queue=processed=4,847, unique ID 4,847, pending raw 0이다.
- meta_state: 298 groups·1,072 cases, `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음은 AUDIT96 및 필요 backfill sync다. 신규78 최초77/78 strict 미확정, AWQ47·AWS86 유보, TIFF 원본 불변/PNG 직접 확인을 보존하며 G338은 gate 해소 전 보류한다.

<!-- luna-sync:G336-state-G337-frontier-20260928 -->
## 최신 Luna 정기 sync — G336 반영·G337 frontier

- G336 stage raw 12건과 induction 1건을 반영했다. Queue=processed=4,833, unique ID 4,833, pending raw 0이다.
- meta_state: 297 groups·1,069 cases, META95 이후 2/6, `meta_due=false`, `manual_parity_audit_due=false`(다음까지 1회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 죄와 벌 지문은 기존 이민선·벤야민 법/폭력 인접 노출과 불일치하여 strict 제외를 적용하지 않는다. 신규75 최초74/75는 strict 성과 미확정이다.

<!-- luna-sync:G335-exposure-G336-frontier-20260928 -->
## 최신 Luna 정기 sync — G335 반영·인접 지문 노출 기록

- G335 stage raw 12건과 induction 1건을 반영했다. Queue=processed=4,820, unique ID 4,820, pending raw 0이다.
- meta_state: 296 groups·1,066 cases, META95 이후 1/3, `meta_due=false`, `manual_parity_audit_due=false`(다음까지 1회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- G335 visual의 LEET2023 Q28~30 벤야민 법/폭력 지문 일부 인접 노출과 정답·SDSS 미노출을 raw대로 보존한다. 정본 일치가 확인된 후속 group만 strict blind 제외하며, 아직 매핑되지 않은 case는 임의 제외하지 않는다. 후속 sealed는 열지 않았다.

<!-- luna-sync:META95-G335-frontier-20260928 -->
## 최신 Luna 정기 sync — META95 반영·G335 frontier

- G334 raw와 META95 raw 1건을 반영했다. Queue=processed=4,807, unique ID 4,807, pending raw 0이다.
- meta_state: 295 groups·1,063 cases, META95 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`(다음까지 1회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- G333 인접 이민선 지문 노출과 G334 blind-only 경제 가능곡선 지문의 불일치를 구별했다. G334에 strict blind 제외를 적용하지 않는다. 다음 AUDIT96 carryover와 신규69 strict 미확정을 보존한다.

<!-- luna-sync:G332-state-20260928 -->
## 최신 Luna 정기 sync — G332 반영·G333 frontier

- G332 AWB/AWC/AWD stage raw 12건과 induction 1건을 반영했다. Queue=processed=4,780, unique ID 4,780, pending raw 0이다.
- meta_state: 293 groups·1,057 cases, META94 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음까지 2회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 G333이다. AWB93·AWC80 site 범위 및 AWD18 역설/엄밀 모순 구분, 신규63 최초62/63 strict 미확정을 보존한다.

<!-- luna-sync:G312-META87-status-20260928 -->
## 최신 Luna 정기 sync — G312 및 META87 상태 확인

- G312 ATT/ATU/ATV의 stage raw 12건과 induction raw 1건을 기존 스크립트로 반영했다. Queue=processed=4,509, unique ID 4,509, pending raw 0이다.
- meta_state: 273 groups·997 cases, META87 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 G313이다. ATT10 최초 경쟁 후보 누락, ATU site7·선지 함축 범위, MEET 근거의 KICE 전이 한계를 unresolved로 보존했다. 의미 재판정이나 source/sealed 열람은 하지 않았다.

<!-- luna-sync:META58-20260922 -->
## Luna 역할 sync — G223 귀납·META58 반영 완료·G224 frontier

- `G223-induction-20260922-01` 및 `META-G221-G222-G223-meta_induction-20260922-58` raw 2건을 절차 기록에 원문 의미 변경 없이 반영했다. AJU 47의 보조 후보 지위를 그대로 보존했다.
- Astra가 알려 준 `②⑤以` → `②·⑤는` 입력 오타는 문서 주석만 추가하고 immutable raw를 보존했다.
- queue 3,323건·processed 3,323건·pending raw 0건. `meta_induction_count=58`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 완료 184 groups·736 cases. 다음 frontier는 **G224 AJV~AJX**이다. META58 due 단계 반영·sync 및 pending 0 검증을 완료했다.
- 기본 모델 보조 에이전트가 Luna의 기계적 반영·상태 관리 역할만 수행했다. source·sealed 열람과 의미 재판정은 수행하지 않았다.

<!-- luna-sync:G223-stages-20260922 -->
## Luna 역할 sync — G223 전체 단계 반영·META58 due

- AJS·AJT·AJU의 blind·answer_check·independent_code·sdss_compare 12 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. G223 induction과 META58은 부모 Astra의 판단 대기 상태이다.
- queue 3,321건·processed 3,321건·pending raw 0건. 완료 184 groups·736 cases, META57 이후 3 groups·10 cases이다. `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 허용 단계는 G223 induction 및 META58이다. due 의미 단계와 Luna sync 및 pending 0 검증 완료 전 **G224 진입 금지** 상태를 보존한다.
- 기본 모델 보조 에이전트가 Luna 상태 관리 역할만 수행했다. source·sealed 자료를 읽거나 의미를 생성하지 않았다.

<!-- luna-sync:G222-induction-20260922 -->
## Luna 역할 sync — G222 귀납 반영 완료

- `G222-induction-20260922-01` raw 1건을 절차 기록에 의미 변경 없이 반영했다. Astra가 알려 준 `②は` → `②는` 입력 오타는 문서 주석으로만 표시하고 raw를 보존했다.
- queue 3,309건·processed 3,309건·pending raw 0건이다. G222 induction 완료, 다음 frontier는 **G223 AJS~AJU**이다. source·sealed 열람과 의미 재판정은 수행하지 않았다.

<!-- luna-sync:G222-stages-20260922 -->
## Luna 역할 sync — G222 전체 단계 반영·G223 frontier

- AJP·AJQ·AJR의 blind·answer_check·independent_code·sdss_compare 12 raw를 기존 스크립트로 의미 변경 없이 반영했다. G222 induction은 부모 Astra의 별도 판단 대기 상태이다.
- queue 3,308건·processed 3,308건·pending raw 0건. 완료 183 groups·733 cases이며 META57 이후 2 groups·7 cases이다. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest 821건 중 consumed_sdss 733건·prepared 88건이며 G024 hold 4건을 제외한 잔여 prepared는 84건이다. 다음 frontier는 **G223 AJS~AJU**이다.
- 기본 모델 보조 에이전트가 Luna의 기계적 상태 관리 역할을 수행했다. source·sealed 신규 열람과 의미 판단은 수행하지 않았다.

<!-- luna-sync:AJI-revision-G222-frontier-20260922 -->
## Luna 역할 sync — AJI 경계 수정 반영·실제 G222 frontier 복원

- `AJI-boundary_revision-20260922-01` raw 1건을 기존 `scripts/luna_process_handoff.py`로 AJI SDSS대조 문서와 processed 원장에 의미 변경 없이 반영했다. 원래 판단·blind는 보존했다.
- queue 3,296건·processed 3,296건·pending raw 0건. 완료 182 groups·730 cases, META57 이후 1 group·4 cases이다. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 실제 manifest는 821건이며 `consumed_sdss` 730건·`prepared` 91건이다. G024 DR~DU hold 4건을 제외하면 G222~G251의 87건이 이미 준비되어 있다. 아래 과거 기록의 READY 0 설명은 최신 파일 상태로 대체한다.
- 다음 frontier는 **G222 AJP~AJR**이다. G223 AJS~AJU, G224 AJV~AJX까지 본문·발문·보기·선지·지시대상·SHA-256·blind/sealed 분리를 재확인했다. 새 source 중복 생성은 하지 않았다. 점검: `data/기본기_연구/prepared_backlog/LUNA_G222_G224_RECHECK_20260922.md`.
- 지정 `gpt-5.6-luna` 모델 실행 불가로 이번 보조 에이전트는 기본 모델에서 Luna의 기계적 반영·상태 관리 역할을 수행했다. 지정 모델 실행으로 기록하지 않는다. 의미 재판정은 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 META51 grouped depth_backfill 완료·checkpoint

- `AUDIT51-sixcases-depth_backfill-20260920-01` grouped raw 1건을 원문 의미 변경 없이 절차 기록과 AFQ·AGT·AGC·AFV·AGW·AGJ 각 case 문서에 연결했다. 최초 raw와 후보/대표 구조, AGJ 63 및 65/62/4 역할을 보존했다.
- queue 2,993건·processed 2,993건·pending 0건이며 `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- prepared 4건은 G024 DR~DU의 SDSS 사전노출 barrier hold로 actionable 0건이다. canonical passages 163개 연결·미사용 0 상태를 보존했다.
- 이번 window는 2,750→2,993, 243 raw 증가와 11 groups·57 cases 완료(신규 직접 blind 47, 후속 10)로 기록한다. G193/G168 strict 제외와 공식 답 기계 연결 한계를 유지한다.
- quota unavailable은 관측되었으나 runtime emergency 경고는 없었으며, 이는 quota 종료가 아니라 현재 준비 가능 코퍼스 소진 checkpoint다. 전체 100코드 연구 완료로 표현하지 않는다.

## 최신 Luna 정기 sync — 2026-09-20 META51 manual parity audit 반영

- `AUDIT-meta51-manual_parity_audit-20260920-17` raw 1건을 원문 의미 변경 없이 반영했다. AGE 23 유지 근거와 AGJ 원문 단초·강도 gap을 보존했다.
- queue 2,992건·processed 2,992건·pending 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `last_manual_parity_audited_meta_count=51`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=["AFQ", "AFV", "AGC", "AGJ", "AGT", "AGW"]`, `semantic_state_review=[]`이다.
- Astra의 grouped depth_backfill 6-case 의미 보강을 대기 중이며 depth 완료 전 최종 상태로 승격하지 않는다.

## 최신 Luna 정기 sync — 2026-09-20 META51 반영·manual parity audit due

- `G202-induction-20260920-01`과 `META-G199-G200-G202-meta_induction-20260920-51` raw 2건을 원문 의미 변경 없이 반영했다. AGJ 원문 단서·강도와 carryover, corpus 미사용 0, G024 hold를 보존했다.
- queue 2,991건·processed 2,991건·pending 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 다음 단계는 META51 manual parity audit이다.
- manifest는 총 667건 중 `consumed_sdss` 663건·`prepared` 4건이며 G024 4건은 hold다. source 조회·backlog 준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 G202 전체 단계·META51 due

- G202 5문항 전체 단계 20건과 AGW source hold 해소 raw 1건을 원문 의미 변경 없이 반영했다. 2022 예시 문항과 실제 시행 기출, Orbi 전재본 원 crop과 공식 배포 호스트 검증, source qualification을 구별해 보존했다.
- queue 2,989건·processed 2,989건·pending 0건이다. G202 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 163 groups·663 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 다음 단계는 META51 induction이다.
- manifest는 총 667건 중 `consumed_sdss` 663건·`prepared` 4건이며, 남은 G024 4건은 hold다. 새 source·backlog 준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 G200 induction 반영

- `G200-induction-20260920-01` raw 1건을 원문 의미 변경 없이 반영했다. source 조회는 수행하지 않았다.
- queue 2,968건·processed 2,968건·pending 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 마지막 준비 목록인 G202 5문항이며, 이후 META51 audit/backfill 절차를 따른다.

## 최신 Luna 정기 sync — 2026-09-20 G200 전체 단계 반영

- G200 6문항 전체 단계 24건을 원문 의미 변경 없이 반영했다. AGN 63/56, AGM 45/17 후보와 AGP 62 충분성 부정 및 원문 범위 한계를 보존했다.
- queue 2,967건·processed 2,967건·pending 0건이다. G200 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 162 groups·658 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 준비된 G202 5문항이며 source 조회·backlog 준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 G199 induction 반영

- `G199-induction-20260920-01` raw 1건을 원문 의미 변경 없이 반영했다. source 조회와 의미 판단은 수행하지 않았다.
- queue 2,943건·processed 2,943건·pending 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. G200 시작 전 재확인한다.

## 최신 Luna 정기 sync — 2026-09-20 G199 전체 단계 반영

- G199 4문항 전체 단계 16건을 원문 의미 변경 없이 반영했다. AGJ의 63 상위 비판 평가, 65 왜곡 기각, 62 충분성 부정, 4 모든 공포 범위 역할을 보존했다.
- queue 2,942건·processed 2,942건·pending 0건이다. G199 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 161 groups·652 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 준비된 G200 6문항이며, source 조회·backlog 준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 G198 induction·META50 반영

- `G198-induction-20260920-01`과 `META-G196-G197-G198-meta_induction-20260920-50` raw 2건을 원문 의미 변경 없이 반영했다. META51 manual parity audit 대상 필드와 carryover를 보존했다.
- queue 2,926건·processed 2,926건·pending 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 다음 frontier는 G199다.
- source 조회·backlog 준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 G198 전체 단계·META50 due

- G198 5문항 전체 단계 20건과 AGD source hold 후속 해소 raw 1건을 원문 의미 변경 없이 반영했다. AGF `primary=[]` 및 후보 20/10/12와 규범적 정당화 전제, AGG 96/39 후보를 보존했다.
- queue 2,924건·processed 2,924건·pending 0건이다. G198 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 160 groups·648 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 다음 단계는 META50 induction이며 G199는 대기한다.
- manifest는 총 667건 중 `consumed_sdss` 648건·`prepared` 19건이다. source 조회·backlog 준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 G197 induction 반영

- `G197-induction-20260920-01` raw 1건을 원문 의미 변경 없이 반영했다. 신규 source 조회와 의미 판단은 수행하지 않았다.
- queue 2,903건·processed 2,903건·pending 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. G198 시작 전 재확인한다.

## 최신 Luna 정기 sync — 2026-09-20 G197 전체 단계 반영

- G197 AFX·AFY·AFZ·AGA·AGB 5문항의 전체 단계 20건과 AFY/AFZ source hold 후속 raw 1건을 원문 의미 변경 없이 반영했다. AFY 17/45, AGB 96/39 후보와 근접어 불확실성, AFZ 43/86의 다변수 고정 조건 순위 연결을 보존했다.
- queue 2,902건·processed 2,902건·pending 0건이다. G197 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 159 groups·643 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. G198 시작 전 meta 상태를 재확인한다.
- manifest는 총 667건 중 `consumed_sdss` 643건·`prepared` 24건이며, 새 source·backlog 준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 G196 induction 반영

- `G196-induction-20260920-01` raw 1건을 원문 의미 변경 없이 반영했다. 신규 source·answer·SDSS는 읽지 않았다.
- queue 2,881건·processed 2,881건·pending 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. G197 진행 중 추가 raw는 차집합만 반영한다.

## 최신 Luna 정기 sync — 2026-09-20 G196 전체 단계 반영

- G196 AFR~AFW 6문항의 blind·answer_check·independent_code·sdss_compare 24건을 원문 의미 변경 없이 반영했다. AFU의 `primary=[]`와 후보 80/17 및 대안 경로, AFR 64/17·AFW 96/39 유보를 보존했다.
- queue 2,880건·processed 2,880건·pending 0건이다. G196 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 158 groups·638 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 656건 중 `consumed_sdss` 638건·`prepared` 18건이다. G197/G198 준비 상태는 보존했으며 새 source·backlog 준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 G195 induction·META49 반영

- `G195-induction-20260920-01`과 `META-G194-G201-G195-meta_induction-20260920-49` raw 2건을 원문 의미 변경 없이 반영했다. 완료된 blind는 재수행하지 않았다.
- queue 2,856건·processed 2,856건·pending 0건이다.
- `meta_state.py`: 완료 157 groups·632 cases, `meta_induction_count=49`, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 G196 AFR 6문항이며, 이후 G197이다. manifest는 647건 중 consumed 632건·prepared 15건이다.

## 최신 Luna 정기 sync — 2026-09-20 G195 전체 단계·META49 due

- G195 AFL~AFQ 6문항의 blind·answer_check·independent_code·sdss_compare와 source hold 후속 crop 해소 raw 등 26건을 원문 의미 변경 없이 반영했다. AFM의 15/16 후보, AFP의 44/15 후보 및 원 source 기계 READY의 그림 누락 한계를 보존했다.
- queue 2,854건·processed 2,854건·pending 0건이다. G195 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 157 groups·632 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 다음 단계는 META49 `meta_induction`이며, 완료 전 새 G196 semantic stage를 시작하지 않는다.
- manifest는 총 647건 중 `consumed_sdss` 632건·`prepared` 15건이다. G196/G197 prepared 상태와 다른 Luna의 준비 작업은 보존했으며, 새 source 열람·backlog 재실행은 하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 G201 induction 및 frontier hold 확정

- `G201-induction-20260920-01` raw 1건을 원문 의미 변경 없이 반영했다. queue 2,828건·processed 2,828건·pending 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 연구 가능한 actionable READY는 없다. prepared 4건(DR·DS·DT·DU, G024)은 SDSS 사전노출 barrier hold이므로 actionable 잔량으로 세지 않고 재독립연구를 금지한다. G195~G200 자료 연결·복원은 다른 helper가 진행 중이다.

## 최신 Luna 정기 sync — 2026-09-20 G194·G201 후속 및 induction 반영

- G201 AGR·AGS·AGT·AGU의 independent_code 4건과 sdss_compare 4건, G194 후속 `induction` 1건을 원문 의미 변경 없이 반영했다. AGR·AGU의 `primary=[]`와 후보 구조를 보존했으며 G201 induction은 아직 추가되지 않았다.
- queue 2,827건·processed 2,827건·pending 0건이다.
- `meta_state.py`: 완료 156 groups·626 cases, `completed_groups_since_last_meta=2`, `completed_questions_since_last_meta=10`, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 630건 중 `consumed_sdss` 626건·`prepared` 4건이다. 새 source·answer·SDSS 열람과 backlog 준비는 수행하지 않았다. G201 induction이 추가되면 별도 sync한다.

## 최신 Luna 정기 sync — 2026-09-20 G194 전체 단계 및 현재 hold 반영

- G194 AFF·AFG·AFH·AFI·AFJ·AFK의 blind·answer_check·independent_code·sdss_compare 24건과 G201 blind/hold raw를 원문 의미 변경 없이 반영했다. AFF/AFG의 `primary=[]` 및 후보 구조를 보존했고, G201은 independent_code 미시작·SDSS 봉인 상태를 유지했다.
- queue 2,818건·processed 2,818건·pending 0건이다. G194 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 155 groups·622 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 630건 중 `consumed_sdss` 622건·`prepared` 8건이다. 새 자료 연결·backlog 준비는 수행하지 않았다. G194 induction 및 G201 후속은 group barrier에 따라 대기한다.

## 최신 Luna 정기 sync — 2026-09-20 META48 지정 depth_backfill 반영

- `AUDIT48-sixcases-depth_backfill-20260920-01` grouped raw 1건을 원문 의미 변경 없이 절차 기록과 ACP·AFB·AFD·AAF·AAK·AEZ 각 case 문서에 연결했다. 최초 raw는 보존했고, revised_primary 빈 배열·후보/대표 구조와 AEZ 조건부 수치 전제를 primary 확정으로 요약하지 않았다.
- 동기화 중 helper가 추가한 G194 AFF·AFG blind raw도 기계 반영했다. queue 2,784건·processed 2,784건·pending 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 630건 중 `consumed_sdss` 616건·`prepared` 14건이다. 새 source·answer·SDSS 열람과 backlog 의미 준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 META48 manual parity audit 반영

- `AUDIT-meta48-manual_parity_audit-20260920-16` raw 1건을 payload 원문 의미 변경 없이 독립연구 진행 기록과 processed 원장에 반영했다. 다중 `case_ids` depth_backfill 지정은 상태 필드로만 기계 반영했으며 의미 보완은 수행하지 않았다.
- queue 2,781건·processed 2,781건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=["AAF", "AAK", "ACP", "AEZ", "AFB", "AFD"]`, `semantic_state_review=[]`이다.
- Astra가 지정된 6개 case의 depth_backfill을 수행 중이며, 완료 전 새 group semantic stage는 시작하지 않는다. 신규 G201 manifest 준비는 다른 helper 영역으로 보존했다.

## 최신 Luna 정기 sync — 2026-09-20 META48 반영·manual parity audit due

- `META-G181-G193-G168-meta_induction-20260920-48` raw 1건을 payload 원문 의미 변경 없이 독립연구 진행 기록과 processed 원장에 반영했다. 새 source·answer·SDSS 열람과 backlog 준비는 수행하지 않았다.
- queue 2,780건·processed 2,780건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 154 groups·616 cases, `meta_induction_count=48`, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 허용 semantic 단계는 Astra의 META48 manual parity audit이며, 완료 전 새 group을 시작하지 않는다.

## 최신 Luna 정기 sync — 2026-09-20 G168 후속 단계·META48 due 반영

- G168 AAF·AAG·AAH·AAI·AAJ·AAK의 공식 crop 후속 blind 1건, 전체 answer_check 6건, independent_code 6건, sdss_compare 6건 등 신규 raw 19건을 원문 의미 변경 없이 기존 연구 문서와 processed 원장에 반영했다. 최초 사전답 노출·strict-blind 제외·최초 hold·공식 답 직접 대조 미검증을 보존했으며, 최초 답 일치도 strict 성과로 승격하지 않았다.
- queue 2,779건·processed 2,779건이며 `record_id` 기준 pending raw는 0건이다. G168 후속 `induction`까지 반영했으며 추가 차집합은 없다.
- `meta_state.py`: 완료 154 groups·616 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=16`, `meta_due=true`, `meta_induction_count=47`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 새 group 시작 전 META48 `meta_induction`이 due다.
- manifest는 총 626건 중 `consumed_sdss` 616건·`prepared` 10건이다. 남은 prepared는 G024 DR~DU hold와 G194 AFF~AFK이며, G194/G201 준비·복원은 다른 helper가 관리한다. 새 source·answer·SDSS 열람과 backlog 재준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 G193 전체 단계·induction 반영

- G193 AFB·AFC·AFD·AFE의 independent_code 4건, sdss_compare 4건 및 `G193-induction-20260920-01` 1건을 원문 의미 변경 없이 기존 연구 문서·독립연구 진행 기록·processed 원장에 반영했다. primary/auxiliary object 배열과 strict-blind 제외, 공식 배포 답표 직접 대조 미검증, 사이트 연결 부재 사전 노출 및 기존 유보를 보존했다.
- queue 2,759건·processed 2,759건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 153 groups·610 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 620건 중 `consumed_sdss` 610건·`prepared` 10건이다. 남은 prepared는 기존 G024 DR~DU 및 G168 AAF~AAK hold이며, 새 source·answer·SDSS 열람과 backlog 준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 META46 반영

- `META-G160-G166-G167-meta_induction-20260920-46` raw 1건을 payload 원문 그대로 반영했다. G168 AAG 대괄호 범위 crop 복원 대기와 helper 표 셀만으로 종료 범위를 확정할 수 없다는 유보를 유지했다.
- queue 2,661건·processed 2,661건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 148 groups·588 cases, `meta_induction_count=46`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 strict READY는 manifest 순서상 **G179**이며, G168 비strict 후속은 범위 복원 후 진행한다.

## 최신 Luna 정기 sync — 2026-09-20 G167 완료·G168 부분 hold

- G167 AAC·AAD·AAE의 blind·answer_check·independent_code·sdss_compare와 G168 AAF·AAG·AAH·AAI·AAJ·AAK의 부분 blind/hold 및 원문 재구성 raw 등 신규 19건을 원문 의미 변경 없이 반영했다. G168은 6건 전체 사전답 노출로 strict-blind 제외하며, AAG range 실제 crop 복원 hold를 유지한다.
- queue 2,660건·processed 2,660건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 148 groups·588 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=10`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- G168 group 완료 처리는 하지 않는다. 다음 semantic 단계는 Astra의 **META46 `meta_induction`**이다.

## 최신 Luna 기계 상태 교정 — 2026-09-20 G166 frontier

- metadata 기준 G165는 manifest에 없고, 다음 prepared frontier는 G166 ZY·ZZ·AAA·AAB이다. G166~G168의 새 READY는 총 13문항이며 blind source와 sealed answer/SDSS/provenance가 분리되어 있다.
- G160과 새 frontier의 출제 연도·문항 anchor는 기계적으로 서로 다름을 확인했지만, G160 동형이의어 문항의 실제 정본 연결은 별도 검증 중인 hold로 유지한다. 기존 source·queue는 변경하지 않았다.
- G166 ZY·ZZ·AAA·AAB blind raw 4건이 append되어 기계 반영했다. queue 2,619건·processed 2,619건이며 pending raw는 0건이다. manifest는 총 598건 중 `consumed_sdss` 578건·`prepared` 20건이다. 기존 preflight의 source provenance 경고와 기존 overlap은 수정·승격하지 않았다. 다음 연구 frontier는 **G166** 후속 단계다.

## 최신 Luna 정기 sync — 2026-09-20 G160 provenance collision hold 반영

- `G160-hold-20260920-provenance-collision-02` raw 1건을 원문 의미 변경 없이 반영했다. 실제 2025년 6월 문제지는 G162의 여러 글 읽기이며 G160 동형이의어 문항과 다르다는 provenance 사실과 최초 helper의 미승인 판단을 보존했다.
- queue 2,615건·processed 2,615건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 145 groups·578 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- G160 연결 검증·완료 승격은 보류한다. 실제 시험 식별은 다른 Luna가 진행 중이다.

## 최신 Luna 정기 sync — 2026-09-20 ZI depth_backfill 반영

- `ZI-depth_backfill-20260920-01` raw 1건을 원문 의미 변경 없이 반영했다. `revised_primary=[]`, 후보 17/25, `working_representative=25`, 최초 기록 보존을 유지했다.
- queue 2,614건·processed 2,614건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 145 groups·578 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- G160 공식 2025년 6월 답표 ⑤②②와 해당 문제지 첫 지문 연결은 아직 미확인인 hold를 유지한다. 다음 신규 frontier는 **G165**다.

## 최신 Luna 정기 sync — 2026-09-20 META45 manual parity audit 반영

- `AUDIT-meta45-manual_parity_audit-20260920-15` raw 1건을 원문 의미 변경 없이 반영했다. ZI depth_backfill 지정과 audit 결과를 그대로 보존했다.
- queue 2,613건·processed 2,613건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: `meta_induction_count=45`, `last_manual_parity_audited_meta_count=45`, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=["ZI"]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 ZI depth_backfill이며, source 열람과 의미 보완은 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 META45 반영

- `META-G162-G164-meta_induction-20260920-45` raw 1건을 payload 원문 그대로 반영했다. ZI/ZK 대칭성 점검을 포함한 다음 manual parity audit 지정은 의미 변경 없이 보존했다.
- queue 2,612건·processed 2,612건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 145 groups·578 cases, `meta_induction_count=45`, `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 **META45 manual parity audit**이며, 새 source 열람과 group 진행은 보류한다.

## 최신 Luna 정기 sync — 2026-09-20 G164 완료·META45 due

- G164 ZQ·ZR·ZS·ZT의 남은 blind·answer_check·independent_code·sdss_compare raw 13건을 원문 의미 변경 없이 반영했다. G164 전체 SDSS compare가 완료되었다.
- queue 2,611건·processed 2,611건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 145 groups·578 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=11`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 front는 새 group이 아니라 Astra의 **META45 `meta_induction`**이며, 이후 manual parity audit이다. G160 source 확인은 별도 Luna가 진행 중인 hold를 유지한다.

## 최신 Luna 정기 sync — 2026-09-20 G163 ZM~ZP 완료

- G163 ZM·ZN·ZO·ZP의 blind·answer_check·independent_code·sdss_compare raw 16건을 원문 의미 변경 없이 반영했다. ZP `primary=[]`, `primary_candidates=[96,39]` 유보를 보존했다.
- G164 ZQ·ZR·ZS blind raw 3건도 동시 append 차집합으로 기계 반영했다. queue 2,598건·processed 2,598건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 144 groups·574 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- G160 정본 헤더 검증 hold는 유지한다. 다음 frontier는 **G164** 후속이며 과거 archive 열람·backlog 확장은 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 G162 ZJ~ZL 완료

- G162 ZJ·ZK·ZL의 blind·answer_check·independent_code·sdss_compare raw 12건을 원문 의미 변경 없이 반영했다. ZK `primary=[]`, `primary_candidates=[17,25]` 유보를 보존했다.
- queue 2,579건·processed 2,579건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 143 groups·570 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- G160 정본 헤더 검증 hold는 유지한다. 다음 prepared frontier는 **G163 metadata**이며 source/backlog 준비는 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-20 META44 반영

- `META-G159-G155-G161-meta_induction-20260920-44` raw 1건을 payload 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. 이번 window의 작업 기준 보강·미해결 경계·G160 정본 연결 유보를 의미 변경 없이 보존했다.
- queue 2,567건·processed 2,567건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 142 groups·567 cases, `meta_induction_count=44`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- G160 official mapping은 실제 문제지·정답표 헤더가 아직 확인되지 않아 재검증 중이며 hold를 유지한다. G160의 sealed 답 불일치 3건은 최초 선택과 sealed 값을 모두 보존하고, G160 완료 처리와 후속 semantic stage를 보류한다.

## 최신 Luna 정기 sync — 2026-09-20 G160·G161 raw 후처리

- G160 ZD·ZE·ZF blind 3건과 answer_check 3건, G161 ZG·ZH·ZI의 blind·answer_check·independent_code·sdss_compare 12건 등 신규 raw 18건을 기존 사례 문서와 processed 원장에 원문 의미 변경 없이 반영했다. G160 answer_check의 sealed 답 불일치 3건은 `needs_astra_review`로 보존했으며, G160 완료로 집계하지 않았다.
- queue 2,566건·processed 2,566건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 142 groups·567 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=10`, `meta_induction_count=43`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- G159·G155·G161 완료 3개 group으로 다음 작업은 **META44 `meta_induction` due**이다. G160 정본 연결·답 검증은 다른 Luna가 수행 중이며, 그 결과 전에는 G160 완료 처리와 후속 semantic stage를 시작하지 않는다. manifest는 총 598건 중 `consumed_sdss` 567건·`prepared` 31건이다.

## 최신 Luna 정기 sync — 2026-09-19 G126 TE~TH 완료

- G126 TE·TF·TG·TH의 blind·answer_check·independent_code·sdss_compare raw 16건과 TH 도식 hold 1건을 원문 그대로 기존 사례 문서·processed 원장에 반영했다. TH 원그림 직접 확인으로 hold 해소된 blind를 보존하고, TE #22/#17, TF #46/#56, TG #17/#45 국소 중첩 및 TH 측정값 변환과 실제 거리 구별을 raw 그대로 유지했다.
- queue 2,077건·processed 2,077건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 116 groups·454 cases, `meta_induction_count=35`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 521건 중 `consumed_sdss` 454건·`prepared` 67건이다. G121 SH 공식 문제지 source hold는 유지한다. 다음 READY metadata frontier는 **G127 TI**이며, SH source hold 해소 전 G121 후속 stage를 재개하지 않는다.

## 최신 Luna 정기 sync — 2026-09-19 META35 반영

- `META-G120-G124-meta_induction-20260919-35` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. 3 groups·15 cases window, 기존 QI/RV anchor 대조, G121 미완료 제외, 최초 code 변경 없음, SW 반사실 범위(인도 명칭만 교체 불가·구성요건 필요)를 모두 raw 의미 그대로 보존했다.
- queue 2,060건·processed 2,060건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 115 groups·450 cases, `meta_induction_count=35`, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`이다.
- 다음 META36에서 manual parity audit due가 예정된다. 새 source·answer·SDSS 열람이나 새 의미 판단은 수행하지 않았다.

## 최신 Luna 정기 sync — 2026-09-19 G124 ST~SX 완료·META35 due

- G124 ST·SU·SV·SW·SX의 blind·answer_check·independent_code·sdss_compare raw 20건을 원문 그대로 기존 사례 문서·processed 원장에 반영했다. ST/SU #10/#12 중첩, SW #12/#45 국소 중첩과 취득 결론·권리 경로 구분을 보존했다.
- queue 2,059건·processed 2,059건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 115 groups·450 cases, META34 이후 3 groups·15 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 521건 중 `consumed_sdss` 450건·`prepared` 71건이다. G121 SH 공식 문제지 source hold는 유지한다. 다음 단계는 **Astra META35 의미 작업**이며 완료 전 새 passage group semantic stage를 시작하지 않는다.

## 최신 Luna 정기 sync — 2026-09-19 G121·G122 raw 후처리

- G121 SD·SE·SF·SG·SI blind 5건과 SD/SH hold 3건, G122 SJ~SO blind·answer_check·independent_code·sdss_compare 24건 등 신규 raw 32건을 원문 그대로 기존 사례 문서·processed 원장에 반영했다. SD 보강표 확인 후 유효 blind 저장 상태를 보존했고, SH 공식 문제지 필요 hold를 유지했다.
- G122 SJ의 primary 빈 배열 및 candidates #60/#64 유보, SO 다음 연도 표제 노출 qualification을 확정 판단으로 승격하지 않았다. G121은 SH blind 미완료로 answer_check·independent_code·SDSS를 시작하지 않았다.
- queue 2,039건·processed 2,039건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 114 groups·445 cases, `meta_induction_count=34`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 521건 중 `consumed_sdss` 445건·`prepared` 76건이다. G024 DR~DU historical prior-exposure hold는 계속 제외하며, 다음 frontier는 **G121 SH 공식 문제지 source hold 해소 후 blind**다.

## 최신 Luna 정기 sync — 2026-09-19 G120 RZ~SC 완료

- G120 RZ·SA·SB·SC의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 기존 사례 문서·processed 원장에 반영했다. RZ #22/#17 국소 중첩, SB #17/#46 국소 중첩, SC 통제 비교와 동방향 복수변화 차이, 공식 답 검증 범위 qualification을 그대로 보존했다.
- queue 2,007건·processed 2,007건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 113 groups·439 cases, `meta_induction_count=34`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 521건 중 `consumed_sdss` 439건·`prepared` 82건이다. G024 DR~DU historical prior-exposure hold는 계속 제외하며, 다음 actionable READY frontier는 **G121 SD**다.

## 최신 source restoration — 2026-09-17

- G071·G072·G073·G074·G075·G081·G084·G086·G090·G095·G096·G098의 46개 case source를 HWPX XML/embedded asset 기준으로 복원하고 manifest·provenance mapping·blind packet을 갱신했다.
- 12개 group은 mechanical `READY`다. LO는 `image6`, MX는 `image3` embedded asset을 연결했다.
- semantic stage, answer check, independent code, SDSS compare는 시작하지 않았다. G101 이후 frontier도 준비하지 않았다.

## 최신 정상 sync — 2026-09-16 최종 G061~G070 후처리

- 마지막 `META-G069-G070-induction-20260916-01` raw 1건을 원문 그대로 반영했다. queue 1,240건·processed 1,240건이며 pending raw는 0건이다. 세션 신규 raw는 129건, G061~G070은 10 groups·29 cases, 누적은 69 groups·261 cases다.
- META17·18·19, META18 manual audit, JI·JQ·JY·JE·JK depth_backfill 5건을 기계적으로 확인했다. 정기 meta baseline 19와 기존 유보는 변경하지 않았다.
- `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`. manifest는 consumed_sdss 261건·G024 hold 4건·actionable prepared 0건이며 다음 frontier는 미준비 G071 KF blind다.

## 최신 정상 sync — 2026-09-16 G070 완료

- KC·KD·KE의 blind·answer_check·independent_code·sdss_compare raw 12건을 원문 그대로 반영했다. queue 1,239건·processed 1,239건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 69 groups·261 cases, META19 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- KE 말미 경계 잔재는 group 식별정보로 확정하지 않고 3 cases 노출 qualification을 보존했다. manifest는 `consumed_sdss` 261건과 G024 hold 4건이다.
- 다음 frontier는 준비되지 않은 G071 KF blind다. G024 hold는 유지한다.

## 최신 정상 sync — 2026-09-16 G069 완료

- KB blind·answer_check·independent_code·sdss_compare raw 10건을 원문 그대로 반영했다. queue 1,227건·processed 1,227건이며 pending raw는 0건이다.
- 선택 그래프 hold 해소 범위, 선형 감쇄 모형, 원배포 PDF 유보를 보존했다. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 frontier는 G070 KC·KD·KE blind다. prepared는 G024 hold 4건과 G070 KC~KE 3건이다.

## 최신 정상 sync — 2026-09-16 G069 source checkpoint

- JZ·KA blind, KB source hold, JY depth_backfill raw 4건을 원문 그대로 반영했다. queue 1,217건·processed 1,217건이며 pending raw는 0건이다.
- KB 선택 그래프 5개 누락 hold와 답·태그 미열람을 유지했다. JY `cellAddr` 보강은 의미 불변으로 반영했다. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 유효 단계는 KB source 복원 후 KB blind이며 G069 완료 집계는 증가시키지 않았다.

## 최신 정상 sync — 2026-09-16 META19 반영

- `META-G066-G068-meta_induction-20260916-19` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,213건·processed 1,213건이며 pending raw는 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `meta_induction_count=19`.
- JU·JY·JE 관련 기존 유보를 보존했으며 다음 frontier는 G069 JZ·KA·KB blind다.

## 최신 정상 sync — 2026-09-16 G068 완료·META19 due

- JW·JX·JY의 blind·answer_check·independent_code·sdss_compare raw 12건을 원문 그대로 반영했다. queue 1,212건·processed 1,212건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 67 groups·255 cases, META18 이후 3 groups·8 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- JY 그림의 공통 장치도·출력 수치표 원화 아님 한계를 유지했다. 다음 허용 단계는 META19 `meta_induction`이다.

## 최신 기계 상태 점검 — 2026-09-16 준비 잔량

- 최신 manifest 265건은 `consumed_sdss` 252건·`prepared` 13건이다. G024 DR~DU 4건은 historical hold이고 G068~G070 JW~KE 9건이 actionable prepared다.
- G065~G067의 JP~JV 7건은 모두 `consumed_sdss`이며 중복·누락은 확인되지 않았다.

## 최신 정상 sync — 2026-09-16 G067 완료

- JU source 보강 blind 1건과 JT·JU·JV의 answer_check·independent_code·sdss_compare raw 9건을 원문 그대로 반영했다. queue 1,200건·processed 1,200건이며 pending raw는 0건이다.
- JU 거리 출력 미명시·조건역 자동 추론 금지, JV 기하 대칭 정성 예측 범위, 로컬 도식 해소와 원배포 PDF 유보를 보존했다. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 frontier는 G068 JW·JX·JY blind이며 JY 그림 복원 경로가 준비되어 있다.

## 최신 정상 sync — 2026-09-16 G067 blind source checkpoint

- JT·JU·JV blind raw 3건을 원문 그대로 반영했다. queue 1,190건·processed 1,190건이며 pending raw는 0건이다.
- JU 도식 추가 복원 대기, 최초 선택 ③·근거 범위·그림 누락 유보를 유지했다. 답·태그 미열람 및 완료 집계 미증가 상태다.
- 다음 단계는 JU 도식 Astra 확인 후 G067 전체 answer_check이며 필요 시 blind 보강이다.

## 최신 정상 sync — 2026-09-16 G066 완료

- JS blind·answer_check·independent_code·sdss_compare raw 7건을 원문 그대로 반영했다. queue 1,187건·processed 1,187건이며 pending raw는 0건이다.
- JS source hold는 blind payload의 직접 도식 판독 범위에서 해소했고 원배포 PDF 직접 검증 유보는 유지했다. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 frontier는 G067 JT·JU·JV blind다. JV 그림 복원 경로가 준비되어 있다.

## 최신 정상 sync — 2026-09-16 G066 source-hold checkpoint

- `JR-blind-20260916-01`과 `JS-hold-20260916-source-01` raw 2건을 원문 그대로 반영했다. queue 1,180건·processed 1,180건이며 pending raw는 0건이다.
- JS 그림 복원 대기와 `needs_astra_review`를 유지했다. 답·코드·SDSS를 공개하지 않았고 G066 완료 집계도 증가시키지 않았다. 다음 유효 단계는 JS source 복원 후 blind다.

## 최신 정상 sync — 2026-09-16 JK depth_backfill 반영

- `JK-depth_backfill-20260916-audit18-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,178건·processed 1,178건이며 pending raw는 0건이다.
- XML 셀 대응 보강과 원배포 PDF 직접 검증 유보를 분리 보존했다. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 frontier는 G066 JR·JS blind다.

## 최신 정상 sync — 2026-09-16 JE depth_backfill 반영

- `JE-depth_backfill-20260916-audit18-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,177건·processed 1,177건이며 pending raw는 0건이다.
- 최초 주 코드 75와 치중→한정 일반화 불인정, 배타적 해석의 잔여 간극 유보를 보존했다. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["JK"]`.
- 다음 허용 단계는 JK depth_backfill이다. 완료 전 G066은 시작하지 않는다.

## 최신 정상 sync — 2026-09-16 META18 manual parity audit 반영

- `AUDIT-meta18-manual_parity_audit-20260916-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,176건·processed 1,176건이며 pending raw는 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["JE", "JK"]`, `last_manual_parity_audited_meta_count=18`.
- 다음 허용 단계는 JE·JK depth_backfill이다. 완료 전 G066은 시작하지 않는다.

## 최신 정상 sync — 2026-09-16 META18 반영·manual audit due

- `META-G063-G065-meta_induction-20260916-18` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,175건·processed 1,175건이며 pending raw는 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`, `meta_induction_count=18`.
- 다음 허용 단계는 manual parity audit이다. JK supplement는 Astra 의미 raw 부재로 미반영했다.

## 최신 정상 sync — 2026-09-16 JQ depth_backfill 반영

- `JQ-depth_backfill-20260916-source-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,174건·processed 1,174건이며 pending raw는 0건이다.
- 복원 도식 PNG 직접 판독 결과는 보존했고 원배포 PDF 미검증 유보도 유지했다. `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`. JK 표 보강은 미반영이다.
- 다음 허용 단계는 META18 `meta_induction`이다.

## 최신 정상 sync — 2026-09-16 G065 완료·META18 due

- JP·JQ의 blind·answer_check·independent_code·sdss_compare raw 8건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,173건·processed 1,173건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 64 groups·247 cases, META17 이후 3 groups·8 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 허용 단계는 META18 `meta_induction`이며 이후 manual parity audit due를 확인한다. JQ 도식·source 유보는 변경하지 않았다.

## 최신 정상 sync — 2026-09-16 G064 완료

- JN·JO의 blind·answer_check·independent_code·sdss_compare raw 8건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,165건·processed 1,165건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 63 groups·245 cases, META17 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 frontier는 G065 JP·JQ blind다. actionable prepared는 G065~G070 JP~KE 20건이며 G024 DR~DU 4건은 historical hold다.

## 최신 정상 sync — 2026-09-16 JI depth_backfill 반영

- `JI-depth_backfill-20260916-source-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,157건·processed 1,157건이며 pending raw는 0건이다.
- 로컬 HWPX 헤더·셀 순서 확인은 로컬 범위의 전사 유보만 보강했고, 원배포 PDF 유보와 최초 판단은 유지했다. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 frontier는 G064 JN·JO blind다.

## 최신 정상 sync — 2026-09-16 G063 완료

- JJ·JK·JL·JM의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,156건·processed 1,156건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 62 groups·243 cases, META17 이후 1 group·4 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 frontier는 G064 JN·JO blind다. actionable prepared는 G064~G070 JN~KE 22건이며 G024 DR~DU 4건은 historical hold다.

## 최신 정상 sync — 2026-09-16 META17 반영

- `META-G060-G062-meta_induction-20260916-17` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,140건·processed 1,140건이며 pending raw는 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `meta_induction_count=17`.
- 다음 frontier는 G063 JJ·JK·JL·JM blind다. G024 historical hold 4건과 G063~G070 JN~KE 26건은 prepared 상태로 유지한다.

## 최신 정상 sync — 2026-09-16 G062 완료·META17 due

- JG·JH·JI의 blind·answer_check·independent_code·sdss_compare raw 12건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,139건·processed 1,139건이며 pending raw는 0건이다. queue 원문은 변경하지 않았다.
- `meta_state.py`: 완료 61 groups·239 cases, META16 이후 3 groups·8 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 허용 단계는 META17 `meta_induction` raw다. manifest prepared 잔량은 G024 hold 4건과 G063~G070 JN~KE 26건이다.


## 최신 정상 sync — 2026-09-16 G061 완료

- JC·JD·JE·JF의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,127건·processed 1,127건이며 `record_id` 기준 pending raw는 0건이다. queue 원문은 변경하지 않았다.
- JD의 범위 보강은 independent payload대로 로컬 HWPX 검증으로 반영했으며 최초 blind 한계와 공식 배포 PDF 직접 시각 대조 아님이라는 유보를 보존했다. G061 SDSS 연결 부재에 따른 판단 보류도 유지한다.
- `meta_state.py`: 완료 60 groups·236 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`. 다음 frontier는 G062 JG·JH·JI blind, G063 JJ~JM은 대기다.


## 최신 정상 sync — 2026-09-15 G060 완료

- 이번 세션 시작 시점 실제 완료 집계 50 passage groups·206 cases에서 G052~G060 후속 raw, META14·META15·META16, META15 manual parity audit, IO·IK depth_backfill을 반영해 59 groups·232 cases가 되었다. G060 JB의 answer_check·independent_code·sdss_compare 3건까지 원 payload 그대로 후처리했다.
- queue 1,111건·processed 1,111건이며 `record_id`/`source_record_id` 차집합은 0건이다. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest prepared 4건은 모두 G024 DR~DU historical preexposure hold로 actionable 잔량은 0건이다. 다음 Excel-style case `JC`는 아직 준비되지 않았으며, 추가 후보 준비와 별도 비독립 검토는 후속 작업으로 남긴다.

## 최신 후처리 완료 — 2026-09-15 사용자 중지

queue 858건과 processed 858건을 `record_id`/`source_record_id` 기준으로 대조해 pending 0건을 확인했다. 직전 sync 이후 32건은 raw payload를 변경하지 않고 기존 사례 문서·절차 기록·CURRENT 및 processed에 반영했다. 마지막 hold는 `SESSION-hold-20260915-user-stop-01`이며 `needs_astra_review`로 보존했다. GZ의 blind ①과 sealed 공식답 ⑤ 불일치는 정본·시험형 대응 확인 전까지 수정하거나 정답 일치로 집계하지 않는다. 사용자 중지에 따라 신규 source/semantic stage/backlog 준비는 수행하지 않았다.

재개 frontier: G043 GZ 공식 답 번호·정본·시험형 대응 확인 → G043 전체 independent_code → barrier 후 SDSS; 다음 G044 independent_code. G045/G046은 미열람.

1. `data/기본기_연구/astra_handoff_queue.jsonl`에서 `record_id` 기준으로 processed 원장에 없는 record를 확인한다.
2. raw 판단을 변경하지 않고 기존 연구 MD/JSONL 구조에 단계별로 반영한다.
3. 누락·충돌·schema 오류를 확인한다. 의미적 판단이 필요한 충돌은 추측하지 말고 `needs_astra_review`로 남긴다.
4. 반영한 record를 `data/기본기_연구/astra_handoff_processed.jsonl`에 `source_record_id`, `processed: true`, 반영 대상 경로와 함께 기록한다. queue 원본은 덮어쓰지 않는다.
5. CURRENT.md를 최신 frontier checkpoint로 갱신한다. 상세 풀이와 raw queue 내용을 반복하지 않는다.
6. 기존 Astra 판단과 연구계획에 근거해 다음 Astra frontier를 정한다. 새로운 연구 결론은 만들지 않는다.
7. 필요할 때만 hash/audit 및 중복·누락 검사를 수행하고, 다음 Astra가 AGENTS+CURRENT만으로 시작 가능한지 확인한다.
8. `data/기본기_연구/prepared_backlog/manifest.jsonl`의 잔량을 확인한다. 최소 30개 아래면 기존 색인·정본 연결 자료만 사용해 후보를 기계적으로 추가하고, 중복·기존 노출·자료 연결을 검사한 뒤 blind packet과 sealed answer/SDSS record를 분리 생성한다. Luna는 이 단계에서 새로운 의미적 코드 판정을 만들지 않는다.

## hard-limit recovery

정상 handoff 없이 Astra가 hard usage limit으로 종료되었을 때도 먼저 queue와 processed ledger를 비교한다. 미처리 raw가 있으면 그 raw만 후처리하고, 미완료 semantic stage·SDSS compare를 추론하거나 보완하지 않는다. 처리된 raw만 processed ledger에 추가하며, 남은 단계와 hold 사유는 CURRENT에 정확히 기록한다. queue와 processed가 이미 정합하면 다음 Astra frontier로 복귀한다.
<!-- luna-sync:SESSION20261004-G501-induction-sync-20261004 -->
## 최신 Luna sync — G501 induction 반영·G502 frontier

- `G501-induction-20261004-01` raw 1건을 반영했다. Queue=processed=7,118 unique, pending=0, duplicate/orphan=0.
- 응시·합격·임용·품계 단계와 명분·결과 구분, 찬성과 우려의 양립을 원raw대로 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 461 groups·1,560 cases, META150 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 Excel-style frontier는 G502의 `BPR, BPS, BPT` 전체 blind다.
- 운영 메모: `scripts/codex_quota` 수정본의 300분 primary·10080분 weekly 구분과 null/partial 정규화·`--diagnostics`를 10 fixture로 검증했다. 승인된 외부 조회 결과는 primary=null, weekly used=90%, remaining=10%였고, sandbox 내부 SQLite 직접 조회는 권한 오류로 수행하지 않았다. runtime `<5%` 경고는 없으며 이는 종료·hold 사유가 아니다. 주간 잔여 10%이므로 원자 stage마다 조회하고 7% 이하이면 정상 handoff한다. 신규 semantic raw 없음, pending=0, G502 미열람 상태를 유지한다.
- quota 조회 결과는 `quota_status: unavailable`로 보존한다. runtime emergency 경고는 관측되지 않았으며, unavailable은 종료·hold 근거가 아니다.
- blind packet의 blind-only 표식과 공식답·SDSS·기존 판정 top-level 키 부재를 기계 확인했고, sealed 자료는 `data/기본기_연구/prepared_backlog/sealed/`에 분리되어 있음을 확인했다.
<!-- luna-sync:SESSION-hold-normal-quota-20261004-01-sync-20261004 -->
## 최신 Luna sync — 정상 quota handoff·G502 SDSS 대기

- G502 `BPR, BPS, BPT`의 blind·answer_check·independent_code 9 raw와 `SESSION-hold-normal-quota-20261004-01` hold 1건을 기존 처리기로 반영했다. Queue=processed=7,128 unique, pending=0, duplicate/orphan=0.
- 세 최초 답 ②·③·③은 공식 답과 일치한다. `past_exposure=unknown`, `strict_blind_eligible=false`를 raw대로 유지하며 엄격 blind 성과로 계산하지 않는다. G502 SDSS compare와 induction은 아직 미완료다.
- `meta_state.py`: 461 groups·1,560 cases, META150 이후 1 group·3 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 이번 run의 신규 완료 범위는 G481~G501이며 최초 오답 BNQ와 기존 strict-blind unknown·품질 제한을 보존한다. 다음 Astra는 G502 전체 SDSS 공개·대조부터 재개하고 G503은 미열람 상태다.
- 정상 handoff는 주간 used 93%/remaining 7% 최초 관측으로 발생했다. primary 5h는 null, runtime emergency는 없으며 연구 완료나 prepared backlog 소진이 아니다.
<!-- luna-sync:SESSION20261005-BQC-depth-sync-20261005 -->
## 최신 Luna sync — BQC backfill 반영·G510 독립 코드 barrier 진행 중

- `BQC-depth_backfill-AUDIT153-20261005-01` raw를 기존 상세 기록에 의미 변경 없이 반영했다. `BQI-depth_backfill-AUDIT153-20261004-01`는 이미 processed이므로 재반영·재연구하지 않았다. G510의 blind 3건과 answer_check 3건, 현재까지 저장된 independent_code raw 1건도 기계적으로 반영했다.
- Queue=processed=7,247 unique, pending=0, duplicate/orphan=0. `meta_state.py` 재실행 결과 469 groups·1,585 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 실제 미완료 frontier는 G510 전체 `BQQ, BQR, BQS`의 independent_code stage barrier 완료다. Manifest 준비 상태 및 blind-source 존재: BQQ — `data/기본기_연구/prepared_backlog/blind_sources/BQQ.json` (prepared, 존재); BQR — `data/기본기_연구/prepared_backlog/blind_sources/BQR.json` (prepared, 존재); BQS — `data/기본기_연구/prepared_backlog/blind_sources/BQS.json` (prepared, 존재). SDSS 공개 전 group barrier를 완료한다. 이번은 정상 연구 중 sync이며 종료/hold가 아니다.
