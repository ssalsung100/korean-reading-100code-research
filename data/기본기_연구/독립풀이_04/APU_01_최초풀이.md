

<!-- luna-raw:APU-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G277",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "current_session": "blind본문·보기표만읽음;답·태그미열람",
    "historical": "unknown;기존참조0"
  },
  "required_information": [
    "보기:제거→죽음,후견인은불이익가능결정금지→자격상실."
  ],
  "minimal_logic_without_codes": "죽음이 본인에게 불이익일 수 있다는 연결을 넣어야 제거 결정이 금지된 결정 범주에 들어간다.①이 결과와 규범 요건을 잇는다.",
  "intermediate_reasoning": [
    "①죽음→불이익가능의빠진연결",
    "②자기결정독점은다른논거",
    "③후견인의죽음결정권은결론과다른방향",
    "④이익일치만으로죽음불이익연결안됨",
    "⑤결론가능성재진술로전제공백남음"
  ],
  "attractive_wrong_answer": 4,
  "exact_error": "후견인과환자이익일치는그럴듯하지만호흡기제거의결과가환자불이익인지말해주지않는다.",
  "limitation": "발문이가정한판사의추론을복원한것이며죽음이항상당사자불이익이라는일반가치판정을내린것아님."
}
```
