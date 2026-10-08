

<!-- luna-raw:BQY-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G512",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2019/2019_answer/table_001.md 홀수형1~3(공식 HWP 추출 표)",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "법이 관습을 바꾼 사례는 바꿀 수 없다는 관습이론의 주장에 반례로 작용한다.문화 변화가 법 개정을 이끈④와 인과 방향이 다르다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BQY-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G512",
  "sdss_seen": false,
  "primary": [
    {
      "code": 63,
      "reason": "각 사례가 관습이론의 주장을 지지하는지 반박하는지 평가한다.③은 약화 사례를 강화라고 뒤집는다."
    }
  ],
  "auxiliary": [
    {
      "code": 36,
      "reason": "성문법은 관습을 바꾸지 못한다는 주장에 실제 변화 유발 사례가 반례로 대응한다."
    },
    {
      "code": 46,
      "reason": "관습→법과 법→관습의 방향을 분리해③과④를 구별한다."
    },
    {
      "code": 16,
      "reason": "①에서 자연적으로 형성된 관습과 권위적으로 제도화한 법을 구별한다."
    }
  ],
  "surface": [
    {
      "code": 77,
      "reason": "⑤는 단일 사례의 지지이지 보편 법칙의 최종 증명이 아니다.이 제한이 있으나③ 결정에 표본 일반화 계산은 불필요하다."
    }
  ],
  "competing_codes": [
    {
      "code": 75,
      "rejection": "이론 귀속만 정확해도③의 강화/약화 방향을 틀릴 수 있다.귀속은 선행하되 결정 연산은 증거 역할 평가다."
    },
    {
      "code": 73,
      "rejection": "③의 사례는 이론의 핵심 주장에 반례로 작용한다.별개 논증의 숨은 전제를 찾아 부정하는 단계는 제시되지 않는다.넓은 수용성 평가와는 중첩 가능."
    },
    {
      "code": 74,
      "rejection": "관습이론과 다른 이론의 상반 예측을 동시에 비교하는 것이 아니라 관습이론 하나에 대한 사례의 부합 여부를 본다."
    }
  ],
  "confidence": 0.97,
  "scope_limit": "③의 역사적 효과는 문항에 주어진 평가로만 취급하며 실제 법제사 인과관계를 외부 사실로 확정하지 않는다."
}
```
