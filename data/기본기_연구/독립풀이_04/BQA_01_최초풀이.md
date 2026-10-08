

<!-- luna-raw:BQA-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G505",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "사례1과 해설",
      "evidence": "실제로 자유롭게 결심하고 행동했으므로 대안가능성이 없어도 책임을 부여한다."
    },
    {
      "location": "첫문단",
      "evidence": "무위는 덜 비난받으며 대안가능성 원칙도 상식적으로 받아들여진다."
    }
  ],
  "minimal_logic_without_codes": "다르게 행동할 수 없었어도 실제 자신의 결심으로 행동해 책임을 지는 사례1이②의 사례다.",
  "intermediate_reasoning": [
    "① 덜 비난받음을 전혀 비난받지 않음으로 바꾼다.",
    "③ 비대칭성은 대안의 유무가 아니라 대안이 없는 같은 조건에서 책임 판단이 다른 것이다.",
    "④ 사례1의 최초 역할은 대안가능성이 책임의 필수 조건이라는 원칙에 대한 반례이며 대칭성 논증은 사례3에서 구성된다.",
    "⑤ 본문은 대안가능성 원칙도 상식적으로 수용된다고 한다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "두 경우 모두 결과가 달라질 수 없는데 책임 여부가 다르다는 조건을 행위에만 대안이 없다는 차이로 옮긴다."
  }
}
```
