# Repository maintenance 최종 정리

작성일: 2026-10-06. 이 3차 단계는 물리적 재배치 대신 탐색을 위한 문서·index 안내를 완성했다. 기존 production 파일을 이동·이름 변경·삭제·reference rewrite하지 않았고, 새 semantic research도 수행하지 않았다.

## 물리 이동을 하지 않은 이유

1·2차 검토에서 725개 reference 후보 중 확인된 production broken reference는 0건이고, migration map상 이동 권고도 0개였다. 현 경로를 유지하면서 inventory와 research index로 논리적 탐색층을 제공하는 편이 원장·blind/sealed barrier·provenance를 보존하고 참조 위험을 줄인다. 이번 단계는 archive 후보를 목록화했을 뿐 실제 archive/delete를 하지 않았다.

## Unresolved reference 최종 분류

`reference_validation.json`의 유일 unresolved인 `scripts/verify_prepared_backlog.py` → `분석/기본기_연구/독립연구_03_최초풀이.md`를 `historical_reference`(confidence high)로 확정했다. script의 `EXISTING` 경로는 `EXISTING.exists()`일 때만 읽는 선택적 overlap 검사에 쓰인다. legacy 03 문서가 없어도 현재 manifest, blind/sealed, queue 검증을 막지 않으며 필수 production 입력도 아니다. 근거와 `final_resolution`은 `data/기본기_연구/reference_validation.json`에 추가했다. production 파일은 수정하지 않았다.

## 사람용 논리적 진입점

[README_RESEARCH_REPOSITORY.md](README_RESEARCH_REPOSITORY.md)에 디렉터리 안내, 11개 authoritative hierarchy, case/group/source/stage별 진입점, 직접 수정 금지 대상, blind/sealed 경계, maintenance 산출물의 용도와 사용자 구분을 기록했다.

## Archive candidate

[archive_candidates.json](../../data/기본기_연구/archive_candidates.json)에 총 13개를 기록했다.

- 명시적 `.bak` 3개는 production 소비 참조를 발견하지 못해 archive 후보로 표시했다. `safe_to_archive=true`, `safe_to_delete=false`; 과거 버전 provenance는 보존해야 한다.
- LEET OCR/source 진단 JSON 10개는 OCR manifest 또는 diagnostic 생성/검수 경로와 연결된다. `referenced_by_production=true`, `safe_to_archive=false`, `safe_to_delete=false`로 보존한다.
- 완전 동일 백업 `scripts/cxresearch.bak-20261002-230430`의 `byte_identical_to`는 현재 `scripts/cxresearch`를 가리킨다. 내용이 동일해도 백업 경로의 역사적 가치는 삭제 근거가 아니다.
- 생성 실패 중간물 또는 명백한 cache로 확정 가능한 추가 파일은 찾지 못했다. 파일명만 비슷한 자료를 후보로 확대하지 않았다.

## Research index coverage

검사는 기존 `research_data_index.json`, queue/processed의 record ID, inventory 경로 목록만 사용했다. 원문 semantic 자료를 보정하지 않았다.

| 연결 단계 | 기계적 coverage | 상태 |
|---|---:|---|
| case → passage_group | 1,671 / 1,671 정합 | 연결 가능 |
| passage_group → case 목록 | 499 groups | 연결 가능 |
| blind source 경로 | 1,671 / 1,671이 index 및 inventory에 존재 | 연결 가능 |
| 시험 family / year / question / candidate ID | 각각 0 / 1,671 채워짐 | index gap. 해당 시험을 찾으려면 정본 source ID/path와 `자료/` 원본을 별도 대조해야 함 |
| official answer/provenance source refs | 112 / 1,671 채워짐 | 부분 연결. 정답 대조 stage는 더 많은 case에 있지만 provenance 참조는 index에 제한적으로 반영됨 |
| SDSS 공개/대조 | 1,663 / 1,671 `sdss_compare` stage 및 complete disclosure 표시 | consumed case는 연결 가능. 나머지 prepared/hold 사례를 완료로 추정하지 않음 |
| blind raw record | index stage record ID 1,670개가 queue 및 processed ledger에서 확인됨 | stage-record 단위 연결. 1,667 case에 연결되어 일부 case는 다중 기록 |
| answer_check raw | 1,681 record ID queue/processed 확인 | record ID 연결 가능 |
| independent_code raw | 1,665 record ID queue/processed 확인 | record ID 연결 가능 |
| sdss_compare raw | 1,663 record ID queue/processed 확인 | record ID 연결 가능 |
| induction | 1 record ID 확인 | 부분 coverage |
| meta_induction / manual_parity_audit | index상 각각 0 stage record | 해당 index 필드 연결 없음. 이것만으로 작업 필요성이나 의미 상태를 추론하지 않음 |
| depth_backfill | 48 record ID 확인 | 해당 기록 연결 가능 |
| reflected Markdown target | blind 1,672, answer_check 1,681, independent_code 1,665, SDSS 1,663, induction 1, depth_backfill 50개 target이 inventory path와 연결 | target 연결 가능. target 수는 stage record 수와 같지 않을 수 있음 |

case→group→blind source→raw stage ID→reflected target까지는 현재 index로 따라갈 수 있다. 모든 case를 시험/연도/문항으로 되짚거나 official answer provenance를 완전히 따라가려면 index coverage가 부족하다. 이를 채우려면 별도 기계적 index 작업이 필요하며 semantic 판단으로 빈칸을 채우지 않는다.

## 무결성 최종 검증

2차 산출물의 기준 hash/row count와 이번 작업 뒤 상태를 비교했다. 아래 원장은 byte-identical이었다.

- queue: 7,605 rows; SHA-256 `74b1e630ddb3808a1fc25d5d047514b8558ddd8f271d1d41a5d629fd568b4195`.
- processed: 7,605 rows; SHA-256 `c49e67a393b517671b94b6e0267689f8250fe55f6d4f2cd38e0cd954ef311818`.
- manifest: 1,671 rows; SHA-256 `29bbdf41af019151d0342a846b3cfa48cec22142f41f24f5d895c4b8e4392e48`.
- meta_state: SHA-256 `2ac212abe6f83b7d2e97f9b2ef0b706bca92bd8bda7dfafb1a2482044be480fc`.
- queue `record_id`와 processed `source_record_id` 대조: pending 0, duplicate 0, orphan 0.
- manifest 상태: `consumed_sdss` 1,663, `prepared` 8. hold 기록 4건과 G024/G370 hold 상태는 2차 기준과 동일하다.
- 새로 생성한 파일은 README, archive candidate JSON, 이 final report 3개다. 별도 요청에 따라 기존 maintenance 파일인 `reference_validation.json`에 unresolved 1건의 `final_resolution`만 추가했다. queue/processed/manifest/meta_state 및 연구 의미 원장은 수정하지 않았다.

## 후속 작업자가 지킬 원칙

1. 기존 경로를 기준으로 시작하고 index를 탐색 도구로 쓴다. 저장소를 보기 좋게 만들기 위한 이동은 하지 않는다.
2. queue는 append-only, processed는 `source_record_id` 연결 ledger, manifest와 meta_state는 operational 원장으로 취급한다. 직접 고치거나 재정렬하지 않는다.
3. manifest가 정한 blind-only source만 blind 단계에서 읽는다. 해당 group 전체 blind와 independent code가 저장될 때까지 sealed answer/SDSS, 정답 필드, 기존 해설·코드 판단을 공개하지 않는다.
4. 원본 정답과 출처 provenance를 확인하고 SDSS는 제3자 후보로 취급한다. index의 빈 필드는 근거 없이 채우지 않는다.
5. byte-identical 여부만으로 자료를 삭제하지 않는다. archive/delete 검토 시 역할·provenance·현재 소비 경로를 각각 확인하고 archive는 원본 경로를 기록한 채 보존한다.
6. G024/G370 hold는 이 유지보수에서 해소하지 않았다. 기존 hold를 그대로 존중한다.
