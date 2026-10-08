

<!-- luna-raw:BLA-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G461",
  "selected_answer": 5,
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
      "location": "ⓓ",
      "evidence": "이효손은 이 씨를 위해3년,훗날 이성손은백 씨를 위해3년 상복."
    },
    {
      "location": "ⓔ",
      "evidence": "이 씨를첩모로강등해첩모용상복을입자고함."
    },
    {
      "location": "ⓐ~ⓒ",
      "evidence": "여러적처모두3년,친모와다른적처차등1년,자기모친만복상의주장차이."
    }
  ],
  "minimal_logic_without_codes": "ⓓ는3년을,ⓔ는첩모를위한상복을요구하므로두입장모두상복을입지않아도된다는⑤가명시적주장과맞지않는다.",
  "intermediate_reasoning": [
    "① ⓐ의모든적처동일대우논리를이성손-백씨관계에도적용하면3년이다.",
    "② ⓑ는이씨를첩모로낮추지않으면서친모와같은3년이아닌1년을주장한다.",
    "③ ⓒ는복상적용을각자친모로제한하며이씨를첩으로강등한다는명시요구는ⓔ에있다.기존적처지위와복상의무를구분한다.",
    "④ ⓒ는이효손의이씨복상을요구하지않고ⓓ는3년을요구한다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "정인지는중혼관행의항구법식화를반대한다는것을이미성립한두처모두의적처지위를박탈했다는명제로바꾼다.명시된처방은각자친모에대한복상이다."
  },
  "scope_limit": "첩모상복의정확한기간은본문에없으므로추정하지않는다."
}
```
