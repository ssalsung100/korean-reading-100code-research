# Corpus Gap Audit

> 기계적 corpus 대조 보고서. 문항 풀이·100코드 판정·연구 의미 판단은 수행하지 않았다.

## Summary

- Target unique questions: 1,147
- Canonical: 1,710
- Already researched: 663
- Local source available: 4
- Local complete: 45 (KICE 문학 target 마더텅 원자료 중앙화 완료)
- Local partial: 0
- External download needed: 5
- Unresolved: 0
- Estimated exam packages to download: 1 (KICE 0 + LEET 1)
- KICE: 0 / LEET: 1 / MEET/DEET: 0 / Other: 0

## Target universe

- `target_source`: `data/기본기_연구/code_study_candidates_v2.jsonl`
- 원장 행 수 1,147건, dedup 후 1,147건. 중복 0건.
- `deduplication_rule`: `canonical_connection.question_id`; absent key는 `exam_family + year + exam_type + question_number`.
- `data/sdss_100codes_catalog.json`의 `unique_question_count: 1147`와 실제 원장 재계산값이 일치한다.

## Canonical corpus

| family | canonical questions | passages/groups |
|---|---:|---:|
| KICE | 700 | 169 passages |
| LEET | 630 | canonical 홀수형 manifest 기준 |
| MEET/DEET | 380 | 125 groups |
| Other | 0 | — |
| **Total** | **1,710** | — |

KICE는 `data/kice_passages.jsonl`·`data/kice_questions.jsonl`, MEET는 `data/meet_passages.jsonl`·`data/meet_questions.jsonl`, LEET는 `자료/LEET_언어이해/검증/텍스트_전수검증_v1.json`의 `question_odd` canonical record를 기준으로 세었다.

## Target ↔ canonical status

| status | count | 기계 판정 |
|---|---:|---|
| CANONICAL_READY | 1,093 | exact canonical connection |
| LOCAL_SOURCE_AVAILABLE | 4 | 2016 KICE B형 문제·정답 원본 묶음 로컬 보유 |
| LOCAL_COMPLETE | 45 | KICE 문학 target; 외부 마더텅 HWPX 원문 중앙화 완료 |
| LOCAL_PARTIAL | 0 | — |
| EXTERNAL_SOURCE_NEEDED | 5 | 2008 LEET 예비시험 충분한 원자료 미확인 |
| TARGET_MAPPING_UNRESOLVED | 0 | — |

## Reconciliation

`TARGET_UNIQUE = CANONICAL_READY + LOCAL_SOURCE_AVAILABLE + LOCAL_COMPLETE + LOCAL_PARTIAL + EXTERNAL_SOURCE_NEEDED + TARGET_MAPPING_UNRESOLVED`

`1,147 = 1,093 + 4 + 45 + 0 + 5 + 0` — 성립.

기존 답안표-only 상태였던 KICE 문학 45문항은 외부 마더텅 국어 문학 HWPX에서 문제 원문을 확인하고 중앙화했다. 45문항은 `LOCAL_COMPLETE`로 승격했으며 KICE 다운로드 패키지는 모두 제거했다. 2008 LEET 예비시험만 충분한 원자료가 확인되지 않은 외부 원자료 필요 상태다.

## KICE 문학 source 재감사 (2026-09-20)

대상은 45문항이다. 프로젝트 루트의 독서 HWPX만 보았던 이전 판정을 폐기하고 외부 마더텅 문학 폴더의 HWPX 7개와 추출 MD 8개를 전수 조사했다. 내부 표지와 문항 범위에서 대상 학년도·시험을 확인했고, 각 target의 지문·발문·선지·보기 원문을 중앙 MD로 옮겼다.

| 학년도 | 시험 | 대상 | source 상태 | 중앙 MD | 추가 다운로드 |
|---:|---|---:|---|---|---|
| 2026 | 수능 | Q18–34 | LOCAL_COMPLETE | 중앙 MD 4개 | 없음 |
| 2024 | 수능 | Q22–29, Q32 | LOCAL_COMPLETE | 중앙 MD 3개 | 없음 |
| 2023 | 수능 | Q31–34 | LOCAL_COMPLETE | 중앙 MD 1개 | 없음 |
| 2023 | 9월 모평 | Q28–31 | LOCAL_COMPLETE | 중앙 MD 1개 | 없음 |
| 2023 | 6월 모평 | Q32–34 | LOCAL_COMPLETE | 중앙 MD 1개 | 없음 |
| 2022 | 수능 | Q28–31 | LOCAL_COMPLETE | 중앙 MD 1개 | 없음 |
| 2021 | 수능 | Q43 | LOCAL_COMPLETE | Q43–45 중앙 블록 | 없음 |
| 2020 | 수능 | Q43–45 | LOCAL_COMPLETE | 중앙 MD 1개 | 없음 |

문항별 `candidate_id`·source path·SHA-256·중앙 MD·정답 source·preparation 상태는 `data/corpus_ingest/kice_literature_local_audit_target_mapping.json`, 상세 조사 근거는 `data/corpus_ingest/KICE_LITERATURE_MOTHERTONG_INGEST.md`에 저장했다. 문학을 독서 canonical schema에 강제하지 않고 `LITERATURE_CANONICAL_SCHEMA_NEEDED`로 남겼다.

## Year / exam coverage

| family | 학년도 | 시험 | target | canonical | local_ingestable | external_needed | unresolved | local_partial | missing q |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| KICE | 2014 | 6평국어A형 | 2 | 2 | 0 | 0 | 0 | 0 | — |
| KICE | 2015 | 수능국어B형 | 2 | 2 | 0 | 0 | 0 | 0 | — |
| KICE | 2016 | 수능국어B형 | 4 | 0 | 4 | 0 | 0 | 0 | — |
| KICE | 2020 | 6평국어 | 1 | 1 | 0 | 0 | 0 | 0 | — |
| KICE | 2020 | 수능국어 | 17 | 14 | 3 | 0 | 0 | 0 | — |
| KICE | 2021 | 수능국어 | 16 | 15 | 1 | 0 | 0 | 0 | — |
| KICE | 2022 | 6평국어 | 4 | 4 | 0 | 0 | 0 | 0 | — |
| KICE | 2022 | 9평국어 | 4 | 4 | 0 | 0 | 0 | 0 | — |
| KICE | 2022 | 수능국어 | 18 | 14 | 4 | 0 | 0 | 0 | — |
| KICE | 2023 | 6평국어 | 11 | 8 | 3 | 0 | 0 | 0 | — |
| KICE | 2023 | 9평국어 | 18 | 14 | 4 | 0 | 0 | 0 | — |
| KICE | 2023 | 수능국어 | 18 | 14 | 4 | 0 | 0 | 0 | — |
| KICE | 2024 | 수능국어 | 26 | 17 | 9 | 0 | 0 | 0 | — |
| KICE | 2025 | 6평국어 | 10 | 10 | 0 | 0 | 0 | 0 | — |
| KICE | 2025 | 수능국어 | 17 | 17 | 0 | 0 | 0 | 0 | — |
| KICE | 2026 | 수능국어 | 34 | 17 | 17 | 0 | 0 | 0 | — |
| LEET | 2008 | 리트예비 | 5 | 0 | 0 | 5 | 0 | 0 | 4–8 |
| LEET | 2009–2026 | 리트언어 | 598 | 598 | 0 | 0 | 0 | 0 | — |
| LEET | 2009 | 리트예비 | 36 | 36 | 0 | 0 | 0 | 0 | — |
| MEET | 2005예비–2012 | 미트언어/예비 | 337 | 337 | 0 | 0 | 0 | 0 | — |

연도별 target/canonical 수는 target 원장과 canonical 연결 상태를 대조한 값이다. 같은 시험 회차의 여러 passage/question range는 하나의 다운로드 package로 묶었다.

## Research count distinction

현재 연구 완료 문항 수는 보호 대상 `data/기본기_연구/meta_state.json`의 `completed_questions_total = 663`이며 canonical corpus 수 1,710과 다른 개념이다. 보호 대상 파일과 기존 연구 판정은 수정하지 않았다.

## Audit safeguards

- queue/processed/meta_state 및 기존 blind/answer_check/independent_code/sdss_compare는 읽기만 했다.
- semantic research, 문항 풀이, 100코드 판정은 수행하지 않았다.
