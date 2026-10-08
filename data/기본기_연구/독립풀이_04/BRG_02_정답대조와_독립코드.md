

<!-- luna-raw:BRG-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G515",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2012/2012_answer/table_001.md 홀수형33~35(공식 HWP 추출 표)",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "귀가의 현실 종속과 춤의 가부장제 반발을 동시에 읽은③만 밑줄의 두 조건을 충족한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BRG-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G515",
  "sdss_seen": false,
  "primary": [
    {
      "code": 37,
      "reason": "현실 종속과 초월 요구라는 두 특징을 함께 보이는 감상 사례를 찾는다."
    }
  ],
  "auxiliary": [
    {
      "code": 28,
      "reason": "종속되면서도 저항 요구를 품는 양보적 결합을 유지한다."
    },
    {
      "code": 23,
      "reason": "종속과 저항 두 요건의 동시 충족을 확인한다."
    },
    {
      "code": 78,
      "reason": "춤을 가부장제에 대한 반발 동기로 읽는다."
    }
  ],
  "surface": [
    {
      "code": 93,
      "reason": "영화가 대중과 교감하는 과정은 밑줄 이후의 배경이다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "외적 귀가와 내적 저항 요구는 같은 층위의 정반대 명제가 아니므로 양립불가가 아니다."
    },
    {
      "code": 59,
      "rejection": "③은 가부장제를 실제 해결하지 않아도 적절하다.해결 성공을 필요한 조건으로 추가할 수 없다."
    },
    {
      "code": 100,
      "rejection": "춤을 저항으로 읽는다고 언제나 비유 의미 대응은 아니다.행위의 사회적 동기 해석이다."
    }
  ],
  "confidence": 0.95,
  "scope_limit": "37/23/28은 사례 탐색·요건 결합·양보 관계의 층위이며 독립된 세 단계로 과잉 계수하지 않는다."
}
```
