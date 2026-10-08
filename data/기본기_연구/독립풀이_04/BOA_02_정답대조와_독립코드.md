

<!-- luna-raw:BOA-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G487",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "폭력 있는 양육친에게 즉시 돌려보내면 자녀의 복리에 맞지 않을 수 있으므로 신속 반환과 복리 원칙이 충돌하는 사례가 늘었다는②가 타당하다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BOA-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G487",
  "minimal_logic_without_codes": "양육친의 폭력에서 도피한 자녀를 신속히 돌려보내면 복리를 해칠 수 있다. 따라서 신속 반환이라는 수단이 모든 상황에서 복리 목적에 부합하지는 않는다.",
  "primary": [
    {
      "code": 24,
      "reason": "통상적인 신속 반환의 원칙에 중대한 위험이라는 예외 상황을 적용한다."
    }
  ],
  "auxiliary": [
    {
      "code": 44,
      "reason": "자녀 복리 목적과 신속 반환 수단을 구분한다."
    },
    {
      "code": 36,
      "reason": "폭력 도피 사례는 모든 신속 반환이 복리에 맞는다는 일반화의 반례다."
    },
    {
      "code": 2,
      "reason": "부합하기 어렵다는 사례가 있다는 판단이며 모든 반환이 나쁘거나 위험 사례는 반드시 거절된다는 주장이 아니다."
    },
    {
      "code": 12,
      "reason": "⑤의 초기 동의에는 귀국 전제가 붙어 있어 이후 반환 거부까지 적법하게 만들지 않는다."
    }
  ],
  "surface": [
    {
      "code": 59,
      "reason": "국제 이동 문제에 대한 협약 해결책이라는 큰 구조는 있으나②의 결정점은 해결책의 예외 상황이다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "신속 반환과 복리가 항상 양립 불가능하다는 결론은 아니다. 보호조치와 반환의 결합도 허용된다."
    },
    {
      "code": 5,
      "rejection": "사례가 늘었다는 시간 변화가 있지만 사건 수의 추세만으로 목적-수단의 충돌을 설명할 수 없다."
    },
    {
      "code": 55,
      "rejection": "반환의 모든 효과가 허위 인과라는 비판이 아니라 특정 위험 조건에서의 예외 판정이다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
