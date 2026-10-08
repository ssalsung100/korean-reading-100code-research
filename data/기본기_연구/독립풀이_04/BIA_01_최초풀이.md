

<!-- luna-raw:BIA-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G435",
  "selected_answer": 4,
  "confidence": 0.94,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BIA.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G435_visual04.md"
  ],
  "necessary_information": [
    {
      "location": "이익분배/정보확산/정당이익 문단",
      "evidence": "상임위 간 혜택교환 약속,본회의 다수선호 실현,다수당 지도부의 상임위 통제를 각각 강조."
    },
    {
      "location": "규칙 정의 및 보기",
      "evidence": "수정불가는 통과안을 변경 없이 가부,수정허용은 본회의의 새로운 수정 가능."
    }
  ],
  "minimal_logic_without_codes": "지역구 혜택 교환 약속은 본회의에서 내용이 바뀌지 않는 수정불가에서 보호된다.수정허용은 본회의 다수 선호를 반영하기 쉽고,수정불가는 다수당이 통제한 상임위안을 유지하기 쉽다.ㄴㄷ인④.",
  "intermediate_reasoning": [
    "ㄱ은 수정 기회 확대를 곧 투표 거래 약속의 안정성 증가로 바꾸지만 본회의 수정은 상임위 간 합의된 혜택을 변경할 수 있다.",
    "ㄴ은 본회의 중심 정보확산 이론에서 지역구 편향안을 본회의가 수정할 기회를 제공한다는 가능성 예측으로 맞는다.",
    "ㄷ은 지도부가 상임위 구성·운영을 통제한 뒤 본회의 소수당 수정활동을 제한하는 제도효과와 연결된다.",
    "어느 규칙도 특정 정책 생산을 현실에서 항상 보장한다는 뜻은 아니다.각 이론이 주목한 이해와 통제 위치에 따른 정성적 예상이다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "규칙상 수정의 자유가 늘면 어떤 이론에서도 원하는 결과가 더 많아진다고 단순화해ㄱ까지 포함한다.기존 혜택교환 약속을 지키는 데 수정 가능성은 오히려 제약 요인이 될 수 있다."
  },
  "unresolved": "ㄱ의 모든 가능한 거래 증가 상황을 논리적으로 불가능하다고 주장하지 않는다.본문의 거래 약속 안정성을 중심으로 한 상대적 제도예측이다."
}
```
