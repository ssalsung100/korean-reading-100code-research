

<!-- luna-raw:BOQ-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G492",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "④는 규칙 채택 자체가 더 적은 공리를 낳는 경우에도 브란트가 그 규칙을 옳다고 인정할 것이라 한다. 이는 규칙 채택의 정당화 조건을 위반한다. 개별 위반이 이익을 늘리는 경우와 다르다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "remaining_uncertainty": "추가 없음"
}
```


<!-- luna-raw:BOQ-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G492",
  "minimal_logic_without_codes": "규칙의 채택 자체가 더 큰 공리를 낳아야 한다는 기준과, 채택된 규칙을 개별 이익 때문에 위반하지 않는다는 기준을 구분한다.④는 전자를 충족하지 않는데 후자의 준수를 적용한다.",
  "primary": [
    {
      "code": 17,
      "reason": "규칙 채택의 평가와 개별 행위 평가라는 판단 단위를 교환하지 않는다."
    }
  ],
  "auxiliary": [
    {
      "code": 10,
      "reason": "규칙이 옳기 위해서는 채택했을 때의 공리가 더 커야 한다는 필요조건을 확인한다."
    },
    {
      "code": 12,
      "reason": "개별 위반의 이익이 크더라도 이미 정당화된 규칙은 지킨다는 조건 범위를 유지한다."
    },
    {
      "code": 75,
      "reason": "권리의 확실성·규범적 힘·직관과 계산에 대한 각 이론의 입장을 보기 상황에 귀속한다."
    },
    {
      "code": 88,
      "reason": "규칙 채택/미채택의 비교와 개별 행위 이익 비교의 단위를 나눈다."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "권리 침해의 허용·금지가 소재이지만④의 직접 오류는 평가 수준과 조건의 교환이다."
    }
  ],
  "competing_codes": [
    {
      "code": 4,
      "rejection": "개별 행위를 규칙 전체와 혼동하는 범위 기술도 가능하지만 단순한 모든/일부의 변환보다 평가 대상의 층위를 바꾼 오류다."
    },
    {
      "code": 20,
      "rejection": "다른 충분한 수단이 있어 기존 수단이 불필요한 사례가 아니라 규칙 정당화의 선행 요건이 빠진 것이다."
    },
    {
      "code": 13,
      "rejection": "권리와 공리가 모든 상황에서 양립 불가능하다고 가정하지 않는다. 이 사례의 조건에서 각 이론이 무엇을 요구하는지 판단한다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
