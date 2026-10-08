

<!-- luna-raw:BNL-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G482",
  "selected_answer": 4,
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
      "location": "마지막 문단",
      "evidence": "편익·비용 실제 측정에는 한계가 있고 화폐화된 성과를 평가해 기존 이해관계자로부터 회수되지 못한 부분에 보상한다."
    },
    {
      "location": "사회성과 정의 및 계정 측정 문단",
      "evidence": "사회학적 관점도 반영하며 지원금은 비용으로 차감한다."
    }
  ],
  "minimal_logic_without_codes": "사회적 가치 제고가 목적이라면 화폐 측정에서 빠진 편익도 평가하도록 보완해야 한다. 측정 한계를 목적에 비추어 보충하는④이다.",
  "intermediate_reasoning": [
    "① 정부 지원금은 기존 이해관계자의 비용 보전이며 이후 잔여 성과에 대한 보상과 구별한다.",
    "② 배당하는 기업이라는 이유만으로 사회적 편익 창출·미회수 잔여가 없다고 할 수 없다.",
    "③ 사회성과 보상은 사회적 활동에 가격을 부여해 가격 기구에 영향을 준다.",
    "⑤ 사회학적 관점을 반영한 사회성과이므로 규범을 전혀 반영할 수 없다는 근거가 없다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "보상이라는 넓은 일상적 명칭과 본문이 정의한 미회수 편익에 대한 사회성과보상을 동일시한다. 이미 받은 지원금을 다시 잔여 보상에 포함한다."
  },
  "source_limit": "그림 placeholder가 있으나 필요한 정의·측정 한계는 본문에 명시되어 있다."
}
```
