

<!-- luna-raw:BQS-blind-20261005-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G510",
  "selected_answer": 1,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "4문단",
      "evidence": "법률의 헌법 기속과 사법 심사는 대표의 다수결을 제한한다."
    },
    {
      "location": "5문단",
      "evidence": "사법 심사가 공적 토론을 촉발·유도한다면 공화주의적 가치를 재평가할 수 있다."
    }
  ],
  "minimal_logic_without_codes": "헌정주의적 수단은 다수결의 제약을 포함하며 공적 토론을 촉진할 수도 있다. 이를 토론을 선출 투표로 대체하는 작용이라 한 ①은 근거와 방향이 맞지 않는다.",
  "intermediate_reasoning": [
    "② 헌법과 충돌한 법률의 효력을 잃게 하므로 의회 권한 제한과 연결된다.",
    "③ 시민 대표의 다수결에 헌법을 우선시키면 민주주의와 긴장 가능성이 있다.",
    "④ 거부권은 제시된 권력분립·상호견제의 구현으로 해석 가능하다. 본문에 거부권 명칭이 직접 등장한 것은 아니다.",
    "⑤ 법의 지배를 자의적 권력 배제와 연결하는 것은 본문 공화주의 목표에 맞는다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "대통령 거부권의 명칭이 본문에 없다는 이유만으로 배제하면 권력분립의 구체적 구현이라는 적용을 놓친다."
  },
  "scope_limit": "사법 심사는 언제나 토론을 촉진한다고 확정하지 않는다. 마지막 문단은 조건부 재평가다."
}
```
