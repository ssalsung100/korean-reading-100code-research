

<!-- luna-raw:BOA-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G487",
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
      "location": "마지막 문단",
      "evidence": "양육친 가정폭력 때문에 도피한 사례가 많아졌고 중대한 위험을 이유로 반환 거절이 가능하다."
    },
    {
      "location": "협약 목적·조건 문단",
      "evidence": "원래 살던 나라에서 양육권을 정하게 하며 같은 국적도 적용, 양쪽 본국 모두 가입 필요, 동의한 이동 뒤 반환 거부도 위법할 수 있다."
    }
  ],
  "minimal_logic_without_codes": "폭력 있는 양육친에게 즉시 돌려보내면 자녀의 복리에 맞지 않을 수 있으므로 신속 반환과 복리 원칙이 충돌하는 사례가 늘었다는②가 타당하다.",
  "intermediate_reasoning": [
    "① 원래 살던 나라와 현재 체류국을 바꿨다.",
    "③ 같은 국적에도 협약이 적용된다고 명시된다.",
    "④ 양쪽 본국 가입 요건을 하나만 가입한 상황으로 완화했다.",
    "⑤ 귀국을 전제로 허락받고 나간 뒤 반환을 거부하면 위법성이 인정될 수 있으므로 최초 동의만으로 이후 적법성이 고정되지 않는다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "처음의 이동 동의를 귀국 조건 없이 영구적인 적법성 보장으로 읽어 이후 반환 거부의 조건 변화를 지운다."
  },
  "scope_limit": "가정폭력 사례의 지문상 예외 논리만 분석한다."
}
```
