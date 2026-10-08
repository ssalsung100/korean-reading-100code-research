

<!-- luna-raw:BPQ-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G501",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "중종은 새 방식 마련을 지시하면서 추천의 폐단도 경계하므로①이 맞는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BPQ-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G501",
  "minimal_logic_without_codes": "중종은 새 방식의 마련과 추천 폐단의 경계를 함께 말한다. 도입 지시가 모든 위험의 부정을 뜻하지 않는다.",
  "primary": [
    {
      "code": 75,
      "reason": "대화 속 인물별 찬성·반대·조건부 경계의 입장을 구분한다."
    }
  ],
  "auxiliary": [
    {
      "code": 14,
      "reason": "도입 추진과 폐단 경계가 함께 성립할 수 있음을 유지한다."
    },
    {
      "code": 19,
      "reason": "천거를 기존 제도의 보완으로 도입한다는 관계를 전면 대체로 바꾸지 않는다."
    },
    {
      "code": 99,
      "reason": "김정의 사소한 폐단이 앞서 지적된 천거의 한계를 가리킴을 복원한다."
    },
    {
      "code": 17,
      "reason": "김정을 반대 집단에 잘못 넣거나 남곤의 반대를 찬성으로 옮기지 않는다."
    }
  ],
  "surface": [
    {
      "code": 63,
      "reason": "서로 비판하지만①의 직접 행동은 중종 발언의 복합 입장 요약이다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "찬성하면 우려를 말할 수 없다는 배타적 분류를 적용하면 중종의 실제 발언을 잃는다."
    },
    {
      "code": 20,
      "rejection": "새 수단이 기존 수단을 완전히 불필요하게 만드는 대체 관계가 명시되지 않았다."
    },
    {
      "code": 65,
      "rejection": "선지가 왜곡한 내용은 있으나 상대 논증을 공격하는 허수아비 구조를 새로 만들어 판단하는 것은 아니다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
