

<!-- luna-raw:BPL-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G500",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "두 모델의 유권자·집권자 선택 설명",
      "evidence": "유권자는 이념 또는 현재 정부의 질과 민주주의 관련 효용을 함께 고려하고 집권자도 조작의 득실·프리미엄을 고려한다."
    }
  ],
  "minimal_logic_without_codes": "두 역할 모두 서로 다른 결과의 득실을 고려하는 선택 상황에 놓일 수 있으므로②가 적절하다.",
  "intermediate_reasoning": [
    "① 두번째 모델은 민주주의 자체의 내재적 가치를 가정하지 않는다.",
    "③ 중도 유권자도 정책 이념의 효용을 고려하되 민주주의 손실과 비교한다.",
    "④ 지지 속 퇴행은 집권자 매력이 높은 경우다.",
    "⑤ 프리미엄은0에서 시작해 조작으로 커질 수 있으며 반복하면0으로 수렴한다는 말은 없다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "미래 정권교체 능력을 중시한다는 도구적 선호를 민주주의 자체의 내재적 가치 선호와 동일시한다."
  },
  "scope_limit": "기출의 가상 정치모형을 판독하며 실제 집단 대상의 선거 전략을 제안하지 않는다."
}
```
