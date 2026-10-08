

<!-- luna-raw:APM-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G275",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "상영장소/광고/유통의차이를성인관람대상차이로바꿈.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APM-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 17,
      "reason": "규제대상인영화/장소/관객범주를구별"
    }
  ],
  "auxiliary": [
    {
      "code": 39,
      "reason": "두등급의차이축을대조"
    },
    {
      "code": 23,
      "reason": "성인관람대상공통"
    }
  ],
  "surface": [
    {
      "code": 5,
      "reason": "제도변화는⑤근거이나정답은대상차이추가"
    }
  ],
  "competitors": [
    {
      "code": 13,
      "refutation": "두등급이달라도관람성인집합은겹칠수있음"
    },
    {
      "code": 79,
      "refutation": "규제가정당한지결정하는문항아님"
    },
    {
      "code": 2,
      "refutation": "허용여부강도도있지만④는허용대상범주가핵심"
    }
  ],
  "counterfactual_probe": "④관람허용대상을상영허용장소로바꾸면참.등급차이에서모든차원이다르다고추론하지않음.",
  "confidence": 0.96,
  "passage_group": "G275",
  "sdss_disclosed": false
}
```
