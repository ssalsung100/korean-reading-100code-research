

<!-- luna-raw:LN-boundary_revision-20260917-01 -->
## Astra raw handoff — boundary_revision

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G081",
  "original_record": "LN-independent_code-20260917-01",
  "original_preserved": true,
  "revision": "#31을 보조에서 표면 후보로 낮춘다. 실제 비교는 화소라는 원소의 개수와 각 원소의 밝기값이지 원소의 수와 집합의 수가 아니다. 원표의 양적 집합 구분을 단어가 비슷하다는 이유로 확장하지 않는다.",
  "revised_primary": [
    17
  ],
  "revised_auxiliary": [
    45
  ],
  "revised_surface": [
    31,
    86,
    49,
    92
  ],
  "reason": "두 수량의 종류가 다르다는 공통성은 #17로 충분하며 #31에 고유한 집합수 판단은 없으므로 독립 보조 연산을 주장할 근거가 부족하다.",
  "repartition_condition": "영상 개수와 영상당 화소수를 비교하여 집합수/원소수 차이가 실제로 정답을 가를 때 #31 재검토.",
  "sdss_disclosed": false,
  "confidence": 0.96
}
```


<!-- luna-raw:LN-sdss_compare-20260917-01 -->
## Astra raw handoff — sdss_compare

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G081",
  "site_original_codes": [],
  "candidate_id": null,
  "site_marked_answer": null,
  "comparison_status": "prepared_linkage_absent",
  "judgment": "준비 SDSS 연결 부재로 의미 비교 불가. 사이트 무표지·불일치로 집계하지 않음.",
  "independent_judgment_preserved": true,
  "barrier_verified": "all_group_independent_code_records_before_any_group_sdss_disclosure",
  "group_independent_record_ids": [
    "LN-independent_code-20260917-01",
    "LO-independent_code-20260917-01",
    "LP-independent_code-20260917-01"
  ],
  "qualification": "LO 그림은 blind 전에 직접 판독; 축소수식 n/2×n/2는 결정근거가 아닌 source보강으로 공식답 공개 후 확인. 이 타이밍·과거 노출 불명·원배포 PDF 미검증 유지. LN #31을 표면으로 내린 독립 후속 revision은 SDSS 전에 저장됨."
}
```
