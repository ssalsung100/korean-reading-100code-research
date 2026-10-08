

<!-- luna-raw:AEZ-sdss_compare-20260920-01 -->
## Astra raw handoff — sdss_compare

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "site_original_codes": [],
  "site_marked_answer": null,
  "comparison_status": "실제 SDSS 연결 없음; 일치·불일치 판정 불가",
  "independent_primary_preserved": [
    45
  ],
  "revision": null,
  "group_barrier": "AEX/AEY/AEZ/AFA 전체 independent_code raw 확인 뒤 최초 공개",
  "exposure_followup": "sealed의2026학년도6월Q10~13은 CURRENT의 과거 공식PDF 범위밖 노출 hold와 겹침. 신규 blind raw는 보존하되 역사적 사전 노출로 strict blind 성과에서 제외해야 함. 별도 정정 hold 저장.",
  "quota_status": "unavailable"
}
```
<!-- luna-raw:AUDIT48-sixcases-depth_backfill-20260920-01:AEZ -->
## Astra grouped depth_backfill 연결 — AEZ

canonical grouped raw는 `분석/기본기_연구/독립연구_04_절차와_진행기록.md`의 동일 record에 보존한다. AEZ 보강 원문은 최초 기록을 덮어쓰지 않고, `original_primary=[45]`, `original_auxiliary=[84,86]`, `revised_primary=[45]`로 기록되었다. B의 9몰은 외부 공급·별도 수소 생성 경로가 없다는 조건부 최대치이며 무조건적 상한으로 승격하지 않고, A의 13.5몰 이상도 부반응을 정확히 0으로 간주한 근사 계산으로 보존한다.
