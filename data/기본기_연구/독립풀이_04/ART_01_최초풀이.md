

<!-- luna-raw:ART-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G294",
  "selected_answer": 2,
  "confidence": 0.93,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "같은 위도에서 난류 영향 유무가 기온 차이를 만들고 일교차를 완화함",
    "장기 기후 예측의 해양 관련 난점",
    "G294_visual02.md 표 직접 확인: 화성 토양100/해수0,지구 해수68"
  ],
  "minimal_logic_without_codes": "화성은 해양이 없어 같은 위도 지역 간 난류 영향 차이가 사라지므로 그 차이를 가진 지구보다 지역 평균 기온 차이가 작을 것으로 추정한다.",
  "intermediate_reasoning": [
    "① 열용량이 큰 해양이 없으므로 표면 열적 조건의 장기 영향이 더 크다고 할 근거가 없다.",
    "② 해류 유무로 생기는 동위도 지역 차이 요인이 없다.",
    "③ 전자기파 전달의 제약은 해수에 관한 것으로 화성 대기에 그대로 옮기지 않는다.",
    "④ 해양 관련 관측·상호작용 난점이 없으므로 본문에서 더 어렵다고 추정하지 않는다.",
    "⑤ 바다의 열적 완충이 없으므로 더 작은 일교차를 추정할 근거가 없다."
  ],
  "attractive_wrong_answer": 5,
  "exact_error": "대기가 희박하거나 온도 범위가 낮다는 사실을 일교차가 작다는 뜻으로 바꾸면 열용량 완충 경로를 놓친다.",
  "uncertainty": "②는 본문과 표의 해양 요인 중심 비교다. 화성의 모든 지형·대기 요인을 실제로 통제한 전역 기후 법칙으로 주장하지 않는다.",
  "quota_status": "unavailable"
}
```
