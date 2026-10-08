

<!-- luna-raw:BEH-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G401",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "발문 긍정 입장에서 부정 평가 비판",
    "2문단 덜 사대적이라는 옹호 논거",
    "3문단 현실적 불가피성과 명분론 차이",
    "4문단 고유/외래 관계에 따른 평가 분기"
  ],
  "minimal_logic_without_codes": "비판 발언이 실제로 어느 편의 논거를 공격하는지 고정한다. 긍정 입장을 지키며 부정 평가의 근거를 공격하는 ㄱ·ㄷ만 선택한다.",
  "intermediate_reasoning": [
    "ㄱ 조선과 동일시하는 부정 평가를 맥락 차이로 비판하므로 긍정 측에 맞다.",
    "ㄴ 덜 사대적이라는 긍정 논거의 의미를 부정하므로 반대 방향이다.",
    "ㄷ 고유=좋음·외래=나쁨의 단순 대립을 부정하면 유교 수용을 부정하는 근거가 약해진다.",
    "ㄹ 기득권 수호를 진정한 이유로 놓고 불가피성 옹호를 공격하므로 부정 측의 비판이다."
  ],
  "attractive_wrong": {
    "choice": 4,
    "exact_error": "ㄴ의 비판 표현 자체만 보고 발화자의 편을 놓친다. 상대적 우위 논거를 공격하면 긍정 평가를 약화한다."
  }
}
```
