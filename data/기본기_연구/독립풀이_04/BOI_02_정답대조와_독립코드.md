

<!-- luna-raw:BOI-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G490",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "크세노폰은 관계 전체를 불명예로 한정하지 않고 특정 조건의 관계를 비판한다.②는 일부 조건에 대한 평가를 역할을 가진 사람 전부의 정의로 확대한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BOI-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G490",
  "minimal_logic_without_codes": "일정한 태도를 보인 경우만 비판하는 크세노폰의 판단을 해당 역할을 가진 모든 사람의 속성으로 바꾼②를 배제한다.",
  "primary": [
    {
      "code": 4,
      "reason": "조건부 부분에 해당하는 평가를 역할 전체의 한정 정의로 넓힌다."
    }
  ],
  "auxiliary": [
    {
      "code": 12,
      "reason": "특정 태도라면 불명예라는 조건의 전건을 누락하지 않는다."
    },
    {
      "code": 75,
      "reason": "서로 다른 역사가의 평가를 주체별로 귀속한다."
    },
    {
      "code": 16,
      "reason": "역할 이름 자체의 정의와 그 역할 수행 방식의 평가를 구별한다."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "명예에 관한 규범적 평가이지만 독자가 새로운 당위를 정하는 것은 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "우정 가능성과 특정 태도 비판은 서로 양립할 수 있어 역할 전체의 불가능으로 바꾸면 안 된다."
    },
    {
      "code": 2,
      "rejection": "필연/가능 강도도 관련되나②의 직접 조작은 평가 대상의 범위를 전체로 넓힌 데 있다."
    },
    {
      "code": 21,
      "rejection": "평가 조건을 역할의 필요충분 정의로 격상할 근거가 없다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
