

<!-- luna-raw:BGE-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G418",
  "selected_answer": 2,
  "confidence": 0.97,
  "exposure": {
    "prior_exposure": "unknown",
    "official_answer_read": false,
    "sdss_read": false,
    "existing_case_analysis_read": false,
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "환원 요건 및 장애 문단",
      "evidence": "빠짐없는 설명예측 필요,근사해는진짜아님,실험자료의존으로환원불성립"
    },
    {
      "location": "visual01",
      "evidence": "ㄱ 실험결과반영조정은설명아님,ㄴ 근사도참값못지않은정확성,ㄷ 원자/분자근사난이도차"
    }
  ],
  "minimal_logic_without_codes": "근사해 때문에 완전 설명예측이 안 된다는 근거를ㄴ이 약화한다.ㄱ은경험조정의존 비판을 강화,ㄷ은상대난이도여서환원성립을 보장하지 않는다.",
  "intermediate_inference": [
    "ㄴ이 받아들여져도 경험자료의존이라는 다른 근거가 남아 결론을 완전히 반박한 것은 아니다.",
    "ㄱ은강한설명요건을 제시해보정된방법의환원주장을더어렵게한다.",
    "ㄷ은더쉽다는것이지정확해를얻거나보정없이완전예측한다는것이아니다."
  ],
  "attractive_wrong_answer": 5,
  "exact_error": "⑤의ㄷ은계산이상대적으로쉬움과환원요건충족을동일시한다.",
  "unresolved": null
}
```
