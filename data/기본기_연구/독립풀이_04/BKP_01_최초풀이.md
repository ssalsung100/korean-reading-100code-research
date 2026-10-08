

<!-- luna-raw:BKP-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G457",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "2문단",
      "evidence": "논박 성공 측은 색의 사적 느낌만 뒤집히고 행동·말은 동일하다고 가정한다."
    },
    {
      "location": "3문단",
      "evidence": "실패 측은 색 외적 따뜻함·생동감과의 관계 때문에 감각질 뒤집힘이 행동 차이를 낳는다고 본다."
    },
    {
      "location": "보기",
      "evidence": "따뜻한 물을 원하는 사람이 빨간 온수 꼭지와 파란 냉수 꼭지 앞에 있다."
    }
  ],
  "minimal_logic_without_codes": "논박 성공 측에서는 느낌이 뒤집혀도 말과 행동이 같아 빨간 온수 꼭지를 틀어야 한다. 따라서 양측 모두 빨간 꼭지를 틀지 않는다고 한 ④는 틀리다.",
  "intermediate_reasoning": [
    "① 빨강-초록의 느낌이 뒤집히므로 실제 빨간 꼭지는 초록 느낌이다.",
    "② 성공 측은 명명 행동이 같다는 가정이라 빨간색이라고 말한다.",
    "③ 실패 측은 색과 따뜻함의 관계를 통해 차이를 주장하므로 뒤집힌 초록 느낌에서 빨강의 따뜻함을 얻지 못한다고 설명한다.",
    "⑤ 빨강↔초록만 뒤집히고 파랑과의 구별이 지워지는 것은 아니므로 양측 모두 두 꼭지를 구별 가능하다고 본다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "사적 느낌이 초록으로 바뀌면 말도 초록으로 바뀔 것이라고 추론해 성공 측이 명시한 말·행동 동일 가정을 지운다."
  },
  "scope_limit": "④는 성공 측이 빨간 꼭지를 튼다는 사실만으로 배제된다. 실패 측이 반드시 파란 꼭지를 튼다거나 구체 대체 행동을 확정하지 않는다."
}
```
