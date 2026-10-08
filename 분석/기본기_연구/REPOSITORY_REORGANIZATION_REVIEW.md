# 저장소 재구성 2차 검토

작성일: 2026-10-06  
범위: 1차 inventory/index/계획/보고서의 검증, 참조 후보 재분류, 이동 위험도 및 최종 migration map 작성. 실제 `mv`/rename/delete/reference rewrite는 수행하지 않았다. 기존 production 파일 및 연구 원장은 변경하지 않았다.

## 1. 요약

- 725개 missing/dangling 후보: `documentation/example` 533, `historical_reference` 121, `provenance_reference` 54, `parser_false_positive` 16, `unresolved` 1.
- `real_broken_reference`: **0건 확인**. 스크립트에서 발견된 구형 `.json` 토큰은 실행부가 현행 `.jsonl` 파일을 사용하거나 문서/출처 문자열로만 나타났다. 현행 파일을 요구하는데 그 파일이 없다는 증거가 확인된 후보는 없었다.
- 파일 위험도(1차 inventory 10,177 항목 기준): SAFE 2,264, CONDITIONAL 1,688, DO_NOT_MOVE 6,225.
- 실제 이동 권고: **0개**. 현 위치 유지: **10,177개**. review 전용 migration map의 각 항목에서 `proposed_path=null`로 기록했다.
- 수동 확인: 유일 unresolved 후보 1건과 16개 parser false positive의 원문 위치를 필요 시 확인한다. 54 provenance 경로는 출처·구버전 명칭의 보존 목적을 지우지 않도록 이동/정리 전에 담당자가 의미를 확인해야 한다. 이는 이 단계에서 이동 제안으로 승격하지 않는다.

## 2. 후보 분류 및 판정 기준

전체 후보별 `from`, 원 토큰, 분류, evidence, confidence, target 존재 여부 및 실행 dereference 판정은 [reference_validation.json](../../data/기본기_연구/reference_validation.json)에 보존했다.

| 분류 | 수 | 판정 근거 |
|---|---:|---|
| A. real_broken_reference | 0 | 실행 가능한 production 입력/출력 경로가 특정되어야 한다. 누락 토큰이 있다는 이유만으로 지정하지 않았다. |
| B. historical_reference | 121 | 과거 CURRENT, 복구, audit, cycle/recovery 로그 등에 기록된 경로 문자열. 현재 runtime dependency로 확인되지 않았다. |
| C. provenance_reference | 54 | 구형 source path/확장자 표기 또는 script의 출처 메타데이터. 현행 canonical `.jsonl`이 별도로 확인된 경우 이를 명시했다. |
| D. documentation/example | 533 | Markdown·운영 지침·prompt 등 설명 텍스트. production dereference 증거 없음. |
| E. generated/temporary_reference | 0 | 후보의 source/token에서 `/tmp`, 임시 또는 진단 output임이 확인되는 항목 없음. |
| F. parser_false_positive | 16 | 한 토큰 안에 복수 경로 조각이 결합되거나 공백을 포함해 단일 경로로 해석할 수 없는 항목. |
| G. unresolved | 1 | 실행 여부 또는 경로 의미를 후보 metadata만으로 확정하지 못함. 수동 문맥 확인 대상으로 남김. |

총계 725. `real_broken_reference` 0은 저장소 전체의 무결성을 절대 보증한다는 뜻이 아니라, 주어진 725 후보 중 현재 실행 경로가 exact missing local file을 실제 요구한다는 사례가 입증되지 않았다는 뜻이다. 1차 inventory에는 줄 번호가 없어 일부 판정은 source 유형과 script 경로 사용을 결합한 평가다. 수동 검토 시 원문 줄 문맥이 우선한다.

## 3. authoritative hierarchy

| 계층 | authoritative source | derived copy / 재생성 가능 자료 |
|---|---|---|
| canonical question/source | 현행 정본 question/passage 원장 및 연결된 원본 시험 자료. 현 저장소의 주요 KICE 정본은 `data/kice_questions.jsonl`, `data/kice_passages.jsonl`; 각 case의 `source_path`/source ID가 특정하는 시험 원문이 우선 | question views, candidate/index 출력, OCR·정규화·렌더 자료. 원본으로 승격하지 않는다. |
| official answer | 원문 시험의 공식 정답표/공식 source. 기존 정본 레코드에서는 provenance가 명시된 official answer field가 연결점 | 별도 인덱스/요약·해설의 정답 표기. 원문 정답표를 대체하지 않는다. |
| blind source | `manifest.jsonl`의 `blind_source`가 지정한 `prepared_backlog/blind_sources/` case 파일 | OCR 추출·question view 및 복사본. blind 입력 원장으로 취급하지 않는다. |
| sealed answer/SDSS | `prepared_backlog/sealed/answer_sdss.jsonl`와 source restoration ledger 등 sealed 원본 파일 | 검색·분석 index, reflected SDSS 비교 문서. 분리 정책상 blind barrier 완료 전 열람 금지. |
| semantic raw queue | `data/기본기_연구/astra_handoff_queue.jsonl` (append-only authoritative raw ledger) | 별도 파생물이 원장의 대체물이 될 수 없다. |
| processed ledger | `data/기본기_연구/astra_handoff_processed.jsonl`, queue `record_id`를 가리키는 처리 상태 원장 | 처리 통계/감사 요약. queue의 의미를 수정하지 않는다. |
| reflected Markdown | 기존 연구 기록 Markdown은 읽기 편한 반영·서술본. queue보다 의미 우선순위가 낮으며 원장 자체를 대체하지 않는다 | Markdown은 raw record로부터의 reflection; 수동 편집 문맥은 보존하되 재생성 여부는 문서별로 확인한다. |
| CURRENT | `분석/기본기_연구/CURRENT.md`는 재개/상태 안내의 현행 operational summary | queue·processed·manifest·meta_state에 의해 검증되는 요약. 독립 의미 원장으로 간주하지 않는다. |
| meta_state | `data/기본기_연구/meta_state.json`의 현재 barrier/counter/hold 상태 | 보고서의 진행률 복사본. 원본 상태를 대체하지 않는다. |
| manifest | `data/기본기_연구/prepared_backlog/manifest.jsonl`의 case별 순서·group·blind source·release status | research_data_index 및 통계/탐색 index는 파생 인덱스. manifest를 재생성·정렬하면 안 된다. |
| provenance/restoration | sealed source restoration ledger, 원본 시험자료 및 기존 source/path metadata | 복구 출력, 정규화본, 렌더본, 경로 요약. byte-identical이어도 역할/provenance가 다르면 합치거나 삭제 후보로 삼지 않는다. |

같은 사실이 여러 파일에 있을 때 raw/source/control 계층을 우선한다. research_data_index와 inventory는 안내용 파생물이며, 이 2차 검토에서 기존 산출물은 덮어쓰지 않았다.

## 4. 이동 위험도 및 최종 map

상세 10,177 항목은 [repository_migration_map.json](../../data/기본기_연구/repository_migration_map.json)에 기록했다.

- **SAFE 2,264**: inventory상 authoritative/control이 아니고 연결 참조도 관측되지 않은 항목. SAFE는 이동 승인 자체가 아니다. 목적지 편익이 불명확해 모두 `proposed_path=null`, `keep_in_place` 취급이다.
- **CONDITIONAL 1,688**: 참조자가 있어 이동한다면 migration map과 기계적 rewrite, 검증이 필요하다. 이 작업은 구체적 목적지와 검증 경로가 정당화되지 않아 이동 제안하지 않는다.
- **DO_NOT_MOVE 6,225**: 원장/현재 상태, blind/sealed 경계, provenance/restoration, authoritative 항목 또는 다중 참조 자산. 특히 queue/processed, manifest, meta_state, active blind/sealed material은 현재 경로를 유지한다.

권고 구조는 기존 연구 시스템 경로를 보존하고 inventory/index로 논리 구조를 제공하는 것이다. 디렉터리 미관을 위한 이동 편익이 참조 갱신·blind/sealed 혼선·provenance 단절 위험을 상회하지 않는다.

## 5. 중복 후보

1차 SHA-256 완전 동일 9개 그룹은 개별 유지한다. review JSON에 각 그룹의 `keep_all_in_place`와 근거를 남겼다. packet 파일은 서로 다른 case ID의 blind source 역할일 수 있고, `KB_diagram.png`/`KB_image14.png`는 blind source 내 연결 역할을 가질 수 있으며, cxresearch backup은 과거 복구 provenance를 갖는다. byte identity만으로 삭제하지 않는다. 16MB 초과 자료의 무차별 재해시는 하지 않았다.

## 6. 불변 검증

검토 중 산출한 기준값은 [reference_validation.json](../../data/기본기_연구/reference_validation.json)의 `baseline_invariants`에 기록했다.

- queue: SHA-256 `74b1e630ddb3808a1fc25d5d047514b8558ddd8f271d1d41a5d629fd568b4195`, 7,605 rows.
- processed: SHA-256 `c49e67a393b517671b94b6e0267689f8250fe55f6d4f2cd38e0cd954ef311818`, 7,605 rows.
- queue `record_id` 대 processed `source_record_id`: pending 0, duplicate 0, orphan 0.
- manifest: 1,671 rows; `consumed_sdss` 1,663, `prepared` 8. case/status snapshot은 JSON에 보존.
- meta_state SHA-256와 hold 4건의 전문도 JSON에 보존했다. G024/G370 hold는 해소하거나 의미를 수정하지 않았다.
- 요청 범위의 불변 파일은 생성 전후 동일 hash/row count를 확인했다.

## 7. 사람 확인 항목

1. reference_validation의 unresolved 한 항목의 source 원문 문맥과 호출 여부.
2. parser false positive 16건 중 향후 자동 migration 후보로 고려할 토큰이 있다면 원문 line을 확인해 개별 reference로 분해할 것.
3. provenance 54건 또는 중복 hash 그룹을 향후 이동/정리하려면 원본 출처, 역할, case linkage를 담당자가 확인할 것.
4. SAFE 분류는 참조 스캐너가 찾지 못한 외부/동적 경로까지 부재한다고 증명하지 않는다. 이동 전에는 해당 자산의 생성·소비 entrypoint를 확인할 것.

## 8. 범위 종료

이 산출물은 review와 migration plan이다. 실제 이동, rename, delete, reference rewrite는 수행하지 않았다. 다음 단계에서 실제 변경을 승인받더라도, 우선 이동 대상이 0개인 현 계획 자체를 기준으로 재검토해야 한다.
