

<!-- luna-raw:AOU-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G269",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "질문지는실험목적위장절차이며내용차이를조작한독립변인이아님.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false,
  "provenance_limit": "봉인원장공식페이지검증정본연결을사용.이번대조에서공식정답표원본을새로열지는않음."
}
```


<!-- luna-raw:AOU-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 43,
      "reason": "실험에서조작·통제·위장절차각역할을구별"
    }
  ],
  "auxiliary": [
    {
      "code": 44,
      "reason": "질문지의실제목적과가정된내용효과측정목적대조"
    },
    {
      "code": 17,
      "reason": "절차요소의기능귀속"
    }
  ],
  "surface": [
    {
      "code": 93,
      "reason": "질문응답소통이있지만메시지내용효과를실험한것아님"
    }
  ],
  "competitors": [
    {
      "code": 46,
      "refutation": "원인효과탐색의설계이나질문지내용효과가측정되었다는근거는없음"
    },
    {
      "code": 53,
      "refutation": "차이가없는질문지조건에서그내용효과의차이를찾을수없음.원리로보조가능하나설계역할확인이선행"
    },
    {
      "code": 74,
      "refutation": "전체가경쟁이론검증이지만④직접오류는조작변인발명"
    }
  ],
  "counterfactual_probe": "질문지내용만다르게한조건을추가하고나머지를동일하게하면④의설계목적이가능.현설계에는그조작없음.",
  "confidence": 0.96,
  "passage_group": "G269",
  "sdss_disclosed": false
}
```
