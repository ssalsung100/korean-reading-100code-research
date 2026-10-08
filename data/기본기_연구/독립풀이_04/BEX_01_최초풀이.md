

<!-- luna-raw:BEX-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G406",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "[A] 세 오류의 정의",
    "보기ㄱ 개념의 확실성→신 실재→개념의 확실성",
    "보기ㄴ 삶의 의지→소중함→절대 자연 이법"
  ],
  "minimal_logic_without_codes": "ㄱ의 최종 근거가 처음 전제로 되돌아가고, ㄴ은 마지막 근거를 절대 이법으로 세워 더 묻지 않게 한다. 각각 순환과 중지다.",
  "intermediate_reasoning": [
    "ㄱ은 여러 근거가 끝없이 추가되지 않고 처음의 확실성을 결론의 신 존재로 다시 보장한다.",
    "ㄴ은 이유를 몇 단계 제시하지만 마지막 자연 이법을 절대적 근거로 놓아 끝낸다.",
    "따라서 순환 논증·절차 단절 조합인④다."
  ],
  "attractive_wrong": {
    "choice": 3,
    "exact_error": "ㄴ에 이유가 연속한다는 겉모양만 보고 무한 소급으로 판단한다. 끝에 절대 자연 이법으로 멈추는 표지가 있다."
  }
}
```
