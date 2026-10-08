# G282 frontier 대조 blocker — 2026-09-27

## 결론

G282 준비는 dry-run에서 멈췄다. 후보목록은 30 groups·91 questions, 첫 group G282/AQG, family MEET30으로 제안됐지만, repository 집계와 candidate 완료 crosswalk 사이의 gap 529가 남는다. `--dry-run` 종료 코드 1은 이 `candidate_completed_crosswalk_gap=529` 항목 때문이다. 나머지 사용자 지정 검증 항목은 모두 0이다.

따라서 실제 READY 상태 기록이나 manifest, blind/sealed 자료, packet은 쓰지 않았다. 외부 다운로드도 하지 않았다. 이 기록은 대조 상태만 보존하며 문항·코드 의미를 판정하지 않는다.

## Dry-run 상태

| 항목 | 건수/값 |
|---|---:|
| 제안 group / question | 30 / 91 |
| 첫 frontier | G282 / AQG |
| family | MEET30 |
| candidate status COMPLETED | 374 |
| candidate status HOLD | 4 |
| candidate status READY_LOCAL_SOURCE | 425 |
| candidate status NEEDS_RESTORE | 335 |
| candidate status SOURCE_MISSING | 9 |
| candidate status 합계 | 1,147 |
| repository completed questions | 903 |
| repository remaining | 244 |
| candidate completion gap | 529 |

Candidate `COMPLETED` 374는 candidate_id/qid/source-coordinate 확인 기준의 상태 집계다. 별도 exact family+year+exam+qn 및 qid 일치 집계는 366이며, 이 안에 HOLD 4건이 포함된다. 두 지표는 별도 dry-run 필드로 보존하고 서로 대체하거나 재해석하지 않는다. 차이 때문에 repository 완료 903건을 candidate 완료 상태로 간주하지 않는다.

## 준비목록 및 hold

현재 manifest는 907 rows다: `consumed_sdss` 903, `prepared` 4. 남은 DR~DU 네 건은 G024 historical hold로 유지되며 소비하거나 후보 집계에서 제거하지 않았다. 현재 manifest에 actionable READY는 0이다. dry-run 제안 G282~G311을 실제 manifest에 추가하지 않았다.

## Source 상태 요약

- `SOURCE_MISSING` 9건: LEET 2008 preliminary Q4–Q8 5건, KICE 2016 수능 B형 Q21–Q24 4건.
- `NEEDS_RESTORE` 335건은 KICE 시각 선택지 중 local official question page가 없는 건, historical passage overlap, 그 밖의 legacy parser/source gap을 포함한다. local question-source 목록에서 KICE 2023·2025·2026 question PDF/page image는 확인되지 않았다. 외부 다운로드는 하지 않았다.
- 기계적 대안으로 high-confidence question-group linkage가 이미 있는 LEET prose/table assets를 anonymous supplement로 normalize하는 dry-run fallback을 기록했다. 이 대안은 실제 READY 기록을 허용하지 않는다.

## Ledger와 상태 보호

Queue와 processed는 읽기 전용으로 유지했다. 기준 snapshot SHA-256은 queue `e98e459b68fe52ae582fae7d213e550e4052930770ea8762ebc33e7769881624`, processed `f0fe43a1d5ceeb02b777b4a07a2ca1d2faeb948b594955ddf88bce9d8abde456`이다. meta_state는 completed 903, meta/audit due false, `depth_backfill_pending=[]`, `semantic_state_review=[]`를 유지한다. 이 reconciliation만으로 집계나 manifest 상태를 갱신하지 않았다.

재개 조건은 529 candidate-completion gap을 candidate_id/qid/source-coordinate evidence로 연결해 해소하는 것이다. 그때까지 G282는 blocked로 남긴다.
