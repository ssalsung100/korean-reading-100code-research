# FC — handoff raw 반영

<!-- luna-raw:FC-sdss_compare-20260913-03 -->
## Astra raw handoff — sdss_compare

원문 raw payload를 그대로 반영했다. Luna는 의미를 재판정하지 않았다.

```json
{
  "record_id": "FC-sdss_compare-20260913-03",
  "case": "FC",
  "stage": "sdss_compare",
  "status": "done",
  "timestamp": "2026-09-13T14:41:56.363356+00:00",
  "payload": {
    "passage_group": "G032",
    "all_group_independent_code_records_before_any_group_sdss_disclosure": true,
    "site_original_codes": [
      "경우의수"
    ],
    "site_code_numbers": [
      90
    ],
    "independent_primary": [
      91
    ],
    "comparison": "독립 주와 불일치·사이트 범위 미확인.",
    "semantic_comparison": "독립 풀이에는 조합 개수나 확률 산출이 없다. 그래프 종류 또는 기울기와1의 대소별 경우를 나누는 범위까지 사이트#90이 포함한다면 접점이 있을 수 있으나 태그 하나로 그 정의를 확정하지 않는다. 비례→같은 증가율→L기울기1이라는 실제 연결을 유지한다.",
    "independent_judgment_preserved": true,
    "revision_after_disclosure": "최초 코드 유지. 동일한 연산의 소재·표현·검증 전략별 관점 중첩을 별도 보존.",
    "unresolved": "FC#90이 경우 분기인지 다른 설명 위치인지 미확인."
  }
}
```
