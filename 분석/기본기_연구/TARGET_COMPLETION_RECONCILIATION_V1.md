# Target completion reconciliation v1 — 2026-09-27

## 범위와 판정 방식

이번 작업은 ID·source coordinate 연결만 수행했다. 문항 지문·선지의 의미, 정답, 코드, SDSS 태그는 해석하지 않았다. `manifest.status=consumed_sdss`인 903건을 연구 쪽 원장으로, `code_study_candidates_v2.jsonl` 1,147건을 target universe로 사용했다. 후보 ID → canonical question ID → 정규화 source coordinate → passage+question의 우선순위로 exact 식별자를 비교했다. 문자열·제목·지문 유사도는 사용하지 않았다.

시험명은 공백/underscore/국어 표기 및 KICE 6평·9평, A/B형, LEET·MEET 표기를 기계적으로 정규화했다. candidate universe의 canonical question ID 중복은 0, source coordinate 중복은 0였다. 903 consumed case는 모두 provenance metadata가 완전했다. 기존 독립풀이 case 파일 2,712개는 식별자 문자열만 스캔해 provenance/raw queue와 대조했으며 추가 exact canonical ID 연결은 없었다. 같은 passage의 target sibling이 있어도 question number가 다르면 target completion으로 세지 않았다. 이번 exact canonical passage ID 대조에서는 NON_TARGET_RESEARCH 537건 중 target sibling이 확인된 case가 0건이었다.

## Research-side reconciliation

| 상태 | 건수 |
|---|---:|
| TARGET_MATCHED | 366 |
| NON_TARGET_RESEARCH | 537 |
| AMBIGUOUS | 0 |
| UNRESOLVED_METADATA | 0 |
| 합계 | 903 |

TARGET_MATCHED는 candidate_id exact 357건, question_id exact 추가 9건이다. 우선순위 기준으로 source-coordinate exact 추가 0건, passage+question exact 추가 0건, verified legacy conversion 추가 0건, unresolved metadata 0건이다. 좌표 일치 corroboration은 366 case에서 있었으나 더 높은 우선순위의 exact identifier가 이미 같은 target을 결정했으므로 중복 coverage로 합산하지 않았다. NON_TARGET_RESEARCH는 complete exact source coordinate가 target universe에 없음을 뜻한다.

## Target-side reconciliation

| 상태 | 건수 |
|---|---:|
| COMPLETED_TARGET | 366 |
| HOLD | 4 |
| NOT_COMPLETED_READY_LOCAL_SOURCE | 425 |
| NOT_COMPLETED_NEEDS_RESTORE | 335 |
| NOT_COMPLETED_SOURCE_MISSING | 9 |
| AMBIGUOUS_COMPLETION | 8 |
| 합계 | 1147 |

COMPLETED_TARGET 366개만 903개 consumed case 중 하나 이상과 exact/mechanical evidence로 연결된다. 이전 preflight가 COMPLETED로 뒀던 374개 중 366개는 consumed case와 연결됐고, 나머지 8개는 과거 ID 흔적은 있으나 consumed case linkage가 없어 AMBIGUOUS_COMPLETION으로 낮췄다. G024 HOLD 4개는 consumed 수와 완료 수에 포함하지 않았다. target remaining은 781개(hold 포함), HOLD를 제외한 비완료 후보는 777개다.

## 중복·모호성·G282

- consumed case → 복수 target candidate: 0
- target candidate → 복수 consumed case duplicate history: 0
- research-side ambiguous / unresolved: 0 / 0
- target-side ambiguous completion: 8 (계속 준비 대상에서 제외)
- G282 준비 재개 안전성: **YES**. 새 crosswalk를 authoritative하게 읽는 preflight dry-run에서 30 groups·91 questions (G282/AQG 시작, MEET/DEET 30 groups)을 다시 확인했다. 제안된 91개 후보는 모두 `NOT_COMPLETED_READY_LOCAL_SOURCE`였고 COMPLETED_TARGET·HOLD·AMBIGUOUS_COMPLETION 겹침은 0이었다. dry-run 검증값은 전부 0이다. 실제 READY/manifest/blind/sealed 파일은 만들지 않았다.

## 불변 원장 확인

Queue SHA-256 `e98e459b68fe52ae582fae7d213e550e4052930770ea8762ebc33e7769881624`; processed SHA-256 `f0fe43a1d5ceeb02b777b4a07a2ca1d2faeb948b594955ddf88bce9d8abde456`. queue와 processed 원장은 수정하지 않았다. 기존 manifest consumed 상태와 G024 HOLD도 수정하지 않았다.

## 산출물

- `data/기본기_연구/research_case_target_crosswalk_v1.jsonl`: consumed case 903행
- `data/기본기_연구/target_completion_crosswalk_v1.jsonl`: target candidate 1,147행
