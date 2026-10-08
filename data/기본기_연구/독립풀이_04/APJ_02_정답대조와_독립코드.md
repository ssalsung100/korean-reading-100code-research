

<!-- luna-raw:APJ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G274",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "부차적인간행위기여를관여불가로강화.행위도덕평가와역사결과도덕설명은분리.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APJ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 1,
      "reason": "부차적기여와기여없음의양·유무차이"
    }
  ],
  "auxiliary": [
    {
      "code": 2,
      "reason": "관여할수없다는불가능성강화"
    },
    {
      "code": 46,
      "reason": "시세기본/행위부차의역사전개기여"
    },
    {
      "code": 83,
      "reason": "사실전개와도덕평가분리"
    }
  ],
  "surface": [
    {
      "code": 9,
      "reason": "중요도서열은있지만낮은서열이없음아님"
    }
  ],
  "competitors": [
    {
      "code": 13,
      "refutation": "시세와행위의완전양립불가를주장한것아님"
    },
    {
      "code": 4,
      "refutation": "모든인간행위를배제하는범위도포함하나핵심은부차적요인을0으로변형"
    },
    {
      "code": 79,
      "refutation": "역사인과에대한도덕설명배제를행위도덕판정금지로넓히면오류"
    }
  ],
  "counterfactual_probe": "①관여할수없다를부차적으로관여한다로수정하면명시문장부합.역사결과의선악귀속을거부해도행위자체의선악평가는남는다.",
  "confidence": 0.97,
  "passage_group": "G274",
  "sdss_disclosed": false
}
```
