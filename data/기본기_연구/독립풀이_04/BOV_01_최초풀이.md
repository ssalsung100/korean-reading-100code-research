

<!-- luna-raw:BOV-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G494",
  "selected_answer": 1,
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
      "location": "엄격한 기준 열거",
      "evidence": "한 주기 난자 수정 최대3, 배아 이식 최대3, 이식할 수보다 많이 수정 금지, 온전한 착상 전 채취 금지."
    },
    {
      "location": "예외·역설 설명",
      "evidence": "결함 배아의 불가피한 배제 가능성을 언급하고 착상 뒤 일부 제거되는 현실을 서술한다."
    }
  ],
  "minimal_logic_without_codes": "①은3개 상한과 이식 예정 수량에 맞춘 수정 제한을 결합해 재진술한다.",
  "intermediate_reasoning": [
    "② 착상 전 채취 금지를 착상 후 분리 금지로 옮겼다.",
    "③ 보존 자체는 금지되지 않으며 이식 불가능하면 반드시 폐기한다는 규정은 제시되지 않았다.",
    "④ 수정 제한을 난자 채취·보관 제한으로 바꿨다.",
    "⑤ 결함이 있는 배아를 불가피하게 배제하는 경우를 지워 어떤 경우에도 적게 이식할 수 없다고 했다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "원칙상 전부 이식한다는 요약만 기억하고 뒤 문단의 결함 예외를 제거해 전칭적으로 강화한다."
  }
}
```
