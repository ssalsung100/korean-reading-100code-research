

<!-- luna-raw:BPV-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G503",
  "selected_answer": 5,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "2문단 도구변수 조건",
      "evidence": "z는 x와 상관관계가 크되 x 외에 y에 영향을 주는 다른 요인과 상관관계가 없어야 한다."
    },
    {
      "location": "끝 문단 재반박",
      "evidence": "과거 유럽인 사망률은 제도를 통한 영향을 제외하면 현재 소득과 상관관계가 없다는 주장."
    }
  ],
  "minimal_logic_without_codes": "과거 정착민 사망률→이주→기술→소득이라는 제도 밖 경로를 중요하게 인정하면 선택한 도구변수의 조건이 깨진다. 그러므로⑤의 경로를 중요한 설명으로 보지 않을 것이다.",
  "intermediate_reasoning": [
    "① 당시 유럽인 사망률에 대한 주장을 오늘날 사망률로 바꾼다.",
    "② 원주민과 유럽인 사망률을 구분하는 반박과 다르다.",
    "③ 과거 제도와 현재 제도 사이 지속성과 높은 관련성을 완전 결정으로 강화한다.",
    "④ 도구변수를 써서 역인과 영향을 분리하려는 본문의 방법과 반대다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "과거 제도가 현재에 영향을 미치고 높은 상관이 남아 있다는 것과 현재 값이 과거 정책에 의해 이미 완전히 결정됐다는 것은 다르다."
  },
  "scope_limit": "⑤는 기술 도입 사건이 아예 없었다는 역사적 단정이 아니라 저자의 도구변수 정당화에서 해당 우회 경로를 중요한 요인으로 인정하지 않는다는 판정이다."
}
```
