# Research data index provenance 보강 v2 감사 보고서

작성일: 2026-10-07

## 재분류 결과

v1의 541 `unresolved`를 기존 537건 SDSS 비적용 감사와 case ID로 대조했다. 537건은 `research_case_target_crosswalk_v1.jsonl`의 `NON_TARGET_RESEARCH` 집합과 완전히 일치하므로 `not_applicable_non_sdss_research`로 분류했다. 남은 4건만 실제 unresolved로 유지했다.

| 상태 | 건수 |
|---|---:|
| complete provenance | 926 |
| not-applicable non-SDSS research | 537 |
| conflicting provenance | 204 |
| genuinely unresolved | 4 |
| **전체** | **1671** |

SDSS 적용성은 별도 축으로 기록했다. 태그 및 candidate provenance가 연결된 1,134건은 `linked`, 검증된 비적용 537건은 `not_applicable_non_sdss_research`다. `expected_but_missing` 0건, SDSS 적용성 `unresolved` 0건이다. 비적용 사례는 provenance incomplete 수에 포함하지 않는다.

## 실제 unresolved 후보 필드 감사

네 건은 모두 G508의 KICE 2016 수능국어B형 문항이다. 아래 두 필드가 실제 필수 결손이다. 다른 요청 필드는 모두 존재한다. `visual_supplements`는 네 건 모두 null이나 v1 기준 선택 필드이며, 해당 case에 연결된 시각 보충자료가 있다는 provenance는 없다.

| case_id | passage_group | 문항 | question_id | 필수 결손 | 선택 필드 미연결 |
|---|---|---:|---|---|---|
| BQJ | G508 | Q21 | `KICE-2016-수능국어B형-Q21-24-Q21` | `official_answer`, `official_answer_source` | `visual_supplements` (선택 필드, null) |
| BQK | G508 | Q22 | `KICE-2016-수능국어B형-Q21-24-Q22` | `official_answer`, `official_answer_source` | `visual_supplements` (선택 필드, null) |
| BQL | G508 | Q23 | `KICE-2016-수능국어B형-Q21-24-Q23` | `official_answer`, `official_answer_source` | `visual_supplements` (선택 필드, null) |
| BQM | G508 | Q24 | `KICE-2016-수능국어B형-Q21-24-Q24` | `official_answer`, `official_answer_source` | `visual_supplements` (선택 필드, null) |

네 건 모두 `exam_family`, `academic_year`, `exam_label`, `exam_type`, `question_number`, `question_id`, `passage_id`, `canonical_source_path`, `candidate_id`, `passage_group`이 확인된다. `site_original_codes`도 candidate provenance에 따라 존재해 SDSS applicability는 `linked`다. `official_answer_source_status`는 “not accessed during source preparation; resolve after group blind barrier”로 기록되어 있다. 공식 답을 보충하거나 봉인 자료를 열지 않았다.

## official answer 누락 집합 검증

- `official_answer` 값이 없는 case: 4건 (BQJ, BQK, BQL, BQM)
- genuinely unresolved: 4건 (BQJ, BQK, BQL, BQM)
- case ID 교집합: 4건 (BQJ, BQK, BQL, BQM)
- 두 집합이 완전히 같은가: **예**
- `official_answer_source` 값이 없는 case 집합도 동일: **예**

## conflict 별도 보존

204건은 `conflicting` 상태로 unresolved와 분리했다. v1의 `provenance_conflicts` 원 객체는 v2에서 전부 그대로 보존했다. field별 집계는 `exam_label` 197건, `canonical_source_path` 7건이다. 표기 차이를 임의 정규화하거나 source-path 충돌을 미해결 4건에 합치지 않았다.

## 방법과 보존 범위

- case ID 집합으로만 non-SDSS 감사 JSONL과 crosswalk를 대조했다.
- v1의 provenance scalar, evidence, conflicts, passage/group, stage 데이터는 그대로 복사하고 새 상태 필드만 추가했다.
- visual supplements와 exam_type은 v1 보고서 기준 선택 필드다. null 상태는 `provenance_optional_unavailable_fields`로 표시하며 unresolved 사유로 계산하지 않았다.
- 기존 입력 파일, manifest, semantic raw queue/processed, `meta_state`는 수정하지 않았다.

## 입력 SHA-256

- v1 enriched index: `4eea7dfa54d83253bd93c40923eb8ee13e52d57e7e68074d6a910ca0914ea806`
- 기존 537건 audit JSONL: `49499ac49bc8637bf29e2997c787442c9d0744a07d302a82bc9453ec0d886e99`
- research target crosswalk: `8873723f785013348bf5f8400c47b2b82071a8345b763d413aecab93618a8d9c`

산출물: `data/기본기_연구/research_data_index_enriched_v2.json`
