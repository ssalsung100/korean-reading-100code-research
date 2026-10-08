

<!-- luna-raw:BHF-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G428",
  "selected_answer": 2,
  "confidence": 0.94,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BHF.json",
  "necessary_information": [
    {
      "location": "1문단",
      "evidence": "이념 체계의 비일관성과 특정 정당에 대한 지속 지지를 구분한다."
    },
    {
      "location": "2문단",
      "evidence": "근접은 유권자-정당 직접 거리, 방향은 원점에 대한 양자의 거리와 방향으로 효용을 계산한다."
    },
    {
      "location": "3~5문단",
      "evidence": "후기는 심리적 요소를 수용했으나 이론 간 경쟁은 유지. 세련된 유권자 입증 근거는 이념에 기초한 실제 선택이다."
    }
  ],
  "minimal_logic_without_codes": "양 이론은 이념적 위치 관계로 효용과 선택을 설명한다. 후기의 보완은 이론 간 이견 해소나 이념 비중 증가를 뜻하지 않으며 정당 일체감 자체의 합리화가 실증 근거도 아니다.②가 가장 적절하다.",
  "intermediate_reasoning": [
    "①이념 체계가 일관되지 않다는 말과 투표 선택이 일관되지 않다는 말을 혼동한다. 지속적 지지가 본문 현상이다.",
    "③경쟁을 계속 유지했다는 마지막 문단과 충돌한다.④심리 개념 추가를 이념 비중 증가라고 바꾼다.⑤실증된 선택의 근거를 정당 일체감 인정으로 바꾼다.",
    "②의 거리 표현은 근접과 방향의 계산을 포괄하는 느슨한 기술이다. 두 이론이 동일한 유권자-정당 직접 거리를 최소화한다는 뜻으로 읽으면 틀리므로 그 범위는 보존한다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "심리적 개념 수용과 세련된 유권자 가설 입증을 연결하지만 입증 근거는 이념 기반 선택의 실증이지 정당 일체감을 합리적이라고 인정한 것이 아니다."
  }
}
```
