# Research data index provenance 보강 보고서

작성일: 2026-10-06

## 작업 범위

기존 `research_data_index.json`의 복사본을 바탕으로 저장소에 이미 존재하는 case-keyed provenance와 explicit candidate mapping만 기계적으로 연결했다. 의미 판단이나 누락값 추정은 하지 않았다. 기존 `research_data_index.json`, semantic raw queue/processed, manifest는 수정하지 않았다.

요청에 적힌 `target_completion_crosswalk_v1.json`과 `code_study_candidates_v2.json`은 현재 경로에 존재하지 않았다. 실제 현재 자료인 `.jsonl` 파일을 사용했다.

- `data/기본기_연구/prepared_backlog/manifest.jsonl`
- `data/기본기_연구/prepared_backlog/sealed/provenance_mapping.jsonl`
- `data/기본기_연구/prepared_backlog/sealed/answer_sdss.jsonl`
- `data/기본기_연구/prepared_backlog/sealed/source_restorations_v1.jsonl`
- `data/기본기_연구/target_completion_crosswalk_v1.jsonl`
- `data/기본기_연구/code_study_candidates_v2.jsonl`
- manifest가 가리키는 blind source JSON의 provenance/link 필드만
- 기존 `data/기본기_연구/research_data_index.json`

Join key는 명시된 `case_id`, `candidate_id`, `matched_case_id`, `case_ids`, `passage_group`이다. 파일 순서나 case ID 순번으로 값을 추론하지 않았다. blind source의 지문·발문·선지는 읽거나 index에 복사하지 않았으며, manifest 연결과 visual supplement 경로만 확인했다.

## Coverage

| 항목 | 결과 |
|---|---:|
| total cases | 1,671 |
| exam_family known | 1,671 |
| year (`academic_year`) known | 1,671 |
| question_number known | 1,671 |
| canonical source known | 1,082 |
| official answer known | 1,667 |
| official answer source known | 1,667 |
| SDSS/site original code known | 1,134 |
| complete provenance cases | 926 |
| conflicting provenance cases | 204 |
| unresolved cases | 541 |

추가로 `exam_label`은 conflict를 null 처리한 뒤 1,474건, `exam_type`은 1,165건에서 확인된다. `visual_supplements`는 출처에 명시된 연결만 case에 붙였으며, visual 자료가 없는 것을 결측 오류로 간주하지 않았다. sealed answer 원장의 “not accessed during source preparation” 문구는 source 경로로 세지 않고 상태로 보존했다. answer source 목록에는 서로 다른 출처 필드의 명시적 참조를 출처별로 보존했다.

### 집계 정의

- `complete provenance cases`: 아래 모든 필드가 존재하고 provenance conflict가 없는 case. `visual_supplements`와 `exam_type`은 선택 자료로 취급했다.
  - `exam_family`, `academic_year`, `exam_label`, `question_number`, `question_id`, `passage_id`, `canonical_source_path`, `candidate_id`, `official_answer`, `official_answer_source`, `site_original_codes`, `passage_group`
- `conflicting provenance cases`: 같은 index field에 대해 서로 다른 명시 값이 확인된 case. conflict field scalar는 null로 두고 모든 원 출처 claim을 `provenance_conflicts`에 기록했다.
- `unresolved cases`: conflict가 없지만 complete 기준 필드 하나 이상이 없는 case. 위 세 상태는 서로 겹치지 않으며 합계는 1,671이다.

충돌은 총 204 case다: `exam_label` 197, `canonical_source_path` 7. exam label은 다른 표기를 정규화하지 않았고, source path도 한쪽을 임의 선택하지 않았다. 이 두 conflict가 아닌 official answer, question ID/passage ID, year, question number, site original code 값에서는 서로 다른 명시 claim 충돌이 확인되지 않았다.

## Index 연결 무결성

새 index와 기존 index를 비교해 아래 항목이 case별로 동일함을 확인했다.

- case ID의 개수와 순서: 동일, 1,671건.
- `passage_group`, `group_case_ids`: 전 case 동일.
- 각 raw stage 객체 전체(`stage`, `record_id`, `processed`, `targets`): 전 case 동일.
- root의 `passage_groups`, `source_to_cases`, `holds`: 동일.
- G024/G370 hold: 기존 4개 record 그대로 유지.

enrichment은 case row에 provenance 필드, evidence, conflict를 추가했을 뿐 기존 raw-stage 연결을 고치지 않았다.

## 원장 불변 검증

이전 maintenance 기준과 비교했으며 모두 동일했다.

- queue: 7,605 rows; SHA-256 `74b1e630ddb3808a1fc25d5d047514b8558ddd8f271d1d41a5d629fd568b4195`.
- processed: 7,605 rows; SHA-256 `c49e67a393b517671b94b6e0267689f8250fe55f6d4f2cd38e0cd954ef311818`.
- manifest: 1,671 rows; SHA-256 `29bbdf41af019151d0342a846b3cfa48cec22142f41f24f5d895c4b8e4392e48`.
- meta_state SHA-256 `2ac212abe6f83b7d2e97f9b2ef0b706bca92bd8bda7dfafb1a2482044be480fc`.
- pending 0, duplicate 0, orphan 0.

## 결과물 및 한계

새 index는 `data/기본기_연구/research_data_index_enriched.json`이다. 기존 `research_data_index.json`은 교체하지 않았다. case별 새 scalar 필드 옆에 `provenance_evidence`, `provenance_conflicts`, `official_answer_source_status`, `sdss_provenance`, `visual_supplements`, `source_restoration_provenance`를 두어 값의 근거를 추적할 수 있다.

case 간 label 표기 정규화, source 경로 역할의 의미적 우열 판정, missing provenance의 외부 보완은 수행하지 않았다. 실제 필드가 충돌하거나 자료가 연결되지 않은 case는 그대로 conflict/unresolved로 남겼다.
