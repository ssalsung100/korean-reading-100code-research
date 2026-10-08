

<!-- luna-raw:AQD-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G280",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "관람자의성적소유위치개입불가를일반작품감상방해로확대불가.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AQD-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 17,
      "reason": "관람자의대상소유역할과관계목격·감상역할구별"
    }
  ],
  "auxiliary": [
    {
      "code": 80,
      "reason": "관객이그림여성에게취할수있는인식태도범위"
    },
    {
      "code": 2,
      "reason": "특정개입불가를감상전체불가로강화하지않음"
    },
    {
      "code": 83,
      "scope": "⑤",
      "reason": "실제분류사실과분류되어서는안된다는평가구별"
    }
  ],
  "surface": [
    {
      "code": 42,
      "reason": "그림밖관객이라는위치는있지만공간출입문제아님"
    }
  ],
  "competitors": [
    {
      "code": 13,
      "refutation": "관계에개입못해도관계를목격하고감상하는것과양립"
    },
    {
      "code": 4,
      "refutation": "일부역할제한을모든감상방해로확대하는범위문제로중첩가능"
    },
    {
      "code": 75,
      "refutation": "화가/관객의경쟁견해우열을판정하는문항아님"
    }
  ],
  "counterfactual_probe": "①감상을방해를관객의자기위한전시품이라는해석을막는다로고치면부합.시선자체가독해를불가능하게한것아님.",
  "confidence": 0.96,
  "passage_group": "G280",
  "sdss_disclosed": false
}
```
