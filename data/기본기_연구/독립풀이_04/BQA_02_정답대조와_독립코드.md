

<!-- luna-raw:BQA-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G505",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "사례1은 대안이 없어도 실제 자유롭게 결심한 행위에 책임을 부여하는 사례다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "scope_limit": "결심/심적 무위/결과의 책임을 구별하고 논자의 논증 목적을 최종 입증과 동일시하지 않는다."
}
```


<!-- luna-raw:BQA-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G505",
  "minimal_logic_without_codes": "책임이 있으려면 다른 선택이 가능해야 한다는 원칙에 사례1은 책임은 있지만 다른 선택은 불가능한 경우를 제시한다.",
  "primary": [
    {
      "code": 36,
      "reason": "대안가능성이 없어도 책임이 있는 사례를 확인하는②는 필요조건 주장에 대한 반례를 찾는다."
    }
  ],
  "auxiliary": [
    {
      "code": 10,
      "reason": "책임에 대안가능성이 필수라는 원칙의 방향을 고정한다."
    },
    {
      "code": 2,
      "reason": "실제 결심의 자유와 다른 결과의 가능성을 구별한다."
    },
    {
      "code": 79,
      "reason": "판정 대상은 행위자의 도덕적 책임이다."
    }
  ],
  "surface": [
    {
      "code": 26,
      "reason": "행위/무위 대비가 있지만②는 그 대비보다 원칙의 반례 확인에 초점을 둔다."
    }
  ],
  "competing_codes": [
    {
      "code": 37,
      "rejection": "일반 사례 대입도 가능하지만 원문 원칙을 만족하지 않는 책임 사례라는 반증 역할이36을 구체화한다.두 번호를 인위적 배타로 만들지는 않는다."
    },
    {
      "code": 46,
      "rejection": "행위가 결과의 원인이라는 점만으로 책임이 자동 결정되지 않는다.반례는 책임과 대안가능성의 관계에 관한 것이다."
    },
    {
      "code": 34,
      "rejection": "무위는 비난이 전혀 없다는①의 전칭 부정이 본문 입장이 아니다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
