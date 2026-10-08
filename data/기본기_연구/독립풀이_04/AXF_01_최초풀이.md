

<!-- luna-raw:AXF-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G342",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "미확정",
  "source_read": [
    "AXF.json",
    "G342_visual01.tif 직접 렌더",
    "G342_visual02.md",
    "G342_visual03.md"
  ],
  "required_information_and_location": [
    "1~2문단: 물과 우무의 서로 다른 전이 온도",
    "3문단: 입자/개체 및 상호작용 구조의 유사성",
    "5문단: 이전 범죄율 상태가 현재 상태에 영향"
  ],
  "minimal_logic_without_codes": "서로 다른 물질은 다른 조건에서 상태가 바뀐다. 구조의 유사성이 모형 전이를 뒷받침해도 구성 요소 종류가 전이 조건에 무관하다는 결론은 나오지 않는다.",
  "intermediate_reasoning": [
    "① 특정 임계점의 급변은 B/D로 확인된다.",
    "②③ 물리 모형의 사회 적용은 구조 유사성에 근거한다.",
    "④ 물 0도와 우무 40/80도는 요소 종류 무관 주장에 반대 증거다.",
    "⑤ 현재 변수 외 직전 상태를 요구하는 이력 특성에 부합한다."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "임의 유비가 아니라 구조 유사성으로 의미 있는 시도라는 3문단을 놓치면③을 배제하지만 본문은 그 타당성을 지지한다.",
  "quota_status": "unavailable"
}
```
