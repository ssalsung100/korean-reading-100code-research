

<!-- luna-raw:BQO-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G509",
  "selected_answer": 4,
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
      "location": "범죄 정의",
      "evidence": "구성요건·위법성·책임 중 하나라도 빠지면 범죄가 성립하지 않는다."
    },
    {
      "location": "㉡ 정의",
      "evidence": "긴급피난이 성립하여 위법성이 없다고 파악하는 사람."
    },
    {
      "location": "정당방위/긴급피난 구분",
      "evidence": "긴급피난은 위법한 침해에 의한 위난일 필요가 없다."
    }
  ],
  "minimal_logic_without_codes": "㉡은 이미 위법성을 부정하므로 범죄 불성립이 결정된다.책임까지 따져야만 범죄 성립 여부가 정해진다는④는㉡의 전제와 맞지 않는다.",
  "intermediate_reasoning": [
    "① 정당방위 입장은 방어 대상이 현재 위법한 침해여야 하므로 B의 행위를 그렇게 볼 것이다.",
    "② 정당방위 주장은 A가 현재의 침해를 방어했다는 목적을 전제한다.",
    "③ 긴급피난은 위난의 원인이 위법한 침해일 필요가 없으므로 맞는다.",
    "⑤ 두 견해 모두 현재 위난과 상당한 이유를 긍정해야 자신의 정당화 주장을 할 수 있다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "필자가 B의 행위를 위법한 침해로 인정하지 않는다는 사실을 정당방위를 주장하는㉠의 가정에 그대로 덮어씌우면 안 된다."
  },
  "scope_limit": "책임을 철학적으로 논의하는 것이 금지된다는 뜻이 아니라 해당 범죄 성립 판정을 위해 더 확인할 필요가 없다는 뜻이다."
}
```
