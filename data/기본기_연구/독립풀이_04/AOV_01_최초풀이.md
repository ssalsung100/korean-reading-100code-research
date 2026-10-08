

<!-- luna-raw:AOV-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G269",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "current_session": "blind-only본문·G269_visual01표만읽음;답·태그미열람",
    "historical": "unknown;기존참조0"
  },
  "required_information": [
    "표:A가행복/나분노,B와C모두무반응. A/C는사전약효정보가없는조건이며각성유무가다름."
  ],
  "minimal_logic_without_codes": "⑤는 A/C 비교에서 실제 달라진 각성을 사전정보 차이로 잘못 해석한다. 같은 비교를 가/나에서 반복해도 변하지 않은 사전정보의 효과는 추론할 수 없다.",
  "intermediate_reasoning": [
    "①B나에각성있어도무반응이므로각성만의충분성부정지지",
    "②B/C에서협력자태도만달라도정서유발안됨",
    "③가행:A/B는정보,A/C는각성차이와반응차이",
    "④A와C각행비교로각성, A내행차이로맥락연결",
    "⑤A/C정보변인조작없고실제차이는각성"
  ],
  "attractive_wrong_answer": 1,
  "exact_error": "B/C가모두무반응이라는것은각성영향이항상0임을보이지않는다.각성만으로충분하지않다는국소가설과구별.",
  "limitation": "각비교의통계적유의성은주어지지않으며발문수준의가설지지방향만판정."
}
```
