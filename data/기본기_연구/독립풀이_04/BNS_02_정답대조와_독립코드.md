

<!-- luna-raw:BNS-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G484",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "보기는 일반 가문·왕가 세자·왕위 계승 뒤의 지위에 따라 적용을 구분한다.①은 그 기준이 나라 안 모든 질서에 일관되게 적용된다고 확대하므로 부적절하다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BNS-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G484",
  "minimal_logic_without_codes": "보기는 일반 친족 질서와 왕가의 세자·군주 지위를 구분해 대우 원칙을 달리 적용한다. 이를 나라 안 모든 질서에 같은 기준이 관철된다고 확대하는①은 부적절하다.",
  "primary": [
    {
      "code": 4,
      "reason": "특정 지위·영역에서 적용되는 원칙을 모든 질서에 일률 적용한다는 범위 확대가①의 직접 오류다."
    }
  ],
  "auxiliary": [
    {
      "code": 75,
      "reason": "보기와 갑·을·글쓴이의 부분적 일치 지점을 각각 유지한다."
    },
    {
      "code": 8,
      "reason": "군주 지위를 고려하는 단계에서는 어머니의 아들이라는 친족 지위만으로 판단하지 않는다."
    },
    {
      "code": 24,
      "reason": "일반 가문의 장자·중자 복제와 왕가의 세자 대우를 구분한다."
    },
    {
      "code": 17,
      "reason": "장자라는 정의상 신분과 장자와 같은 대우를 받는 지위를 혼동하지 않는다."
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "세자 이전·세자·즉위 뒤 구분이 있으나 시간의 경과 자체보다 각 지위에 적용되는 규칙 차이가 중요하다."
    }
  ],
  "competing_codes": [
    {
      "code": 18,
      "rejection": "장자가 아니면서 장자와 같은 대우를 받는 것은 동일 술어에 대한 동시 긍정·부정이 아니다."
    },
    {
      "code": 13,
      "rejection": "보기는 갑·을과 서로 다른 논점에서 일치할 수 있으므로 이론 간 모든 논점의 전면 배타를 전제하지 않는다."
    },
    {
      "code": 21,
      "rejection": "장자 정의는 필요하지만①의 결정점은 정의의 양방향 추론이 아니라 규칙 적용 범위다."
    }
  ],
  "confidence": 0.93,
  "sdss_seen": false,
  "scope_limit": "보기의 왕에 대한 구체 복제를 새로 확정하지 않는다. 세자 대우와 군주 지위의 문장 범위 안에서 판단한다."
}
```
