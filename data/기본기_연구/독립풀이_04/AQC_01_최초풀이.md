

<!-- luna-raw:AQC-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G280",
  "selected_answer": 5,
  "confidence": 0.98,
  "exposure": {
    "current_session": "blind-only,답·태그미열람",
    "historical": "unknown;기존참조0"
  },
  "required_information": [
    "4문단:드러남/전시구별,피부·체모를가장수단으로삼음,일종의복장."
  ],
  "minimal_logic_without_codes": "복장은 실제 옷이 아니라 보는 사람을 위해 전시물로 구성되어 이미 꾸며진 외관이라는 뜻이다.⑤가 문맥을 보존한다.",
  "intermediate_reasoning": [
    "①판단자의적이라는결론없음",
    "②도덕적수치심평가아님",
    "③모든표정/자세가거짓이라는필수조건은과도",
    "④실제옷입은누드존재의논증아님",
    "⑤전시자체가구성과가장"
  ],
  "attractive_wrong_answer": 3,
  "exact_error": "가장이라는표현을모델의거짓표정연기만으로좁히면피부·체모를포함한전시구성전체를놓침."
}
```
