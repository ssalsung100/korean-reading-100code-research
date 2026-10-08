

<!-- luna-raw:BPD-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G497",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "조각 모델은 제작 도중의 영감에 따라 초기 구상과 희곡을 바꿀 수 있다. 작가의 말을 확고한 지침으로 고정한④는 심포니식 절대성을 옮긴다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "confidence_after_check": 0.99,
  "remaining_uncertainty": "추가 없음"
}
```


<!-- luna-raw:BPD-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G497",
  "minimal_logic_without_codes": "조각 모델의 수정 가능한 초기 구상에 심포니 모델의 절대적 지침 지위를 옮긴④를 배제한다.",
  "primary": [
    {
      "code": 17,
      "reason": "희곡의 절대성·수정 가능성을 어느 모델에 귀속하는지 구분한다."
    }
  ],
  "auxiliary": [
    {
      "code": 75,
      "reason": "세 모델의 희곡-공연 관계를 비교한다."
    },
    {
      "code": 5,
      "reason": "작업 중 영감에 따른 구상 변화를 허용하는지 추적한다."
    },
    {
      "code": 2,
      "reason": "자료로 참조함과 확고한 지침으로 구속됨의 강도를 나눈다."
    },
    {
      "code": 69,
      "reason": "악보·영화 제작·조각이라는 비유의 관계 구조를 연극 제작에 대응한다."
    }
  ],
  "surface": [
    {
      "code": 9,
      "reason": "희곡과 연출의 상대 위계가 있지만 단순 높낮이보다 제작 중 수정 가능성이 결정점이다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "조각 모델이 희곡을 참조하는 것까지 금지한 것은 아니므로 참조와 자유로운 변형을 배타로 두지 않는다."
    },
    {
      "code": 94,
      "rejection": "새 영감이 필요하다고 초기 구상이 전혀 없어야 한다는 뜻은 아니다."
    },
    {
      "code": 20,
      "rejection": "여러 모델이 존재한다는 것만으로 같은 목적의 대체 충분조건들이 모두 입증된 것은 아니다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
