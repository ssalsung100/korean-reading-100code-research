

<!-- luna-raw:BOL-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G491",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "초기 반발이 시간이 지나 수용으로 바뀌면 긍정적 반응 모델의 방향에 가까워진다.③이 본문에 맞는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_restoration_before_disclosure": false
}
```


<!-- luna-raw:BOL-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G491",
  "minimal_logic_without_codes": "처음에는 반발하던 여론도 시간이 지나 결정을 수용하는 방향으로 바뀔 수 있어 두 모델의 예상 반응이 수렴한다.",
  "primary": [
    {
      "code": 5,
      "reason": "초기 반발 상태에서 이후 수용 상태로 변화하는 흐름을 읽는다."
    }
  ],
  "auxiliary": [
    {
      "code": 3,
      "reason": "즉각적 반응과 시간이 지난 반응을 같은 시점의 성질로 합치지 않는다."
    },
    {
      "code": 74,
      "reason": "네 모델이 설명하는 반응 양상을 각기 유지한다."
    },
    {
      "code": 2,
      "reason": "시간에 따른 수렴은 경향이며 모든 사례의 필연적 결과가 아니다."
    },
    {
      "code": 49,
      "reason": "반발 감소와 수용 증가의 방향을 대응한다."
    }
  ],
  "surface": [
    {
      "code": 86,
      "reason": "지문에 일치도 비율이 있으나③은 정확 비율의 계산이 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "초기 반발 모델과 나중 수용 모델은 서로 다른 시간에서 같은 사례를 설명할 수 있어 전면 배타가 아니다."
    },
    {
      "code": 57,
      "rejection": "여러 모델이 있다고 특정 조건에서 가지를 선택하는 분기 규칙이 주어진 것은 아니다."
    },
    {
      "code": 91,
      "rejection": "시간이 늘면 일정 비율로 반발이 줄어든다는 수학적 법칙은 없다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
