

<!-- luna-raw:BPR-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G502",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "원하는 대로 상상하는 것과 실제 참이라고 믿는 것은 다르며, 후자가 더 어렵다는②가 본문의 문제 제기와 맞는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BPR-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G502",
  "minimal_logic_without_codes": "상상하거나 믿는 듯 행동하는 것과 내용을 참이라고 실제로 믿는 것은 다른 능력이다. 이를 구분하면②의 어려움 비교가 성립한다.",
  "primary": [
    {
      "code": 16,
      "reason": "믿음·상상·가정적 행동과 수의적 즉각 변화의 개념 조건을 구별한다."
    }
  ],
  "auxiliary": [
    {
      "code": 80,
      "reason": "참이라고 여기는 인식적 태도와 단순 표상을 구분한다."
    },
    {
      "code": 2,
      "reason": "원하는 대로 할 수 있음과 실제 믿음을 형성할 수 있음의 가능성 범위를 나눈다."
    },
    {
      "code": 3,
      "reason": "장기간의 간접 영향과 즉각적 선택을 같은 시점의 수의성으로 처리하지 않는다."
    },
    {
      "code": 10,
      "reason": "의무·책임에는 행위 선택 능력이 필요하다는⑤의 방향을 유지한다."
    }
  ],
  "surface": [
    {
      "code": 78,
      "reason": "의지와 행위가 소재이나②는 특정 행동의 실제 동기를 새로 설명하는 문제가 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "상상과 믿음이 서로 다른 개념이라고 동시에 가질 수 없는 태도로 단정하지 않는다."
    },
    {
      "code": 46,
      "rejection": "습관이 믿음에 영향을 주는 인과와 즉각적 수의성의 개념 조건을 구분한다."
    },
    {
      "code": 4,
      "rejection": "모든 믿음이 불가능하다는 전칭 논쟁을②의 상상/믿음 구별에 먼저 확정할 필요는 없다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
