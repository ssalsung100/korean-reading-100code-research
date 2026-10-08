

<!-- luna-raw:ASZ-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G305",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "supplement_seen": "G305_visual01.md"
  },
  "needed_information_locations": [
    "프로게스틴 추가가 유방암 비율 증가 가능",
    "경구투여의 간 일차대사→응고인자 촉진→폐혈전색전증 증가",
    "비교A 성분변경/B 경로변경"
  ],
  "minimal_logic_without_codes": "가설이 맞다면 프로게스틴 없는 단독군은 유방암이 더 낮고,경구 대신 피부 패치군은 폐혈전색전증이 더 낮아④다.",
  "intermediate_reasoning": [
    "A는에스트로겐고정·프로게스틴유무변경. B는복합성분고정·투여경로변경. 각각지정된질환의증가경로를제거한다."
  ],
  "attractive_wrong_answer": 5,
  "exact_error": "A의 방향은 맞지만 B에서 경구 대사 경로 제거의 효과를 반대로 적었다.",
  "quota_status": "unavailable"
}
```
