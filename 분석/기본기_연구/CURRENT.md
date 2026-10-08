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

<!-- luna-sync:SESSION20261004-BPW-depth-sync-20261004 -->
## 최신 Luna sync — BPW depth backfill 반영·BQI/BQC 대기

- BPW depth backfill raw 1건을 기계적으로 반영했다. 수치 반례의 가상 모형, 최초·공식 답 ④, 문맥 해석 확신도 0.88 제한을 원raw대로 보존했으며 Luna는 의미를 재판정하지 않았다.
- queue/processed unique=7,237, pending=0, duplicate/orphan=0. `meta_state.py`: 469 groups·1,585 cases; `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[BQC, BQI]`, `semantic_state_review=[]`.
- 신규 group은 열지 않으며 BQI·BQC depth backfill은 Astra가 이어서 작성한다. 사용자 기준의 7% 정상 중단 해제를 유지한다.

<!-- luna-sync:SESSION-hold-normal-quota-20261004-01-sync-20261004 -->
## 최신 Luna sync — 정상 quota handoff·G502 SDSS 대기

- G502 BPR·BPS·BPT blind·answer_check·independent_code 9 raw와 정상 quota hold 1건 반영. Queue=processed=7,128 unique, pending=0, duplicate/orphan=0.
- 최초 답 ②·③·③은 공식 답과 일치하나 `past_exposure=unknown`, `strict_blind_eligible=false`를 보존한다. SDSS compare·induction은 미완료, G503은 미열람이다.
- `meta_state.py`: 461 groups·1,560 cases; META150 이후 1/3, due/depth/semantic review 모두 없음. 이번 run 완료 범위 G481~G501 및 최초 오답 BNQ의 기존 제한을 보존한다.
- 주간 remaining 7%(used 93%) 정상 handoff이며 primary 5h=null, runtime emergency 없음. 연구 완료·backlog 소진이 아니다. 다음 Astra는 G502 SDSS 공개·대조부터 재개한다.

<!-- luna-sync:SESSION20261004-G501-induction-sync-20261004 -->
## 최신 Luna sync — G501 induction 반영·G502 frontier

- `G501-induction-20261004-01` raw 1건을 반영했다. Queue=processed=7,118 unique, pending=0, duplicate/orphan=0.
- 응시·합격·임용·품계 단계와 명분·결과 구분, 찬성과 우려의 양립을 원raw대로 보존했다. `meta_state.py`: 461 groups·1,560 cases, META150 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G502 전체 blind cases `BPR, BPS, BPT`이며 manifest 1,671건이다.
- 운영 메모: `scripts/codex_quota` 수정본의 300분 primary·10080분 weekly 구분과 null/partial 정규화·`--diagnostics`를 10 fixture로 검증했다. 승인된 외부 조회 결과는 primary=null, weekly used=90%, remaining=10%였고, sandbox 내부 SQLite 직접 조회는 권한 오류로 수행하지 않았다. runtime `<5%` 경고는 없으며 이는 종료·hold 사유가 아니다. 주간 잔여 10%이므로 원자 stage마다 조회하고 7% 이하이면 정상 handoff한다. 신규 semantic raw 없음, pending=0, G502 미열람 상태를 유지한다.
- quota 조회 결과는 `quota_status: unavailable`로 보존한다. runtime emergency 경고는 관측되지 않았으며, unavailable은 종료·hold 근거가 아니다.

<!-- luna-sync:SESSION20261003-G479-META143-sync-20261003 -->
## Luna sync — G479 induction·META143 반영·G480 frontier

- `G479-induction-20261003-01` 및 `META143-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,809 unique, pending=0, duplicate/orphan=0.
- BND ℓ 해석·명시 표기 부재·반례, 90 행동 기준, BNC 비공집합 전제의 AUDIT144 carryover를 raw 그대로 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 439 groups·1,495 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G480 전체 cases `BNE, BNF, BNG`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BNE.json`, `BNF.json`, `BNG.json`이다.

<!-- luna-sync:SESSION20261003-G479-basic-hold-sync-20261003 -->
## Luna sync — G479 기본 stage·BND source hold 반영·induction/META143 대기

- BNB·BNC·BND 기본 12 raw와 `BND-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,807 unique, pending=0, duplicate/orphan=0.
- BND의 `ℓ≥2`는 정본에 별도 표기된 명시 조건이 아니라 본문 예시에서 채택한 해석임을 보존했다. `ℓ=1` 반례와 확신도 0.89, 90 경우 검토 역할 보강 및 최초 31 주도 raw 그대로 유지했다.
- `meta_state.py`: 439 groups·1,495 cases, `meta_due=true`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G479 induction 및 META143 전에는 다음 group으로 넘어가지 않는다. 다음 group G480은 `BNE, BNF, BNG`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BNE.json`, `BNF.json`, `BNG.json`이다.

<!-- luna-sync:SESSION20261003-G478-induction-sync-20261003 -->
## Luna sync — G478 induction 반영·G479 frontier

- `G478-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,794 unique, pending=0, duplicate/orphan=0.
- G478 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 438 groups·1,492 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G479 전체 cases `BNB, BNC, BND`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BNB.json`, `BNC.json`, `BND.json`이다.

<!-- luna-sync:SESSION20261003-G478-basic-sync-20261003 -->
## Luna sync — G478 BMY/BMZ/BNA 기본 4단계 반영·induction 대기

- BMY·BMZ·BNA의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,793 unique, pending=0, duplicate/orphan=0.
- 2024 LEET 정답 PDF를 사용한 공식답 source를 보존했다. BMY94 범위 유보(새 규범 부재와 가치 관점의 가설성 구분), BMZ68 재반론과 전면 입증의 구분, BNA40/42 경계 중첩을 raw 그대로 유지했다.
- `meta_state.py`: 438 groups·1,492 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G478 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G479는 `BNB, BNC, BND`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BNB.json`, `BNC.json`, `BND.json`이다.

<!-- luna-sync:SESSION20261003-G477-induction-sync-20261003 -->
## Luna sync — G477 induction 반영·G478 frontier

- `G477-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,781 unique, pending=0, duplicate/orphan=0.
- 생성/재생 흐름과 순농도, 전체/부분 수율, 고정 출력·효율·투입 구분을 raw 그대로 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 437 groups·1,489 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G478 전체 cases `BMY, BMZ, BNA`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMY.json`, `BMZ.json`, `BNA.json`이다.

<!-- luna-sync:SESSION20261003-G477-basic-sync-20261003 -->
## Luna sync — G477 BMV/BMW/BMX 기본 4단계 반영·induction 대기

- BMV·BMW·BMX의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,780 unique, pending=0, duplicate/orphan=0.
- BMW85 정확 범위 유보, BMX46/49 대체 풀이 및 84/85 동일 조건 표상 중첩, 고정 ATP 조건을 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 437 groups·1,489 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G477 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G478은 `BMY, BMZ, BNA`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMY.json`, `BMZ.json`, `BNA.json`이다.

<!-- luna-sync:SESSION20261003-G476-META142-sync-20261003 -->
## Luna sync — G476 induction·META142 반영·G477 frontier

- `G476-induction-20261003-01` 및 `META142-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,768 unique, pending=0, duplicate/orphan=0.
- 정의 전체/부분 속성, 공존/기능 동일, 순간 지원/수렴 경로 구분과 원 태그 유보를 raw 그대로 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 436 groups·1,486 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G477 전체 cases `BMV, BMW, BMX`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMV.json`, `BMW.json`, `BMX.json`이다.

<!-- luna-sync:SESSION20261003-G476-basic-hold-sync-20261003 -->
## Luna sync — G476 기본 stage·BMT source hold 반영·induction/META142 대기

- BMS·BMT·BMU 기본 12 raw와 `BMT-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,766 unique, pending=0, duplicate/orphan=0.
- BMT 공식 명칭 `배너지와 뒤플로` 복원과 최초 hold를 보존했다. BMS2 범위 유보, BMT58 국소 공통 전제, BMU 지원 후 반복 경로와 임계 경계를 raw 그대로 유지했다.
- `meta_state.py`: 436 groups·1,486 cases, `meta_due=true`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G476 induction 및 META142 전에는 다음 group으로 넘어가지 않는다. 다음 group G477은 `BMV, BMW, BMX`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMV.json`, `BMW.json`, `BMX.json`이다.

<!-- luna-sync:SESSION20261003-G475-induction-sync-20261003 -->
## Luna sync — G475 induction 반영·G476 frontier

- `G475-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,753 unique, pending=0, duplicate/orphan=0.
- G475 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 435 groups·1,483 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G476 전체 cases `BMS, BMT, BMU`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMS.json`, `BMT.json`, `BMU.json`이다.

<!-- luna-sync:SESSION20261003-G475-basic-hold-sync-20261003 -->
## Luna sync — G475 기본 stage·BMR source hold 반영·induction 대기

- BMP·BMQ·BMR 기본 12 raw와 `BMR-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,752 unique, pending=0, duplicate/orphan=0.
- BMR 공식 명칭 `낙론계 유학자들` 복수 복원과 최초 hold를 보존했다. 리기 공존과 기능 동일의 비동일성, 82 결합 후보와 역사 정반합 확정의 한계도 raw 그대로 유지했다.
- `meta_state.py`: 435 groups·1,483 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G475 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G476은 `BMS, BMT, BMU`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMS.json`, `BMT.json`, `BMU.json`이다.

<!-- luna-sync:SESSION20261003-G474-induction-sync-20261003 -->
## Luna sync — G474 induction 반영·G475 frontier

- `G474-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,739 unique, pending=0, duplicate/orphan=0.
- G474 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 434 groups·1,480 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G475 전체 cases `BMP, BMQ, BMR`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMP.json`, `BMQ.json`, `BMR.json`이다.

<!-- luna-sync:SESSION20261003-G474-basic-hold-sync-20261003 -->
## Luna sync — G474 기본 stage·BMN source hold 반영·induction 대기

- BMM·BMN·BMO 기본 12 raw와 `BMN-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,738 unique, pending=0, duplicate/orphan=0.
- BMN21 정의→속성 방향과 역충분성 부정, BMO 혈통 필요요건의 단독 충분화 오류를 raw 그대로 보존했다. BMN 공식 명칭 `마흐디` 복원과 최초 hold도 유지했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 434 groups·1,480 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G474 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G475는 `BMP, BMQ, BMR`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMP.json`, `BMQ.json`, `BMR.json`이다.

<!-- luna-sync:SESSION20261003-BACKFILL141-BLT-sync-20261003 -->
## Luna sync — BLT depth backfill 반영·G474 blind frontier

- `BACKFILL141-BLT-depth_backfill-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,725 unique, pending=0, duplicate/orphan=0.
- K/U/E와 추가 H1~H3를 분리하고, 조건부 증명일 뿐 원문 자족성을 해소하지 않으며 최초 blind에 소급하지 않는다는 한계를 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 433 groups·1,477 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G474 전체 cases `BMM, BMN, BMO`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMM.json`, `BMN.json`, `BMO.json`이다.

<!-- luna-sync:SESSION20261003-AUDIT141-sync-20261003 -->
## Luna sync — AUDIT141 반영·BLT depth backfill 대기·G474 잠금

- `AUDIT141-manual_parity_audit-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,724 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 433 groups·1,477 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[BLT]`, `semantic_state_review=[]`.
- 원판정을 그대로 보존했으며 Luna는 의미 보강을 추가하지 않았다. BLT depth backfill 완료 전에는 G474 group을 열지 않는다.

<!-- luna-sync:SESSION20261003-G473-META141-sync-20261003 -->
## Luna sync — G473 induction·META141 반영·AUDIT141 대기

- `G473-induction-20261003-01` 및 `META141-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,723 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 433 groups·1,477 cases, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- raw의 원문 의미와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 감사 의미 판정이나 backfill을 추가하지 않았다. AUDIT141 완료 전에는 G474 group을 열지 않는다.

<!-- luna-sync:SESSION20261003-G473-basic-hold-sync-20261003 -->
## Luna sync — G473 기본 stage·BML source hold 반영·induction/META141 대기

- BMJ·BMK·BML 기본 12 raw와 `BML-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,721 unique, pending=0, duplicate/orphan=0.
- BML3은 규범적 선차·구성 순서 후보이지 실제 시간 순서 확정이 아님을 보존했다. BMK46 범위 유보와 BML 정본 복원 및 최초 hold 원기록도 raw 그대로 유지했다.
- `meta_state.py`: 433 groups·1,477 cases, `meta_due=true`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G473 induction 및 META141 전에는 다음 group으로 넘어가지 않는다. 다음 group G474는 `BMM, BMN, BMO`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMM.json`, `BMN.json`, `BMO.json`이다.

<!-- luna-sync:SESSION20261003-G472-induction-sync-20261003 -->
## Luna sync — G472 induction 반영·G473 frontier

- `G472-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,708 unique, pending=0, duplicate/orphan=0.
- G472 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 432 groups·1,474 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G473 전체 cases `BMJ, BMK, BML`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMJ.json`, `BMK.json`, `BML.json`이다.

<!-- luna-sync:SESSION20261003-G472-basic-sync-20261003 -->
## Luna sync — G472 BMG/BMH/BMI 기본 4단계 반영·induction 대기

- BMG·BMH·BMI의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,707 unique, pending=0, duplicate/orphan=0.
- BMG91 규범적 비례 후보와 수학적 정비례를 구분하고, BMH4 범위 유보 및 BMI19가 본문 한 저자의 처방 구조라는 점을 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 432 groups·1,474 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G472 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G473은 `BMJ, BMK, BML`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMJ.json`, `BMK.json`, `BML.json`이다.

<!-- luna-sync:SESSION20261003-G471-induction-sync-20261003 -->
## Luna sync — G471 induction 반영·G472 frontier

- `G471-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,695 unique, pending=0, duplicate/orphan=0.
- G471 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 431 groups·1,471 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G472 전체 cases `BMG, BMH, BMI`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMG.json`, `BMH.json`, `BMI.json`이다.

<!-- luna-sync:SESSION20261003-G471-basic-sync-20261003 -->
## Luna sync — G471 BMD/BME/BMF 기본 4단계 반영·induction 대기

- BMD·BME·BMF의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,694 unique, pending=0, duplicate/orphan=0.
- BME 자격 없음과 부도덕·가치 0의 구분, BMF 잠재능력과 현재 실현의 구분 및 site38 범위 유보를 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 431 groups·1,471 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G471 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G472은 `BMG, BMH, BMI`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMG.json`, `BMH.json`, `BMI.json`이다.

<!-- luna-sync:SESSION20261003-G470-META140-sync-20261003 -->
## Luna sync — G470 induction·META140 반영·G471 frontier

- `G470-induction-20261003-01` 및 `META140-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,682 unique, pending=0, duplicate/orphan=0.
- BMC 최초 오답과 해석 강도 유보, G468 공식 범위 복원의 초기 오류·crop 정정 이력을 엄격히 보존했다. AUDIT141 표본 대상 carryover도 유지하며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 430 groups·1,468 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G471 전체 cases `BMD, BME, BMF`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMD.json`, `BME.json`, `BMF.json`이다.

<!-- luna-sync:SESSION20261003-G470-basic-sync-20261003 -->
## Luna sync — G470 BMA/BMB/BMC 기본 4단계 반영·induction/META140 대기

- BMA·BMB·BMC의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,680 unique, pending=0, duplicate/orphan=0.
- BMC 최초 답 ①과 공식 답 ③의 불일치를 보존하며 blind 기록을 덮지 않았다. ③ 특정 진술의 관점 대응과 자각 강도 유보, 32 국소 교집합만 확인(양차집합 미입증), 19 범위 유보도 raw 그대로 보존했다.
- `meta_state.py`: 430 groups·1,468 cases, `meta_due=true`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G470 induction 및 META140 전에는 다음 group으로 넘어가지 않는다. 다음 group G471은 `BMD, BME, BMF`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMD.json`, `BME.json`, `BMF.json`이다.

<!-- luna-sync:SESSION20261003-G469-induction-sync-20261003 -->
## Luna sync — G469 induction 반영·G470 frontier

- `G469-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,668 unique, pending=0, duplicate/orphan=0.
- G469 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 429 groups·1,465 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G470 전체 cases `BMA, BMB, BMC`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMA.json`, `BMB.json`, `BMC.json`이다.

<!-- luna-sync:SESSION20261003-G469-basic-sync-20261003 -->
## Luna sync — G469 BLX/BLY/BLZ 기본 4단계 반영·induction 대기

- BLX·BLY·BLZ의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,667 unique, pending=0, duplicate/orphan=0.
- 2021 LEET 배포용 HWP 답 source를 사용한 BLX/BLY 같은 45의 하위 행동 차이와 BLZ19/59/40 층위 유보를 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 429 groups·1,465 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G469 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G470은 `BMA, BMB, BMC`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BMA.json`, `BMB.json`, `BMC.json`이다.

<!-- luna-sync:SESSION20261003-G468-induction-sync-20261003 -->
## Luna sync — G468 induction 반영·G469 frontier

- `G468-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,655 unique, pending=0, duplicate/orphan=0.
- 공식 범위 복원의 초기 오류와 crop 직접 확인에 따른 정정 이력을 원raw대로 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 428 groups·1,462 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G469 전체 cases `BLX, BLY, BLZ`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLX.json`, `BLY.json`, `BLZ.json`이다.

<!-- luna-sync:SESSION20261003-G468-hold-resolution-sync-20261003 -->
## Luna sync — G468 기본 stage·BLV source hold/해소 raw 반영·induction 대기

- BLU·BLV·BLW 기본 12 raw, `BLV-hold-source-20261003-01`, `G468-hold-source-resolved-20261003-01` 총 14 raw를 기존 처리기로 반영했다. Queue=processed=6,654 unique, pending=0, duplicate/orphan=0.
- BLV 최초 blind 기록과 `[A]` 범위 오기에서 공식 crop 직접 확인으로 정정한 이력을 함께 보존했다. BLW71은 관련성 충족 전제에서 ⑤의 실질 보조로 추가하고 ③ 정답 주를 유지했다. 그룹 hold 해소는 새 완료 case로 계수하지 않았다.
- `meta_state.py`: 428 groups·1,462 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G468 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G469는 `BLX, BLY, BLZ`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLX.json`, `BLY.json`, `BLZ.json`이다.

<!-- luna-sync:SESSION20261003-G467-META139-sync-20261003 -->
## Luna sync — G467 induction·META139 반영·G468 frontier

- `G467-induction-20261003-01` 및 `META139-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,640 unique, pending=0, duplicate/orphan=0.
- BLR/BLT의 배경지식 한계를 원문 자족 근거로 승격하지 않는 메타 기준을 보존했다. raw의 원문 의미와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 427 groups·1,459 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G468 전체 cases `BLU, BLV, BLW`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLU.json`, `BLV.json`, `BLW.json`이다.

<!-- luna-sync:SESSION20261003-G467-basic-hold-sync-20261003 -->
## Luna sync — G467 기본 stage·BLR 수식 source hold 반영·induction/META139 대기

- BLR·BLS·BLT 기본 12 raw와 `BLR-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,638 unique, pending=0, duplicate/orphan=0.
- BLR·BLT의 배경 물리지식 보조 사용 및 원문만으로 완결되지 않는 한계를 raw 그대로 보존했다. BLR 수식 복원 원기록과 BLS98/BLT2 범위 유보도 유지했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 427 groups·1,459 cases, `meta_due=true`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G467 induction 및 META139 전에는 다음 group으로 넘어가지 않는다. 다음 group G468은 `BLU, BLV, BLW`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLU.json`, `BLV.json`, `BLW.json`이다.

<!-- luna-sync:SESSION20261003-G466-induction-sync-20261003 -->
## Luna sync — G466 induction 반영·G467 frontier

- `G466-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,625 unique, pending=0, duplicate/orphan=0.
- G466 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 426 groups·1,456 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G467 전체 cases `BLR, BLS, BLT`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLR.json`, `BLS.json`, `BLT.json`이다.

<!-- luna-sync:SESSION20261003-G466-basic-sync-20261003 -->
## Luna sync — G466 BLO/BLP/BLQ 기본 4단계 반영·induction 대기

- BLO·BLP·BLQ의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,624 unique, pending=0, duplicate/orphan=0.
- 15/10의 기준·필요요건 중첩과 13/12의 배타·조건 표상 중첩을 별개 필수 연산으로 계수하지 않는 판정을 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- 격리 SQLite probe도 30초 내 initialize 응답을 받지 못해 실제 quota 수치는 확인되지 않았다. 이 운영 한계는 연구 종료 조건으로 사용하지 않는다. 기존 auth/DB·repo helper와 프로브는 변경하지 않았다.
- `meta_state.py`: 426 groups·1,456 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G466 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G467은 `BLR, BLS, BLT`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLR.json`, `BLS.json`, `BLT.json`이다.

<!-- luna-sync:SESSION20261003-G465-induction-sync-20261003 -->
## Luna sync — G465 induction 반영·G466 frontier

- `G465-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,612 unique, pending=0, duplicate/orphan=0.
- G465 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 425 groups·1,453 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G466 전체 cases `BLO, BLP, BLQ`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLO.json`, `BLP.json`, `BLQ.json`이다.

<!-- luna-sync:SESSION20261003-G465-basic-sync-20261003 -->
## Luna sync — G465 BLL/BLM/BLN 기본 4단계 반영·induction 대기

- BLL·BLM·BLN의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,611 unique, pending=0, duplicate/orphan=0.
- 사이트 포괄 구조와 정답 국소 판정의 차이, BLN 외모 동일과 모든 속성 동일의 비동일성을 뒷받침하는 원문 근거를 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 425 groups·1,453 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G465 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G466은 `BLO, BLP, BLQ`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLO.json`, `BLP.json`, `BLQ.json`이다.

<!-- luna-sync:SESSION20261003-AUDIT138-sync-20261003 -->
## Luna sync — AUDIT138 반영·G465 blind frontier

- `AUDIT138-manual_parity_audit-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,599 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 424 groups·1,450 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 표본감사에서 새 semantic backfill이 없다는 판정은 기존 유보를 해소하지 않는다. 띄어쓰기 가독성 제한도 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- 다음 blind frontier는 G465 전체 cases `BLL, BLM, BLN`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLL.json`, `BLM.json`, `BLN.json`이다.

<!-- luna-sync:SESSION20261003-G464-META138-sync-20261003 -->
## Luna sync — G464 induction·META138 반영·AUDIT138 대기

- `G464-induction-20261003-01` 및 `META138-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,598 unique, pending=0, duplicate/orphan=0.
- raw의 원문 의미와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 424 groups·1,450 cases, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- AUDIT138 완료 전에는 다음 G465 group을 열지 않는다. 감사 내용과 필요한 보강은 주 Astra가 직접 수행한다.

<!-- luna-sync:SESSION20261003-G464-basic-sync-20261003 -->
## Luna sync — G464 BLI/BLJ/BLK 기본 4단계 반영·induction/META138 대기

- BLI·BLJ·BLK의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,596 unique, pending=0, duplicate/orphan=0.
- BLI55 오답 범위 추가, BLJ88 유보, BLK59 정책·성과 층위 후보를 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 424 groups·1,450 cases, `meta_due=true`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G464 induction 및 META138 전에는 다음 group으로 넘어가지 않는다. 다음 group G465는 `BLL, BLM, BLN`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLL.json`, `BLM.json`, `BLN.json`이다.

<!-- luna-sync:SESSION20261003-G463-induction-sync-20261003 -->
## Luna sync — G463 induction 반영·G464 frontier

- `G463-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,584 unique, pending=0, duplicate/orphan=0.
- BLF01 최초 원장을 유지하며 SDSS 공개 전 독립코드정정02의 보조코드 4 철회를 후속 판정으로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 423 groups·1,447 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G464 전체 cases `BLI, BLJ, BLK`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLI.json`, `BLJ.json`, `BLK.json`이다. G464 이후 manifest상 순차 prepared 잔량은 216 cases·74 groups, 마지막 case ID는 `BTP`이다.

<!-- luna-sync:SESSION20261003-G463-correction-sync-20261003 -->
## Luna sync — G463 기본 stage·BLG source hold·BLF 후속 정정 반영·induction 대기

- BLF·BLG·BLH 기본 12 raw, `BLG-hold-source-20261003-01`, `BLF-independent_code-20261003-02` 총 14 raw를 기존 처리기로 반영했다. Queue=processed=6,583 unique, pending=0, duplicate/orphan=0.
- BLG는 정답 공개 전 공식 2020 HWP에서 실제 명칭 `‘초봉’의 몰락 과정`과 발문을 복원한 뒤 blind 완료했으며 최초 hold 원기록을 보존했다. BLF01 최초 원장을 유지하고 SDSS 공개 전 independent_code의 보조코드 4 철회는 후속 판정으로 함께 보존했다. BLH12 근거 부족 및 범위 유보도 raw 그대로 유지했다.
- `meta_state.py`: 423 groups·1,447 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G463 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G464은 `BLI, BLJ, BLK`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLI.json`, `BLJ.json`, `BLK.json`이다.

<!-- luna-sync:SESSION20261003-G462-induction-sync-20261003 -->
## Luna sync — G462 induction 반영·G463 frontier

- `G462-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,569 unique, pending=0, duplicate/orphan=0.
- G462 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 422 groups·1,444 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G463 전체 cases `BLF, BLG, BLH`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLF.json`, `BLG.json`, `BLH.json`이다.

<!-- luna-sync:SESSION20261003-G462-basic-sync-20261003 -->
## Luna sync — G462 BLC/BLD/BLE 기본 4단계 반영·induction 대기

- BLC·BLD·BLE의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,568 unique, pending=0, duplicate/orphan=0.
- BLC12 추가와 5 최초 판정, BLE 한 질량 중복과 전체 식별 불가능의 구분을 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 422 groups·1,444 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G462 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G463은 `BLF, BLG, BLH`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLF.json`, `BLG.json`, `BLH.json`이다.

<!-- luna-sync:SESSION20261003-G461-META137-sync-20261003 -->
## Luna sync — G461 induction·META137 반영·G462 frontier

- `G461-induction-20261003-01` 및 `META137-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,556 unique, pending=0, duplicate/orphan=0.
- raw의 원문 의미와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 421 groups·1,441 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G462 전체 cases `BLC, BLD, BLE`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLC.json`, `BLD.json`, `BLE.json`이다.

<!-- luna-sync:SESSION20261003-G461-basic-sync-20261003 -->
## Luna sync — G461 BKZ/BLA/BLB 기본 4단계 반영·induction/META137 대기

- BKZ·BLA·BLB의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,554 unique, pending=0, duplicate/orphan=0.
- BLA1 누락의 공개 후 핵심 후보 추가와 75 최초 판정, BLB98 범위 유보를 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 421 groups·1,441 cases, `meta_due=true`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G461 induction 및 META137 전에는 다음 group으로 넘어가지 않는다. 다음 group G462은 `BLC, BLD, BLE`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BLC.json`, `BLD.json`, `BLE.json`이다.

<!-- luna-sync:SESSION20261003-G460-induction-sync-20261003 -->
## Luna sync — G460 induction 반영·G461 frontier

- `G460-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,542 unique, pending=0, duplicate/orphan=0.
- G460 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 420 groups·1,438 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G461 전체 cases `BKZ, BLA, BLB`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKZ.json`, `BLA.json`, `BLB.json`이다.

<!-- luna-sync:SESSION20261003-G460-basic-sync-20261003 -->
## Luna sync — G460 BKW/BKX/BKY 기본 4단계 반영·induction 대기

- BKW·BKX·BKY의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,541 unique, pending=0, duplicate/orphan=0.
- 2020 LEET 공식답 source를 사용한 BKX63 논거 효과와 공격 대상 식별의 구분, BKY26 기준상 이분류 후보를 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 420 groups·1,438 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G460 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G461은 `BKZ, BLA, BLB`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKZ.json`, `BLA.json`, `BLB.json`이다.

<!-- luna-sync:SESSION20261003-G459-induction-sync-20261003 -->
## Luna sync — G459 induction 반영·G460 frontier

- `G459-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,529 unique, pending=0, duplicate/orphan=0.
- G459 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 419 groups·1,435 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G460 전체 cases `BKW, BKX, BKY`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKW.json`, `BKX.json`, `BKY.json`이다.

<!-- luna-sync:SESSION20261003-G459-basic-hold-sync-20261003 -->
## Luna sync — G459 기본 stage·BKU source hold 반영·induction 대기

- BKT·BKU·BKV 기본 12 raw와 `BKU-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,528 unique, pending=0, duplicate/orphan=0.
- BKU는 정답 공개 전 공식 HWP에서 실제 명칭 `최근의 극우민족주의`와 발문을 복원한 뒤 blind 완료했으며, 최초 source hold 원기록을 보존했다. BKT19 지문 후보 정확 범위 유보와 BKV2 가능성 한계도 raw 그대로 보존했다.
- `meta_state.py`: 419 groups·1,435 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G459 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G460은 `BKW, BKX, BKY`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKW.json`, `BKX.json`, `BKY.json`이다.

<!-- luna-sync:SESSION20261003-G458-META136-sync-20261003 -->
## Luna sync — G458 induction·META136 반영·G459 frontier

- `G458-induction-20261003-01` 및 `META136-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,515 unique, pending=0, duplicate/orphan=0.
- raw의 원문 의미와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다. 기존 기록의 `BKR98` 표기는 `BKQ98`로 기계적으로 정정했다.
- `meta_state.py`: 418 groups·1,432 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G459 전체 cases `BKT, BKU, BKV`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKT.json`, `BKU.json`, `BKV.json`이다.

<!-- luna-sync:SESSION20261003-G458-basic-hold-sync-20261003 -->
## Luna sync — G458 기본 stage·BKQ source hold 반영·induction/META136 대기

- BKQ·BKR·BKS 기본 12 raw와 `BKQ-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,513 unique, pending=0, duplicate/orphan=0.
- BKQ는 정답 공개 전 공식 HWP에서 실제 명칭 `온톨로지`와 발문을 복원한 뒤 blind 완료했으며, 최초 source hold 원기록을 보존했다. BKQ98 관계 판독 후보 범위 유보와 BKS27/22 중첩도 raw 그대로 보존했다.
- quota 조회의 SQLite state runtime 초기화 실패는 운영 한계로만 기록한다. 실제 한도값이 아니며 세션 종료·handoff trigger로 사용하지 않는다. 계정·설정·스크립트는 수정하지 않았다.
- `meta_state.py`: 418 groups·1,432 cases, `meta_due=true`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G458 induction 및 META136 전에는 다음 group으로 넘어가지 않는다. 다음 group G459은 `BKT, BKU, BKV`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKT.json`, `BKU.json`, `BKV.json`이다.

<!-- luna-sync:SESSION20261003-G457-induction-sync-20261003 -->
## Luna sync — G457 induction 반영·G458 frontier

- `G457-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,500 unique, pending=0, duplicate/orphan=0.
- G457 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 417 groups·1,429 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G458 전체 cases `BKQ, BKR, BKS`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKQ.json`, `BKR.json`, `BKS.json`이다.

<!-- luna-sync:SESSION20261003-G457-basic-hold-sync-20261003 -->
## Luna sync — G457 기본 stage·BKO source hold 반영·induction 대기

- BKN·BKO·BKP 기본 12 raw와 `BKO-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,499 unique, pending=0, duplicate/orphan=0.
- BKO는 정답 공개 전 공식 HWP에서 실제 명칭 `비판`과 발문을 복원한 뒤 blind 완료했으며, 최초 source hold 원기록을 보존했다. BKN19/20 층위 차이와 BKP20 현상·기능 및 물질·정신 축 차이 유보도 raw 그대로 보존했다.
- `meta_state.py`: 417 groups·1,429 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G457 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G458은 `BKQ, BKR, BKS`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKQ.json`, `BKR.json`, `BKS.json`이다.

<!-- luna-sync:SESSION20261003-G456-induction-sync-20261003 -->
## Luna sync — G456 induction 반영·G457 frontier

- `G456-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,486 unique, pending=0, duplicate/orphan=0.
- G456 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 416 groups·1,426 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G457 전체 cases `BKN, BKO, BKP`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKN.json`, `BKO.json`, `BKP.json`이다.

<!-- luna-sync:SESSION20261003-G456-basic-sync-20261003 -->
## Luna sync — G456 BKL/BKM 기본 4단계 반영·induction 대기

- BKL·BKM의 blind·answer_check·independent_code·sdss_compare 총 8 raw를 기존 처리기로 반영했다. Queue=processed=6,485 unique, pending=0, duplicate/orphan=0.
- BKL42 정답의 국소 대표 병렬 후보와 74 최초 주, BKM59/46 유보를 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 416 groups·1,426 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G456 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group G457은 `BKN, BKO, BKP`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKN.json`, `BKO.json`, `BKP.json`이다.

<!-- luna-sync:SESSION20261003-BACKFILL135-BKK-sync-20261003 -->
## Luna sync — BKK depth backfill 반영·G456 blind frontier

- `BACKFILL135-BKK-depth_backfill-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,477 unique, pending=0, duplicate/orphan=0.
- 65의 배제에 고의성 부재를 사용하지 않는 보강, 65 국소 후보와 64 경계 유보, 62 최초 주 유지를 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 415 groups·1,424 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G456 전체 cases `BKL, BKM`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKL.json`, `BKM.json`이다.

<!-- luna-sync:SESSION20261003-AUDIT135-sync-20261003 -->
## Luna sync — AUDIT135 반영·BKK depth backfill 대기·G456 잠금

- `AUDIT135-manual_parity_audit-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,476 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 415 groups·1,424 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[BKK]`, `semantic_state_review=[]`.
- AUDIT135의 BKK depth backfill 완료 전에는 G456 group을 열지 않는다. Luna는 의미 판단이나 보강을 추가하지 않았다.

<!-- luna-sync:SESSION20261003-G455-META135-sync-20261003 -->
## Luna sync — G455 induction·META135 반영·AUDIT135 대기

- `G455-induction-20261003-01` 및 `META135-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,475 unique, pending=0, duplicate/orphan=0.
- raw의 원문 의미와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 415 groups·1,424 cases, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- AUDIT135 및 주 Astra의 필요한 depth backfill 전에는 다음 G456 group을 열지 않는다.

<!-- luna-sync:SESSION20261003-G455-basic-hold-sync-20261003 -->
## Luna sync — G455 기본 stage·BKK source hold 반영·induction/META135 대기

- BKI·BKJ·BKK 기본 12 raw와 `BKK-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,473 unique, pending=0, duplicate/orphan=0.
- BKK는 정답 공개 전 공식 HWP에서 실제 명칭 `문제점`과 발문을 복원한 뒤 blind 완료했으며, 최초 source hold 원기록을 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 415 groups·1,424 cases, `meta_due=true`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G455 induction 및 META135 전에는 다음 group으로 넘어가지 않는다. 다음 group G456은 `BKL, BKM`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKL.json`, `BKM.json`이다.

<!-- luna-sync:SESSION20261003-G454-induction-sync-20261003 -->
## Luna sync — G454 induction 반영·G455 frontier

- `G454-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,460 unique, pending=0, duplicate/orphan=0.
- G454 induction raw와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 414 groups·1,421 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G455 전체 cases `BKI, BKJ, BKK`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKI.json`, `BKJ.json`, `BKK.json`이다.

<!-- luna-sync:SESSION20261003-G454-basic-sync-20261003 -->
## Luna sync — G454 BKF/BKG/BKH 기본 4단계 반영·induction 대기

- BKF·BKG·BKH의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,459 unique, pending=0, duplicate/orphan=0.
- BKF83 국소 보조 상향, BKG98 실제로부터 관계의 국소 후보 및 범위 유보, BKH26 대조와 배타성의 구분을 raw 그대로 보존했다. Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 414 groups·1,421 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G454 induction 전에는 다음 group으로 넘어가지 않는다. 다음 group은 G455 `BKI, BKJ, BKK`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKI.json`, `BKJ.json`, `BKK.json`이다.

<!-- luna-sync:SESSION20261003-G453-induction-sync-20261003 -->
## Luna sync — G453 induction 반영·G454 frontier

- `G453-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,447 unique, pending=0, duplicate/orphan=0.
- G453 induction raw 의미와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 413 groups·1,418 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 blind frontier는 G454 전체 cases `BKF, BKG, BKH`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKF.json`, `BKG.json`, `BKH.json`이다.

<!-- luna-sync:SESSION20261003-G453-basic-sync-20261003 -->
## Luna sync — G453 BKC/BKD/BKE 기본 4단계 반영·induction 대기

- BKC·BKD·BKE의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,446 unique, pending=0, duplicate/orphan=0.
- BKE visual02 눈금 부분 잘림으로 답 결정에 필요한 비율을 추정하지 않았다는 제한을 raw 그대로 보존했다. 기존 최초 기록·사이트 태그·유보도 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 413 groups·1,418 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G453 induction 전 다음 group은 잠금 유지한다. 다음 actionable group은 G454 전체 cases `BKF, BKG, BKH`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKF.json`, `BKG.json`, `BKH.json`이다.

<!-- luna-sync:SESSION20261003-G452-META134-sync-20261003 -->
## Luna sync — G452 induction·META134 반영·G453 frontier

- `G452-induction-20261003-01` 및 `META134-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,434 unique, pending=0, duplicate/orphan=0.
- raw의 원문 의미와 기존 최초 기록·사이트 태그·유보를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 412 groups·1,415 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 actionable group은 G453 전체 cases `BKC, BKD, BKE`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BKC.json`, `BKD.json`, `BKE.json`이다.

<!-- luna-sync:SESSION20261003-G452-basic-sync-20261003 -->
## Luna sync — G452 BKA/BKB blind·BJZ/BKA/BKB 기본 4단계 반영·G452 induction 대기

- `BKA`, `BKB` blind 및 `BJZ/BKA/BKB` answer_check·independent_code·sdss_compare 총 11 raw를 기존 처리기로 반영했다. Queue=processed=6,432 unique, pending=0, duplicate/orphan=0.
- G452 세 cases의 group-wide blind·answer·independent·SDSS barrier가 raw 순서대로 충족되었다. Astra raw 의미를 보존했으며 Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 412 groups·1,415 cases, `meta_due=true`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- prepared backlog manifest는 1,671건이며 `consumed_sdss=1,415`, `prepared=256`이다. G452 induction 및 다음 의무는 주 Astra가 수행한다.

<!-- luna-sync:SESSION20261003-BJZ-blind-sync-20261003 -->
## Luna sync — BJZ blind raw 반영·G452 blind barrier 진행 중

- `BJZ-blind-20261003-01` 미처리 raw 1건을 기존 처리기로 반영했다. Queue=processed=6,421 unique, pending=0, duplicate/orphan=0.
- BJZ 최초 답 ④·확신도 0.99·공식 답/SDSS/기존 판정 미노출 기록을 보존했다. `past_exposure=unknown`, `strict_blind_eligible=false`도 원raw 그대로 유지한다.
- G452의 blind 완료는 BJZ 1/3이다. 같은 group의 `BKA`, `BKB` blind raw가 저장되기 전에는 answer_check를 시작하지 않는다. 다음 Excel-style case ID는 `BKA`이다.
- `meta_state.py`: 411 groups·1,412 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- prepared backlog manifest는 1,671건이며 `consumed_sdss=1,412`, `prepared=259`이다. 최소 잔량 미만이 아니므로 기계적 후보 추가는 하지 않았다. BJZ/BKA/BKB blind source와 sealed answer/SDSS는 분리되어 있다.

<!-- luna-sync:SESSION20261003-G451-induction-sync-20261003 -->
## Luna sync — G451 induction 반영·G452 frontier

- `G451-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,420 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G452 전체 cases `BJZ, BKA, BKB`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BJZ.json`, `BKA.json`, `BKB.json`이다.

<!-- luna-sync:SESSION20261003-G451-sourcehold-sync-20261003 -->
## Luna sync — G451 기본 stage·BJX source hold 반영·induction 대기

- BJW·BJX·BJY 기본 12 raw와 `BJX-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,419 unique, pending=0, duplicate/orphan=0.
- BJX 답 공개 전 명칭 복원으로 source hold는 해소됐지만 최초 원장을 보존한다. BJY61 무관 배경정보 기능(출제 의도 추정 아님)도 raw 그대로 유지한다.
- `meta_state.py`: 411 groups·1,412 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G451 induction 전에는 다음 group으로 넘어가지 않는다. Luna는 의미 판단을 추가하거나 수정하지 않았다.

<!-- luna-sync:SESSION20261003-G450-induction-sync-20261003 -->
## Luna sync — G450 induction 반영·G451 frontier

- `G450-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,406 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G451 전체 cases `BJW, BJX, BJY`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BJW.json`, `BJX.json`, `BJY.json`이다.

<!-- luna-sync:SESSION20261003-G450-basic-sync-20261003 -->
## Luna sync — G450 BJT/BJU/BJV 기본 4단계 반영·induction 대기

- BJT·BJU·BJV의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,405 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 410 groups·1,409 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BJT48 범위, BJU52 국소 통제 감소, BJV24 특수 환경 범위 유보를 raw 그대로 보존한다. G450 induction 전 다음 group은 잠금 유지한다.

<!-- luna-sync:SESSION20261003-G449-META133-sync-20261003 -->
## Luna sync — G449 induction·META133 반영·G450 frontier·구조 감사

- `G449-induction-20261003-01` 및 `META133-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,393 unique, pending=0, duplicate/orphan=0.
- META133 필수 12필드와 유보를 raw 그대로 보존했다. `meta_state.py`: 409 groups·1,406 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G447~G449 11 cases 실제 queue 구조 감사: group-wide barrier 위반 0, 경쟁 코드 2~4개 위반 0, 최초답-공식답 불일치 0, raw record_id 중복 0. 의미 전수검증이 아닌 기계 구조 검증이다.
- 다음 frontier는 G450 전체 cases `BJT, BJU, BJV`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BJT.json`, `BJU.json`, `BJV.json`이다.

<!-- luna-sync:SESSION20261003-G449-sourcehold-sync-20261003 -->
## Luna sync — G449 기본 stage·BJR source hold 반영·induction/META133 대기

- BJP·BJQ·BJR·BJS 기본 16 raw와 `BJR-hold-source-20261003-01` 총 17 raw를 기존 처리기로 반영했다. Queue=processed=6,391 unique, pending=0, duplicate/orphan=0.
- BJR 답 공개 전 명칭 복원으로 source hold는 해소됐지만 최초 원장을 보존한다. BJP99 및 BJR48 사이트 범위 유보도 raw 그대로 유지한다.
- `meta_state.py`: 409 groups·1,406 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G449 induction 및 META133 전에는 다음 group으로 넘어가지 않는다. Luna는 의미 판단을 추가하거나 수정하지 않았다.

<!-- luna-sync:SESSION20261003-G448-induction-sync-20261003 -->
## Luna sync — G448 induction 반영·G449 frontier

- `G448-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,374 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G449 전체 cases `BJP, BJQ, BJR, BJS`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BJP.json`, `BJQ.json`, `BJR.json`, `BJS.json`이다.

<!-- luna-sync:SESSION20261003-G448-basic-sync-20261003 -->
## Luna sync — G448 BJL/BJM/BJN/BJO 기본 4단계 반영·induction 대기

- BJL·BJM·BJN·BJO의 blind·answer_check·independent_code·sdss_compare 총 16 raw를 기존 처리기로 반영했다. Queue=processed=6,373 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 408 groups·1,402 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BJM 시간 되돌리기와 현재 살해의 구분, BJN 평가 불가·중립값 구분 및 19 유보를 raw 그대로 보존한다. G448 induction 전 다음 group은 잠금 유지한다.

<!-- luna-sync:SESSION20261003-G447-induction-sync-20261003 -->
## Luna sync — G447 induction 반영·G448 frontier

- `G447-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,357 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G448 전체 cases `BJL, BJM, BJN, BJO`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BJL.json`, `BJM.json`, `BJN.json`, `BJO.json`이다.

<!-- luna-sync:SESSION20261003-G447-basic-sync-20261003 -->
## Luna sync — G447 BJI/BJJ/BJK 기본 4단계 반영·induction 대기

- BJI·BJJ·BJK의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,356 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 407 groups·1,398 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 선택적 경로 차단·본문 우회 없는 모형·강화와 반증 구분을 raw 그대로 보존한다. G447 induction 전 다음 group은 잠금 유지한다.

<!-- luna-sync:SESSION20261003-BACKFILL132-BJG-sync-20261003 -->
## Luna sync — BJG depth backfill 반영·G447 frontier

- `BACKFILL132-BJG-depth_backfill-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,344 unique, pending=0, duplicate/orphan=0.
- BJG 69 surface→실질 보조 상향과 최초 62 주·유일 주 유보를 raw 그대로 보존한다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G447 전체 cases `BJI, BJJ, BJK`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BJI.json`, `BJJ.json`, `BJK.json`이다.

<!-- luna-sync:SESSION20261003-AUDIT132-sync-20261003 -->
## Luna sync — AUDIT132 반영·BJG depth backfill 잠금

- `AUDIT132-manual_parity_audit-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,343 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[BJG]`, `semantic_state_review=[]`.
- BJG depth backfill 완료 전 다음 group frontier는 잠금 유지한다. Luna는 의미 판단을 추가하거나 수정하지 않았다.

<!-- luna-sync:SESSION20261003-G446-META132-sync-20261003 -->
## Luna sync — G446 induction·META132 반영·AUDIT132 잠금·구조 감사

- `G446-induction-20261003-01` 및 `META132-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,342 unique, pending=0, duplicate/orphan=0.
- META132 필수 12필드와 유보를 raw 그대로 보존했다. `meta_state.py`: 406 groups·1,395 cases, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G444~G446 8 cases 실제 queue 구조 감사: group-wide barrier 위반 0, 경쟁 코드 2~4개 위반 0, 최초답-공식답 불일치 0, raw record_id 중복 0. 의미 전수검증이 아닌 기계 구조 검증이다.
- AUDIT132 반영 전 다음 group 잠금 유지한다.

<!-- luna-sync:SESSION20261003-G446-sourcehold-sync-20261003 -->
## Luna sync — G446 기본 stage·BJF source hold 반영·induction/META132 대기

- BJF·BJG·BJH 기본 12 raw와 `BJF-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,340 unique, pending=0, duplicate/orphan=0.
- BJF 답 공개 전 명칭 복원으로 source hold는 해소됐지만 최초 원장을 보존한다. BJG69 주·보조 유보도 raw 그대로 유지한다.
- `meta_state.py`: 406 groups·1,395 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G446 induction 및 META132 전에는 다음 group으로 넘어가지 않는다. Luna는 의미 판단을 추가하거나 수정하지 않았다.

<!-- luna-sync:SESSION20261003-G445-induction-sync-20261003 -->
## Luna sync — G445 induction 반영·G446 frontier

- `G445-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,327 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G446 전체 cases `BJF, BJG, BJH`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BJF.json`, `BJG.json`, `BJH.json`이다.

<!-- luna-sync:SESSION20261003-G445-basic-sync-20261003 -->
## Luna sync — G445 BJC/BJD/BJE 기본 4단계 반영·induction 대기

- BJC·BJD·BJE의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,326 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 405 groups·1,392 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BJD19 범위 유보, BJE 특정 DAG에서만 3단계 중복 및 순환 반모형을 raw 그대로 보존한다. 4n 서식 불확실성은 이번 판정에 사용하지 않았다는 제한도 보존한다. G445 induction 전 다음 group은 잠금 유지한다.

<!-- luna-sync:SESSION20261003-G444-induction-sync-20261003 -->
## Luna sync — G444 induction 반영·G445 frontier

- `G444-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,314 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G445 전체 cases `BJC, BJD, BJE`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BJC.json`, `BJD.json`, `BJE.json`이다.

<!-- luna-sync:SESSION20261003-G444-sourcehold-sync-20261003 -->
## Luna sync — G444 기본 stage·BJB source hold 반영·induction 대기

- BJA·BJB 기본 8 raw와 `BJB-hold-source-20261003-01` 총 9 raw를 기존 처리기로 반영했다. Queue=processed=6,313 unique, pending=0, duplicate/orphan=0.
- BJB 희생자 의식·발문 복원으로 source hold는 해소됐지만 최초 원장 보존을 유지한다. BJA42 범위 유보와 BJB59 과제 구조도 raw 그대로 보존한다.
- `meta_state.py`: 404 groups·1,389 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G444 induction 전에는 다음 group으로 넘어가지 않는다. Luna는 의미 판단을 추가하거나 수정하지 않았다.

<!-- luna-sync:SESSION20261003-G443-META131-sync-20261003 -->
## Luna sync — G443 induction·META131 반영·G444 frontier·구조 감사

- `G443-induction-20261003-01` 및 `META131-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,304 unique, pending=0, duplicate/orphan=0.
- META131 필수 12필드와 유보를 raw 그대로 보존했다. `meta_state.py`: 403 groups·1,387 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G438~G443 신규 17 cases 실제 queue 구조 감사: group-wide barrier 위반 0, 경쟁 코드 2~4개 위반 0, 최초답-공식답 불일치 0, raw record_id 중복 0. 의미 전수검증이 아닌 기계 구조 검증이다.
- 다음 frontier는 G444 전체 cases `BJA, BJB`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BJA.json`, `BJB.json`이다.

<!-- luna-sync:SESSION20261003-G443-basic-sync-20261003 -->
## Luna sync — G443 BIX/BIY/BIZ 기본 4단계 반영·induction/META131 대기

- BIX·BIY·BIZ의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,302 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 403 groups·1,387 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BIY19 사이트 범위 미확정과 BIZ75/12 역할 구분을 raw 그대로 보존한다. G443 induction과 META131 전에는 다음 group으로 넘어가지 않는다.

<!-- luna-sync:SESSION20261003-G442-induction-sync-20261003 -->
## Luna sync — G442 induction 반영·G443 frontier

- `G442-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,290 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G443 전체 cases `BIX, BIY, BIZ`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BIX.json`, `BIY.json`, `BIZ.json`이다.

<!-- luna-sync:SESSION20261003-G442-basic-sync-20261003 -->
## Luna sync — G442 BIU/BIV/BIW 기본 4단계 반영·induction 대기

- BIU·BIV·BIW의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,289 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 402 groups·1,384 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BIU40 surface의 공개 후 실질 보조 상향 기록은 최초 판정과 분리 보존하며, BIW50 오답 범위도 raw 그대로 유지한다. G442 induction 전 다음 group은 잠금 유지한다.

<!-- luna-sync:SESSION20261003-G441-induction-sync-20261003 -->
## Luna sync — G441 induction 반영·G442 frontier

- `G441-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,277 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G442 전체 cases `BIU, BIV, BIW`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BIU.json`, `BIV.json`, `BIW.json`이다.

<!-- luna-sync:SESSION20261003-G441-basic-sync-20261003 -->
## Luna sync — G441 BIR/BIS/BIT 기본 4단계 반영·induction 대기

- BIR·BIS·BIT의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,276 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 401 groups·1,381 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BIR 공유 명제와 실제 논증 전제의 한계, BIT 양립·지지·확정 구분을 raw 그대로 보존한다. G441 induction 전 다음 group은 잠금 유지한다.

<!-- luna-sync:SESSION20261003-G440-META130-sync-20261003 -->
## Luna sync — G440 induction·META130 반영·G441 frontier

- `G440-induction-20261003-01` 및 `META130-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,264 unique, pending=0, duplicate/orphan=0.
- META130 필수 12필드와 유보를 raw 그대로 보존했다. `meta_state.py`: 400 groups·1,378 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G441 전체 cases `BIR, BIS, BIT`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BIR.json`, `BIS.json`, `BIT.json`이다.

<!-- luna-sync:SESSION20261003-G440-basic-sync-20261003 -->
## Luna sync — G440 BIO/BIP/BIQ 기본 4단계 반영·induction/META130 대기

- BIO·BIP·BIQ의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,262 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 400 groups·1,378 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BIQ [A]는 답 공개 후 SDSS 전 Astra 확인과 최초 추정의 시간차를 raw 그대로 보존한다. G440 induction 및 META130 전에는 다음 group으로 넘어가지 않는다.

<!-- luna-sync:SESSION20261003-G439-induction-sync-20261003 -->
## Luna sync — G439 induction 반영·G440 frontier

- `G439-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,250 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G440 전체 cases `BIO, BIP, BIQ`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BIO.json`, `BIP.json`, `BIQ.json`이다.

<!-- luna-sync:SESSION20261003-G439-basic-sync-20261003 -->
## Luna sync — G439 BIL/BIM/BIN 기본 4단계 반영·induction 대기

- BIL·BIM·BIN의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,249 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 399 groups·1,375 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BIL51 사이트 범위 및 BIN 여성 본인 형벌 해석 미확정을 raw 그대로 보존한다. G439 induction 전 다음 group은 잠금 유지한다.

<!-- luna-sync:SESSION20261003-G438-induction-sync-20261003 -->
## Luna sync — G438 induction 반영·G439 frontier

- `G438-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,237 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G439 전체 cases `BIL, BIM, BIN`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BIL.json`, `BIM.json`, `BIN.json`이다.

<!-- luna-sync:SESSION20261003-G438-basic-sync-20261003 -->
## Luna sync — G438 BIJ/BIK 기본 4단계 반영·induction 대기

- BIJ·BIK의 blind·answer_check·independent_code·sdss_compare 총 8 raw를 기존 처리기로 반영했다. Queue=processed=6,236 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 398 groups·1,372 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BIJ67 독립 충분 근거 해석 미확정과 BIK26 포괄성 제한을 raw 그대로 보존한다. G438 induction 전 다음 group은 미열람·잠금 상태다.

<!-- luna-sync:SESSION20261003-BACKFILL129-BHY-sync-20261003 -->
## Luna sync — BHY depth backfill 반영·G438 frontier

- `BACKFILL129-BHY-depth_backfill-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,228 unique, pending=0, duplicate/orphan=0.
- 같은 1T라도 다른 임계 온도에서 측정된 자료이므로 코드 43은 부분 조건 확인으로 한정한다는 수정과 원 raw 의미를 보존한다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G438 전체 cases `BIJ, BIK`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BIJ.json`, `BIK.json`이다.

<!-- luna-sync:SESSION20261003-AUDIT129-sync-20261003 -->
## Luna sync — AUDIT129 반영·BHY depth backfill 잠금·G428~G437 구조 감사

- `AUDIT129-manual_parity_audit-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,227 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[BHY]`, `semantic_state_review=[]`.
- G428~G437 30 cases 실제 queue를 기계 감사했다: group-wide blind→answer_check→independent_code→sdss_compare barrier 위반 0, 경쟁 코드 2~4개 위반 0, 최초답-공식답 불일치 0, raw record_id 중복 0. 의미 검증이 아닌 구조 검증이다.
- BHY depth backfill raw 반영 전 다음 group 잠금 유지한다.

<!-- luna-sync:SESSION20261003-G437-META129-sync-20261003 -->
## Luna sync — G437 induction·META129 반영·AUDIT129 잠금

- `G437-induction-20261003-01` 및 `META129-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,226 unique, pending=0, duplicate/orphan=0.
- META129 필수 필드와 유보를 raw 그대로 보존했다. `meta_state.py`: 397 groups·1,370 cases, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 group은 `AUDIT129` raw 반영 전까지 잠금 유지한다. Luna는 의미 판단을 추가하거나 수정하지 않았다.

<!-- luna-sync:SESSION20261003-G437-basic-sync-20261003 -->
## Luna sync — G437 BIF/BIG/BIH/BII 기본 4단계 반영·induction/META129 대기

- BIF·BIG·BIH·BII의 blind·answer_check·independent_code·sdss_compare 총 16 raw를 기존 처리기로 반영했다. Queue=processed=6,224 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 397 groups·1,370 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BIG 잔여 청구액과 원 투자 손실의 구분을 raw 그대로 보존한다. G437 induction과 META129 전에는 다음 group으로 넘어가지 않는다.

<!-- luna-sync:SESSION20261003-G436-induction-sync-20261003 -->
## Luna sync — G436 induction 반영·G437 frontier

- `G436-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,208 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G437 전체 cases `BIF, BIG, BIH, BII`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BIF.json`, `BIG.json`, `BIH.json`, `BII.json`이다.

<!-- luna-sync:SESSION20261003-G436-basic-sync-20261003 -->
## Luna sync — G436 BIC/BID/BIE 기본 4단계 반영·induction 대기

- BIC·BID·BIE의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,207 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 396 groups·1,366 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BIC 유형·수정보 범위, BIE 가설 지정, BID 분모 0 한계를 raw 그대로 보존한다. G436 induction 전 다음 group은 미열람·잠금 상태다.

<!-- luna-sync:SESSION20261003-G435-induction-sync-20261003 -->
## Luna sync — G435 induction 반영·G436 frontier

- `G435-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,195 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G436 전체 cases `BIC, BID, BIE`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BIC.json`, `BID.json`, `BIE.json`이다.

<!-- luna-sync:SESSION20261003-G435-sourcehold-sync-20261003 -->
## Luna sync — G435 기본 stage·BIB source hold 반영·induction 대기

- BHZ·BIA·BIB 기본 12 raw와 `BIB-hold-source-20261003-01` 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,194 unique, pending=0, duplicate/orphan=0.
- BIB blind 전 발문·[A] 범위 복원으로 source hold는 해소됐지만 최초 hold 원장은 보존한다. BIA85 사이트 범위 미확정 및 BIB 수정안 제출 조건 유보도 raw 그대로 유지한다.
- `meta_state.py`: 395 groups·1,363 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G435 induction 전에는 다음 group을 열지 않는다. Luna는 의미 판단을 추가하거나 수정하지 않았다.

<!-- luna-sync:SESSION20261003-G434-META128-sync-20261003 -->
## Luna sync — G434 induction·META128 반영·G435 frontier

- `G434-induction-20261003-01` 및 `META128-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,181 unique, pending=0, duplicate/orphan=0.
- META128 필수 12필드와 유보를 raw 그대로 보존했다. `meta_state.py`: 394 groups·1,360 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G435 전체 cases `BHZ, BIA, BIB`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BHZ.json`, `BIA.json`, `BIB.json`이다.

<!-- luna-sync:SESSION20261003-G434-basic-sync-20261003 -->
## Luna sync — G434 BHW/BHX/BHY 기본 4단계 반영·induction/META128 대기

- BHW·BHX·BHY의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,179 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 394 groups·1,360 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BHW45/69 및 BHY 정규화 지표의 한계를 raw 그대로 보존한다. G434 induction과 META128 전에는 다음 group으로 넘어가지 않는다.

<!-- luna-sync:SESSION20261003-G433-induction-sync-20261003 -->
## Luna sync — G433 induction 반영·G434 frontier

- `G433-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,167 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G434 전체 cases `BHW, BHX, BHY`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BHW.json`, `BHX.json`, `BHY.json`이다.

<!-- luna-sync:SESSION20261003-G433-basic-sync-20261003 -->
## Luna sync — G433 BHT/BHU/BHV 기본 4단계 반영·induction 대기

- BHT·BHU·BHV의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,166 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 393 groups·1,357 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BHU80/93 유일 주 유보와 BHV 결합처리 효과·각 효과 분해 한계를 raw 그대로 보존한다. G433 induction 전에는 다음 group으로 넘어가지 않는다.

<!-- luna-sync:SESSION20261003-G432-induction-sync-20261003 -->
## Luna sync — G432 induction 반영·G433 frontier·G428~G432 구조 감사

- `G432-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,154 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G428~G432 14 cases의 실제 queue 순서를 기계 확인했다: blind→answer_check→independent_code→sdss_compare barrier 위반 0, 경쟁 코드 2~4개 위반 0, 최초답-공식답 불일치 0, raw record_id 중복 0. 이는 의미 판정 감사가 아니다.
- 다음 frontier는 G433 전체 cases `BHT, BHU, BHV`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BHT.json`, `BHU.json`, `BHV.json`이다.

<!-- luna-sync:SESSION20261003-G432-basic-sync-20261003 -->
## Luna sync — G432 BHQ/BHR/BHS 기본 4단계 반영·induction 대기

- BHQ·BHR·BHS의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,153 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 392 groups·1,354 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BHS [A] source restoration은 답 공개 후 SDSS 전 Astra 시각 확인으로 기록된 raw 의미를 보존하고, 최초 blind source limitation의 시간차도 유지한다. G432 induction 전에는 다음 group으로 넘어가지 않는다.

<!-- luna-sync:SESSION20261003-G431-META127-sync-20261003 -->
## Luna sync — G431 induction·META127 반영·G432 frontier

- `G431-induction-20261003-01` 및 `META127-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,141 unique, pending=0, duplicate/orphan=0.
- META127 필수 12필드와 모든 유보를 raw 그대로 보존했다. `meta_state.py`: 391 groups·1,351 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G432 전체 cases `BHQ, BHR, BHS`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BHQ.json`, `BHR.json`, `BHS.json`이다.

<!-- luna-sync:SESSION20261003-G431-basic-sync-20261003 -->
## Luna sync — G431 BHN/BHO/BHP 기본 4단계 반영·induction/META127 대기

- BHN·BHO·BHP의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,139 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 391 groups·1,351 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G431 induction과 META127이 미완료이므로 다음 group은 잠금 유지한다. Luna는 의미 판단을 추가하거나 수정하지 않았다.

<!-- luna-sync:SESSION20261003-G430-induction-sync-20261003 -->
## Luna sync — G430 induction 반영·G431 frontier

- `G430-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,127 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G431 전체 cases `BHN, BHO, BHP`이며 blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BHN.json`, `BHO.json`, `BHP.json`이다.

<!-- luna-sync:SESSION20261003-G430-basic-sync-20261003 -->
## Luna sync — G430 BHK/BHL/BHM 기본 4단계 반영·induction 대기

- BHK·BHL·BHM의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,126 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 390 groups·1,348 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 최초 `past_exposure=unknown` 및 strict blind 제외, BHK③·⑤와 BHM 인과 한계 유보를 raw 그대로 보존한다. G430 induction 전에는 다음 group으로 넘어가지 않는다.

<!-- luna-sync:SESSION20261003-G429-induction-sync-20261003 -->
## Luna sync — G429 induction 반영·G430 frontier

- `G429-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,114 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 actionable frontier는 G430이며 전체 group_case_ids는 `G430=[BHK, BHL, BHM]`이다. blind-only sources는 `data/기본기_연구/prepared_backlog/blind_sources/BHK.json`, `BHL.json`, `BHM.json`이다.

<!-- luna-sync:SESSION20261003-G429-basic-sync-20261003 -->
## Luna sync — G429 BHH/BHI/BHJ 기본 4단계 반영·induction 대기

- BHH·BHI·BHJ의 blind·answer_check·independent_code·sdss_compare 총 12 raw를 기존 처리기로 반영했다. Queue=processed=6,113 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 389 groups·1,345 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 현재 G429 induction이 미완료이므로 다음 group은 잠금 유지한다. 다음 actionable stage는 G429 induction이며, frontier group_case_ids 전체는 `G429=[BHH, BHI, BHJ]`이다. blind-only source는 `BHH.json`, `BHI.json`, `BHJ.json`이다.

<!-- luna-sync:SESSION20261003-BACKFILL126-BHG-sync-20261003 -->
## Luna sync — BHG depth backfill 반영·G429 frontier

- `BACKFILL126-BHG-depth_backfill-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,101 unique, pending=0, duplicate/orphan=0.
- BHG 후기 예선 0/9 및 본선 면적 판단은 추가 계산 관례에 따른 조건부 주장으로 제한한다. 원문 전허용 모형의 유일성은 미해결이며 최초 blind raw와 이 유보를 보존한다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 actionable frontier는 G429의 BHH이며 blind-only source는 `data/기본기_연구/prepared_backlog/blind_sources/BHH.json`이다. 부모가 다음 group blind를 이어갈 수 있다.

<!-- luna-sync:SESSION20261003-BACKFILL126-BHF-sync-20261003 -->
## Luna sync — BHF depth backfill 반영·BHG 보강 대기

- `BACKFILL126-BHF-depth_backfill-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,100 unique, pending=0, duplicate/orphan=0.
- BHF의 표현 범위 유보와 원 blind 보존을 raw 그대로 유지한다. `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[BHG]`, `semantic_state_review=[]`.
- BHG depth backfill 전까지 다음 group frontier는 잠금 유지한다. Luna는 의미 판단을 추가하거나 수정하지 않았다.

<!-- luna-sync:SESSION20261003-AUDIT126-sync-20261003 -->
## Luna sync — AUDIT126 반영·BHF/BHG depth backfill 잠금

- `AUDIT126-manual_parity_audit-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,099 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 388 groups·1,342 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[BHF, BHG]`, `semantic_state_review=[]`.
- 감사가 지정한 BHF·BHG depth backfill pending을 그대로 보존한다. 두 보강 raw sync 전까지 다음 group frontier는 잠금 유지한다. Luna는 의미 판단을 추가하거나 수정하지 않았다.

<!-- luna-sync:SESSION20261003-G428-META126-sync-20261003 -->
## Luna sync — G428 induction·META126 반영·AUDIT126 잠금

- `G428-induction-20261003-01` 및 `META126-meta_induction-20261003-01` raw 2건을 기존 처리기로 반영했다. Queue=processed=6,098 unique, pending=0, duplicate/orphan=0.
- META126 필수 필드는 raw 그대로 보존·반영했다. `meta_state.py`: 388 groups·1,342 cases, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 actionable stage는 `AUDIT126`이며, 감사 raw 저장·동기화 전까지 다음 group frontier는 잠금 유지한다. Luna는 의미 판단을 추가하거나 수정하지 않았다.

<!-- luna-sync:SESSION20261003-G428-basic-sync-20261003 -->
## Luna sync — G428 BHF/BHG 기본 4단계 반영·induction 대기

- BHF·BHG의 blind·answer_check·independent_code·sdss_compare 총 8 raw를 기존 처리기로 반영했다. Queue=processed=6,096 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 388 groups·1,342 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=7`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G428 전체 SDSS 단계까지 반영됐지만 induction은 아직 미완료다. 다음 actionable stage는 G428 induction이며, induction 전에는 다음 group으로 넘어가지 않는다. Astra raw 의미는 보존하고 Luna는 재판정하지 않았다.

<!-- luna-sync:SESSION20261003-G427-induction-sync-20261003 -->
## Luna sync — G427 induction 반영·G428 frontier

- `G427-induction-20261003-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,088 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 387 groups·1,340 cases, `completed_groups_since_last_meta=2`, `completed_questions_since_last_meta=5`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G427 induction의 경계·반례·생성 원칙과 미해결 항목은 Astra raw 의미 그대로 보존했으며 Luna는 재판정하지 않았다.
- 다음 actionable frontier는 G428의 BHF·BHG blind 단계다. blind-only source는 `data/기본기_연구/prepared_backlog/blind_sources/BHF.json` 및 `BHG.json`이며, 다음 group 답·태그·원문은 아직 공개하지 않는다.

<!-- luna-sync:SESSION20261003-G427-BHD-BHE-sync-20261003 -->
## Luna sync — G427 BHD/BHE 기본 stage 반영·induction 대기

- G427 BHD·BHE의 blind·answer_check·independent_code·sdss_compare 기본 raw 8건을 기존 처리기로 반영했다. Queue=processed=6,087 unique, pending=0, duplicate/orphan=0.
- `meta_state.py`: 387 groups·1,340 cases, `completed_groups_since_last_meta=2`, `completed_questions_since_last_meta=5`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BHD29 사이트 국소 범위 미확정 및 BHE78/10 유일 주 유보를 raw 의미 그대로 유지한다. G427 induction은 Astra 수행 대기이며 완료로 추론하지 않는다.
- 다음 단계는 G427 induction raw 반영이다. 이후 frontier는 다음 Excel-style case ID BHF이며, induction 전에는 새 group blind로 넘어가지 않는다.

<!-- luna-sync:SESSION20261002-G427-frontier-20261002 -->
## Luna sync — G426 induction 반영·G427 BHD/BHE blind frontier

- `G426-induction-20261002-r5-01` raw 1건을 기존 처리기로 반영했다. Queue=processed=6,079 unique, pending=0, duplicate/orphan=0.
- G426의 SDSS 대조와 induction raw 반영이 끝났다. Astra raw 의미는 보존했으며 Luna는 재판정하지 않았다.
- `meta_state.py`: 386 groups·1,338 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Manifest prepared 333건(hold 포함). 다음 frontier는 G427의 BHD·BHE blind이며, blind-only source부터 시작한다.

<!-- luna-sync:SESSION20261002-G426-sdss-sync-20261002 -->
## Luna sync — G426 SDSS 대조 3건 반영·induction 대기

- BHA·BHB·BHC `sdss_compare` raw 3건을 기존 처리기로 반영했다. Queue=processed=6,078 unique, pending=0, duplicate/orphan=0.
- 세 case의 group-wide independent-code barrier 이후 SDSS 공개·대조가 저장되었다. G426 induction은 Astra 판단 대기이며, Luna가 완료로 추론하지 않는다.
- `meta_state.py`: 기계 요약상 완료 386 groups·1,338 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Manifest prepared 333건(hold 포함), 다음 Excel-style case ID BHD. G426 induction raw 반영 전에는 새 group blind로 넘어가지 않는다.

<!-- luna-sync:SESSION20261002-G426-partial-sync-20261002 -->
## Luna sync — G426 group blind·answer·independent 반영, SDSS 대기

- BHA·BHB·BHC의 미처리 raw 9건을 기존 처리기로 반영했다. Queue=processed=6,075 unique, pending=0, duplicate=0, orphan=0. 각 문항의 blind·answer_check·independent_code가 기록됐으며 group 전체 독립 판정 뒤 SDSS 공개 barrier는 충족했다. 아직 `sdss_compare` 및 G426 induction raw가 없어 group 완료로 세지 않는다.
- 세 최초 답은 ③·⑤·②로 공식 답과 일치한다. blind 기록의 `past_exposure=unknown`, `strict_blind_eligible=false`를 그대로 보존하며 엄격 blind 성과로 산입하지 않는다. blind packet 경로는 모두 존재하고 `blind_only=true`, `source_role=anonymous_blind_source`; 답·태그·기존 판정은 패킷에 없다.
- meta_state 동기화: 완료 385 groups·1,335 cases, `meta_due=false`, `manual_parity_audit_due=false`, depth backfill=[], semantic review=[]. Manifest prepared 333건(기존 hold 행 포함), 잔량 30 미만이 아니므로 후보 준비는 불필요하다.
- **현재 잠금 frontier:** G426의 SDSS 공개·대조 단계. 세 independent_code raw가 모두 저장됐으므로 Astra가 group 전체 barrier를 재확인한 뒤에만 sealed SDSS를 공개한다. 이어 G426 induction 필요 여부/기록은 Astra 판단을 기다린다.
- **다음 Excel-style case ID:** BHD. G426의 SDSS 대조와 induction 처리 전에는 새 group blind로 넘어가지 않는다. 코드 판정과 유보는 queue raw 그대로 유지한다.

<!-- luna-sync:SESSION20261002-G425-final-sync-20261002 -->
## Luna sync — G425 전체 반영·META125 완료·G426 미열람 frontier

- G425 BGX·BGY·BGZ 기본 12 raw, G425 induction 및 META125를 기존 처리기로 반영했다. Queue=processed=6,066 unique, pending=0.
- `meta_state.py`: 완료 385 groups·1,335 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BGU/BGS 및 BGZ19 유보, BGW/BGY 답 공개 전 blind 부록 복원 지위를 원기록대로 보존한다. 다음 frontier G426은 미열람·미노출이다.

<!-- luna-sync:SESSION20261002-G424-final-sync-20261002 -->
## Luna sync — G424 전체 반영·induction 완료·G425 미열람 frontier

- G424 BGU·BGV·BGW 기본 12 raw, BGW source hold 1건, induction 1건을 기존 처리기로 반영했다. Queue=processed=6,052 unique, pending=0.
- 세 case의 blind·answer_check·independent_code·sdss_compare coverage와 실제 queue 순서 barrier를 확인했다. BGW source hold는 blind 이전의 immutable hold로 보존한다.
- BGU②의 빈도·협화 정도 및 ⑤의 유일 복원, 사이트 85 범위는 미해결 유보를 유지한다. 다음 frontier G425는 미열람·미노출이다.

<!-- luna-sync:SESSION20261002-G423-induction-sync-20261002 -->
## Luna sync — G423 전체 반영·induction 완료·G424 미열람 frontier

- G423 BGR·BGS·BGT의 12 raw와 G423 induction 1 raw를 기존 처리기로 기계 반영했다. Queue=processed=6,038 unique, pending=0.
- 세 case 모두 4단계 coverage를 충족했고, 실제 queue 순서의 group barrier 위반은 0건이다. 최초답은 BGR③·BGS①·BGT②로 공식 답과 모두 일치한다.
- G423 induction 반영이 완료됐다. 다음 frontier G424는 미열람·미노출로 잠금 해제한다.

<!-- luna-sync:SESSION20261002-G411-G422-hold-20261002 -->
## Luna sync — G411~G422 완료·hold 인계·G423 미열람

- `SESSION20261002-G411-G422-hold-20261002-r3-01`까지 반영했다. Queue=processed=6,025 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 382 groups·1,326 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G411~G422 12 groups·33 cases, 132 stage raw의 queue 줄 인덱스 barrier·답 일치·blind `exact_error`·경쟁 코드 2~4개·raw ID 중복을 기계 검증했고 오류 0건이다. 이는 의미 판정 전수감사가 아니다.
- hold 사유는 응답예산 인계이며 quota unavailable이다. 실제 quota 경고·임계 관측은 없고 연구 완료가 아니다. 다음 frontier G423은 미열람·미노출이다.

<!-- luna-sync:SESSION20261002-G422-META124-20261002 -->

- G422 BGO·BGP·BGQ의 기본 12 stage, induction 1건, META124 1건을 기존 처리기로 반영했다. Queue=processed=6,024 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 382 groups·1,326 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BGO4③ 국소 오답, BGP19 본문 구조, BGQ12 조건부 포섭 범위를 보존한다. 다음 frontier G423은 미열람·미노출 상태로 잠금 해제한다.
- G411~G422 33 case·132 stage raw의 구조 검증은 오류 0건이며 의미 판정 전수감사가 아니다.

<!-- luna-sync:SESSION20261002-G421-20261002 -->

- G421 BGM·BGN의 기본 8 stage와 induction 1건, 총 9 raw를 기존 처리기로 반영했다. Queue=processed=6,010 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BGM95는 국소 전제의 범위 유보, BGN42는 개별 기업을 경계 기준으로 보존한다. 다음 frontier G422는 미열람·미노출 상태로 잠금 해제한다.

<!-- luna-sync:SESSION20261002-G420-20261002 -->
## Luna sync — G420 완료·G421 미열람 frontier 해제

- G420 BGJ·BGK·BGL의 기본 12 stage와 induction 1건, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=6,001 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BGJ2/54 국소 중첩, BGK95 지문 범위 유보, BGL20 대안 수단과 정당화 기여 조건을 보존한다. G421은 미열람·미노출 상태로 잠금 해제한다.
- G411~G420 28 case, 112 stage raw의 실제 queue 줄 인덱스 barrier·최초답/공식답·blind `exact_error`·경쟁 코드 2~4개·raw ID 중복을 기계 검증했고 오류 0건이다. 이는 의미 판정 전수감사가 아니다.

<!-- luna-sync:SESSION20261002-G419-META123-AUDIT123-BFQ-BGA-20261002 -->
## Luna sync — AUDIT123 backfill 완료·G420 미열람 frontier 해제

- BACKFILL123-BGA raw 1건을 기존 처리기로 반영했다. Queue=processed=5,988 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G411~G419 25 case의 실제 queue 줄 인덱스 stage barrier를 기계 검증했다. 각 case의 blind·answer_check·independent_code·sdss_compare 4단계, 최초답-공식답 일치, blind `exact_error`, 경쟁 코드 2~4개, raw ID 중복을 확인했고 오류 0건이다. 이는 의미 판정 전수감사가 아니다.
- AUDIT123의 BFQ·BGA 두 보강 대상이 모두 해소되었다. 다음 frontier G420은 미열람·미노출 상태로 잠금 해제한다.

<!-- luna-sync:SESSION20261002-G419-META123-AUDIT123-BFQ-20261002 -->
## Luna sync — BFQ backfill 완료·BGA backfill 대기·G420 잠금

- BACKFILL123-BFQ raw 1건을 기존 처리기로 반영했다. Queue=processed=5,987 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[BGA]`, `semantic_state_review=[]`.
- AUDIT123의 두 보강 대상 중 BFQ는 해소되었고 BGA만 남았다. BGA 보강 완료 전 G420은 잠금 유지한다.

<!-- luna-sync:SESSION20261002-G419-META123-AUDIT123-20261002 -->
## Luna sync — AUDIT123 완료·BFQ/BGA depth backfill 대기·G420 잠금

- AUDIT123 raw 1건을 기존 처리기로 반영했다. Queue=processed=5,986 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[BFQ, BGA]`, `semantic_state_review=[]`.
- 감사에서 지정한 BFQ·BGA 두 보강 대상을 그대로 보존한다. 부모의 depth backfill 완료 전 G420은 잠금 유지한다.

<!-- luna-sync:SESSION20261002-G419-META123-20261002 -->
## Luna sync — G419·META123 완료·AUDIT123 대기·G420 잠금

- G419 BGH·BGI·BGJ의 기본 12 stage, induction 1건, META123 1건을 기존 처리기로 반영했다. Queue=processed=5,985 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 379 groups·1,318 cases, `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BGH24 합법적 예외와 운영 위반 구분, BGI 추론 강도 보존. AUDIT123은 부모 수행 대기이므로 G420은 잠금 유지한다.

<!-- luna-sync:SESSION20261002-G418-20261002 -->
## Luna sync — G418 완료·G419 미열람 frontier 해제

- G418 BGD·BGE·BGF의 기본 12 stage와 induction 1건, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,971 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 378 groups·1,315 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BGD③ 방법론적 비대칭 범위와 수식 전사 누락 한계, BGE 약화와 완전 반박의 구분, BGF37/69 국소 중첩을 유지한다. 다음 frontier G419는 미열람·미노출 상태로 잠금 해제한다.

<!-- luna-sync:SESSION20261002-G417-20261002 -->
## Luna sync — G417 완료·G418 미열람 frontier 해제

- G417 BGB·BGC의 기본 8 stage와 induction 1건, 총 9 raw를 기존 처리기로 반영했다. Queue=processed=5,958 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 377 groups·1,312 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BGC는 실제 위험의 인과와 위험 인지의 인과를 분리하고, BGB1 범위 유보를 유지한다. 다음 frontier G418은 미열람·미노출 상태로 잠금 해제한다.

<!-- luna-sync:SESSION20261002-G416-META122-20261002 -->
## Luna sync — G416·META122 완료·G417 미열람 frontier 해제

- G416 BFY·BFZ·BGA의 기본 12 stage와 induction 1건, META122 1건을 기존 처리기로 반영했다. Queue=processed=5,949 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 376 groups·1,310 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BGA19는 독학 성취가 능력부족 연결을 반증하는 강한 보조라는 raw 의미를 보존하고, BFY61 범위 유보를 유지한다. 다음 frontier G417은 미열람·미노출 상태로 잠금 해제한다.

<!-- luna-sync:SESSION20261002-G415-20261002 -->
## Luna sync — G415 완료·G416 미열람 frontier 해제

- G415 BFV·BFW·BFX의 기본 12 stage와 induction 1건, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,935 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 375 groups·1,307 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BFX 공식 선지·시각자료 매핑은 사후 provenance 확인으로 보존하며 최초 blind 번호를 소급 승격하지 않는다. 구조는 `((A,D),C),B`로 기록하고, 다음 frontier G416은 미열람·미노출 상태로 잠금 해제한다.

<!-- luna-sync:SESSION20261002-G414-20261002 -->
## Luna sync — G414 완료·G415 미열람 frontier 해제

- G414 BFT·BFU의 기본 8 stage와 induction 1건, 총 9 raw를 기존 처리기로 반영했다. Queue=processed=5,922 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 374 groups·1,304 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BFT17/98은 국소 중첩을 보존하고, BFU8/12는 같은 규칙의 구체·포괄 기술로서 별도 필수행동 중복계수하지 않는다. 다음 frontier G415는 미열람·미노출 상태로 잠금 해제한다.

<!-- luna-sync:SESSION20261002-G413-META121-20261002 -->
## Luna sync — G413·META121 완료·G414 미열람 frontier 해제

- G413 BFQ·BFR·BFS의 기본 12 stage, induction 1건, META121 1건을 기존 처리기로 반영했다. Queue=processed=5,913 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 373 groups·1,302 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G413 세 case의 blind·answer_check·independent_code·sdss_compare stage barrier와 induction을 충족했다. BFQ⑤ 부합 해석, BFS 증거힘의 가산성·기준시점, 92/63 유일 주 우선 제한 유보를 유지한다.
- G413 induction의 결합확률 반모형은 논리 검사용이며 실제 사례 추정이 아니다. 다음 frontier G414는 미열람·미노출 상태로 잠금 해제한다.

<!-- luna-sync:SESSION20261002-G412-20261002 -->
## Luna sync — G412 완료·G413 미열람 frontier 해제

- G412 BFN·BFO·BFP의 기본 12 stage와 induction 1건, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,899 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 372 groups·1,299 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G412의 세 case는 blind·answer_check·independent_code·sdss_compare 각 1건 및 induction 1건으로 stage barrier를 충족했다. BFP20 정확범위·③ 제소/실체 성립 구별, BFN26 완전배타 일반화 금지 유보를 유지한다.
- 기존 raw 의미를 보존하며 다음 frontier G413은 미열람·미노출 상태로 잠금 해제한다.

<!-- luna-sync:SESSION20261002-G411-20261002 -->
## Luna sync — G411 완료·G412 미열람 frontier 해제

- G411 BFK·BFL·BFM의 기본 12 stage와 induction 1건, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,886 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 371 groups·1,296 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G411의 세 case는 blind 3·answer_check 3·independent_code 3·sdss_compare 3 및 induction 1건으로 stage barrier를 충족했다. 공식 정답 원 HWP 정답표 독립 시각 대조는 미실시 한계를 유지한다.
- BFM② 장소 범위 유보, strictblind unknown 제외 및 기존 raw 의미 보존을 유지한다. 다음 frontier G412는 미열람·미노출 상태로 잠금 해제한다.

<!-- luna-sync:SESSION20261002-hold-G399-G410-20261002 -->
## 최신 세션 인계 — 최종 hold 반영·G411 잠금 해제

- BACKFILL120-BFJ 및 최종 hold raw 등 추가 2 raw를 반영했다. Queue=processed=5,873 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BEM·BFJ depth backfill이 모두 완료되어 다음 frontier G411은 미열람·미노출 상태로 잠금 해제한다. BEM 문맥 동일률 해석 유보는 유지한다.
- G399~G410 36 cases 최종 기계 검증: 최초답=공식답 36/36, `exact_error` 누락 0, record_id 중복 0, 실제 queue 줄 인덱스 stage barrier 위반 group 0.

<!-- luna-sync:SESSION20261002-G385-G398-context-01 -->
## 이전 세션 인계 — G399 미열람 당시

- Hold raw `SESSION20261002-hold-G385-G398-context-01`까지 반영: Queue=processed=5,704 unique, pending=0. 인계 사유는 응답·컨텍스트 예산이며 quota 조회는 unavailable, runtime quota emergency는 관측되지 않았다.
- G385~G398은 14 groups·42 case 기록이다. 기계 검증에서 모든 case가 blind/answer_check/independent_code/sdss_compare 각 1건, group stage barrier 14/14 통과, 최초답-공식답 불일치 0, 최초답=매력 오답 0, exact_error 누락 0. 이 수치는 case 기록 수이며 고유 원문 전수 중복검증을 뜻하지 않는다.
- BDV는 MEET-2012-Q12, 기존 핵심8코드 기준 9장 F와 동일한 기노출 사례이므로 신규 고유 문항 및 strict-blind 성과로 세지 않는다. 나머지도 과거 노출 unknown인 경우 strict-blind 성과 확정에서 제외한다.
- BCT: ‘억압의 필연적 경로’ 설명은 원문의 가능성을 과강화한 오류로 철회. 최초 blind와 답⑤는 보존하며 ㄷ의 연역 타당성·공식답 유일성은 미해결. BDN: 전신 되먹임의 순효과·공식답 유일성 미해결. BDM⑤ 정량 방향 유보, BCP 기능 확장 한계·BDB 20 필수성·BDF 12 범위 미확정도 유지. 반모형은 논리 검사용이며 실제 생물 모형·치료 지침이 아니다.
- G398 BDX/BDY/BDZ는 후보 색인에 등재됐지만 matched_case_id=null이며 기존 연구 case 중복으로 확정하지 않는다.
- META116 완료; `meta_due=false`, `manual_parity_audit_due=false`, depth backfill=[], semantic_state_review=[]. Hold 처리 원장에는 `needs_astra_review`(미완료/hold 보존)로 남고, meta_state의 semantic_state_review에는 포함되지 않았다.
- 다음 frontier G399는 미열람·미노출이며 잠금 해제. 새 세션에서 AGENTS/CURRENT/ASTRA_START, meta_state/quota/pending을 점검한 뒤 G399 blind부터 시작한다.

<!-- luna-sync:G398-META116-20261002 -->
## Luna sync — G398·META116 완료·G399 미열람·잠금 해제

- G398 induction 1건과 META116 meta_induction 1건, 총 2 raw를 기존 처리기로 반영했다. Queue=processed=5,703 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 358 groups·1,257 cases, META116 이후 0 groups·0 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G398 및 META116 완료. G399 잠금을 해제하며 다음 frontier G399는 미열람·미노출이다.
- BDV는 기존 핵심8코드 기준 9장 F 중복이며 provenance MEET-2012-Q12로 확인된 기노출 사례다. 최초 unknown 기록과 strictblind 제외를 유지하고 신규 고유문항 수에 더하지 않는다. G398 BDX·BDY·BDZ는 후보 색인 등록만 확인됐고 matched_case_id가 없어 기존 연구 중복으로 확정하지 않는다.
- 기존 의미 유보 유지: BCTㄷ 공식답 유일성, BCP 기능 확장 한계, BDB 20 필수성, BDF 12 범위, BDN 전신 되먹임 순효과·유일성, BDM⑤ 정량 방향.

<!-- luna-sync:G398-sync-20261002 -->
## Luna sync — G398 stage 반영·META116 선행·G399 잠금

- G397 induction 1건과 G398 기본 12 stage, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,701 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 358 groups·1,257 cases, META115 이후 3 groups·9 cases; `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G398 induction 및 META116은 미완료다. META116을 먼저 완료할 때까지 G399를 잠근다.
- G398의 BDX·BDY·BDZ 원문 ID는 기존 후보 색인에 등록돼 있으나 `matched_case_id=null`이므로 이미 연구된 case로 확정하지 않는다. BDV는 provenance MEET-2012-Q12로 확인된 기존 핵심8코드 기준 9장 F와 중복으로 확정하며, 신규 고유 문항 수에 더하지 않는다.
- 기존 의미 유보 유지: BCTㄷ 공식답 유일성, BCP 기능 확장 한계, BDB 20 필수성, BDF 12 범위, BDN 전신 되먹임 순효과·유일성, BDM⑤ 정량 방향.

<!-- luna-sync:G397-sync-20261002 -->
## Luna sync — G397 stage 반영·BDV provenance 정정·G398 미열람

- G396 induction 1건과 G397 기본 12 stage, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,687 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 357 groups·1,254 cases, META115 이후 2 groups·6 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G397 induction은 미완료다. 다음 frontier G398은 미열람·미노출이다.
- BDV provenance는 공개 후 MEET-2012-Q12로 확인됐다. 현재 세션에서 읽은 핵심 8코드 기준 9장의 기존 F와 동일 문항으로 처리한다. 최초 `unknown` 기록은 보존하되 strict blind 자격은 false이며, 신규 고유 문항 수에 더하지 않고 기존 연구 중복으로 표시한다. case 수와 고유 원문 수를 혼동하지 않는다.
- 기존 미해결 유지: BCTㄷ 공식답 유일성, BCP 기능 확장 한계, BDB 20 필수성, BDF 12 범위, BDN 전신 되먹임 순효과·유일성, BDM⑤ 정량 방향.

<!-- luna-sync:G396-sync-20261002 -->
## Luna sync — G396 stage 반영·G396 induction 미완료·G397 미열람

- G396(BDR·BDS·BDT) 기본 12 stage raw를 기존 처리기로 반영했다. Queue=processed=5,674 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 356 groups·1,251 cases, META115 이후 1 group·3 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G396 induction은 미완료다. 다음 frontier G397은 미열람·미노출이다.
- 기존 미해결 유지: BCTㄷ 공식답 유일성, BCP 기능 확장 한계, BDB 20 필수성, BDF 12 범위, BDN 전신 되먹임 순효과·유일성, BDM⑤ 정량 방향.

<!-- luna-sync:G395-META115-20261002 -->
## Luna sync — G395·META115 완료·G396 미열람·잠금 해제

- G395 induction 1건과 META115 meta_induction 1건, 총 2 raw를 기존 처리기로 반영했다. Queue=processed=5,662 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 355 groups·1,248 cases, META115 이후 0 groups·0 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G395 및 META115 완료. G396 잠금을 해제하며 다음 frontier G396은 미열람·미노출이다.
- BDN 전신 되먹임 순효과·공식답 유일성은 미해결로 유지하고, BDM⑤ 정량 방향 해석도 유보한다.

<!-- luna-sync:G395-sync-20261002 -->
## Luna sync — G395 stage 반영·META115 선행·G396 잠금

- G394 induction 1건과 G395(BDO·BDP·BDQ) 기본 12 stage, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,660 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 355 groups·1,248 cases, META114 이후 3 groups·9 cases; `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G395 induction 및 META115는 미완료다. META115를 먼저 완료할 때까지 G396을 잠근다.
- G394 반모형은 논리 검사용이며 실제 생물 모형이 아니다. BDN·BDM 관련 기존 유보를 유지한다.

<!-- luna-sync:G394-sync-20261002 -->
## Luna sync — G394 stage 반영·G394 induction 미완료·G395 미열람

- G393 induction 1건과 G394(BDL·BDM·BDN) 기본 12 stage, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,647 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 354 groups·1,245 cases, META114 이후 2 groups·6 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G394 induction은 미완료다. 다음 frontier G395는 미열람·미노출이다.
- BDN은 최초답 ③과 공식답 ③이 일치한다. 전신 되먹임의 순효과와 답의 유일성은 미해결이며, 치료 지침으로 확대하지 않는다. 기존 BCTㄷ·BCP·BDB·BDF 유보도 유지한다.

<!-- luna-sync:G393-sync-20261002 -->
## Luna sync — G393 stage 반영·G393 induction 미완료·G394 미열람

- G393(BDI·BDJ·BDK) 기본 12 stage raw를 기존 처리기로 반영했다. Queue=processed=5,634 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 353 groups·1,242 cases, META114 이후 1 group·3 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G393 induction은 미완료다. 다음 frontier G394는 미열람·미노출이다.
- 기존 의미 유보 유지: BCTㄷ 공식답 유일성 미해결, BCP 기능 확장 한계 미확정, BDB 20 필수성 미확정, BDF 12 범위 미확정.

<!-- luna-sync:BACKFILL114-BDF-20261002 -->
## Luna sync — BACKFILL114 완료·G393 frontier 해제

- BACKFILL114 depth_backfill raw 1건(BDF)을 기존 처리기로 반영했다. Queue=processed=5,622 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- BACKFILL114 지정 backfill이 모두 반영되어 G393 잠금을 해제한다. 다음 frontier G393은 미열람·미노출이다.
- 의미 유보는 그대로 유지: BCTㄷ 공식답 유일성 미해결, BCP 기능 확장 한계 미확정, BDB 20 필수성 미확정, BDF 12 범위 미확정.

<!-- luna-sync:BACKFILL114-BDB-20261002 -->
## Luna sync — BDB backfill 반영·G393 잠금 유지

- BACKFILL114 depth_backfill raw 1건(BDB)을 기존 처리기로 반영했다. Queue=processed=5,621 unique, pending=0, duplicate=0, orphan=0.
- BDB의 20 복수성을 삭제해도 연결 보완은 성립하지만, 그것만으로 20의 필수성이 확정되지는 않는다는 raw의 한정을 보존한다.
- `meta_state.py`: `manual_parity_audit_due=false`, `depth_backfill_pending=["BDF"]`, `semantic_state_review=[]`. BDF 반영 전까지 G393 잠금을 유지한다.

<!-- luna-sync:BACKFILL114-BCT-20261002 -->
## Luna sync — BCT 후속 정정 반영·G393 잠금 유지

- BACKFILL114 depth_backfill raw 1건(BCT)을 기존 처리기로 반영했다. Queue=processed=5,620 unique, pending=0, duplicate=0, orphan=0.
- BCT의 최초 blind raw와 최초 답 ⑤는 보존한다. 후속 정정으로, 최초 blind의 ‘억압의 필연적 경로’는 원문의 ‘초래할 수 있다’를 과강화한 표현임을 철회한다.
- BCTㄷ의 연역적 타당성과 공식답 유일성은 미해결로 유지한다.
- `meta_state.py`: `manual_parity_audit_due=false`, `depth_backfill_pending=["BDB", "BDF"]`, `semantic_state_review=[]`. 남은 backfill 반영 전까지 G393을 잠근다.

<!-- luna-sync:BACKFILL114-BCP-20261002 -->
## Luna sync — BCP backfill 반영·G393 잠금 유지

- BACKFILL114 depth_backfill raw 1건(BCP)을 기존 처리기로 반영했다. Queue=processed=5,619 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `manual_parity_audit_due=false`, `depth_backfill_pending=["BCT", "BDB", "BDF"]`, `semantic_state_review=[]`.
- BCP 지정 대응표 보강을 반영했다. BCPㄱ의 엄격 범주 확장 여부는 해결된 것으로 처리하지 않는다. 남은 backfill 반영 전까지 G393 잠금을 유지한다.

<!-- luna-sync:AUDIT114-20261002 -->
## Luna sync — AUDIT114 반영·depth backfill 선행·G393 잠금

- AUDIT114 raw 1건을 기존 처리기로 반영했다. Queue=processed=5,618 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `manual_parity_audit_due=false`, `depth_backfill_pending=["BCP", "BCT", "BDB", "BDF"]`, `semantic_state_review=[]`.
- 지정된 depth_backfill raw 4건을 반영할 때까지 G393 잠금을 유지한다.

<!-- luna-sync:G392-META114-20261002 -->
## Luna sync — G392·META114 완료·AUDIT114 선행·G393 잠금

- G392 induction 1건과 META114 meta_induction 1건, 총 2 raw를 기존 처리기로 반영했다. Queue=processed=5,617 unique, pending=0, duplicate=0, orphan=0. Raw 문자열은 수정 없이 보존했다.
- `meta_state.py`: 완료 352 groups·1,239 cases, META114 이후 0 groups·0 cases; `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 단계는 Astra의 AUDIT114이며, audit에서 지정될 경우 필요한 depth_backfill까지 반영한 뒤 G393을 시작한다.

<!-- luna-sync:G392-sync-20261002 -->
## Luna sync — G392 stage 반영·META114 선행·G393 잠금

- G391 induction 1건과 G392(BDG·BDH) 기본 8 stage, 총 9 raw를 기존 처리기로 반영했다. Queue=processed=5,615 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 352 groups·1,239 cases, META113 이후 3 groups·8 cases; `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G392 induction 및 META114는 미완료다. META114를 먼저 완료할 때까지 G393을 잠근다. 개별 시험번호는 이 동기화에서 기록하지 않는다.

<!-- luna-sync:G391-sync-20261002 -->
## Luna sync — G391 stage 반영·G391 induction 미완료·G392 미열람

- G390 induction 1건과 G391(BDD·BDE·BDF) 기본 12 stage, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,606 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 351 groups·1,237 cases, META113 이후 2 groups·6 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G391 induction은 미완료다. 다음 frontier G392는 미열람·미노출이다.

<!-- luna-sync:G390-sync-20261002 -->
## Luna sync — G390 stage 반영·G390 induction 미완료·G391 미열람

- G390(BDA·BDB·BDC) 기본 12 stage raw를 기존 처리기로 반영했다. Queue=processed=5,593 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 350 groups·1,234 cases, META113 이후 1 group·3 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G390 induction은 미완료다. 다음 frontier G391은 미열람·미노출이다.

<!-- luna-sync:G389-META113-20261002 -->
## Luna sync — G389·META113 완료·G390 미열람

- G389 induction 1건과 META113 meta_induction 1건, 총 2 raw를 기존 처리기로 반영했다. Queue=processed=5,581 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 349 groups·1,231 cases, META113 이후 0 groups·0 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G389 및 META113 단계 완료. 다음 frontier G390은 미열람·미노출이다.

<!-- luna-sync:G389-sync-20261002 -->
## Luna sync — G389 stage 반영·META113 선행·G390 잠금

- G388 induction 1건과 G389 기본 12 stage, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,579 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 349 groups·1,231 cases, META112 이후 3 groups·9 cases; `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G389 induction 및 META113은 미완료다. META113을 먼저 마칠 때까지 G390을 잠근다.

<!-- luna-sync:G388-sync-20261002 -->
## Luna sync — G388 stage 반영·G388 induction 미완료·G389 미열람

- G387 induction 1건과 G388(BCU·BCV·BCW) 기본 12 stage, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,566 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 348 groups·1,228 cases, META112 이후 2 groups·6 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G388 induction은 미완료다. 다음 frontier G389은 미열람·미노출이다.

<!-- luna-sync:G387-sync-20261002 -->
## Luna sync — G387 stage 반영·G387 induction 미완료·G388 미열람

- G387( BCR·BCS·BCT ) 기본 12 stage raw를 기존 처리기로 반영했다. Queue=processed=5,553 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 347 groups·1,225 cases, META112 이후 1 group·3 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G387 induction은 미완료다. 다음 frontier G388은 미열람·미노출이다.

<!-- luna-sync:G386-META112-20261002 -->
## Luna sync — G386·META112 완료·G387 미열람

- G386 induction 1건과 META112 meta_induction 1건, 총 2 raw를 기존 처리기로 반영했다. Queue=processed=5,541 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 346 groups·1,222 cases, META112 이후 0 groups·0 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G386 및 META112 단계 완료. 다음 frontier G387은 미열람·미노출이다.

<!-- luna-sync:G386-sync-20261002 -->
## Luna sync — G386 stage 반영·META112 선행·G387 잠금

- G385 induction 1건과 G386(BCO·BCP·BCQ) 기본 12 stage, 총 13 raw를 기존 처리기로 반영했다. Queue=processed=5,539 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 346 groups·1,222 cases, META111 이후 3 groups·11 cases; `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G386 induction은 미완료다. META112가 due이므로 이를 먼저 완료할 때까지 G387을 잠근다.

<!-- luna-sync:G385-sync-20261002 -->
## Luna sync — G385 stage 반영·G386 미열람

- G385(BCK·BCL·BCM·BCN)의 blind/answer_check/independent_code/sdss_compare 16 raw를 기존 처리기로 반영했다. Queue=processed=5,526 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 345 groups·1,219 research cases, META111 이후 2 groups·8 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G385 induction은 미완료다. 다음 frontier G386은 미열람·미노출이며, G385 induction을 마치기 전 계속 연구하지 않는다.

<!-- luna-sync:SESSION20261002-G384-G385-context-handoff -->
## 최신 Luna sync — G384 완료·응답/컨텍스트 인계·G385 미열람

- G384 induction 및 `SESSION20261002-hold-G376-G384-context-01` raw까지 반영했다. Queue=processed=5,510 unique, pending=0, duplicate=0, orphan=0. 인계 사유는 응답·컨텍스트 예산이며 quota emergency가 아니다. raw의 `quota_status=unavailable`은 unavailable 그대로 보존한다.
- G376~G384 9 groups·28 cases 기계검증: 모든 group에서 blind 전체 → 최초 answer_check 전체 → independent_code 전체 → SDSS compare 전체 순서 통과, barrier/coverage 위반 0. 최초답 공식 일치 27/28(BCF만 불일치), 선택답=매력 오답 중복 0/28, `exact_error` 누락·공백 0/28.
- `meta_state.py`: 완료 344 groups·1,215 research cases, META111 이후 1 group·4 cases; `meta_due=false`, `manual_parity_audit_due=false`, depth backfill=[], semantic review=[].
- 다음 frontier G385는 미열람·미노출(blind source/공식답/SDSS/기존 판정 모두 false). 다음 단계는 새 Astra 세션에서 AGENTS/CURRENT/ASTRA_START 확인 후 meta_state/quota/pending 점검, 이어 G385 group blind다. 미완료 semantic stage 없음.
- BCF 최초답 실패와 ㄹ 배제·공식 정답 유일성 미해결, BBS 간접조건 유보는 그대로 유지하며 사후에 최초 기록을 덮어쓰지 않는다.

<!-- luna-sync:BACKFILL111-complete-G384-frontier-20261002 -->
## 최신 Luna sync — BACKFILL111 완료·G384 frontier 재개

- BACKFILL111 depth_backfill raw 1건(BBS·BCF)을 기존 처리기로 의미 변경 없이 반영했다. Queue=processed=5,492 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`. 지정 backfill이 모두 반영되어 G384 잠금을 해제한다. G384는 아직 미열람 frontier다.
- backfill 판단의 범위를 보존한다. 가상 반모형은 원문 밖 실제 과학사 사실이 아닌 논리 검사용이다. BCF는 지정 논거 보강을 완료했으나 ㄹ 배제 및 공식 정답 유일성은 미해결이다.
- G376~G383 신규 24 cases 기계 점검: 8 groups 모두 blind 3/3 → 최초 answer_check 3/3 → independent_code 3/3 → SDSS compare 3/3 순서 통과, coverage/barrier 위반 0. 최초 선택답과 공식 답은 23/24 일치(BCF만 불일치). 최초 선택답=매력 오답 중복 0/24, `exact_error` 누락·공백 0/24.
- BCF answer_check 보충02는 independent_code 뒤·SDSS compare 전에 기록된 별도 provenance 보충이며 원기록과 queue 위치를 그대로 유지했다.

<!-- luna-sync:BACKFILL111-partial-20261002 -->
## 최신 Luna sync — BACKFILL111 일부 반영·G384 잠금 유지

- BACKFILL111 depth_backfill raw 1건(BBJ·BCE)을 기존 처리기로 의미 변경 없이 반영했다. Queue=processed=5,491 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["BBS","BCF"]`, `semantic_state_review=[]`.
- raw의 가상 반모형은 원문 밖의 실제 과학사 사실이 아니라 논리 검사용이라는 범위를 그대로 보존한다. 나머지 BBS·BCF backfill 반영 전까지 G384는 잠근다.

<!-- luna-sync:AUDIT111-backfill-lock-20261002 -->
## 최신 Luna sync — AUDIT111 반영·depth backfill 선행·G384 잠금

- AUDIT111 manual_parity_audit raw 1건을 기존 처리기로 의미 변경 없이 반영했다. Queue=processed=5,490 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 343 groups·1,211 research cases; `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=["BBJ","BBS","BCE","BCF"]`, `semantic_state_review=[]`.
- AUDIT111은 지정 표본의 질적 parity 감사이며, stage barrier에 대한 기계 검증과 구분한다. 다음 Astra raw인 지정 depth_backfill 4건을 반영할 때까지 G384는 잠근다.
- META111 carryover의 `shared_structure` 원raw는 그대로 두고, 한국어 정정 표기 `shared_structure_ko` 지시를 별도 보존한다.

<!-- luna-sync:META111-AUDIT111-lock-20261002 -->
## 최신 Luna sync — META111 반영·AUDIT111 선행·G384 잠금

- G383 induction 및 META111 meta_induction raw 각 1건을 기존 처리기로 payload 의미 변경 없이 반영했다. Queue=processed=5,489 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 343 groups·1,211 research cases, META111 이후 0 groups·0 cases; `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- META111 carryover의 표기 정정 지시를 별도 보존한다: raw의 `shared_structure`는 변경하지 않고 한국어 정정 표기 `shared_structure_ko`를 적용 대상으로 기록한다.
- 다음 허용 작업은 Astra의 AUDIT111 및 audit에서 지시될 경우 필요한 depth_backfill raw 저장과 Luna sync다. 모두 반영할 때까지 G384는 잠근다.

<!-- luna-sync:G383-META111-lock-20261002 -->
## 최신 Luna sync — G383 stage 반영·META111 선행·G384 잠금

- G383(BCD·BCE·BCF)의 기본 12 stage raw와 BCF answer_check provenance 보충 1 raw를 기존 처리기로 의미 변경 없이 반영했다. Queue=processed=5,487 unique, pending=0, duplicate=0, orphan=0.
- 기계 stage 확인: blind 3건 → 최초 answer_check 3건 → independent_code 3건 → SDSS compare 3건 순서로 group barrier를 지켰다. BCF answer_check 보충02는 independent_code 이후, SDSS compare 전에 저장된 별도 후속 record로 순서를 그대로 보존한다.
- BCF는 최초 답 ③과 공식 답 ②의 불일치 및 ㄹ 배제 근거 미확정을 보존한다. 재검증 보충을 최초 blind 성과나 최초 판정에 소급하지 않는다.
- `meta_state.py`: 완료 343 groups·1,211 research cases, META110 이후 3 groups·9 cases; `meta_due=true`, `manual_parity_audit_due=false`(다음 parity audit까지 1 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음은 META111 raw 저장 후 상태를 재확인한다. 후속 AUDIT111 및 필요한 backfill 검토가 끝날 때까지 G384는 잠근다.

<!-- luna-sync:G382-G383-frontier-20261002 -->
## 최신 Luna sync — G382 완료·G383 frontier

- G382(BCA·BCB·BCC)의 blind·answer_check·independent_code·sdss_compare 12 raw와 induction 1 raw를 기존 처리기로 의미 변경 없이 반영했다. Queue=processed=5,474 unique, pending=0, duplicate=0, orphan=0.
- G382 stage coverage는 네 단계 각각 3/3이며 group barrier 위반 0건이다. BCB93/97의 소통/발화 의도 층위와 BCC100의 범위 유보를 구분해 보존한다.
- `meta_state.py`: 완료 342 groups·1,208 research cases, META110 이후 2 groups·6 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G383이며 아직 미열람이다. 연구를 이어간다.

<!-- luna-sync:G381-G382-frontier-20261002 -->
## 최신 Luna sync — G381 완료·G382 frontier

- G381(BBX·BBY·BBZ)의 blind·answer_check·independent_code·sdss_compare 12 raw와 induction 1 raw를 기존 처리기로 의미 변경 없이 반영했다. Queue=processed=5,461 unique, pending=0, duplicate=0, orphan=0.
- G381 stage coverage는 네 단계 각각 3/3이며 group barrier 위반 0건이다. BBY10의 사례요건 층위와 BBZ40의 부분/전체·17 단위 귀속 사후 후보는 서로 구분해 보존한다.
- `meta_state.py`: 완료 341 groups·1,205 research cases, META110 이후 1 group·3 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G382이며 아직 미열람이다. 연구를 이어간다.

<!-- luna-sync:META110-G381-frontier-20261002 -->
## 최신 Luna sync — META110 반영·G381 frontier 재개

- G380 induction 및 META110 meta_induction raw 각 1건을 기존 처리기로 payload 의미 변경 없이 반영했다. Queue=processed=5,448 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 340 groups·1,202 research cases, META110 이후 0 groups·0 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G381이며 아직 미열람이다. 연구를 이어간다.

<!-- luna-sync:G380-META110-lock-20261002 -->
## 최신 Luna sync — G380 stage 반영·META110 선행·G381 잠금

- G380(BBU·BBV·BBW)의 blind·answer_check·independent_code·sdss_compare 12 raw를 기존 처리기로 의미 변경 없이 반영했다. Queue=processed=5,446 unique, pending=0, duplicate=0, orphan=0.
- G380 stage coverage는 네 단계 각각 3/3이며, group barrier 위반 0건이다. BBW100 사후 후보와 최초 주 코드 44는 별개 기록으로 보존한다.
- `meta_state.py`: 완료 340 groups·1,202 research cases, META109 이후 3 groups·9 cases; `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 허용 작업은 Astra의 G380 induction 및 META110 raw 저장과 Luna sync다. 해당 raw 반영 전까지 다음 frontier G381은 잠근다.

<!-- luna-sync:G379-G380-frontier-20261002 -->
## 최신 Luna sync — G379 stage 반영·G380 frontier

- G379(BBR·BBS·BBT)의 blind·answer_check·independent_code·sdss_compare 12 raw와 G379 induction 1 raw를 기존 처리기로 의미 변경 없이 반영했다. Queue=processed=5,434 unique, pending=0, duplicate=0, orphan=0.
- G379 stage coverage는 네 단계 각각 3/3이며, group barrier 위반 0건이다. BBT10/37은 Astra raw가 기록한 국소 동일 연산 후보 범위로 보존하며 전역 통합으로 확대하지 않는다.
- `meta_state.py`: 완료 339 groups·1,199 research cases, META109 이후 2 groups·6 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G380이며 아직 미열람이다. 연구를 이어간다.

<!-- luna-sync:G378-complete-G379-frontier-20261002 -->
## 최신 Luna sync — G378 완료·G379 frontier

- G378(BBO·BBP·BBQ)의 blind·answer_check·independent_code·sdss_compare 12 raw와 G378 induction 1 raw를 기존 처리기로 의미 변경 없이 반영했다. Queue=processed=5,421 unique, pending=0, duplicate=0, orphan=0.
- 이번 세션의 G376~G378, 3 groups·9 cases stage coverage를 기계 검증했다. 각 group에서 blind 3/3 < answer_check 3/3 < independent_code 3/3 < SDSS compare 3/3이며 barrier 위반 0건이다. 이는 절차 검증이며 의미적 audit 생성은 아니다.
- `meta_state.py`: 완료 338 groups·1,196 research cases, META109 이후 1 group·3 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G379이며 아직 미열람이다. 연구를 이어간다.

<!-- luna-sync:META109-G378-frontier-20261002 -->
## 최신 Luna sync — META109 반영·G378 frontier 재개

- G377 induction 및 META109 meta_induction raw 각 1건을 기존 처리기로 payload 의미 변경 없이 반영했다. Queue=processed=5,408 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 337 groups·1,193 research cases, META109 이후 0 groups·0 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G378이며 아직 미열람이다. 연구를 이어간다.

<!-- luna-sync:G377-META109-lock-20261002 -->
## 최신 Luna sync — G377 완료·META109 선행·G378 잠금

- G377(BBL·BBM·BBN)의 blind·answer_check·independent_code·sdss_compare 12 raw를 기존 처리기로 의미 변경 없이 반영했다. Queue=processed=5,406 unique, pending=0, duplicate=0, orphan=0.
- 기계적 stage barrier 확인: 전체 blind 3건 < answer_check 3건 < independent_code 3건 < SDSS compare 3건; 위반 0건.
- `meta_state.py`: 완료 337 groups·1,193 research cases, META108 이후 3 groups·9 cases. `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 허용 작업은 Astra의 META109(및 관련 G377 induction) raw 저장과 Luna sync다. 해당 raw 반영 전까지 다음 frontier G378은 잠근다.

<!-- luna-sync:G376-complete-G377-frontier-20261002 -->
## 최신 Luna sync — G376 완료·G377 frontier

- G376(BBI·BBJ·BBK)의 blind·answer_check·independent_code·sdss_compare 12 raw와 G376 induction 1 raw를 기존 처리기로 의미 변경 없이 반영했다. Queue=processed=5,394 unique, pending=0, duplicate=0, orphan=0.
- 기계적 stage barrier 확인: 세 문항 전체 blind가 answer_check보다 앞서고, 전체 independent_code가 SDSS 공개보다 앞선다. 각 stage coverage 3/3이며 위반 0건.
- `meta_state.py`: 완료 336 groups·1,190 research cases, META108 이후 2 groups·6 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G376 induction 반영 완료. 다음 frontier는 G377이며 아직 미열람이다. 연구 전체는 완료되지 않았다.

<!-- luna-sync:SESSION-G366-G375-G376-frontier-20261001 -->
## 최신 Luna sync — G366~G375 마감·G376 미열람 frontier

- `SESSION20261001-hold-G366-G375-context-01`까지 반영했다. 응답·컨텍스트 예산 인계이며 quota emergency가 아니다. Queue=processed=5,381 unique, pending=0, duplicate=0, orphan=0.
- 이번 세션 완료 cohort는 G366~G369 및 G371~G375, 9 groups·28 cases다. G370 source-unavailable hold 4건은 완료 분모에서 제외했다. 네 stage coverage는 각각 28/28, group barrier 위반 0건. 최초답 공식 일치 28/28, blind/answer selected 불일치 0, 매력 오답=선택 답 중복 0, exact_error 누락 0.
- `meta_state.py`: 완료 335 groups·1,187 research cases, META108 이후 1 group·3 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Manifest 1,671 rows 중 prepared 484건. G024 DR~DU와 G370 BAP~BAS historical/source hold 8건은 준비 잔량에 포함되나 actionable에서 제외되어 actionable prepared는 476건이다. 다음 frontier는 manifest case ID BBI·BBJ·BBK인 G376이며, 원문은 미열람 상태다.
- 보존: G368 공식 source 복원 provenance와 strict-blind 제한; G370 source-unavailable hold; G372 BAW81 표면한정·BAX44 국소용법/주우선순위 유보 및 BACKFILL108; G373 100 태그 범위·BBB18 평가기준 유보; G375 공식도식 이미지 우선, source-quality issue와 최초 hold 원기록.

<!-- luna-sync:SESSION-G347-G364-G365-resume-20260928 -->
## 세션 인계 — G347~G364 sync 완료·G365 미열람

- `SESSION20260928-hold-20260928-context-handoff-01`까지 sync했다. 이번 인계는 응답·컨텍스트 예산에 따른 것이며 quota emergency는 아니다. Queue=processed=5,234 unique, pending0, duplicate/orphan0.
- G347~G364의 18 groups·56 cases를 queue 순서로 기계 검증했다. 각 semantic stage 56건씩 존재하며 all-group-blind-before-answer 및 all-group-independent-before-SDSS 위반 0, coverage 오류 0이다. 이 세션 56개 최초 선택 답은 56/56 공식 답과 일치한다.
- 누적 meta_state는 325 completed groups·1,156 research cases, META105 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`다. Research 누적 1,156과 사이트 전체 1,147은 다른 분모다.
- Manifest `prepared` 잔량 24건(기존 G024 hold 4건, actionable 20건). G365 첫 case ID는 AZZ이며 G365는 blind source·공식 답·SDSS·기존 판정 모두 미열람이다. 다음 재개는 새 세션에서 `AGENTS.md`/`CURRENT.md`/`ASTRA_START.md`를 읽고 meta_state·quota·pending을 확인한 뒤 G365 group blind다. 연구 전체는 완료되지 않았다.
- 보존: AYP/AZI 최초 오답 필드 오류 및 사후보충은 성과에 소급하지 않음, strict blind 미확정·AXH 및 AVE/ATK 실패, AXW/AYE/AZO 원 hold와 복원 후 별도 blind, G348 안테나 분수계수 전사 누락, 사이트 범위 미확정 및 G354 identifier typo의 META102 정정.


<!-- luna-sync:AUDIT105-AZW-backfill-lock-20260928 -->
## 현재 진행 상태 — AUDIT105 반영·AZW backfill 선행·G365 잠금

- `AUDIT105-manual_parity_audit-20260928-01` raw 1건을 기존 Luna 스크립트로 payload 의미 변경 없이 반영했다. Queue=processed=5,232 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 325 completed groups·1,156 cases, META105 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["AZW"]`, `semantic_state_review=[]`.
- 다음 허용 작업은 Astra의 AZW depth_backfill raw 저장 및 Luna sync다. 반영 전까지 G365는 잠근다.
- AYP·AZI 최초 오답 분석의 irreversible 품질 제한과 기존 사이트·코드 범위 유보, hold·exposure provenance를 유지한다.


<!-- luna-sync:META105-AUDIT105-lock-20260928 -->
## 현재 진행 상태 — META105 반영·AUDIT105 선행·G365 잠금

- META105와 G364 induction raw 각 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue=processed=5,231 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 325 completed groups·1,156 cases, META105 이후 0/0, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 허용 작업은 Astra의 AUDIT105 및 지정 depth_backfill raw 저장과 Luna sync다. 모두 반영하기 전까지 G365는 잠근다.
- 기존 사이트·코드 범위 유보, AYP·AZI 품질 제한, 이미지 provenance 및 hold·노출 제한을 유지한다.


<!-- luna-sync:G364-META105-lock-20260928 -->
## 현재 진행 상태 — G364 반영·META105 선행·G365 잠금

- G364 세 사례 전체 stage raw 12건과 G363 induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Astra 보고상 최초 답 ③·②·①은 공식 답과 일치한다.
- Queue=processed=5,229 unique, pending raw=0, duplicate/orphan 없음. `meta_state.py`: 325 completed groups·1,156 cases, META104 이후 3 groups·9 cases, `meta_due=true`, `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 허용 작업은 Astra의 G364 induction 및 META105 raw 저장과 Luna sync다. META105/AUDIT105 및 필요한 backfill 반영 전까지 G365는 잠근다.
- 사이트 범위 유보, AYP·AZI 품질 제한, AZC/AZS 판정 유보, 이미지 provenance 및 기존 hold·노출 제한은 그대로 유지한다.


<!-- luna-sync:G363-G364-frontier-20260928 -->
## 현재 진행 상태 — G363 반영·G364 frontier

- G363 세 사례 전체 stage raw 12건과 G362 induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Astra 보고상 최초 답 ⑤·①·⑤는 공식 답과 일치한다.
- Queue=processed=5,216 unique, pending raw=0, duplicate/orphan 없음. `meta_state.py`: 324 completed groups·1,153 cases, META104 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- Blind raw에 기록된 그림 3개 JPG 직접 확인 이력을 보존한다. 사이트 87은 공간 농도 그래프 범위 후보로만 두고, 기울기의 수치 계산으로 판단하지 않는 유보를 유지한다.
- 다음 frontier는 G364이며 G363 induction raw는 Astra 추가 대기다. AZS95 및 서로 다른 집계 분모 유보도 보존한다.


<!-- luna-sync:G362-G363-frontier-20260928 -->
## 현재 진행 상태 — G362 반영·G363 frontier

- G362 세 사례 전체 stage raw 12건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Astra 보고상 최초 답 ④·⑤·④는 공식 답과 일치한다.
- Queue=processed=5,203 unique, pending raw=0, duplicate/orphan 없음. `meta_state.py`: 323 completed groups·1,150 cases, META104 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- AZS95는 기준 필요성 후보와 특정 해결 방법의 유일 필요성을 구분해 유보한다. 이 구분과 기타 site/independent 차이는 raw 의미 그대로 유지한다.
- 다음 frontier는 G363이며 G362 induction raw는 Astra 추가 대기다. research cases와 사이트 전체의 분모 차이도 유지한다.


<!-- luna-sync:META104-G362-frontier-20260928 -->
## 현재 진행 상태 — META104 반영·G362 frontier

- G361 induction 및 META104 raw 각 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue=processed=5,191 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 322 completed groups·1,147 research cases, META104 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G362다. research cases 1,147과 사이트 전체 1,147은 분모와 범위가 서로 달라 같은 집계로 취급하지 않는다.
- AZO 원 source hold와 공식 강조구 보충 provenance, AYP·AZI 품질 제한, G348 전사 한계, 사이트 범위 유보 및 기존 노출 제한을 보존한다.


<!-- luna-sync:G361-META104-lock-20260928 -->
## 현재 진행 상태 — G361 반영·META104 선행·G362 잠금

- G361 AZO·AZM·AZN·AZP의 전체 stage raw 16건, AZO 원 source hold, G360 induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Astra 보고상 최초 답 ①·⑤·①·④는 공식 답과 일치한다.
- Queue=processed=5,189 unique, pending raw=0, duplicate/orphan 없음. AZO 원 hold는 별도 원기록으로 유지한다.
- `meta_state.py`: 322 completed groups·1,147 cases, META103 이후 3 groups·10 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 허용 작업은 Astra의 G361 induction 및 META104 raw 저장과 Luna sync다. 그 전까지 G362는 잠근다. AZO 복원 blind의 provenance는 공식 강조구 보충파일 범위로 유지하며, 기존 사이트 범위 유보·품질·노출 제한을 보존한다.


<!-- luna-sync:G360-G361-frontier-20260928 -->
## 현재 진행 상태 — G360 반영·G361 frontier

- G360 세 사례 전체 stage raw 12건과 G359 induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Astra 보고상 최초 답 ①·③·④는 공식 답과 일치한다.
- Queue=processed=5,171 unique, pending raw=0, duplicate/orphan 없음. `meta_state.py`: 321 completed groups·1,143 cases, META103 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 근거 범위는 신채호 논설의 문항 내 해석이며 외부 역사 사실 검증이 아니다. 사이트 범위 미확정도 raw대로 보존한다.
- 다음 frontier는 G361이며 G360 induction raw는 Astra 추가 대기다. AZI·AYP 최초 오답 분석 성과 제외 등 기존 품질 제한을 유지한다.


<!-- luna-sync:G359-G360-frontier-20260928 -->
## 현재 진행 상태 — G359 반영·G360 frontier

- G359 세 사례 전체 stage raw 12건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue=processed=5,158 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 320 completed groups·1,140 cases, META103 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 품질 제한: AZI blind의 매력 오답 번호 필드에 선택 답 ④가 잘못 기입되었고 answer_check에서 사후 보충했다. 선택 답 정확성은 별도로 보존하되, 최초 오답 분석 완비 성과에서는 제외한다. AYP의 동일한 성과 제외 제한도 유지하며 두 원blind는 수정하지 않는다.
- 다음 frontier는 G360이다. G359 induction raw는 Astra 추가 대기이며, 기타 사이트 범위 유보·hold·노출 제한을 보존한다.


<!-- luna-sync:META103-G359-frontier-20260928 -->
## 현재 진행 상태 — META103 반영·G359 frontier

- G358 induction 및 META103 raw 각 1건을 기존 Luna 스크립트로 payload 의미 변경 없이 반영했다. Queue=processed=5,146 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 319 completed groups·1,137 cases, META103 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G359다. 사례의 사이트 범위 미확정은 raw 그대로 유지한다. 기존 AYP 품질 제한·AXC/AZC 유보·hold 및 exposure provenance도 보존한다.


<!-- luna-sync:G358-META103-lock-20260928 -->
## 현재 진행 상태 — G358 반영·META103 선행·G359 잠금

- G358 세 사례의 전체 stage raw 12건과 G357 induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue=processed=5,144 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 319 completed groups·1,137 cases, META102 이후 3 groups·9 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 허용 작업은 Astra의 G358 induction 및 META103 raw 저장과 Luna sync다. 반영 전까지 G359는 잠근다.
- SDSS와 독립 판정 간 사이트 범위 미확정은 raw대로 유지한다. AZC 사이트19 범위 유보, AYP irreversible 품질 제한, TIFF 원본/노출 provenance 및 기존 hold를 보존한다.


<!-- luna-sync:G357-G358-frontier-20260928 -->
## 현재 진행 상태 — G357 반영·G358 frontier

- G357 세 사례의 전체 stage raw 12건과 G356 induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Astra 보고상 최초 답 ②·①·①은 공식 답과 일치한다.
- Queue=processed=5,131 unique, pending raw=0, duplicate/orphan 없음. `meta_state.py`: 318 completed groups·1,134 cases, META102 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G358이다. AZC의 사이트 19 범위 유보를 유지하며, G357 induction raw는 Astra 추가 대기다. 기존 source hold·노출·성과 제한도 보존한다.


<!-- luna-sync:G356-G357-frontier-20260928 -->
## 현재 진행 상태 — G356 반영·G357 frontier

- G356 세 사례 전체 stage raw 12건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Astra 보고상 최초 답 ③·④·④는 공식 답과 일치한다.
- Queue=processed=5,118 unique, pending raw=0, duplicate/orphan 없음. `meta_state.py`: 317 completed groups·1,131 cases, META102 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G356 blind raw에 기록된 대로 뷰어가 거부한 `G356_visual01.tif`의 RGB PNG 변환본 `G356_visual01.png`를 Astra가 직접 확인했다. 외부 source 열람은 없었으며 원 TIFF는 유지한다.
- 다음 frontier는 G357이다. G356 induction raw는 Astra 추가 대기다. AYP irreversible 품질 제한 및 기존 hold·노출 제한은 유지한다.


<!-- luna-sync:BACKFILL102-G356-frontier-20260928 -->
## 현재 진행 상태 — BACKFILL102 반영·G356 frontier

- `BACKFILL102-depth_backfill-20260928-01`을 기존 Luna 스크립트로 raw 의미 변경 없이 반영했다. Queue=processed=5,106 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 316 completed groups·1,128 cases, META102 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- AUDIT102가 지정한 AYQ·AYT backfill을 반영해 G356 잠금이 해제됐다. 다음 frontier는 G356이다.
- AYP 최초 오답 분석의 irreversible 품질 제한, G354 식별자 오기 정정 provenance, AYE source hold와 복원 blind 기록 등 기존 보존 조건을 유지한다.


<!-- luna-sync:AUDIT102-AYQ-AYT-backfill-lock-20260928 -->
## 현재 진행 상태 — AUDIT102 반영·AYQ/AYT backfill 선행·G356 잠금

- `AUDIT102-manual_parity_audit-20260928-01`을 기존 Luna 스크립트로 payload 의미 변경 없이 반영했다. Queue=processed=5,105 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 316 completed groups·1,128 cases, META102 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["AYQ", "AYT"]`, `semantic_state_review=[]`.
- 다음 허용 작업은 Astra의 AYQ·AYT depth_backfill raw 저장 및 Luna sync다. 이를 완료하기 전 G356은 잠근다. depth 판정·보충은 Astra가 수행한다.
- AYP 최초 오답 분석의 품질 제한은 irreversible로 유지한다. 원blind 및 G354 AYU/AXU 오기 정정 provenance도 원raw 불변으로 보존한다.


<!-- luna-sync:G355-META102-AUDIT102-lock-20260928 -->
## 현재 진행 상태 — G355 반영·META102/AUDIT102 선행·G356 잠금

- G355의 전체 stage raw 12건과 G354 induction raw 1건을 기존 Luna 스크립트로 payload 의미 변경 없이 반영했다. Queue=processed=5,102 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 316 completed groups·1,128 cases, META101 이후 3 groups·9 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음은 Astra의 META102와 AUDIT102, 필요한 depth_backfill raw 작성 및 Luna sync다. 해당 sync 완료 전 G356은 잠근다.
- G354 induction raw의 `AYU의 59/80` 표기는 Astra 오기라는 지시를 기록하되 immutable raw는 고치지 않는다. Astra가 META102에서 `AXU`로 명시 정정할 예정이다. Luna는 의미를 추론해 수정하지 않는다. AYP blind 오류의 사후 보충·원blind 불변·성과 비소급 제한도 유지한다.


<!-- luna-sync:G354-G355-frontier-20260928 -->
## 현재 진행 상태 — G354 반영·G355 frontier

- G354 세 사례의 전체 stage raw 12건과 G353 induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue=processed=5,089 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 315 completed groups·1,125 cases, META101 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G355다. G354 induction raw는 Astra가 추가할 예정이다.
- AYP blind의 매력 오답 입력 오류와 answer_check 사후 보충은 유지한다. 원blind 불변이며 최초 오답 분석 성과로 소급하지 않는다. 기존 AYE hold·복원 blind 및 기타 노출·유보 제한도 보존한다.


<!-- luna-sync:G353-G354-frontier-20260928 -->
## 현재 진행 상태 — G353 반영·G354 frontier

- G353 AYO·AYP·AYQ의 전체 stage raw 12건을 기존 Luna 스크립트로 원문 의미 변경 없이 반영했다. Astra 보고상 최초 선택 답 3건은 모두 공식 답과 일치한다.
- Queue=processed=5,076 unique, pending raw=0, duplicate/orphan 없음. `meta_state.py`: 314 completed groups·1,122 cases, META101 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 품질 제한: AYP blind raw의 `most_attractive_wrong_answer`에 선택 답 ②가 잘못 기입되었고, answer_check에서 사후 보충했다. 원blind는 수정하지 않았으며 최초 오답 분석 성과로 소급 집계하지 않는다.
- 다음 frontier는 G354다. 기존 AYE hold·복원 blind 기록, G348 전사 한계, HOLD·실패·노출 제한을 유지한다.


<!-- luna-sync:META101-G353-frontier-20260928 -->
## 현재 진행 상태 — META101 반영·G353 frontier

- G352 induction 및 META101 raw 각 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue=processed=5,064 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 313 completed groups·1,119 cases, META101 이후 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 frontier는 G353이다. AYE source hold와 복원 blind 기록, G348 안테나 분수계수 전사 누락 한계 및 기존 HOLD·실패·노출 제한은 유지한다.


<!-- luna-sync:G352-META101-lock-20260928 -->
## 현재 진행 상태 — G352 반영·META101 선행·G353 잠금

- G352 AYL·AYM·AYN blind·answer_check·independent_code·sdss_compare raw 12건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Astra 보고상 최초 답 ④·⑤·②는 공식 답과 일치한다.
- Queue=processed=5,062 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 313 completed groups·1,119 cases, META100 이후 3 groups·10 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 허용 작업은 Astra의 G352 induction 및 META101 raw 저장과 Luna sync다. 반영 전까지 G353은 잠근다. AYE source hold와 복원 blind 기록, G348 안테나 분수계수 전사 누락 한계, G024 HOLD·이전 실패·사전노출 제한을 유지한다.


<!-- luna-sync:G350-G351-G352-frontier-20260928 -->
## 현재 진행 상태 — G350·G351 반영·G352 frontier

- G350 AYE·AYF·AYG와 G351 AYH·AYI·AYJ·AYK의 전체 단계 raw 28건 및 AYE source hold raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. 두 group의 일곱 사례는 모두 manifest상 `consumed_sdss`다.
- Queue=processed=5,050 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py`: 312 completed groups·1,116 cases, META100 이후 2 groups·7 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- AYE 원 source hold와 복원 blind raw를 별도 기록으로 보존한다. G350·G351 induction raw 각 1건도 반영했다. 다음 frontier는 G352(AYL~AYN)이며, META100 운영 규칙에 따라 세 번째 group 완료 시 due raw 반영·sync 전까지 다음 frontier를 진행하지 않는다. 사이트와 독립 판정 차이·미확정은 raw대로 유지한다.


<!-- luna-sync:AUDIT99-sync-20260928 -->
## 현재 진행 상태 — AUDIT99 반영·depth backfill 선행·G347 잠금

- `AUDIT99-manual_parity_audit-20260928-01` raw 1건을 payload 의미 변경 없이 독립연구 진행 기록과 processed 원장에 반영했다. AXH의 절차상 제한·strict 제외와 AXO/AXQ/AXU의 depth 보충 지정, 사이트 범위 미확정을 그대로 보존한다.
- Queue=processed=4,977 unique, pending raw=0, duplicate/orphan 없음.
- `meta_state.py` 동기화 결과: META99 이후 완료 group/question 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["AXO", "AXQ", "AXU"]`, `semantic_state_review=[]`이다.
- prepared backlog는 총 1,180건 중 `consumed_sdss` 1,100건·`prepared` 80건이다. G024 DR~DU 4건은 HOLD로 유지하고, 다음 actionable frontier/Excel-style case ID는 **AXV (G347)**로 기록한다.
- 다음 허용 작업은 Astra의 AXO·AXQ·AXU `depth_backfill` raw 작성 및 Luna sync다. 이를 완료하기 전 G347 신규 semantic stage는 잠근다. G024 HOLD·이전 실패·사전노출 제한은 유지한다.

<!-- luna-sync:META99-audit-lock-20260928 -->
## 현재 진행 상태 — META99 반영·manual audit 선행·G347 잠금

- G346 induction과 META99 raw를 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue=processed=4,976, pending raw=0, orphan/duplicate=0.
- `meta_state.py`: 307 groups·1,100 cases, `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음은 Astra의 manual parity audit raw 및 필요한 depth backfill raw다. 완료·sync 확인 전까지 G347은 잠근다.

<!-- luna-sync:G346-META99-lock-20260928 -->
## 현재 진행 상태 — G346 완료·META99 선행·G347 잠금

- G346 전체 stage raw를 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue=processed=4,974, pending raw=0, orphan/duplicate=0.
- `meta_state.py`: 307 groups·1,100 cases, META98 이후 3 groups·9 cases, `meta_due=true`, `manual_parity_audit_due=false`(다음까지 1회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 작업은 Astra의 G346 induction 및 META99 raw 저장과 sync다. 반영 전까지 G347은 잠근다.

<!-- luna-sync:G345-final-20260928 -->
## 현재 진행 상태 — G345 완료·G346 frontier

- G345 전체 stages 및 `G345-induction-20260928-01`을 기존 Luna 스크립트로 raw 의미 변경 없이 반영했다. Queue=processed=4,962, pending raw=0, orphan/duplicate=0.
- `meta_state.py`: 306 groups·1,097 cases, META98 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음까지 1회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 G346이다.

<!-- luna-sync:G344-final-20260928 -->
## 현재 진행 상태 — G344 완료·G345 frontier

- G344 전체 SDSS compare와 `G344-induction-20260928-01`을 기존 Luna 스크립트로 raw 의미 변경 없이 반영했다. Queue=processed=4,949, pending raw=0, orphan/duplicate=0.
- `meta_state.py`: 305 groups·1,094 cases, META98 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음까지 1회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 G345이다.

<!-- luna-sync:META98-G344-frontier-20260928 -->
## 현재 진행 상태 — META98 반영·G344 frontier

- `META98-meta_induction-20260928-01`과 `G343-induction-20260928-01`을 기존 Luna 스크립트로 raw 의미 변경 없이 반영했다. Queue=processed=4,936, pending raw=0, orphan/duplicate=0.
- `meta_state.py`: 304 groups·1,091 cases, META98 이후 0 groups·0 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음까지 1회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- G344 잠금이 해제됐다. 다음 frontier는 G344이다.

<!-- luna-sync:G343-final-20260928 -->
## 현재 진행 상태 — G343 완료·META98 선행·G344 잠금

- G343 전체 raw stages를 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue=processed=4,934, pending raw=0, orphan/duplicate=0.
- `meta_state.py`: 304 groups·1,091 cases, META97 이후 3 groups·10 cases, `meta_due=true`, `manual_parity_audit_due=false`(다음까지 2회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 작업은 Astra의 META98 `meta_induction` raw 저장 및 sync다. META98 반영 전까지 G344는 잠근다.

<!-- luna-sync:G342-final-20260928 -->
## 현재 진행 상태 — G342 완료·G343 frontier

- G342 AXF/AXG/AXH/AXI의 blind·answer_check·independent_code·SDSS compare 및 `G342-induction-20260928-01`을 raw 의미 변경 없이 반영했다. AXH의 원 hold raw는 유지하고, 공식 문제지에서 복원한 선지 보충자료와 별도 resolved 기록을 보존한다.
- G342 네 사례의 최초 답은 모두 공식 답과 일치했다. 단, helper 노출 및 AXH의 source 경로 이탈이 있어 G342 전체를 strict blind 성과에서 제외한다.
- Queue와 processed는 각각 4,922건이며 unique ID 기준 pending 0, orphan 0, duplicate 0이다. `meta_state.py`: 303 groups·1,088 cases, META97 이후 2 groups·7 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음까지 2회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 G343이다. G342의 원 hold 삭제나 정답·SDSS 재열람 없이 이 상태를 유지한다.

<!-- luna-sync:G342-crosswalk-frontier-20260928 -->
## 현재 진행 상태 — crosswalk 반영·G342~G370 READY frontier

- 전체 연구 완료는 302 groups·1,084 cases다. G312~G341의 90 cases는 crosswalk에 모두 `TARGET_MATCHED`로 반영됐다. 이 cohort의 최초 답은 89/90이며 AVE 최초③·공식⑤·확신도 .91 실패를 불변 보존한다. 사후 해석은 최초 성과에 소급하지 않으며, 신규 90건은 strict 성과 미확정이다.
- Target crosswalk: 1,147 rows, completed 547, remaining 600. 미완료 구분은 READY_LOCAL_SOURCE 244, NEEDS_RESTORE 335, SOURCE_MISSING 9, HOLD 4, AMBIGUOUS_COMPLETION 8이다. Research crosswalk: 1,084 rows(547 TARGET_MATCHED, 537 NON_TARGET_RESEARCH). 두 crosswalk와 연구 완료 1,084의 분모를 합산하지 않는다. duplicates 0, HOLD/AMBIGUOUS overlap 0이다.
- Queue=processed=4,903 unique IDs, pending raw=0, duplicate ID=0이다. G312~G341 passage-group barrier는 30/30 통과했다.
- Manifest: consumed_sdss=1,084, prepared=96. G342~G370는 29 groups·92 LEET cases READY_LOCAL_SOURCE이며 첫 frontier는 G342/AXF, 마지막은 G370/BAS다. 이 준비 cohort 바깥에 추가 actionable READY는 0이다. 나머지 4 prepared는 G024 DR/DS/DT/DU HOLD로 유지하며 임의 소비·제외하지 않는다.
- 마지막 preparation preflight: [LUNA_FRONTIER_PREFLIGHT_20260928_G342.md](prepared_backlog/LUNA_FRONTIER_PREFLIGHT_20260928_G342.md). 신규 semantic work는 아직 시작하지 않았다.
- META88~META97, AUDIT90/AUDIT93/AUDIT96 및 BACKFILL90/BACKFILL93/BACKFILL96 상태를 보존한다. 현재 meta_state는 `meta_due=false`, `manual_parity_audit_due=false`(다음까지 2회), `depth_backfill_pending=[]`, `semantic_state_review=[]`다.
- AXB 원 hold는 유지되고, 공식 LEET 2013 홀수형 `table_018.md`에서 복원한 `<가정>`을 출처로 연결한 resolved blind가 별도 보존된다. 정답·SDSS는 복원 단계에서 열람하지 않았다. 기존 AVE 실패와 strict 연구 상태도 유지한다.
- quota unavailable 상태를 그대로 유지한다.

<!-- luna-sync:G312-G341-final-sync-20260928 -->
- quota unavailable 상태를 그대로 유지한다.

<!-- luna-sync:META88-G314-frontier-20260928 -->
## 현재 진행 상태 — G312 및 induction 반영 완료·G313 frontier

- G312 ATT/ATU/ATV의 12 stage raw와 `G312-induction-20260928-01`을 기존 Luna 스크립트로 반영했다. Queue 4,509건·processed 4,509건·unique ID 각각 4,509건·pending raw 0건이다.
- meta_state: 273 groups·997 cases, META87 이후 2 groups·6 cases. `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 별도 due 판단은 새 group 착수 전 다시 확인한다.
- G312 induction에서 unresolved로 둔 ATT 10 최초 경쟁 후보 누락, ATU site7 및 선지 함축 범위, MEET 자료의 KICE 전이 한계를 보존했다. raw 판단 의미를 보충하거나 수정하지 않았다.
- 다음 frontier는 G313. Queue와 processed 차집합을 확인했으며 미처리 raw는 없다. source·sealed 파일은 이번 sync에서 열지 않았다.
- quota unavailable은 그대로 유지한다.

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

<!-- luna-sync:G293-ARQ-hold-20260927 -->
## 현재 상태 — G293 blind 보류·정정 raw 대기

- ARO/ARP blind 2건과 ARQ hold 1건을 반영했다. Queue 4,241건·processed 4,241건·pending raw 0건이다.
- ARQ의 기존 hold raw는 그대로 보존한다. `blind_sources/ARQ.json`이 선언한 `blind_sources/G293_visual01.png` 파일은 존재하며 정상 PNG(1034×880)다. Astra가 도식을 직접 확인했고, 출력에서 `visual_supplements`를 빠뜨린 판독 실수로 판명되어 정정 blind/resolved_hold raw를 기다린다. metadata 불일치 주장은 철회됐다.
- ARQ 정정 raw가 저장되기 전까지 G293 answer_check·independent_code·SDSS 단계는 봉인 상태로 둔다. 다음 연구 frontier는 G293 ARQ의 blind 복구 완료 후 재개한다. quota unavailable 상태를 유지한다.

<!-- luna-sync:META83-final-20260927 -->
## 현재 상태 — META83 완료·G299 frontier

- META83 meta_induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,319건·processed 4,319건·pending raw 0건이다.
- meta_state: 259 groups·955 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- 다음 frontier는 G299 ASG이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:META86-final-20260928 -->
## 현재 상태 — META86 완료·G308 frontier

- META86 meta_induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,441건·processed 4,441건·pending raw 0건이다.
- meta_state: 268 groups·982 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- 다음 frontier는 G308 ATH이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G309-final-20260928 -->
## 현재 상태 — G309 완료·G310 blind 진행 중

- G309 ATK/ATL/ATM stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,469건·processed 4,467건이며, 확인 시점 미처리 2건은 G310 ATN/ATO blind raw다. G309 자체 raw는 모두 처리됐다.
- meta_state: 270 groups·988 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- Queue raw 기계 집계 G282~G309: 28 groups·85 cases, 네 stage 각 85건, group barrier 28/28 통과. 최초 answer_check는 84/85 일치, 1건 불일치(ATK 최초 ④·공식 ②, 확신도 0.94 실패)다. 정답 확인 뒤 보완 풀이는 이 최초 성과를 변경하지 않는다. 노출 상태가 확인되지 않거나 strict 대상이 아닌 사례가 포함되므로 이를 strict blind 성과로 단정하지 않는다.
- ATK의 독립 후보 10 누락, 도덕적 강조와 법적 박탈 해석 한계는 AUDIT87 우선 표본으로 보존한다.
- 다음 frontier는 G310 ATN이며 group 전체 blind 장벽을 먼저 완료해야 한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G308-final-20260928 -->
## 현재 상태 — G308 완료·G309 frontier

- G308 ATH/ATI/ATJ stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,454건·processed 4,454건·pending raw 0건. Queue SHA-256 `b9afbb7a075c7bdd8db1a7ec62fd0f183f8d324d9b5b7f2c6269f963dd1c4983`이다.
- meta_state: 269 groups·985 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ATH 코드 47의 정확 범위 미확정을 보존한다. ATJ의 정답 비판 세 경로와 오답 65 제거 경로는 분리해 보존한다.
- 다음 frontier는 G309 ATK이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G307-final-20260928 -->
## 현재 상태 — G307 완료·META86 선행

- G307 ATE/ATF/ATG stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,440건·processed 4,440건·pending raw 0건. Queue SHA-256 `be520de1a5d6430e3dd77b212f7f2dbddf8895c912fdd38ed4e602325ef641bd`이다.
- meta_state: 268 groups·982 cases, `meta_due=true`(META86 필요), `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ATE 사이트 2와 ATG 코드 28의 정확 범위는 미확정으로 보존한다.
- 다음 frontier는 G308 ATH이나, 새 group 전에 META86을 저장·sync하고 이후 due 상태를 재산정해야 한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G306-final-20260928 -->
## 현재 상태 — G306 완료·G307 frontier

- G306 ATB/ATC/ATD의 stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,427건·processed 4,427건·pending raw 0건. Queue SHA-256 `da9bd2133e0d0cfc9c08b79d33f053be32ccf055952b064aedb778f86d5b2547`이다.
- meta_state: 267 groups·979 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- G306은 초기 핵심8코드 자료의 중산층 점수표 함수/인과 예시에 사전 노출되어 `strict_blind_eligible=false`다. 정답·SDSS 선공개는 없었지만 성과 집계에서 무노출로 세거나 strict blind 성과로 단정하지 않는다.
- 다음 frontier는 G307 ATE이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G305-final-20260927 -->
## 현재 상태 — G305 완료·G306 frontier

- G305 ASY/ASZ/ATA stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,414건·processed 4,414건·pending raw 0건. Queue SHA-256 `59675c33818515db185cd20fe3ac7477dd022c313c006ed1abb3897c184f2447`이다.
- meta_state: 266 groups·976 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- 연구 지문 내부 판단을 실제 처방·금기 판단으로 외삽하지 않는 범위 제한을 보존한다.
- 다음 frontier는 G306 ATB이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:META85-final-20260927 -->
## 현재 상태 — META85 완료·G305 frontier

- META85 meta_induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,401건·processed 4,401건·pending raw 0건이다.
- meta_state: 265 groups·973 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- 다음 frontier는 G305 ASY이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G304-final-20260927 -->
## 현재 상태 — G304 완료·META85 선행

- G304 ASV/ASW/ASX stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,400건·processed 4,400건·pending raw 0건. Queue SHA-256 `cd21d1e96f02683d692b6db480c6fa5f21b10a143773da7c673bbe2918f9194b`이다.
- meta_state: 265 groups·973 cases, `meta_due=true`(META85 필요), `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- 다음 frontier는 G305 ASY이나, 새 group 전에 META85를 저장·sync하고 이후 due 상태를 재산정해야 한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G303-final-20260927 -->
## 현재 상태 — G303 완료·G304 frontier

- G303 ASS/AST/ASU stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,387건·processed 4,387건·pending raw 0건. Queue SHA-256 `61814efc8cff4d0bcb7bb76e298962a5db0f65abb072f46e7ba39b8d9ce82dbc`이다.
- meta_state: 264 groups·970 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ASS 필요조건은 역방향으로 확장하지 않고, AST의 경우 명제와 조건문 층위를 구분한 상태를 보존한다.
- 다음 frontier는 G304 ASV이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G302-final-20260927 -->
## 현재 상태 — G302 완료·G303 frontier

- G302 ASP/ASQ/ASR stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,374건·processed 4,374건·pending raw 0건. Queue SHA-256 `ecf708b23059f451dd352d87d9bc75c90751fd47281dd54a18342341d1c3f10c`이다.
- meta_state: 263 groups·967 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ASR 코드 13은 규범적 부적합이지 실제 행동의 논리적 존재 불가능이 아니라는 범위 제한을 보존한다.
- 다음 frontier는 G303 ASS이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:AUDIT84-backfill-final-20260927 -->
## 현재 상태 — AUDIT84 backfill 반영·G302 재개 가능

- AUDIT84 depth_backfill raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영하고 ASI/ASJ/ASN 상세 파일에 원장 참조를 추가했다.
- ASI의 `effective_primary=17`, `auxiliary=2`, `deferred=19`는 최초 원본을 변경하지 않는 후속 상태로 별도 표시했다.
- Queue 4,361건·processed 4,361건·pending raw 0건. `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- due 작업이 해소되어 다음 frontier G302 ASP를 시작할 수 있다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:AUDIT84-final-20260927 -->
## 현재 상태 — AUDIT84 완료·depth backfill 대기

- AUDIT84 manual_parity_audit raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,360건·processed 4,360건·pending raw 0건이다.
- `meta_state`: `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[ASI, ASJ, ASN]`·`semantic_state_review=[]`이다.
- G302 ASP frontier는 Astra가 ASI/ASJ/ASN depth_backfill raw를 작성·저장하고 Luna sync한 뒤 재개한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:META84-final-20260927 -->
## 현재 상태 — META84 완료·manual parity audit 선행

- META84 meta_induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,359건·processed 4,359건·pending raw 0건이다.
- `meta_state`: `meta_due=false`, `manual_parity_audit_due=true`(remaining 0), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- G302 ASP frontier는 Astra가 due manual parity audit raw를 작성·저장하고 Luna sync한 뒤 재개한다. 이후 due/backfill을 재산정한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G301-final-20260927 -->
## 현재 상태 — G301 완료·META84 선행

- G301 ASM/ASN/ASO stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,358건·processed 4,358건·pending raw 0건. Queue SHA-256 `c68d6fadf0aa5a28a007dc81245f0307a83b592dae7dd94977b803d806f5528e`이다.
- meta_state: 262 groups·964 cases, `meta_due=true`(META84 필요), `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ASM 코드 78의 후속 보조 후보와 ASN의 두려움 전면 부정 금지 의미를 보존한다.
- 다음 frontier는 G302 ASP이나, 새 group 전에 META84를 저장·sync하고 이후 due 상태를 재산정해야 한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G300-final-20260927 -->
## 현재 상태 — G300 완료·G301 frontier

- G300 ASJ/ASK/ASL stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,345건·processed 4,345건·pending raw 0건. Queue SHA-256 `05f1dce870fedf0856623c9546d4a572353f7889e747335e2c1e6d03376a00a6`이다.
- meta_state: 261 groups·961 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ASL의 약화와 완전 반증은 강도 차이로 구분해 보존한다.
- 다음 frontier는 G301 ASM이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G299-final-20260927 -->
## 현재 상태 — G299 완료·G300 frontier

- G299 ASG/ASH/ASI stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,332건·processed 4,332건·pending raw 0건. Queue SHA-256 `8bb4377b09add1828d36c2b304ca6843680156403d23522004f1b15dd8d974bf`이다.
- meta_state: 260 groups·958 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ASI의 최초 보조 코드 19는 근거 불충분으로 유효성을 유보한다. 사이트 19라는 번호 일치만으로 일치 성과를 계수하지 않으며 AUDIT84 표본 carryover로 보존한다.
- 다음 frontier는 G300 ASJ이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G298-final-20260927 -->
## 현재 상태 — G298 완료·META83 선행

- G298 ASD/ASE/ASF stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,318건·processed 4,318건·pending raw 0건. Queue SHA-256 `f1a8ce684508e5a92a890a7e4ffec26a6427b03ecfbb891218cbf5a660b341bf`이다.
- meta_state: 259 groups·955 cases, `meta_due=true`(META83 필요), `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ASD 코드 1의 범위 미확정과 ASE 코드 19의 상호 논거 보완 의미를 보존한다.
- 다음 frontier는 G299 ASG이나, 새 group 전에 META83을 저장·sync하고 이후 due 상태를 재산정해야 한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G297-final-20260927 -->
## 현재 상태 — G297 완료·G298 frontier

- G297 ASA/ASB/ASC stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,305건·processed 4,305건·pending raw 0건. Queue SHA-256 `9169d4420ae45f33231b50372d6ef1a37ab435573edf2b05977b5b9ceaa148c4`이다.
- meta_state: 258 groups·952 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ASC의 최초 동일시 표현은 값 평가를 부가한다는 뜻으로 한정한 answer_check 보완 의미를 보존한다.
- 다음 frontier는 G298 ASD이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G296-final-20260927 -->
## 현재 상태 — G296 완료·G297 frontier

- G296 ARX/ARY/ARZ blind·answer_check·independent_code·sdss_compare stage raw 12건과 induction 1건, 총 13건을 반영했고 queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,292건·processed 4,292건·pending raw 0건. Queue SHA-256 `10becefda4d56941256df86236144b1c4930ec6b114558825898cd29e7e2ba24`이다.
- meta_state: 257 groups·949 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- 다음 frontier는 G297 ASA이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:META82-and-G282-G295-audit-20260927 -->
## 현재 상태 — META82 완료·G296 frontier

- META82 meta_induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,280건·processed 4,280건·pending raw 0건이다.
- meta_state: 256 groups·946 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- Queue raw만 기계적으로 확인한 G282~G295 집계: 14 groups·43 cases, blind/answer_check/independent_code/sdss_compare 각 43건, group stage barrier 14/14 통과. 최초 answer_check의 `match=true` 43/43이며 `blind_answer == official_answer`도 43/43 일치한다. 전체 43건의 historical exposure는 모두 확인 불가이므로 이를 strict blind 성과로 단정하지 않는다.
- 다음 frontier는 G296 ARX이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G295-final-20260927 -->
## 현재 상태 — G295 완료·META82 선행

- G295 ARU/ARV/ARW stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,278건·processed 4,278건·pending raw 0건. Queue SHA-256 `9564eda3fa6591aa995701cfa701e0af7038b3a9082742f806663a4fb9b585a4`이다.
- meta_state: 256 groups·946 cases, `meta_due=true`(META82 필요), `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ARU 코드 28의 정확 범위와 ARW 코드 1의 범위 미확정 상태를 보존한다.
- 다음 frontier는 G296 ARX이나, 새 group 전에 META82를 저장·sync하고 이후 due 상태를 재산정해야 한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G294-final-20260927 -->
## 현재 상태 — G294 완료·G295 frontier

- G294 ARR/ARS/ART stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,265건·processed 4,265건·pending raw 0건. Queue SHA-256 `c7e1fa23dba4f6559df7a145e5d7a1815e091eaa495370ef99bfe6ed24907a91`이다.
- meta_state: 255 groups·943 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ARS 카오스의 엄밀 요건 한계와 ART 코드 98의 범위 미확정 상태를 보존한다.
- 다음 frontier는 G295 ARU이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G293-final-20260927 -->
## 현재 상태 — G293 완료·G294 frontier

- G293은 기존 ARO/ARP blind 및 ARQ hold 3 raw에 더해 ARQ 유효 blind/resolved_hold 정정, 세 문항 answer_check 3·independent_code 3·sdss_compare 3, induction 1을 반영해 총 14 raw가 됐다. 최초 `ARQ-hold-20260927-01`은 불변 보존했다.
- Queue 4,252건·processed 4,252건·pending raw 0건. 세 문항 blind 기록은 모두 전체 answer_check보다 앞서고, group barrier가 통과됐다.
- meta_state: 254 groups·940 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ARQ 정정 blind/resolved_hold로 보류가 해결됐다. 다음 frontier는 G294 ARR이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:AUDIT81-backfill-final-20260927 -->
## 현재 상태 — AUDIT81 backfill 반영·G293 재개 가능

- AUDIT81 depth_backfill raw 1건을 AQG/AQW/ARA/ARE에 걸쳐 기존 Luna 스크립트로 의미 변경 없이 반영했다. 네 상세 파일에 원장 참조를 추가했다.
- AQW는 보완 raw 저장이 해석 해결을 뜻하지 않으며, `code_boundary_evidence_status=unresolved`이고 확정 전역 경계 근거에서 제외됨을 명시했다.
- Queue 4,238건·processed 4,238건·pending raw 0건. `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- due 작업이 모두 해소되어 다음 frontier G293 ARO를 시작할 수 있다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:AUDIT81-final-20260927 -->
## 현재 상태 — AUDIT81 완료·depth backfill 대기

- AUDIT81 manual_parity_audit raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,237건·processed 4,237건·pending raw 0건이다.
- meta_state: `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[AQG, AQW, ARA, ARE]`·`semantic_state_review=[]`이다.
- G293 ARO frontier는 Astra가 AQG/AQW/ARA/ARE depth_backfill raw를 저장한 뒤 Luna sync하고 대기 상태를 재산정한 다음 재개한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:META81-final-20260927 -->
## 현재 상태 — META81 완료·manual parity audit 선행

- META81 meta_induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,236건·processed 4,236건·pending raw 0건이다.
- meta_state: 253 groups·937 cases, `meta_due=false`, `manual_parity_audit_due=true`(remaining 0), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- G293 ARO frontier는 Astra의 due manual parity audit raw 작성·Luna sync 및 이후 due/backfill 재산정 뒤 재개한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G292-final-20260927 -->
## 현재 상태 — G292 완료·META81 선행

- G292 ARL/ARM/ARN stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,235건·processed 4,235건·pending raw 0건. Queue SHA-256 `09d786489775f0188490359a55405a879872506e01dcf71e640cc02c462beddd`이다.
- meta_state: 253 groups·937 cases, `meta_due=true`(META81 필요), `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- AQG69의 경쟁 코드 반증에서 미지 사실 추론 금지 기준을 보정할 필요가 있다는 Astra 후속 감사 대상을 보존한다.
- 다음 frontier는 G293 ARO이나, 새 group 전에 META81을 저장·sync하고 이후 due audit/backfill을 재산정·처리해야 한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G291-final-20260927 -->
## 현재 상태 — G291 완료·G292 frontier

- G291 ARI/ARJ/ARK stage 12건과 induction 1건, 총 13 raw를 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,222건·processed 4,222건·pending raw 0건. Queue SHA-256 `74dcdfa6c60815157d7d76cd31519b06cfeeb5192bdafc074de9493d76979430`이다.
- meta_state: 252 groups·934 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ARJ의 코드 59 해결책 방향과 코드 75/28 양보 귀속 경로를 함께 보존했다.
- 다음 frontier는 G292 ARL이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G290-final-20260927 -->
## 현재 상태 — G290 완료·G291 frontier

- G290 ARF/ARG/ARH stage 12건과 induction 1건, 총 13 raw를 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,209건·processed 4,209건·pending raw 0건. Queue SHA-256 `a1149545f510f78f1dbb4fa1c790553f244ef56c5dd064df253ab5fd9845f15b`이다.
- meta_state: 251 groups·931 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ARF/ARG/ARH의 경로별 8/10, 원관계 12/10, 오독 관계 25 구분을 그대로 보존했다.
- 다음 frontier는 G291 ARI이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:META80-final-20260927 -->
## 현재 상태 — META80 완료·G290 frontier

- META80 meta_induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,196건·processed 4,196건·pending raw 0건이다.
- meta_state: 250 groups·928 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- AUDIT81 carryover로 AQW/ARA/ARE의 미해결 판정·범위 한계를 보존한다.
- 다음 frontier는 G290 ARF이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G289-final-20260927 -->
## 현재 상태 — G289 완료·META80 선행

- G289 ARC/ARD/ARE stage raw 12건과 induction 1건, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,195건·processed 4,195건·pending raw 0건. Queue SHA-256 `8afa6fcb69b5734d64b6eec3b3f6eb7244a3b3772ffe0ee099f4c04cf2213cd4`이다.
- meta_state: 250 groups·928 cases, `meta_due=true`(META80 필요), `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ARE 사이트 19의 정확 범위는 미확정으로 보존한다.
- 다음 frontier는 G290 ARF이나, 새 group 전에 META80을 저장·sync하고 due 상태를 다시 확인해야 한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G288-final-20260927 -->
## 현재 상태 — G288 완료·G289 frontier

- G288 AQZ/ARA/ARB stage 12건과 induction 1건, 총 13 raw를 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,182건·processed 4,182건·pending raw 0건. Queue SHA-256 `c32543a7e0f9eb29e9accf7b9dae7187769cf55ef7625d9af28a3f4a6286cdc0`이다.
- meta_state: 249 groups·925 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- ARA①의 동일 결과 보장 한계를 보존했다. ARB는 사이트 1을 양/질 공동 후보로 추가하되 최초 37 판정을 유지했다. 이를 확정된 전역 경계로 일반화하지 않는다.
- 다음 frontier는 G289 ARC이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G287-final-20260927 -->
## 현재 상태 — G287 완료·G288 frontier

- G287 AQW/AQX/AQY stage 12건과 induction 1건, 총 13 raw를 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,169건·processed 4,169건·pending raw 0건. Queue SHA-256 `4b5a5da8f998fd5575eaf8e760954f9773d0581d26b0578e5a10202955e1e187`이다.
- meta_state: 248 groups·922 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- AQW는 정답 일치이며 세부 근거와 16/46 경쟁은 미확정으로 보존하고, 다음 audit 표본 carryover로 기록됐다. 이를 새 전역 경계로 일반화하지 않는다.
- 다음 frontier는 G288 AQZ이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:META79-final-20260927 -->
## 현재 상태 — META79 완료·G287 frontier

- META79 meta_induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,156건·processed 4,156건·pending raw 0건이다.
- meta_state: 247 groups·919 cases, `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 2회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- 다음 frontier는 G287 AQW이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G286-final-20260927 -->
## 현재 상태 — G286 완료·META79 선행

- G286 AQT/AQU/AQV의 blind 3·answer_check 3·independent_code 3·sdss_compare 3과 G286 induction 1 raw, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,155건·processed 4,155건·pending raw 0건. Queue SHA-256 `5e57fd07f8f3e7552d74c915eeaa6a66f3efb05d20a13e3e2c202ff9ff098fee`이다.
- meta_state: 247 groups·919 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- 다음 frontier는 G287 AQW이나, 새 group 전에 META79를 저장·sync하고 due 상태를 다시 확인해야 한다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G285-final-20260927 -->
## 현재 상태 — G285 완료·G286 frontier

- G285 AQQ/AQR/AQS의 blind 3·answer_check 3·independent_code 3·sdss_compare 3과 G285 induction 1 raw, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,142건·processed 4,142건·pending raw 0건. Queue SHA-256 `1e40eb4c38e4512e068c139c31d51d0a240636d4d0d052695deeb72e4f63e05b`로 반영 전후 불변이다.
- meta_state: 246 groups·916 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- 다음 frontier는 G286 AQT이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:G284-final-20260927 -->
## 현재 상태 — G284 완료·G285 frontier

- G284 AQN/AQO/AQP의 blind 3·answer_check 3·independent_code 3·sdss_compare 3과 G284 induction 1 raw, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 stage barrier가 확인됐다.
- Queue 4,129건·processed 4,129건·pending raw 0건. meta_state: 245 groups·913 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- 다음 frontier는 G285 AQQ이다. quota unavailable 상태를 그대로 보존한다.

<!-- luna-sync:AUDIT78-backfill-final-20260927 -->
## 현재 상태 — AUDIT78 backfill 반영·G284 재개 가능

- AUDIT78 depth_backfill raw의 AQI/AQL evidence_additions, 유보·제한을 원문 의미 그대로 기존 스크립트로 반영했다. AQI/AQL 상세 기록에는 해당 raw 원장 참조만 추가했다.
- Queue 4,116건·processed 4,116건·pending raw 0건. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- due 작업이 모두 해소되어 다음 frontier G284 AQN을 시작할 수 있다. quota unavailable 상태는 기존대로 보존한다.

<!-- luna-sync:AUDIT78-final-20260927 -->
## 현재 상태 — AUDIT78 완료·depth backfill 대기

- AUDIT78 manual_parity_audit raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,115건·processed 4,115건·pending raw 0건이다.
- `meta_state`: `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 3회), `depth_backfill_pending=[AQI, AQL]`·`semantic_state_review=[]`이다.
- G284 frontier 재개 전 Astra가 AQI/AQL depth_backfill raw를 작성·저장하고 Luna sync해야 한다.

<!-- luna-sync:META78-final-20260927 -->
## 현재 상태 — META78 완료·manual parity audit 선행

- META78 meta_induction raw 1건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 4,114건·processed 4,114건·pending raw 0건이다.
- meta_state: 244 groups·910 cases, `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- G284 AQN frontier 재개 전 Astra가 due manual parity audit raw를 작성·저장하고 Luna sync해야 한다. 이후 due/backfill을 재산정한다.

<!-- luna-sync:G283-final-20260927 -->
## 현재 상태 — G283 완료·META78 선행

- G283 AQK/AQL/AQM의 blind 3·answer_check 3·independent_code 3·sdss_compare 3과 G283 induction 1 raw, 총 13건을 기존 Luna 스크립트로 의미 변경 없이 반영했다. Queue 순서에서 group 전체 blind → answer_check → independent_code → SDSS barrier가 확인됐다.
- Queue 4,113건·processed 4,113건·pending raw 0건. Queue SHA-256 `1223f32260d01eae10bd1cd85ec4913eb49a925444d46524f040327ba03848c7`이다.
- meta_state: 244 groups·910 cases, `meta_due=true`(META78 필요), `manual_parity_audit_due=false`(다음 audit까지 1회), `depth_backfill_pending=[]`·`semantic_state_review=[]`이다.
- 다음 prepared frontier는 G284 AQN이나, 새 group에 앞서 META78과 그 뒤 재산정되는 audit/backfill 필요 여부를 먼저 처리해야 한다. quota unavailable 상태를 유지한다. 요청 모델 gpt-5.6-luna 미제공으로 gpt-6-luna가 sync했다.

<!-- luna-sync:G282-final-20260927 -->
## 현재 상태 — G282 완료·G283 frontier

- G282 AQG~AQJ의 blind 4·answer_check 4·independent_code 4·sdss_compare 4와 G282 induction 1 raw를 기존 Luna 스크립트로 의미 변경 없이 반영했다. 네 문항 모두 전체 stage barrier를 통과했다.
- Queue 4,100건·processed 4,100건·pending raw 0건. Queue SHA-256 `cbd11324528d0e9a2e26a60fe9edb5a4114d8372414b3d29126eab7a21bafe08`로 반영 전후 불변이다.
- meta_state: 243 groups·907 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 1회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- 다음 frontier는 G283 AQK이다. quota는 unavailable로 보존한다. 요청 모델 gpt-5.6-luna 미제공으로 gpt-6-luna가 sync했다.

<!-- luna-sync:G282-source-prepared-20260927 -->
## 현재 상태 — G282~G311 source preparation 완료

- Overall research corpus: `research_completed_total = 903`문항. 이 누적에는 target universe 밖의 KICE 연구 537문항도 포함되며 기존 귀납·meta/audit evidence를 보존한다.
- Current target universe: `target_completed = 366 / 1147`; `target not completed = 781` (HOLD·모호·missing 포함). READY_LOCAL_SOURCE 425, NEEDS_RESTORE 335, SOURCE_MISSING 9, HOLD 4, AMBIGUOUS_COMPLETION 8.
- 새 READY: G282~G311, 30 passage groups·91 questions, AQG~ATS. Family는 MEET/DEET 30 groups. G282/AQG가 첫 READY이며 blind·sealed source·packet은 생성했으나 semantic research는 아직 시작하지 않았다.
- Manifest: 998 rows — consumed_sdss 903, prepared 95 (신규 READY 91 + G024 DR~DU HOLD 4). 기존 G024 HOLD 및 target 밖 연구는 변경하지 않았다.
- Crosswalk-aware preflight의 required checks는 모두 0이다. 신규 91 후보는 COMPLETED_TARGET·HOLD·AMBIGUOUS_COMPLETION과 겹치지 않는다.
- Queue/processed는 수정하지 않았다. SHA-256: queue `e98e459b68fe52ae582fae7d213e550e4052930770ea8762ebc33e7769881624`, processed `f0fe43a1d5ceeb02b777b4a07a2ca1d2faeb948b594955ddf88bce9d8abde456`.
- Crosswalk: `data/기본기_연구/target_completion_crosswalk_v1.jsonl`, `data/기본기_연구/research_case_target_crosswalk_v1.jsonl`; preparation report: `data/기본기_연구/prepared_backlog/LUNA_FRONTIER_PREFLIGHT_20260927_G282.md`.

<!-- luna-sync:G252-G281-final-20260927 -->
## Luna 역할 sync — G252~G281 준비목록 소진 checkpoint

- 신규 범위 G252~G281만 집계했다. 30 groups·86 cases·392 raw이며, stage raw는 blind 86, answer_check 88(최초 86 + ANI 보충 2), independent_code 86, sdss_compare 86이다. induction 30, META68~77 10, manual audit 3, depth_backfill 3건(총 6 cases)이다. 이전 G232~G251은 이번 집계에서 제외했다.
- 최초 group stage barrier는 30/30 통과했다: group 전체 blind → case별 최초 answer_check 전체 → group 전체 independent_code → group 전체 SDSS. 최초 공식 대조 86건 중 85건 일치, ANI-answer_check-20260927-01 1건 불일치를 그대로 보존한다. ANI answer_check -02/-03은 별도 보충 기록이며 최초 barrier 집계에 넣지 않는다. 보충은 ANG/ANH independent_code 뒤, ANI independent_code 앞에 추가됐다.
- raw 원장의 record_id는 모두 고유하고 queue 4,083건의 record_id가 processed 4,083건에서 모두 대응하며 pending은 0이다. 처리 스크립트는 queue를 쓰지 않는다. 다만 이전 기준 hash가 없어 세션 간 payload 불변성 자체의 hash 검증은 수행 불가로 남긴다.
- meta_state: 242 groups·903 cases, META77, meta_due=false, manual_parity_audit_due=false(다음 audit까지 1회), depth_backfill_pending=[]·semantic_state_review=[]. manifest 907건 중 consumed_sdss 903건, prepared 4건이며 네 건 모두 G024 DR~DU historical hold로 미소비 상태다. actionable prepared 0건이다.
- 이는 현재 준비목록 소진 checkpoint이며 quota 종료가 아니다. quota unavailable은 그대로 보존한다. source/sealed 원문은 열람하지 않았다.

<!-- luna-sync:META77-G280-20260927 -->
## Luna 역할 sync — G280 전체 단계·META77 반영 완료·G281 frontier

- AQB/AQC/AQD stage raw 12건, G280 induction 1건, META77 meta_induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. AQC의 일반적 가장 필수성과 특정 표정 연기의 필수성을 구분했다.
- queue 4,074건·processed 4,074건·pending raw 0건. meta_state 기준 241 groups·901 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 1회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 901건·prepared 6건이며 마지막 group G281의 AQE/AQF 두 사례가 남았다. due 해소 후 다음 frontier는 G281 AQE이다. quota unavailable 유지, source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G279-20260927 -->
## Luna 역할 sync — G279 전체 단계·귀납 반영 완료·G280 frontier

- APY/APZ/AQA stage raw 12건과 G279 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. APY의 승인 비유일 필요 조건과 침묵 미인지 대안을 보존하고, AQA 코드 2의 범위는 미확정으로 유지했다.
- queue 4,060건·processed 4,060건·pending raw 0건. meta_state 기준 240 groups·898 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 2회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 898건·prepared 9건이며 마지막 준비 group은 G281이다. 다음 frontier는 G280 AQB이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G278-20260927 -->
## Luna 역할 sync — G278 전체 단계·귀납 반영 완료·G279 frontier

- APV/APW/APX stage raw 12건과 G278 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. APW 코드 10의 정의 요건 층위와 최초 판정 코드 74를 분리해 보존했다.
- queue 4,047건·processed 4,047건·pending raw 0건. meta_state 기준 239 groups·895 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 2회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 895건·prepared 12건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G279 APY이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:META76-G277-20260927 -->
## Luna 역할 sync — G277 전체 단계·META76 반영 완료·G278 frontier

- APS/APT/APU stage raw 12건, G277 induction 1건, META76 meta_induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. APT 17/98과 APU 60/66/12가 같은 연결을 다르게 보는 관점 차이를 보존했다.
- queue 4,034건·processed 4,034건·pending raw 0건. meta_state 기준 238 groups·892 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 2회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 892건·prepared 15건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G278 APV이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G276-20260927 -->
## Luna 역할 sync — G276 전체 단계·귀납 반영 완료·G277 frontier

- APP/APQ/APR stage raw 12건과 G276 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. 관리인의 비속박 상태를 뒷받침할 근거가 없다는 점과 실제 속박 확정을 구분해 보존했다.
- queue 4,020건·processed 4,020건·pending raw 0건. meta_state 기준 237 groups·889 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 3회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 889건·prepared 18건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G277 APS이다. G277 완료 후 META76을 예정한다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G275-20260927 -->
## Luna 역할 sync — G275 전체 단계·귀납 반영 완료·G276 frontier

- APM/APN/APO stage raw 12건과 G275 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. APN의 정의·필요 조건·사례 연결과 최초 판정을 그대로 보존했다.
- queue 4,007건·processed 4,007건·pending raw 0건. meta_state 기준 236 groups·886 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 3회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 886건·prepared 21건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G276 APP이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:AUDIT75-final-G274-20260927 -->
## Luna 역할 sync — G274 전체 단계·META75/AUDIT75/backfill 완료·G275 frontier

- API/APJ/APK/APL stage raw 16건, G274 induction 1건, META75 meta_induction 1건, AUDIT75 manual_parity_audit 1건, APB/APH depth_backfill 1건을 기존 스크립트로 의미 변경 없이 반영했다.
- APH 공식 답 ②를 유지하되 D>M이 유일하게 필요한 전제인지 확정 유보한다. 순증가와 부족 해소를 별개로 구분하는 수정을 보존했다.
- queue 3,994건·processed 3,994건·pending raw 0건. meta_state 기준 235 groups·883 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 3회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- APB 공식 crop과 provenance는 sealed/G271_APB_official_diagram_labeled_20260927.png 및 provenance.json에 보존됐다고 보고받았다. due 단계 해소 후 다음 frontier는 G275 APM이다. quota unavailable 유지, source/sealed를 열람하지 않았다.

<!-- luna-sync:G273-20260927 -->
## Luna 역할 sync — G273 전체 단계·귀납 반영 완료·G274 frontier

- APF/APG/APH stage raw 12건과 G273 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. APH의 순공급 단순 모형, 전시 위험, 정량 자료 한계를 함께 보존했다.
- queue 3,974건·processed 3,974건·pending raw 0건. meta_state 기준 234 groups·879 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 1회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 879건·prepared 28건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G274 API이다. 이후 META75와 manual audit 단계를 진행할 예정이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G272-20260927 -->
## Luna 역할 sync — G272 전체 단계·귀납 반영 완료·G273 frontier

- APC/APD/APE stage raw 12건과 G272 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. APE의 공개 후 코드 20과 최초 판정 코드 73을 분리해 보존했다.
- queue 3,961건·processed 3,961건·pending raw 0건. meta_state 기준 233 groups·876 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 1회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 876건·prepared 31건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G273 APF이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:META74-G271-20260927 -->
## Luna 역할 sync — G271 전체 단계·META74 반영 완료·G272 frontier

- APA/APB stage raw 8건, G271 induction 1건, META74 meta_induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. APA90 적용 범위 미확정 상태를 유지했다.
- APB 이미지에 문자 노드가 없다는 점과 blind 기록에서 도식을 사용한 한계를 그대로 보존했다.
- queue 3,948건·processed 3,948건·pending raw 0건. meta_state 기준 232 groups·873 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 1회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 873건·prepared 34건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G272 APC이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G270-20260927 -->
## Luna 역할 sync — G270 전체 단계·귀납 반영 완료·G271 frontier

- AOX/AOY/AOZ stage raw 12건과 G270 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. AOY의 공간 조건 아래 코드 13 공개 후 후보 지위와 코드 42 유일 주 지위 미확정을 보존했다.
- queue 3,938건·processed 3,938건·pending raw 0건. meta_state 기준 231 groups·871 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 2회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 871건·prepared 36건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G271 APA이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G269-20260927 -->
## Luna 역할 sync — G269 전체 단계·귀납 반영 완료·G270 frontier

- AOU/AOV/AOW stage raw 12건과 G269 induction 1건을 기존 스크립트로 반영했다. MEET 공식 페이지 검증본과 봉인 답 연결의 사용 범위를 보존했다.
- AOV 코드 43/53 중첩 및 AOL과 AOV에서 코드 43의 필수성 차이를 그대로 기록했다. AOW의 이론 예측과 실제 관측은 서로 구분했다.
- queue 3,925건·processed 3,925건·pending raw 0건. meta_state 기준 230 groups·868 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 2회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 868건·prepared 39건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G270 AOX이다.
- quota unavailable 유지. sealed 답·source 원문을 열람하거나 의미를 재판정하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:META73-G268-20260927 -->
## Luna 역할 sync — G268 전체 단계·META73 반영 완료·G269 frontier

- AOR/AOS/AOT stage raw 12건, G268 induction 1건, META73 meta_induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. 사이트 코드 적용 범위 미확정과 최초 판정을 유지했다.
- queue 3,912건·processed 3,912건·pending raw 0건. meta_state 기준 229 groups·865 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 2회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 865건·prepared 42건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G269 AOU이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G267-20260927 -->
## Luna 역할 sync — G267 전체 단계·귀납 반영 완료·G268 frontier

- AOP/AOQ stage raw 8건과 G267 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. AOP 코드 42와 AOQ 코드 59의 적용 범위 미확정 상태를 보존했다.
- queue 3,898건·processed 3,898건·pending raw 0건. meta_state 기준 228 groups·862 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 3회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 862건·prepared 45건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G268 AOR이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G266-20260927 -->
## Luna 역할 sync — G266 전체 단계·귀납 반영 완료·G267 frontier

- AOM/AON/AOO stage raw 12건과 G266 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. AON 코드 2/4/19 및 AOO 코드 62의 범위 미확정 상태를 보존했다.
- queue 3,889건·processed 3,889건·pending raw 0건. meta_state 기준 227 groups·860 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 3회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 860건·prepared 47건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G267 AOP이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:AUDIT72-final-G265-20260927 -->
## Luna 역할 sync — G265 전체 단계·META72/AUDIT72/backfill 완료·G266 frontier

- AOK/AOL stage raw 8건, G265 induction 1건, META72 meta_induction 1건, AUDIT72 manual_parity_audit 1건, AOE/AOL depth_backfill 1건 등 총 12 raw를 기존 스크립트로 반영했다. AOL의 직접 정답 근거와 다른 선지 실험 분석 범위 차이는 유지했다.
- AOL depth_backfill은 최초 43 판정을 보존하면서 사후 정답 직접 경로의 유일 주 지위를 철회하고, 46/17/5 후보와 43 범위 제한 수정을 명시했다.
- queue 3,876건·processed 3,876건·pending raw 0건. meta_state 기준 226 groups·857 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 3회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- due가 모두 해소되어 다음 frontier는 G266 AOM이다. quota unavailable 유지, source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G264-20260927 -->
## Luna 역할 sync — G264 전체 단계·귀납 반영 완료·G265 frontier

- AOH/AOI/AOJ stage raw 12건과 G264 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다.
- queue 3,864건·processed 3,864건·pending raw 0건. meta_state 기준 225 groups·855 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 1회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 855건·prepared 52건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G265 AOK이다. 다음 meta_induction은 META72이며 그 뒤 manual parity audit due가 예상된다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G263-20260927 -->
## Luna 역할 sync — G263 전체 단계·귀납 반영 완료·G264 frontier

- AOE/AOF/AOG stage raw 12건과 G263 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. AOE의 코드 42/2 사이트 적용 범위 미확정 상태를 보존했다.
- queue 3,851건·processed 3,851건·pending raw 0건. meta_state 기준 224 groups·852 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 1회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 852건·prepared 55건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G264 AOH이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:META71-G262-20260927 -->
## Luna 역할 sync — G262 전체 단계·META71 반영 완료·G263 frontier

- AOB/AOC/AOD stage raw 12건, G262 induction 1건, META71 meta_induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. AOC의 코드 12/15/45 중첩과 사이트 코드 19의 적용 범위 미확정 상태를 그대로 보존했다.
- queue 3,838건·processed 3,838건·pending raw 0건. meta_state 기준 223 groups·849 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 1회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 849건·prepared 58건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G263 AOE이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G261-20260927 -->
## Luna 역할 sync — G261 전체 단계·귀납 반영 완료·G262 frontier

- ANY/ANZ/AOA stage raw 12건과 G261 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. AOA의 ② 명시 근거 한계는 공식 정답 ④와 구분해 보존했다.
- queue 3,824건·processed 3,824건·pending raw 0건. meta_state 기준 222 groups·846 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 2회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 846건·prepared 61건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G262 AOB이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G260-20260927 -->
## Luna 역할 sync — G260 전체 단계·귀납 반영 완료·G261 frontier

- ANV/ANW/ANX stage raw 12건과 G260 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. ANW의 코드 17/44 국소 중첩 최초 판정을 보존했다.
- queue 3,811건·processed 3,811건·pending raw 0건. meta_state 기준 221 groups·843 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 2회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 843건·prepared 64건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G261 ANY이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:META70-G259-20260927 -->
## Luna 역할 sync — G259 전체 단계·META70 반영 완료·G260 frontier

- ANS/ANT/ANU stage raw 12건, G259 induction 1건, META70 meta_induction 1건을 기존 스크립트로 의미 변경 없이 반영했다.
- queue 3,798건·processed 3,798건·pending raw 0건. meta_state 기준 220 groups·840 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 2회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 840건·prepared 67건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G260 ANV이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G258-20260927 -->
## Luna 역할 sync — G258 전체 단계·귀납 반영 완료·G259 frontier

- ANP/ANQ/ANR stage raw 12건과 G258 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. 최초 판정과 공개 후 판정의 구분을 raw 기록대로 유지했다.
- queue 3,784건·processed 3,784건·pending raw 0건. meta_state 기준 219 groups·837 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 3회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 837건·prepared 70건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G259 ANS이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:G257-20260927 -->
## Luna 역할 sync — G257 전체 단계·귀납 반영 완료·G258 frontier

- ANM/ANN/ANO stage raw 12건과 G257 induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. ANN의 코드 58 적용 범위는 미확정 상태 그대로 보존했다.
- queue 3,771건·processed 3,771건·pending raw 0건. meta_state 기준 218 groups·834 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 3회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 834건·prepared 73건이다. G024 DR~DU 4건 hold를 제외한 G258~G281 69건은 기계적 노출 검증 문제 0으로 `data/기본기_연구/prepared_backlog/LUNA_G258_G281_RECHECK_20260927.md`에 기록되어 있다. 다음 frontier는 G258 ANP이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다. 지정 gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 Luna 기계적 sync를 수행했다.

<!-- luna-sync:AUDIT69-G256-final-20260927 -->
## Luna 역할 sync — G256 전체 단계·META69·AUDIT69 backfill 완료·G257 frontier

- ANJ/ANK/ANL stage 12건, G256 induction, META69 meta_induction, AUDIT69 manual_parity_audit, AUDIT69_BACKFILL depth_backfill 등 총 16 raw를 기존 스크립트로 의미 변경 없이 반영했다. backfill은 ANI/ANL 두 사례이다.
- queue 3,758건·processed 3,758건·pending raw 0건. meta_state 기준 217 groups·831 cases, meta_due=false, manual_parity_audit_due=false(다음 audit까지 3회), depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 831건·prepared 76건이다. G024 DR~DU 4건은 hold이며, due 단계 해소 후 다음 frontier는 G257 ANM이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G255-20260927 -->
## Luna 역할 sync — G255 전체 단계·보충 대조·귀납 반영 완료·G256 frontier

- ANG/ANH/ANI stage 12건, ANI answer_check 보충 2건, G255 induction 1건을 기존 스크립트로 반영했다. ANI 공식 정답 대조의 match=false를 세 raw 모두 그대로 보존했으며, 재검토 답안 수용을 blind 성공으로 재분류하지 않았다.
- ANI 공식 문제·정답 HWP 추출 검증은 sealed/ANI_OFFICIAL_SOURCE_RECHECK_20260927.md에 기계 기록으로 보존되어 있다. 이번 Luna sync는 그 파일이나 원문 source를 읽지 않았다.
- 원래 group 전체 answer_check 기록이 independent_code보다 먼저 저장된 상태를 보존한다. ANI answer_check 보충 raw는 다른 case의 independent_code raw 뒤에 추가되었으므로, append 순서만으로 초기 group barrier 위반으로 해석하지 않는다.
- ANI 의미 한계: 정답 ②를 대부분으로 받아들여도 전후 참여량이 증가하지 않았음을 증명할 수 없다. 이 제한을 추후 해석·경계 판정에 계속 보존한다.
- queue 3,742건·processed 3,742건·pending raw 0건. meta_state 기준 216 groups·828 cases, meta_due=false, manual_parity_audit_due=false, depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 828건·prepared 79건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G256 ANJ이다. quota unavailable을 유지하고 source/sealed를 열람하거나 의미를 재판정하지 않았다.

<!-- luna-sync:G254-induction-20260927 -->
## Luna 역할 sync — G254 전체 단계·귀납 반영 완료·G255 frontier

- ANE/ANF stage raw 8건과 G254-induction-20260927-01 1건을 기존 스크립트로 의미 변경 없이 반영했다. 신규 review 표시는 없다.
- queue 3,727건·processed 3,727건·pending raw 0건이다. meta_state 기준 215 groups·825 cases, meta_due=false, manual_parity_audit_due=false, depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 825건·prepared 82건이다. G024 DR~DU 4건은 hold이며, 다음 frontier는 G255 ANG이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G253-meta68-20260927 -->
## Luna 역할 sync — G253 전체 단계·META68 반영 완료·G254 frontier

- ANB/ANC/AND stage raw 12건, G253 induction 1건, META68 meta_induction 1건을 기존 스크립트로 의미 변경 없이 반영했다. 신규 review 표시는 없다.
- queue 3,718건·processed 3,718건·pending raw 0건이다. meta_state 기준 214 groups·823 cases, meta_due=false, manual_parity_audit_due=false이며 다음 audit은 META69에서 due 예정, depth_backfill_pending=[]·semantic_state_review=[]이다.
- manifest 907건 중 consumed_sdss 823건·prepared 84건이다. G024 DR~DU 4건은 hold이며, 미소비 frontier는 G254 ANE부터다. 다음 group은 G254이다.
- quota unavailable 유지. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G252-stages-induction-20260927 -->
## Luna 역할 sync — G252 전체 단계·귀납 반영 완료·G253 frontier

- AMY/AMZ/ANA blind·answer_check·independent_code·sdss_compare 12 raw와 G252-induction-20260927-01 1 raw를 기존 스크립트로 상세 문서 및 처리 원장에 의미 변경 없이 반영했다. 새 항목의 needs_astra_review 표시는 없다.
- queue 3,704건·processed 3,704건·pending raw 0건을 queue record_id와 processed source_record_id 기준으로 확인했다. meta_state.py 기준 213 groups·820 cases, meta_due=false, manual_parity_audit_due=false, depth_backfill_pending=[], semantic_state_review=[]이다.
- manifest는 907건 중 consumed_sdss 820건·prepared 87건이다. 준비 backlog의 미소비 사례는 G253~G281 83건이며, G024 DR~DU 4건은 hold로 유지한다. 다음 frontier는 G253, 다음 case ANB이다. 기계적 노출 재검증은 data/기본기_연구/prepared_backlog/LUNA_G252_G257_RECHECK_20260927.md에 기록되어 있다.
- quota unavailable 상태를 그대로 보존했다. source/sealed 열람·의미 재판정은 하지 않았으며, meta induction은 Astra raw를 그대로 후처리했다. gpt-5.6-luna 미제공으로 사용 가능한 gpt-6-luna가 기계적 sync를 수행했다.

# CURRENT — 평가원 문체·100코드 기본기 연구
<!-- luna-sync:G251-final-state-20260927 -->
## Luna 역할 sync — G251 및 2026-09-27 누적 상태 확인

- G251 AMV/AMW/AMX stage 12건과 `G251-induction-20260927-01`을 반영했다. queue/processed는 3,691/3,691, pending 0이다. 이번 날짜 신규 raw 259건은 blind 57, answer_check 57, independent_code 57, sdss_compare 57, induction 20, meta_induction 7, manual_parity_audit 2, depth_backfill 2건이다. stage case 57개·group 20개이며 answer_check `match=true` 57건이다. G232~G251 20개 group 모두 max(blind index)<min(answer_check)<min(independent_code)<min(sdss_compare) 순서 검증을 통과했다.
- `meta_state.py`: 212 groups·817 cases 완료, meta_induction_count 67, `meta_due=false`, `manual_parity_audit_due=false`(다음까지 2), `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest 821건 중 consumed_sdss 817, prepared 4(DR/DS/DT/DU, G024), 신규 미소비 준비 사례 0건이다. prepared 4건은 모두 blind·answer_check만 있고 independent_code·sdss_compare는 없다. 노출 근거는 `G024-hold-20260912-preexposure-barrier-01` 및 `G024-hold-20260912-quota-threshold-01`: DR의 답과 SDSS #49가 source 열람 전에 노출되어 group 전체 strict blind 자격이 없고 독립 판정 단계에 진입하지 않는다는 hold다. 재blind·독립 최초 판정을 만들지 말고, 명시된 비독립 절차 없이 이 사례의 의미 연구를 재개하지 않는다. 이를 exclude로 바꾸지 않는다.
- manifest 마지막 group은 G251이다. G252는 준비된 사례로 기록되어 있지 않으며, 다음 작업은 신규 source 후보 준비다. G024 네 사례는 hold 상태로 남긴다.
- 집계는 queue/processed/manifest/meta_state 메타데이터만 사용했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:META67-G251-frontier-20260927 -->
## Luna 역할 sync — G250 귀납·META67 반영 완료·G251 frontier

- G250 AMT/AMU의 stage raw 8건과 `G250-induction-20260927-01`, `META67-meta_induction-20260927-01` raw를 기존 스크립트로 의미 변경 없이 반영했다. 미확정 상태는 Astra raw 그대로 보존했다.
- queue 3,678건·processed 3,678건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 211 groups·814 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 2회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G251**이다. induction·META67 raw 모두 처리되었고 추가 검토 표시는 없다. 마지막 manifest group은 G251이다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G249-complete-20260927 -->
## Luna 역할 sync — G249 전체 단계·귀납 반영 완료·G250 frontier

- G249 AMR/AMS의 stage raw 8건과 `G249-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 후보 미확정 및 공개 전후 후보 구분은 Astra raw 그대로 보존했다.
- queue 3,668건·processed 3,668건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 210 groups·812 cases, META66 이후 2 groups·5 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 3회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G250**이다. G249 induction 반영과 pending 0 검증을 마쳤으며 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G248-complete-20260927 -->
## Luna 역할 sync — G248 전체 단계·귀납 반영 완료·G249 frontier

- G248 AMO/AMP/AMQ의 blind·answer_check·independent_code·sdss_compare raw 12건과 `G248-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 후보와 미확정 지위는 Astra raw 그대로 보존했다.
- queue 3,659건·processed 3,659건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 209 groups·810 cases, META66 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 3회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G249**이다. G248 induction 반영과 pending 0 검증을 마쳤으며 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:AUDIT66-backfill-G248-20260927 -->
## Luna 역할 sync — META66 audit·2-case depth_backfill 완료·G248 frontier

- `AUDIT66_BACKFILL-depth_backfill-20260927-01` 2-case raw를 기존 스크립트로 반영했다. AML ①의 정량 검증 유보와 정답 ③을 구별해 보존하고 의미를 수정하지 않았다.
- queue 3,646건·processed 3,646건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 208 groups·807 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 3회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- due semantic 단계와 backfill이 해소되어 다음 frontier는 **G248**이다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G246-complete-20260927 -->
## Luna 역할 sync — G246 전체 단계·귀납 반영 완료·G247 frontier

- G246 AMI/AMJ/AMK/AML의 stage raw 16건과 `G246-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 58 범위 미확정과 AML ①의 속력 단순 합산 불가 한계 등 Astra payload를 그대로 보존했다.
- queue 3,634건·processed 3,634건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 207 groups·805 cases, META65 이후 2 groups·7 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 1회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G247**이다. G246 induction 반영과 pending 0 검증을 마쳤으며 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G245-complete-20260927 -->
## Luna 역할 sync — G245 전체 단계·귀납 반영 완료·G246 frontier

- G245 AMF/AMG/AMH의 blind·answer_check·independent_code·sdss_compare raw 12건과 `G245-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 미확정 상태는 Astra raw 그대로 보존했다.
- queue 3,617건·processed 3,617건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 206 groups·801 cases, META65 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 1회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G246**이다. G245 induction 반영과 pending 0 검증을 마쳤으며 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:META65-G245-frontier-20260927 -->
## Luna 역할 sync — G244 귀납·META65 반영 완료·G245 frontier

- G244 AMC/AMD/AME의 stage raw 12건과 `G244-induction-20260927-01`, `META65-meta_induction-20260927-01` raw를 기존 스크립트로 의미 변경 없이 반영했다. Astra의 후보와 미확정 지위를 보존했다.
- queue 3,604건·processed 3,604건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 205 groups·798 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 1회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G245**이다. induction·META65 raw 모두 처리되었고 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G243-complete-20260927 -->
## Luna 역할 sync — G243 전체 단계·귀납 반영 완료·G244 frontier

- G243 AMA/AMB의 blind·answer_check·independent_code·sdss_compare raw 8건과 `G243-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 후보 및 미확정 지위는 Astra raw 그대로 보존했다.
- queue 3,590건·processed 3,590건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 204 groups·795 cases, META64 이후 2 groups·5 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 2회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G244**이다. G243 induction 반영과 pending 0 검증을 마쳤으며 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G242-complete-20260927 -->
## Luna 역할 sync — G242 전체 단계·귀납 반영 완료·G243 frontier

- G242 ALX/ALY/ALZ의 blind·answer_check·independent_code·sdss_compare raw 12건과 `G242-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 후보와 미확정 지위는 Astra raw 그대로 보존했다.
- queue 3,581건·processed 3,581건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 203 groups·793 cases, META64 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 2회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G243**이다. G242 induction 반영과 pending 0 검증을 마쳤으며 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:META64-G242-frontier-20260927 -->
## Luna 역할 sync — G241 귀납·META64 반영 완료·G242 frontier

- G241 ALU/ALV/ALW의 stage raw 12건, `G241-induction-20260927-01`, `META64-meta_induction-20260927-01` raw를 기존 스크립트로 의미 변경 없이 반영했다. ALU blind의 경쟁 오답 번호 오기(5)와 answer_check의 실제 경쟁 오답 1 정정 기록도 보존했다.
- queue 3,568건·processed 3,568건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 202 groups·790 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 2회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G242**이다. induction·META64 raw는 모두 처리되었고 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G240-complete-20260927 -->
## Luna 역할 sync — G240 전체 단계·귀납 반영 완료·G241 frontier

- G240 ALR/ALS/ALT의 blind·answer_check·independent_code·sdss_compare raw 12건과 `G240-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 후보·미확정 상태는 Astra raw 그대로 보존했다.
- queue 3,554건·processed 3,554건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 201 groups·787 cases, META63 이후 2 groups·7 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 3회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G241**이다. G240 induction 반영과 pending 0 검증을 마쳤으며 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G239-complete-20260927 -->
## Luna 역할 sync — G239 전체 단계·귀납 반영 완료·G240 frontier

- G239 ALN/ALO/ALP/ALQ의 blind·answer_check·independent_code·sdss_compare raw 16건과 `G239-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 미확정 판정은 Astra raw 그대로 보존했다.
- queue 3,541건·processed 3,541건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 200 groups·784 cases, META63 이후 1 group·4 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 3회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G240**이다. G239 induction 반영과 pending 0 검증을 마쳤으며 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:AUDIT63-backfill-G239-20260927 -->
## Luna 역할 sync — META63 audit·7-case depth_backfill 완료·G239 frontier

- `AUDIT63_BACKFILL-depth_backfill-20260927-01` 7-case raw를 기존 스크립트로 반영했다. 후보의 독립 판정과 공개 후 구분, 미확정 지위 등 Astra payload를 수정하지 않고 보존했다.
- queue 3,524건·processed 3,524건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 199 groups·780 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 3회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- due semantic 단계와 backfill이 해소되어 다음 frontier는 **G239**이다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G237-complete-20260927 -->
## Luna 역할 sync — G237 전체 단계·귀납 반영 완료·G238 frontier

- G237 ALH/ALI/ALJ의 blind·answer_check·independent_code·sdss_compare raw 12건과 `G237-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 후보·대표·미확정 상태는 Astra raw 그대로 보존했다.
- queue 3,508건·processed 3,508건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 198 groups·777 cases, META62 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 1회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G238**이다. G237 induction 반영과 pending 0 검증을 마쳤으며 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G236-complete-20260927 -->
## Luna 역할 sync — G236 전체 단계·귀납 반영 완료·G237 frontier

- G236 ALE/ALF/ALG의 blind·answer_check·independent_code·sdss_compare raw 12건과 `G236-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 미확정 판정은 Astra raw 그대로 보존했다.
- queue 3,495건·processed 3,495건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 197 groups·774 cases, META62 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 1회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G237**이다. G236 induction 반영과 pending 0 검증을 마쳤으며 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:META62-G236-frontier-20260927 -->
## Luna 역할 sync — G235 귀납·META62 반영 완료·G236 frontier

- G235 ALC/ALD의 blind·answer_check·independent_code·sdss_compare raw 8건, `G235-induction-20260927-01`, `META-G233-G234-G235-meta_induction-20260927-62` raw를 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 후보·대표 및 미확정 상태는 Astra raw 그대로 보존했다.
- queue 3,482건·processed 3,482건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 196 groups·771 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 1회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G236**이다. 두 의미 단계의 raw 모두 processed 상태이며 추가 검토 표시는 없다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G234-complete-20260927 -->
## Luna 역할 sync — G234 전체 단계·귀납 반영 완료·G235 frontier

- G234 AKZ/ALA/ALB의 blind·answer_check·independent_code·sdss_compare raw 12건과 `G234-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 후보 미확정 상태는 Astra raw 그대로 보존했다.
- queue 3,472건·processed 3,472건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 195 groups·769 cases, META61 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 2회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G235**이다. G234 induction 반영과 pending 0 검증을 마쳤다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G233-complete-20260927 -->
## Luna 역할 sync — G233 전체 단계·귀납 반영 완료·G234 frontier

- G233 AKW/AKX/AKY의 blind·answer_check·independent_code·sdss_compare raw 12건과 `G233-induction-20260927-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 후보·대표 및 유일성 미확정은 Astra raw 그대로 보존했다.
- queue 3,459건·processed 3,459건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 194 groups·766 cases, META61 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 2회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 준비 frontier는 **G234**이다. G233 induction 반영과 pending 0 검증을 마쳤다.
- quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:META61-G233-frontier-20260927 -->
## Luna 역할 sync — META61 반영 완료·G233 frontier

- `META-G230-G231-G232-meta_induction-20260927-61` raw 1건을 기존 스크립트로 절차 기록과 processed 원장에 의미 변경 없이 반영했다. raw 검토 표시는 없으며 Astra payload를 그대로 보존했다.
- queue 3,446건·processed 3,446건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 193 groups·763 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 2회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G233**이다. quota 상태는 unavailable로 보존한다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G232-stages-induction-20260927 -->
## Luna 역할 sync — G232 전체 단계·귀납 반영, META61 대기

- G232 AKT/AKU/AKV의 blind·answer_check·independent_code·sdss_compare raw 12건과 `G232-induction-20260927-01` raw 1건을 기존 스크립트로 문서 및 processed 원장에 의미 변경 없이 반영했다. primary_candidates·representative_primary·유일성 미확정은 raw대로 보존했으며, 스키마 검토가 필요한 새 G232 기록은 확인되지 않았다.
- queue 3,445건·processed 3,445건·pending raw 0건을 `source_record_id` 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 193 groups·763 cases, META60 이후 3 groups·9 cases, `meta_due=true`, `manual_parity_audit_due=false`, 다음 audit까지 3회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 단계는 Astra의 **META61 `meta_induction`**이다. raw 작성·후처리 sync·pending 0 확인 전 **G233 진입 금지**.
- quota 상태는 unavailable로 보존한다. 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 기계적 sync를 수행했으며 source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G231-induction-20260926 -->
## Luna 역할 sync — G231 귀납 반영·G232 frontier

- `G231-induction-20260926-01` raw 1건을 기존 스크립트로 절차 기록에 의미 변경 없이 반영했다. 원문·최초 판정·후보 미확정 상태를 보존했다.
- queue 3,432건·processed 3,432건·pending raw 0건을 source record ID 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 192 groups·760 cases, META60 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 3회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G232**이다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G231-stages-20260926 -->
## Luna 역할 sync — G231 전체 단계 반영·귀납 대기

- G231 AKQ/AKR/AKS의 blind·answer_check·independent_code·sdss_compare raw 12건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 원문·최초 판정·후보 미확정 상태는 raw 그대로 보존했다.
- queue 3,431건·processed 3,431건·pending raw 0건을 source record ID 기준으로 확인했다. `meta_state.py` 직접 출력 기준 완료 192 groups·760 cases, META60 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- Astra의 G231 induction raw를 기다린다. 반영 후 다음 manifest frontier는 **G232**이다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G230-induction-20260926 -->
## Luna 역할 sync — G230 귀납 반영·G231 frontier

- `G230-induction-20260926-01` raw 1건을 기존 스크립트로 절차 기록에 의미 변경 없이 반영했다. 구조화 후보·대표·미확정 상태는 Astra raw대로 보존했다.
- queue 3,419건·processed 3,419건·pending raw 0건을 source record ID 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 191 groups·757 cases, META60 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 3회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G231**이다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G230-stages-20260926 -->
## Luna 역할 sync — G230 전체 단계 반영·귀납 대기

- G230 AKN/AKO/AKP의 blind·answer_check·independent_code·sdss_compare raw 12건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. 구조화 후보·대표·미확정 항목은 Astra raw 그대로 보존했다.
- queue 3,418건·processed 3,418건·pending raw 0건을 source record ID 기준으로 확인했다. `meta_state.py` 직접 출력 기준 완료 191 groups·757 cases, META60 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- Astra의 G230 induction raw를 기다린다. 반영 후 다음 manifest frontier는 **G231**이다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:META60-depth-backfill-20260926 -->
## Luna 역할 sync — META60 depth_backfill 완료·G230 frontier

- `AUDIT60-fourcases-depth_backfill-20260926-01` 및 `AUDIT60-AKM-depth_backfill-20260926-02` raw 2건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. Astra의 원문 보강과 역할 필드 정렬 판단을 그대로 보존했다.
- queue 3,406건·processed 3,406건·pending raw 0건을 source record ID 기준으로 검증했다. `meta_state.py` 직접 출력: `meta_due=false`, `manual_parity_audit_due=false`, `last_manual_parity_audited_meta_count=60`, 다음 audit까지 3회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- AKM ⓓ 원 PDF 대조 결과는 ‘좌파 야당’으로, 부모가 공식 crop을 직접 확인했다. 영구 crop은 `data/기본기_연구/prepared_backlog/blind_sources/G229_AKM_official_crop_20260926.png`; PDF·페이지·bbox·해시 provenance는 `data/기본기_연구/prepared_backlog/sealed/G229_AKM_official_crop_provenance_20260926.json`에 저장했다.
- depth_backfill 완료 및 pending 0 검증에 따라 다음 frontier는 **G230**이다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. 의미 판단은 생성하지 않았다.

<!-- luna-sync:META60-audit-20260926 -->
## Luna 역할 sync — G229 induction·META60·manual parity audit 반영

- `G229-induction-20260926-01`, `META-G227-G228-G229-meta_induction-20260926-60`, `AUDIT-meta60-manual_parity_audit-20260926-20` raw 3건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다.
- queue 3,404건·processed 3,404건·pending raw 0건을 source record ID 기준으로 검증했다. `meta_state.py` 직접 출력은 `meta_due=false`, `manual_parity_audit_due=false`, `last_manual_parity_audited_meta_count=60`, 다음 audit까지 3회, `depth_backfill_pending=[AKG, AKH, AKJ, AKK, AKM]`, `semantic_state_review=[]`이다.
- Astra가 수행할 depth_backfill 및 필드 정렬 검토가 남아 있어 **G230 진입 금지**.
- AKM ⓓ의 공식 원문 표지는 PDF 인쇄 12쪽, Q24 보기에서 ‘좌파 야당’으로 확인했다. 확인용 crop: `/tmp/g229_akm_q24_choice_d_official_crop.png`. blind source·연구 raw는 수정하지 않았다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. 원문 표지 확인과 기계적 반영 외 의미 재판정은 하지 않았다.

<!-- luna-sync:G229-stages-20260926 -->
## Luna 역할 sync — G229 전체 단계 반영·META60 대기

- G229 AKK/AKL/AKM의 blind·answer_check·independent_code·sdss_compare raw 12건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다.
- AKM blind의 ⓓ 표기 ‘좌파 야당’을 정본 전사와 대조했다. `자료/LEET_언어이해/전사_검수완료/2022/q22-24.md`의 보기 문장도 동일하게 ‘좌파 야당’이다. raw/source 및 연구 원장은 수정하지 않았다.
- queue 3,401건·processed 3,401건·pending raw 0건을 source record ID 기준으로 확인했다. `meta_state.py` 직접 출력 기준 완료 190 groups·754 cases, META59 이후 3 groups·9 cases, `meta_due=true`, `manual_parity_audit_due=false`, 다음 audit까지 1회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- Astra의 G229 induction 및 META60 raw를 기다린다. 후속 sync에서 manual parity audit 상태를 다시 확인하기 전 **G230 진입 금지**.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. 문구 확인 외 source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G228-induction-20260926 -->
## Luna 역할 sync — G228 귀납 반영·G229 frontier

- `G228-induction-20260926-01` raw 1건을 기존 스크립트로 절차 기록에 의미 변경 없이 반영했다. AKJ의 최초 blind ②·확신도 0.9와 공식 ⑤ 불일치 및 주 코드 유일성 미확정은 보존되어 있다.
- queue 3,389건·processed 3,389건·pending raw 0건을 source record ID 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 189 groups·751 cases, META59 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 1회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G229**이다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G228-stages-20260926 -->
## Luna 역할 sync — G228 전체 단계 반영·귀납 대기

- G228 AKH/AKI/AKJ의 4단계 raw 12건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다.
- AKJ는 blind 답 ②·확신도 0.9와 공식 답 ⑤의 불일치를 보존했다. 최초 선택·추론 기록을 덮어쓰지 않고 정답 대조 후 교정과 구별한다. 주 코드 유일성 미확정도 유지한다.
- queue 3,388건·processed 3,388건·pending raw 0건을 source record ID 기준으로 확인했다. `meta_state.py` 직접 출력 기준 완료 189 groups·751 cases, META59 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- Astra의 G228 induction raw를 대기한다. 반영 후 다음 manifest frontier로 이동한다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G227-induction-20260926 -->
## Luna 역할 sync — G227 귀납 반영·G228 frontier

- `G227-induction-20260926-01` raw 1건을 기존 스크립트로 절차 기록에 의미 변경 없이 반영했다.
- queue 3,376건·processed 3,376건·pending raw 0건을 source record ID 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 188 groups·748 cases, META59 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 1회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G228**이다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G227-stages-20260926 -->
## Luna 역할 sync — G227 전체 단계 반영·귀납 대기

- G227 AKE/AKF/AKG의 blind·answer_check·independent_code·sdss_compare raw 12건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다.
- queue 3,375건·processed 3,375건·pending raw 0건을 source record ID 기준으로 확인했다. `meta_state.py` 직접 출력 기준 완료 188 groups·748 cases, META59 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- Astra의 G227 induction raw를 대기한다. induction 반영 및 pending 0 검증 뒤 다음 manifest frontier는 **G228**이다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:META59-G226-20260926 -->
## Luna 역할 sync — G226 귀납·META59 반영·G227 frontier

- `G226-induction-20260926-01` 및 `META-G224-G225-G226-meta_induction-20260926-59` raw 2건을 기존 스크립트로 절차 기록에 의미 변경 없이 반영했다. 원 판단과 미확정 주 후보를 그대로 보존했다.
- queue 3,363건·processed 3,363건·pending raw 0건을 source record ID 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 187 groups·745 cases, META59 이후 0 groups·0 cases, `meta_due=false`, `manual_parity_audit_due=false`, 다음 audit까지 1회, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 **G227**이다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G226-stages-20260926 -->
## Luna 역할 sync — G226 전체 단계 반영·META59 due

- G226 AKB/AKC/AKD의 blind·answer_check·independent_code·sdss_compare raw 12건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다.
- queue 3,361건·processed 3,361건·pending raw 0건을 source record ID 기준으로 확인했다. `meta_state.py` 직접 출력 기준 완료 187 groups·745 cases, META58 이후 3 groups·9 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- Astra의 **G226 induction 및 META59 raw**를 대기한다. 귀납·META59 반영과 pending 0 검증 전 **G227 진입 금지**.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G225-complete-20260926 -->
## Luna 역할 sync — G225 전체 단계·귀납 반영·G226 frontier

- G225 AJY/AJZ/AKA의 4단계 raw 11건과 `G225-induction-20260926-01` raw 1건을 기존 스크립트로 문서 및 processed 원장에 의미 변경 없이 반영했다.
- queue 3,349건·processed 3,349건·pending raw 0건을 source record ID 기준으로 검증했다. `meta_state.py` 직접 출력 기준 완료 186 groups·742 cases, last meta 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 manifest 순서의 **G226**이다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. source/sealed 열람이나 의미 재판정은 하지 않았다.

<!-- luna-sync:G224-sdss-20260926 -->
## Luna 역할 sync — G224 SDSS·귀납 반영·G225 frontier

- G224 AJV~AJX의 `sdss_compare` raw 3건과 `G224-induction-20260926-01` raw 1건을 기존 스크립트로 문서와 processed 원장에 의미 변경 없이 반영했다. SDSS 비교의 독립 판정, 제3자 후보 차이, 미해결 경계와 귀납 결과를 모두 원문대로 보존했다.
- 후속으로 도착한 G225 AJY blind raw 1건도 기계적으로 반영했다. `meta_state.py` 동기화 결과 완료 185 groups·739 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. queue 3,337건·processed 3,337건·pending raw 0건을 source record ID 대조로 검증했다. AJY raw만으로 G225 완료나 답 확인을 추론하지 않는다.
- 다음 frontier는 **G225 AJY부터**다.
- 지정 모델 `gpt-5.6-luna`는 현재 제공되지 않아 사용 가능한 `gpt-6-luna`로 Luna의 기계적 sync 역할을 수행했다. blind/sealed 자료를 열람하거나 의미 판단을 생성하지 않았다.

<!-- luna-sync:G224-raw-recovery-20260926 -->
## Luna 자동 인수인계 — G224 AJV~AJX 미처리 raw 9건 반영

- queue 3,332건·processed 3,332건·pending raw 0건. AJV~AJX의 blind 3건, answer_check 3건, independent_code 3건을 기존 사례 문서에 Astra raw 의미 변경 없이 반영했다.
- G224는 independent_code까지 완료되었고 SDSS 공개·대조는 아직 시작하지 않았다. 같은 group의 SDSS stage barrier를 유지하며, G224 완료 group으로 계수하거나 다음 semantic stage를 추론하지 않는다.
- `meta_state.py` 동기화 결과 `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 완료 집계는 184 groups·736 cases로 유지한다.
- prepared backlog는 821건 중 `consumed_sdss` 736건, `consumed_independent_code` 3건, `prepared` 82건이다. G024 DR~DU hold 4건을 제외한 실행 가능 prepared는 78건이며, 최소 threshold 미만이 아니므로 후보 추가 준비는 하지 않았다.
- 다음 Excel-style case ID는 **AJY**이다. `verify_prepared_backlog.py`의 전체 저장소 경고(`source_extra_keys`, `source_provenance_not_anonymous`)는 기존 자산에 남아 있으며 이번 G224 처리로 새로 의미 판단하거나 수정하지 않았다.

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

<!-- luna-sync:G221-final-20260921-54 -->
## Luna 자동 인수인계 — G221 전체 반영·G203~G221 barrier 최종 점검

- AJL~AJO의 blind·answer_check·independent_code·sdss_compare 16 raw와 `G221-induction-20260921-01` raw 1건을 기존 스크립트로 원문 의미 변경 없이 반영했다. G221 induction을 포함한 최종 queue 상태를 확정했다.
- queue 3,295건·processed 3,295건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 182 groups·730 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=57`, `last_manual_parity_audited_meta_count=57`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 730건·`prepared` 4건이다. prepared 4건은 G024 DR~DU hold이며 실행 가능한 READY는 0건이다. 현재 준비 목록 소진 상태를 100코드 연구 완료로 표현하지 않는다.
- G203~G221 19 groups·67 cases를 queue/manifest로 기계 점검한 결과, 모든 case의 최종 유효 blind와 independent_code record가 존재했다(각 barrier 누락 0건). 과거 hold marker(AIC·AIN·AIR·AIW)는 후속 유효 stage와 함께 보존했다.
- 다음 작업은 새 canonical source 준비와 미확정 경계 반례 확보다. 기존 G024 hold와 미확정 판정은 보존한다.

<!-- luna-sync:AUDIT57-BACKFILL-20260921-53 -->
## Luna 자동 인수인계 — META57 four-case depth_backfill 완료·G221 frontier

- `AUDIT57-fourcases-depth_backfill-20260921-01` raw 1건을 원문 의미 변경 없이 반영했다. AIR 19 철회와 후보 44·10/작업 대표 44, AIT 42 보조, AIN 5 보조·46 특정 오답, AIU 부정·범위 분리 내용을 raw 그대로 보존했다.
- queue 3,278건·processed 3,278건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- depth_backfill이 완료되어 다음 frontier는 마지막 준비 group **G221 AJL~AJO**이다.

<!-- luna-sync:AUDIT57-20260921-52 -->
## Luna 자동 인수인계 — META57 manual parity audit 반영·4-case depth hold

- `AUDIT-meta57-manual_parity_audit-20260921-19` raw 1건을 원문 의미 변경 없이 반영했다. 최초 raw와 기존 후보·대표 구조는 보존하고 semantic 판단을 생성하지 않았다.
- queue 3,277건·processed 3,277건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `last_manual_parity_audited_meta_count=57`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=["AIN", "AIR", "AIT", "AIU"]`, `semantic_state_review=[]`이다.
- 부모 Astra의 4-case 원문 보강 raw 도착 전 G221 AJL~AJO를 시작하지 않는다.

<!-- luna-sync:G220-20260921-51 -->
## Luna 자동 인수인계 — G220 4단계 반영·META57 due·G221 hold

- AJH~AJK의 blind·answer_check·independent_code·sdss_compare 16 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. 후보·대표 구조를 raw 그대로 보존했다.
- `G220-induction-20260921-01`과 `META-G218-G219-G220-meta_induction-20260921-57` raw 2건도 완료 상태로 반영했다. queue 3,276건·processed 3,276건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 181 groups·726 cases, `meta_due=false`, `manual_parity_audit_due=true`, `meta_induction_count=57`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 726건·`prepared` 8건이다. G220 AJH~AJK는 `consumed_sdss`로 기계 갱신했으며 G221 AJL~AJO prepared 상태를 보존했다.
- 다음 허용 단계는 부모 Astra의 META57 manual parity audit과 필요 depth_backfill이다. audit/backfill/sync 완료 전 G221 AJL~AJO를 시작하지 않는다.

<!-- luna-sync:G219-20260921-50 -->
## Luna 자동 인수인계 — G219 4단계 반영·G220 frontier

- AJC~AJG의 blind·answer_check·independent_code·sdss_compare 20 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. 후보·대표 구조를 raw 그대로 보존했다.
- `G219-induction-20260921-01` raw 1건도 Astra 완료 상태로 반영했다. queue 3,258건·processed 3,258건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 180 groups·722 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=56`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 722건·`prepared` 12건이다. G219 AJC~AJG는 `consumed_sdss`로 기계 갱신했으며 G220 AJH~AJK crop 사전 준비와 부모 확인 대기는 보존했다.
- 현재 다음 prepared frontier는 **G220 AJH~AJK**이다. G219 induction은 완료 상태이며 G220 범위 확인은 부모 Astra 지시에 따른다.

<!-- luna-sync:G218-20260921-49 -->
## Luna 자동 인수인계 — G218 4단계 반영·G219 frontier

- AIY~AJB의 blind·answer_check·independent_code·sdss_compare 16 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. 후보·대표 구조와 사전노출 한계를 raw 그대로 보존했다.
- `G218-induction-20260921-01` raw 1건도 Astra 완료 상태로 반영했다. queue 3,237건·processed 3,237건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 179 groups·717 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=56`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 717건·`prepared` 17건이다. G218 AIY~AJB는 `consumed_sdss`로 기계 갱신했으며, G024 DR~DU hold와 다른 prepared 상태는 보존했다.
- 현재 다음 prepared frontier는 **G219 AJC~AJG**이다. G218 induction은 완료 상태이며 다음 group semantic stage는 부모 Astra 지시에 따른다.

<!-- luna-sync:G216-final-20260921-48 -->
## Luna 자동 인수인계 — G216 AIW 범위 해소·META56 due

- AIW 범위 해소 후 blind 1건, AIV·AIW answer_check·independent_code·sdss_compare 6건을 기존 스크립트로 원문 의미 변경 없이 반영했다.
- `G216-induction-20260921-01`과 `META-G215-G217-G216-meta_induction-20260921-56` raw 2건도 완료 상태로 반영했다. queue 3,220건·processed 3,220건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 178 groups·713 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=56`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 713건·`prepared` 21건이다. G216 AIV·AIW는 `consumed_sdss`로 기계 갱신했으며 G217 완료 상태는 유지했다.
- META56 due가 해소되어 다음 frontier는 **G218 AIY~AJB**이다. manifest prepared 21건 중 G024 DR~DU hold 4건을 제외한 실행 가능 사례는 17건이다.

<!-- luna-sync:G217-20260921-47 -->
## Luna 자동 인수인계 — G217 AIX 완료·G216 AIW 재개 선행

- AIX의 blind·answer_check·independent_code·sdss_compare 4 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다.
- `G217-induction-20260921-01` raw 1건도 Astra 완료 상태로 반영했다. queue 3,211건·processed 3,211건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 177 groups·711 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- G217 induction은 완료 상태이며, AIW crop 도착에 따라 부모 Astra가 G216을 먼저 재개한다. G215·G217 기준 2 groups·7 cases 누적이며 G216 완료 시 META56 due 예정이다.

<!-- luna-sync:G216-hold-20260921-46 -->
## Luna 자동 인수인계 — G216 partial blind·AIW hold 반영

- AIV blind 1건과 AIW `hold` 1건을 기존 스크립트로 원문 의미 변경 없이 반영했다. 범위 복원 전 G216 전체 answer/SDSS 봉인과 완료 계수 제외를 보존했다.
- queue 3,206건·processed 3,206건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 176 groups·710 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- G215 6 cases 완료 이후 G216 범위 복원 및 G217 AIX prepared의 병행 가능 여부는 부모 Astra가 meta 상태를 확인해 결정한다. G216은 전체 완료 group으로 계수하지 않는다.

<!-- luna-sync:G215-final-20260921-45 -->
## Luna 자동 인수인계 — G215 AIR scope 해소·20 raw 반영

- AIR scope 해소 후 blind 1건, answer_check·independent_code·sdss_compare 18건, AIQ boundary_revision 1건을 기존 스크립트로 원문 의미 변경 없이 반영했다. AIQ 초기 `46`에서 `[]`로 바뀐 전후 정정 raw와 후보 `[46,17]`, 작업 대표 `46`의 구별을 보존했다.
- `G215-induction-20260921-01` raw 1건도 Astra 완료 상태로 반영했다. queue 3,204건·processed 3,204건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 176 groups·710 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 710건·`prepared` 24건이다. G215 AIP~AIU는 기계 상태를 갱신했으며, 다른 prepared와 G024 DR~DU hold는 보존했다.
- 현재 다음 prepared frontier는 **G216 AIV~AIW**이다. G215 induction은 완료 상태이며 다음 group semantic stage는 부모 Astra 지시에 따른다.

<!-- luna-sync:G214-final-20260921-44 -->
## Luna 자동 인수인계 — G214 AIN hold 해소·META55 due

- AIN crop 직접 확인 후 blind 1건과 AIL·AIM·AIN·AIO의 answer_check·independent_code·sdss_compare 12건을 기존 스크립트로 원문 의미 변경 없이 반영했다. AIN `resolved_hold`와 전체 barrier를 보존했다.
- `G214-induction-20260921-01`과 `META-G211-G213-G214-meta_induction-20260921-55` raw 2건도 완료 상태로 반영했다. queue 3,183건·processed 3,183건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 175 groups·704 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=55`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 704건·`prepared` 30건이다. G214 AIL~AIO는 `consumed_sdss`로 기계 갱신했으며 G215 AIR crop 도착은 META55 이후 재개 상태로 보존한다.
- META55 due가 해소되어 다음 frontier **G215 AIR 범위 crop 직접 확인**부터 후속 semantic stage를 재개할 수 있다.

<!-- luna-sync:G215-hold-20260921-43 -->
## Luna 자동 인수인계 — G215 blind 일부·AIR hold 반영

- AIP·AIQ·AIS·AIT·AIU blind 5건과 AIR `hold` 1건을 기존 스크립트로 원문 의미 변경 없이 반영했다. AIR [A]~[C] 범위 기계 복원 요청, G215 전체 answer/SDSS 봉인, 완료 계수 제외를 보존했다.
- queue 3,168건·processed 3,168건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 174 groups·700 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- G214 AIN crop 도착은 부모가 G214를 먼저 마감할 선행 상태로 유지한다. G215는 전체 완료 group으로 계수하지 않는다.

<!-- luna-sync:G214-hold-20260921-42 -->
## Luna 자동 인수인계 — G214 blind 일부·AIN hold 반영

- AIL·AIM·AIO blind 3건과 AIN `hold` 1건을 기존 스크립트로 원문 의미 변경 없이 반영했다. 원문 [A]~[F] 범위 crop 복원 대기, G214 전체 answer/SDSS 봉인을 보존했다.
- queue 3,162건·processed 3,162건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 174 groups·700 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. G214는 완료 group으로 계수하지 않았다.
- G211·G213 완료로 META55까지 2 groups·8 questions가 누적되었으며, G214 전체 완료 시 META55 due가 된다. 부모 source 복원 전 G214 후속 answer/SDSS를 시작하지 않는다.

<!-- luna-sync:G213-20260921-41 -->
## Luna 자동 인수인계 — G213 4단계 반영·G214 frontier

- AIH~AIK의 blind·answer_check·independent_code·sdss_compare 16 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. 후보·작업 대표 구조와 group SDSS barrier를 보존했다.
- `G213-induction-20260921-01` raw 1건도 Astra 완료 상태로 반영했다. queue 3,158건·processed 3,158건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 174 groups·700 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=54`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 700건·`prepared` 34건이다. G213 AIH~AIK는 `consumed_sdss`로 기계 갱신했으며, 다른 prepared와 G024 DR~DU hold는 보존했다.
- 현재 다음 prepared frontier는 **G214 AIL~AIO**이다. G213 induction은 완료 상태이며 다음 group semantic stage는 부모 Astra 지시에 따른다.

<!-- luna-sync:G211-AIC-20260921-40 -->
## Luna 자동 인수인계 — G211 AIC hold 해소·전체 4문항 완료

- AIC 유효 blind 1건과 AIA~AID의 answer_check·independent_code·sdss_compare 12건을 기존 스크립트로 원문 의미 변경 없이 반영했다. AIC의 `resolved_hold_record`와 전체 group barrier, 기존 후보·대표 구조를 보존했다.
- `G211-induction-20260921-01` raw 1건도 Astra 완료 상태로 반영했다. queue 3,141건·processed 3,141건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 173 groups·696 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 696건·`prepared` 38건이다. G211 AIA~AID는 `consumed_sdss`로 기계 갱신했으며 AIC hold 해소를 반영했다. semantic review 잔여는 없다.
- 다음 미완료 frontier는 **G213 AIH~AIK**이다. G211 induction은 완료 상태이며 source 표제 노출 한계는 별도로 보존한다.

<!-- luna-sync:AUDIT54-BACKFILL-20260921-39 -->
## Luna 자동 인수인계 — META54 seven-case depth_backfill 완료·G211 재개

- `AUDIT54-sevencases-depth_backfill-20260921-01` raw 1건을 원문 의미 변경 없이 반영하고 AHF·AHG·AHJ·AHM·AHQ·AHX·AIF case 문서에 연결했다. 최초 primary와 기존 후보·대표 구조는 보존했다.
- queue 3,127건·processed 3,127건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- depth_backfill이 완료되어 부모 Astra는 G211 AIC crop 직접 확인부터 연구를 재개할 수 있다.

<!-- luna-sync:AUDIT54-20260921-38 -->
## Luna 자동 인수인계 — META54 manual parity audit 반영·7-case depth hold

- `AUDIT-meta54-manual_parity_audit-20260921-18` raw 1건을 원문 의미 변경 없이 반영했다. 최초 primary와 기존 후보·대표 구조는 보존하고, 의미 수정 판정은 수행하지 않았다.
- queue 3,126건·processed 3,126건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 172 groups·692 cases, `meta_due=false`, `manual_parity_audit_due=false`, `last_manual_parity_audited_meta_count=54`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=["AHF", "AHG", "AHJ", "AHM", "AHQ", "AHX", "AIF"]`, `semantic_state_review=[]`이다.
- 부모 Astra가 지정 7개 case의 원문 직접 검토와 보강 raw를 작성 중이다. depth_backfill 완료 전 G211 AIC 재개 및 다음 semantic stage는 hold로 유지한다.

<!-- luna-sync:G212-20260921-37 -->
## Luna 자동 인수인계 — G212 4단계 반영·META54 due

- AIE~AIG의 blind·answer_check·independent_code·sdss_compare 12 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. 후보·작업 대표 구조와 AIU/AJK v2 파생 경로 보존 상태를 건드리지 않았다.
- `G212-induction-20260921-01`과 `META-G209-G210-G212-meta_induction-20260921-54` raw 2건도 완료 상태로 반영했다. queue 3,125건·processed 3,125건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 172 groups·692 cases, `meta_due=false`, `manual_parity_audit_due=true`, `meta_induction_count=54`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. G211 AIC hold는 완료 group으로 계수하지 않았다.
- manifest는 총 734건 중 `consumed_sdss` 692건·`prepared` 42건이다. G212 AIE~AIG는 `consumed_sdss`로 기계 갱신했으며 G211 prepared/hold와 다른 prepared는 보존했다.
- 다음 허용 단계는 부모 Astra의 META54 manual parity audit과 필요 depth_backfill이다. G211 AIC 복원은 audit/backfill/sync 완료 전 재개하지 않으며, audit 후 G211을 다음 frontier로 보존한다. G213 AIH~AIK는 prepared 상태로 유지한다.

<!-- luna-sync:G211-hold-20260921-36 -->
## Luna 자동 인수인계 — G211 blind 일부·AIC hold 반영

- AIA·AIB·AID blind 3건과 AIC `hold` 1건을 기존 스크립트로 원문 의미 변경 없이 반영했다. AIC의 A/B 범위 복원 대기, G211 전체 answer/SDSS 봉인, AID ⑤ 말미 편집 표제 노출에 따른 strict 한계를 보존했다.
- queue 3,111건·processed 3,111건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 171 groups·689 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=53`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. G211은 전체 완료 group으로 계수하지 않았다.
- manifest는 총 734건 중 `consumed_sdss` 689건·`prepared` 45건이다. G211 AIA~AID의 prepared 상태와 AIC hold를 보존했다. G212 AIE~AIG 등 미사용 prepared는 유지하며 G211 마감 전 META54 여부를 확정하지 않는다.

<!-- luna-sync:G210-20260921-35 -->
## Luna 자동 인수인계 — G210 4단계 반영·G211 frontier

- AHZ 유일 case의 blind·answer_check·independent_code·sdss_compare 4 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. 원문 경로 파생본과 후보·대표 구조를 보존했다.
- `G210-induction-20260921-01` raw 1건도 Astra 완료 상태로 반영했다. queue 3,107건·processed 3,107건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 171 groups·689 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=53`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 689건·`prepared` 45건이다. G210 AHZ는 `consumed_sdss`로 기계 갱신했으며, 다른 prepared와 G024 DR~DU hold는 보존했다.
- 현재 다음 prepared frontier는 **G211 AIA~AID**이다. G210 induction은 완료 상태이며 다음 group semantic stage는 부모 Astra 지시에 따른다. META54는 G211 완료 시점 due 예정이다.

<!-- luna-sync:G209-20260921-34 -->
## Luna 자동 인수인계 — G209 4단계 반영·G210 frontier

- AHW~AHY의 blind·answer_check·independent_code·sdss_compare 12 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. source 표제·작품 친숙성으로 strict 무오염을 주장하지 않는다는 기록과 candidate ID는 있으나 site code가 빈 배열이라 비교할 수 없다는 한계를 보존했다.
- `G209-induction-20260921-01` raw 1건도 Astra 완료 상태로 반영했다. queue 3,102건·processed 3,102건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 170 groups·688 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=53`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 688건·`prepared` 46건이다. G209 AHW~AHY는 `consumed_sdss`로 기계 갱신했으며, G210~G221의 부가 편집 표제 제거 파생본에 따른 manifest·packet·blind_source 경로 변경은 보존했다.
- 현재 다음 prepared frontier는 **G210 AHZ**이다. G209 induction은 완료 상태이며 다음 group semantic stage는 부모 Astra 지시에 따른다.

<!-- luna-sync:G208-20260921-33 -->
## Luna 자동 인수인계 — G208 4단계 반영·META53 due·G209 hold

- AHS~AHV의 blind·answer_check·independent_code·sdss_compare 16 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. 후보·작업 대표 구조와 공식답의 기계 연결 한계를 raw 그대로 보존했다.
- `G208-induction-20260921-01`과 `META-G206-G207-G208-meta_induction-20260921-53` raw 2건도 완료 상태로 반영했다. queue 3,089건·processed 3,089건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 169 groups·685 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=53`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. META54 audit carryover는 보존했다.
- manifest는 총 734건 중 `consumed_sdss` 685건·`prepared` 49건이다. G208 AHS~AHV는 `consumed_sdss`로 기계 갱신했으며, 다른 prepared와 G024 DR~DU hold는 보존했다.
- META53 due가 해소되어 다음 prepared frontier **G209 AHW~AHY**의 semantic stage를 시작할 수 있다.

<!-- luna-sync:G207-20260921-32 -->
## Luna 자동 인수인계 — G207 4단계 반영·G208 frontier

- AHO~AHR의 blind·answer_check·independent_code·sdss_compare 16 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. AHR의 공식 PDF 그림 직접 확인과 공식답 canonical 기계 연결의 구별, 빈 `primary`, 후보·작업 대표 구조를 raw 그대로 보존했다.
- `G207-induction-20260921-01` raw 1건도 Astra 완료 상태로 반영했다. queue 3,071건·processed 3,071건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 168 groups·681 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=52`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 681건·`prepared` 53건이다. G207 AHO~AHR은 `consumed_sdss`로 기계 갱신했으며, 다른 prepared와 G024 DR~DU hold는 보존했다.
- 현재 다음 prepared frontier는 **G208 AHS~AHV**이다. G207 induction은 완료 상태이며 다음 group semantic stage는 부모 Astra 지시에 따른다.

<!-- luna-sync:G206-20260921-31 -->
## Luna 자동 인수인계 — G206 4단계 반영·G207 frontier

- AHL~AHN의 blind·answer_check·independent_code·sdss_compare 12 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. 빈 `primary`, 후보·작업 대표 구조와 공식답의 기계 연결 한계를 raw 그대로 보존했다.
- `G206-induction-20260921-01` raw 1건도 Astra 완료 상태로 반영했다. queue 3,054건·processed 3,054건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 167 groups·677 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=52`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 677건·`prepared` 57건이다. G206 AHL~AHN은 `consumed_sdss`로 기계 갱신했으며, 다른 prepared와 G024 DR~DU hold는 보존했다. G206 induction도 완료 raw로 반영했다.
- 현재 다음 prepared frontier는 **G207 AHO~AHR**이다. G206 induction과 다음 group semantic stage는 부모 Astra 지시에 따른다.

<!-- luna-sync:G205-20260921-30 -->
## Luna 자동 인수인계 — G205 전체 반영·META52 해소·G206 frontier

- AHH~AHK의 blind·answer_check·independent_code·sdss_compare 16 raw를 기존 스크립트로 원문 의미 변경 없이 반영했다. 빈 `primary`, 후보·작업 대표 구조와 공식답의 기계 연결 한계를 raw 그대로 보존했다.
- `G205-induction-20260921-01`과 `META-G203-G204-G205-meta_induction-20260921-52` raw 2건도 완료 상태로 반영했다. queue 3,041건·processed 3,041건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 166 groups·674 cases, `meta_due=false`, `manual_parity_audit_due=false`, `meta_induction_count=52`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 674건·`prepared` 60건이다. G205 AHH~AHK는 `consumed_sdss`로 기계 갱신했으며, 다른 prepared와 G024 DR~DU hold는 보존했다.
- META52 due가 해소되어 다음 prepared frontier **G206 AHL~AHN**의 semantic stage를 시작할 수 있다.

<!-- luna-sync:G204-20260921-29 -->
## Luna 자동 인수인계 — G204 전체 단계·induction 반영·G205 frontier

- AHD~AHG의 blind·answer_check·independent_code·sdss_compare 16 raw와 `G204-induction-20260921-01` raw 1건을 기존 스크립트로 원문 의미 변경 없이 반영했다. 빈 `primary`, 후보·작업 대표 구조와 공식답의 기계 연결 한계는 raw 그대로 보존했다.
- queue 3,023건·processed 3,023건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 165 groups·670 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 670건·`prepared` 64건이다. G204 AHD~AHG는 `consumed_sdss`로 기계 갱신했으며, 다른 prepared와 G024 DR~DU hold는 보존했다. G204 induction도 Astra 완료 raw로 반영했다.
- 현재 다음 Excel-style frontier는 **G205 AHH~AHK**이다. 다음 group semantic stage는 부모 Astra 지시에 따른다.

<!-- luna-sync:G203-20260921-28 -->
## Luna 자동 인수인계 — G203 raw 13건 반영·G204 frontier

- `AHA~AHC`의 blind·answer_check·independent_code·sdss_compare 12건과 `G203-induction-20260921-01` raw 1건을 기존 스크립트로 원문 의미 변경 없이 반영했다. 최초 raw의 빈 `primary`, 후보·작업 대표 구조, 공식답의 canonical 기계 연결과 직접 정답표 미검증 한계를 보존했다.
- queue 3,006건·processed 3,006건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 164 groups·666 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 734건 중 `consumed_sdss` 666건·`prepared` 68건이다. G203 AHA~AHC는 기계적으로 `consumed_sdss`로 갱신했으며 G024 DR~DU hold는 유지한다. `G203-induction-20260921-01`은 Astra 완료 판단(`stage=induction`, `status=done`)으로 raw·processed 반영을 완료했다.
- 현재 다음 Excel-style frontier는 **G204 AHD~AHG**이다. G203 induction은 완료 상태이며, 다음 group semantic stage는 부모 지시에 따른다.

<!-- luna-preflight:20260920-G203-corpus-exhausted -->
## Luna frontier preflight — 2026-09-20

- 시작 frontier는 G203이었다. canonical passage 163개를 기계 대조한 결과 미사용 passage가 0개여서 추가로 검사할 passage group은 0개, 새 READY/NEEDS_RESTORE/UNRESOLVED도 0개였다.
- manifest는 667건( consumed_sdss 663건·prepared 4건 )이며 prepared 4건은 기존 G024 DR~DU SDSS 사전노출 barrier hold다. actionable READY는 0건이고 첫 Astra READY group도 없다.
- SDSS linkage 연결·미연결 신규 case는 각각 0건이다. 복원한 visual/source asset은 없다. 다음 preparation frontier는 G203 이후이며 새 canonical source 확보 전까지 준비할 수 없다.
- 이 preflight는 기계적 corpus preparation만 수행했으며 semantic research·정답 추론·코드 판정을 수행하지 않았다. queue/processed/meta_state는 작업 전후 동일하고, CURRENT만 이번 결과 기록을 위해 갱신했다.

<!-- luna-sync:AUDIT51-BACKFILL-20260920-27 -->
## Luna 자동 인수인계 — META51 grouped depth_backfill 완료·현재 코퍼스 소진 checkpoint

- `AUDIT51-sixcases-depth_backfill-20260920-01` grouped raw 1건을 원문 의미 변경 없이 절차 기록과 AFQ·AGT·AGC·AFV·AGW·AGJ 각 case 문서에 연결했다. 최초 raw와 다섯 사례의 빈 revised_primary·후보/대표 구조, AGJ 63 유지 및 65/62/4 역할을 보존했다.
- queue 2,993건·processed 2,993건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 163 groups·663 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest prepared 4건은 G024 DR~DU의 SDSS 사전노출 barrier hold이며 actionable은 0건이다. canonical passages 163개는 모두 연결되었고 미사용 0 상태를 보존한다.
- 이번 연구 window는 queue 2,750건에서 2,993건으로 243건 증가했으며 11 groups·57 cases 완료(신규 직접 blind 47, 기존 후속 10)로 기록한다. G193/G168 strict 제외와 공식 답 기계 연결 한계를 유지한다.
- quota helper는 모두 unavailable이었고 runtime emergency 경고는 관측되지 않았다. 현재 상태는 quota 종료가 아니라 기존 준비 가능 코퍼스 소진에 따른 작업 정리다. 전체 100코드 연구 완료로 표현하지 않으며, 다음 필요 작업은 새 정본 준비와 기존 미확정 경계 반례 확보다.

<!-- luna-sync:AUDIT51-20260920-26 -->
## Luna 자동 인수인계 — META51 manual parity audit 반영

- `AUDIT-meta51-manual_parity_audit-20260920-17` raw 1건을 원문 의미 변경 없이 반영했다. AGE 23 유지 근거와 AGJ 원문 단초·강도 gap을 보존했다.
- queue 2,992건·processed 2,992건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 163 groups·663 cases, `meta_due=false`, `manual_parity_audit_due=false`, `last_manual_parity_audited_meta_count=51`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=["AFQ", "AFV", "AGC", "AGJ", "AGT", "AGW"]`, `semantic_state_review=[]`이다.
- Astra의 grouped depth_backfill 6-case 의미 보강을 대기 중이며 depth 완료 전 최종 상태로 승격하지 않는다.

<!-- luna-sync:META51-20260920-25 -->
## Luna 자동 인수인계 — G202 induction·META51 반영

- `G202-induction-20260920-01`과 `META-G199-G200-G202-meta_induction-20260920-51` raw 2건을 원문 의미 변경 없이 반영했다. META51 audit 대상인 AGJ 원문 단서·강도 및 carryover를 보존했고, corpus 현재 준비 가능·미사용 0 상태와 G024 hold를 유지했다.
- queue 2,991건·processed 2,991건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 163 groups·663 cases, `meta_induction_count=51`, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 다음 단계는 Astra META51 manual parity audit이다.
- manifest는 총 667건 중 `consumed_sdss` 663건·`prepared` 4건이며, 남은 G024 4건은 기존 hold다. source 조회·backlog 준비는 수행하지 않았다.

<!-- luna-sync:G202-20260920-24 -->
## Luna 자동 인수인계 — G202 전체 단계·META51 due

- G202 5문항의 blind·answer_check·independent_code·sdss_compare 20건과 AGW source hold 해소 raw 1건을 원문 의미 변경 없이 반영했다. 2022 예시 문항과 실제 시행 기출의 구별, Orbi 문제지 전재본 원 crop과 공식 배포 호스트 검증의 구별, source qualification을 보존했다.
- queue 2,989건·processed 2,989건이며 `record_id` 기준 pending raw는 0건이다. G202 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 163 groups·663 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=15`, `meta_due=true`, `meta_induction_count=50`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 다음 단계는 META51 induction이며 성급히 종료하지 않는다.
- manifest는 총 667건 중 `consumed_sdss` 663건·`prepared` 4건이다. 남은 G024 4건만 hold이며 actionable READY로 세지 않는다. canonical passages 163개 연결 및 미사용 0 상태는 helper의 기계 결과로 보존하고, 새 source·backlog 준비는 수행하지 않았다.

<!-- luna-sync:G200-induction-20260920-23 -->
## Luna 자동 인수인계 — G200 induction 반영

- `G200-induction-20260920-01` raw 1건을 원문 의미 변경 없이 반영했다. source 조회는 수행하지 않았다.
- queue 2,968건·processed 2,968건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 162 groups·658 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 준비 목록의 마지막 G202 5문항이며, 이후 META51 audit/backfill 절차를 따른다.

<!-- luna-sync:G200-20260920-22 -->
## Luna 자동 인수인계 — G200 전체 단계 반영

- G200 6문항의 blind·answer_check·independent_code·sdss_compare 24건을 원문 의미 변경 없이 반영했다. AGN 63/56 후보, AGM 45/17 후보, AGP 62 충분성 부정과 원문 범위 한계를 보존했다.
- queue 2,967건·processed 2,967건이며 `record_id` 기준 pending raw는 0건이다. G200 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 162 groups·658 cases, `completed_groups_since_last_meta=2`, `completed_questions_since_last_meta=10`, `meta_due=false`, `meta_induction_count=50`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 준비된 G202 5문항이며, source 조회·backlog 준비는 수행하지 않았다.

<!-- luna-sync:G199-induction-20260920-21 -->
## Luna 자동 인수인계 — G199 induction 반영

- `G199-induction-20260920-01` raw 1건을 원문 의미 변경 없이 반영했다. source 조회와 의미 판단은 수행하지 않았다.
- queue 2,943건·processed 2,943건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 161 groups·652 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. G200 시작 전 부모가 이 상태를 재확인한다.

<!-- luna-sync:G199-20260920-20 -->
## Luna 자동 인수인계 — G199 전체 단계 반영

- G199 4문항의 blind·answer_check·independent_code·sdss_compare 16건을 원문 의미 변경 없이 반영했다. AGJ의 63 상위 비판 평가, 65 왜곡 기각, 62 충분성 부정, 4 모든 공포 범위의 역할을 보존했다.
- queue 2,942건·processed 2,942건이며 `record_id` 기준 pending raw는 0건이다. G199 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 161 groups·652 cases, `completed_groups_since_last_meta=1`, `completed_questions_since_last_meta=4`, `meta_due=false`, `meta_induction_count=50`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 준비된 G200 6문항이며, G199 induction과 META51 대상 필드는 보존한다. source 조회·backlog 준비는 수행하지 않았다.

<!-- luna-sync:META50-20260920-19 -->
## Luna 자동 인수인계 — G198 induction·META50 반영

- `G198-induction-20260920-01`과 `META-G196-G197-G198-meta_induction-20260920-50` raw 2건을 원문 의미 변경 없이 반영했다. META51 manual parity audit 대상 필드와 carryover를 보존했다.
- queue 2,926건·processed 2,926건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 160 groups·648 cases, `meta_induction_count=50`, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 다음 연구 frontier는 G199다.
- source 조회·backlog 준비는 수행하지 않았다.

<!-- luna-sync:G198-20260920-18 -->
## Luna 자동 인수인계 — G198 전체 단계·META50 due

- G198 5문항의 blind·answer_check·independent_code·sdss_compare 20건과 AGD source hold 후속 해소 raw 1건을 원문 의미 변경 없이 반영했다. AGF의 `primary=[]` 및 후보 20/10/12, 규범적 정당화 전제를 보존하고 AGG 96/39 후보도 유지했다.
- queue 2,924건·processed 2,924건이며 `record_id` 기준 pending raw는 0건이다. G198 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 160 groups·648 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=16`, `meta_due=true`, `meta_induction_count=49`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 다음 단계는 META50 induction이며, 완료 전 G199를 시작하지 않는다.
- manifest는 총 667건 중 `consumed_sdss` 648건·`prepared` 19건이다. source 조회·backlog 준비는 수행하지 않았다.

<!-- luna-sync:G197-induction-20260920-17 -->
## Luna 자동 인수인계 — G197 induction 반영

- `G197-induction-20260920-01` raw 1건을 원문 의미 변경 없이 반영했다. 신규 source 조회와 의미 판단은 수행하지 않았다.
- queue 2,903건·processed 2,903건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 159 groups·643 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. G198 시작 전 이 상태를 기준으로 재확인한다.

<!-- luna-sync:G197-20260920-16 -->
## Luna 자동 인수인계 — G197 전체 단계 반영

- G197 AFX·AFY·AFZ·AGA·AGB 5문항의 blind·answer_check·independent_code·sdss_compare 20건과 AFY/AFZ source hold 후속 raw 1건을 원문 의미 변경 없이 반영했다. AFY 17/45 후보, AGB 96/39 후보와 근접어 불확실성, AFZ 43/86의 다변수 고정 조건 순위 연결 행동을 보존했다.
- queue 2,902건·processed 2,902건이며 `record_id` 기준 pending raw는 0건이다. G197 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 159 groups·643 cases, `completed_groups_since_last_meta=2`, `completed_questions_since_last_meta=11`, `meta_due=false`, `meta_induction_count=49`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. G198 시작 전 meta 상태를 재확인한다.
- manifest는 총 667건 중 `consumed_sdss` 643건·`prepared` 24건이다. 새 source·answer·SDSS 열람과 backlog 준비는 수행하지 않았다.

<!-- luna-sync:G196-induction-20260920-15 -->
## Luna 자동 인수인계 — G196 induction 반영

- `G196-induction-20260920-01` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록과 processed 원장에 반영했다. 신규 source·answer·SDSS는 읽지 않았다.
- queue 2,881건·processed 2,881건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 158 groups·638 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. G197 blind 진행 중 추가 raw는 차집합만 반영한다.

<!-- luna-sync:G196-20260920-14 -->
## Luna 자동 인수인계 — G196 전체 단계 반영

- G196 AFR~AFW 6문항의 blind·answer_check·independent_code·sdss_compare 24건을 원문 의미 변경 없이 기존 사례 문서와 processed 원장에 반영했다. AFU의 `primary=[]`와 후보 80/17, 긍정 확인과 오답 배제의 대안 경로를 보존했으며 AFR 64/17·AFW 96/39 유보도 유지했다.
- queue 2,880건·processed 2,880건이며 `record_id` 기준 pending raw는 0건이다. G196 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 158 groups·638 cases, `completed_groups_since_last_meta=1`, `completed_questions_since_last_meta=6`, `meta_due=false`, `meta_induction_count=49`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 656건 중 `consumed_sdss` 638건·`prepared` 18건이다. G197/G198 prepared 상태와 다른 Luna의 준비 작업은 보존했으며, 새 source·backlog 준비는 수행하지 않았다.

<!-- luna-sync:META49-20260920-13 -->
## Luna 자동 인수인계 — G195 induction·META49 반영

- `G195-induction-20260920-01`과 `META-G194-G201-G195-meta_induction-20260920-49` raw 2건을 원문 의미 변경 없이 독립연구 진행 기록과 processed 원장에 반영했다. 완료된 blind는 재수행하지 않았다.
- queue 2,856건·processed 2,856건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 157 groups·632 cases, `meta_induction_count=49`, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=2`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 연구 frontier는 G196 AFR 6문항이며, 이후 G197이다. manifest는 총 647건 중 `consumed_sdss` 632건·`prepared` 15건이고, 새 source·backlog 준비는 수행하지 않았다.

<!-- luna-sync:G195-20260920-12 -->
## Luna 자동 인수인계 — G195 전체 단계·META49 due

- G195 AFL~AFQ 6문항의 blind·answer_check·independent_code·sdss_compare와 source hold 후속 crop 해소 raw 등 26건을 원문 의미 변경 없이 기존 사례 문서와 processed 원장에 반영했다. AFM의 15/16 후보, AFP의 44/15 후보 및 원 source 기계 READY의 그림 누락 한계를 보존했다.
- queue 2,854건·processed 2,854건이며 `record_id` 기준 pending raw는 0건이다. G195 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 157 groups·632 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=16`, `meta_due=true`, `meta_induction_count=48`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 다음 단계는 META49 `meta_induction`이며, 완료 전 새 G196 semantic stage를 시작하지 않는다.
- manifest는 총 647건 중 `consumed_sdss` 632건·`prepared` 15건이다. G196/G197 prepared 상태와 다른 Luna의 준비 작업은 보존했으며, 새 source 열람·backlog 재실행은 하지 않았다.

<!-- luna-sync:G201-20260920-11 -->
## Luna 자동 인수인계 — G201 induction 및 frontier hold 확정

- `G201-induction-20260920-01` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록과 processed 원장에 반영했다. queue 2,828건·processed 2,828건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 156 groups·626 cases, `completed_groups_since_last_meta=2`, `completed_questions_since_last_meta=10`, `meta_due=false`, `meta_induction_count=48`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 현재 다음 연구 가능한 actionable READY는 없다. manifest의 prepared 4건(DR·DS·DT·DU, G024)은 SDSS 사전노출 barrier hold이므로 actionable 4건으로 세지 않으며 재독립연구를 시작하지 않는다. G195~G200 자료 연결·복원은 다른 helper가 진행 중이다.

<!-- luna-sync:G194-G201-20260920-10 -->
## Luna 자동 인수인계 — G194·G201 후속 및 induction 반영

- G201 AGR·AGS·AGT·AGU의 independent_code 4건과 sdss_compare 4건, G194 후속 `induction` 1건을 원문 의미 변경 없이 기존 사례 문서·독립연구 진행 기록·processed 원장에 반영했다. AGR·AGU의 `primary=[]`와 후보 구조를 보존했으며 G201 induction은 아직 추가되지 않았다.
- queue 2,827건·processed 2,827건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 156 groups·626 cases, `completed_groups_since_last_meta=2`, `completed_questions_since_last_meta=10`, `meta_due=false`, `meta_induction_count=48`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 630건 중 `consumed_sdss` 626건·`prepared` 4건이다. 새 source·answer·SDSS 열람과 backlog 준비는 수행하지 않았다. G201 induction이 추가되면 별도 sync한다.

<!-- luna-sync:G194-20260920-09 -->
## Luna 자동 인수인계 — G194 전체 단계 및 현재 hold 반영

- G194 AFF·AFG·AFH·AFI·AFJ·AFK의 blind·answer_check·independent_code·sdss_compare 24건과 queue에 함께 들어온 G201 blind/hold raw를 의미 변경 없이 기존 사례 문서와 processed 원장에 기계 반영했다. AFF/AFG의 `primary=[]` 및 후보 구조를 보존했고, G201은 independent_code 미시작·SDSS 봉인 상태를 유지했다.
- queue 2,818건·processed 2,818건이며 `record_id` 기준 pending raw는 0건이다. G194 induction은 아직 추가되지 않았다.
- `meta_state.py`: 완료 155 groups·622 cases, `completed_groups_since_last_meta=1`, `completed_questions_since_last_meta=6`, `meta_due=false`, `meta_induction_count=48`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 630건 중 `consumed_sdss` 622건·`prepared` 8건이다. 신규 자료 연결·backlog 준비는 수행하지 않았다. G194 induction 및 G201 후속은 group barrier에 따라 대기한다.

<!-- luna-sync:AUDIT48-BACKFILL-20260920-08 -->
## Luna 자동 인수인계 — META48 지정 depth_backfill 반영

- `AUDIT48-sixcases-depth_backfill-20260920-01` grouped raw 1건을 원문 의미 변경 없이 절차 기록과 ACP·AFB·AFD·AAF·AAK·AEZ 각 case 문서에 연결했다. 최초 raw는 immutable로 보존했고, revised_primary 빈 배열·후보/대표 구조와 AEZ 조건부 수치 전제를 primary 확정으로 요약하지 않았다.
- 동기화 중 helper가 추가한 G194 AFF·AFG blind raw도 기존 도구로 기계 반영했다. queue 2,784건·processed 2,784건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 154 groups·616 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 630건 중 `consumed_sdss` 616건·`prepared` 14건이다. 새 source·answer·SDSS 열람과 backlog 의미 준비는 수행하지 않았다.

<!-- luna-sync:AUDIT48-sixcases-depth_backfill-20260920-01 -->
## Luna 자동 인수인계 — META48 manual parity audit 반영

- `AUDIT-meta48-manual_parity_audit-20260920-16` raw 1건을 payload 원문 의미 변경 없이 독립연구 진행 기록과 processed 원장에 반영했다. 다중 `case_ids` depth_backfill 지정은 상태 필드로만 기계 반영했으며, 의미 보완은 수행하지 않았다.
- queue 2,781건·processed 2,781건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 154 groups·616 cases, `meta_induction_count=48`, `last_manual_parity_audited_meta_count=48`, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=["AAF", "AAK", "ACP", "AEZ", "AFB", "AFD"]`, `semantic_state_review=[]`이다.
- Astra가 지정된 6개 case의 depth_backfill을 수행 중이며, 완료 전 새 group semantic stage는 시작하지 않는다. 신규 G201 manifest 준비는 다른 helper 영역으로 보존했다.

<!-- luna-sync:META48-20260920-06 -->
## Luna 자동 인수인계 — META48 반영·manual parity audit due

- `META-G181-G193-G168-meta_induction-20260920-48` raw 1건을 payload 원문 의미 변경 없이 독립연구 진행 기록과 processed 원장에 반영했다. 새 source·answer·SDSS 열람과 backlog 준비는 수행하지 않았다.
- queue 2,780건·processed 2,780건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 154 groups·616 cases, `meta_induction_count=48`, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 허용 semantic 단계는 Astra의 META48 manual parity audit이며, 완료 전 새 group을 시작하지 않는다.

<!-- luna-sync:G168-20260920-05 -->
## Luna 자동 인수인계 — G168 후속 단계·META48 due 반영

- G168 AAF·AAG·AAH·AAI·AAJ·AAK의 실제 공식 crop 후속 blind 1건, 전체 answer_check 6건, independent_code 6건, sdss_compare 6건 등 queue 차집합 19건을 원문 의미 변경 없이 기존 사례 문서와 processed 원장에 반영했다. G168의 최초 사전답 노출·strict-blind 제외·최초 hold와 공식 답 직접 대조 미검증 유보를 보존했으며, 최초 답 일치도 strict 성과로 승격하지 않았다.
- queue 2,779건·processed 2,779건이며 `record_id` 기준 pending raw는 0건이다. G168 후속 `induction`까지 반영했으며 추가 차집합은 없다.
- `meta_state.py`: 완료 154 groups·616 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=16`, `meta_due=true`, `meta_induction_count=47`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다. 새 group 시작 전 **META48 `meta_induction`이 due**다.
- manifest는 총 626건 중 `consumed_sdss` 616건·`prepared` 10건이다. 남은 prepared는 G024 DR~DU hold와 새로 기계 준비된 G194 AFF~AFK이며, G194/G201 준비·복원은 다른 helper가 관리한다. Luna는 backlog를 재준비하거나 source·answer·SDSS를 열지 않았다.

<!-- luna-sync:G193-20260920-04 -->
## Luna 자동 인수인계 — G193 전체 단계·induction 후처리 완료

- G193 AFB·AFC·AFD·AFE의 independent_code 4건, sdss_compare 4건 및 후속 `G193-induction-20260920-01` 1건을 queue 원문 의미 변경 없이 기존 사례 문서·독립연구 진행 기록·processed 원장에 반영했다. primary/auxiliary object 배열, 사이트 연결 부재 사전 노출에 따른 strict-blind 제외, 공식 배포 답표 직접 대조 미검증, 기존 유보를 그대로 보존했다.
- queue 2,759건·processed 2,759건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 153 groups·610 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 620건 중 `consumed_sdss` 610건·`prepared` 10건이다. 남은 prepared는 기존 G024 DR~DU 및 G168 AAF~AAK hold이며, 새 source·answer·SDSS 열람과 backlog 준비는 수행하지 않았다.
- G193 전체 stage와 induction이 완료되었으므로 다음 Astra semantic 단계는 현재 prepared/hold frontier의 기존 barrier와 `meta_state.py` due 상태를 따른다. 새 group 진행 전 meta due 및 manual parity audit due는 모두 false다.

<!-- luna-sync:G193-20260920-03 -->
## Luna 자동 인수인계 — G193 raw 후처리·frontier preflight 반영

- G193 AFB·AFC·AFD·AFE의 blind 4건과 group barrier 이후 answer_check 4건을 queue 원문 의미 변경 없이 기존 사례 문서와 processed 원장에 반영했다. 실제 SDSS 태그·기존 코드 판정은 공개하지 않았고, 사이트 연결 부재 사전 노출에 따른 strict-blind 제외 qualification과 기존 hold를 보존했다.
- queue 2,750건·processed 2,750건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 152 groups·606 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- manifest는 총 620건 중 `consumed_sdss` 606건·`prepared` 14건이다. 기준 미만 잔량에 따라 기존 canonical 색인을 기계 검사했으나 G194·G201은 `NEEDS_RESTORE`, G195~G200·G202는 `UNRESOLVED`로 새 READY를 추가하지 못했다. 의미 판정·자료 복원은 수행하지 않았다.
- 다음 Astra semantic frontier는 G193의 전체 independent_code이며, 같은 group의 SDSS 공개는 independent_code barrier 이후에만 가능하다. 다음 Excel-style case ID는 **AFB**다. G193 후속 전 새 group을 시작하지 않는다.

<!-- luna-sync:G181-induction-G193-hold-20260920-01 -->
## Luna 정기 sync — G181 induction·G193 linkage hold 반영

- `G181-induction-20260920-01`과 `G193-hold-20260920-linkage-absence-disclosure-01` raw 2건을 의미 변경 없이 기계 반영했다. G193의 실제 답·태그·원문은 열지 않았다.
- queue 2,742건·processed 2,742건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 152 groups·606 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 frontier는 G193 blind이며, G193 linkage absence hold는 보존한다.

<!-- luna-sync:G181-20260920-02 -->
## Luna 정기 sync — G181 전체 단계 반영

- G181 ACS·ACT·ACU·ACV·ACW·ACX의 ACU blind 후속과 전체 answer_check·independent_code·sdss_compare raw 19건을 의미 변경 없이 기계 반영했다. 앞선 ACU 범위 hold 원장은 보존하며, 공식 PDF crop 검증에 따른 후속 raw 의미도 그대로 반영했다.
- queue 2,740건·processed 2,740건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 152 groups·606 cases, `completed_groups_since_last_meta=1`, `completed_questions_since_last_meta=6`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- G181 induction raw가 추가되면 별도 sync로 반영한다. 다음 prepared frontier metadata는 G193이며, 기존 hold는 유지한다.

<!-- luna-sync:G181-G192-META47-20260920-01 -->
## Luna 정기 sync — G181 blind·G192 완료·META47 반영

- G181 ACS·ACT·ACV·ACW·ACX blind 5건과 ACU hold 1건, G192 AEX·AEY·AEZ·AFA 16건 및 historical exposure hold 1건, META47 raw 1건을 의미 변경 없이 기계 반영했다. ACU의 answer/SDSS 및 G181 후속 단계는 공개하지 않았다.
- G192 네 사례의 기존 `exposure_status=unknown`을 historical exposure hold와 연결해 `historical_exposure=true`, `strict_blind_eligible=false`로 보강했다. 최초 raw와 기존 unknown 상태의 이력은 보존했다.
- queue 2,719건·processed 2,719건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 151 groups·600 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- G181 ACU hold는 범위 supplement 확인 후 Astra 직접 대조를 기다리며, 다음 G181 단계는 group blind barrier를 따른다.

<!-- luna-sync:G180-20260920-01 -->
## Luna 정기 sync — G180 ACO·ACP·ACQ·ACR 완료

- G180 4문항의 blind·answer_check·independent_code·sdss_compare raw 16건과 후속 `induction` raw 1건을 의미 변경 없이 기계 반영했다.
- queue 2,695건·processed 2,695건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 150 groups·596 cases, `completed_groups_since_last_meta=2`, `completed_questions_since_last_meta=8`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 strict READY metadata는 G181 ACS·ACT·ACU·ACV·ACW·ACX이며, 이후 G192이다. 기존 G024·G168 hold는 유지한다.

<!-- luna-sync:G179-20260920-01 -->
## Luna 정기 sync — G179 ACK·ACL·ACM·ACN 완료

- G179의 `independent_code` 4건, `sdss_compare` 4건 및 후속 `induction` 1건을 Astra raw 의미 그대로 기계 반영했다. 독립 코드의 의미·경쟁 코드·SDSS 미연결 상태는 재판정하지 않았다.
- queue 2,678건·processed 2,678건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 149 groups·592 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`이다.
- 다음 strict READY metadata는 G180 ACO·ACP·ACQ·ACR이며, 이후 G181·G192이다. 기존 G024·G168 hold는 유지한다.

## 최신 Luna 자동 인수인계 — 2026-09-20 G179 raw 후처리·G192 기계 준비

- `ACK/ACL/ACM/ACN` G179의 blind 4건과 answer_check 4건, 총 8건을 queue 원문 의미 변경 없이 기존 사례 문서와 processed 원장에 반영했다. blind 원문은 답·SDSS·기존 코드 판정 미노출 상태로 저장된 기록을 보존하고, answer_check는 group 전체 blind barrier 이후 raw로 반영했다.
- queue 2,669건·processed 2,669건이며 `record_id` 기준 pending raw 0건, queue/processed 중복 0건이다. `meta_state.py` 동기화는 정상이며 `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 유지한다.
- prepared backlog는 총 616건 중 `consumed_sdss` 588건·`prepared` 28건이다. 기준 미만 잔량에 따라 기존 canonical index를 기계 검사해 G182~G192를 점검했으며, G192만 READY로 추가했다. **다음 Excel-style case ID는 AEX**이고, G192의 AEX·AEY·AEZ·AFA blind packet/source와 sealed provenance/answer 자료를 분리 생성했다.
- G182/G189는 `NEEDS_RESTORE`, G183~G188·G190·G191은 `UNRESOLVED`로 남겼다. 시각자료 복원·정본 확인·노출/코드 의미 판단은 수행하지 않았다. G168 사전답 노출 및 AAG crop hold도 그대로 유지한다.
- Astra 다음 semantic frontier는 기존 미완료 G179 `independent_code`이며, 같은 group의 SDSS 공개는 전체 independent_code barrier 이후에만 가능하다. G179 후속 완료 전 G192 blind를 시작하지 않는다.

## 최신 Luna 정기 sync — 2026-09-20 META46 반영

- `META-G160-G166-G167-meta_induction-20260920-46` raw 1건을 payload 원문 그대로 반영했다. G168 AAG 대괄호 범위 crop 복원 대기와 helper 표 셀만으로 종료 범위를 확정할 수 없다는 유보를 유지했다.
- queue 2,661건·processed 2,661건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 148 groups·588 cases, `meta_induction_count=46`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 strict READY는 manifest 순서상 **G179**이며, G168 비strict 후속은 범위 복원 후 진행한다.

## 최신 Luna 정기 sync — 2026-09-20 G167 완료·G168 부분 hold

- G167 AAC·AAD·AAE의 blind·answer_check·independent_code·sdss_compare와 G168 AAF·AAG·AAH·AAI·AAJ·AAK의 부분 blind/hold 및 원문 재구성 raw 등 신규 19건을 원문 의미 변경 없이 반영했다. G168은 6건 전체 사전답 노출로 strict-blind 제외하며, AAG range 실제 crop 복원 hold를 유지한다.
- queue 2,660건·processed 2,660건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 148 groups·588 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=10`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- G168 group 완료 처리는 하지 않는다. 다음 semantic 단계는 Astra의 **META46 `meta_induction`**이다.

## 최신 Luna 정기 sync — 2026-09-20 G166 후속·G167/G168 exposure 점검

- G166 ZY·ZZ·AAA·AAB의 independent_code·sdss_compare raw 8건을 원문 의미 변경 없이 반영했다. G166은 공식 전체 답표 반환 전에 4문항 blind가 완료된 상태로 보존한다.
- G167/G168 provenance를 기계 대조한 결과, 2026학년도 6월 모평과 일치하는 미완료 READY는 G168 AAF·AAG·AAH·AAI·AAJ·AAK이며, 공식 전체 답표 노출 범위에 해당하므로 `exposed=true` 및 strict blind 제외 대상으로 후속 metadata 보강이 필요하다. G167 AAC·AAD·AAE는 2026학년도 9월 모평으로 해당 없음.
- regular Luna의 신규 manifest 준비와 충돌하지 않도록 이번에는 manifest exposure 필드를 직접 수정하지 않고 case ID·노출 판정만 전달한다.
- queue 2,641건·processed 2,641건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 147 groups·585 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.

## 최신 Luna 정기 sync — 2026-09-20 G160 정본 정정·후속 stage 완료

- G160 ZD·ZE·ZF의 answer_check·independent_code·sdss_compare raw 9건과 `EXPOSURE-hold-20260920-official-pdf-unscoped-output-01` hold 1건을 원문 의미 변경 없이 기존 문서·processed 원장에 반영했다. 2026학년도 6월 모의평가 정본의 corrected official answers는 ZD/ZE/ZF `④/⑤/③`이며 최초 blind `④/⑤/③`과 최초 sealed `⑤/②/②`를 모두 보존했다.
- 2025학년도 6월로 잘못 연결된 기존 provenance·supplement는 보존하고, 실제 2026학년도 6월 문제지·정답표 연결과 SDSS 실제 연결 없음 한계를 후속 raw 그대로 기록했다. G160의 새 독립 판정은 Astra raw를 기계 반영했으며 Luna는 의미를 재판정하지 않았다.
- web 공식 PDF의 범위 밖 Q4~Q13 및 전체 답표가 반환된 노출 hold를 보존한다. 해당 시험의 미완료·신규 case는 strict blind 성과에서 제외하며, G166 4문항은 노출 전 blind 완료 상태를 보존한다.
- queue 2,633건·processed 2,633건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 146 groups·581 cases, `meta_induction_count=45`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 연구 상태는 기존 G166 후속 frontier를 유지하며, 새 준비작업은 별도 정기 Luna 절차에서 담당한다.

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

## 최신 Luna 정기 sync — 2026-09-20 G155 YK~YM 완료

- G155 YM blind 및 YK/YL/YM의 answer_check·independent_code·sdss_compare 신규 raw 10건을 기존 사례 문서와 processed 원장에 원문 의미 변경 없이 반영했다. YM의 `primary=[]`, `primary_candidates=[46,78]`, 과거 hold·노출 이력을 보존했다.
- queue 2,548건·processed 2,548건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 141 groups·564 cases, `meta_induction_count=43`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- G155 YK/YL/YM manifest 상태는 모두 `consumed_sdss`이며 SDSS 연결 태그 부재를 의미 판단으로 승격하지 않았다. 다음 frontier는 **G160 ZD·ZE·ZF**다. sealed source는 읽지 않았다.

## 최신 Luna 정기 sync — 2026-09-19 G159 YZ~ZC 완료

- G159 YZ~ZC의 answer_check·independent_code·sdss_compare raw 12건을 원문 의미 변경 없이 반영했다. YZ primary 빈 배열·56/60 후보 유보와 ZC 동일 농도·동일 부착량 구분을 보존했다.
- queue 2,538건·processed 2,538건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 140 groups·561 cases, `completed_groups_since_last_meta=1`, `completed_questions_since_last_meta=4`, `meta_induction_count=43`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 frontier는 복원 파일이 확인된 G155 YM blind 직접판독이다. 기존 G155 YK/YL blind 기록은 보존하며, YM 도식 의미는 Astra 직접 판독 전 확정하지 않는다.

## 최신 Luna 정기 sync — 2026-09-19 G157 YR~YU 완료·G158 READY 확인

- G157 YR~YU의 blind·answer_check·independent_code·sdss_compare raw 16건을 마지막 `YU-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. YT 완전분기 모형 한정 역추론과 1/2 효능감 미식별 한계를 보존했으며 YM source는 수정하지 않았다.
- queue 2,504건·processed 2,504건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 138 groups·553 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- metadata상 다음 READY frontier는 G158 YV·YW·YX·YY 4건이다.

## 최신 Luna 정기 sync — 2026-09-19 G156 YN~YQ 완료·YM hold 유지

- G156 YN~YQ와 G155 YK/YL blind·YM hold의 신규 raw 23건을 마지막 `YQ-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. YM은 fresh recovery가 진행 중이므로 기존 helper 부재 보고와 정확 문항 anchor 미확인 한계를 보존했고 source 파일은 수정하지 않았다.
- queue 2,488건·processed 2,488건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 137 groups·549 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- metadata상 G157은 YR·YS·YT·YU 4건이 `prepared`이며, 현재는 YM 복원 대기 또는 G157 YR frontier로 이어진다.

## 최신 Luna 정기 sync — 2026-09-19 TF depth_backfill 반영·G155 READY 확인

- `TF-depth_backfill-20260919-01` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다. 최초 46 대표, revised primary 빈 배열, 46/56 후보, aux17 및 원래 오답 범위를 보존했다.
- queue 2,465건·processed 2,465건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 136 groups·545 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- metadata상 다음 READY frontier는 G155 YK·YL·YM 3건이다.

## 최신 Luna 정기 sync — 2026-09-19 META42 manual parity audit 반영

- `AUDIT-meta42-manual_parity_audit-20260919-14` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다. 56 catalog의 설명항·피설명항·인과적 설명 별칭과 TF 최초 판정 대칭 문제를 보존했으며 의미 보완은 하지 않았다.
- queue 2,464건·processed 2,464건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 136 groups·545 cases, `meta_induction_count=42`, `last_manual_parity_audited_meta_count=42`, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=["TF"]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 TF depth_backfill이다.

## 최신 Luna 정기 sync — 2026-09-19 META42 반영·manual parity audit due

- `META-G152-G154-meta_induction-20260919-42` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다. TF와 YD의 46/56 대칭 감사 대상은 그대로 보존했다.
- queue 2,463건·processed 2,463건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 136 groups·545 cases, `meta_induction_count=42`, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 manual parity audit이다.

## 최신 Luna 정기 sync — 2026-09-19 G154 YH~YJ 완료·META42 due

- G154 YH~YJ의 신규 raw 10건을 마지막 `YJ-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. YI 17/22 유보와 YJ 내부 단계·영역 지도 순서 구별을 보존했다.
- queue 2,462건·processed 2,462건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 136 groups·545 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=9`, `meta_induction_count=41`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 META42이며 이후 manual parity audit을 진행한다.

## 최신 Luna 정기 sync — 2026-09-19 G153 YE~YG 완료·G154 YH/YI blind·YJ hold

- G153 YE~YG 및 G154 YH/YI blind·YJ hold의 신규 raw 16건을 마지막 `YG-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. YF 원도식의 둘 다 상승·상대 부족과 절대 감소의 구별 및 이전 hold를 보존했고, YJ 범위 보강파일은 Astra 직접 확인 전 hold로 유지했다.
- queue 2,452건·processed 2,452건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 135 groups·542 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 순서는 YJ 보강 source 확인 후 G154 후속이다.

## 최신 Luna 정기 sync — 2026-09-19 G152 YB~YD 완료·G153 READY 확인

- G152 YB~YD의 신규 raw 13건을 마지막 `YD-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. YC 범위 hold 2건과 첫·끝 문장 보강 후 blind를 보존했으며, YD primary 빈 배열·46/56 후보와 설명 근거 부재를 절대 불가능 판정으로 확대하지 않는 한계를 유지했다.
- queue 2,436건·processed 2,436건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 134 groups·539 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- metadata상 다음 READY frontier는 G153 YE·YF·YG 3건이다.

## 최신 Luna 정기 sync — 2026-09-19 META41 반영

- `META-G147-G150-G151-meta_induction-20260919-41` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다. XH·XV·YA 후보와 모형·전사 검증 범위 한계를 보존했다.
- queue 2,423건·processed 2,423건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 133 groups·536 cases, `meta_induction_count=41`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 frontier는 현재 진행 중인 G152 YC이다.

## 최신 Luna 정기 sync — 2026-09-19 G151 XY/XZ/YA 완료·META41 due

- G151 XY·XZ·YA와 G152 YB blind의 신규 raw 14건을 마지막 `YA-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. XZ 보강 hold 해소, YA 25/93 후보 유보, UW/VA provenance SHA-256 교정과 범위 의미 보존을 유지했다.
- queue 2,422건·processed 2,422건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 133 groups·536 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=13`, `meta_induction_count=40`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra META41이다.

## 최신 Luna 정기 sync — 2026-09-19 G147 XI·XF~XI 완료

- G147 XI 보강 및 XF~XI의 신규 raw 13건을 마지막 `XI-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. XI는 공식표 전사 직접 확인 범위로 보존하고 시각 crop 검증 주장은 추가하지 않았다. XH 10/12/22 후보 유보와 비교축·증가량/증가율 한계를 유지했다.
- queue 2,408건·processed 2,408건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 132 groups·533 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- metadata상 다음 READY frontier는 G151 XY·XZ·YA 3건이다.

## 최신 Luna 정기 sync — 2026-09-19 G150 XS~XX·G147 XF~XI raw 반영

- G150 XS~XX의 신규 raw와 G147 XF/XG/XH blind·XI hold raw를 마지막 `XX-sdss_compare-20260919-01`까지 총 29건 반영했다. XI 보강 2파일은 Astra 직접 확인 전 hold로 유지하고, XS 선택표 보강blind 이력·XV 75/78 유일 주 유보·XX 과제 적합성 한계를 보존했다.
- queue 2,395건·processed 2,395건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 131 groups·529 cases, `meta_induction_count=40`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 순서는 XI 보강 source 직접 확인 후 G147 후속이다.

## 최신 Luna 정기 sync — 2026-09-19 META40 반영

- `META-G137-G138-G146-meta_induction-20260919-40` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다. source 파편 노출과 가격상한 일반화 금지 한계를 보존했다.
- queue 2,366건·processed 2,366건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 130 groups·523 cases, `meta_induction_count=40`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 frontier는 G147 XF이다.

## 최신 Luna 정기 sync — 2026-09-19 G146 WZ~XE 완료·META40 due

- G146 WZ~XE의 blind·answer_check·independent_code·sdss_compare raw 24건을 마지막 `XE-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. XB 말미 다음 자료 파편 노출, XD 상대가격 제약 한계, XA 필요조건 과장 금지 payload를 보존했다.
- queue 2,365건·processed 2,365건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 130 groups·523 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=12`, `meta_induction_count=39`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 META40 `meta_induction`이며 새 의미 판단은 생성하지 않았다.

## 최신 Luna 정기 sync — 2026-09-19 G138 VK~VM 완료·G146 WZ frontier 확인

- G138 VK~VM의 blind·answer_check·independent_code·sdss_compare raw 12건을 마지막 `VM-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. VL의 궁극 목적과 한 기능 구별, VM의 인식과 미래 실천 의지 구별 한계를 보존했다.
- queue 2,341건·processed 2,341건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 129 groups·517 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- metadata상 G139·G148은 `NEEDS_RESTORE`(visual material linked asset 미확보), G140~G145·G149·G165는 `UNRESOLVED`(passage/stem/choices completeness 또는 choice parse 실패)로 보류되어 manifest에 prepared case를 추가하지 않았다. 현재 실제 READY frontier는 G146 WZ이며 G139~G145의 미래 문항 내용은 열지 않았다.

## 최신 Luna 정기 sync — 2026-09-19 G137 VH~VJ 완료

- G137 VH~VJ의 blind·answer_check·independent_code·sdss_compare raw 12건을 마지막 `VJ-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. VI의 기록된 방법과 일반적으로 좋은 방법의 구별, VJ 지침 적용 범위를 보존했다.
- queue 2,329건·processed 2,329건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 128 groups·514 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 frontier는 G138 VK이다.

## 최신 Luna 정기 sync — 2026-09-19 TG depth_backfill 반영

- `TG-depth_backfill-20260919-01` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다. 최초 17 판정과 revised primary 빈 배열·17/45 후보, 명시된 오답 범위 3/10/49를 보존했으며 확정 배타 주 코드 집계에서 제외했다.
- queue 2,317건·processed 2,317건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 127 groups·511 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 frontier는 G137 VH이다.

## 최신 Luna 정기 sync — 2026-09-19 META39 manual parity audit 반영

- `AUDIT-meta39-manual_parity_audit-20260919-13` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다. 이전 TG와 신규 UJ의 정답 직접 경로 대조를 TG depth_backfill 대상으로 지정한 상태를 보존했으며, Astra backfill 전 의미 수정은 하지 않았다.
- queue 2,316건·processed 2,316건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 127 groups·511 cases, `meta_induction_count=39`, `last_manual_parity_audited_meta_count=39`, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=["TG"]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 TG depth_backfill이다.

## 최신 Luna 정기 sync — 2026-09-19 META39 반영·manual parity audit due

- `META-G132-G133-G136-meta_induction-20260919-39` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다. TG/UJ 동일 범위 대칭 비교는 Astra audit에서 수행할 대상으로 보존했다.
- queue 2,315건·processed 2,315건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 127 groups·511 cases, `meta_induction_count=39`, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 manual parity audit이며 audit raw 저장·후속 Luna sync 전 새 group 연구를 시작하지 않는다.

## 최신 Luna 정기 sync — 2026-09-19 G136 VE~VG 완료·META39 due

- G136 VE~VG의 blind·answer_check·independent_code·sdss_compare raw 12건을 마지막 `VG-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. VE 사진 직접 미판독 범위와 원표 미검증·SDSS 부재 한계를 보존했다.
- queue 2,314건·processed 2,314건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 127 groups·511 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=13`, `meta_induction_count=38`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 META39이며, 이후 manual parity audit due를 확인한다.

## 최신 Luna 정기 sync — 2026-09-19 G133 UP·UM~UR 완료

- G133 UP·UM~UR의 신규 raw 19건을 마지막 `UR-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. UQ primary 빈 배열·17/75 후보와 UP 기준·분류 관점 한계를 보존했으며 G132/G133 source hold 해소 상태를 유지했다.
- queue 2,302건·processed 2,302건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 126 groups·508 cases, `meta_induction_count=38`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- manifest는 총 598건 중 `consumed_sdss` 508건·`prepared` 90건이다. 다음 frontier는 G136 VE이며, 기존 backlog 추가 준비 결과는 유지한다.

## 최신 Luna 정기 sync — 2026-09-19 G132 UK·UI~UL 완료

- G132 UK·UI~UL의 신규 raw 13건을 마지막 `UL-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. UK·UL source hold 및 공식/canonical 차이를 보존했고, UI #17/#22·UJ #17/#45·UL #45/#46 유일 주 유보를 구조화 payload 그대로 유지했다.
- queue 2,283건·processed 2,283건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 125 groups·502 cases, `meta_induction_count=38`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 frontier는 UP 번호표 supplement 직접 확인 후 G133 후속이다.

## 최신 Luna 정기 sync — 2026-09-19 META38 반영·UK/UP source hold 유지

- `META-G131-G134-G135-meta_induction-20260919-38` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다.
- queue 2,270건·processed 2,270건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 124 groups·498 cases, `meta_induction_count=38`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- UK 공식 선택표 crop과 UP 번호표 supplement는 확보되었으나 Astra 직접 판독 전 hold로 유지한다. 다음 frontier는 UK 원표 직접 판독 후 G132 후속, 그 다음 UP 복구 후 G133 후속이다.

## 최신 Luna 정기 sync — 2026-09-19 G135 UY~VD 완료·META38 due

- G135 UY~VD의 blind·answer_check·independent_code·sdss_compare raw 22건을 마지막 `VD-sdss_compare-20260919-01`까지 기존 문서·processed 원장에 의미 변경 없이 반영했다. UP 보강파일은 Astra 직접 확인 전 상태로 보존하고, UK 공식 선택표 hold도 유지했다.
- queue 2,269건·processed 2,269건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 124 groups·498 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=16`, `meta_induction_count=37`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 META38 `meta_induction`이며, 기존 backlog 보충 결과는 유지하고 새 group 연구는 META38 후속 sync 전 시작하지 않는다.

## 최신 Luna 기계적 backlog 준비 — 2026-09-19 G139~G168 preflight

- prepared 29건 도달에 따라 `scripts/luna_prepare_frontier.mjs`로 미사용 exact-canonical 후보 G139~G168 30개 group을 기계 검사했다. READY 20개 group·77건(G146~G147, G150~G164, G166~G168)을 blind source·packet·sealed provenance/answer 분리 상태로 추가했다.
- NEEDS_RESTORE는 G139·G148, UNRESOLVED는 G140~G145·G149·G165로 metadata hold만 남겼다. 시각 asset 복원과 의미 판단은 수행하지 않았다. 새 READY의 SDSS linkage는 0건이며 sealed answer/SDSS는 blind barrier 뒤에 둔다.
- manifest는 총 598건 중 `consumed_sdss` 492건·`prepared` 106건이다. preflight 기계 검증은 content leakage 0·blind leakage 0·question duplicates 0을 확인했으며, 기존 source provenance 경고 11건과 existing case overlap 2건은 보존했다.
- 새 준비 결과 보고서는 `data/기본기_연구/prepared_backlog/LUNA_FRONTIER_PREFLIGHT_20260918.md`에 저장했다. 첫 READY frontier는 G146 WZ이며, hold/unresolved group은 복원·정본 확인 전 연구하지 않는다.

## 최신 Luna 정기 sync — 2026-09-19 G134 완료·G132/G133/G135 hold 보존

- 마지막 `UX-sdss_compare-20260919-01`까지 신규 raw 40건을 기존 연구 문서·processed 원장에 의미 변경 없이 반영했다. G134 US~UX는 완료했으며, G132 UI·UJ·UL 및 G133 UM·UN·UO·UQ·UR, G135 UY·UZ는 blind만 완료 상태를 보존했다. UK 선택표 hold, UP 번호표 hold, VA `[A]` 범위 hold와 VB~VD 미착수 상태도 유지했다.
- queue 2,247건·processed 2,247건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 123 groups·492 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- manifest는 총 521건 중 `consumed_sdss` 492건·`prepared` 29건이다. prepared가 30건 미만이므로 backlog 보충 기준에 진입했지만, 이번 sync에서는 신규 후보·sealed 자료를 추가로 읽거나 대규모 준비를 수행하지 않았다. 다음 처리는 기존 hold source 복원과 prepared metadata 확인을 우선한다.

## 최신 Luna 정기 sync — 2026-09-19 G131 UE~UH 완료

- G131 UE~UH의 blind·answer_check·independent_code·sdss_compare raw 16건을 마지막 `UH-sdss_compare-20260919-01`까지 원문 의미 변경 없이 반영했다. UG primary 빈 배열·12/22 후보와 UH 가상모형의 기능별 상태갱신·안전성 비교 범위를 보존했다.
- queue 2,207건·processed 2,207건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 122 groups·486 cases, `meta_induction_count=37`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- manifest는 총 521건 중 `consumed_sdss` 486건·`prepared` 35건이다. prepared가 30건 이상이므로 backlog 추가 준비는 수행하지 않았다. 다음 frontier는 G132 UI이다.

## 최신 Luna 정기 sync — 2026-09-19 META37 반영·G131 준비 확인

- `META-G121-G129-G130-meta_induction-20260919-37` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다.
- queue 2,191건·processed 2,191건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 121 groups·482 cases, `meta_induction_count=37`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- manifest metadata상 G131은 존재하며 UE~UH 4건이 모두 `prepared`이고 source quality는 visual placeholder 없음·canonical link exact·choice parse complete·text markers preserved, exposure는 unknown이다. 이후 G132~G138도 prepared 상태다.
- manifest는 총 521건 중 `consumed_sdss` 482건·`prepared` 39건이다. prepared가 30건 이상이므로 backlog 추가 준비는 필요하지 않다. 다음 frontier는 G131 UE이며, 새 semantic 단계는 Astra 진행 지시에 따른다.

## 최신 Luna 정기 sync — 2026-09-19 G130 TZ~UD 완료·META37 due

- G130 TZ~UD의 신규 raw 18건을 마지막 `UD-sdss_compare-20260919-01`까지 기존 연구 문서·processed 원장에 의미 변경 없이 반영했다. UA primary 빈 배열·10/12/79 후보, UC primary 빈 배열·12/22/79 후보, UB 개별 법령 전칭 범위 우열 미확정 한계를 보존했다.
- queue 2,190건·processed 2,190건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 121 groups·482 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=16`, `meta_induction_count=36`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 META37 `meta_induction`이며, raw 저장·Luna sync·pending 0 검증 전 새 group 연구를 시작하지 않는다.

## 최신 Luna 정기 sync — 2026-09-19 G129 완료·G130 TZ/UA blind 반영

- G129 TU~TY의 blind·answer_check·independent_code·sdss_compare와 TX `[A]` 범위 hold/보강blind raw, G130 TZ·UA blind raw를 마지막 `TY-sdss_compare-20260919-01`까지 총 23건 반영했다. TV primary 빈 배열·17/22 후보, TW의 복합 84/63, TY의 거래 항목 변화 45 대표 판정을 raw 의미 그대로 보존했다.
- TX 범위 hold 해소 이력과 원표 미검증·SDSS 부재 한계를 유지했다. G130 TZ·UA는 blind만 완료되어 후속 단계는 시작하지 않는다.
- queue 2,172건·processed 2,172건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 120 groups·477 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 frontier는 G130 UB이다.

## 최신 Luna 정기 sync — 2026-09-19 G121 SH 재개·SD~SI 후속 반영

- `SH-blind-20260919-01`과 SD~SI의 answer_check·independent_code·sdss_compare raw 19건을 마지막 `SI-sdss_compare-20260919-01`까지 기존 연구 문서·processed 원장에 의미 변경 없이 반영했다. SG의 primary 빈 배열·17/22 후보, SH의 39/91 두 단계 비교대상 식별·비례비교 판정과 canonical⑤ M/m source 보강을 raw 그대로 보존했으며, 원래 hold·source 기록은 덮어쓰지 않았다.
- SH 공식 원문 supplement는 `data/기본기_연구/prepared_backlog/blind_sources/SH_official_question_supplement_20260919.json`에 보존되어 Astra 직접 확인 후 blind가 완료되었다.
- queue 2,149건·processed 2,149건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 119 groups·472 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 frontier는 G129 TU이다.

## 최신 Luna 정기 sync — 2026-09-19 TP·TS depth_backfill 반영

- `TP-TS-depth_backfill-20260919-01` 결합 raw 1건을 TP·TS 사례 문서와 독립연구 진행 기록·processed 원장에 원문 의미 그대로 반영했다. 최초 주 판정과 17/22 작업대표는 보존하고, 유일 주 확정 집계에는 포함하지 않았다.
- queue 2,130건·processed 2,130건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 118 groups·466 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 확인했다.
- 다음 Excel-style frontier는 **G129 TU**이며, 새 group 진행 전 현재 상태를 기준으로 한다.

## 최신 Luna 정기 sync — 2026-09-19 META36 manual parity audit 반영

- `AUDIT-meta36-manual_parity_audit-20260919-12` raw 1건을 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다. TP·TS depth_backfill 지정과 최초 주 판정 보존을 기록했으며, Luna는 의미 보완·판정 수정을 수행하지 않았다.
- queue 2,129건·processed 2,129건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 118 groups·466 cases, `meta_induction_count=36`, `last_manual_parity_audited_meta_count=36`, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=3`, `depth_backfill_pending=["TP", "TS"]`를 확인했다.
- 다음 semantic 단계는 Astra의 TP·TS depth_backfill이며, 실제 수정은 해당 raw 후속 작업에서 별도로 수행한다.

## 최신 Luna 정기 sync — 2026-09-19 META36 반영·manual parity audit due

- `META-G126-G128-meta_induction-20260919-36` raw 1건을 필수 12개 필드와 함께 원문 의미 변경 없이 독립연구 진행 기록·processed 원장에 반영했다. 새 의미 판단과 audit raw 생성은 수행하지 않았다.
- queue 2,128건·processed 2,128건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 118 groups·466 cases, `meta_induction_count=36`, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`를 확인했다.
- 다음 semantic 단계는 Astra의 manual parity audit이며, audit raw 저장과 후속 Luna sync 전 새 group 연구를 시작하지 않는다.

## 최신 Luna 정기 sync — 2026-09-19 G128 TO~TT 완료·META36 due

- 마지막 raw `TT-sdss_compare-20260919-01`까지 G128 TO~TT의 신규 raw 20건을 기존 연구 문서·processed 원장에 원문 의미 그대로 반영했다. 새 의미 판단과 META36 raw 생성은 수행하지 않았다.
- queue 2,127건·processed 2,127건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 118 groups·466 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=16`, `meta_induction_count=35`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`를 확인했다.
- 운영 규칙에 따라 다음 semantic 단계는 Astra의 META36 `meta_induction` raw 저장이며, 이후 Luna sync와 pending raw 0 검증 전 새 group 연구를 시작하지 않는다.

## 최신 Luna 정기 sync — 2026-09-19 G127 완료·G128 TO~TR blind 반영

- `astra_handoff_queue.jsonl`의 마지막 raw `TN-sdss_compare-20260919-01`까지 신규 raw 전부를 기존 연구 문서·processed 원장에 의미 변경 없이 반영했다. TK 선택표 source hold와 TL `[A]` 범위 hold는 blind source 보강 근거를 보존한 채 후속 G127 blind에 연결했다.
- G127 TI~TN은 blind·answer_check·independent_code·sdss_compare 전 단계가 완료되었다. G128은 TO·TP·TQ·TR blind만 완료되었고 TS·TT는 미완료이므로 answer_check·independent_code·SDSS를 시작하지 않는다.
- queue 2,107건·processed 2,107건이며 `record_id` 기준 pending raw 0건이다. `meta_state.py`: 완료 117 groups·460 cases, `meta_induction_count=35`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`를 확인했다.
- 다음 frontier는 G128 TS·TT blind 완료 후 group barrier 확인이다. meta/audit/backfill raw는 새로 생성하지 않았다.

## 최신 Luna 정기 sync — 2026-09-19 G127 TI blind 반영·TK source hold

- G127 `TI-blind-20260919-01`과 `TK-hold-20260919-missing-choice-table-01`을 raw payload 그대로 기존 연구 문서에 반영했다. TI는 blind 단계만 완료했고, TK는 canonical 선택표 공란으로 source hold를 유지한다.
- G127은 TK 유효 blind 전 전체 answer_check를 시작하지 않는다. TI 다음 Excel-style frontier는 **TJ**이며, TK hold 해소 전 G127 group 후속 단계(answer_check·independent_code·SDSS)는 금지한다.
- queue 2,079건·processed 반영 후 pending raw 0건이다. `meta_state.py` 동기화 후 완료 116 groups·454 cases, `meta_induction_count=35`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`를 확인한다.
- manifest는 총 521건 중 `consumed_sdss` 454건·`prepared` 67건이다. backlog는 30건 미만이 아니므로 후보 추가 준비를 하지 않는다. G121 SH 공식 문제지 source hold도 계속 유지한다.

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

## 최신 Luna handoff sync — 2026-09-19 META34 반영

- `META-G114-G119-meta_induction-20260919-34` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. 신규 경계는 작업 기준 보강으로만 보존했으며 최초 주 코드 수정·전역 코드 통합은 수행하지 않았다.
- queue 1,991건·processed 1,991건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 112 groups·435 cases, `meta_induction_count=34`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 actionable READY frontier는 **G120 RZ**다. QZ 유보와 RX 노출·분모 한계는 기존 기록 그대로 유지한다.

## 최신 Luna handoff sync — 2026-09-19 G119 RV~RY 완료

- G119 RV·RW·RX·RY의 신규 blind·answer_check·independent_code·sdss_compare raw 16건과 RX hold 1건을 원 payload 그대로 기존 사례 문서·processed 원장에 반영했다. RX의 보조 답 노출 qualification, 분모 고정 문맥, canonical 원표 기계 복원 이력과 hold 경과를 보존했다.
- queue 1,990건·processed 1,990건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 112 groups·435 cases, META33 이후 3 groups·13 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 다음 단계는 Astra의 META34 의미 작업이며 Luna가 추론으로 해결하지 않는다.
- manifest는 총 521건 중 `consumed_sdss` 435건·`prepared` 86건이다. G024 DR~DU historical prior-exposure hold는 계속 제외하며, 다음 actionable READY frontier는 **G120 RZ**다.

## 최신 Luna source restoration — 2026-09-19 G119 RX 선택지 B열 보강

- RX blind source의 누락된 `<보기>` B열을 canonical HWPX/XML의 Q086 선택지 조판에서 기계적으로 복원해 [RX choice table supplement](../../data/기본기_연구/prepared_backlog/blind_sources/RX_choice_table.md)에 저장했다. A/B 5행과 행·열 구조만 보강했으며 답·SDSS·해설·코드 의미는 포함하지 않았다.
- sealed provenance는 [RX provenance](../../data/기본기_연구/prepared_backlog/sealed/RX_choice_table_provenance_20260919.json)에 분리 저장했다. RX hold는 Astra의 blind 직접 확인 전까지 유지한다.

## 최신 Luna handoff sync — 2026-09-19 G118 RQ~RU 및 induction 후처리

- G118 RQ·RR·RS·RT·RU의 blind·answer_check·independent_code·sdss_compare raw 20건과 `G118-induction-20260919-01` raw 1건을 queue 원문 그대로 기존 사례 문서·독립연구 진행 기록·processed 원장에 반영했다. 동일 지문 내 비교 의미만 보존했으며 전역 코드 통합·의미 재판정은 수행하지 않았다.
- queue 1,973건·processed 1,973건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 111 groups·431 cases, `meta_induction_count=33`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 521건 중 `consumed_sdss` 431건·`prepared` 90건이다. G024 DR~DU historical prior-exposure hold는 계속 제외하며, 다음 actionable READY frontier는 **G119 RV**다.

## 최신 Luna handoff sync — 2026-09-18 G114 QW~QZ 후속 raw 후처리

- queue의 미처리 raw 16건(G114 QW~QZ blind·answer_check·independent_code·sdss_compare)을 원 payload 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,952건·processed 1,952건이며 `record_id` 기준 pending raw는 0건이다.
- `meta_state.py`: 완료 110 passage groups·426 cases, `meta_induction_count=33`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 이번 raw에는 meta/audit/backfill이 없으므로 상태 의미를 추가하지 않았다.
- manifest는 총 521건 중 `consumed_sdss` 426건·`prepared` 95건이다. G024 DR~DU historical prior-exposure hold는 계속 제외한다. 다음 actionable READY frontier는 G118 RQ이다.
- QZ는 공식 답 ④와 최초 답이 일치하지만 ③의 문언(정확히 하나/적어도 하나)과 학생 존재 전제에 따른 배제 강도는 unresolved로 보존했다. 문항 오류 확정·복수 정답 주장·유일성 증명 완료로 승격하지 않았다.
- manifest는 총 521건 중 `consumed_sdss` 422건·`prepared` 99건이다. G024 DR~DU historical prior-exposure hold는 계속 제외한다.
- QR 수식 평탄화와 QV 후속 연도 경계 잔재 qualification은 원 raw 문구 그대로 보존했으며, Luna는 의미를 재판정하지 않았다.
- QI·QJ의 유일 주 우선순위 유보와 인접 코드 중첩은 raw 문구 그대로 보존했다. Luna는 raw 판단 의미를 수정하지 않았고, 답·SDSS·기존 코드 판정을 새로 열람하거나 추론하지 않았다.
- backlog는 30건 미만이 아니므로 후보를 추가 준비하지 않았다. blind source/packet과 sealed answer·SDSS 분리 상태를 유지했다.
- 기계 검증: content leakage 0, question duplicate 0. 기존 provenance 경고 11건(IK·IO·IR·IW·IX·KS·LJ·LK·LN·LR·MX), identity leak 3건, existing overlap 2건은 변경 없이 보존된 경고다.
- 다음 Astra frontier는 **G118 RQ**이다. G024 DR~DU historical hold는 소비하지 않는다.

## 최신 Luna handoff sync — 2026-09-18 META32 반영

- `META-G106-G108-meta_induction-20260918-32` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. PR 엔트로피 최대 유일성 증명 미포함 qualification과 PH 유일 주 유보를 보존했으며, Luna는 의미를 재판정하지 않았다.
- queue 1,871건·processed 1,871건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 106 groups·407 cases, `meta_induction_count=32`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 521건 중 `consumed_sdss` 407건·`prepared` 114건이다. G024 DR~DU historical hold를 제외한 다음 READY frontier는 **QH / G111**이다.
- blind source·packet 경로, 중복, content leakage는 기계 점검으로 이상 없음이다. 기존 source provenance 경고(IK·IO·IR·IW·IX·KS·LJ·LK·LN·LR·MX)와 기존 overlap 2건은 변경하지 않았다. 답·SDSS·기존 코드 판정은 새로 열람하거나 추론하지 않았다.
- prepared 부족(19건)에 따라 기존 canonical `data/kice_passages.jsonl`·`data/kice_questions.jsonl`의 미사용 passage만 기계적으로 검사해 G109~G138을 준비했다. READY 23개 group·110건을 추가했으며 G109 NEEDS_RESTORE, G110·G115~G117·G123·G125 UNRESOLVED는 semantic 판단 없이 보류했다. blind source와 sealed provenance/answer 분리는 유지했다.
- 다음 Astra Excel-style case ID는 **QH**이며, 허용 다음 단계는 G111 QH blind다.

## 최신 Luna handoff sync — 2026-09-17 G103 완료

- G103 OX·OY·OZ·PA의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 반영했다. OX primary 빈 값과 candidates #56/#64 유보를 확정 주로 승격하지 않았다.
- queue 1,789건·processed 1,789건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 102 groups·387 cases, META30 이후 2 groups·10 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 411건 중 `consumed_sdss` 387건·`prepared` 24건이다. 다음 metadata frontier는 G104이며, prepared 보충은 기존 group·원장 충돌을 피하는 기계 단계로 다음에 수행한다.

## 최신 Luna handoff sync — 2026-09-17 G102 완료

- G102 OR·OS·OT·OU·OV·OW의 blind·answer_check·independent_code·sdss_compare raw 24건을 queue 원문 그대로 반영했다. OU 고정 분자/분모, OT 선후 기제, SDSS 연결 부재를 보존했다.
- queue 1,773건·processed 1,773건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 101 groups·383 cases, META30 이후 1 group·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 411건 중 `consumed_sdss` 383건·`prepared` 28건이다. 다음 metadata frontier는 G103이며, prepared 잔량 28건에 대한 기계적 보충은 다음 준비 단계에서 수행한다.

## 최신 Luna handoff sync — 2026-09-17 NV depth_backfill 반영

- `NV-depth_backfill-20260917-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. 현재 유일 주 유보, candidates #45/#2, 최초 #45 이력 및 확정 주 집계 분리를 보존했다.
- queue 1,749건·processed 1,749건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 100 groups·377 cases, META30 이후 0 groups·0 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 metadata frontier는 G102 OR부터다. G024 DR~DU prior-exposure hold는 계속 제외한다.

## 최신 Luna handoff sync — 2026-09-17 META30 audit 반영

- `AUDIT-meta30-manual_parity_audit-20260917-10` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다.
- queue 1,748건·processed 1,748건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["NV"]`, `last_manual_parity_audited_meta_count=30`이다.
- NV depth_backfill 완료 전 새 semantic stage·새 group을 시작하지 않는다. backfill은 Astra가 직접 수행한다.

## 최신 Luna handoff sync — 2026-09-17 META30 반영

- `META-G099-G101-meta_induction-20260917-30` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다.
- queue 1,747건·processed 1,747건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 100 groups·377 cases, `meta_induction_count=30`, `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`이다.
- META30 manual parity audit 완료 전 새 group을 시작하지 않는다. 표본 감사 대상은 Astra가 직접 수행한다.

## 최신 Luna handoff sync — 2026-09-17 G101 완료·META30 due

- G101 ON·OO·OP·OQ의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 반영했다. OQ의 단순 갱신 모형 한계와 출력/정답 구별을 보존했다.
- queue 1,746건·processed 1,746건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 100 groups·377 cases, META29 이후 3 groups·12 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 411건 중 `consumed_sdss` 377건·`prepared` 34건이다. META30 `meta_induction` 전 다음 group semantic stage를 시작하지 않는다.
- quota 관측은 helper sandbox/default 및 escalated 호출이 모두 unavailable이었고, 별도 read-only `codex app-server --stdio </dev/null` startup 진단은 sqlite runtime 초기화 실패와 read-only filesystem 경고를 출력했다. 이는 handoff/종료 트리거가 아니며 quota 값을 추정하지 않았다.

## 최신 Luna handoff/preparation sync — 2026-09-17 G100·G101~G108

- `G099-G100-induction-20260917-01` raw 1건을 queue 원문 그대로 반영했다. queue 1,730건·processed 1,730건이며 `record_id` 기준 pending raw는 0건이다.
- G100 완료 후 남은 실행 가능 prepared가 없고 G024 DR~DU만 prior-exposure hold였으므로, 기존 KICE canonical 색인에서 G101~G108 중 G105를 제외한 7개 READY group·34 cases(ON~PU)를 기계적으로 추가했다. manifest는 총 411건 중 `consumed_sdss` 373건·`prepared` 38건이다.
- G105는 Q32 `incomplete_visual_or_table`로 제외했다. 신규 READY는 visual placeholder 없음·choices 5개·exact canonical link·기계적 공식답 검증을 통과했으며 SDSS linkage는 0건으로 빈 값 유지했다. blind/sealed 분리와 G024 재blind 금지를 보존했다.
- `meta_state.py`: 완료 99 groups·373 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 다음 Excel-style frontier는 **ON / G101**이며 다음 preparation frontier는 G109다. 상세 기계 보고는 [PREPARE_FRONTIER_101_108_20260917.md](../../data/기본기_연구/prepared_backlog/PREPARE_FRONTIER_101_108_20260917.md)에 기록했다.

## 최신 Luna handoff sync — 2026-09-17 G100 완료

- G100 OJ·OK·OL·OM의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 반영했다.
- queue 1,729건·processed 1,729건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 99 groups·373 cases, META29 이후 2 groups·8 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 377건 중 `consumed_sdss` 373건·`prepared` 4건이며 남은 prepared는 G024 DR·DS·DT·DU historical prior-exposure hold뿐이다. 이 hold는 재blind·새 independent 판정 금지로 유지하고, 현재 실행 가능한 새 frontier는 없다.
- 신규 준비 의무 문구는 `분석/기본기_연구/LUNA_HANDOFF.md` 166행에 있다: “manifest의 잔량을 확인한다. 최소 30개 아래면 기존 색인·정본 연결 자료만 사용해 후보를 기계적으로 추가하고 … blind packet과 sealed answer/SDSS record를 분리 생성한다.” 이번 sync에서는 사용자 지시에 따라 신규 자료 열람·준비를 하지 않았다. quota unavailable은 종료 트리거가 아니다.

## 최신 Luna handoff sync — 2026-09-17 G099 완료

- G099 OF·OG·OH·OI의 blind·answer_check·independent_code·sdss_compare raw 13건을 queue 원문 그대로 반영했다. OH 원식 `B/A` 복원과 source hold 해소, #84 몫과 상수 구별을 보존했다.
- queue 1,713건·processed 1,713건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 98 groups·369 cases, META29 이후 1 group·4 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 377건 중 `consumed_sdss` 369건·`prepared` 8건이다. 다음 metadata frontier는 G100이다.
- historical G024 DR·DS·DT·DU는 기존 기록상 prior-exposure hold이며 independent_code·SDSS 미실행 상태다. manifest의 현재 `exposure_status`는 `unknown`; 기존 hold 기록에는 재개에 필요한 개별 원자료 목록이 명시되어 있지 않아 새 자료·답·SDSS를 추정하거나 노출하지 않았다.

## 최신 Luna handoff/source sync — 2026-09-17 G099 OH source hold

- `OH-hold-20260917-equation-01` raw 1건을 queue 원문 그대로 반영했다. G099 answer barrier는 유지하며 OF·OG·OI blind 진행과 분리했다.
- canonical HWPX `고3 기출/2027 고3 국어 독서_Ⅲ. 과학.hwpx`의 `Contents/section0.xml`에서 [OH blind source supplement](../../data/기본기_연구/prepared_backlog/blind_sources/OH_canonical_source_supplement.json)를 저장했다. 문항 앵커 1015, table 1714273485, target `cellAddr=(1,2)`, `cellSpan=(3,1)`, equation 1714273486의 원 script `{B} over {A}`와 인접 텍스트를 기록했다. 답·SDSS·해설은 읽지 않았다.
- queue 1,697건·processed 1,697건이며 `record_id` 기준 pending raw는 0건이다. OH source hold 해소 여부와 G099 후속 semantic stage는 Astra가 직접 확인한다.

## 최신 Luna handoff sync — 2026-09-17 META29 반영

- `META-G096-G098-meta_induction-20260917-29` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다.
- queue 1,696건·processed 1,696건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 97 groups·365 cases, `meta_induction_count=29`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 추가 backlog 준비는 수행하지 않았다. historical hold G024 DR~DU를 제외한 다음 metadata frontier는 G099 OF다.

## 최신 Luna handoff sync — 2026-09-17 G098 완료

- G098 OA·OB·OC·OD·OE의 blind·answer_check·independent_code·sdss_compare raw 20건을 queue 원문 그대로 반영했다. #24 NY/OD 예외의 효과·주체·범위와 #17/#45 역할 대응 중첩을 보존했다.
- queue 1,695건·processed 1,695건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 97 groups·365 cases, META28 이후 3 groups·16 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 377건 중 `consumed_sdss` 365건·`prepared` 12건이다. META29 `meta_induction` 전 다음 group을 시작하지 않는다.

## 최신 Luna handoff sync — 2026-09-17 G097 완료

- G097 NU·NV·NW·NX·NY·NZ의 blind·answer_check·independent_code·sdss_compare raw 24건을 queue 원문 그대로 반영했다. NW `[가]` 조판 미확인·명시식 계산, NY 해지권과 지급 책임·인과 요건과 실제 인과 추론의 구별, SDSS 연결 부재를 보존했다.
- queue 1,675건·processed 1,675건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 96 groups·360 cases, META28 이후 2 groups·11 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 377건 중 `consumed_sdss` 360건·`prepared` 17건이다. 다음 metadata frontier는 G098이며, 현재 요청에 따라 추가 backlog 준비는 수행하지 않았다.

## 최신 Luna handoff sync — 2026-09-17 G096 완료

- G096 NP·NQ·NR·NS·NT의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 반영했다. NS source hold 해소, 기대 대응 ② 검증, 최초 누락 보존, #60/#69 국소 중첩과 유추·완성 유비 역할 구별을 유지했다.
- queue 1,651건·processed 1,651건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 95 groups·354 cases, META28 이후 1 group·5 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 377건 중 `consumed_sdss` 354건·`prepared` 23건이다. 다음 metadata frontier는 G097이며, 현재 요청에 따라 추가 backlog 준비는 수행하지 않았다.

## 최신 Luna handoff/source sync — 2026-09-17 G096 NS source hold

- `NS-hold-20260917-choice-table-01` 및 후속 `NS-hold-20260917-partial-mapping-02`를 포함한 미처리 raw 5건을 queue 원문 그대로 반영했다. NP·NQ·NR·NT blind 4건도 함께 반영했으며 G096 answer barrier는 유지한다.
- canonical HWPX `고3 기출/2027 고3 국어 독서_Ⅰ. 인문, 독서.hwpx`의 `Contents/section0.xml`에서 NS 선택지 ①~⑤ 전체와 `<보기>` 3열 셀을 확인해 [NS blind source supplement](../../data/기본기_연구/prepared_backlog/blind_sources/NS_canonical_source_supplement.json)로 저장했다. 선택지는 5개 문단 앵커, `<보기>`는 `tbl=1943574696`, `cellAddr=(1,2)`, `cellSpan=(3,1)`로 기록했으며 답·SDSS·해설은 읽지 않았다.
- queue 1,635건·processed 1,635건이며 `record_id` 기준 pending raw는 0건이다. NS source hold 해소 여부와 G096 후속 semantic stage는 Astra가 직접 확인한다.

## 최신 Luna handoff sync — 2026-09-17 META28 반영

- `META-G093-G095-meta_induction-20260917-28` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다.
- queue 1,629건·processed 1,629건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 94 groups·349 cases, `meta_induction_count=28`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 신규 backlog 준비는 보류했다. historical hold G024 DR~DU를 제외한 다음 metadata frontier는 G096 NP부터다.

## 최신 Luna handoff sync — 2026-09-17 G095 완료

- G095 NK·NL·NM·NN·NO의 blind·answer_check·independent_code·sdss_compare raw 20건을 queue 원문 그대로 기존 사례 문서·processed 원장에 반영했다. 사이트 태그 연결 부재를 보존했다.
- queue 1,628건·processed 1,628건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 94 groups·349 cases, META27 이후 3 groups·12 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 377건 중 `consumed_sdss` 349건·`prepared` 28건이다. META28 `meta_induction` 전 새 group semantic stage를 시작하지 않는다.

## 최신 Luna handoff sync — 2026-09-17 G094 완료

- G094 NG·NH·NI·NJ의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 기존 사례 문서·processed 원장에 반영했다. NG #64와 LU 유보를 구별하고, NJ⑤의 목적 추론·필연 추론 구별 및 말미 제목 잔여 한계, SDSS 연결 부재를 보존했다.
- queue 1,608건·processed 1,608건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 93 groups·344 cases, META27 이후 2 groups·7 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 377건 중 `consumed_sdss` 344건·`prepared` 33건이다. 다음 metadata frontier는 G095이며, 새 group semantic stage 전 meta_state를 다시 확인한다.

## 최신 Luna handoff sync — 2026-09-17 G093 완료

- G093 ND·NE·NF의 blind·answer_check·independent_code·sdss_compare raw 12건을 queue 원문 그대로 기존 사례 문서·processed 원장에 반영했다. NF⑤ 본문 정성모형 한계, ND 필요조건의 본문 경로 한정, SDSS 연결 부재를 보존했다.
- queue 1,592건·processed 1,592건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 92 groups·340 cases, META27 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 377건 중 `consumed_sdss` 340건·`prepared` 37건이다. 다음 metadata frontier는 historical hold G024 DR~DU를 제외하면 G094 NG부터이며, 현재 prepared 잔량은 추가 준비 기준(30건 미만)에 해당하지 않는다.

## 최신 Luna handoff sync — 2026-09-17 MF depth_backfill 반영

- `MF-depth_backfill-20260917-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. MF 원답·최초 #46, 유일 주 우선순위 유보, candidates #46/#56과 확정 주 집계 분리를 보존했으며 전역 번호 통합은 수행하지 않았다.
- queue 1,580건·processed 1,580건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 91 groups·337 cases, META27 이후 0 groups·0 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 metadata frontier는 historical hold G024 DR~DU를 제외하면 G093 ND부터다. 신규 group 시작 전 meta_state를 다시 확인한다.

## 최신 Luna handoff sync — 2026-09-17 META27 audit 반영

- `AUDIT-meta27-manual_parity_audit-20260917-09` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. MF depth_backfill 필요 사유와 LU 기존 주 유보를 그대로 보존했다.
- queue 1,579건·processed 1,579건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["MF"]`, `last_manual_parity_audited_meta_count=27`이다.
- MF depth_backfill 완료 전 새 passage group을 시작하지 않는다. backfill은 Astra가 직접 수행한다.

## 최신 Luna handoff sync — 2026-09-17 META27 반영

- `META-G090-G092-meta_induction-20260917-27` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다.
- queue 1,578건·processed 1,578건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 91 groups·337 cases, `meta_induction_count=27`, `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`이다.
- META27 manual parity audit 완료 전 새 passage group을 시작하지 않는다. audit 및 필요한 depth_backfill은 Astra가 직접 수행한다.

## 최신 Luna handoff sync — 2026-09-17 G092 correction 완료

- G092 NB·NC의 official-correction answer_check 2건, independent_code 2건, sdss_compare 2건을 queue 원문 그대로 반영했다. 교정 ID `G092-B-odd-Q29-Q30-20260917`와 원답 보존, `official-correction` 성공 상태를 유지했으며 SDSS 연결 부재는 보존했다.
- queue 1,577건·processed 1,577건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 91 groups·337 cases, META26 이후 3 groups·7 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 377건 중 `consumed_sdss` 337건·`prepared` 40건이다. G092 hold는 해소되었고, META27 `meta_induction` raw 저장·Luna sync·pending=0 검증 전 다음 group을 시작하지 않는다.

## 최신 Luna handoff/source sync — 2026-09-17 G092 crop 보강

- G092의 추가 hold raw 3건을 queue 원문 그대로 반영했다. stale canonical/variant guard 및 crop 범위 한계를 보존했으며 코드·정답 의미를 새로 판정하지 않았다.
- queue 1,571건·processed 1,571건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 90 groups·335 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. NB·NC answer provenance hold는 유지한다.
- 기존 combined crop은 이력으로 보존하고, sealed 아래에 Q29 왼쪽 전체(⑤ 포함), Q30 오른쪽 단독, 시험지 header, 정답표 header crop을 추가했다. supplement에 실제 visible scope와 기존 crop의 하단 잘림·Q31~33 인접 본문 포함 한계를 기록했다.

## 최신 Luna handoff/source sync — 2026-09-17 G092 answer provenance hold

- G092 NB·NC blind 2건, answer_check `needs_astra_review` 2건, `G092-hold-20260917-answer-variant-01` 1건을 queue 원문 그대로 기존 사례 문서·processed 원장에 반영했다. blind 선택과 sealed 기존값은 보존했으며 canonical variant/후보 의미 판정은 Astra 확인 대상으로 남겼다.
- queue 1,569건·processed 1,569건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 90 groups·335 cases, META26 이후 2 groups·5 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. NB·NC는 answer provenance hold로 완료 집계·SDSS 공개를 진행하지 않는다.
- G086에서 확보한 2016 수능 B형 자료를 재사용해 [G092 provenance supplement](../../data/기본기_연구/prepared_backlog/sealed/G092_official_provenance/G092_answer_provenance_supplement_20260917.json), Q29~30 문제 crop, 홀수형 정답표 Q29~30 셀 crop을 sealed 아래에 저장했다. 다른 미진행 문항 정답은 추출하지 않았다. 다음 frontier는 NB·NC provenance의 Astra 직접 시각 대조다.

## 최신 Luna handoff sync — 2026-09-17 G091 완료

- G091 MY·MZ·NA의 independent_code 3건과 sdss_compare 3건을 queue 원문 그대로 기존 사례 문서·processed 원장에 반영했다. 최초 blind·answer_check 기록은 보존했고, SDSS 연결 부재는 사이트 불일치로 세지 않았다.
- queue 1,564건·processed 1,564건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 90 groups·335 cases, META26 이후 2 groups·5 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 377건 중 `consumed_sdss` 335건·`prepared` 42건이다. G091의 #88/#86 국소 중첩 유보와 `[가]` 조판 범위·원배포 정답표 provenance 한계를 유지한다. 다음 actionable frontier는 historical hold G024 DR~DU를 제외한 G092 NB~NC blind다.

## 최신 Luna handoff sync — 2026-09-17 G091 blind·answer_check 반영

- G091 MY·MZ·NA의 blind 3건과 answer_check 3건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. 최초 blind 선택·노출 상태는 보존했고, 세 문항 모두 공식 답 대조까지 완료됐다.
- queue 1,558건·processed 1,558건이며 `record_id` 기준 pending raw는 0건이다. `meta_state.py`: 완료 89 groups·332 cases, META26 이후 1 group·2 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 총 377건 중 `consumed_sdss` 332건·`prepared` 45건이다. G091 전체 independent_code 저장 전 SDSS 공개를 시작하지 않으며, 다음 Astra Excel-style frontier는 **MY independent_code**다. 이후 MZ·NA independent_code를 마친 뒤 group barrier를 확인한다.
- prepared backlog가 30건 이상이므로 후보 추가는 수행하지 않았다. blind packet·sealed answer/SDSS 분리, 중복·노출·source 점검 결과의 기존 경고와 provenance 유보는 변경하지 않았다.

## 최신 Luna handoff sync — 2026-09-17 G090 완료

- G090 MW·MX의 blind·answer_check·independent_code·sdss_compare 후속 raw 7건을 반영했다. MX 그림 source hold 이력은 보존하고, Astra의 직접 그림 판독으로 후속 blind가 유효화되어 group을 완료 집계했다.
- queue 1,552건·processed 1,552건이며 pending raw는 0건이다. `meta_state.py`: 완료 89 groups·332 cases, META26 이후 1 group·2 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 `consumed_sdss` 332건·`prepared` 45건이다. 다음 actionable frontier는 G091 MY이다. MX 곡선은 정성 모형으로만 기록하고 정확비례 주장은 하지 않으며 기존 source provenance 한계를 유지한다.

## 최신 Luna/source sync — 2026-09-17 G090 MX visual source 보강

- G090 MX hold와 관련 raw 2건을 반영해 queue 1,545건·processed 1,545건, pending raw 0건을 확인했다. MX blind 유효화와 그림 의미 판독은 Astra 직접 확인 전까지 완료로 집계하지 않는다.
- MX의 누락 `<그림>`은 canonical HWPX `고3 기출/2027 고3 국어 독서_Ⅲ. 과학.hwpx` `Contents/section0.xml`의 `hc:img binaryItemIDRef=image3` embedded bitmap으로 복원했다. 기존 asset을 재사용했으며 축·중심부 구간·곡선 A/B 라벨을 포함한다.
- provenance와 MX blind source 연결을 갱신했다. 답·SDSS·해설·코드 판정은 열람하지 않았다. 다음은 Astra의 MX 그림 직접 판독이다.

## 최신 Luna handoff sync — 2026-09-17 META26 반영

- `META-G087-G089-meta_induction-20260917-26` raw 1건을 원문 그대로 반영했다. queue 1,543건·processed 1,543건이며 pending raw는 0건이다.
- `meta_state.py`: `meta_induction_count=26`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 다음 frontier는 G090이며 현재 metadata만 보고한다.
- manifest는 `consumed_sdss` 330건·`prepared` 47건이다. 기존 canonical/AB/source 한계와 G086 교정 provenance 유보를 유지한다.

## 최신 Luna handoff sync — 2026-09-17 G089 완료·META26 due

- G089 MU·MV의 blind·answer_check·independent_code·sdss_compare raw 8건을 queue 원문 그대로 반영했다.
- queue 1,542건·processed 1,542건이며 pending raw는 0건이다. `meta_state.py`: 완료 88 groups·330 cases, META25 이후 3 groups·11 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 `consumed_sdss` 330건·`prepared` 47건이다. META26 `meta_induction` 완료 전 다음 group semantic stage를 시작하지 않는다.

## 최신 Luna handoff sync — 2026-09-17 G088 완료

- G088 MQ·MR·MS·MT의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 반영했다. variant AB 후보 유일값 guard 통과와 AB 두 형식의 번호·선지 동일성 신규 검증은 구분해 보존했다.
- queue 1,534건·processed 1,534건이며 pending raw는 0건이다. `meta_state.py`: 완료 87 groups·328 cases, META25 이후 2 groups·9 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 `consumed_sdss` 328건·`prepared` 49건이다. 다음 actionable frontier는 G089 MU이다.

## 최신 Luna handoff sync — 2026-09-17 G087 완료

- G087 ML·MM·MN·MO·MP의 blind·answer_check·independent_code·sdss_compare raw 20건을 queue 원문 그대로 반영했다. A형 candidate/answer 일치 guard 확인은 실제 공식 정답표 신규 확인과 구분해 보존했다.
- queue 1,518건·processed 1,518건이며 pending raw는 0건이다. `meta_state.py`: 완료 86 groups·324 cases, META25 이후 1 group·5 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 `consumed_sdss` 324건·`prepared` 53건이다. G086 교정값과 canonical 전수 미검증 유보를 유지한다. 다음 actionable frontier는 G088 MQ이다.

## 최신 Luna handoff sync — 2026-09-17 META25 반영

- `META-G084-G086-meta_induction-20260917-25` raw 1건을 원문 그대로 반영했다. queue 1,498건·processed 1,498건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 85 groups·319 cases, `meta_induction_count=25`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. META25는 G084~G086 window를 닫았고 다음 actionable frontier는 G087 ML이다.
- G086 variant fallback 교정에 따라 명시 variant 일치·후보 충돌 guard와 8회귀 검증, Python compile·Node syntax 통과를 기록했다. 기존 canonical 자료 전수 재생성·재검증은 수행하지 않았다.
- META25 raw의 `同じ` 표기는 immutable 원문으로 유지한다. 기존 LU #56/#64 유보와 G086 provenance·SDSS 연결 부재도 그대로 보존한다.

## 최신 Luna handoff sync — 2026-09-17 G086 official correction 완료·META25 due

- G086 MH~MK의 official-correction answer_check·independent_code·sdss_compare raw 12건을 반영했다. 최초 blind 선택은 보존하고, sealed의 기존 답은 역사값으로 유지하며 B형 홀수형 공식표 매핑 교정값 ⑤·①·①·④를 현 유효값으로 기록했다.
- 각 correction record에는 `original_official_answer`, `corrected_official_answer`, `answer_mapping_status="superseded_wrong_variant_A_for_B"`, correction ID·sealed supplement 경로를 추가했다. canonical DB는 재작성하지 않았다.
- queue 1,497건·processed 1,497건이며 pending raw는 0건이다. `meta_state.py`: 완료 85 groups·319 cases, META24 이후 3 groups·12 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- G086 hold는 source mapping correction으로 해소되었고 최초 blind 수정으로 기록하지 않는다. SDSS 연결 부재는 유지한다. META25 window는 G084~G086이며, 귀납 전 다음 group semantic stage를 시작하지 않는다.

## 최신 Luna handoff sync — 2026-09-17 G086 provenance guard 보강

- `G086-hold-20260917-answer-variant-03` raw 1건을 반영해 queue 1,485건·processed 1,485건, pending raw 0건을 확인했다. G086 answer conflict와 variant fallback 원인 raw는 의미 변경 없이 보존한다.
- G086 공식 문제·정답 원문과 Q17~20 한정 crop을 `prepared_backlog/sealed/G086_official_provenance/`로 이동했다. supplement 내부 경로도 sealed로 갱신했으며 blind_sources에는 답 포함 provenance 자료를 남기지 않았다.
- Q17~20 문제 지면 crop, B형 홀수형 정답표 제목·Q17~20 표 부분 crop의 페이지 인덱스·hash를 supplement에 기록했다. G086 SDSS·후속 의미 판정은 계속 hold다.

## 최신 Luna handoff sync — 2026-09-17 G086 answer provenance hold

- G086 MH~MK의 answer_check needs_astra_review 4건과 answer provenance hold 2건을 포함해 신규 raw 10건을 반영했다. queue 1,484건·processed 1,484건이며 pending raw는 0건이다.
- canonical metadata로 G086을 2016학년도 수능 국어 B형 홀수형 17~20번으로 식별하고, 제3자 보관 문제 PDF와 B형 홀수형 정답표 원문을 별도 supplement에 저장했다. 공식표 매핑은 MH=17→⑤, MI=18→①, MJ=19→①, MK=20→④이며 sealed 기존 값은 덮어쓰지 않았다.
- 현재 G086은 answer provenance conflict hold이며 SDSS 공개·후속 semantic stage를 시작하지 않는다. `meta_state.py`: 완료 84 groups·315 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`. manifest는 `consumed_sdss` 315건·`prepared` 62건이다.

## 최신 Luna handoff sync — 2026-09-17 G085 완료

- G085 MD·ME·MF·MG의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 반영했다. 기존 판정·source 한계·LU 유보는 변경하지 않았다.
- queue 1,474건·processed 1,474건이며 pending raw는 0건이다. `meta_state.py`: 완료 84 groups·315 cases, META24 이후 2 groups·8 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 `consumed_sdss` 315건·`prepared` 62건이다. G024 DR~DU historical hold를 제외한 다음 actionable frontier는 G086 MH이다.

## 최신 Luna handoff sync — 2026-09-17 G084 완료

- G084 LZ·MA·MB·MC의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 반영했다. LU depth_backfill의 주 코드 유보와 기존 source·노출 한계는 변경하지 않았다.
- queue 1,458건·processed 1,458건이며 pending raw는 0건이다. `meta_state.py`: 완료 83 groups·311 cases, META24 이후 1 group·4 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 `consumed_sdss` 311건·`prepared` 66건이다. G024 DR~DU 4건 historical hold를 제외한 다음 actionable frontier는 G085 MD~MG이다.

## 최신 Luna handoff sync — 2026-09-17 LU depth_backfill 반영

- `LU-depth_backfill-20260917-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. 최초 #56 판정·#64 보조 이력은 보존하고, `primary_candidates=[56,64]`, `revised_primary=[]` 및 유일 주 코드 우선순위 유보를 그대로 유지했다.
- queue 1,442건·processed 1,442건이며 pending raw는 0건이다. `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 frontier는 G084이며, 현재는 metadata만 보고한다. manifest는 `consumed_sdss` 307건·`prepared` 70건이다.

## 최신 Luna handoff sync — 2026-09-17 META24 manual parity audit 반영

- `AUDIT-meta24-manual_parity_audit-20260917-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,441건·processed 1,441건이며 pending raw는 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `last_manual_parity_audited_meta_count=24`, `depth_backfill_pending=["LU"]`이다. 감사 raw가 지정한 LU depth_backfill 완료 전 G084 semantic stage를 시작하지 않는다.
- LU의 #56 서술 기능 주 판정과 #56/#64 최소 판별 근거 gap, LR crop·XML 범위 구별 및 기존 hold 이력은 raw 의미 그대로 보존했다.

## 최신 Luna handoff sync — 2026-09-17 META24 반영·manual parity audit due

- `META-G081-G083-meta_induction-20260917-24` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,440건·processed 1,440건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 82 groups·307 cases, `meta_induction_count=24`, `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`이다. 다음 허용 작업은 META24 manual parity audit이며, audit 완료 전 G084 semantic stage를 시작하지 않는다.
- META24의 LR source correction은 공식 형식 PDF crop 직접 확인, XML insertion anchor와 실제 bracket 범위 구별, 제3자 보관 EBSi PDF provenance라는 raw 의미를 그대로 보존했다. manifest는 `consumed_sdss` 307건·`prepared` 70건이다.

## 최신 Luna handoff sync — 2026-09-17 G083 완료·META24 due

- G083 LU·LV·LW·LX·LY의 blind·answer_check·independent_code·sdss_compare raw 20건을 queue 원문 그대로 반영했다. 기존 노출·source 한계와 Astra 판정을 변경하지 않았다.
- queue 1,439건·processed 1,439건이며 pending raw는 0건이다. `meta_state.py`: 완료 82 groups·307 cases, META23 이후 3 groups·12 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- META24 window는 G081~G083(LN~LY, 12 cases)이며, META24 `meta_induction` raw 저장·Luna sync·pending=0 검증 전 다음 group semantic stage를 시작하지 않는다. manifest는 `consumed_sdss` 307건·`prepared` 70건이다.

## 최신 Luna handoff sync — 2026-09-17 G082 완료

- G082 LQ·LR·LS·LT의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 반영했다. LR은 공식 형식 PDF crop을 Astra가 직접 확인해 `[A]` 범위를 보강했으며, 이전 XML anchor/topology 기반 확정 주장은 배제하고 hold 이력을 보존했다.
- queue 1,419건·processed 1,419건이며 pending raw는 0건이다. `meta_state.py`: 완료 81 groups·302 cases, META23 이후 2 groups·7 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 377건 중 `consumed_sdss` 302건·`prepared` 75건이다. 다음 Astra frontier는 G083 LU~LY이며, G024 DR~DU 4건은 historical preexposure hold로 유지한다.

## 최신 Luna handoff sync — 2026-09-17 G082 blind hold

- LQ·LS·LT blind raw 3건과 LR source-range hold raw 2건을 queue 원문 그대로 반영했다. queue 1,405건·processed 1,405건이며 pending raw는 0건이다.
- LR은 [A] 세로괄호 전체 범위 evidence가 확인되지 않아 `needs_astra_review` hold를 유지한다. G082 전체 blind barrier 전 answer_check·independent_code·SDSS 공개를 시작하지 않는다.
- `meta_state.py`: 완료 80 groups·298 cases, META23 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- manifest는 377건 중 `consumed_sdss` 298건·`prepared` 79건이다. blind source 누락 0건, blind packet 금지 필드 점검 0건, 후보 중복 0건을 확인했다. 다음 Astra Excel-style case ID는 **LR**이며, 우선 공식 형식의 [A] 범위 source 보강/직접 판독이다.

## 최신 Luna sync — 2026-09-17 G081 완료

- G081 LN·LO·LP의 12단계 raw와 `LN-boundary_revision` 1건을 queue 원문 그대로 사례 문서·processed 원장에 반영했다. queue 1,400건·processed 1,400건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 80 groups·298 cases, META23 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- LN 최초 #31 보조→후속 #31 표면 수정 raw를 모두 보존했다. 축소 수식 supplement 직접 확인은 answer 공개 후였고 결정 근거 불필수였다는 timing qualification도 유지했다. 다음 Astra frontier는 실제 group G082 LQ부터다.

## 최신 Luna sync — 2026-09-17 META23 반영

- `META-G078-G080-meta_induction-20260917-23` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,387건·processed 1,387건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 79 groups·295 cases, `meta_induction_count=23`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 다음 Astra frontier는 G081 LN~LP다.

## 최신 Luna sync — 2026-09-17 G080 완료·META23 due

- G080 LL·LM의 blind·answer_check·independent_code·sdss_compare raw 8건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,386건·processed 1,386건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 79 groups·295 cases, META22 이후 3 groups·8 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 허용 작업은 META23 `meta_induction`(G078~G080, 8 cases)이다. META23 완료 전 G081 semantic stage를 시작하지 않는다.

## 최신 Luna sync — 2026-09-17 G079 완료

- G079 LJ·LK의 최초 blind·source 보강·hold·answer_check·independent_code·sdss_compare pending raw 11건을 queue 원문 그대로 반영했다. queue 1,378건·processed 1,378건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 78 groups·293 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- LJ equation, LK 표 오매핑 교정과 정확표, 두 풀이 경로 및 최초 blind 기록을 보존했다. 다음 Astra frontier는 실제 manifest상 G080 LL~LM이다.

## 최신 Luna source restoration — 2026-09-17 G079 LJ

- G079 LJ 선택지 ①의 누락 수식을 canonical HWPX `고3 기출/2027 고3 국어 독서_Ⅲ. 과학.hwpx` `Contents/section0.xml`에서 확인했다. `hp:equation id="1947855565"`, script `{1} over {9}`이며 번호·앞뒤 텍스트 anchor와 LK 표 cell mapping은 `LJ_LK_canonical_supplement_20260917.json`에 보존했다.
- LJ/LK blind source에 supplement 경로와 manifest provenance를 기계적으로 연결했다. 답·SDSS·의미 판단은 수행하지 않았다. LJ는 Astra source hold 해소 후 직접 blind 판독한다.

## 최신 Luna sync — 2026-09-17 G078 완료

- G078 LF·LG·LH·LI의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 기계적으로 반영했다. queue 1,367건·processed 1,367건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 77 groups·291 cases, META22 이후 1 group·4 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 기존 source·노출·판정 한계는 변경하지 않았다. 다음 Astra frontier는 실제 manifest상 G079 LJ부터 시작한다.

## 최신 Luna sync — 2026-09-17 META22 반영

- `META-G075-G077-meta_induction-20260917-22` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 기계적으로 반영했다. queue 1,351건·processed 1,351건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 76 groups·287 cases, `meta_induction_count=22`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 Astra frontier는 실제 manifest상 G078 LF부터 시작한다.

## 최신 Luna sync — 2026-09-17 G077 완료·META22 due

- G077 LB·LC·LD·LE의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 기계적으로 반영했다. 마지막 case LE까지 포함해 queue 1,350건·processed 1,350건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 76 groups·287 cases, META21 이후 3 groups·11 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 허용 작업은 META22 `meta_induction`(G075~G077, 11 cases)이며 완료 전 신규 group semantic stage를 시작하지 않는다.

## 최신 Luna sync — 2026-09-17 G076 완료

- G076 KX·KY·KZ·LA의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 기계적으로 반영했다. queue 1,334건·processed 1,334건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 75 groups·283 cases, META21 이후 2 groups·7 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- KY 필요조건 부정 조건 근거, KZ 지리·관계 집단 유보, 독립 판단 후 sealed source 식별 순서는 raw payload 그대로 보존했다. 다음 Astra frontier는 G077 LB~LD 등 manifest상 다음 group이다.

## 최신 Luna sync — 2026-09-17 G075 완료

- G075 KU·KV·KW의 blind·answer_check·independent_code·sdss_compare raw 12건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 기계적으로 반영했다. queue 1,318건·processed 1,318건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 74 groups·279 cases, META21 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 다음 Astra frontier는 G076 KX~LA blind다.

## 최신 Luna sync — 2026-09-17 KT depth backfill 반영

- `KT-depth_backfill-20260917-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 기계적으로 반영했다. 후속 주 우선순위 #15, 보조 #100·#96 및 최초 #100 판정을 보존했다. queue 1,306건·processed 1,306건이며 pending raw는 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 다음 Astra frontier는 G075 KU~KW blind다.

## 최신 Luna sync — 2026-09-17 META21 manual parity audit 반영

- `AUDIT-meta21-manual_parity_audit-20260917-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 기계적으로 반영했다. queue 1,305건·processed 1,305건이며 pending raw는 0건이다.
- `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `last_manual_parity_audited_meta_count=21`, `depth_backfill_pending=["KT"]`이다.
- 다음 Astra 작업은 KT depth backfill이며, 완료 전 G075 semantic stage를 시작하지 않는다.

## 최신 Luna sync — 2026-09-17 META21 반영·manual parity audit due

- `META-G072-G074-meta_induction-20260917-21` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 기계적으로 반영했다. queue 1,304건·processed 1,304건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 73 groups·276 cases, `meta_induction_count=21`, `meta_due=false`, `manual_parity_audit_due=true`, `manual_parity_audits_remaining_to_next=0`, `depth_backfill_pending=[]`이다.
- 다음 Astra 작업은 `for_meta_count=21` manual parity audit이다. 감사 전 새 semantic stage·group은 시작하지 않는다.

## 최신 Luna sync — 2026-09-17 G074 완료·META21 due

- G074 KQ·KR·KS·KT의 후속 answer_check·independent_code·sdss_compare raw 13건을 queue 원문 그대로 사례 문서와 processed 원장에 반영했다. queue 1,303건·processed 1,303건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 73 groups·276 cases, META20 이후 3 groups·11 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 다음 허용 작업은 META21 `meta_induction`(G072~G074, 11 cases)이며 그 전 새 group을 시작하지 않는다.
- KS visual supplement의 좌표는 `approximate_rectangular_regions_not_panel_boundaries` qualification을 명시했다. 그림 의미·코드 판정은 raw payload를 변경하지 않았다.

## 최신 Luna source restoration — 2026-09-17 G074 KS

- G074 KS의 누락된 보기 만화 bitmap을 로컬 canonical HWPX `고3 기출/2027 고3 국어 독서_Ⅴ. 예술.hwpx`의 `Contents/section0.xml` `binaryItemIDRef="image2"`에서 복원했다. 원본 asset은 `data/기본기_연구/prepared_backlog/blind_sources/KS_assets/KS_comic_original.bmp`, 칸 󰊱~󰊶 좌표 연결은 `KS_visual_supplement_20260917.json`에 보존했다.
- 답·SDSS·그림 의미는 열람하거나 판단하지 않았다. KS hold raw와 KR·KT blind raw를 포함해 queue 1,290건·processed 1,290건, pending raw 0건이다. KS blind 유효화 및 G074 후속 단계는 Astra가 직접 그림을 판독한 뒤 진행한다.

## 최신 Luna sync — 2026-09-17 G073 완료

- G073 KN·KO·KP의 blind·answer_check·independent_code·sdss_compare raw 12건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 기계적으로 반영했다. queue 1,286건·processed 1,286건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 72 groups·272 cases, META20 이후 2 groups·7 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- KP 복원 그림 직접 판독 및 KO 경로별 주 코드 유보는 raw payload 그대로 보존했다. 다음 Astra frontier는 G074 KQ~KT blind다.

## 최신 Luna sync — 2026-09-17 G072 완료

- G072 KJ·KK·KL·KM의 blind·answer_check·independent_code·sdss_compare raw 16건과 후속 `G072-boundary_revision-20260917-01` raw 1건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 기계적으로 반영했다. queue 1,274건·processed 1,274건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 71 groups·269 cases, META20 이후 1 group·4 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- KL 논리 표기 관련 유보, 후속 경계 수정 raw, G072의 SDSS 연결·출처 qualification은 원문 그대로 보존했다. 다음 Astra frontier는 G073 KN~KP blind다.

## 최신 Luna sync — 2026-09-17 META20 반영

- `META-G069-G071-meta_induction-20260917-20` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 기계적으로 반영했다. queue 1,257건·processed 1,257건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 70 groups·265 cases, `meta_induction_count=20`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- META20의 기존 경계·반례·노출 유보는 raw payload 그대로 보존했다. 다음 Astra frontier는 G072 KJ~KM blind다.

## 최신 Luna sync — 2026-09-17 G071 완료·META20 due

- G071 KF·KG·KH·KI의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 기계적으로 반영했다. queue 1,256건·processed 1,256건이며 pending raw는 0건이다.
- `meta_state.py`: 완료 70 groups·265 cases, META19 이후 3 groups·10 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- G071의 준비 자료 SDSS 연결 부재와 원배포 PDF 직접 대조 아님이라는 qualification을 유지했다. 독립 코드·경계 판단은 raw payload를 변경하지 않았다.
- 다음 Astra 작업은 G069~G071 및 JZ~KI 10 cases를 대상으로 한 META20 `meta_induction`이다. META20 raw 저장·Luna sync·pending raw=0 검증 전에는 G072 semantic stage를 시작하지 않는다.

## 최신 source restoration — 2026-09-17

- 사용자 지정 12개 group(G071, G072, G073, G074, G075, G081, G084, G086, G090, G095, G096, G098)의 46개 blind source를 로컬 canonical HWPX XML 기준으로 복원했다.
- 선택지 복원 대상 KI·KM·KO·KT·KW·MC·MI·NO·NT·OE는 `hp:t` 후행 텍스트까지 회수하여 5개 선택지로 저장했다. G073의 KP 등 사용자가 지정하지 않은 case의 기존 canonical placeholder는 의미적으로 보완하지 않았다.
- LO(G081)는 HWPX `image6`, MX(G090)는 HWPX `image3` embedded bitmap을 BMP/PNG로 보존하고 blind supplement로 연결했다.
- 12개 group은 mechanical completeness를 통과하여 `READY`로 승격했다. semantic 풀이·정답 확인·코드 판정·SDSS 대조는 수행하지 않았다.
- G101 이후 frontier와 source는 준비하지 않았다. 상세 복원 결과는 `data/기본기_연구/prepared_backlog/SOURCE_RESTORE_20260917.md` 및 JSON에 보존했다.

## 최신 Luna prepared-backlog preflight — 2026-09-17

- `분석/기본기_연구/LUNA_PREPARE_FRONTIER.md` 지시에 따라 의미적 연구 없이 G071~G100의 연속 30개 KICE passage group을 기계적으로 검사했다.
- 새 `READY`는 18 groups·66 cases이며 manifest는 `consumed_sdss` 261건, historical preexposure hold 4건, 새 actionable prepared 66건이다. 연구 완료 집계·meta_state·Astra queue/processed는 변경하지 않았다.
- G071 KF~KI, G072 KJ~KM, G073 KN~KP, G074 KQ~KT, G075 KU~KW, G084 LZ~MC, G086 MH~MK, G095 NK~NO, G096 NP~NT, G098 OA~OE는 텍스트/선지 완전성 또는 choice parse가 미완전하여 `UNRESOLVED`로 등록하지 않고 보고서에 보류했다.
- G081 LN~LP 및 G090 MW~MX는 시각자료 placeholder가 있으나 blind-safe asset 연결을 확인하지 못해 `NEEDS_RESTORE`로 보류했다. 이번 preflight에서 복원한 asset은 없다.
- 기계적으로 정확한 SDSS linkage는 새 준비 cases에서 0건이며, 답·태그는 sealed에만 분리했다. 상세 결과는 `data/기본기_연구/prepared_backlog/LUNA_FRONTIER_PREFLIGHT_20260917.md`에 보존했다.
- 다음 준비 frontier는 G101 이후이며, 현재 Astra가 즉시 시작할 수 있는 첫 READY group은 G076 KX~LA이다. G071 KF는 source 복원 전까지 유효 blind frontier로 진행하지 않는다.

## 최신 Luna sync — 2026-09-16 최종 G061~G070 후처리

- 마지막 `META-G069-G070-induction-20260916-01` raw 1건을 원문 그대로 반영했다. queue 1,240건·processed 1,240건이며 pending raw는 0건이다. 세션 시작 1,111건 대비 신규 raw는 129건이며, G061~G070 신규 10 groups·29 cases를 반영해 누적 69 groups·261 cases가 되었다.
- 정기 meta baseline은 19로 유지하고, META17·META18·META19, META18 manual audit, JI·JQ·JY·JE·JK depth_backfill 5건의 처리 상태를 기계적으로 확인했다. `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 최신 manifest는 `consumed_sdss` 261건, historical preexposure hold 4건(DR~DU), actionable prepared 0건이다. 다음 frontier는 아직 준비되지 않은 G071 KF blind이며 G024 hold는 신규 blind로 되돌리지 않는다.
- quota는 모든 실조회가 unavailable 상태였고 emergency 또는 `<=7%` 관측은 없었다. 새 semantic/source/backlog는 추가하지 않았으며 기존 판정·provenance·노출 유보를 유지했다.

## 최신 Luna sync — 2026-09-16 G070 완료

- KC·KD·KE의 blind·answer_check·independent_code·sdss_compare raw 12건을 원문 그대로 반영했다. queue 1,239건·processed 1,239건이며 pending raw는 0건이다.
- `meta_state.py` 결과: 완료 69 passage groups·261 cases, META19 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- KE 말미 `## 2015학년도` 경계 잔재는 group 식별정보로 확정하지 않고 3 cases의 노출 qualification 원문을 유지했다. 최신 manifest는 `consumed_sdss` 261건이며 G024 DR~DU 4건만 historical preexposure hold다.
- 다음 frontier는 아직 준비되지 않은 G071 KF blind다. G024 hold를 신규 blind로 되돌리지 않는다.

## 최신 Luna sync — 2026-09-16 G069 완료

- KB blind·answer_check·independent_code·sdss_compare raw 10건을 원문 그대로 반영했다. queue 1,227건·processed 1,227건이며 pending raw는 0건이다.
- KB 선택 그래프 hold는 로컬 이미지·번호 anchor 확인 범위에서 해소했다. 선형 감쇄 모형과 원배포 PDF 직접 검증 유보를 유지했다. `meta_state.py`: 완료 68 groups·258 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 Astra frontier는 G070 KC·KD·KE blind다. 최신 manifest prepared는 G024 DR~DU historical hold 4건과 G070 KC~KE 3건이다.

## 최신 Luna sync — 2026-09-16 G069 source checkpoint

- JZ·KA blind, KB source hold, JY depth_backfill raw 4건을 원문 그대로 반영했다. queue 1,217건·processed 1,217건이며 pending raw는 0건이다.
- KB 선택 그래프 5개 누락으로 hold를 유지하고 답·태그를 공개하지 않았다. JY 로컬 표 `cellAddr` 보강은 의미 불변으로 반영했으며 `meta_state.py`: 완료 67 groups·255 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 유효 blind는 KB source 복원 후 KB blind다. G069 완료 집계는 증가시키지 않았다.

## 최신 Luna sync — 2026-09-16 META19 반영

- `META-G066-G068-meta_induction-20260916-19` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,213건·processed 1,213건이며 pending raw는 0건이다.
- `meta_state.py` 결과: 완료 67 passage groups·255 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `meta_induction_count=19`이다.
- JU 문맥 추론·미명시 거리 출력 한계, JY 그림 출처 범위, JE 이전 유보를 보존했다. 다음 Astra frontier는 G069 JZ·KA·KB blind다.

## 최신 Luna sync — 2026-09-16 G068 완료·META19 due

- JW·JX·JY의 blind·answer_check·independent_code·sdss_compare raw 12건을 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,212건·processed 1,212건이며 pending raw는 0건이다.
- `meta_state.py` 결과: 완료 67 passage groups·255 cases, META18 이후 3 groups·8 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- JY 그림은 공통 장치도이며 출력 수치표 원화가 아니라는 한계를 보존한다. 다음 허용 단계는 META19 `meta_induction`이며, 그 전 G069 semantic stage를 시작하지 않는다.

## 최신 기계 상태 점검 — 2026-09-16 G068 이후 준비 잔량

- 최신 manifest 265건을 직접 집계했다. `consumed_sdss` 252건, `prepared` 13건이며, G024 DR~DU 4건은 historical preexposure hold, G068 JW·JX·JY·G069 JZ·KA·KB·G070 KC·KD·KE 9건이 다음 actionable prepared다.
- G065 JP·JQ, G066 JR·JS, G067 JT·JU·JV는 모두 `consumed_sdss`로 기계 상태가 정합한다. 중복·누락 정리는 필요하지 않았다.

## 최신 Luna sync — 2026-09-16 G067 완료

- JU source 보강 blind 1건과 JT·JU·JV의 answer_check·independent_code·sdss_compare raw 9건을 직전 checkpoint 뒤 원문 그대로 반영했다. queue 1,200건·processed 1,200건이며 pending raw는 0건이다.
- JU 거리 출력 미명시 유보와 조건역 자동 추론 금지, JV 기하 대칭 정성 예측 범위를 유지했다. G067 도식 source 대기는 로컬 범위에서 해소했고 원배포 PDF 직접 검증 한계는 유지했다. `meta_state.py`: 완료 66 groups·252 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 Astra frontier는 G068 JW·JX·JY blind다. JY 그림 복원 경로가 준비되어 있다.

## 최신 Luna sync — 2026-09-16 G067 blind source checkpoint

- JT·JU·JV blind raw 3건을 원문 그대로 반영했다. queue 1,190건·processed 1,190건이며 pending raw는 0건이다.
- JU 본문의 집/A/B 경로 도식은 추가 복원 대기 상태이며, 최초 선택 ③과 근거 범위·그림 누락 유보를 유지한다. 답·태그는 미열람이고 완료 집계는 증가시키지 않았다. `meta_state.py`: 완료 65 groups·249 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 단계는 JU 도식 Astra 확인 후 G067 전체 answer_check이며, 필요 시 blind 보강을 먼저 한다.

## 최신 Luna sync — 2026-09-16 G066 완료

- JS blind·answer_check·independent_code·sdss_compare raw 7건을 직전 checkpoint 뒤 원문 그대로 반영했다. queue 1,187건·processed 1,187건이며 pending raw는 0건이다.
- JS source hold는 blind payload의 직접 도식 판독으로 해소된 범위만 반영하고 원배포 PDF 직접 검증 유보를 유지했다. `meta_state.py`: 완료 65 groups·249 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 Astra frontier는 G067 JT·JU·JV blind다. JV 그림 복원 경로는 준비된 상태이며 새 source 준비는 수행하지 않았다.

## 최신 Luna sync — 2026-09-16 G066 source-hold checkpoint

- `JR-blind-20260916-01`과 `JS-hold-20260916-source-01` raw 2건을 원문 그대로 반영했다. queue 1,180건·processed 1,180건이며 pending raw는 0건이다.
- JS 그림은 source 복원 대기로 `needs_astra_review`를 보존한다. JR의 답·코드·SDSS와 JS의 답·태그는 아직 공개하지 않았고, G066 완료 집계도 증가시키지 않았다. `meta_state.py`: 완료 64 groups·247 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 유효 blind는 JS source 복원 후 JS blind이며, 같은 group의 답·코드·SDSS는 JS blind 완료 전 공개하지 않는다.

## 최신 Luna sync — 2026-09-16 JK depth_backfill 반영

- `JK-depth_backfill-20260916-audit18-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,178건·processed 1,178건이며 pending raw는 0건이다.
- XML 셀 대응 보강과 원배포 PDF 직접 검증 유보를 분리해 보존했다. `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 다음 Astra frontier는 G066 JR·JS blind다.

## 최신 Luna sync — 2026-09-16 JE depth_backfill 반영

- `JE-depth_backfill-20260916-audit18-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,177건·processed 1,177건이며 pending raw는 0건이다.
- 최초 주 코드 75를 유지하고, 치중→한정 일반화 불인정 및 배타적 해석의 잔여 간극 유보를 payload대로 보존했다. `meta_state.py`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["JK"]`.
- 다음 허용 단계는 JK depth_backfill이며 완료 전 G066을 시작하지 않는다.

## 최신 Luna sync — 2026-09-16 META18 manual parity audit 반영

- `AUDIT-meta18-manual_parity_audit-20260916-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,176건·processed 1,176건이며 pending raw는 0건이다.
- `meta_state.py` 결과: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["JE", "JK"]`, `last_manual_parity_audited_meta_count=18`이다. audit의 점수·유보 의미는 수정하지 않았다.
- 다음 허용 단계는 JE·JK depth_backfill이며, 두 backfill 완료 전 G066 신규 semantic stage를 시작하지 않는다. JK supplement는 Astra raw가 없는 상태를 유지한다.

## 최신 Luna sync — 2026-09-16 META18 반영·manual audit due

- `META-G063-G065-meta_induction-20260916-18` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,175건·processed 1,175건이며 pending raw는 0건이다.
- `meta_state.py` 결과: 완료 64 passage groups·247 cases, `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`, `meta_induction_count=18`이다.
- 다음 허용 단계는 manual parity audit이며, audit 완료 전 G066 신규 semantic stage를 시작하지 않는다. JK 표 supplement는 확보 상태만 보존하고 Astra 의미 raw가 없어 추가 반영하지 않았다.

## 최신 Luna sync — 2026-09-16 JQ depth_backfill 반영

- `JQ-depth_backfill-20260916-source-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,174건·processed 1,174건이며 pending raw는 0건이다.
- Astra의 복원 도식 PNG 직접 판독 결과는 payload대로 보존하고, 원배포 PDF 미검증 유보를 유지했다. `meta_state.py`는 `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. JK 표 보강은 semantic raw가 없어 반영하지 않았다.
- 다음 허용 단계는 META18 `meta_induction`이다.

## 최신 Luna sync — 2026-09-16 G065 완료·META18 due

- JP·JQ의 blind·answer_check·independent_code·sdss_compare raw 8건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,173건·processed 1,173건이며 pending raw는 0건이다.
- `meta_state.py` 결과: 완료 64 passage groups·247 cases, META17 이후 3 groups·8 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 허용 단계는 META18 `meta_induction`이며, 이후 manual parity audit due를 확인한다. JQ 도식은 기계 복원 상태를 보존하고 Astra 미열람에 따른 기존 source 유보를 유지한다. prepared actionable은 G066~G070 JR~KE 18건이며 G024 DR~DU 4건은 historical hold다.

## 최신 Luna sync — 2026-09-16 G064 완료

- JN·JO의 blind·answer_check·independent_code·sdss_compare raw 8건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,165건·processed 1,165건이며 pending raw는 0건이다.
- `meta_state.py` 결과: 완료 63 passage groups·245 cases, META17 이후 2 groups·6 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 Astra frontier는 G065 JP·JQ blind다. manifest prepared actionable은 G065~G070 JP~KE 20건이며 G024 DR~DU 4건은 historical preexposure hold로 유지한다.

## 최신 Luna sync — 2026-09-16 JI depth_backfill 반영

- `JI-depth_backfill-20260916-source-01` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,157건·processed 1,157건이며 pending raw는 0건이다.
- 로컬 HWPX 헤더·셀 순서 확인으로 JI 표 전사 유보를 로컬 범위에서만 보강했으며, 원배포 PDF 직접 대조 유보와 최초 판단은 유지한다. `meta_state.py`는 `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 Astra frontier는 G064 JN·JO blind다.

## 최신 Luna sync — 2026-09-16 G063 완료

- JJ·JK·JL·JM의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,156건·processed 1,156건이며 pending raw는 0건이다. queue 원문은 변경하지 않았다.
- `meta_state.py` 결과: 완료 62 passage groups·243 cases, META17 이후 1 group·4 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 Astra frontier는 G064 JN·JO blind다. manifest prepared actionable은 G064~G070 JN~KE 22건이며 G024 DR~DU 4건은 historical preexposure hold로 유지한다.

## 최신 Luna sync — 2026-09-16 META17 반영

- `META-G060-G062-meta_induction-20260916-17` raw 1건을 원문 그대로 독립연구 진행 기록과 processed 원장에 반영했다. queue 1,140건·processed 1,140건이며 pending raw는 0건이다. queue 원문은 변경하지 않았다.
- `meta_state.py` 결과: 완료 61 passage groups·239 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `meta_induction_count=17`이다.
- 다음 Astra frontier는 G063 JJ·JK·JL·JM blind다. manifest prepared는 G024 historical preexposure hold 4건과 G063~G070 JN~KE 26건이며, G063은 JJ~JM으로 정확히 구분한다.

## 최신 Luna sync — 2026-09-16 G062 완료·META17 due

- JG·JH·JI의 blind·answer_check·independent_code·sdss_compare raw 12건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,139건·processed 1,139건이며 pending raw는 0건이다. queue 원문은 변경하지 않았다.
- `meta_state.py` 결과: 완료 61 passage groups·239 cases, META16 이후 3 groups·8 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 허용 단계는 root가 작성할 META17 `meta_induction` raw이며, 그 전까지 신규 semantic stage를 시작하지 않는다. manifest prepared 잔량은 G024 historical hold 4건과 G063~G070 JN~KE 26건이다.

## 최신 Luna sync — 2026-09-16 G061 완료

- JC·JD·JE·JF의 blind·answer_check·independent_code·sdss_compare raw 16건을 queue 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 1,127건·processed 1,127건이며 `record_id` 기준 pending raw는 0건이다. queue 원문은 변경하지 않았다.
- JD의 ⓐ 범위 보강은 independent payload대로 로컬 HWPX 검증으로 보존했다. 최초 blind의 밑줄 범위 한계와 공식 배포 PDF 직접 시각 대조 아님이라는 유보를 덮어쓰지 않았다. G061 네 사례의 SDSS 연결은 빈 배열이므로 판단 보류 상태를 유지한다.
- `meta_state.py` 결과: 완료 60 passage groups·236 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. manifest는 G061까지 `consumed_sdss` 236건이며 G024 historical preexposure hold 4건과 다음 준비 frontier G062 JG·JH·JI, G063 JJ~JM이 남아 있다.
- 다음 Astra frontier는 G062 JG·JH·JI blind다. 새 source 준비·의미 판정은 이번 sync에서 수행하지 않았다.

## 최신 Luna sync — 2026-09-15 G060 완료·prepared frontier 소진

- 이번 세션 시작 시점의 실제 완료 집계는 50 passage groups·206 cases였고, G052~G060 후속 raw와 META14·META15·META16, META15 audit, IO·IK depth_backfill을 반영한 최종 실제 집계는 59 passage groups·232 cases다. 이번 G060 JB answer_check·independent_code·sdss_compare raw 3건도 원 payload 그대로 반영했다. queue 원문은 변경하지 않았다.
- `meta_state.py` 최종 결과: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 기존 유보·provenance qualification·사전노출 hold는 변경하지 않았다.
- manifest prepared 4건은 모두 G024 DR·DS·DT·DU historical preexposure hold이며 actionable 잔량은 0건이다. 다음 Excel-style case `JC`는 아직 준비되지 않았다. 추가 신규 준비와 별도 비독립 검토는 후속 작업으로 남기고 이번 sync에서는 수행하지 않았다.

## 최신 Luna sync — 2026-09-15 G051 완료

- G051 HY·HZ·IA·IB의 blind·answer_check·independent_code·sdss_compare raw 16건을 원문 그대로 기존 사례 문서와 processed 원장에 반영했다. queue 994건·processed 994건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- 네 문항의 blind 답·공식 답 일치 상태를 raw대로 보존했다. 최초 노출 이력, 법 외부 적용 금지, IB 사전 구획 유보도 수정 없이 유지한다.
- `meta_state.py` 실제 결과: 완료 50 passage groups·206 cases, META13 이후 1 group·4 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 Astra frontier는 G052 IC blind다.

## 최신 Luna sync — 2026-09-15 META13 반영

- `META-G048-G050-meta_induction-20260915-13` raw 1건을 원 payload 그대로 독립연구 진행 기록과 processed 원장에 기계적으로 반영했다. queue 978건·processed 978건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- 조건부 행동 동치·전역 동치, 지지 부족·명시 반례, 기호 속성·표현 기능 보강과 payload의 원문 오탈자를 수정 없이 보존했다.
- `meta_state.py` 실제 결과: 완료 49 passage groups·202 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`; 다음 audit까지 2회다.
- 다음 Astra frontier는 G051 HY blind다.

## 최신 Luna sync — 2026-09-15 G050 완료·META13 trigger

- 직전 sync 이후 미처리 raw 9건(HV·HW·HX 각 answer_check·independent_code·sdss_compare)을 queue 원문 그대로 기존 사례 문서와 processed 원장에 기계적으로 반영했다. queue 977건·processed 977건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- G050 전체 3 cases의 answer_check·independent_code·SDSS 대조를 완료했다. source 노출·복원 한계와 기존 qualification은 raw대로 보존했다.
- `meta_state.py` 실제 집계는 49 passage groups·202 cases, META12 이후 3 groups·11 cases, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 Astra 허용 단계는 META13 `meta_induction`이다. 새 G051 연구는 META13 raw 저장 및 Luna sync·pending 0 검증 후 시작한다.

## 최신 Luna sync — 2026-09-15 G049 완료

- 직전 sync 이후 미처리 raw 12건(HR·HS·HT·HU 각 answer_check·independent_code·sdss_compare)을 queue 원문 그대로 기존 사례 문서와 processed 원장에 기계적으로 반영했다. queue 968건·processed 968건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- G049 전체 4 cases의 answer_check·independent_code·SDSS 대조를 완료했다. 최초 사전노출 이력과 HT 수식 미검증 등 기존 한계를 raw대로 보존했다. G050은 blind 전체 완료 상태이며 답·SDSS는 미공개다.
- `meta_state.py` 실제 집계는 48 passage groups·199 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. META12 이후 완료는 2 groups·8 cases다.
- 다음 Astra frontier는 G050 전체 answer_check다. G050 answer_check·independent_code·SDSS barrier를 순서대로 지킨다.

## 최신 Luna sync — 2026-09-15 G048 완료·G049/G050 blind 완료

- 직전 sync 이후 미처리 raw 17건을 queue 원문 그대로 반영했다. G048 HP·HQ blind 및 HN~HQ 전체 answer_check·independent_code·sdss_compare 16건, HW label hold 1건을 기존 사례 문서·processed 원장에 기계적으로 반영했다. queue 956건·processed 956건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- G048(4 cases)은 전체 답·independent_code·SDSS까지 완료했다. G049(HR·HS·HT·HU)와 G050(HV·HW·HX)은 전체 blind가 저장되었으나 답·SDSS는 미공개다. HW 그림·가나 anchor 복원과 label hold qualification을 보존한다.
- `meta_state.py` 실제 집계는 47 passage groups·195 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. G049/G050 blind raw는 완료 집계에 아직 추가되지 않는다.
- 다음 허용 semantic stage는 G049 전체 answer_check다. G049 answer_check·independent_code·SDSS 완료 전 G050 답 공개를 시작하지 않는다.

## 최신 Luna sync — 2026-09-15 G048~G050 시각 복원 대기 중간 상태

- 직전 sync 이후 미처리 raw 11건을 queue 원문 그대로 기존 사례 문서·CURRENT·processed 원장에 기계적으로 반영했다. queue 939건·processed 939건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- G048은 HN·HO blind가 저장되었고 HP·HQ source hold, G049는 HR·HS·HT blind 및 HU hold, G050은 HV·HX blind 및 HW 이미지 hold 상태다. 세 group 모두 답·SDSS는 미공개이며 answer_check·independent_code·SDSS를 시작하지 않는다.
- HP/HQ/HU의 source 복원과 HW blind 이미지 복원 대기 상태를 보존한다. source 완료 후 Astra가 G048부터 누락 blind를 완성하며, 모든 group barrier를 충족하기 전 다음 semantic stage로 진행하지 않는다. 정답·태그를 추정하거나 노출하지 않았다.
- `meta_state.py`의 실제 완료 집계는 46 passage groups·191 cases이며 `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 이번 중간 상태 raw는 완료 집계를 증가시키지 않는다.
- 다음 frontier는 source 복원 완료 후 G048 blind 완성이다. 이는 정기 SDSS 완료 sync가 아닌 시각 복원 대기 checkpoint다.

## 최신 Luna sync — 2026-09-15 HK depth backfill 완료

- `HK-depth_backfill-20260915-audit12-01` raw 1건을 원 payload 그대로 기존 HK 연구 문서와 processed 원장에 기계적으로 반영했다. queue 928건·processed 928건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- 고정 곡률·초기 길이=호 길이의 명시 모형에서 ⑤ 기하 근거를 도출한 내용과, 일반 실제 열팽창 모형 보증이 아님·축방향/구속 가정 유보·원 ③/주 46 불변을 raw대로 보존했다.
- `meta_state.py` 결과: 실제 완료 집계 46 passage groups·191 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- META12 audit 및 지정 backfill이 모두 종료되었으므로 다음 Astra frontier는 G048 HN blind다.

## 최신 Luna sync — 2026-09-15 HI depth backfill

- `HI-depth_backfill-20260915-audit12-01` raw 1건을 원 payload 그대로 기존 HI 연구 문서와 processed 원장에 기계적으로 반영했다. queue 927건·processed 927건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- HI 감사 요구의 증거 등급과 현 텍스트 내 답 판정 영향 명료화를 raw대로 반영했다. semantic backfill 완료와 공식 `[A]` 괄호 source 복원은 구분하며, source hold는 명시적으로 미해소로 유지한다.
- `meta_state.py` 결과: 실제 완료 집계 46 passage groups·191 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["HK"]`이다.
- HK backfill 완료 전에는 새 group을 시작하지 않는다.

## 최신 Luna sync — 2026-09-15 GK depth backfill

- `GK-depth_backfill-20260915-audit12-01` raw 1건을 원 payload 그대로 기존 GK 연구 문서와 processed 원장에 기계적으로 반영했다. queue 926건·processed 926건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- GK의 명시 근거 회수 대안 및 기존 삭제 probe의 증명 범위 제한 보강, 최초 주 코드 74 보존을 raw대로 반영했다. Luna는 의미를 수정하지 않았다.
- `meta_state.py` 결과: 실제 완료 집계는 46 passage groups·191 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["HI", "HK"]`이다.
- HI·HK backfill 완료 전에는 새 group을 시작하지 않는다.

## 최신 Luna sync — 2026-09-15 META12 manual parity audit

- `AUDIT-meta12-manual_parity_audit-20260915-01` raw 1건을 원 payload 그대로 독립연구 진행 기록과 processed 원장에 기계적으로 반영했다. queue 925건·processed 925건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- audit 표집은 8 cases·6 groups이며 전체 완료 수와 구분한다. 실제 전체 집계는 `completed_passage_groups_total=46`, `completed_questions_total=191`이다.
- `meta_state.py` 결과: `meta_induction_count=12`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["GK", "HI", "HK"]`이다. audit가 지정한 세 backfill은 Astra가 각각 저장 직후 sync한다.
- HI 범위 후보 qualification, HK⑤ 기하 범위, HM 필요조건 대안 등 audit raw의 의미는 Luna가 수정하지 않았다. depth backfill 완료 전 새 G048은 시작하지 않는다.

## 최신 Luna sync — 2026-09-15 META12 반영·manual audit due

- `META-G045-G047-meta_induction-20260915-12` raw 1건을 원 payload 그대로 독립연구 진행 기록과 processed 원장에 기계적으로 반영했다. queue 924건·processed 924건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- `meta_state.py` 결과: `meta_induction_count=12`, `meta_due=false`, `manual_parity_audit_due=true`, `depth_backfill_pending=[]`; 완료 집계는 46 passage groups·191 cases다. `manual_parity_audits_remaining_to_next=0`을 보존한다.
- META12 raw의 HI 범위 후보 qualification, HK⑤ 기하 범위, HM 필요조건 대안 등 이월·미해소 항목은 의미를 추가하지 않고 payload와 상태에 그대로 보존했다.
- 다음 Astra 허용 단계는 META12에 대한 `manual_parity_audit`이며, 필요 시 명시된 `depth_backfill`을 저장하고 sync할 때까지 G048을 시작하지 않는다.

## 최신 Luna sync — 2026-09-15 G047 완료·meta12 trigger

- 직전 sync 이후 미처리 raw 17건을 queue 원문 그대로 반영했다. G047 HJ·HK·HL·HM의 16건(blind·answer_check·independent_code·sdss_compare)과 HI 범위 evidence hold 1건을 기존 사례 MD·절차 기록·processed 원장에 기계적으로 반영했다. queue 923건·processed 923건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- G047은 사이트 태그 연결을 포함해 전체 4단계가 완료되었다. HJ·HL 그림의 주 Astra 사후 직접 확인 및 교재 경유 qualification, HI 범위 supplement의 로컬 후보·공식 직접 검증 아님·기존 미확인 상태를 raw대로 보존했다. 의미 재판정은 하지 않았다.
- `meta_state.py` 결과: 실제 완료 집계는 46 passage groups·191 cases, `completed_groups_since_last_meta=3`, `completed_questions_since_last_meta=9`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 번호 최댓값과 완료 수량을 혼동하지 않는다.
- 다음 허용 단계는 3개 group 완료 규칙에 따라 META12 `meta_induction`을 먼저 저장하고 Luna sync·pending 0 검증을 수행하는 것이다. 그 뒤 다음 group을 진행한다.

## 최신 Luna sync — 2026-09-15 G046 완료

- 직전 sync 이후 미처리 raw 8건(HH·HI 각 blind·answer_check·independent_code·sdss_compare)을 queue 원문 그대로 기존 사례 MD와 processed 원장에 기계적으로 반영했다. queue 906건·processed 906건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- G046(HH·HI)은 전체 4단계가 완료되었고, 두 문항의 blind 답과 공식 답 일치 상태를 raw대로 보존했다. `[A]` 정확 괄호 범위 미검증은 미해소로 유지하며 대응 단락 텍스트로 풀이 완료된 사실만 반영했다.
- `meta_state.py` 결과: 완료 46 passage groups·187 cases, `meta_induction_count=11`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다.
- 다음 Astra frontier는 G047 HJ blind다. 신규 source나 semantic 추론은 수행하지 않았다.

## 최신 Luna sync — 2026-09-15 G045 완료·identity exposure 보존

- 직전 sync 이후 미처리 raw 12건(HE·HF·HG 각 blind·answer_check·independent_code·sdss_compare)을 queue 원문 그대로 기존 사례 MD와 processed 원장에 기계적으로 반영했다. queue 897건·processed 897건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- 후속 `BACKLOG-hold-20260915-identity-exposure-01` raw 1건을 identity exposure 보존용 hold로 추가 반영했다. 최종 queue 898건·processed 898건이며 차집합은 0건이다. 원문·정답·태그 미노출, 향후 blind identity 구분 방침과 2011 수능 37~39번 제외 이력은 그대로 보존한다.
- G045(HE·HF·HG)는 전체 blind·answer_check·independent_code·SDSS 대조까지 완료했다. 2011 수능 언어 정답 전체 및 37~39번 노출 제외 이력은 기존 상태 그대로 보존한다.
- `source_gz`가 준비 후보 HN~IR의 시험 연도·회차·문항번호를 보고한 identity exposure 기록과, 원문·정답·태그 미노출 및 향후 구분 방침을 보존했다. 이를 새 사례의 blind 오염으로 과장하지 않았다.
- `meta_state.py` 결과: 완료 44 passage groups·185 cases, `meta_induction_count=11`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`. 현재 manifest는 226건(소비 완료 185, prepared 41)이다.
- 다음 Astra frontier는 G046 HH blind다. G045 완료 후 meta11 상태는 due가 아니므로 새 group을 진행할 수 있다.

## 최신 Luna sync — 2026-09-15 META11 반영

- `META-G042-G044-meta_induction-20260915-11` raw 1건을 원 payload 그대로 독립연구 진행 기록과 processed 원장에 기계적으로 반영했다. queue 885건·processed 885건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- `meta_state.py` 결과: `meta_induction_count=11`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`; 완료 집계는 43 passage groups·182 cases다. `manual_parity_audits_remaining_to_next=1`을 보존한다.
- META11 payload의 `next_falsification_targets`·`unresolved_boundaries` 및 GZ 원답/범위 qualification은 의미를 재작성하지 않고 raw 기록과 상태에 보존했다. 기존 최초 코드·GZ 홀수형 ⑤ 및 짝수형 ① 이력은 변경하지 않았다.
- 다음 Astra frontier는 G045 blind다. 새 group 시작 전 META11 sync와 pending 0 검증이 완료된 상태다.

## 최신 Luna sync — 2026-09-15 G043 완료·meta10 trigger

- 직전 sync 이후 미처리 raw 12건을 queue 원문 그대로 기존 사례 MD·CURRENT·processed 원장에 기계적으로 반영했다. queue 884건·processed 884건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- G043(GW·GX·GY·GZ·HA)은 전체 independent_code와 SDSS 대조까지 완료했다. GZ의 짝수형 답 ① 직접 대조 결과는 공식 형식 제3자 첨부 경유라는 qualification과 함께 보존하며, 기존 홀수형 답 ⑤ 및 mismatch는 변경하지 않았다. `[A]` 사후 완전 범위 확인은 GZ SDSS raw에 보존했다. G044(HB·HC·HD)도 완료 상태다.
- GZ form-verification hold 및 answer_check 보완 raw를 `needs_astra_review`/완료 상태 그대로 반영했으며, Luna는 답·정본·코드 의미를 재판정하지 않았다.
- `meta_state.py` 실행 결과 완료 집계는 passage group 43개·case 182개, `meta_induction_count=10`, `meta_due=true`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. prepared backlog는 13건이다.
- 3개 group(G042~G044)·11개 case 완료로 meta10 due가 발생했다. 다음 Astra는 새 G045 blind보다 `meta_induction`을 먼저 수행해야 한다. meta raw 저장 및 다음 Luna sync 후에 G045 blind를 시작한다.

## 최신 Luna sync — 2026-09-15 G044 완료·사후 감사 raw 반영

- 직전 sync 이후 미처리 raw 6건(HB·HC·HD 각 `independent_code` 및 `sdss_compare`)을 queue 원문 그대로 기존 사례 MD와 processed 원장에 기계적으로 반영했다. queue 872건·processed 872건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- G044(HB·HC·HD)는 group 전체 independent_code와 SDSS 대조까지 완료했다. G043은 GZ의 공식 답 번호·정본·시험형 대응 확인이 진행 중이며, 최초 blind ①과 sealed 공식 답 ⑤ 불일치 및 `needs_astra_review`를 유지한다. GZ 불일치가 해소되기 전 G043 전체 independent_code·SDSS를 시작하지 않는다.
- 직전 원장의 후속 사후 감사 raw 8건(DV-GA·DZ-EO-EP-EJ·AB-BZ-CT-GC·FH-FN-FT-GJ-ET·FF-FL·FX-EF·FD-EI·ANCHORS-O1-O8)은 모두 queue에 보존되어 있으며, 이번 sync 시점에 이미 처리된 상태를 유지한다. Luna는 depth backfill·boundary revision의 의미를 추가하거나 수정하지 않았다.
- `meta_state.py` 실행 결과 `meta_induction_count=10`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. 완료 집계는 passage group 42개·case 177개다. prepared backlog는 21건이며 다음 대기 범위는 G045~G047이다.
- 다음 Astra frontier는 G043 GZ 정본·시험형 대응 확인이다. 이후 G043 전체 independent_code→group barrier→SDSS 순서를 지키고, G044는 완료 상태로 재풀이하지 않는다.

## 최신 Luna sync — 2026-09-15 사용자 중지 후처리

- 직전 sync 이후 미처리 32건을 queue 원문 그대로 기존 사례 MD/절차 기록 및 processed 원장에 기계적으로 반영했다. queue 858건·processed 858건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- G042(GT·GU·GV)는 blind·answer_check·independent_code·SDSS 대조까지 완료했다. G043(GW·GX·GY·GZ·HA)은 blind 전체와 GW·GX·GY·HA answer_check를 반영했으며 GZ는 `needs_astra_review`로 보존한다. G044(HB·HC·HD)은 blind·answer_check 전체를 반영했다. G043/G044 independent_code 및 SDSS 대조는 미착수다.
- GZ의 최초 blind 답 ①과 sealed 공식 답 ⑤ 불일치는 시험형 차이 또는 정본 연결 문제로 미확정이다. 복원 선택지 ①(지구/회귀년/항성년)과 최초 의미 판단 및 mismatch raw를 보존하며 정답 일치로 집계하지 않는다. Luna는 번호를 추론해 수정하지 않았다.
- 마지막 raw는 사용자 중지 hold다. 신규 source/sealed/해설/SDSS/코드 판정·귀납·backlog 준비를 수행하지 않았다. meta 상태는 count 10, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`로 유지한다.
- 재개 지점은 G043 GZ 공식 답 번호와 정본·시험형 대응 확인이다. 그 확인 전 G043 전체 independent_code와 SDSS를 시작하지 않는다. 이후 G044 전체 independent_code→장벽 확인→SDSS 순서를 지키며 G045/G046 자료는 미열람 상태로 둔다.

## 최신 Luna sync — G039~G041 및 meta10 반영

- queue 원문을 수정하지 않고 cutoff `SYNC-hold-20260915-three-groups-01`까지 미처리 raw 40건을 기존 문서와 processed 원장에 기계적으로 반영했다. 현재 queue 826건·processed 826건이며 record_id 차집합은 0건이다.
- G039·G040·G041 완료와 meta10 raw를 보존한다. `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`이다. hold raw는 `needs_astra_review`로 보존했다.
- 다음 Astra frontier는 G042의 `GT` blind이다. 이번 sync에서는 source·answer·SDSS를 열지 않았고 의미 재판정을 하지 않았다.

업데이트: 2026-09-14 (Luna quota handoff 후처리 완료)

## 최신 Luna 상태 — G039 답 대조 대기

- 신규 hold raw 1건을 원 payload 그대로 CURRENT와 processed 원장에 반영했다. queue 786건·processed 786건이며 `record_id`/`source_record_id` 차집합은 0건이다. queue 원문은 변경하지 않았다.
- quota 실측은 primary remaining 96%, weekly remaining 6%다. 현재 frontier는 G039(GK·GL·GM)이며 세 문항 blind가 모두 저장되어 있고 answer_check·independent_code·SDSS compare는 미착수다. 다음 Astra 단계는 GK answer_check이며, group 전체 answer_check→전체 independent_code→장벽 확인 후 SDSS 공개 순서를 유지한다.
- 공식 답·SDSS 태그는 미공개다. GL 그림 판독으로 기존 그림 누락 hold는 해소된 기록을 유지하되, 원 표기 수식 검증 한계와 기존 qualification은 보존하며 이번 후처리에서 재판정하지 않았다.
- 신규 source·sealed 자료 열람, backlog 준비, semantic 연구는 수행하지 않았다. 최신 meta 상태는 `meta_induction_count=9`, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`로 보존한다.

## 과거 상태 기록 — G032 완료, G033 독립 코드 진행 중

- G031 및 G032 전체 단계와 G032 induction을 반영했다. G032(EZ·FA·FB·FC)는 blind, answer_check, independent_code, SDSS 대조 및 induction까지 완료다. 보조원의 EBSI 해설 우발 노출은 Astra 답·해설 미노출과 구분해 원문 hold에 보존했고, G032를 절차 전체 무오염 strict 성과로 확정하지 않는다.
- G033(FD·FE·FF·FG·FH)은 blind와 answer_check까지 전체 완료. independent_code는 FD·FE만 완료했고 FF·FG·FH는 미완료이며, group SDSS는 미공개다. 다음 Astra 단계는 FF independent_code다. 세 문항 independent_code가 모두 저장되기 전 G033 SDSS 공개 금지.
- FH 선택지 뒤 `##2026학년도` 추출 경계 잔재는 blind raw 품질 사항으로 보존했다. G032 지수·분수 복원은 로컬 canonical 연결 기출 수록 HWPX 기반이며 KICE 원 배포 PDF 직접 대조 완료로 기록하지 않는다.
- G024(DR·DS·DT·DU) 4개 prior-exposure hold는 유지한다. 기존 hold를 backlog 소비 가능 수에 포함하지 않는다.

## 처리 원장과 범위

- 이번 quota handoff 차집합 32건을 기존 case별 Markdown 및 절차 기록에 원문 payload 그대로 반영하고 processed 원장에 추가했다. queue 원장은 변경하지 않았으며 queue 648건, processed 648건, record_id 차집합 0건이다.
- G033 hold 당시 기계 기록은 prepared manifest 155건·완료 129문항이다. 이를 기준으로 남은 26문항 중 G033 5문항은 진행 중, 순차 소비 대기분은 21문항으로 기록한다. 별도 G024 hold 4건은 이 수에 포함하지 않는다. manifest·backlog·source는 이번 후처리에서 수정하거나 새로 열지 않았다.
- 다음 Excel-style case ID는 `FF`다. G033 SDSS 이후 meta 상태를 sync해 3 groups/14 questions 도달 시 meta7 trigger를 확인한다. 마지막 sync의 meta6 상태는 `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`다.
- primary remaining 7%, weekly remaining 39% threshold handoff를 반영했다. quota가 새 연구 중지를 지시하므로 이번 Luna 처리는 저장된 raw와 상태 복구에 한정한다.

## 기존 유보 사항

- G024(DR·DS·DT·DU)의 사전노출 hold와 independent_code/SDSS 미실행 상태를 유지한다.
- DP `[A]` 정확 범위, G022 표상 층위, 기존 미확인 사이트 적용 위치는 이 반영으로 해소되지 않았다.

<!-- luna-checkpoint:2026-09-10-G015-blind-complete -->
## Luna recovery checkpoint — 2026-09-10

- queue/processed 비교 후 미처리 raw 6건을 모두 반영했다. 현재 queue 283건과 processed 283건이 record_id 기준으로 정합하며 미처리 raw는 0건이다.
- G015 CC·CD·CE·CF의 blind raw가 모두 저장되었다. 공식답·independent_code·SDSS는 아직 공개하지 않았으며, 다음 허용 semantic stage는 G015 전체 `answer_check`이다. CE·CF 최초 기록과 기존 노출 표시는 보존한다.
- meta_induction payload는 필수 필드를 갖춘 채 연구 진행 기록에 기계적으로 반영했다. `meta_state.py` 동기화 결과 `meta_due=false`, `manual_parity_audit_due=false`, 완료 group 14개·case 54개를 보존한다. Luna는 meta 의미를 추가하지 않았다.
- prepared backlog manifest는 86건, 소비 완료 54건, 잔량 32건이다. 잔량이 최소 기준 30건 이상이므로 후보 추가를 수행하지 않았다. 다음 준비 Excel-style case ID는 `CC`이며, 이는 현재 G015 semantic barrier가 해제된 뒤 소비할 첫 미소비 case다.
- blind packet/source와 sealed answer/SDSS/provenance 분리는 유지된다. verifier 결과: content leakage 0, identity leakage 0, question duplicate 0, existing overlap 0, errors 0.
- hold·unavailable·quota threshold 및 기존 unresolved 항목은 `needs_astra_review` 또는 기존 보류 상태로 보존했으며, Luna는 의미적 재판정을 하지 않았다.


<!-- luna-raw:G015-hold-20260910-user-stop-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "사용자가 현재 atomic semantic stage 저장 후 새 case/group/stage 없이 종료하라고 지시함.",
  "last_completed_atomic_record": "CD-blind-20260910-01",
  "group_case_ids": [
    "CC",
    "CD",
    "CE",
    "CF"
  ],
  "blind_done": [
    "CC",
    "CD"
  ],
  "blind_pending": [
    "CE",
    "CF"
  ],
  "official_answers_disclosed": false,
  "sdss_disclosed": false,
  "barrier": "all_group_blind_records_before_any_group_answer_check 미충족. G015 정답 대조·독립 코드·SDSS 공개를 시작하지 않음.",
  "next_semantic_stage_if_resumed": "기존 미처리 raw 후처리 및 상태 복구 후 CE blind. CF blind까지 저장한 다음에만 group 전체 answer_check 허용.",
  "exposure_note": "CC/CD raw의 같은 지문 사전노출 표시는 보존. 엄격 blind 성과에 포함하지 않음.",
  "new_research_after_stop_request": false,
  "quota_note": "사용자 중단이며 quota threshold/hard limit 중단으로 기록하지 않음."
}
```

<!-- luna-raw:QUOTA-hold-20260910-post-meta-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "quota_status": "unavailable",
  "checkpoint": "첫 meta_induction 저장·sync 직후",
  "last_successful_observation": {
    "primary_remaining_percent": 13,
    "weekly_remaining_percent": 47,
    "qualification": "과거 조회값. 현재값 추정하지 않음"
  },
  "action": "unavailable 자체는 handoff 아님. runtime 경고 우선, polling 지속"
}
```


<!-- luna-raw:QUOTA-hold-20260910-post-CE-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "quota_status": "unavailable",
  "checkpoint": "CE blind 직후",
  "action": "추정 없음; runtime 경고 우선; unavailable 자체로 중단하지 않음"
}
```


<!-- luna-raw:G015-hold-20260910-quota-threshold-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "quota helper 최초 threshold 관측",
  "quota": {
    "primary_used_percent": 98,
    "primary_remaining_percent": 2,
    "weekly_used_percent": 55,
    "weekly_remaining_percent": 45
  },
  "previous_poll": "CF blind 직후 sandbox 조회 unavailable. 같은 helper를 승인된 sandbox 밖에서 재조회하여 실제 값 확보. 추정값 사용 없음.",
  "last_completed_atomic_record": "CF-blind-20260910-01",
  "new_records_since_processed": 6,
  "blind_done": [
    "CC",
    "CD",
    "CE",
    "CF"
  ],
  "answer_check_done": [],
  "independent_code_done": [],
  "sdss_compare_done": [],
  "official_answers_disclosed": false,
  "sdss_disclosed": false,
  "meta": "META-G001-G014-meta_induction-20260910-01 저장 후 sync 완료; meta_due=false; manual_parity_audit_due=false",
  "next_semantic_stage": "다음 Astra 세션에서 G015 전체 answer_check부터. CC/CD 재풀이 금지, CE/CF 최초 기록 보존. 그 뒤 전체 independent_code 저장 후에만 SDSS 공개.",
  "action": "추가 semantic work 없이 즉시 Luna spawn. 신규 raw 후처리 완료까지 대기 후 종료."
}
```


<!-- luna-raw:CH-hold-20260910-source-missing-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G016",
  "reason": "blind-only source의 5개 선택지가 모두 빈 문자열이다. 선택 번호를 결정할 수 없어 blind 완료를 선언하지 않는다.",
  "completed_partial_reasoning_without_codes": "일자리 감소 산업 비중이 시행집단에 더 크므로 프로그램이 없을 때 시행집단의 고용률 증가는 비교집단보다 작다. 더 큰 비교집단 증가를 빼면 효과 추정은 더 작아진다. A=작을, B=작을.",
  "selected_answer": null,
  "confidence_in_partial_relation": "높음",
  "next_work": "공식 원문에서 선택지 표만 blind-only supplement로 복원하고 번호 매핑을 직접 확인한다.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "same_passage_prior_exposure": true
  },
  "barrier": "CH의 유효 blind가 완료되기 전 G016 전체 공식답 대조 금지"
}
```


<!-- luna-raw:CK-hold-20260911-source-missing-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G017",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/CK.json",
  "reason": "choices가 빈 배열이고 stem 끝에는 ① Ⓐ만 남아 있어 Ⓒ의 실제 선택지 번호 확인이 필요하다.",
  "completed_partial_reasoning_without_codes": "부적절한 항목은 Ⓒ이다. (가)는 동일성·비동일성을 정의하나 개념의 변화 과정은 제시하지 않는다. (나)도 미메시스를 정의하므로 개념 정의 자체도 (가)만의 차이가 아니다.",
  "selected_answer": null,
  "selected_activity_label": "Ⓒ",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "same_passage_prior_exposure": "이번 세션에서 처음 읽음. 과거 학습 노출 여부 확인 불가"
  },
  "next_work": "기계적 원문 복원으로 Ⓐ~Ⓔ의 선택지 번호 표를 blind supplement에 보존한 뒤 유효 blind를 저장한다.",
  "barrier": "G017 전체 blind 완료 전 답·태그 공개 금지"
}
```


<!-- luna-raw:CT-hold-20260911-source-check-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G018",
  "reason": "공통 지문의 자녀 한 명 보장 비율 수식이 누락되어 수치 판정 불가. 또한 현재 ⑤는 사망 당시 남은 B 재산에서 취득하는 이익이 동일하다는 표현이므로 주어진 B=100과 일치해 보인다. 선택지 전체 원문 충실성 확인이 필요하다.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "상승 원인이 노력인지에 따라 부족액 계산에 쓰는 A 가치는 300 또는 700이다. 이미 받은 B=100은 같고, 반환 지분 계산의 A 가치는 두 경우 모두 사망 당시 700이다. 현 source의 ⑤는 가상 총이익이 아닌 남은 재산에서 취득할 이익으로 적혀 있다.",
  "next_work": "누락 분수와 CT 모든 선택지를 공식 원문에서 blind-only supplement로 복원한 뒤 직접 재판독. 정답을 먼저 보아 문구를 맞추지 않는다.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false
  },
  "barrier": "CT 유효 blind 전 G018 공식답 대조 금지"
}
```


<!-- luna-raw:CW-hold-20260911-diagram-missing-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G019",
  "reason": "보기에는 노드 a~e 이름만 추출되어 화살표의 방향·연결이 없다. 순환/분배를 계산할 그래프를 임의 추측하지 않는다.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "각 링크의 전달값은 송신 노드 값×0.5/송신 노드의 나가는 링크 수이고 각 수신 노드 값은 들어온 값의 합이다. d=e=16은 고정. 실제 연결 복원 전 수치 확정 불가.",
  "next_work": "원본 도식의 blind-only 이미지 supplement를 직접 읽어 간선 방향과 개수를 기록한 뒤 풀이한다.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false
  },
  "barrier": "CW 유효 blind 전 G019 전체 공식답 대조 금지"
}
```


<!-- luna-raw:CW-hold-20260911-vector-fidelity-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G019",
  "reason": "첫 SVG supplement의 viewBox 폭은22714이나 c 중심22778·선 끝28695가 밖에 있고 선분들이 노드 바깥에서 끝나 원본 그룹 변환·연결 형태 충실성이 미확정이다. 이를 유효 원문 그림으로 채택하지 않는다.",
  "rejected_as_verified_source": "data/기본기_연구/prepared_backlog/blind_sources/CW_graph_supplement.svg",
  "next_work": "원본 HWPX의 실제 렌더 또는 공식 PDF 그림으로 시각 확인 후 blind 풀이. 단순 좌표 재배열이나 선택지 역추정으로 연결을 만들지 않는다.",
  "selected_answer": null,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "unverified_vector_geometry_seen": true,
    "valid_original_graph_seen": false
  },
  "barrier": "G019 답·태그 계속 미공개. CU·CV·CX 최초 기록 유지"
}
```


<!-- luna-raw:G019-hold-20260911-quota-threshold-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "quota helper에서 primary remaining 7% 최초 관측. 정상 Luna handoff.",
  "quota": {
    "primary_used_percent": 93,
    "primary_remaining_percent": 7,
    "weekly_used_percent": 72,
    "weekly_remaining_percent": 28
  },
  "last_completed_atomic_record": "CW-hold-20260911-vector-fidelity-02",
  "completed_groups_this_session": [
    "G016",
    "G017",
    "G018"
  ],
  "meta_record": "META-G015-G017-meta_induction-20260911-01",
  "meta_state_last_sync": {
    "meta_due": false,
    "manual_parity_audit_due": false,
    "completed_groups": 18,
    "completed_cases": 72
  },
  "current_group": "G019",
  "blind_done": [
    "CU",
    "CV",
    "CX"
  ],
  "blind_pending": [
    "CW"
  ],
  "answer_check_done": [],
  "independent_code_done": [],
  "sdss_compare_done": [],
  "exposure": {
    "G019_official_answers_seen": false,
    "G019_sdss_seen": false,
    "CW_unverified_svg_seen": true,
    "CW_valid_original_graph_seen": false
  },
  "next_work": "CW 원본 그림의 시각 충실성 검증 및 blind 풀이. CU·CV·CX 재풀이 금지. 그 후에만 G019 전체 answer_check→전체 independent_code→SDSS 공개.",
  "source_recovery_agent": "/root/restore_ch_source에서 HWPX 변환행렬 적용/렌더 기계 작업 진행 중. Luna는 결과 경로·provisional 상태만 받아 보존하고 간선 판단이나 풀이를 생성하지 말 것.",
  "action": "새 semantic stage·source read·SDSS·meta 없이 즉시 fresh Luna medium spawn, raw 후처리 완료 대기 후 Astra 종료.",
  "source_quality_carryover": [
    "CH 선택지 표 복원",
    "CK 번호 표 복원",
    "CT 원본 XML 분수 복원. 첫 파생 텍스트 supplement complete 주장은 수식 완전성 아님",
    "CW 첫 SVG는 provisional이며 유효 원문으로 채택하지 않음"
  ]
}
```


<!-- luna-raw:G021-hold-20260912-quota-threshold-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "primary remaining7% 최초 관측에 따른 정상 handoff. caution10%에서 DH atomic independent_code 하나 저장 후 재조회하여 threshold 확인.",
  "quota": {
    "primary_used_percent": 93,
    "primary_remaining_percent": 7,
    "weekly_used_percent": 88,
    "weekly_remaining_percent": 12
  },
  "last_completed_atomic_record": "DH-independent_code-20260912-01",
  "completed_groups_this_session": [
    "G020",
    "G019"
  ],
  "total_completed_groups": 20,
  "total_completed_cases": 82,
  "current_group": "G021",
  "group_cases": [
    "DE",
    "DF",
    "DG",
    "DH"
  ],
  "blind_done": [
    "DE",
    "DF",
    "DG",
    "DH"
  ],
  "answer_check_done": [
    "DE",
    "DF",
    "DG",
    "DH"
  ],
  "independent_code_done": [
    "DE",
    "DF",
    "DG",
    "DH"
  ],
  "sdss_compare_done": [],
  "exposure": {
    "G021_official_answers_seen": true,
    "G021_sdss_seen": false,
    "G019_CW_original_application_render_seen": true,
    "G019_CW_strict_new_blind_excluded": true
  },
  "meta_state_last_sync": {
    "meta_due": false,
    "manual_parity_audit_due": false,
    "depth_backfill_pending": [],
    "meta_induction_count": 3,
    "last_manual_parity_audited_meta_count": 3
  },
  "new_semantic_assets": [
    "META-G018-G020-meta_induction-20260912-01",
    "AUDIT-meta3-manual_parity_audit-20260912-01",
    "CY-depth_backfill-20260912-01",
    "G020-induction-20260912-01"
  ],
  "next_work": "G021 전체 independent_code 저장 장벽을 확인한 뒤 SDSS 공개·대조부터 재개. 필요 시 G021 induction 및 CT/DG 조건별 규칙 범위 비교. 신규 G022 전 meta_state sync 필수. 이미 저장된 blind/answer/independent 재풀이 금지.",
  "source_quality": [
    "CW 공식 HWP application render crop을 직접 판독하여 hold 해소. 외부 화살표 자체는 원본에 존재; 기존 SVG 방향·연결·화살촉 불충실성과 구별.",
    "CZ [A] 시각 범위 미확정 보존.",
    "G018~G020 meta에 기존 unresolved 및 사이트 적용 범위 미확인 보존."
  ],
  "luna_action": "신규 queue raw를 의미 변경 없이 기존 MD/JSONL·processed에 반영하고 CURRENT 상단을 최신화. G021 미공개 SDSS를 Luna가 추론·대조하지 않음. 필요 backlog 준비는 blind/sealed 분리된 기계 작업만.",
  "action": "safe raw/checkpoint 저장 직후 fresh gpt-5.6-luna medium, fork none 실제 spawn. 후처리 완료 대기 후 Astra 종료."
}
```


<!-- luna-raw:EF-hold-20260913-source-missing-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G027",
  "reason": "blind source에 평가 대상 학생의 독서 목적·지문·실제 밑줄 표시가 없고 선택지 표시 기호도 빈 따옴표로 누락됨. 본문 규칙만으로 선택지 평가 불가.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "독서 목적을 기준으로 주요 정보와 표시 체계의 적합성을 판단해야 한다. 실제 적용 지문과 표시가 없어 번호 선택을 보류한다.",
  "next_work": "공식 원문의 EF 학생 적용 자료와 선택지 표시 기호를 기계적으로 blind-only supplement로 복원한 뒤 주 Astra가 직접 판독.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "existing_judgment_seen": false
  },
  "barrier": "ED·EE blind 원본 유지. EF 유효 blind raw 저장 전 G027 전체 answer_check 금지."
}
```


<!-- luna-raw:QUOTA-hold-20260913-unavailable-observations-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "quota_status": "unavailable",
  "observations": [
    "G025 SDSS compare·sync 직후 sandbox helper unavailable",
    "G026 answer_check 직후 sandbox helper unavailable"
  ],
  "subsequent_actual_observations": [
    {
      "checkpoint": "G025 induction 직후 승인된 외부 helper",
      "primary_remaining_percent": 80,
      "weekly_remaining_percent": 81
    },
    {
      "checkpoint": "G026 EA independent 전 승인된 외부 helper",
      "primary_remaining_percent": 71,
      "weekly_remaining_percent": 80
    },
    {
      "checkpoint": "G026 induction 직후 승인된 외부 helper",
      "primary_remaining_percent": 63,
      "weekly_remaining_percent": 78
    }
  ],
  "action": "unavailable은 해당 조회 상태로 보존하고 잔량 추정하지 않음. 이후 실제 성공 조회만 별도 사용. unavailable 자체는 handoff 아님.",
  "runtime_warning_observed": false
}
```


<!-- luna-raw:G028-hold-20260913-quota-threshold-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "primary remaining7% 최초 관측에 따른 정상 Luna handoff. caution9%에서 EG atomic answer_check 하나 저장 후 재조회하여 threshold 확인.",
  "quota": {
    "primary_used_percent": 93,
    "primary_remaining_percent": 7,
    "weekly_used_percent": 30,
    "weekly_remaining_percent": 70
  },
  "runtime_emergency_warning_observed": false,
  "last_completed_atomic_record": "EG-answer_check-20260913-01",
  "completed_groups_this_session": [
    "G025",
    "G026",
    "G027"
  ],
  "total_completed_groups": 26,
  "total_completed_cases": 106,
  "current_group": "G028",
  "group_cases": [
    "EG",
    "EH",
    "EI",
    "EJ",
    "EK",
    "EL"
  ],
  "blind_done": [
    "EG",
    "EH",
    "EI",
    "EJ",
    "EK",
    "EL"
  ],
  "answer_check_done": [
    "EG"
  ],
  "answer_check_pending": [
    "EH",
    "EI",
    "EJ",
    "EK",
    "EL"
  ],
  "independent_code_done": [],
  "sdss_compare_done": [],
  "exposure": {
    "G028_official_answers_seen": [
      "EG"
    ],
    "G028_sdss_seen": false,
    "EF_official_original_render_seen": true,
    "G024_prior_exposure_hold": "유지; 새 판단 없음"
  },
  "meta_state_last_sync": {
    "meta_due": false,
    "manual_parity_audit_due": false,
    "depth_backfill_pending": [],
    "meta_induction_count": 5
  },
  "meta_record": "META-G025-G027-meta_induction-20260913-01",
  "boundary_record": "G025-G026-boundary_revision-20260913-01",
  "next_work": "다음 Astra는 G028 EH answer_check부터. EG 재대조와 G028 재blind 금지. EH~EL 공식답 대조 전체 저장 뒤 전체 independent_code; 그 전체 저장 전에는 G028 SDSS 공개 금지.",
  "source_quality": "EF 누락 hold는 원본 HWPX application render crop 직접 판독으로 해결. blind_sources/EF_original_question_crop.png와 supplement 및 sealed provenance 보존. 기존 DP·G022 등 유보는 meta에 유지.",
  "luna_action": "queue 최초475건 이후 신규 raw를 의미 변경 없이 기존 MD/JSONL·processed에 반영하고 CURRENT·handoff·checkpoint 최신화. 최초 raw 수정 금지. 미완료 G028 answer_check/independent/SDSS를 추론하지 말 것. 이번에는 backlog 추가나 새 의미 판단 없이 후처리 범위를 완료한다.",
  "action": "raw/checkpoint 저장 직후 fresh gpt-5.6-luna medium fork none 실제 spawn. 후처리 완료 대기 후 Astra 종료."
}
```


<!-- luna-raw:QUOTA-hold-20260913-G029-before-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "quota_status": "unavailable",
  "checkpoint": "G028 induction 저장 및 새 G029 전 sync 후 sandbox helper",
  "subsequent_actual_observation": {
    "primary_remaining_percent": 75,
    "weekly_remaining_percent": 65,
    "method": "승인된 sandbox 밖 helper"
  },
  "action": "unavailable 자체는 중단 조건 아님. 추정 없이 실제 성공 관측을 별도 보존. runtime warning 미관측."
}
```


<!-- luna-raw:QUOTA-hold-20260913-G029-blind-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "quota_status": "unavailable",
  "checkpoint": "G029 전체 blind 직후 sandbox helper",
  "subsequent_actual_observation": {
    "primary_remaining_percent": 66,
    "weekly_remaining_percent": 63,
    "method": "승인된 외부 helper"
  },
  "action": "실패 조회와 실제 성공 조회를 분리 보존. runtime emergency 미관측."
}
```


<!-- luna-raw:ES-hold-20260913-source-missing-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G030",
  "reason": "보기는 다음과 같은 댓글이 달렸다고 하나 실제 댓글·발화자·지목 대상이 blind source에서 누락되어 있다. A/B/C의 가해 책임 비교를 결정할 수 없다.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "㉮·㉯는 실명 또는 주변 정보로 제3자가 사용자를 특정할 수 있는지,㉰는 ID만으로 공격 대상이 표시되었는지를 기준으로 삼는다. 댓글의 실제 대상과 발화자 자료가 없으므로 개별 A/B/C의 책임은 유보한다.",
  "next_work": "공식 원문 댓글 부분만 blind-only supplement로 기계 복원한 뒤 주 Astra가 직접 판독.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "existing_judgment_seen": false
  },
  "barrier": "EQ·ER 최초풀이 보존. ES 유효 blind 저장 및 ET blind 완료 전 G030 전체 answer_check 금지."
}
```


<!-- luna-raw:G030-hold-20260913-quota-threshold-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "primary remaining4% 최초 threshold 관측. caution8%에서 atomic meta_induction 하나 저장·sync 후 다음 stage 전 재조회로 확인. 정상 Luna handoff.",
  "quota": {
    "primary_used_percent": 96,
    "primary_remaining_percent": 4,
    "weekly_used_percent": 46,
    "weekly_remaining_percent": 54
  },
  "runtime_emergency_warning_observed": false,
  "last_completed_atomic_record": "META-G028-G030-meta_induction-20260913-02",
  "completed_groups_this_session": [
    "G028",
    "G029",
    "G030"
  ],
  "total_completed_groups": 29,
  "total_completed_cases": 120,
  "current_group": "G030",
  "group_cases": [
    "EQ",
    "ER",
    "ES",
    "ET"
  ],
  "blind_done": [
    "EQ",
    "ER",
    "ES",
    "ET"
  ],
  "answer_check_done": [
    "EQ",
    "ER",
    "ES",
    "ET"
  ],
  "independent_code_done": [
    "EQ",
    "ER",
    "ES",
    "ET"
  ],
  "sdss_compare_done": [
    "EQ",
    "ER",
    "ES",
    "ET"
  ],
  "meta_state_last_sync": {
    "meta_due": false,
    "meta_induction_count": 6,
    "manual_parity_audit_due": true,
    "depth_backfill_pending": []
  },
  "next_work": "다음 Astra는 manual_parity_audit(meta6)→명시 depth_backfill→각 raw 직후 sync부터 시작. 새 group보다 audit 우선. 이미 처리된 case/stage 재연구 금지. prepared backlog 실제 잔량은 Luna가 기계 확인하고 G024 사전노출 hold를 신규 연구 대상으로 소비하지 말 것.",
  "source_quality": [
    "ES 댓글 원본 HWPX BinData 이미지 복원·주 Astra 직접 판독으로 source hold 해소. 원본 BMP/PNG/provenance 유지.",
    "기존 DP·CZ[A]·G022 및 기타 meta carryover 유보는 유지."
  ],
  "new_boundary": "EO 최초#45 주/#17 보조는 원장 보존, DZ 공식 원문과 반례 대조 후 유일 주 우선순위 유보를 별도 boundary_revision 및 meta에 기록.",
  "exposure": {
    "G030_official_answers_seen": true,
    "G030_sdss_seen": true,
    "ES_original_comment_image_seen": true,
    "G024_prior_exposure_hold": "유지"
  },
  "luna_action": "직전 bounded Luna가 DZ-EO-EP-boundary_revision-20260913-02까지 42건 반영했으므로 processed source_record_id 차집합만 후처리. queue 원본 불변, payload 의미 보존. 미완료 audit/backfill 및 사이트 세부 범위를 추론하지 않음. CURRENT·checkpoint·handoff 상단 최신화. 이번 종료 후처리에서 backlog 추가나 새 의미 연구 불필요.",
  "action": "safe raw/checkpoint 직후 fresh gpt-5.6-luna medium fork none 실제 spawn. 후처리 완료 대기 후 Astra 종료."
}
```


<!-- luna-raw:FI-hold-20260914-source-missing-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G034",
  "reason": "blind source 선택지가 ㉮ 열만 있고 ㉯ 열이 모두 누락되어 ①/② 등의 번호를 결정할 수 없음",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "설의 중국어 방은 같은 입력·출력 역할에도 중국어 앎이 같지 않음을 보인다. 따라서㉮는 의식과 함수적 역할. (나)의 결론에서 지각은 물질 반응도 의식 판단도 아닌 내 몸의 체험이므로㉯는 몸의 체험.",
  "confidence_in_partial_relation": "높음",
  "next_work": "FI 공식 원문 선택지 표의㉯ 열을 blind-only supplement로 기계 복원한 뒤 주 Astra가 번호 직접 확인",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "prior_training_exposure": "확인 불가"
  },
  "barrier": "G034 FI~FN 전체 유효 blind raw 저장 전 공식답 공개 금지"
}
```


<!-- luna-raw:G036-hold-20260914-quota-threshold-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "primary remaining5% 최초 threshold 관측. caution8%에서 FV atomic answer_check 하나 저장 후 재조회해 정상 Luna handoff.",
  "quota": {
    "primary_used_percent": 95,
    "primary_remaining_percent": 5,
    "weekly_used_percent": 77,
    "weekly_remaining_percent": 23
  },
  "runtime_emergency_warning_observed": false,
  "last_completed_atomic_record": "FV-answer_check-20260914-01",
  "processed_at_session_start": 648,
  "completed_groups_this_session": [
    "G033",
    "G034",
    "G035"
  ],
  "total_completed_groups": 34,
  "total_completed_cases": 146,
  "current_group": "G036",
  "group_cases": [
    "FU",
    "FV",
    "FW",
    "FX",
    "FY"
  ],
  "blind_done": [
    "FU",
    "FV",
    "FW",
    "FX",
    "FY"
  ],
  "answer_check_done": [
    "FU",
    "FV"
  ],
  "answer_check_pending": [
    "FW",
    "FX",
    "FY"
  ],
  "independent_code_done": [],
  "sdss_compare_done": [],
  "exposure": {
    "G036_official_answers_seen": [
      "FU",
      "FV"
    ],
    "G036_official_answers_unseen": [
      "FW",
      "FX",
      "FY"
    ],
    "G036_sdss_seen": false,
    "G024_prior_exposure_hold": "유지; 새 연구 없음"
  },
  "meta_state_last_sync": {
    "meta_due": false,
    "manual_parity_audit_due": false,
    "depth_backfill_pending": [],
    "meta_induction_count": 8,
    "baseline_completed_groups": 34,
    "baseline_completed_questions": 146
  },
  "new_semantic_assets": [
    "META-G031-G033-meta_induction-20260914-01",
    "G033-G034-boundary_revision-20260914-01",
    "G034-induction-20260914-01",
    "META-G034-G035-meta_induction-20260914-01"
  ],
  "next_work": "다음 Astra는 G036 FW answer_check부터. FU/FV 재대조·G036 재blind 금지. FW/FX/FY 공식답 대조를 전부 저장한 뒤 G036 전체 independent_code, 그 전체 저장 후에만 SDSS 공개. 새 group 전 meta_state 실행. G035 귀납은 meta8에 통합되어 별도 반복 귀납 불필요.",
  "source_quality": [
    "FI 최초 선택지㉯ 열 누락 hold 보존. 보조원 XML 기계 복원 FI_choices_supplement.json을 주 Astra 직접 판독한 뒤 유효 blind 완료. 정본 연결 provenance 별도 보존; KICE 원 PDF 직접 대조 아님.",
    "G032 우발 해설 노출 및 로컬 수록 HWPX 수식 복원 qualification 유지. FH 경계 잔재·G024·DP/CZ/G022 기존 hold 유지."
  ],
  "luna_action": "queue/processed source_record_id 차집합만 후처리. raw immutable 유지하고 신규 payload를 기존 MD/JSONL 및 processed에 반영. CURRENT/ASTRA_CHECKPOINT/handoff 최신화. semantic 판단 보완 금지. 미완료 G036 답/태그 및 신규 blind source를 읽지 말 것. 실제 수량·ID·장벽은 기계 검증. 이번에는 backlog 추가 없이 후처리만 수행.",
  "action": "safe raw/checkpoint 저장 직후 gpt-5.6-luna medium fork none 실제 spawn. 후처리 완료 대기 후 Astra 종료."
}
```


<!-- luna-raw:GL-hold-20260914-source-missing-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G039",
  "reason": "blind source 보기가 측정 장치 그림이라고 하나 그림이 누락되어 있다.지문 수식에도2f1₁이라는 첨자 추출 흔적이 있어④의 정확 수식 대조가 필요하다.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "소리 자극으로 청세포가 반응하여 발생한 귀의 소리는 자극보다 먼저 감지될 수 없다는①의 오류가 유력하다.하지만 장치 그림 및④ 수식 원문을 확인하지 않아 전체 유효blind 완료를 선언하지 않는다.",
  "next_work": "공식 연결 원문에서 GL 장치 그림과 해당 지문 수식만 blind-only supplement로 기계 복원 후 주 Astra가 직접 판독한다.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "barrier": "G039 전체 유효blind 완료 전 답 공개 금지.GK 최초blind 보존;GM 독립blind는 가능.",
  "source_quality": "manifest visual_placeholder=false는 실제 그림 존재를 보장하지 않았다.기계 verifier 오류0과 의미·시각 완전성은 구별한다."
}
```


<!-- luna-raw:G039-hold-20260914-quota-threshold-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "caution primary9%/weekly8%에서 GL atomic blind 저장 직후 실측이 primary1%/weekly7%로 최초 threshold에 도달함.정상 Luna handoff.",
  "quota": {
    "primary_used_percent": 99,
    "primary_remaining_percent": 1,
    "weekly_used_percent": 93,
    "weekly_remaining_percent": 7
  },
  "runtime_emergency_warning_observed": false,
  "processed_at_session_start": 717,
  "last_completed_atomic_record": "GL-blind-20260914-02",
  "completed_groups_this_session": [
    "G036",
    "G037",
    "G038"
  ],
  "current_group": "G039",
  "group_cases": [
    "GK",
    "GL",
    "GM"
  ],
  "blind_done": [
    "GK",
    "GL",
    "GM"
  ],
  "answer_check_done": [],
  "independent_code_done": [],
  "sdss_compare_done": [],
  "exposure": {
    "G039_official_answers_seen": false,
    "G039_sdss_seen": false,
    "GL_source_identity_seen_during_restoration": true,
    "GL_device_figure_directly_seen": true
  },
  "meta_state_last_sync": {
    "meta_due": false,
    "manual_parity_audit_due": false,
    "depth_backfill_pending": [],
    "meta_induction_count": 9,
    "baseline_completed_groups": 37,
    "baseline_completed_questions": 162
  },
  "new_semantic_assets": [
    "G036-induction-20260914-02",
    "G036-G037-induction-20260914-02",
    "META-G036-G038-meta_induction-20260914-02",
    "AUDIT-meta9-manual_parity_audit-20260914-02",
    "GJ-depth_backfill-20260914-02",
    "GC-depth_backfill-20260914-02"
  ],
  "source_quality": [
    "GL 그림 누락 hold는 canonical 연결 로컬 HWPX 추출그림의 주 Astra 직접 판독으로 해소.원 배포 정본 확인 아님.",
    "GL 최대 주파수식의2f1₁ 중복 첨자 원 표기는 미검증.보조원 GL_formula_supplement.md 정규화는 원 수식 독립 검증이 아니다.GL 답1은 수식 없이 자극→발생→전달의 순서로 결정하여blind 저장.④의 수식 대응 불확실성 및 전체 원문 완전검증 성과 제외를 보존.",
    "GC② 상세 법해석 및GD 기간 부가 해석 유보.사전 뜻 구획 미검증 유지.",
    "기존G024·DP/CZ·G032 노출/정본 qualification 모두 유지."
  ],
  "backlog_preparation": "병행 Luna가G038~G046/GF~HI30문항 기계 준비.보고상manifest191문항46groups 및누출/중복/error0.현재G039 진행중이며G040부터 대기.기계 검증0이어도GL 그림 누락이 발견되어 원문 완전성 보증으로 사용하지 않는다.",
  "next_work": "다음 Astra는G039 GK answer_check부터.전체blind 완료이므로group 전체answer_check→전체independent_code→장벽 확인 후SDSS 공개.답/태그는 현재 모두 미공개.이미 완료한G036~G038 및meta9/audit/backfill 반복 금지.",
  "luna_action": "queue/processed source_record_id 차집합만 기존MD/JSONL 및processed에 원 payload대로 반영.CURRENT/ASTRA_CHECKPOINT/handoff 최신화.raw 수정 금지.미완료G039 답/태그 및새blind source 열지 말고 의미 판단 보완 금지.GL 수식 정규화 한계와GC 유보가 해소된 것으로 기록하지 말 것.실제ID/단계/미처리수는 기계 확인.추가backlog 준비 없이 이번 후처리만 완료.",
  "action": "safe raw/checkpoint 저장 직후fresh gpt-5.6-luna medium fork none 실제spawn.후처리 대기 후Astra 종료."
}
```


<!-- luna-raw:G039-hold-20260914T060728Z-session-start-weekly-threshold -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "새 세션 초기 실제 quota 조회에서 weekly remaining 6% 최초 관측. 사용자 정상 handoff threshold에 따라 신규 semantic stage 시작 전 중지.",
  "quota": {
    "primary_used_percent": 4,
    "primary_remaining_percent": 96,
    "weekly_used_percent": 94,
    "weekly_remaining_percent": 6
  },
  "runtime_emergency_warning_observed": false,
  "queue_before_checkpoint": 785,
  "processed_before_checkpoint": 785,
  "unprocessed_before_checkpoint": 0,
  "current_group": "G039",
  "group_cases": [
    "GK",
    "GL",
    "GM"
  ],
  "blind_done": [
    "GK",
    "GL",
    "GM"
  ],
  "answer_check_done": [],
  "independent_code_done": [],
  "sdss_compare_done": [],
  "new_semantic_research_this_session": false,
  "exposure": {
    "new_blind_source_read": false,
    "G039_official_answers_seen": false,
    "G039_sdss_seen": false,
    "prior_source_qualifications": "기존 GL 그림 복원 및 수식 원표기 미검증 qualification 보존. 이번 세션 재판단 없음."
  },
  "meta_state_last_sync": {
    "meta_due": false,
    "manual_parity_audit_due": false,
    "depth_backfill_pending": [],
    "meta_induction_count": 9,
    "completed_groups": 37,
    "completed_questions": 162
  },
  "next_work": "quota가 허용되는 다음 Astra 세션에서 GK answer_check부터. G039 전체 answer_check→전체 independent_code 저장→장벽 확인→SDSS 공개. 기존 blind 및 완료 meta9/audit/backfill 반복 금지.",
  "luna_action": "신규 hold raw만 원 payload로 기존 기록·processed에 반영. CURRENT와 checkpoint 최신화. 신규 source·sealed answer/SDSS 열람 및 의미 판단·backlog 준비 금지. queue 원문 불변. 후처리 완료를 보고.",
  "action": "checkpoint 저장 직후 gpt-5.6-luna medium fork none 실제 spawn, 후처리 완료 대기 후 Astra 종료."
}
```


<!-- luna-raw:GN-hold-20260915-missing-figure-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G040",
  "reason": "blind source에 보기 그래프의 노드/간선 위치가 없다. 시계/반시계 및 ㉠~㉢·ⓐⓑ 대응을 결정할 수 없다.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "C는 콜리신으로 S에 우세, R은 저항성과 C보다 빠른 증식으로 C에 우세, S는 R보다 빠른 증식으로 R에 우세다. C→S→R→C의 순환이나 도형상의 방향과 빈칸 위치는 미확인이다.",
  "next_work": "보조원이 답/태그 없는 공식 문제 그림을 복원하면 주 Astra가 직접 판독하여 선택지 매핑한다. [A] 정확 범위도 확인 필요.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "GN 유효 blind 저장 전 G040 답 공개 금지",
  "source_quality": "manifest visual_placeholder=false가 보기 그림 완전성을 보장하지 않음"
}
```


<!-- luna-raw:GQ-hold-20260915-choice-map-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G041",
  "reason": "목표 설정 항목이 stem에 있고 choices 마지막이 빈 문자열이다. 항목과 공식 선택 번호의 매핑을 검증할 수 없다.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "글에는 한자 구성 원리를 이용한 이론 설명은 있으나 특성을 보여 주는 영화 작품을 폭넓게 모아 제시한 내용이 없다. 따라서 자료 수집 항목이 구현되지 않았다.",
  "tentative_mapping_not_answer": "목표/예상독자/내용/자료/논지의 다섯 항목이라면 자료는 네 번째지만 추출 배열 index로 번호를 확정하지 않는다.",
  "next_work": "공식 문제 원문에서 번호와 항목 대응만 blind supplement로 복원 후 직접 확인",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "GQ 유효 blind 완료 전 G041 전체 답 대조 금지"
}
```


<!-- luna-raw:SYNC-hold-20260915-three-groups-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "사용자 신규 운영 규칙:마지막 Luna sync 이후3개 passage group 완전 완료마다 due meta/audit/backfill 저장→Luna sync1회→pending raw0 확인→Astra 연구 계속. quota emergency 우선.",
  "completed_groups_since_last_luna_sync": [
    "G039",
    "G040",
    "G041"
  ],
  "last_completed_atomic_record": "META-G039-G041-meta_induction-20260915-01",
  "meta_state_after_sync": {
    "meta_induction_count": 10,
    "meta_due": false,
    "manual_parity_audit_due": false,
    "depth_backfill_pending": []
  },
  "next_passage_group": "G042",
  "next_case": "GT",
  "next_stage": "blind",
  "next_group_exposure": {
    "blind_source_seen": false,
    "official_answer_seen": false,
    "sdss_seen": false
  },
  "quota_status": "unavailable",
  "runtime_emergency_warning_observed": false,
  "action": "진행 중 Luna에 정식 sync 요청. queue 원문 불변,신규 raw 문서/processed 반영 및 CURRENT/checkpoint 최신화. pending0 확인 후 같은 Astra 연구 계속. quota handoff나 세션 종료로 기록하지 않는다.",
  "operating_instruction_persistence": "Luna가 AGENTS.md 및 ASTRA_START.md에 신규3group sync 규칙 추가."
}
```


<!-- luna-raw:GV-hold-20260915-graph-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G042",
  "reason": "A 및ⓐⓑⓒ 그래프가 blind source에 없어 변화 종류를 기호/선택 번호에 대응할 수 없다.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "㉠만기 접근은 같은 금리 변화에 따른 가격 변화폭 감소이므로 가격-금리 곡선의 가파름이 줄어드는 변화다.㉡주식 수익 증가는 채권 수요 감소로 같은 금리에서 가격이 더 낮아질 수 있는 변화다.",
  "next_work": "답/태그 없는 원문 그래프 복원 후 축 방향과 A/ⓐⓑⓒ 위치를 직접 판독한다.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "GV 유효 blind 전 G042 전체 답 공개 금지"
}
```


<!-- luna-raw:GZ-hold-20260915-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G043",
  "reason": "선택지 다섯 개가 모두 빈 문자열이고 지문 천체 그림/[A] 범위가 누락되어 번호 선택 불가.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "회전하는 식탁은 지구 공전의 반대쪽으로 이동하는 춘분 위치에 대응한다. 창가를 걷는 철수는 지구,이동하는 식탁까지 먼저 오는57초는 회귀년,고정된 폭포 방향까지 돌아오는60초는 항성년에 대응할 것으로 판단한다.",
  "confidence_in_partial_mapping": "높음,그림의 실제 대상 표지와 선택지 매핑은 미확인",
  "next_work": "답/태그 없는 선택지 표와 공통 지문 그림 및[A] 범위를 복원해 주 Astra가 직접 판독한다.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "GZ 유효 blind 전 G043 전체 답 공개 금지"
}
```


<!-- luna-raw:HD-hold-20260915-graph-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G044",
  "reason": "보기 A/B 그래프가 빠져 기준 저항,정상상태 저항 및50%/90% 도달 시간을 읽을 수 없다.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "가스 종류는 저항 증가/감소 방향,감도는 정상값과 공기 중 기준값의 상대차,응답 시간은 목표 비율 도달 시간으로 각각 판정해야 한다. 정상값이 같다고 응답 시간이 같다고 할 수는 없다.",
  "next_work": "복원 그래프에서A/B 기준값·정상값·변화 곡선·시점 표지를 직접 읽고 선택지를 판정",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "HD 유효 blind 전 G044 전체 답 공개 금지"
}
```


<!-- luna-raw:SESSION-hold-20260915-user-stop-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
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
```


<!-- luna-raw:GZ-hold-20260915-form-verification-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G043",
  "completed_verification": "주 Astra가 로컬 KICE 정답표 이미지의 홀수형 제목·35번⑤와 EBSI 문제 전체 페이지의 짝수형 제목·35번① 지구/회귀년/항성년을 직접 확인. 서로 다른 시험형 자료를 대조한 사실은 확정. 짝수형 공식 정답표 번호는 아직 직접 미확인.",
  "sources": [
    "자료/평가원_정답표/OCR대조_페이지/2011_수능/page_001.png",
    "/tmp/gz_page_012.png"
  ],
  "original_blind_preserved": true,
  "original_mismatch_preserved": true,
  "next_work": "짝수형 공식 정답표 원문 직접 확인 후 유효 answer_check 보완. 그 전G043 전체 independent_code/SDSS 금지.",
  "exposure": {
    "G043_sdss_seen": false,
    "G043_official_answers_seen": true,
    "incidental_source_exposure": "전체 문제 이미지 우측/하단2011수능37~39번 지문·선지 일부가 함께 표시됨. 홀수형 정답표1~50번도 함께 표시됨. 향후 해당 사례를 신규 strict blind로 집계하지 말 것.",
    "strict_performance_note": "GZ의 최초 풀이 노출 상태는 당시 raw 보존. 사후 확인을 새로운 blind 성과로 세지 않음."
  },
  "quota_status": "unavailable",
  "reason": "번호 대응 검증 진행 중;세션 종료hold 아님"
}
```


<!-- luna-raw:BACKLOG-hold-20260915-identity-exposure-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "기계 보조원의 신규 준비 완료 보고에 허용한 case/group/path/count 외 시험 연도·회차·문항번호가 포함되어 주 Astra에 노출됨. 의미 연구 중단이나 quota handoff가 아니라 향후 노출 기록용 hold.",
  "case_range": "HN~IR",
  "passage_groups": [
    "G048",
    "G049",
    "G050",
    "G051",
    "G052",
    "G053",
    "G054",
    "G055",
    "G056"
  ],
  "exposure": {
    "source_identity_seen": true,
    "blind_source_seen": false,
    "official_answers_seen": false,
    "sdss_seen": false,
    "prior_project_judgments_seen": false
  },
  "next_work": "각 사례 시작 시 source_identity_disclosed_before_blind=true를 보존. 공식답/태그 노출로 등치하지 않음. 완료보고에 시험식별정보를 넣지 않도록 보조원에 지시함. 기존2011수능언어 노출 제외 유지.",
  "mechanical_report": "신규31건,manifest226;content leakage0/duplicates0/overlap0/errors0;identity leakage검사2건은보조원추가확인중이며해소된것으로확정하지않음.",
  "raw_semantic_research_on_new_backlog": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:HI-hold-20260915-range-evidence-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G046",
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/HI_A_range_supplement.md",
    "data/기본기_연구/prepared_backlog/sealed/HI_A_range_provenance.json"
  ],
  "reason": "補助원 supplement는 로컬 교재 HWPX와 정규화 MD 경유인데 실제 원문 세로괄호 범위라고 확정한다. 주 Astra가 확보된 증거만으로 공식 원배포 괄호 직접 검증 완료라고 판단할 수 없어 기존 미확인을 유지한다.",
  "completed_judgment": "제안 범위의 문장들은 기존 blind source와 연결되지만 실제 괄호의 시작/끝 증거는 별도다. HI 풀이 자체의 완료와 원문 범위 완전검증을 분리.",
  "next_work": "보조원에 로컬 교재 기반 범위 후보 qualification으로 정정하고 공식 문제 괄호 이미지 확보 요청. 주 Astra 직접 확인 전 범위 미확인 해소 금지.",
  "original_blind_preserved": true,
  "sdss_disclosed": true,
  "new_blind_performance_claimed": false,
  "session_stop": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:HP-hold-20260915-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G048",
  "reason": "보기악보및ⓐ~ⓔ위치가누락되어선지의지시대상을판독할수없음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "본문상라단조는경건·웅장,다장조는기쁨.끊기는음형은눈물,상행가락은높음을표현할수있으나실제악보의기호와지시대상이없는상태에서는번호판정불가.",
  "next_work": "답/태그없는원문악보와ⓐ~ⓔ지시범위복원후직접판독",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_identity_disclosed_before_blind": true
  },
  "group_barrier": "HP/HQ유효blind저장전G048전체answer_check금지",
  "source_quality": "manifest complete/visual_placeholder=false가실제시각·표완전성보증아님",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:HQ-hold-20260915-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G048",
  "reason": "선택지의A/B두열중한열만추출된것으로보이며B열번호대응을확인할수없음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "손가락으로가야금줄을연주하는행위는뜯다,채로장구를연주하는행위는치다가자연스럽다.그짝의실제선택번호는아직미확인.",
  "next_work": "공식선택표A/B각행의두단어를blind-only로복원후번호선택",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_identity_disclosed_before_blind": true
  },
  "group_barrier": "HP/HQ유효blind저장전G048전체answer_check금지",
  "source_quality": "manifest complete/visual_placeholder=false가실제시각·표완전성보증아님",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:HU-hold-20260915-target-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G049",
  "reason": "공통본문의㉮가측정앞에있으나밑줄끝범위가보존되지않음.발문이요구하는말이측정인지뒤절전체인지확정원문이필요.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "측정이라는단어를대상으로한다면②~⑤는양을대중/재기/가늠/어림하는행위이며①은이미주어진개수를단위로환산한다.다만대상범위를추정한채최종번호를저장하지않는다.",
  "next_work": "공식문제원문의㉮밑줄범위를답/태그없이확인한뒤유효blind선택저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_identity_disclosed_before_blind": true
  },
  "group_barrier": "HR/HS/HTblind는저장됨.HU유효blind전G049전체answer_check금지.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:HW-hold-20260915-path-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G050",
  "reason": "보기(가)/(나)의헤드이동경로그림이없어실제경로를스케줄링방식에대응할수없음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "53에서증가방향으로진행중이다.SCAN은증가방향의98,122,183을처리하고끝199까지갔다감소방향요청을처리한다.LOOK은대기최댓값183에서되돌아온다.SSTF는현재53에서가장가까운37로먼저갈것이다.어느경로가그림(가)/(나)인지미확인.",
  "next_work": "답/태그없는(가)/(나)경로그림의트랙표지와이동순서를복원한뒤직접판독",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_identity_disclosed_before_blind": true
  },
  "group_barrier": "HW유효blind전G050전체답대조금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:HW-hold-20260915-label-map-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G050",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/HW_paths.png",
  "reason": "두경로는직접판독했으나합친이미지에(가)/(나)라벨이없어위아래순서와원문지시대응을기계확인중.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "위그림은53→37→14→98→122→183으로매단계가장가까운요청을선택한다.아래그림은53→98→122→183→37→14로현재증가방향을유지하다최대요청183에서반전하고199까지가지않는다.각각SSTF와LOOK에해당한다.",
  "next_work": "위=가/아래=나의실제문서앵커대응을확인후선택표번호대응;확인전순서추정금지",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_identity_disclosed_before_blind": true
  },
  "source_qualification": "로컬교재시각자료image11/image12결합경유이며원배포문제PDF직접검증아님.",
  "group_barrier": "HW유효blind전G050전체답공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:IK-hold-20260915-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G054",
  "reason": "blind packet에 A/B/C 속력 분포 그래프가 없어 곡선 라벨을 온도·기체에 대응할 수 없음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "같은 25℃에서 무거운 크립톤이 더 느리고 가벼운 아르곤이 더 빠르다. 같은 아르곤이면 727℃가 25℃보다 빠르다. 따라서 꼭짓점 왼쪽부터 크립톤25℃, 아르곤25℃, 아르곤727℃. A/B/C의 실제 위치는 미확인.",
  "next_work": "A/B/C 곡선 라벨이 포함된 답·태그 없는 공식 시각 원문을 blind_sources에 복원 후 주 Astra가 직접 판독",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_identity_disclosed_before_blind": true
  },
  "group_barrier": "IK 유효 blind 저장 전 G054 전체 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:IO-hold-20260915-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G055",
  "reason": "보기의 A/B/C 부피-압력 그래프와 P1/P2/P3 표지가 누락되어 구간별 곡선 관계를 판독할 수 없음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "압력이0에 가까워지고 거리가 멀어지면 인력 영향이 약해지므로①의 상호 작용 증가 주장은 지지되지 않는다. 압력을 높여도 실제 기체는 반발력으로 이상 기체만큼 부피가 줄지 않으므로⑤는 부적절하다. 나머지 구간별 A/B의 상대 곡선 위치 미확인.",
  "next_work": "A/B/C·P1/P2/P3 및 실제 축 표기 그래프를 blind-only로 복원하고 직접 판독. 원문 누락 수식도 가능하면 문장 앵커와 함께 복원하되 답/태그/해설 혼입 금지.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_identity_disclosed_before_blind": true
  },
  "group_barrier": "IO 유효 blind 저장 전 G055 전체 answer_check 금지. G054 답대조 먼저 수행.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:IR-hold-20260915-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G056",
  "reason": "보기 그림 누락으로 ㉠~㉣이 두 셀의 G/p형 어느 위치인지 확인할 수 없음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "같은 블록 두 셀을 먼저 소거하여 <0 0>을 만든 뒤 둘째 셀에1을 쓴다. 소거는 두 셀 p형에20V, 쓰기는 둘째 셀G에20V. 지시기호 위치와 선택 번호 대응은 미확인.",
  "next_work": "두 셀 구조와 ㉠~㉣을 포함한 보기 그림 및 단계별 선택표 원문 앵커 복원 후 Astra 직접 판독",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_identity_disclosed_before_blind": true
  },
  "group_barrier": "IR 유효 blind 전 G056 전체 답공개 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:IW-hold-20260915-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G058",
  "reason": "[A] 시작/끝 괄호가 누락되어 질문 근거의 허용 범위를 확정할 수 없음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "두 전제에서 의식의 실재 함의 차이를 설명하는 문단이 포함되면①이 직접 답해진다. 다만 packet의[A]위치만으로 실제 범위를 확정하지 않는다.",
  "next_work": "[A] 세로괄호 시작·끝이 보이는 공식 문제 crop 또는 로컬 문서 범위 근거 복원",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_identity_disclosed_before_blind": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "IW/IX 유효 blind 전 G058 전체 답 공개 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:IX-hold-20260915-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G058",
  "reason": "학습 활동지 선택번호가 문장 중간에서 분리되어 ⑤가 비어 있고 실제①~⑤의 귀속 범위를 알 수 없음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "스트로슨은 자아 인식이 경험에서 추상화된다고 하므로 경험적 인식이 자아 인식에 의존한다는 문장이 잘못이다. 그 문장의 실제 선택번호는 현 packet만으로 확정하지 않는다.",
  "next_work": "학습 활동지 전체 표와①~⑤ 번호의 문장 대응을 시각 또는 XML 앵커로 복원",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_identity_disclosed_before_blind": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "IW/IX 유효 blind 전 G058 전체 답 공개 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:IW-hold-20260915-range-evidence-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G058",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/IW_A_range_supplement.md",
  "reason": "supplement는 텍스트 [A] 이후 문단을 범위 후보로 삼았으나 실제 세로괄호의 시작/끝 증거가 없다. 제안 범위는 스트로슨 비판까지 포함하므로 문항①/②의 답 가능성을 바꾸는 실질적 불확실성이다.",
  "selected_answer": null,
  "completed_judgment": "원래 두 전제의 의식 함의 차이 문단을 포함한 범위면①이 직접 답해진다. 현재 supplement처럼 뒤의 스트로슨 문단까지 포함하면②도 답 후보가 된다. 따라서 텍스트 표식 뒤에 있다는 이유로 범위를 확정하지 않는다.",
  "next_work": "공식 문제 형식의 원문 PDF에서[A]세로괄호와 주위 문단을 포함한 crop을 확보.원배포서버직접bytes가아니라도공식형식PDF보관본인지provenance분리.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "IW 유효 blind 저장 전 G058 전체 답공개 금지",
  "source_hold_preserved": true,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:JS-hold-20260916-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G066",
  "reason": "보기의A~E다이빙자세그림과검은회전축·화살표가packet에누락. B의실제자세및각단계비교를판독할수없음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "외부돌림힘없으므로공중각운동량은보존되어①은맞지않음.같은선수의자세변화만으로질량요소의총질량이줄어드는②는지지되지않음.팔다리전개시축거리증가로관성이커지는모형에④의감소는반대. B가최소관성자세인지의직접그림근거는없음.",
  "next_work": "A~E자세·축·방향이모두보이는답/태그없는공식도식또는로컬HWPXembedded원그림복원후주Astra직접판독. 선지소거만으로그림을추정복원하지않음.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "JS유효blind raw저장전G066 JR/JS전체answer_check금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:KB-hold-20260916-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G069",
  "reason": "복원된보기물체·A/B/C그림은직접확인했으나선택지①~⑤가빈문자열로만있어그래프번호를판독할수없음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "B방향은그림의45도평행광선이고,환산값은투과량이아닌감쇄량이다. 각평행경로의물체통과길이·재질을따라감쇄프로파일을비교해야한다. 선지그래프형태와번호대응없음.",
  "next_work": "공식원문또는로컬HWPX의①~⑤그래프전체를번호순서와축기준포함하여blind_sources에복원. 각이미지별선택번호의XML앵커필수.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "KB유효blind저장전G069전체answer_check금지. JZ/KAblind만완료.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:KS-hold-20260917-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G074",
  "reason": "blind source의 보기 만화 칸1~6 이미지가 빠져 각 선지의 시각 근거를 검증할 수 없음. READY metadata보다 실제 source 상태를 우선.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "본문은 정지 이미지에서도 움직임을 상상할 수 있고 효과선이 이를 더욱 부추긴다고 한다. 효과선 제거로 모든 움직임 단서가 사라진다는 일반화는 의심되지만 실제 칸4와 나머지 칸의 언어/비언어 정보·형태·크기를 아직 보지 못했다.",
  "next_work": "Luna가 답·태그 없이 로컬 HWPX의 보기 만화 bitmap과 칸 연결 provenance를 복원하면 주 Astra가 직접 확인하여 KS blind 저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "KS 유효 blind 저장 전 G074 전체 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:LJ-hold-20260917-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G079",
  "reason": "선택지①의 배수 수식이 누락되어 문장 전체의 참거짓을 검증할 수 없음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "거리3배이면 제곱 반비례로 플럭스1/9. 겉보기 등급 -1과1은 두 등급 차이이므로 약2.5²=6.25배이며⑤의2.5배는 틀린 방향이다. 그러나①이 올바르게1/9라고 쓰였는지 현재 원문에 없으므로 유일답을 확정하지 않음.",
  "next_work": "Luna의 로컬 HWPX equation/선택번호 anchor 복원 뒤 주 Astra가① 수식을 확인하고 blind 저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "LJ 유효 blind 저장 전 G079 전체 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:LK-hold-20260917-source-map-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G079",
  "reason": "LK 보강파일이 rowCnt4/colCnt5와 col5까지의 3행6열 mapping을 동시에 주장하여 원XML 좌표라는 provenance가 자기불일치. 최초 선형 표 풀이를 원XML 검증 완료로 승격할 수 없음.",
  "original_blind_preserved": true,
  "selected_answer": 3,
  "next_work": "Luna가 실제 LK 표의 tc/cellAddr/cellSpan/텍스트를 그대로 추출하여 인접 표 오매핑 여부를 교정하면 Astra가 수치·헤더·행 귀속을 확인.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "LJ/LK 최초 blind는 저장됐지만 신규 발견 source provenance 불일치 해소 전 G079 answer_check 보류.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:LR-hold-20260917-source-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G082",
  "reason": "발문이 지정한[A]세로괄호의 시작·끝 근거가 blind packet에서 빠지고 문단 중간의[A]문자만 남아 있음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "전체 본문에서는 취미판단이 개별대상의 형식에 대한 쾌/불쾌로 미추를 정하며 교훈·실용·개념을 배제하므로 권선징악의 교훈을 이유로 아름답다고 하는 선지가 의심된다. 다만[A]의 실제 근거 범위를 아직 확인하지 못함.",
  "next_work": "Luna가 원본 형식의 세로괄호 범위 evidence를 blind supplement로 제공한 뒤 주 Astra가 직접 확인하고 LR blind 저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "LR 유효 blind 전 G082 전체 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:LR-hold-20260917-range-evidence-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G082",
  "reason": "LR_scope_supplement_20260917.json은[A]marker cell과 뒤의 취미판단 정의 시작 문구만 제공하며 세로괄호 끝 위치는 not_confirmed. 처음 hold를 해소할 충분한 시각/범위 근거가 아직 없음.",
  "selected_answer": null,
  "next_work": "해당 공식 형식 원문 PDF 또는 HWPX 렌더링에서[A]세로괄호 전체와 앞뒤 본문을 포함하는 crop 확보. 인쇄본의 정확한 범위를 직접 판독할 것.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_collection_title_disclosed": true
  },
  "source_hold_preserved": true,
  "group_barrier": "LR 유효blind 전 G082전체 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:LR-hold-20260917-range-topology-03 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G082",
  "reason": "新版 supplement의 start/end anchor는 본문 한 문장 중간에 삽입된 괄호 표 object의 XML 앞뒤 위치다. 주어진 두 anchor 사이에는 본문 내용이 없으므로 실제 지면 세로괄호가 감싸는 텍스트 범위를 입증하지 못한다. 표 자체 border topology와 본문에 대한 수직 배치는 구별해야 한다.",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/LR_scope_supplement_20260917.json",
  "rejected_source_claim": "start_and_end_verified_from_canonical_hwpx_table_topology",
  "selected_answer": null,
  "next_work": "보조자가 검증완료 주장을 철회하고 공식 형식 PDF 또는 실제 HWPX 렌더링의 세로괄호와 본문 전체 crop을 복원. XML로 확인하려면 object 위치·높이와 실제 조판 본문 좌표가 모두 필요.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "source_collection_title_disclosed": true
  },
  "group_barrier": "LR 유효 blind 저장 전 G082 전체 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G086-hold-20260917-answer-provenance-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G086",
  "case_ids": [
    "MH",
    "MI",
    "MJ",
    "MK"
  ],
  "reason": "네 sealed 정답이 모두 blind 풀이 및 명시 원문 근거와 충돌. 해당 시험지·정답표 연결을 검증할 때까지 독립 코드/SDSS 진행 보류.",
  "mechanical_provenance_finding": "scripts/luna_prepare_frontier.mjs:132~133은 q.answer를 복사하면서 official_answer_verified라는 source 문자열을 고정 기재한다. 이 출력 문자열 자체는 실제 정답표 확인을 실행했다는 증거가 아니다. 정확한 상류 오류 원인은 아직 미확정.",
  "completed_work": "그룹 전체 blind와 최초 sealed 대조 raw 저장. 최초 답·prepared_reference_answer·불일치 이유를 모두 보존.",
  "next_work": "Luna의 공식형식 시험지 및 정답표 번호 연결 evidence 확보 후 Astra 직접 대조. canonical question text와 answer mapping이 서로 다른 시험형/번호에서 결합했는지 확인.",
  "exposure": {
    "official_answer_reference_seen": true,
    "official_answer_independently_verified": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G086-hold-20260917-answer-provenance-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G086",
  "case_ids": [
    "MH",
    "MI",
    "MJ",
    "MK"
  ],
  "reason": "정답 provenance 확인 계속. 기존 blind와 최초 불일치 기록은 수정하지 않음.",
  "mechanical_provenance_finding": "scripts/normalize_kice_reading_corpus.py choose_answer는 answer_table_ids를 순회하여 candidates[table_variant]=value로 저장하며 같은 variant 키는 덮어쓴다. 이후 official_answer_verified는 answer is not None로 설정된다. 검증 표기는 원문 선택지 순서와의 대조까지 수행했다는 뜻이 아니다.",
  "hypothesis_not_confirmed": "같은 A/B variant 안의 홀수형·짝수형 또는 다른 표가 한 키로 합쳐질 수 있으나 G086의 실제 원인으로 아직 확정하지 않음.",
  "next_work": "Luna가 확보한 문제 원문과 공식형식 정답표에서 시험연도·A/B형·홀짝형·문항번호·선택지 순서를 대조한 뒤 주 Astra가 확정",
  "exposure": {
    "prepared_reference_answer_seen": true,
    "sdss_seen": false
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G086-hold-20260917-answer-variant-03 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G086",
  "case_ids": [
    "MH",
    "MI",
    "MJ",
    "MK"
  ],
  "reason": "정답 오연결의 구체 원인 확인: B형 문항이 A형 단독 candidate 정답을 승계함.",
  "mechanical_evidence": [
    "provenance_mapping은 2016 수능B Q17~20을 가리킴",
    "해당 canonical 4 records의 variant는 B이나 answer_candidates는 각각 A:②/A:④/A:②/A:③뿐임",
    "normalize_kice_reading_corpus.py choose_answer는 요청 B candidate가 없으면 모든 candidate의 값 집합 크기가1인지 검사해 그 유일값을 반환함",
    "그 결과 A형 단독값이 B형 answer로 채택되고 answer is not None 조건으로 official_answer_verified=true가 됨"
  ],
  "supersedes_hypothesis": "앞 hold의 홀짝 중복키 가능성은 이번 G086 확정 원인으로 채택하지 않음. 이번 확인된 원인은 요청 B형 부재 상태에서 A형 단독값을 수용한 fallback.",
  "next_work": "실제 2016 수능B 문제와 B형 공식 정답표의 번호·선택지 대조 후 교정된 answer_check raw 저장. 기존 A형 오연결 값은 이력 보존.",
  "exposure": {
    "prepared_reference_answer_seen": true,
    "sdss_seen": false
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:MX-hold-20260917-missing-graph-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G090",
  "reason": "발문이 곡선 B의 실제 그림을 지시하지만 blind packet에 그림 placeholder만 있고 그래프 asset·축·A/B 위치가 연결되지 않음.",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "본문상 보통 물질은 중심에 집중되고 암흑 물질은 궤도 안쪽에 퍼진 추가 중력 원천이다. 중심부 거리-속력 관계만으로 암흑물질의 중심 집중을 단정한④는 의심되지만 실제 중심부 곡선 모양과 A/B 경계를 아직 직접 보지 못했다.",
  "next_work": "Luna가 답·SDSS 없이 canonical HWPX embedded 원그래프 또는 공식형식 문제 crop을 blind_sources에 복원하면 Astra가 축·곡선·중심부 범위를 직접 판독하여 MX blind 저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "MW blind는 완료. MX 유효 blind 저장 전 G090 모든 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G092-hold-20260917-answer-variant-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G092",
  "case_ids": [
    "NB",
    "NC"
  ],
  "reason": "sealed 정답과 원문의 충돌; B형 문항에 A형 단독 정답 candidate가 연결된 상태를 확인",
  "mechanical_evidence": [
    "provenance와 canonical question_id는 2016 수능B Q29/Q30",
    "두 canonical record는 variant=B이나 answer_candidates가 각각 A:⑤/A:②뿐임",
    "sealed 공식정답 필드는 canonical answer⑤/②를 복사함. official_answer_verified=true는 B형 원표 검증의 증거가 아님"
  ],
  "next_work": "Luna가 기존 G086 공식형식 B형 문제·홀수형 정답표에서 Q29/Q30만 crop하면 주 Astra가 문항·선지순서·표 번호를 직접 대조하여 correction raw 저장",
  "exposure": {
    "prepared_reference_answer_seen": true,
    "official_answer_independently_verified": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "original_blind_preserved": true,
  "group_barrier": "정답 provenance hold 해소 전 independent_code·SDSS 공개 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G092-hold-20260917-stale-canonical-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G092",
  "case_ids": [
    "NB",
    "NC"
  ],
  "reason": "현재 정규화 코드의 guard와 과거 생성 canonical/backlog 상태를 구별해야 함",
  "mechanical_evidence": [
    "현재 scripts/normalize_kice_reading_corpus.py choose_answer는 명시 A/B variant와 같은 candidate만 허용",
    "현재 answer_is_mechanically_resolved도 B candidate 부재를 거부",
    "그러나 G092 canonical은 여전히 B문항에 A답 단독 연결 상태. 현재 guard 신규 회귀라고 주장할 수 없고 과거 산출물 잔존 문제로 제한"
  ],
  "next_work": "NB/NC 공식형식 정답표 대조 후 기존 값을 덮어쓰지 않고 correction raw 및 supplement 저장. 향후 prepared 답 공개시 후보와 variant의 실제 일치를 확인.",
  "exposure": {
    "prepared_reference_answer_seen": true,
    "sdss_seen": false
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G092-hold-20260917-crop-scope-03 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G092",
  "case_ids": [
    "NB",
    "NC"
  ],
  "completed_source_check": "정답표 crop에서29→④,30→⑤를 직접 확인. 문제 crop에서 Q30 보기·5선지와 Q29①~④는 blind packet과 일치.",
  "remaining_source_gap": "Q29⑤ 하단이 잘렸고 시험지와 정답표의 B형/홀수형 제목은 현재 crop에 없음. 제목·형식·선지전체 직접 대조 완료로 승격하지 않음.",
  "next_work": "Luna가 Q29⑤까지 온전한 crop, Q30 한정 crop, 문제지 및 정답표 header를 제공한 후 주 Astra가 확인하여 correction 저장",
  "exposure": {
    "prepared_reference_answer_seen": true,
    "answer_table_cells_seen": true,
    "sdss_seen": false,
    "incidental_other_source": "첫 문제 crop 오른쪽에 인접 Q31~33 문학지문 앞부분이 포함됨. 해당 범위는 재 blind로 주장하지 않음; 다른 정답은 미노출"
  },
  "original_blind_preserved": true,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:NS-hold-20260917-choice-table-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G096",
  "reason": "발문은ⓐ/ⓑ/ⓒ세열을㉮~㉱와대응시키는표인데blindchoices는각선지의첫글자㉮/㉮/㉱/㉱/㉱만남아ⓑ/ⓒ열이없음.",
  "selected_answer": null,
  "next_work": "Luna가답·태그없이로컬canonicalHWPX에서선택지①~⑤의3열표를cell주소/헤더와함께blind_sources에복원. 주Astra가대응관계와선택번호를직접확인.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "G096전체유효blind저장전모든answer_check금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:NS-hold-20260917-partial-mapping-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G096",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "ⓐ실험동물은이미반응이알려진출발대상이므로㉮아는개.ⓑ유사성은㉰비슷한외형.ⓒ반응결과는출발대상에대해이미아는추가특성인㉯사나움/물려는버릇.㉱다른개는추론의도착대상인인간에대응. 따라서기대대응은㉮-㉰-㉯이나선택번호는누락표복원전확정불가.",
  "reason": "현재선택지에는ⓑ/ⓒ열이없음",
  "next_work": "원표①~⑤3열복원후기대대응이있는선택번호를직접확인해유효blind저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "NP/NQ/NR/NTblind저장완료,NS유효blind전G096answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:OH-hold-20260917-missing-ratio-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G099",
  "reason": "보기문장이 A와B를측정하여 로열의일당량을구하면으로끊겨계산식이누락. A/B인지B/A인지공식원문없이는선택지방향을확정할수없음.",
  "selected_answer": null,
  "next_work": "Luna가로컬HWPX의OH보기equation원식과인접텍스트/문항앵커를blind_sources에복원. 답/태그/해설은열람금지.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "OH유효blind전G099전체answer_check금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:QI-hold-20260918-missing-flowchart-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G111",
  "reason": "blind source의 보기가 제목 뒤에서 끝나며 ⓐ~ⓔ 절차 도식이 없다. 선택지는 각 위치를 지시하므로 원도식 없이 번호 대응을 확정할 수 없다.",
  "selected_answer": null,
  "next_work": "Luna가 기존 canonical HWPX의 해당 문항 보기 도식을 답/태그 없이 찾아 blind_sources에 이미지 또는 충실한 노드·방향·분기 전사로 복원. Astra가 직접 판독 후 QI blind 저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "QI 유효 blind 저장 전 G111 모든 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:RX-hold-20260919-missing-choice-column-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G119",
  "selected_answer": null,
  "reason": "blind source 선택지가 A열만 남아 있고 B열이 누락되어 번호 대응을 확정할 수 없음",
  "completed_partial_reasoning_without_codes": "실제 성분 존재 집단에서 위음성이 적을수록 민감도가 높다. 실제 성분 부재 집단에서 진음성이 많을수록 특이도가 높다. 비교 시 각 집단의 검사 수 고정/비율 기준이라는 문맥을 전제로 A=위음성, B=진음성. A만 남은④⑤ 중 선택할 근거 없음.",
  "next_work": "Luna가 로컬 canonical 원문에서 RX 선택지 5행 A/B 두 열을 답·SDSS 없이 blind_sources에 복원하면 Astra가 직접 확인 후 유효 blind 저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "RX 유효 blind 저장 전 G119 전체 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:SD-hold-20260919-choice-alignment-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G121",
  "selected_answer": null,
  "reason": "blind source에서 첫 예측 행이 stem에 들어가 있고 choices는 다음 행부터 시작하며⑤는 빈 값. 원래①~⑤ 번호와 표 행의 대응을 확정할 수 없음.",
  "completed_partial_reasoning_without_codes": "본문은 서양 우주론 영향 아래 중국의 우주론 변화·회통을 소개하므로 그 예측을 예측과 다름이라고 점검한 행이 부적절하다. 다만 선택지 번호 대응이 손상되어 번호는 유보.",
  "next_work": "Luna가 답/SDSS/해설 없이 canonical 원표의 다섯 행과 원래①~⑤ 대응을 blind_sources 보강 파일로 복원.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "SD 포함 G121 전체 유효 blind 저장 전 모든 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:SH-hold-20260919-mass-symbol-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G121",
  "selected_answer": null,
  "reason": "blind source⑤는 지구 질량을 소문자m으로 쓰고 뒤의 등가 질점은 대문자M으로 씀. 원문의 대소문자 및 [A] 범위 복원 전 선지의 참거짓을 확정하기 어려움.",
  "next_work": "Luna가 답/SDSS/해설 없이 canonical 원문 SH①~⑤의 질량·거리 기호와 [A] 범위를 기계 복원. 특히⑤ 지구 질량 M/m 직접 확인용 crop 또는 XML 근거를 blind_sources에 제공.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "SH 포함 G121 전체 유효 blind 저장 전 모든 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:SH-hold-20260919-canonical-symbol-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G121",
  "selected_answer": null,
  "reason": "Luna가 복원한 canonical HWPX에도⑤의 지구 질량 소문자m/등가 질점 대문자M 불일치가 그대로 존재함. [A] 범위는 뉴턴 문단으로 확인했으나 기호 문제는 미해소.",
  "completed_partial_reasoning_without_codes": [
    "① 같은 두께·밀도의 바깥 껍질은 부피·질량이 더 크다. 각각 중심으로 환원하면 태양까지 거리는 같아서 큰 껍질의 인력이 더 크다.",
    "② 태양 중심의 가상 질점m과 지구 전체 질량의 곱, 지구 중심의 가상 질점m과 태양 전체 질량의 곱은 다르다. 태양 질량이 더 크므로 두 힘을 같다고 할 수 없다. 실제 두 천체의 상호 힘이 같다는 명제를 서로 다른 가상 질점-천체 비교에 잘못 적용한 것으로 보인다.",
    "③ 실제 지구M·달m을 각각 중심 질점으로 환원하면 중심 간 거리에서 질량 곱이 보존된다.",
    "④ 하나의 태양 부피 요소를 기준으로 지구의 각 부피 요소 인력을 합산하는 방식은 본문과 일치.",
    "⑤ 지구 질량 표기가 M이면 중심 간 거리R+h 및 질량 곱 보존으로 적절하지만, 현재 소문자m 표기는 뒤의M과 대응하지 않음. 원기호 확인 전⑤를 임의로 정상화하지 않음."
  ],
  "next_work": "공식 시험지 SH⑤·header 한정 원문 복원 후 Astra가 M/m을 직접 확인하고 유효 blind 저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "G121 모든 answer_check 금지 유지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:TH-hold-20260919-missing-beacon-diagram-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G126",
  "selected_answer": null,
  "reason": "보기는 세 원·비콘1/2/3·P/Q의 도식을 지시하지만 blind source에 실제 도식이 없고 주석만 남음. 원 반지름과 위치 관계를 읽을 수 없음.",
  "next_work": "Luna가 답·SDSS·해설 없이 canonical 원문에 포함된 TH 도식 이미지를 blind_sources로 추출하고 주 Astra가 직접 판독. 필요한 기호·원 경계를 포함한 원이미지를 제공.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "TH 포함 G126 전체 유효 blind 저장 전 모든 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:TL-hold-20260919-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G127",
  "selected_answer": null,
  "provisional_answer": 5,
  "completed_partial_reasoning_without_codes": "㉠은 기록된 사실도 허구일 수 있어 확인하려는 태도다. ⑤의 증언 변형 가능성 및 다른 자료와의 진위 검증은 이 태도를 적용한다. ①②는 비판이 아니고 ③은 항상 반대편이라는 일반화 문제, ④는 주관성만으로 사료 가치를 전면 배제하는 문제여서 진위 확인과 다르다. 다만 [A]의 실제 범위가 지문 말미 표지만으로 남아 비판 대상과의 대응 확정은 보류한다.",
  "reason": "발문이 지시하는 [A] 시작/끝 조판이 blind source에 보존되지 않음",
  "next_work": "Luna가 원문 [A] 범위를 기계 복원하면 Astra가 대상과 비판의 대응을 직접 확인해 유효 blind 저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "G127 전체 유효 blind 전 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:TX-hold-20260919-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G129",
  "selected_answer": null,
  "provisional_answer": 3,
  "reason": "[A] 표지의 시작/끝이 blind source에 보존되지 않음. 발문이 명시적으로[A]를 지시해 범위 확인 필요.",
  "completed_partial_reasoning_without_codes": "지문 말미의 보호수준-비용 관계를 기준으로 보면③은 방향 오류다. 보호를 낮추면 더 많은 사람이 접근해 접근 비용이 낮아지므로 보호 완화로 접근 비용을 높이고 싶다는 설명은 어긋난다.① 유인 비용 중시→보호 강화,② 보호 약함→창출 유인 저하,④ 소득 최저에서 벗어날 때 보호 약화 후 높은 소득에서 강화,⑤ 유인비용 감소·접근비용 증가는 문단과 부합. 다만[A] 범위 복원 전 유효 blind 완료로 세지 않음.",
  "next_work": "Luna [A] 범위 supplement를 Astra가 직접 확인 후 유효 blind 저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:UK-hold-20260919-choice-table-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G132",
  "selected_answer": null,
  "completed_partial_reasoning_without_codes": "특징점은 주위와 밝기 차이가 뚜렷하고 흔들리거나 회전해도 그 차이가 유지되어야 한다. A=클수록,B=작을수록,C=시간. 현재②는 그 조합이 보이지만③의 C열 등 다른 행이 누락되어 원표 번호 대응·유일성을 확인하지 않고 선택 확정 보류.",
  "reason": "선택표①③⑤ 등에 B/C열 누락. 단일 완전행만 보고 정답 확정하지 않음.",
  "next_work": "Luna가 원표①~⑤ A/B/C 세열 복원 후 Astra가 직접 대조하여 유효 blind 저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "UK 포함 G132전체 유효 blind 전 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:UL-hold-20260919-missing-frames-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G132",
  "selected_answer": null,
  "provisional_answer": 2,
  "completed_partial_reasoning_without_codes": "본문은 회전 보정 후 빈 공간을 자르면 프레임 크기가 작아진다고 하므로②가 유력.① 특징점은 피사체 특징이지 프레임 모서리 자체가 아님.③ 서로 다른 모서리 사이가 아닌 같은 특징점의 시간간 이동을 비교.④ 촬영 후 이미지는DIS 보정 대상.⑤ 아직 소프트웨어 보정 전인데DIS 불완전 결과라고 읽을 수 없음. 그러나㉠/㉡ 그림이 없어 실제 프레임과의 대응을 확인하기 전 유효 blind 보류.",
  "reason": "보기의 두 연속 프레임 원이미지가 blind source에 없음",
  "next_work": "Luna가 원그림·㉠㉡표지 추출 후 Astra 직접 확인",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "G132 모든 유효 blind 전 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:UP-hold-20260919-choice-alignment-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G133",
  "selected_answer": null,
  "reason": "최초 콜링우드 행이stem에 들어가고 후속행들이한칸씩밀려⑤빈값. 원번호 대응 유보.",
  "completed_partial_reasoning_without_codes": "디키 행이 부적절하다. 제도론은 예술계의 자격 수여 절차로 예술을 분류하며, 신발 원주인의 화가 신분이 물건에 특별한 가치를 준다는 논리로 그림을 예술로 평가하지 않는다. 나머지 행은 감정표현·맥락정보·형식요소·개인감상에 각각 대응한다.",
  "next_work": "Luna가 원5행과①~⑤ 번호를 복원한 뒤 Astra가 직접 선택번호확인",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "UP 포함G133유효blind전 answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:UK-hold-20260919-canonical-null-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G132",
  "selected_answer": null,
  "reason": "UK_choice_table_supplement_20260919.json의canonical원문에도①③C열·⑤B/C열이공란. 기계전사보강만으로원자료누락은해소되지않음.",
  "next_work": "공식시험지 UK 선택표①~⑤ 세열 crop 확보후주Astra직접확인. 현재②확정하지않음.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "UK유효blind전G132answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:UW-hold-20260919-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G134",
  "selected_answer": null,
  "provisional_answer": 3,
  "reason": "[A] 시작·끝이 blind 원문에서 명확하지 않아 지정 주장 범위 확인 필요.",
  "completed_partial_reasoning_without_codes": "③이 유력하다. 동일론은 물리체계에서 정신이 실현될 수 있다고 보지 기계는 정신이 없다고 단정한 뒤 수학추론을 인정하는 입장이 아니다.③은 비판 대상의 입장을 잘못 귀속한다.①이해/사용,②행동/감성,④프로그램/선택,⑤모방/실제 차이를 들어 능력의 동일성을 공격하는 나머지 비판과 다르다.",
  "next_work": "Luna[A]범위보강을직접확인후유효blind저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "UW유효blind전G134answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:VA-hold-20260919-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G135",
  "selected_answer": null,
  "provisional_answer": 4,
  "reason": "[A] 지정 범위의 시작/끝이 blind 원문에서 평탄화됨.",
  "completed_partial_reasoning_without_codes": "④가 유력. 베어내는 과정2는 바나나 자체의 과정1과 교차하지 그림자의 과정3과 교차하지 않는다. 바나나의 변화가 그림자에 반영되는 것과 그림자 자체가 베어내기 과정과 같은 시공간에서 만나는 것은 다르다. 스티로폼의 국소 일그러짐은 그림자가 지나가면 사라지고 스티로폼도 변하지 않는다.",
  "next_work": "원[A]범위보강을Astra가직접확인후유효blind저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:XI-hold-20260919-choice-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G147",
  "selected_answer": null,
  "reason": "선택표㉯/㉰열누락및[A]시작·끝평탄화. 번호확정불가.",
  "completed_partial_reasoning_without_codes": "같은배율·시간조건에서초기량이큰ⓐ는같은사이클의절대증가량이더크다. Ct는공통검출발색도에이를때이므로각각Ct에서의발색도는같고ⓐ가더일찍도달해Ct값은작다. 기대대응은㉮ⓑ보다많음/㉯ⓑ와같음/㉰ⓑ보다작음. 같은시간의발색도와각자Ct시점의발색도를혼동하지않음.",
  "next_work": "원①~⑤3열과[A]범위복원후Astra직접확인. 표적DNA증폭의본문모형외실험조건은추가하지않음.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "XI유효blind전G147answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:XS-hold-20260919-empty-choice-table-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G150",
  "selected_answer": null,
  "reason": "선택표①~⑤ⓐⓑⓒ평가값이전부공란.",
  "completed_partial_reasoning_without_codes": "ⓐ적절: (가)는묵자의음악거부와여씨춘추를대조하고,(나)는조성음악의아름다움과표현주의의탈피를대조.ⓑ적절: (나)는모차르트교향곡·달에홀린피에로라는특정작품예시, (가)는특정작품명없이선왕음악의일반적범주.ⓒ부적절: (가)는다른예술갈래와비교하지않음. 기대대응은적절/적절/부적절이나번호미확정.",
  "next_work": "Luna원표3열·번호보강후Astra직접확인.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "XS유효blind전G150answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:XZ-hold-20260919-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G151",
  "selected_answer": null,
  "provisional_answer": 5,
  "reason": "[A]지정범위시작·끝이blind원문에서평탄화됨.",
  "completed_partial_reasoning_without_codes": "ⓐ는작품이위대한이유를책에서찾으려는질문,ⓑ는책이제시한해설이지질문자체아님.ⓒ는책앞뒤내용의종합.ⓓ는자신이좋아하는일에대한자기질문,ⓔ는글쓰기가행복했던자기경험을근거로답함. 따라서⑤가유력.③은ⓐ질문과다른ⓓ의답을연결하고④는ⓑ해설을질문으로바꿈.",
  "next_work": "Luna[A]범위보강후Astra직접확인하여유효blind저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "XZ유효blind전G151answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:YC-hold-20260919-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G152",
  "selected_answer": null,
  "provisional_answer": 4,
  "reason": "[A]시작·끝이blind원문에서평탄화됨.",
  "completed_partial_reasoning_without_codes": "ⓓ는주제관련단어를중요하게여겨집중하는경우로,중요하지않은단어보다고정시간·횟수가증가하는방향이다.④의짧고적다는방향은반대.ⓐ중요단어고정,ⓑ도약중건너뛴단어미이해,ⓒ앞으로되돌아감의역방향도약,ⓔ생소단어연속의긴고정은본문설명에맞는다.",
  "next_work": "원[A]범위보강후Astra직접확인해유효blind저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "YC유효blind전G152answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:YC-hold-20260919-missing-text-anchor-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G152",
  "selected_answer": null,
  "reason": "YC_A_range_supplement_20260919.json에XML문단번호만있고해당문단의시작·끝문장전사가없어blind원문과범위대응을직접확인할수없음.",
  "next_work": "Luna가p3166첫·마지막문장을그대로추가하면Astra가blind원문과대조. 이전부분추론보존,groupanswer봉인유지.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:YF-hold-20260919-diagram-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G153",
  "selected_answer": null,
  "provisional_answer": 5,
  "reason": "도식화한것이라는발문이있지만원도식이없고[A]범위도평탄화됨.",
  "completed_partial_reasoning_without_codes": "본문상㉠어휘력높음→읽기양증가→어휘습득기회증가→다시어휘력상승,㉡은반대방향누적으로격차확대. 따라서⑤가유력하고지능차이로설명하는④는마지막의의와도충돌.①읽기양반대,②③격차해소쉬워짐은본문과반대. 도식의㉠㉡대응과범위원문확인후번호확정예정.",
  "next_work": "Luna도식및[A]시작·끝문장복원후Astra직접판독",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "YF유효blind전G153answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:YJ-hold-20260919-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G154",
  "selected_answer": null,
  "provisional_answer": 3,
  "reason": "[A]범위시작·끝평탄화로지정범위확인필요.",
  "completed_partial_reasoning_without_codes": "본문은글자를깨치기이전부터점진적발달과생활속통합지도를지지,보기는성숙및기초글자기능이후발달·듣기말하기읽기쓰기순차지도를지지.③의발달시작시점차이가유력.①②는서로역할교환,④⑤는보기의순차·성숙조건을양쪽공통으로옮김.",
  "next_work": "[A]첫·끝문장보강후Astra직접대조하여유효blind저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:YL-hold-20260919-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G155",
  "selected_answer": null,
  "provisional_answer": 5,
  "reason": "발문이지시하는[A]첫·끝범위가blind원문에서평탄화됨.",
  "completed_partial_reasoning_without_codes": "㉮는이미과제를받아독서를시작하게된사건이므로때문에동기.㉯철학지식과㉰뿌듯함은다읽고얻을것으로기대하는결과라위하여동기.⑤가유력. 기대결과를이미경험한계기로바꿀수없음.",
  "next_work": "[A]첫·끝문장보강확인후유효blind저장",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:YM-hold-20260919-missing-diagram-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G155",
  "selected_answer": null,
  "reason": "보기제목뒤에내용이없어㉠㉡㉢라벨및화살표를확인할수없음.",
  "completed_partial_reasoning_without_codes": "본문은성공적독서경험이새독서의계기이면서다시기대하는목적이되어경험반복을이끈다고설명한다. 이설명만으로도식의기호를임의배정하지않는다.",
  "next_work": "Luna원도식추출후Astra가세라벨·화살표직접판독하여선지판정",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "YL/YM포함G155전체유효blind전answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:YO-hold-20260919-AB-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G156",
  "selected_answer": null,
  "provisional_answer": 5,
  "reason": "[A]/[B]각범위가blind원문에서문단뒤로평탄화되어시작·끝확인필요.",
  "completed_partial_reasoning_without_codes": "⑤가유력. 데이터이동은무상전송이며비용절감효익은전송받는기업에대해제시된다. 전송하는㉯가이동대가로경제적이득을얻는다는연결은본문근거가없다.①받는기업생성비절감,②지정된신규기업의거래비절감,③비공유에따른자체생성비·진입곤란,④기존집중과공유위축은본문각설명과부합.",
  "next_work": "Luna[A]/[B]첫끝문장보강후Astra직접확인. 전송자의가능한모든간접경제효과를일반적으로부정하지않음.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:YQ-hold-20260919-empty-choice-table-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G156",
  "selected_answer": null,
  "reason": "ⓐ/ⓑ어휘선택표5행모두빈값.",
  "completed_partial_reasoning_without_codes": "ⓐ는데이터생성·유통이더수월해진다는의미,ⓑ는은행간약정을근거로부분시행했다는의미다. 구체후보단어와선택번호가없어적합성확정불가.",
  "next_work": "원①~⑤두열어휘복원후Astra가문맥에대입하여직접판정",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "YO/YQ포함G156전체유효blind전answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:YM-hold-20260919-source-anchor-review-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G155",
  "selected_answer": null,
  "reason": "기존YM_diagram_supplement는지문[A]표p3069와첫문항p3077을anchor로기록하여실제YM보기위치의도식부재를입증하는지불명확. canonical전체에도식이없다는결론으로승격하지않음.",
  "next_work": "fresh Luna가정확한YM발문뒤원도식위치를검증하고YM_verified_diagram_supplement_20260919.json으로원자료만제공. Astra직접판독전선택기호배정금지.",
  "source_qualification": "기존supplement의hash표기도실제동일파일검증값과불일치하여metadata신뢰성검토필요. 최초source보고삭제·raw덮어쓰기하지않음.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:YY-hold-20260919-missing-graph-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G158",
  "selected_answer": null,
  "reason": "보기의흡착세기/촉매활성그래프와ⓐ~ⓓ위치가없어선지비교대상관계확정불가.",
  "completed_partial_reasoning_without_codes": "본문은흡착이너무약해도너무강해도활성이낮다는비단조관계를제시한다. 금속의순서·높이를모르므로어느기호가강한흡착/높은활성인지추정하지않는다.",
  "next_work": "정확한YY원그래프축·기호복원후Astra가직접판독하여방향·최댓값비교",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "YY유효blind전G158answer공개금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G160-hold-20260920-provenance-collision-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G160",
  "case_ids": [
    "ZD",
    "ZE",
    "ZF"
  ],
  "reason": "sealed provenance에서 G160 S180~182 동형이의어와 G162 S189~191 여러 글 읽기에 동일한 2025학년도6월 Q1~3 키가 붙어 있다. 서로 다른 지문이 동일 시험·번호에 귀속되는 충돌을 직접 확인.",
  "completed_checks": [
    "G160 최초 선택④⑤③과 sealed⑤②② 불일치 보존.",
    "G162 최초 선택⑤②②와 sealed⑤②② 일치.",
    "Luna의 첫 supplement는 실제2025년6월 답표 헤더와⑤②②만 확인했으며 G160 지문과 공식 문제지의 일치를 입증하지 않았다."
  ],
  "not_accepted_claim": "supplement의 status mechanical_provenance_and_answer_table_link_verified와 번호 밀림 없음 표현은 G160 정본 연결 확인으로 승인하지 않음. 이미 잘못 붙었을 수 있는 provenance label을 다시 확인한 것만으로는 충분하지 않다.",
  "next_work": "동형이의어 원지문의 실제 시험·연도와 Q1~3 문항을 확인한 뒤 그 시험의 정답표를 대조. original blind/sealed/canonical 값 모두 덮어쓰지 않고 보강 기록에 분리.",
  "exposure": {
    "official_answer_values_seen": "잘못 연결 가능성이 있는2025년6월⑤②②",
    "sdss_seen": false,
    "independent_code_started": false
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:EXPOSURE-hold-20260920-official-pdf-unscoped-output-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "G160 공식 source 직접 확인을 위한 web open/search 출력이 지정Q1~3 외 문제지Q4~13 텍스트와2026학년도6월 국어 전체 답표까지 반환함.",
  "exposed_scope": "2026학년도6월 Q4~13 문제·일부선지 텍스트 및 공통/선택 정답표 전체. 다른 group 기존 판단을 변경하지 않음.",
  "required_followup": "동일 시험 미완료·신규 case는 이 세션의 사전답 노출 여부를 보존하고 strict blind 성과에서 제외. 이미 group blind를 완료한 사례의 최초raw는 그대로 보존. Luna가 새 준비 case의 provenance metadata만 대조하여 노출 연결을 기록할 수 있음.",
  "exposure_provenance": "web open EBSI 공식 문제지 및 KICE답표 검색의 범위 밖 자동 출력",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AAD-hold-20260920-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G167",
  "selected_answer": null,
  "provisional_answer": 5,
  "reason": "blind source의[A]가 문단뒤 고립 표지로 평탄화되어 지시 범위 첫·끝이 확인되지 않음.",
  "completed_partial_reasoning_without_codes": "전체 본문3문단에는 학습 정보가 정확해도 추출·조합 과정에서 왜곡될 수 있다는 내용이 있어⑤가 유력. [A]가 그문단을 포함하는지 원자료 범위 확인 필요.",
  "next_work": "canonical [A] 시작·끝 문장만 기계 복원 후 Astra 직접확인하여 유효풀이 저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "AAD 포함G167 전체blind 전 answer 공개 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AAG-hold-20260920-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G168",
  "selected_answer": null,
  "provisional_answer": 3,
  "strict_blind_eligible": false,
  "reason": "[A]의 정확한 첫·끝 문장이 blind source 평탄화로 미확인. 이미 정답·공식 텍스트 노출된 사례지만 범위 근거는 별도 확인 필요.",
  "completed_partial_reasoning_without_codes": "과도 법개입→자율 기능 훼손→법적 해결 요구 증가→더 큰 개입의 순환으로 이전 비법적 과제까지 법 과제로 이동하는③이 유력.",
  "next_work": "[A] 범위 텍스트 anchor를 원자료에서 복원 후 직접 대조.",
  "exposure": {
    "official_answer_seen": true,
    "official_source_seen": true,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "G168 전체 코드없는 재구성 저장 전 신규 answer_check와 independent_code 시작 안 함",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:ACU-hold-20260920-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G181",
  "selected_answer": null,
  "provisional_answer": 5,
  "reason": "blind source의[A]가 전체 지문 뒤 고립 표지로 평탄화되어 시작·끝 범위가 확인되지 않음.",
  "completed_partial_reasoning_without_codes": "(나) 마지막 문단의 수빈은 현실 위기에 대응하여 현실 너머 이상세계를 탐색하는 역할을 강조한다. 보기 입장은 유토피아 붕괴가 현실 너머 해답의 부재를 보여준다고 주장하므로⑤가 유력하다. 실제[A]의 범위와 일치하는지 확인 필요.",
  "next_work": "Luna가 공식/canonical 원자료에서[A] 첫·끝 문장과 범위 provenance만 blind supplement로 기계 복원; Astra 직접 대조 후 유효 blind 저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "ACU 포함 G181 전체 유효 blind 전 answer_check 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G192-hold-20260920-historical-exposure-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "case_ids": [
    "AEX",
    "AEY",
    "AEZ",
    "AFA"
  ],
  "reason": "blind source의 익명화로 새 풀이 단계에는 시험 식별을 하지 않았으나 SDSS 공개 단계 sealed provenance가2026학년도6월Q10~13임을 확인했다. 저장소의 기존 EXPOSURE-hold-20260920-official-pdf-unscoped-output-01은 해당 범위 원문 및 전체 답표의 과거 노출을 명시한다.",
  "strict_blind_eligible": false,
  "exposure": {
    "current_session_answer_before_blind": false,
    "historical_official_source_and_answer_exposure": true,
    "sdss_before_independent_code": false
  },
  "original_blind_preserved": true,
  "required_followup": "G192 네 문항은 실제 풀이와 모든 최초 raw를 보존하되 strict blind 정확도 집계에서 제외. manifest exposure unknown을 historical exposure로 기계 보강. 기존 준비metadata unknown과 이번 발견을 모두 보존.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:ACU-hold-20260920-reconstructed-range-not-verified-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G181",
  "case_ids": [
    "ACU"
  ],
  "reason": "ACU_A_range_supplement_20260920.png를 직접 보니 원자료 렌더 crop이 아니라 첫·끝 문장을 새로 배치한 재구성 이미지다. supplement scope_rule은 표지 직후 문단 전체라고 선언하지만 원문 대괄호의 실제 시작·끝이나 표 구조 전체에 의한 범위 근거가 제시되지 않았다.",
  "not_accepted_claim": "blind_range_anchor_restored_mechanically 상태를 유효 범위 복원 완료로 승인하지 않는다. 첫끝 anchor 재출력은 범위의 독립 근거가 아니다.",
  "completed_checks": [
    "JSON의 marker_cell은row1 col0 colspan2에[A]가 있다고만 기록. 표 전체 텍스트 셀과 경계가 없음.",
    "PNG에 원래 대괄호 형태와 마지막 경계가 보이지 않으며 텍스트 재조판이라는kind 자체가 이를 명시."
  ],
  "next_work": "실제 공식 PDF 또는 원 HWPX 렌더에서 대괄호 시작·끝이 함께 보이는 crop을 제공. 원자료로부터 범위가 명백한 전체 XML table subtree를 제공하는 경우 Astra가 셀/경계 구조 직접 검토. 처음 supplement와 raw는 보존하고 verified 후속 파일 분리.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "G181 전체answer/SDSS 계속봉인",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:ACU-hold-20260920-floating-bracket-needs-render-03 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G181",
  "case_ids": [
    "ACU"
  ],
  "reason": "verified_table 직접 판독 결과3행2열 표는[A]중앙 표지와 위아래 대괄호 선만 가진 부유 객체다. 본문 텍스트는 표 셀 안에 없어서 이 표 자체로 어느 문장의 시작·끝과 일치하는지 확정할 수 없다.",
  "source_findings": [
    "table textWrap SQUARE, treatAsChar0, vertRelTo PARA, height13109와 경계선 정보는 있으나 앵커 본문 문단의 line segment 및 페이지 좌표 매핑이 없다.",
    "5개 셀은빈값 또는[A]뿐이다. 전체 문단이라는 최초scope_rule을지지하는구조가아니다."
  ],
  "next_work": "실제 공식 문제지 해당[A]와 인접 본문을 한 화면에 담은 crop을 blind_sources에 저장. PDF 또는 원 HWPX의 실제 렌더만 허용; 원래 문제·지문 밖 정답과 타 문항은 부모에게 노출 금지.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "G181 answer/SDSS 봉인유지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G193-hold-20260920-linkage-absence-disclosure-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "case_ids": [
    "AFB",
    "AFC",
    "AFD",
    "AFE"
  ],
  "reason": "기계준비Luna최종보고가SDSS linkage0건이라고blind/independent전공개했다. 실제태그·답·해설은부모에게공개되지않았으나사이트연결부재정보의사전노출은기록한다.",
  "exposure": {
    "official_answer_seen": false,
    "actual_sdss_tags_seen": false,
    "sdss_linkage_absence_disclosed_before_blind": true,
    "prior_project_judgment_seen": false
  },
  "strict_blind_qualification": "SDSS대조상태사전노출이있어완전무오염성과로승격하지않음. 직접풀이와독립코드판정은실제태그·답을보지않고진행가능.",
  "next_work": "manifest및blind_source만으로groupblind진행. groupbarrier계속적용. 향후기계보고는태그부재도공개하지않도록통지완료.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFJ-hold-20260920-source-markers-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "selected_answer": null,
  "provisional_answer": 2,
  "reason": "[A]표지가평탄화되어범위시작·끝이확인되지않고보기표의원행열도직접확인전.",
  "completed_partial_reasoning_without_codes": "P-Q=550/440=5/4, Q-R=660/550=6/5이므로전자1.25가후자1.2보다커②의더좁다는진술이틀린것으로예상. [A]가관련정의를포함하는지확인필요.",
  "next_work": "공식PDF의[A]대괄호와보기P/Q/R/S표crop직접판독후유효blind저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인불가",
    "source_boundary_residue": "AFK말미##2018학년도만노출. 해당group식별미확정."
  },
  "group_barrier": "AFJ/AFK포함6문항의유효blindraw전answer/SDSS공개금지.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFK-hold-20260920-source-markers-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "selected_answer": null,
  "provisional_answer": 4,
  "reason": "선택지별비교대상용언의밑줄표시가JSON에보존되어있지않음.",
  "completed_partial_reasoning_without_codes": "버리다·주다·두다·보다가앞용언에의미를더하는용법인반면구해오다의오다가실제이동이면자립용언으로④가유력. 정확한표시대상확인전확정안함.",
  "next_work": "공식PDF의AFK다섯선지밑줄을그대로보이는crop을확인하고문맥기능비교. 다음시험제목은crop에서제외.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인불가",
    "source_boundary_residue": "AFK말미##2018학년도만노출. 해당group식별미확정."
  },
  "group_barrier": "AFJ/AFK포함6문항의유효blindraw전answer/SDSS공개금지.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGS-hold-20260920-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "selected_answer": null,
  "provisional_answer": 3,
  "reason": "[A]표지가본문뒤고립되어정확시작·끝이평탄화source에서확인되지않음.",
  "completed_partial_reasoning_without_codes": "전체본문은가상환경변화에따라트레드밀기울기가변경될수있다고하여③이유력.관성센서는속도변화율·회전속도,압력센서는뛰는힘,컴퓨터는바닥제어역할. [A]실제범위확인필요.",
  "next_work": "공식PDF[A]대괄호와첫끝문장을함께보이는crop직접판독.",
  "group_barrier": "AGR/AGT/AGU저장,AGS유효blind전G201answer/SDSS계속봉인.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFJ-hold-20260920-table-crop-clipped-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "selected_answer": null,
  "provisional_answer": 2,
  "reason": "공식[A]crop으로음정·협화도문단범위는직접확인했으나별도PQRS표crop이숫자행하단에서잘림.원래숫자·행열완전검증으로승격하지않음.",
  "next_work": "표숫자행과하단선전체가보이는v2crop직접확인후AFJ유효blind저장. 기존crop보존.",
  "group_barrier": "AFJ유효blind전G194answer/SDSS계속봉인.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFO-hold-20260920-missing-graphs-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "selected_answer": null,
  "reason": "blind source에a/b/c각그래프의모양·축이없고선지표만있다.본문[가]범위도고립표지여서실제범위확인이필요.기계READY의시각자료완전성은승인하지않음.",
  "completed_partial_reasoning_without_codes": "㉠실질통화량은단기상승뒤원래수준,㉡금리는단기하락뒤반등,㉢환율은단기급등뒤일부하락하되최초보다높은장기균형으로수렴. 어느그래프가a/b/c인지는원그림없이정할수없음.",
  "next_work": "공식PDF의세그래프·선지매칭표및[가]범위원crop복원후직접판독.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "AFO유효blind전G195answer/SDSS봉인유지.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFO-hold-20260920-scope-crop-clipped-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "selected_answer": null,
  "provisional_answer": 4,
  "completed_partial_reasoning_without_codes": "실제a곡선은하락뒤최초수준복귀,b는급상승뒤최초보다높은수준수렴,c는상승뒤최초수준복귀. 따라서㉠실질통화량c/㉡금리a/㉢환율b대응이며JSON선지④가유력.",
  "reason": "그래프직접확인은완료했으나[가]crop이문단중간부터시작해범위상단과㉠~㉢표지가없다. 범위전체검증으로승격하지않음.",
  "next_work": "본문[가]상하단전체및㉠~㉢,보기선지번호매칭표의공식v2crop직접확인후유효blind저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "AFO유효blind전G195answer/SDSS봉인유지.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFY-hold-20260920-A-range-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "selected_answer": null,
  "provisional_answer": 4,
  "reason": "[A]가flat본문뒤고립표지여서정확범위상하단확인전.",
  "completed_partial_reasoning_without_codes": "본문의갑은채권투자자·보장매입자,을은기초채권발행자,병은신용위험을떠안는보장매도자이므로④가유력. 표시범위와㉠~㉢원문위치확인필요.",
  "next_work": "공식PDF[A]실제대괄호와㉠~㉢전체crop확인후유효blind저장.",
  "group_barrier": "AFY유효blind전G197answer/SDSS봉인.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGD-hold-20260920-missing-A-marker-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "selected_answer": null,
  "provisional_answer": 2,
  "reason": "발문은[A]의물음을요구하지만blind본문에[A]표지·범위가누락됨. 첫문단일것이라고추정하여범위검증완료처리하지않음.",
  "completed_partial_reasoning_without_codes": "방충망수선은임의규정이므로계약에말이없으면법의임대인의무,계약에서세입자부담으로달리정하면그계약적용. 어느쪽도달리정하거나침묵했다는이유로불이익없어ㄱ·ㄷ②가유력.",
  "next_work": "공식문제지의[A]첫끝·대괄호직접판독후유효blind저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "AGD포함G198전체유효blind전answer/SDSS봉인.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGW-hold-20260920-choice-shift-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "selected_answer": null,
  "provisional_answer": 2,
  "reason": "사용설명서첫항목이stem에있고choices는후속4항목+빈값이어서5선지번호대응소실.",
  "completed_partial_reasoning_without_codes": "본문은과충전양·과방전과수명관계를말하지만허용충전전류초과와수명감소의직접근거는없다. 해당항목이원자료②일가능성있으나번호추정으로확정하지않음.",
  "next_work": "공식사용설명서5유의사항과번호의원crop직접확인후선택답저장.",
  "group_barrier": "G202전체유효blind전answer/SDSS봉인.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIC-hold-20260921-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G211",
  "selected_answer": null,
  "provisional_answer": 3,
  "reason": "blind전사문 [A]/[B]가각각발화뒤에단독배치되어공식대괄호범위의시작끝을직접확인하지못함.",
  "completed_partial_reasoning_without_codes": "제원들은태보의죽음무릅쓴충을칭송하고태보는뜻을정해변치않고죽어서도간하겠다고다짐하므로③유력.정확범위확인전유효blind확정안함.",
  "next_work": "공식문제지 또는원HWPX실제렌더에서[A][B]첫끝과괄호가보이는blind-only crop확인",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "AIC유효blind전G211전체answer/SDSS봉인",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIN-hold-20260921-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G214",
  "selected_answer": null,
  "provisional_answer": 2,
  "reason": "[A]~[F]표지가행사이에평탄화되어각대괄호의정확시작끝미확인.",
  "completed_partial_reasoning_without_codes": "바람흔들림뒤이윽고홀씨일어나버섯피어남의순차관계가②를지지할듯함.다른선지는순환·대립·인과·동질로관계를바꾸지만원범위검증전확정안함.",
  "next_work": "공식문제PDF또는원HWPX렌더에서[A]~[F]모든괄호와시구범위를blindcrop으로확인",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "AIN유효blind전G214전체answer/SDSS봉인",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIR-hold-20260921-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "selected_answer": null,
  "provisional_answer": 3,
  "reason": "[A][B]범위시작끝미표시이며[C]표지가(나)후반아닌(가)초반에있어범위전사손상가능성.",
  "completed_partial_reasoning_without_codes": "금단의담은머뭇거리게하지만넘기의신명을가능하게하는도전·도반.③이유력.목련과감나무는일반화사례이지뿌리잎의상호협력관계아님.정확범위전확정안함.",
  "next_work": "공식PDF(나)전체시와[A][B][C]대괄호의실제시작끝crop직접확인.특히[C]위치복원.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "AIR유효blind전G215전체answer/SDSS봉인",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIW-hold-20260921-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G216",
  "selected_answer": null,
  "provisional_answer": 4,
  "reason": "[A]~[C]표지가각발화뒤에만있어공식대괄호범위시작끝미확인.",
  "completed_partial_reasoning_without_codes": "갑순이할머니는상대가고의감금이라비난함을알고모르고잠갔다고의도성을부정한다.④비난파악못함이틀려유력.범위확인전유효blind보류.",
  "next_work": "공식PDF[A][B][C]발화전체대괄호시작끝crop확인",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false
  },
  "group_barrier": "G216전체answer/SDSS봉인",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:ARQ-hold-20260927-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G293",
  "selected_answer": null,
  "provisional_answer": 2,
  "reason": "blind-only source에 [시각 자료 1] 자리표시자만 있고 도식 자체가 제시되지 않았다. metadata의 visual_placeholder=false와 실제 source 상태가 다르다.",
  "completed_partial_reasoning_without_codes": "보기의 절연체 변위를 용수철 늘어남에 대응하는 설명은 연속 매질의 역학적 모형을 시사해②가 유력하다. 원 도식 확인 전 시각자료 완전성 및 유효 blind를 확정하지 않는다.",
  "next_work": "공식 원문의 ARQ 보기 도식과 해당 문항만 포함하는 blind-only crop을 확보해 직접 확인한 뒤 유효 blind raw 저장.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "blind_passage_and_choices_seen": true,
    "diagram_seen": false
  },
  "group_barrier": "ARO/ARP blind 저장됨. ARQ 유효 blind 전 G293 전체 answer_check/SDSS 계속 봉인.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AXB-hold-20260928-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G340",
  "incomplete_stage": "blind",
  "reason": "blind-only에선택에필수인<가정>내용누락.도식은층구조,MD는보기ㄱㄴㄷ만존재.",
  "next_work": "Luna가공식문제지에서<가정>만복원→Astra직접풀이→group전체blind장벽확인후answer_check",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "read": [
      "AXB.json",
      "G340_visual01.tif",
      "G340_visual02.md"
    ]
  },
  "group_stage_barrier": "AWZ/AXA blind저장완료,AXB미완료이므로G340답·SDSS봉인유지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AXH-hold-20260928-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "incomplete_stage": "blind",
  "selected_answer": null,
  "reason": "선지④ 주어인 그리스문자와 선지⑤ 비교 기준 그리스문자가 blind 전사에서 소실됐다. 그림의 α/β는 확인했으나 선지의 어느 문자인지 원문 확인 필요.",
  "completed_partial_reasoning_without_codes": "① E에서 오른쪽 이동은 미미한 감소,② F에서 오른쪽은 급감,③ G에서 왼쪽은 급증 가능. α는 저→고 전이 경계,β는 고→저 전이 경계다.",
  "next_work": "공식 문제지 AXH 선지④⑤의 α/β만 blind-only 원문으로 복원 후 Astra 직접 확인.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "AXH 유효 blind 저장 전 G342 전체 정답·SDSS 봉인",
  "passage_group": "G342",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G342-hold-20260928-helper-exposure-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G342",
  "reason": "원문 복원 Luna가 prepared_backlog 전체 제한검색 과정에서 sealed/answer_sdss.jsonl AXH 행의 정답·사이트코드에 우발 노출됐다고 보고. Astra에 실제 답·코드 내용은 전달되지 않았다.",
  "exposure": {
    "helper_official_answer_seen": true,
    "helper_sdss_seen": true,
    "astra_official_answer_seen": false,
    "astra_sdss_seen": false
  },
  "strict_blind_eligible": false,
  "scope": "G342를 엄격 무오염 성과로 집계하지 않음. AXF/AXG/AXI 최초 raw 및 AXH 원 hold 불변 보존.",
  "next_work": "정답·코드 내용 전달 없이 공식 문제지 선지④⑤만 복원. Astra의 직접풀이 계속 가능하나 무오염 승격 금지.",
  "quota_status": "unavailable"
}
```
<!-- luna-sync:AUDIT99-20260928 -->
## 현재 진행 상태 — AUDIT99 반영·depth backfill 선행·G347 잠금

- `AUDIT99-manual_parity_audit-20260928-01` raw 1건을 payload 의미 변경 없이 독립연구 진행 기록과 processed 원장에 반영했다. AXH의 절차상 제한·strict 제외와 AXO/AXQ/AXU의 depth 보충 지정, 사이트 범위 미확정을 그대로 보존한다.
- Queue=processed=4,977 unique, pending raw=0이다. duplicate/orphan 없음.
- `meta_state.py` 동기화 결과: META99 이후 완료 group/question 0/0, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=["AXO", "AXQ", "AXU"]`, `semantic_state_review=[]`이다.
- 다음 허용 작업은 Astra의 AXO·AXQ·AXU `depth_backfill` raw 작성 및 Luna sync다. 이를 완료하기 전 G347 신규 semantic stage는 잠근다. G024 HOLD·이전 실패·사전노출 제한은 유지한다.


<!-- luna-raw:AXW-hold-20260928-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G347",
  "incomplete_stage": "blind",
  "hold_reason": "지문1문단과 발문의 동일 [시각 자료1] 강조구가 blind packet에서 누락. 제공된 보충1은 보기ㄱㄴㄷ이며 누락 구절 자체를 복원하지 않음.",
  "next_work": "공식 문제지에서 강조구와 발문 표적을 기계적으로 확인하여 blind_sources에 출처 달린 보충파일로 저장한 뒤 Astra가 직접 읽고 blind 판단.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "AXV·AXX blind 저장; AXW 미완료이므로 G347 정답/SDSS 공개 금지",
  "tentative_answer_not_finalized": true,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AYE-hold-20260928-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G350",
  "incomplete_stage": "blind",
  "hold_reason": "발문 및1문단말미 강조구가 [시각자료1]로 치환됐고 제공표는 세율상황표라 강조구 복원자료 아님. 문맥 추정만으로 표적을 확정하지 않음.",
  "next_work": "Luna 공식문제지 강조구·발문만 복원한 blind_sources 자료를 읽고 최초 blind 완료.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "AYF·AYG blind 저장,AYE 미완료;group 정답/SDSS 금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AZO-hold-20260928-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G361",
  "incomplete_stage": "blind",
  "hold_reason": "공통지문끝과AZO발문의강조구가[시각자료1]로치환돼표적누락. 제공보충은시작품이며표적복원아님.",
  "next_work": "Luna공식문제지강조구복원본을blind_sources에서직접읽은뒤blind판정",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "AZM/AZN/AZP blind저장,AZO미완료;G361답/SDSS금지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:SESSION20260928-hold-20260928-context-handoff-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "hold_reason": "이번 Astra 실행의 응답·컨텍스트 예산 한계에 따른 안전한 세션 인계. quota threshold나 runtime emergency 관측으로 기록하지 않는다.",
  "last_completed_group": "G364",
  "last_completed_semantic_record": "BACKFILL105-depth_backfill-20260928-01",
  "next_group": "G365",
  "next_stage": "새 세션에서 AGENTS/CURRENT/ASTRA_START→meta_state/quota→pending확인 후 G365 group blind",
  "incomplete_semantic_stage": null,
  "next_group_exposure": {
    "blind_source_seen": false,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "runtime_emergency_observed": false,
  "quota_status": "unavailable",
  "research_complete": false,
  "completed_this_session_groups": [
    "G347",
    "G348",
    "G349",
    "G350",
    "G351",
    "G352",
    "G353",
    "G354",
    "G355",
    "G356",
    "G357",
    "G358",
    "G359",
    "G360",
    "G361",
    "G362",
    "G363",
    "G364"
  ],
  "completed_this_session_cases": 56,
  "preserve": [
    "AYP/AZI최초오답란오류와사후보충의비소급",
    "strict blind미확정·기존AXH제한·AVE/ATK실패",
    "AXW/AYE/AZO원hold와공식복원후별도blind",
    "G348안테나분수누락",
    "사이트범위미확정·G354식별자오기의META102정정"
  ],
  "luna_next": "신규hold포함pending모두sync,checkpoint/CURRENT/handoff갱신,새원문읽기없이재개상태검증"
}
```


<!-- luna-raw:BAI-hold-20261001-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "incomplete_stage": "blind",
  "selected_answer": null,
  "provisional_answer": 2,
  "hold_reason": "선지④ 절대온도 수치와 본문 수치·기호가 전사에서 누락되어 선택지 전체를 검증하지 못함.",
  "completed_partial_reasoning_without_codes": "② 선택적 광자 흡수는 본문에 명시.①은 감지 진동수를 원자 속도로,③은 냉각 대상을 광자로 바꾼다.⑤는 개별 제어 불가와 충돌.④의 정확 수치 확인 전 유효 blind 확정 보류.",
  "next_work": "공식 문제 원문에서 본문 수식 및 BAI④ 절대온도 수치를 blind-only로 복원",
  "passage_group": "G368",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "blind_text_and_five_supplements_seen": true
  },
  "group_barrier": "G368 전체 유효 blind 저장 전 answer/SDSS 봉인 유지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:BAJ-hold-20261001-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "incomplete_stage": "blind",
  "selected_answer": null,
  "hold_reason": "①②③④⑤에 포함된 에너지·준위 기호들이 전사에서 소실. 도식 E1/E2/ΔE는 읽었으나 각 선지의 논항 배치를 추정으로 채울 수 없음.",
  "completed_partial_reasoning_without_codes": "접근 원자는 광원 진동수를 높게 감지하므로 공명 진동수 광원 자체는 흡수 조건을 넘긴다. 흡수와 방출의 에너지는 관측 조건을 구분해야 함. 선지 원기호 확인 전 답 미정.",
  "next_work": "공식 BAJ 다섯 선지와 그림 호칭 및 본문 에너지 수식을 원기호 보존해 blind-only 복원",
  "passage_group": "G368",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "blind_text_and_five_supplements_seen": true
  },
  "group_barrier": "G368 전체 유효 blind 저장 전 answer/SDSS 봉인 유지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:BAK-hold-20261001-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "incomplete_stage": "blind",
  "selected_answer": null,
  "hold_reason": "보기 기준 속도와 ㄱㄴㄷ의 속도 계수가 모두 누락. 제공된 MD에서도 복원되지 않음.",
  "completed_partial_reasoning_without_codes": "498Hz에 접근할 때 감지 주파수가 500Hz가 되는 기준 속도는 존재. 방향과 켜진 스피커를 각각 보존해야 하나 계수 부재로 ㄱㄴㄷ 공명 여부 판단 불가.",
  "next_work": "공식 BAK 보기 전체와 기준 및 ㄱㄴㄷ 속도 기호·계수를 blind-only 복원",
  "passage_group": "G368",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "blind_text_and_five_supplements_seen": true
  },
  "group_barrier": "G368 전체 유효 blind 저장 전 answer/SDSS 봉인 유지",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G368-hold-20261001-crop-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G368",
  "incomplete_stage": "blind",
  "hold_reason": "G368_restore_2016_odd_p13_left/right 및 p14_left/right를 직접 보았으나 crop 좌표가 열 전체를 담지 않아 우측 선지와 하단 BAK 조건이 잘림. 첫 복원 시도만으로 유효 blind 확정 불가.",
  "next_work": "동일 공식 HWP 렌더 page013/page014를 blind_sources에 전체 복사한 후 직접 확인",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "partial_official_crops_seen": true
  },
  "group_barrier": "BAI/BAJ/BAK 유효 blind 미완료; 답/SDSS 봉인",
  "original_holds_preserved": true
}
```


<!-- luna-raw:G370-hold-20261001-source-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G370",
  "case_ids": [
    "BAP",
    "BAQ",
    "BAR",
    "BAS"
  ],
  "incomplete_stage": "blind",
  "selected_answer": null,
  "hold_reason": "공통 지문이 본 지문은 온라인 게시가 불가능하다는 안내와 작품 출처만으로 대체되어 있다. 실제 소설 본문 및[A][B],㉠~㉤,ⓐⓑ의 위치·문맥 모두 부재. 제공visual01은 감상 보기뿐이다. manifest source_quality complete 표시는 실제 상태와 맞지 않는다.",
  "next_work": "Luna가 공식 질문 원본의 실제 본문 존재 여부를 확인하여 지문과 모든 범위 표지가 보이는 question-only 자료를 blind_sources로 복원. 공식본도 안내문뿐이면 source_unavailable로 유지하고 답/태그를 열지 않는다.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "question_choices_seen": true,
    "passage_seen": false,
    "appreciation_view_seen": true,
    "historical_exposure": "확인 불가"
  },
  "group_barrier": "G370 유효 blind 0/4. 전체 답/SDSS 봉인.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:G370-hold-20261001-source-unavailable-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G370",
  "case_ids": [
    "BAP",
    "BAQ",
    "BAR",
    "BAS"
  ],
  "incomplete_stage": "blind",
  "hold_reason": "Luna가2017 LEET 홀수/짝수 공식 질문 HWP를 기계 확인한 결과[7~10] 실제 소설 본문은 없고 온라인 게시 불가 안내뿐임. source_unavailable 유지.",
  "source_verification_role": "공식 질문 파일의 본문 부재는 Luna 기계 보고이며 Astra의 직접 소설 읽기나 코드 판단 아님.",
  "source_paths": [
    "자료/LEET_언어이해/원본/2017/2017_question_odd_2017학년도_법학적성시험_언어이해(홀수형)_수정.hwp"
  ],
  "next_work": "G370은 원문 확보 전 blind 보류·답/SDSS 봉인. 독립된 다음 prepared G371로 진행. G370을 완료/제외 또는 성공 사례로 계수하지 않음.",
  "resume_condition": "공식 시험의 실제 본문·범위 표지를 검증할 수 있는 question-only 자료 확보",
  "next_group": "G371",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "passage_seen": false,
    "choices_and_appreciation_view_seen": true
  },
  "original_hold_preserved": true,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:BBF-hold-20261001-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "incomplete_stage": "blind",
  "selected_answer": null,
  "provisional_answer": 5,
  "hold_reason": "상자·화살표 선택지를 텍스트로 옮긴 packet만 읽음.공식 도식에서 병렬 실험과 후속 연결이 전사와 일치하는지 직접 확인 전 유효 blind 보류.",
  "completed_partial_reasoning_without_codes": "유리공명기와합성기실험→복합음의단음조합입증→현공명영감→코르티착안→공명이론.옴의귀의분리감각주장전체를먼저증명했다는ㄱ은실험결론보다강함.",
  "next_work": "공식도식 question-only page를blind_sources에서직접확인",
  "group_barrier": "G375전체blind전답/SDSS봉인",
  "passage_group": "G375",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BBF.json",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:SESSION20261001-hold-G366-G375-context-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "hold_reason": "이번 연구 응답의 처리·컨텍스트 예산 한계에 따른 안전한 세션 인계. frontier 완료나 준비 사례 소진,quota 임계값을 종료 이유로 삼지 않는다.",
  "last_completed_group": "G375",
  "last_completed_semantic_record": "G375-induction-20261001-01",
  "completed_this_session_groups": [
    "G366",
    "G367",
    "G368",
    "G369",
    "G371",
    "G372",
    "G373",
    "G374",
    "G375"
  ],
  "completed_this_session_cases": 28,
  "next_group": "G376",
  "next_stage": "새 Astra 세션에서 AGENTS/CURRENT/ASTRA_START→meta_state/quota→pending확인 뒤 G376 group blind",
  "incomplete_semantic_stage": null,
  "persistent_source_holds": [
    {
      "group": "G370",
      "cases": [
        "BAP",
        "BAQ",
        "BAR",
        "BAS"
      ],
      "stage": "blind",
      "reason": "공식질문원본에도본문부재",
      "answers_sdss_sealed": true
    }
  ],
  "next_group_exposure": {
    "blind_source_seen": false,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "runtime_emergency_observed": false,
  "quota_status": "unavailable",
  "research_complete": false,
  "meta_audit_work": [
    "META106",
    "META107",
    "META108",
    "AUDIT108",
    "BACKFILL108 BAT/BAX/BBC"
  ],
  "preserve": [
    "BAX최초44및사후17/25후보·유일44철회비소급",
    "BAT⑤범위·BBC③강도유보",
    "G368기호복원·원hold4와불완전crop",
    "G375원도식합류/기존순차전사오류·BBFhold와유효blind분리",
    "G370source_unavailable4사례미완료",
    "과거노출미확정·원정답표독립대조미완료·기존품질제한불변"
  ],
  "luna_next": "본hold포함pending전부sync,이번28사례장벽·stagecoverage·답대조·오답번호기계검증,CURRENT/checkpoint/handoff에G376미열람및sourcehold를명시하고pending0확인.새source읽기금지."
}
```


<!-- luna-raw:SESSION20261002-hold-G376-G384-context-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "hold_reason": "이번 응답의 처리·컨텍스트 예산 한계에 따른 안전한 세션 인계.완료 frontier/배치/준비사례소진을 종료 사유로 삼지 않으며 quota emergency도 아님.",
  "last_completed_group": "G384",
  "last_completed_semantic_record": "G384-induction-20261002-01",
  "completed_this_session_groups": [
    "G376",
    "G377",
    "G378",
    "G379",
    "G380",
    "G381",
    "G382",
    "G383",
    "G384"
  ],
  "completed_this_session_cases": 28,
  "next_group": "G385",
  "next_stage": "새 Astra 세션에서 AGENTS/CURRENT/ASTRA_START→meta_state/quota/pending 확인 후 G385 group blind.기존 BCF 실패/미해결과 BBS 간접조건 유보는 소급 수정하지 않음.",
  "incomplete_semantic_stage": null,
  "next_group_exposure": {
    "blind_source_seen": false,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "runtime_emergency_observed": false,
  "quota_status": "unavailable",
  "research_complete": false,
  "meta_audit_work": [
    "META109",
    "META110",
    "META111",
    "AUDIT111",
    "BACKFILL111 BBJ/BCE 논리반모형 및 BBS/BCF 입력경로대조"
  ],
  "preserve": [
    "BCF 최초③/공식② 실패·ㄹ배제/공식정답유일성 논증 미해결.사후보강을성공으로소급금지.",
    "BCF 원문이미지직접확인/정답HWP추출대응Luna보고와원정답표직접렌더미실시 구분.",
    "BCF answer_check02는독립판정후SDSS전provenance보충.최초필수group barrier와구분.",
    "BBJ가속·BCE확률반모형은실제과학모형아닌논리검증용.",
    "BBS/BCF 고려요소의간접영향 허용범위 유보.",
    "G383 shared_structure 언어오기는META111의한국어정정및shared_structure_ko를권위로보존;원raw변경금지.",
    "과거노출미확정으로strict blind확정성과제외·G024/G370 sourcehold·이전모든품질제한유지."
  ],
  "luna_next": "이hold까지pending전부sync,CURRENT/ASTRA_CHECKPOINT/기존handoff 최신상태갱신,28사례 stage coverage·두필수barrier·최초답27/28·매력오답번호·exact_error 기계검증,pending0/meta-auditfalse/backfillempty 확인.새source/봉인열람금지."
}
```


<!-- luna-raw:SESSION20261002-hold-G385-G398-context-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "hold_reason": "이번 응답의 처리·컨텍스트 예산에 따른 안전한 연구 세션 인계.완료한 passage/batch/frontier 또는 quota unavailable을 종료 사유로 삼지 않으며 quota emergency도 아님.",
  "last_completed_group": "G398",
  "last_completed_semantic_record": "META116-meta_induction-20261002-01",
  "completed_this_session_groups": [
    "G385",
    "G386",
    "G387",
    "G388",
    "G389",
    "G390",
    "G391",
    "G392",
    "G393",
    "G394",
    "G395",
    "G396",
    "G397",
    "G398"
  ],
  "completed_this_session_case_records": 42,
  "counting_limit": "42개 case 기록 중 BDV는 기존F와 원문 동일·태그/판정요약 기노출.새 고유문항으로 가산 금지.다른 case도 과거노출unknown으로 strictblind 확정성과 제외.원문고유수 전수중복검증 완료라고 주장하지 않음.",
  "next_group": "G399",
  "next_stage": "새 Astra 세션에서 AGENTS/CURRENT/ASTRA_START→meta_state/quota/pending 점검 후 G399 group blind.그룹 전체 barrier 유지.",
  "incomplete_semantic_stage": null,
  "next_group_exposure": {
    "blind_source_seen": false,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "runtime_emergency_observed": false,
  "quota_status": "unavailable",
  "quota_history": "세션 시작 및 그룹/주요전환마다 scripts/codex_quota 실제호출,모두unavailable.7%이하나runtime5%경고 관측 없음.",
  "research_complete": false,
  "meta_audit_work": [
    "META112",
    "META113",
    "META114",
    "AUDIT114",
    "BACKFILL114 BCP/BCT/BDB/BDF",
    "META115",
    "META116"
  ],
  "preserve": [
    "BCT 최초⑤/공식⑤ 일치와 별개로 억압의 필연적 경로라는 설명은 원문가능성을과강화한오류로철회.ㄷ연역타당성/유일성미해결.",
    "BDN 최초③/공식③ 일치와 별개로 장소별개입·전신되먹임순효과/유일성미해결;BDM⑤기질증가/효소감소에서산출감소정량필연성유보.",
    "BCPㄱ기능적유추의엄격분류확장유보,BDB20필수성미확정,BDF12범위미확정.",
    "BDV=MEET2012Q12=기존F.노출후재검토로만계수;원blindunknown기록과후속정정둘다보존.",
    "G398후보색인존재는완료연구중복확정이아님.matched_case_id=null이며과거노출unknown.",
    "BCF기존최초실패·ㄹ배제/유일성미해결,BBS간접조건, G024/G370 sourcehold와이전모든제한유지.",
    "이번가상반모형들은논리검사용이며실제법률·생물학사실/치료지침아님.",
    "공식답은봉인된공식전사필드대조.원정답표독립시각대조미실시."
  ],
  "luna_next": "이hold까지sync,이번42case14group의stagecoverage/barrier/선택답대조/매력오답번호/exact_error기계검증.CURRENT·ASTRA_CHECKPOINT·기존인수인계문서상단을G399미열람·실제제한포함최신요약으로갱신.AGENTS원문변경금지.새source/답/태그읽기금지.pending0및meta/auditfalse,backfillempty확인후보고.",
  "expected_queue_after_sync": 5704
}
```
<!-- luna-sync:SESSION20261002-G399-20261002 -->
## 최신 세션 인계 — G399 완료·G400 미열람

- G399(BEA·BEB·BEC) 기본 12 stage(각 blind·answer_check·independent_code·sdss_compare) 총 12 raw를 반영했다. Queue=processed=5,716 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 359 groups·1,260 cases, META116 이후 1 group·3 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G399 induction은 미완료다. 다음 frontier G400은 미열람·미노출이며, G399 induction 완료 전까지 다음 group 연구를 잠근다.
- G399 SDSS 대조에서 BEA 주46 유지·44 보조 확장, BEB 주92 유지·2 사후 보조 후보, BEC 주15 유지·94 국소 보조 후보를 raw 의미 그대로 반영했다. 기존 의미 유보는 변경하지 않는다.
<!-- luna-sync:SESSION20261002-G399-20261002 -->
## 최신 세션 인계 — G399 완료·G400 미열람

- G399(BEA·BEB·BEC) 기본 12 stage와 induction 1건, 총 13 raw를 반영했다. Queue=processed=5,717 unique, pending=0, duplicate=0, orphan=0.
- `meta_state.py`: 완료 359 groups·1,260 cases, META116 이후 1 group·3 cases; `meta_due=false`, `manual_parity_audit_due=false`(다음 audit까지 1 meta), `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- G399 기본 stage와 induction을 완료했다. 다음 frontier G400은 미열람·미노출이며 잠금 해제한다.
- G399 SDSS 대조에서 BEA 주46 유지·44 보조 확장, BEB 주92 유지·2 사후 보조 후보, BEC 주15 유지·94 국소 보조 후보를 raw 의미 그대로 반영했다. 기존 의미 유보는 변경하지 않는다.


<!-- luna-raw:SESSION20261002-hold-G399-G410-response-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "현재 응답 작업 예산에 따른 안전 인계. frontier/batch 완료나 quota unavailable 자체를 연구 완료 사유로 삼는 것이 아니며 연구 전체는 미완료.",
  "quota_status": "unavailable",
  "runtime_quota_emergency_observed": false,
  "quota_threshold_observed": false,
  "completed_groups": [
    "G399",
    "G400",
    "G401",
    "G402",
    "G403",
    "G404",
    "G405",
    "G406",
    "G407",
    "G408",
    "G409",
    "G410"
  ],
  "completed_case_range": "BEA~BFJ,36case 기록",
  "completed_meta": [
    "META117",
    "META118",
    "META119",
    "META120"
  ],
  "completed_manual_audits": [
    "AUDIT117",
    "AUDIT120"
  ],
  "completed_backfills": [
    "BACKFILL117-BEB",
    "BACKFILL117-BEE",
    "BACKFILL120-BEM",
    "BACKFILL120-BFJ"
  ],
  "raw_persistence": "모든 완료 판단은 append 완료. Luna가 남은 raw·본hold를 동기화하고 pending0 및 due상태를 검증해야 함.",
  "next_frontier": "G411",
  "next_stage": "새 세션 AGENTS/CURRENT/ASTRA_START 복원→meta_state·quota·pending검사→due해소 확인→G411 blind",
  "exposure": {
    "G411_blind_source_read": false,
    "G411_official_answer_read": false,
    "G411_sdss_read": false
  },
  "incomplete_semantic_stage": null,
  "persistent_limitations": [
    "BFE 최초 blind는 표적 문구 결손 아래 조건부. 정답 공개 전 공식HWP_XML로 정당 수 산정 복원; 원blind지위 소급 승격 없음.",
    "모든 case의 과거노출unknown으로 strictblind 성과 확정 제외.36case는 신규고유문항 수 검증 아님.",
    "BEM 동일 채널률 전제·정답 유일성 유보, BFJ 검증 관련성과 확정 인과 입증 구별",
    "BEB 문맥적 보 사용, BED⑤ 범위, BEE65 등 사이트 정확범위와 기존 BCT·BDN·BDM·BCP·BDB·BDF·BCF·BBS 유보 유지"
  ],
  "semantic_corrections": [
    "BED74/75의 인위적 배타 경계 인상을 기존 C074_075 통합군 기준으로 정정",
    "BEY⑤에서 직접 대화 전후만으로 근심 영향 부재를 단정하지 않도록 제한"
  ],
  "new_recording_principle": "G408부터 general_task와 decisive_relation을 분리하여 포괄 작업명과 구체 판단 관계를 모두 보존."
}
```


<!-- luna-raw:SESSION20261002-G411-G422-hold-20261002-r3-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "reason": "이번 응답의 작업·컨텍스트 예산에 따른 안전 인계. passage/batch/frontier 완료나 quota unavailable 자체를 연구 완료 사유로 삼는 것이 아니며 연구 전체는 미완료.",
  "quota_status": "unavailable",
  "quota_threshold_observed": false,
  "runtime_quota_emergency_observed": false,
  "completed_groups": [
    "G411",
    "G412",
    "G413",
    "G414",
    "G415",
    "G416",
    "G417",
    "G418",
    "G419",
    "G420",
    "G421",
    "G422"
  ],
  "completed_case_range": "BFK~BGQ,33case 기록",
  "completed_meta": [
    "META121",
    "META122",
    "META123",
    "META124"
  ],
  "completed_manual_audits": [
    "AUDIT123"
  ],
  "completed_backfills": [
    "BACKFILL123-BFQ",
    "BACKFILL123-BGA"
  ],
  "raw_persistence": "완료 판단은 모두 append됨. 이 hold 및 잔여raw는 Luna 최종 sync·검증 대상.",
  "incomplete_semantic_stage": null,
  "next_frontier": "G423",
  "next_stage": "새 Astra 세션에서 AGENTS/CURRENT/ASTRA_START 복원→meta_state·quota·pending검사→due없음확인→G423 blind",
  "exposure": {
    "G423_blind_source_read": false,
    "G423_official_answer_read": false,
    "G423_sdss_read": false
  },
  "persistent_limitations": [
    "모든case 과거노출unknown으로 strict-blind 성과확정 제외.33case는33개 신규고유원문 증명 아님.",
    "BFX 최초번호는조건부였으며정답·SDSS공개후공식매핑④확인.구조답과최초지위는보존.",
    "BGD/BGQ수식전사누락이있으나문장근거로판정.원정답표독립시각대조는미실시.",
    "BFM②장소범위,BFP20·③제소,BFQ⑤부합,BFS합기준시점,BFY61,BFX23,BGD③,BGH24,BGI추론,BGK/BGM95 및 이전유보 지속.",
    "LEET관찰이며KICE교차검증없이최종평가원생성규칙으로승격하지 않음."
  ],
  "semantic_corrections": [
    "BFQ36은반례가주어졌다는이유로낮출수없어강한보조로보강.",
    "BGA독학문장삭제후에도작품의사실성증거가남으므로이전삭제검사과장을철회.19는강한보조이나단독필수경로아님."
  ],
  "luna_next": "이hold까지sync.33case실제queue줄stagebarrier·답대조·exact_error·경쟁2~4·raw중복을검증.CURRENT/ASTRA_CHECKPOINT/기존인수인계상단에G423미열람과실제제한을반영.AGENTS수정및새source/답/태그열람금지.pending0·meta/auditfalse·depth[] 확인 후보고."
}
```


<!-- luna-raw:BGW-hold-source-20261002-r4-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G424",
  "reason": "blind-only packet의 <조건> 미전사. 세 tif는 음정진행·주요3화음 도표·보기 악보이며 조건이 없다.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "provisional_observation": "보기 각 마디 음명은 솔도도 / 도라도파미 / 레솔파 / 미솔솔미도. 조건 없이 화음 배정의 허용 규칙을 확정하지 않는다.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown"
  },
  "next_work": "Luna가 공식 원문 조건만 blind-only 부록으로 복원한 뒤 직접 읽고 최초 풀이 완결. 그룹 전체 blind 완료 전 answer_check 금지.",
  "quota_status": "unavailable",
  "runtime_emergency_observed": false
}


<!-- luna-raw:BIB-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G435",
  "reason": "blind packet 발문이 정리한에서 끊기고[A] 범위표지가 누락되어 기계적 정본 복원 요청.답 선택은 아직 저장하지 않음.",
  "next_action": "정본에서 완전한 발문과[A]범위를 blind-only 보충 후 BIB blind 완료.그 전 group 답공개 금지.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BHZ/BIA blind 저장, BIB blind 미완료."
}
```


<!-- luna-raw:BJB-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G444",
  "reason": "본문집단심성명칭과BJB발문대상이[시각자료1]로빠짐.연결된visual01은다른보기사건으로해당명칭을복원하지못함.",
  "next_action": "공식문제에서빠진인라인표현과BJB완전발문을blind-only보충한뒤blind풀이.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BJA blind저장,BJB미완료.전체답공개금지."
}
```


<!-- luna-raw:BJF-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G446",
  "reason": "본문첫문단끝과BJF발문대상의인라인표현이[시각자료1]로누락.보충파일은BJG/BJH보기라누락표현을복원하지못함.",
  "next_action": "공식정본에서인라인표현과완전발문을blind-only보충.그동안같은group다른문항blind만진행가능.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "모든blind저장전전체공식답비공개."
}
```


<!-- luna-raw:BJR-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G449",
  "reason": "본문마지막주체와BJR평가대상이[시각자료1]로누락.보충파일은BJS보기라실제표현복원안됨.",
  "next_action": "누락주체와완전발문blind-only정본복원후BJR풀이.다른groupcaseblind는진행가능.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "모든blind저장전전체답비공개."
}
```


<!-- luna-raw:BJX-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G451",
  "reason": "본문마지막개정대상과BJX발문대상이[시각자료1]로누락.보충파일은BJY보기임.",
  "next_action": "누락표현과완전발문을정본blind-only보충후BJX풀이.다른문항blind진행가능.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "모든blind저장전전체답비공개."
}
```


<!-- luna-raw:BKK-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G455",
  "reason": "본문 마지막 문단 비판 명칭과 BKK 발문 대상이 [시각 자료 1]로 누락. 보충 파일은 BKJ 보기여서 명칭을 복원하지 못한다.",
  "incomplete_stage": "blind",
  "next_action": "Luna가 정본에서 누락 명칭·표지와 완전 발문만 blind-only 부록으로 복원한 후 BKK blind를 직접 수행한다.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BKI blind 저장; BKJ/BKK 완료 전 group 전체 답 공개 금지.",
  "selected_answer": null
}
```


<!-- luna-raw:BKO-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G457",
  "reason": "마지막 문단 명칭과 BKO 발문이 시각 자료 placeholder로 누락.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "next_action": "공식 HWP의 실제 인라인 명칭과 완전 발문을 blind-only 부록으로 복원한 뒤 직접 풀이.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BKN blind 저장. BKO/BKP blind 저장 전 그룹 답 공개 금지."
}
```


<!-- luna-raw:BKQ-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G458",
  "reason": "본문 첫 인라인 명칭과 BKQ 발문 대상이 시각 자료 placeholder로 누락.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "next_action": "공식 HWP 실제 명칭과 완전 발문 blind-only 복원 후 직접 풀이.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "모든 group blind 저장 전 답·SDSS 비공개."
}
```


<!-- luna-raw:BKU-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G459",
  "reason": "2문단 인라인 대상과 BKU 발문 대상 누락.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "next_action": "공식HWP에서 대상 명칭·완전발문을 blind-only 복원 후 풀이.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BKT만 blind 저장.전체blind완료전 답공개 금지."
}
```


<!-- luna-raw:BLG-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G463",
  "reason": "첫문단집중적으로그려진대상과BLG발문대상의인라인명칭누락.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "next_action": "공식2020HWP의실제명칭·완전발문을blind-only복원후풀이.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BLF blind저장.전체blind완료전답공개금지."
}
```


<!-- luna-raw:BLR-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G467",
  "reason": "공통본문의운동에너지·중력위치에너지·중력및역학적에너지수식과변수표기가빈괄호·쉼표로소실됨.두그림은궤도만포함해수식을복원하지못함.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "next_action": "공식문제HWP/PDF에서공통본문의전체수식·변수정의·그림참조표기를blind-only부록으로복원한뒤BLR·BLT판정.외부물리식으로빈칸을대체하지않는다.",
  "exposure": {
    "blind_source_seen": true,
    "visuals_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "그룹blind미완료.공식답·SDSS전부비공개유지."
}
```


<!-- luna-raw:BLV-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G468",
  "reason": "공통본문의두시각자료placeholder로[A]·[B]범위가소실됨.BL V는[A],BL W는[B]를명시적으로지시하므로정확범위및누락본문존재확인이필요.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "next_action": "공식문제에서[A]/[B]시작·끝과그내부텍스트를blind-only부록으로복원.연륜연대계산의원문표현도보존.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "그룹blind미완료.공식답·태그전부비공개."
}
```


<!-- luna-raw:G468-hold-source-resolved-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G468",
  "case_ids": [
    "BLU",
    "BLV",
    "BLW"
  ],
  "resolves": "BLV-hold-source-20261003-01",
  "resolution": "주에이전트가공식렌더crop을직접확인.[A]는2005년수목예시한문단,[B]는전문가증거기준의마지막한문단.첫복원부록의[A]첫5문단주장은잘못이어서시각좌표확인후정정됨.",
  "evidence": [
    "data/기본기_연구/prepared_backlog/blind_sources/BLV_A_official_bracket_crop.png",
    "data/기본기_연구/prepared_backlog/blind_sources/BLV_B_official_bracket_crop.png",
    "data/기본기_연구/prepared_backlog/blind_sources/BLV-hold-source-20261003-appendix.md"
  ],
  "original_blind_preserved": true,
  "answer_effect": "세blind선택·논리변경없음.BL V계산은처음부터정확한예시문단에한정.BL W는마지막문단과보기기준사용.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "next_action": "group전체blind저장확인후answer_check시작.",
  "source_policy": "텍스트앵커와대괄호의실제범위를동일시하지않는다.미확인범위를공식렌더확인으로가장한최초보조보고는판정근거로채택하지않았다."
}
```


<!-- luna-raw:BML-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G473",
  "reason": "본문첫인라인명칭및BML발문의두비교대상이placeholder로소실.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "next_action": "공식2021HWP/렌더에서두명칭과완전발문을blind-only복원.이름을선지에서추정해복원완료로기록하지않는다.",
  "exposure": {
    "blind_source_seen": true,
    "supplement_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BMJ/BMK blind저장.BML완료전그룹공식답비공개."
}
```


<!-- luna-raw:BMN-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G474",
  "reason": "수단 항쟁 문단의 인라인 명칭과 BMN 발문 대상이 placeholder로 소실됨.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "next_action": "공식2021HWP에서 실제 명칭과 완전 발문을 blind-only 복원한 뒤 풀이.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BMM blind 저장. BMN·BMO 완료 전 그룹 답 공개 금지."
}
```


<!-- luna-raw:BMR-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G475",
  "reason": "후반의 이이 계승자 인라인 명칭과 BMR의 입장 지시 대상이 placeholder로 소실됨.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "next_action": "공식2021HWP에서 대상이 한 사람인지 복수인지 포함해 명칭·완전 발문을 blind-only 복원한다.",
  "exposure": {
    "blind_source_seen": true,
    "supplement_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BMP/BMQ blind 저장. BMR 완료 전 그룹 답 공개 금지."
}
```


<!-- luna-raw:BMT-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G476",
  "reason": "마지막 문단의 인라인 주체와 BMT 발문 대상이 placeholder로 소실됨.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "next_action": "공식2021HWP에서 복수 주체 명칭과 완전 발문을 blind-only 복원한다.",
  "exposure": {
    "blind_source_seen": true,
    "visuals_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BMS blind 저장. BMT/BMU 완료 전 그룹 답 공개 금지."
}
```


<!-- luna-raw:BND-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G479",
  "reason": "ℓ 허용범위가 ㄷ 판정에 영향을 줌.추출본은 한 민감값 집합이 ℓ-다양성을 만족하지 못한다고 설명하지만 ℓ≥2의 별도 수식·주석 존재 여부는 불명확.정본 조건 누락 가능성을 확인한다.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "provisional_calculation": "(a)의 동질집합은 크기2·서로다른민감값2인 집합3개,(b)는 크기4/2·민감값2인 집합2개.ℓ=1 허용 시ㄷ의 같은ℓ 결론에 반례가 있고 ℓ≥2이면 해당 조건에서 양쪽ℓ=2가 된다.",
  "next_action": "공식2024PDF에서 ℓ 정의·범위조건·문항보기 주석을 blind-only crop과 텍스트로 확인.답·SDSS 비공개 유지.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BNB/BNC blind저장,BND미완료.그룹공식답공개금지."
}
```


<!-- luna-raw:BNG-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G480",
  "reason": "BNG 보기 수식과 선지의 R/DC/OC 및 부등호가 전용 글리프로 추출되어 정확한 기호 확인이 필요함.",
  "incomplete_stage": "blind",
  "selected_answer": null,
  "next_action": "공식2024PDF의 BNG 보기·선지 전체를 blind-only crop으로 확인하고 수식·비교기호를 정확히 전사한다.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BNE/BNF blind 저장. BNG 완료 전 공식답·태그 비공개."
}
```
<!-- luna-sync:SESSION20261003-G480-sync-20261003 -->
## 최신 Luna sync — G480 기본 stage·BNG source hold 및 SDSS 대조 반영

- BNE·BNF·BNG의 blind·answer_check·independent_code·sdss_compare 12 raw와 `BNG-hold-source-20261003-01` 1건을 기존 처리기로 반영했다. Queue=processed=6,822 unique, pending=0, duplicate/orphan=0.
- BNG source hold는 원raw와 `needs_astra_review`를 보존했다. 세 case의 group barrier는 blind 전체 → answer_check 전체 → independent_code 전체 → SDSS 대조 순서로 통과했으며, Luna는 의미를 재판정하지 않았다.
- `meta_state.py`: 440 groups·1,498 cases, META143 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `manual_parity_audits_remaining_to_next=1`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- prepared manifest는 1,671건이며 최소 임계치 미만이 아니어서 후보 추가 준비는 하지 않았다. 다음 Excel-style frontier는 G481의 `BNH, BNI, BNJ`; 다음 Astra 단계는 이 group 전체 blind다. blind-only source는 `data/기본기_연구/prepared_backlog/blind_sources/BNH.json`, `BNI.json`, `BNJ.json`이다.
- blind packet의 blind-only 표식과 공식답·SDSS·기존 판정 top-level 키 부재를 기계 확인했고, sealed 자료는 `data/기본기_연구/prepared_backlog/sealed/`에 분리되어 있음을 확인했다. 다음 Astra가 blind 단계에서 sealed/canonical/기존 판정 자료를 열지 않도록 한다.


<!-- luna-raw:BOH-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G489",
  "incomplete_stage": "blind",
  "reason": "추출된 표에서 효소㉣ 행 뒤에 유로포르피리노젠I→코프로포르피리노젠I 반응이 별도 행으로 나타나 병합셀 귀속을 공식 표에서 확인해야 함.",
  "next_action": "정답·SDSS를 노출하지 않은 BOH 공식 보기 표의 tight crop을 blind_sources 아래 복원하고 효소㉣에 두 반응이 속하는지 직접 확인한다.",
  "provisional_answer": 3,
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BOF·BOG blind 저장, BOH 미완료. group 공식답·SDSS 공개 금지."
}
```


<!-- luna-raw:BON-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G491",
  "incomplete_stage": "blind",
  "reason": "보기의 여론 변화 그래프가 시각 자료1 placeholder로 빠져 추세·비율·시점이 확인되지 않는다.",
  "next_action": "BON 공식 여론 변화 그래프와 범례·시점 표시만 tight crop으로 복원한 뒤 직접 판독한다. 정답·SDSS 미공개 유지.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BOL·BOM blind 완료, BON 미완료. group answer_check 금지."
}
```


<!-- luna-raw:G493-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G493",
  "case_ids": [
    "BOS",
    "BOT"
  ],
  "incomplete_stage": "blind",
  "reason": "BOS가참조하는공통그래프가placeholder이며BOT의[A]괄호범위가추출본맨아래표시로만남아공식범위확인이필요하다.",
  "next_action": "공식2025홀수형의솔로우성장모형그래프와[A]범위를각각tightcrop으로blind_sources에복원한다. 답·태그·기존해설미공개.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BORblind저장,BOS/BOT미완료.전체blind전공식답금지."
}
```


<!-- luna-raw:BPB-hold-source-20261003-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G496",
  "incomplete_stage": "blind",
  "reason": "보기의 두 상황에서 읽기·쓰기·완료·롤백 순서를 표시한 그림이 placeholder로 빠졌다.",
  "next_action": "공식2025홀수형 BPB 보기의 두상황그림과 번호·범례를 tightcrop으로 복원한 뒤 원문상의 순서만 분석한다. 답·SDSS비공개 유지.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BPAblind저장,BPB미완료. 전체group답확인금지."
}
```


<!-- luna-raw:BPK-hold-source-20261004-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G499",
  "incomplete_stage": "blind",
  "reason": "공통그림1·2가placeholder로빠져FEEL조건표의비교연산자와숫자구간표기·조건열의원형을확인할필요가있다.",
  "next_action": "공식2026홀수형 DMN지문의그림1DRD와그림2의사결정테이블을tightcrop으로복원하고본문의경계표기와직접대조한다. 답·SDSS미공개유지.",
  "provisional_answer": 4,
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BPI·BPJblind저장,BPK미완료. group답확인금지."
}
```


<!-- luna-raw:BPN-hold-source-20261004-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G500",
  "incomplete_stage": "blind",
  "reason": "보기 그림1의V1~V4와L/R위치, 그림2의연도별분포가placeholder로빠짐.",
  "next_action": "공식2026홀수형 해당문항의두그래프·축·범례만tightcrop으로복원해직접판독한다. 답·SDSS미공개유지.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BPL·BPMblind저장,BPN미완료로group답확인금지."
}
```


<!-- luna-raw:SESSION-hold-normal-quota-20261004-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "handoff_mode": "normal_quota_threshold",
  "reason": "실제 quota 조회에서 주간 잔여7%(used93)가 처음 관측되어 신규 semantic stage를 중단한다. runtime<5% 경고에 의한 emergency가 아니다.",
  "quota": {
    "quota_status": "partial",
    "primary_used_percent": null,
    "primary_remaining_percent": null,
    "weekly_used_percent": 93,
    "weekly_remaining_percent": 7
  },
  "last_completed_atomic_record": "BPT-independent_code-20261004-01",
  "passage_group": "G502",
  "case_ids": [
    "BPR",
    "BPS",
    "BPT"
  ],
  "completed_stages": "세 case 모두 blind·answer_check·independent_code raw 저장 완료. group 전체 blind→답대조, group 전체 독립판정 barrier 유지.",
  "incomplete_stages": [
    "G502 전체 sdss_compare",
    "G502 induction",
    "이후 meta_state 재확인 및 다음 frontier"
  ],
  "next_action": "Luna가 신규9개 연구raw와 이hold를 의미변경없이sync하고pending0·CURRENT를갱신한다. 다음Astra는G502전체independent_code저장을확인한뒤SDSS공개·대조부터재개한다.",
  "exposure": {
    "G502_blind_sources_seen": true,
    "G502_official_answers_seen": true,
    "G502_sdss_seen": false,
    "G503_sources_seen": false,
    "strict_blind_eligible": false
  },
  "last_observed_meta_state": {
    "meta_due": false,
    "manual_parity_audit_due": false,
    "depth_backfill_pending": []
  },
  "operational_note": "scripts/codex_quota는7일창을primary슬롯으로받고secondary=null인응답을수정처리한다.창길이300/10080으로구분하며없는5시간값은null.10fixture검증통과.실제조회는승인된sandbox외부실행으로성공했다.",
  "termination_gate": "A: 주간 remaining<=7 정상handoff. prepared backlog 소진이나 연구완료로 기록하지 않는다.",
  "raw_ledger_policy": "기존원장·최초판정·유보는불변. 미완료SDSS·귀납을Luna가추론해완성하지않는다."
}
```
<!-- luna-sync:SESSION-hold-normal-quota-20261004-01-sync-20261004 -->
## 최신 Luna sync — 정상 quota handoff·G502 SDSS 대기

- `BPR, BPS, BPT`의 blind·answer_check·independent_code 9 raw와 `SESSION-hold-normal-quota-20261004-01` hold 1건을 의미 변경 없이 반영했다. Queue=processed=7,128 unique, pending=0, duplicate=0, orphan=0.
- G502 세 최초 답은 공식 답과 일치한다(②·③·③). `past_exposure=unknown`, `strict_blind_eligible=false`를 보존하여 엄격 blind 성과에서 제외한다. G502 SDSS 공개·대조와 induction은 미완료이며 Luna가 추론으로 채우지 않는다.
- `meta_state.py`: 완료 461 groups·1,560 cases, META150 이후 1 group·3 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 이번 run의 신규 완료 범위는 G481~G501이며, 최초 오답 기록 BNQ는 원기록과 기존 품질·노출 제한을 유지한다. 다음 Astra 단계는 G502 전체 independent-code barrier 확인 후 SDSS 공개·대조부터 재개한다. G503은 미열람이다.
- 정상 handoff 사유는 주간 remaining 7%(used 93%) 최초 관측이며 runtime emergency가 아니다. primary 5h 값은 null로 보존한다. 연구 전체 완료나 backlog 소진으로 해석하지 않는다.


<!-- luna-raw:SESSION-hold-normal-quota-20261004-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "handoff_mode": "normal_quota_threshold",
  "reason": "새 세션 초기 scripts/codex_quota 실제 조회에서 weekly remaining=7%(used=93%) 관측. 신규 semantic stage 시작 전에 정상 handoff. runtime emergency 경고는 관측되지 않음.",
  "quota": {
    "quota_status": "partial",
    "primary_used_percent": null,
    "primary_remaining_percent": null,
    "weekly_used_percent": 93,
    "weekly_remaining_percent": 7
  },
  "passage_group": "G502",
  "case_ids": [
    "BPR",
    "BPS",
    "BPT"
  ],
  "completed_stages": "CURRENT 기준 세 case blind·answer_check·independent_code 완료 및 processed. 이번 세션 신규 의미 판단 없음.",
  "incomplete_stages": [
    "G502 전체 sdss_compare",
    "G502 induction"
  ],
  "next_action": "Luna가 이 hold 및 미처리 raw를 기계적으로 sync하고 pending=0 검증. 다음 quota 허용 세션에서 G502 전체 independent_code barrier 확인 후 SDSS 대조부터 재개.",
  "exposure": {
    "this_session_new_blind_source_read": false,
    "this_session_sealed_read": false,
    "G502_sdss_seen": false,
    "G503_sources_seen": false,
    "strict_blind_eligible": false
  },
  "last_observed_meta_state": {
    "completed_passage_groups_total": 461,
    "completed_questions_total": 1560,
    "meta_due": false,
    "manual_parity_audit_due": false,
    "depth_backfill_pending": [],
    "semantic_state_review": []
  },
  "termination_gate": "A: 실제 주간 remaining<=7 정상 handoff. 연구 완료 또는 prepared backlog 소진이 아님."
}
```
<!-- luna-sync:SESSION-hold-normal-quota-20261004-02-sync-20261004 -->
## 최신 Luna sync — 사용자 지시에 따른 정상 7% 중단 해제·G502 SDSS 재개

- `SESSION-hold-normal-quota-20261004-02` 원raw는 불변 보존했다. 주간 remaining 7%(used 93%)만을 이유로 한 정상 handoff 중단은 사용자 최신 지시에 따라 해제한다. runtime emergency 경고는 관측되지 않았다.
- G502 BPR·BPS·BPT의 blind·answer_check·independent_code barrier와 hold raw를 기계적으로 보존했다. 다음 연구는 G502 전체 SDSS 공개·대조부터 재개한다. G503은 미열람이다.
- 이번 sync 후 queue/processed unique=7,129, pending=0, duplicate/orphan=0. `meta_state.py`: 461 groups·1,560 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
<!-- luna-sync:SESSION20261004-G502-sdss-sync-20261004 -->
## 최신 Luna sync — G502 SDSS 대조 반영·induction 대기

- G502 BPR·BPS·BPT `sdss_compare` raw 3건을 기계적으로 반영했다. SDSS 제3자 색인과 독립 판정의 일치·불일치 및 유보를 원raw대로 보존했으며 Luna는 의미를 재판정하지 않았다.
- queue/processed unique=7,132, pending=0, duplicate/orphan=0. `meta_state.py`: 461 groups·1,560 cases; `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`.
- 주간 remaining 7%에 따른 정상 중단 해제 상태를 유지한다. G502 induction은 미완료이며 다음 단계는 해당 induction raw 저장 후 반영이다. G503은 미열람이다.


<!-- luna-raw:BPY-hold-source-20261004-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G504",
  "incomplete_stage": "blind",
  "reason": "blind source의[A][B][C]가 선지⑤ 뒤에 모여 있어 정확한 본문 구간 경계가 소실됐다.구간 관계를 묻는 BPY는 공식 범위 확인이 필요하다.",
  "next_action": "공식 문제지에서[A]~[C]표시 범위만 blind-only source로 복원해 직접 확인.정답·SDSS는 그룹 blind 완료까지 비공개.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BPX blind 저장,BPY 미완료.BPZ는 별도 풀이 가능하나 전체 답 공개 금지."
}
```


<!-- luna-raw:G508-hold-answer-source-20261004-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G508",
  "case_ids": [
    "BQJ",
    "BQK",
    "BQL",
    "BQM"
  ],
  "incomplete_stage": "answer_check",
  "reason": "그룹 전체 blind raw 저장 후 answer-only 공개 결과 공식 정답이 null이며 source preparation 때 접근하지 않았다는 표식만 존재한다.",
  "next_action": "provenance에서 시험과 번호를 식별하고 공식 정답표를 연결한 뒤 네 답을 직접 대조한다.독립 코드 판정과 SDSS 공개는 아직 시작하지 않는다.",
  "exposure": {
    "group_all_blind_saved": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "네 blind 완료.공식 답 복원 대기.답을 사이트태그·예상답으로 보충하지 않는다."
}
```


<!-- luna-raw:G509-hold-answer-source-20261004-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G509",
  "case_ids": [
    "BQN",
    "BQO",
    "BQP"
  ],
  "incomplete_stage": "answer_check",
  "reason": "세 case 전체 blind 저장 후 answer-only 공개했으나 준비파일의 공식답이null이다.",
  "next_action": "공식 출제시험·번호와 정답표를 연결해 대조.독립 코드·SDSS 미시작 상태 유지.",
  "exposure": {
    "group_all_blind_saved": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "전체blind완료,정답정본연결대기"
}
```
<!-- luna-sync:SESSION20261005-BQC-depth-sync-20261005 -->
## 최신 Luna sync — BQC backfill 반영·G510 독립 코드 barrier 진행 중

- `BQC-depth_backfill-AUDIT153-20261005-01` raw를 기존 상세 기록에 의미 변경 없이 반영했다. `BQI-depth_backfill-AUDIT153-20261004-01`는 이미 processed이므로 재반영·재연구하지 않았다. G510의 blind 3건과 answer_check 3건, 현재까지 저장된 independent_code raw 1건도 기계적으로 반영했다.
- Queue=processed=7,247 unique, pending=0, duplicate/orphan=0. `meta_state.py` 재실행 결과 469 groups·1,585 cases, `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`.
- 다음 실제 미완료 frontier는 G510 전체 `BQQ, BQR, BQS`의 independent_code stage barrier 완료다. Manifest 준비 상태 및 blind-source 존재: BQQ — `data/기본기_연구/prepared_backlog/blind_sources/BQQ.json` (prepared, 존재); BQR — `data/기본기_연구/prepared_backlog/blind_sources/BQR.json` (prepared, 존재); BQS — `data/기본기_연구/prepared_backlog/blind_sources/BQS.json` (prepared, 존재). SDSS 공개 전 group barrier를 완료한다. 이번은 정상 연구 중 sync이며 종료/hold가 아니다.


<!-- luna-raw:BRN-hold-20261005-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G520",
  "case_ids": [
    "BRN"
  ],
  "incomplete_stage": "blind",
  "reason": "blind source의학습활동지선지가잘못분할되어선지③에행크스진술2와에이어진술3이함께들어가고선지⑤에는쪽번호062만존재한다.본문첫머리도2027교재HWPX출처이므로공식문항구조와답번호를확인할blind-only복원이필요하다.",
  "next_action": "보조에이전트가공식출제시험및문항을기계적으로연결하여학생활동지선지①~⑤의구조를blind-onlysource에복원.정답·SDSS·기존판정은주Astra에게노출하지말것.복원전선택답확정금지.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown"
  },
  "completed_judgment": "선택답·코드판정없음.원문구조결손진단만완료.",
  "group_barrier": "BRN blind미완료.정답및SDSS공개금지."
}
```


<!-- luna-raw:BRN-hold-20261005-02 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G520",
  "incomplete_stage": "blind",
  "reason": "복원된선지배열의번호는5개이나활동지[진술1~3]의문장내용이빠져표제만남음.추가복원요청.",
  "next_action": "세진술본문을blindsource에복원하고공식원문구조근거를명확히한뒤선택답저장.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "assistant_restorer_sealed_row_accessed": true,
    "assistant_restorer_sealed_values": "official_answer=null,site_original_codes=null;정답번호·태그값노출없음",
    "strict_blind_eligible": false
  },
  "initial_hold_preserved": true
}
```


<!-- luna-raw:BSR-hold-20261005-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G530",
  "incomplete_stage": "blind",
  "reason": "[A]로부터추론불가한항목을묻지만blind본문에[A]시작·종료표시가없다.인접한장닭사건문단일것으로추정할수있어도범위밖진술로오답을배제하지않도록공식범위확인필요.",
  "next_action": "기계적보조가공식원문[A]범위만복원한blind-only자료를제공한뒤주Astra직접풀이.",
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false
  },
  "group_barrier": "BSQblind저장,BSR미완료.BSS독립blind가능하나group정답·SDSS공개금지."
}
```


<!-- luna-raw:G024-hold-20261005-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G024",
  "case_ids": [
    "DR",
    "DS",
    "DT",
    "DU"
  ],
  "incomplete_stage": "independent_code",
  "reason": "최신원장의20260912preexposure-barrierhold를재확인. DR의공식답·사이트49가group원문이전에노출되었고원hold가다른case의최초독립판정생성을명시적으로금지한다.현재사용자도group전체independent이전SDSS공개금지장벽을유지한다.과거quota7%hold는현재quota로승계하지않지만노출장벽은해소되지않았다.",
  "completed_stages": [
    "group전체blind/노출인지기록",
    "group전체answer_check"
  ],
  "not_performed": [
    "재blind",
    "최초independent_code생성",
    "SDSS추가공개",
    "새코드의미판정"
  ],
  "next_action": "독립최초연구로재개하지않는다.명시적으로정해진사전노출사례비독립검토절차가마련될때기존기록을보존한별도후속연구만가능.",
  "exposure": {
    "DR_answer_and_site49_preexposed": true,
    "DS_DT_DU_answers_seen": true,
    "DS_DT_DU_sdss_seen": false,
    "strict_blind_eligible": false,
    "this_session_new_original_or_sealed_read": false
  },
  "original_records_immutable": true,
  "research_completed": false,
  "disposition": "기존절차상non_actionable_hold유지.완료·성공·새독립연구실적아님."
}
```


<!-- luna-raw:G370-hold-20261005-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G370",
  "case_ids": [
    "BAP",
    "BAQ",
    "BAR",
    "BAS"
  ],
  "incomplete_stage": "blind",
  "reason": "현재blind4파일과공식2017LEET홀수원렌더4쪽을주Astra가직접확인.두지문상자는본문없이온라인게시불가안내와이청준가면의꿈출처만존재한다.원문본문·[A][B]·기호문맥이없어독해와선지판정불가.",
  "evidence": "data/기본기_연구/prepared_backlog/blind_sources/G370_source_notice_20261005.png",
  "origin": "자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2017/page_004.png",
  "next_action": "실제시험에제시된본문과모든범위표시를검증할수있는question-only원문을확보하면그룹전체blind부터재개.현재안내문이나작품제목으로원문·답·코드를추정하지않는다.",
  "exposure": {
    "actual_passage_seen": false,
    "official_answer_seen": false,
    "sdss_seen": false,
    "this_session_choices_read": false,
    "source_notice_seen": true
  },
  "research_completed": false,
  "disposition": "source_unavailable유지.완료·제외·성공사례로계수하지않음.",
  "original_hold_preserved": true
}
```


<!-- luna-raw:SESSION20261005-hold-20261005-01 -->
## Astra raw handoff — hold

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "handoff_mode": "source_and_stage_barrier_block",
  "termination_gate": "D: G370은공식배포본원문누락으로복원전진행불가.다른미완료G024는기존사전SDSS노출장벽때문에현재절차로독립단계진입불가.전체manifest에서그외actionablepreparedgroup은없음을Luna최종검증할것.",
  "completed_this_run": {
    "passage_groups": [
      "G510",
      "G511",
      "G512",
      "G513",
      "G514",
      "G515",
      "G516",
      "G517",
      "G518",
      "G519",
      "G520",
      "G521",
      "G522",
      "G523",
      "G524",
      "G525",
      "G526",
      "G527",
      "G528",
      "G529",
      "G530",
      "G531",
      "G532",
      "G533",
      "G534",
      "G535",
      "G536",
      "G537"
    ],
    "groups": 28,
    "cases": 78,
    "meta_induction_count": 9,
    "meta_ids": [
      "META154",
      "META155",
      "META156",
      "META157",
      "META158",
      "META159",
      "META160",
      "META161",
      "META162"
    ],
    "manual_parity_audits": [
      "AUDIT156",
      "AUDIT159",
      "AUDIT162"
    ],
    "depth_backfill_cases": [
      "BQC",
      "BQT",
      "BRJ",
      "BSA",
      "BSD",
      "BRN",
      "BSP",
      "BSL",
      "BTH"
    ]
  },
  "remaining": {
    "G024": "DR/DS/DT/DU:기존blind·answer보존,최초independent생성금지hold",
    "G370": "BAP/BAQ/BAR/BAS:실제본문누락,blind0/4,답·SDSS봉인"
  },
  "meta_state_last_observed": {
    "completed_groups": 497,
    "completed_cases": 1663,
    "meta_due": false,
    "manual_parity_audit_due": false,
    "depth_backfill_pending": []
  },
  "quota": {
    "last_available_primary_remaining_percent": null,
    "last_available_weekly_remaining_percent": 51,
    "runtime_emergency_observed": false,
    "stop_is_quota_triggered": false
  },
  "next_action": "Luna가신규hold3건만의미변경없이sync하고pending0/중복고아0/전체manifest의actionable0을검증.원장·CURRENT에연구총완료나8보류완료를선언하지말것.이후원문복원또는명시비독립검토절차가생기면재개.",
  "original_records_immutable": true,
  "strict_blind_performance_note": "신규78사례모두과거노출unknown또는확인노출로엄격blind성공실적에서제외.최초답과사후판정수정시점을유지."
}
```
