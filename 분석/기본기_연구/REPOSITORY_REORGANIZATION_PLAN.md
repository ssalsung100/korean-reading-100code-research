# 저장소 자료 재구성 계획

작성일: 2026-10-06. 이번 산출물은 inventory/index/계획/보고서뿐이며 기존 자료의 이동·이름변경·삭제·참조 수정은 수행하지 않았다.

## 1. 현재 구조 개요

- 스캔 범위: `data/기본기_연구/`, `분석/기본기_연구/`, `자료/`, `scripts/`, 루트의 Markdown/JSON/JSONL/스크립트 파일. 실제 파일 수 15,452, inventory 항목/파일군 10,177, 총 계량 가능 크기 169,058,151 bytes.
- 범주별 파일 수: A=343, B=2,245, C=3,408, E=3,983, F=170, G=28
.
- 주요 하위 트리는 원본·렌더(`자료/`), blind input 및 sealed/ledger(`data/기본기_연구/`), 반영 연구 기록·재개 상태(`분석/기본기_연구/`), 경로 소비 script(`scripts/`)로 분산되어 있다.

## 2. 파일 종류별 개수

- `.bak-20261002-230430`: 2
- `.bak-before-factchat`: 1
- `.bmp`: 35
- `.html`: 1
- `.hwp`: 17
- `.jpeg`: 19
- `.jpg`: 53
- `.json`: 2,230
- `.jsonl`: 16
- `.lock`: 1
- `.md`: 7,295
- `.mjs`: 3
- `.mp3`: 4
- `.pdf`: 30
- `.png`: 246
- `.ps1`: 8
- `.py`: 99
- `.pyc`: 72
- `.svg`: 2
- `.tif`: 29
- `.tiff`: 1
- `.tsv`: 1
- `.xml`: 1
- `.zip`: 5
- `[no extension]`: 6

## 3. authoritative source 목록

- `AGENTS.md`
- `분석/기본기_연구/CURRENT.md`
- `분석/기본기_연구/ASTRA_START.md`
- `data/기본기_연구/meta_state.json`
- `data/기본기_연구/prepared_backlog/manifest.jsonl`
- `data/기본기_연구/astra_handoff_queue.jsonl`
- `data/기본기_연구/astra_handoff_processed.jsonl`
- manifest의 `blind_source`, queue payload의 `answer_source`/`sourceID`, 원본 시험 자료 경로는 각각 해당 case의 참조 필드가 가리키는 자산이 authoritative 연결점이다. 이 보고서는 필드를 재해석하지 않았다.

## 4. derived/copied/cache/diagnostic 구분

- derived: `분석/기본기_연구/` 반영문서와 CURRENT, manifest/queue를 사람이 탐색하도록 요약한 산출물.
- control: manifest, queue, processed, meta_state 및 복구·검증용 script. 원장을 재생성하거나 재정렬하면 안 된다.
- 원본/가공본: `자료/` 원본과 페이지 렌더/정규화 텍스트가 공존한다. 출처 ledger 및 script 연결을 확인하기 전 이동 금지.
- cache/diagnostic/historical: 파일명만으로 확정 가능한 항목이 적으므로 개별 후보는 inventory의 low confidence 분류로 남겼다.

## 5. 중복 후보

- 완전 동일 SHA-256 파일군 9개: data/기본기_연구/prepared_backlog/blind_sources/KB_diagram.png = data/기본기_연구/prepared_backlog/blind_sources/KB_image14.png; data/기본기_연구/prepared_backlog/packets/BQN.md = data/기본기_연구/prepared_backlog/packets/BQO.md = data/기본기_연구/prepared_backlog/packets/BQP.md; data/기본기_연구/prepared_backlog/packets/BQQ.md = data/기본기_연구/prepared_backlog/packets/BQR.md = data/기본기_연구/prepared_backlog/packets/BQS.md; data/기본기_연구/prepared_backlog/packets/BQT.md = data/기본기_연구/prepared_backlog/packets/BQU.md = data/기본기_연구/prepared_backlog/packets/BQV.md; data/기본기_연구/prepared_backlog/packets/BQW.md = data/기본기_연구/prepared_backlog/packets/BQX.md = data/기본기_연구/prepared_backlog/packets/BQY.md; data/기본기_연구/prepared_backlog/packets/BQZ.md = data/기본기_연구/prepared_backlog/packets/BRA.md; data/기본기_연구/prepared_backlog/packets/BRB.md = data/기본기_연구/prepared_backlog/packets/BRC.md = data/기본기_연구/prepared_backlog/packets/BRD.md; data/기본기_연구/prepared_backlog/packets/BRE.md = data/기본기_연구/prepared_backlog/packets/BRF.md = data/기본기_연구/prepared_backlog/packets/BRG.md; scripts/cxresearch = scripts/cxresearch.bak-20261002-230430

같은 basename·비슷한 크기만으로 중복을 선언하지 않았다. 전체 경로별 크기/hash는 inventory에 기록했다.

## 6. dangling reference 후보

- 텍스트 corpus에서 파일 경로 형태로 보이나 스캔 파일/파일시스템에서 찾지 못한 토큰 725개. 이들은 템플릿, 과거 경로, 절대 경로 일부일 수 있어 자동 수정 대상이 아니다.
- `AGENTS.md` → `data/kice_questions.json`
- `AGENTS.md` → `data/기본기_연구/astra_handoff_queue.json`
- `AGENTS.md` → `data/기본기_연구/prepared_backlog/manifest.json`
- `DB_자산_인덱스.md` → `data/code_candidate_review_queue.json`
- `DB_자산_인덱스.md` → `data/code_candidate_review_queue_by_code.json`
- `DB_자산_인덱스.md` → `data/kice_passages.json`
- `DB_자산_인덱스.md` → `data/kice_questions.json`
- `DB_자산_인덱스.md` → `data/meet_passages.json`
- `DB_자산_인덱스.md` → `data/meet_passages_raw.json`
- `DB_자산_인덱스.md` → `data/meet_questions.json`
- `DB_자산_인덱스.md` → `data/meet_questions_raw.json`
- `DB_자산_인덱스.md` → `data/meet_visuals.json`
- `DB_자산_인덱스.md` → `data/sdss_indexed_questions.json`
- `data/기본기_연구/astra_handoff_processed.jsonl` → `data/기본기_연구/astra_handoff_queue.json`
- `data/기본기_연구/astra_handoff_processed.jsonl` → `data/기본기_연구/독립연구_04_절차와_진행기록.md`
- `data/기본기_연구/code_reviews_01.jsonl` → `data/kice_passages.json`
- `data/기본기_연구/code_reviews_01.jsonl` → `data/kice_questions.json`
- `data/기본기_연구/code_reviews_02.jsonl` → `data/kice_questions.json`
- `data/기본기_연구/code_study_candidates_v2.jsonl` → `data/kice_questions.json`
- `data/기본기_연구/code_study_candidates_v2.jsonl` → `data/meet_questions.json`
- `data/기본기_연구/code_study_candidates_v2.jsonl` → `data/meet_questions_raw.json`
- `data/기본기_연구/code_study_coverage_v2.json` → `data/code_candidate_review_queue.json`
- `data/기본기_연구/code_study_coverage_v2.json` → `data/kice_questions.json`
- `data/기본기_연구/code_study_coverage_v2.json` → `data/meet_questions.json`
- `data/기본기_연구/code_study_coverage_v2.json` → `data/meet_visuals.json`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `data/kice_passages.json`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `data/kice_questions.json`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `data/기본기_연구/astra_handoff_processed.json`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `data/기본기_연구/astra_handoff_queue.json`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `data/기본기_연구/prepared_backlog/blind_sources/BHA.json data/기본기_연구/prepared_backlog/blind_sources/BHB.json data/기본기_연구/prepared_backlog/blind_sources/BHC.json`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `data/기본기_연구/prepared_backlog/blind_sources/G426_visual02.md data/기본기_연구/prepared_backlog/blind_sources/G426_visual03.md`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `data/기본기_연구/prepared_backlog/manifest.json`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `data/기본기_연구/prepared_backlog/sealed/answer_sdss.json`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `data/기본기_연구/prepared_backlog/sealed/source_restorations_v1.json`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `data/기본기_연구/research_case_target_crosswalk_v1.json`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `data/기본기_연구/target_completion_crosswalk_v1.json`
- `data/기본기_연구/cxresearch_loop_logs/astra-turn-1-20261002-235041.jsonl` → `분석/기본기_연구/CURRENT.md 분석/기본기_연구/ASTRA_START.md`
- `data/기본기_연구/cxresearch_loop_logs/luna-recovery-20261002-234658.jsonl` → `data/kice_passages.json`
- `data/기본기_연구/cxresearch_loop_logs/luna-recovery-20261002-234658.jsonl` → `data/kice_questions.json`
- `data/기본기_연구/cxresearch_loop_logs/luna-recovery-20261002-234658.jsonl` → `data/meet_questions.json`
- `data/기본기_연구/cxresearch_loop_logs/luna-recovery-20261002-234658.jsonl` → `data/기본기_연구/astra_handoff_processed.json`
- `data/기본기_연구/cxresearch_loop_logs/luna-recovery-20261002-234658.jsonl` → `data/기본기_연구/astra_handoff_queue.json`
- `data/기본기_연구/cxresearch_loop_logs/luna-recovery-20261002-234658.jsonl` → `data/기본기_연구/prepared_backlog/manifest.json`
- `data/기본기_연구/cxresearch_loop_logs/luna-recovery-20261002-234658.jsonl` → `data/기본기_연구/research_case_target_crosswalk_v1.json`
- `data/기본기_연구/cxresearch_loop_logs/luna-recovery-20261002-234658.jsonl` → `data/기본기_연구/target_completion_crosswalk_v1.json`
- `data/기본기_연구/cxresearch_loop_logs/luna-recovery-20261002-234658.jsonl` → `data/기본기_연구/독립연구_04_절차와_진행기록.md`
- `data/기본기_연구/cxresearch_loop_logs/luna-recovery-20261002-234658.jsonl` → `분석/기본기_연구/CURRENT.md 분석/기본기_연구/LUNA_HANDOFF.md 분석/기본기_연구/LUNA_HANDOFF_START.md`
- `data/기본기_연구/cxresearch_loop_logs/luna-recovery-20261002-234658.jsonl` → `분석/기본기_연구/독립풀이_04/BHA_02_정답대조와_독립코드.md`
- `data/기본기_연구/cycle_logs/astra-20260909-234305.jsonl` → `data/kice_questions.json`
- `data/기본기_연구/cycle_logs/astra-20260909-234305.jsonl` → `data/기본기_연구/astra_handoff_queue.json`
- `data/기본기_연구/cycle_logs/astra-20260909-234305.jsonl` → `data/기본기_연구/prepared_backlog/blind_sources/AA.json data/기본기_연구/prepared_backlog/blind_sources/AB.json`
- `data/기본기_연구/cycle_logs/astra-20260909-234305.jsonl` → `data/기본기_연구/prepared_backlog/manifest.json`
- `data/기본기_연구/cycle_logs/astra-20260909-234305.jsonl` → `분석/기본기_연구/CURRENT.md 분석/기본기_연구/ASTRA_START.md`
- `data/기본기_연구/cycle_logs/astra-20260909-234305.jsonl` → `분석/기본기_연구/핵심8코드_경계와_판독기준_v1.md data/기본기_연구/코드군_통합가설_v1.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/kice_passages.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/kice_questions.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/meet_questions.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/meet_questions_raw.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/기본기_연구/astra_handoff_processed.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/기본기_연구/astra_handoff_processed.jsonl data/기본기_연구/prepared_backlog/manifest.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/기본기_연구/astra_handoff_queue.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/기본기_연구/astra_handoff_queue.jsonl data/기본기_연구/astra_handoff_processed.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/기본기_연구/code_reviews_01.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/기본기_연구/code_reviews_02.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/기본기_연구/code_study_candidates_v2.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/기본기_연구/cycle_logs/luna-20260909-234305.json`
- `data/기본기_연구/cycle_logs/luna-20260909-234305.jsonl` → `data/기본기_연구/prepared_backlog/manifest.json`
- `data/기본기_연구/prepared_backlog/LUNA_FRONTIER_PREFLIGHT_20260917.md` → `data/kice_passages.json`
- `data/기본기_연구/prepared_backlog/LUNA_FRONTIER_PREFLIGHT_20260917.md` → `data/kice_questions.json`
- `data/기본기_연구/prepared_backlog/LUNA_FRONTIER_PREFLIGHT_20260918.md` → `data/kice_passages.json`
- `data/기본기_연구/prepared_backlog/LUNA_FRONTIER_PREFLIGHT_20260918.md` → `data/kice_questions.json`
- `data/기본기_연구/prepared_backlog/LUNA_FRONTIER_PREFLIGHT_20260920.md` → `data/kice_passages.json`
- `data/기본기_연구/prepared_backlog/LUNA_FRONTIER_PREFLIGHT_20260920.md` → `data/kice_questions.json`
- `data/기본기_연구/prepared_backlog/blind_sources/BPY_ranges_supplement.json` → `data/기본기_연구/prepared_backlog/sealed/provenance_mapping.json`
- `data/기본기_연구/prepared_backlog/blind_sources/CH_choices_supplement.json` → `data/기본기_연구/prepared_backlog/sealed/provenance_mapping.json`
- `data/기본기_연구/prepared_backlog/blind_sources/G196_canonical_mapping_20260920.json` → `data/kice_passages.json`
- `data/기본기_연구/prepared_backlog/blind_sources/G197_canonical_mapping_20260920.json` → `data/kice_passages.json`
- `data/기본기_연구/prepared_backlog/blind_sources/G198_canonical_mapping_20260920.json` → `data/kice_passages.json`
- `data/기본기_연구/prepared_backlog/blind_sources/G199_canonical_mapping_20260920.json` → `data/kice_passages.json`
- `data/기본기_연구/prepared_backlog/blind_sources/G200_canonical_mapping_20260920.json` → `data/kice_passages.json`
- 전체 목록은 `repository_inventory.json`의 `dangling_reference_candidates`에 있다.

## 7. 이름 규칙이 불일치하는 파일군

- 연구자료는 `독립풀이_XX/CASE_단계.md`, 평면형 진행기록, 대소문자/밑줄을 섞은 source asset, 날짜 suffix를 가진 진단/복구물이 함께 존재한다.
- `blind_sources` case별 파일과 group source notice/visual supplement가 같은 디렉터리 규칙을 공유할 수 있으므로 파일명 정규화는 참조 확인 후 별도 작업으로 남긴다.

## 8. 추천 최종 디렉터리 구조 (제안, 미적용)

```text
자료/원본/{KICE,LEET,MEET_DEET}/{시험·연도}/
자료/정규화/{시험·연도}/
data/기본기_연구/blind/{case_id}/
data/기본기_연구/sealed/{시험·연도}/
data/기본기_연구/ledger/{queue,processed,manifest,state}/
data/기본기_연구/derived/{case_id,group_id}/
data/기본기_연구/diagnostics/
분석/기본기_연구/{CURRENT,기준,진행,반영자료}/
```

모든 이동은 후속 단계에서 참조 consumer 목록과 restore/verifier 영향을 검증한 뒤 별도 변경으로 한다.

## 9. 실제 이동 시 수정해야 할 script/reference 목록

- 경로 문자열 검색 corpus: `scripts/**`, `AGENTS.md`, `분석/기본기_연구/**`, `data/기본기_연구/**`; 전체 파일 관계는 inventory의 `references_from`/`references_to`에 기록.
- 핵심 연결: manifest `blind_source`, visual supplements, queue payload의 `answer_source`·provenance, processed `targets`, CURRENT 재개 위치, meta_state 계산/원장 탐색, verifier 및 source restore script.
- 현재 정확히 일치하는 경로 참조 기준으로 이동 영향은 inventory에서 파일별 확인한다. 참조 0건은 안전성 증거로 간주하지 않는다.

## 10. 절대 이동하면 안 되는 파일

- `astra_handoff_queue.jsonl`, `astra_handoff_processed.jsonl`, `prepared_backlog/manifest.jsonl`, `meta_state.json`은 기준 경로와 원문 hash를 고정 유지한다.
- 모든 `prepared_backlog/blind_sources/**`, sealed 답/SDSS/provenance 자산, 원본 출처/복원 ledger에서 authoritative인 원본.
- G024/G370 hold evidence/source 및 현재 CURRENT 재개 정보를 담은 파일.

## 11. 안전하게 바로 정리 가능한 파일

- 이번 1차 작업에는 기존 파일 중 이동·이름 변경·삭제·참조 변경을 바로 수행할 대상으로 지정하지 않았다. 요청된 신규 index와 보고 산출물만 추가했다.
- 동일 hash는 격리 후보로 제시 가능하나 실파일 변경은 별도 승인 가능한 검토 단계로 남긴다.

## 12. 사람이 확인해야 하는 애매한 파일

- `confidence=low` 또는 category G인 파일, hash 중복군, dangling 후보, 원본/렌더/정규화 텍스트의 연결이 자동 참조 문자열로 확인되지 않는 파일.
- unresolved holds: G024 DR/DS/DT/DU 및 G370 BAP/BAQ/BAR/BAS. 본 인덱스는 원장의 hold 내용만 연결하고 상태를 바꾸지 않는다.

## 기계적 기준선

- queue rows=7605, sha256=74b1e630ddb3808a1fc25d5d047514b8558ddd8f271d1d41a5d629fd568b4195; processed rows=7605, sha256=c49e67a393b517671b94b6e0267689f8250fe55f6d4f2cd38e0cd954ef311818.
- queue stage counts: answer_check=1689, blind=1674, boundary_revision=21, depth_backfill=89, hold=180, independent_code=1672, induction=388, manual_parity_audit=54, meta_induction=162, sdss_compare=1676
.
- pending=0, duplicate record_id=0, orphan processed=0.
- manifest cases=1671, status counts: consumed_sdss=1663, prepared=8.

