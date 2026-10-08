

<!-- luna-raw:AAK-sdss_compare-20260920-01 -->
## Astra raw handoff — sdss_compare

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G168",
  "site_original_codes": [],
  "candidate_id": null,
  "site_marked_answer": null,
  "comparison_status": "site_linkage_absent_no_semantic_comparison",
  "independent_primary_preserved": [
    96
  ],
  "finding": "실제 연결 후보·태그가 없어 독립 판정과 의미 대조할 사이트 판단이 없다. 사이트가 코드를 부정했다고 해석하지 않고 일치·불일치 집계에서도 제외한다.",
  "revision": "독립 코드 및 국소 중첩 유보 유지.",
  "barrier_verified": "G168 여섯 문항 전체 independent_code raw 저장 후에만 SDSS 공개.",
  "strict_blind_eligible": false,
  "exposure_qualification": "과거 공식 원문·전체정답 노출에 따른 비strict 재구성. AAG는 공식 범위 crop 직접 확인 후 후속 blind raw로 hold 해소.",
  "answer_provenance_limit": "이번 대조는 canonical answer의 기계 연결이며 공식 배포 답표 직접 검증으로 승격하지 않는다.",
  "quota_status": "unavailable"
}
```
<!-- luna-raw:AUDIT48-sixcases-depth_backfill-20260920-01:AAK -->
## Astra grouped depth_backfill 연결 — AAK

canonical grouped raw는 `분석/기본기_연구/독립연구_04_절차와_진행기록.md`의 동일 record에 보존한다. AAK 보강 원문은 최초 기록을 덮어쓰지 않고, `original_primary=[96]`, `original_auxiliary=[39]`, `revised_primary=[]`, `primary_candidates=[96,39]`, `working_representative=96`으로 기록되었다. 39를 주 후보로 보강하되 별도 필수 연산으로 중복 집계하지 않는다.
