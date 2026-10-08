# 평가원형 기본기 연구 저장소 안내

이 안내서는 저장소를 처음 보는 사람이 연구 자료의 권위 순서와 case 탐색 경로를 빠르게 찾도록 돕는다. 디렉터리 이동 대신 현재 연구 시스템과 blind/sealed 경계를 유지한다.

## 5분 구조 안내

- `자료/`: 시험 원본, 스캔/OCR, 렌더, 검수 및 출처·복원 자료.
- `data/기본기_연구/`: prepared blind input, sealed answer/SDSS, 원장, manifest, case별 reflected 풀이, index와 자동화 상태.
- `분석/기본기_연구/`: 진행 상태·절차·기준·종합 기록과 저장소 유지보수 안내.
- `scripts/`: 연구 원장 반영, backlog 준비, 검사 및 자료 생성 도구.
- 루트의 `AGENTS.md`, 인수인계 문서와 `DB_자산_인덱스.md`: 작업 규칙과 상위 자료 안내. 상세 사실은 아래의 원장과 출처를 확인한다.

## 빠른 탐색표

| 목적 | 시작 경로 | 참고 |
|---|---|---|
| 현재 연구 진행 상태 | `분석/기본기_연구/CURRENT.md` | 요약 상태. 원장과 manifest로 확인한다. |
| 특정 case 찾기 | `data/기본기_연구/research_data_index.json` → `case_to_group` | case ID에서 group, blind source, stage record ID와 대상 문서를 찾는다. |
| 특정 passage_group 찾기 | 같은 JSON의 `passage_groups` | group에서 case ID 목록으로 이동한다. |
| 특정 시험/연도/문항 찾기 | `data/kice_questions.jsonl`, LEET/MEET 정본 인덱스와 `자료/` | research index의 시험 식별 필드는 대부분 비어 있어 index만으로는 찾을 수 없다. source ID와 원본을 교차 확인한다. |
| 최초 blind 풀이 보기 | `data/기본기_연구/독립풀이_04/{CASE}_01_최초풀이.md` | 과거 연구는 `독립풀이_03/`. index의 blind stage target 우선. |
| 정답 대조 보기 | `독립풀이_04/{CASE}_02_정답대조와_독립코드.md` | answer_check와 독립 코드가 한 문서에 반영된 경우가 많다. |
| 독립 코드 판정 보기 | 위 정답대조 문서와 queue의 `independent_code` record | 상세 반영 문서의 경쟁 코드·판정 근거를 확인한다. |
| SDSS 대조 보기 | `독립풀이_04/{CASE}_03_SDSS대조.md` | raw `sdss_compare`와 함께 확인한다. |
| induction/meta/audit 보기 | `분석/기본기_연구/독립연구_04_절차와_진행기록.md`, 관련 기준·audit 문서, queue stage | case index에는 개별 induction/audit coverage가 제한적으로만 연결된다. |
| 원본 문제지/정답표 찾기 | `자료/`의 시험별 원본과 검수완료 자료; 정본 JSONL의 `source_path`/source ID | 정답은 공식 정답표를 기준으로 provenance를 확인한다. |
| hold 상태 확인 | `data/기본기_연구/meta_state.json`의 holds, index `holds`, `CURRENT.md` | G024/G370 hold는 원문과 원래 사유를 함께 본다. |
| 새 후속 연구 준비 | `AGENTS.md`, `분석/기본기_연구/ASTRA_START.md`, `CURRENT.md`, `prepared_backlog/manifest.jsonl` | 새 판단은 절차·group barrier를 따르고 raw queue에 먼저 보존한다. |

## 연구 자료 authoritative hierarchy

| 대상 | Authoritative | Derived / 탐색용 | 직접 수정 가능 여부 |
|---|---|---|---|
| 1. canonical/original question source | `data/kice_questions.jsonl`, `data/kice_passages.jsonl` 및 case의 source ID/path가 가리키는 공식 시험 원문. LEET/MEET은 해당 정본·검수완료 원문 연결 | OCR, 정규화본, 시각자료 catalogue, question views, candidate index | 원본 파일을 직접 고치지 않는다. 정정은 출처·정본 절차에 따라 별도 검수한다. |
| 2. blind research source | `prepared_backlog/manifest.jsonl`의 `blind_source`가 가리키는 `data/기본기_연구/prepared_backlog/blind_sources/` 파일 | 추출 텍스트, packet, case 안내 index | 내용/연결을 임의로 수정하지 않는다. blind 결과는 raw 기록 절차를 따른다. |
| 3. official answer | 시험기관의 공식 정답표/원문. case에 대해 봉인된 official answer field와 source provenance 연결은 `prepared_backlog/sealed/answer_sdss.jsonl` 및 정본 question source에 기록 | 해설·색인·반영 풀이의 답 표기 | 봉인 answer 원장은 직접 수정하지 않는다. 답 수정은 공식 출처를 재검증해 통제된 append/recovery 절차를 따른다. |
| 4. sealed SDSS/site tag | `prepared_backlog/sealed/answer_sdss.jsonl`의 SDSS/site tag 필드와 연계 provenance | 반영된 SDSS 대조문, 요약/index | 직접 수정하지 않는다. 해당 group의 모든 blind 및 independent_code barrier 뒤에만 공개한다. |
| 5. Astra semantic raw | `data/기본기_연구/astra_handoff_queue.jsonl` | reflected 문서와 통계 | 기존 행 수정·삭제·재정렬 금지. 신규 판단은 append-only 절차로 기록한다. |
| 6. processed ledger | `data/기본기_연구/astra_handoff_processed.jsonl`의 `source_record_id` 처리 추적 | 처리율·checkpoint 요약 | 직접 편집하지 않는다. Luna 처리·복구 절차가 관리한다. |
| 7. 사람이 읽는 reflected 풀이 | `data/기본기_연구/독립풀이_04/` 및 과거 `독립풀이_03/` | queue raw의 읽기 쉬운 반영본 | 절차상 Luna가 반영한다. 의미 수정이 필요하면 raw 판정과 함께 검토한다. |
| 8. manifest | `data/기본기_연구/prepared_backlog/manifest.jsonl` | `research_data_index.json`의 group/case 안내 | 직접 편집·정렬·재생성 금지. prepared/consumed 상태와 barrier의 operational 원장이다. |
| 9. meta_state | `data/기본기_연구/meta_state.json` | CURRENT/보고서의 상태 요약 | 직접 편집 금지. 전용 상태관리 절차로 갱신한다. |
| 10. CURRENT | `분석/기본기_연구/CURRENT.md` | 시작 안내 및 다음 frontier 요약 | 기본적으로 Luna가 관리한다. queue/manifest/meta_state와 불일치하면 원장을 따른다. |
| 11. provenance/restoration | 공식 시험 원문, `prepared_backlog/sealed/` provenance/restoration ledger, 검수완료 source manifest | 복원 출력·OCR·렌더·crosswalk | 출처·원래 경로의 증거이므로 직접 덮어쓰거나 삭제하지 않는다. 복원은 전용 절차로 별도 기록한다. |

`SDSS`는 제3자 후보 색인이지 정답의 권위자가 아니다. 정답은 공식 원문·정답표의 provenance를 기준으로 본다.

## Blind / sealed 경계

해당 passage group의 blind raw record 전체가 저장되기 전에는 다음을 열지 않는다: `prepared_backlog/sealed/answer_sdss.jsonl`, `source_restorations`/provenance sealed 파일, 원래 `data/kice_questions.jsonl`의 정답 필드, 후속 candidate index, 기존 해설·독립 코드 판정, SDSS 반영문. 같은 group의 모든 blind raw 저장 후 group 전체 answer_check를 진행하고, 이어 group 전체 independent_code를 완료한 뒤에만 SDSS를 공개한다. 한 case의 SDSS를 먼저 본 뒤 같은 group의 다른 case를 독립 판정하지 않는다. 준비된 blind-only source는 manifest가 지정한 파일만 사용한다.

## 절대 직접 수정하지 말 것

- `data/기본기_연구/astra_handoff_queue.jsonl`
- `data/기본기_연구/astra_handoff_processed.jsonl`
- `data/기본기_연구/prepared_backlog/manifest.jsonl`
- `data/기본기_연구/meta_state.json`
- `prepared_backlog/blind_sources/`와 `prepared_backlog/sealed/`의 active source/answer/provenance
- migration map에서 `DO_NOT_MOVE`로 지정된 authoritative, control, blind/sealed, provenance 핵심 파일

이 목록은 변경 요청이 있어도 기존 기록을 덮어쓰는 방식으로 수정하지 말라는 뜻이다. 새 판단과 상태 변화는 정해진 append/processing 절차를 사용한다.

## 1·2차 repository maintenance 산출물

| 파일 | 용도 | 주 사용자 |
|---|---|---|
| `분석/기본기_연구/REPOSITORY_REORGANIZATION_PLAN.md` | 1차 inventory 범위·분류·중복 및 dangling 발견 내역 | 사람 |
| `분석/기본기_연구/REPOSITORY_REORGANIZATION_REPORT.md` | 1차 불변성·작업 범위 기록 | 사람 |
| `분석/기본기_연구/RESEARCH_DATA_INDEX.md` | JSON index의 사람이 읽는 설명 | 사람 |
| `분석/기본기_연구/REPOSITORY_REORGANIZATION_REVIEW.md` | 725 후보 재분류, hierarchy 및 위험도 판정 | 사람 |
| `data/기본기_연구/repository_inventory.json` | 파일/hash/reference/중복 inventory 원본 | 자동화 우선, 사람 검토 가능 |
| `data/기본기_연구/research_data_index.json` | case/group/stage/source/target의 field-level 탐색 index | 자동화 우선, 사람·후속 작업도 사용 |
| `data/기본기_연구/repository_migration_map.json` | 이동 위험도와 현재 경로 유지 판정; 이번 map의 실제 move 권고는 0 | 자동화·감사 |
| `data/기본기_연구/reference_validation.json` | 725 reference 분류, evidence와 최종 unresolved 해소 | 자동화·감사 |
| `data/기본기_연구/archive_candidates.json` | 삭제/이동 없이 보존 검토만 할 후보 목록 | 자동화·감사 |
| `분석/기본기_연구/REPOSITORY_MAINTENANCE_FINAL.md` | 3차 최종 정리·불변 검증 요약 | 사람 |

Index/inventory/migration/reference 결과는 파생 산출물이다. 수동으로 authoritative 원장을 대체하거나 원본 의미를 보정하지 않는다. 갱신 시 원자료에서 재생성하고 이전 결과와 diff를 확인한다.
