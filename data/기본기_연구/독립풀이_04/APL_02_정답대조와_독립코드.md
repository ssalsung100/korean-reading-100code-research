

<!-- luna-raw:APL-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G274",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "특수하고무법칙적인시세를무시하고과거성패에서현재추이를법칙적으로전망하는태도와상충.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APL-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 77,
      "reason": "특수한과거성패에서현재추이를일반법칙으로확장하는문제"
    }
  ],
  "auxiliary": [
    {
      "code": 83,
      "reason": "도덕평가와역사사실을분리해읽음"
    },
    {
      "code": 63,
      "reason": "편견적역사서술의신뢰성을검토"
    },
    {
      "code": 46,
      "reason": "선악·지모가성패를필연결정한다는인과서술비판"
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "과거/현재대조는있으나핵심은전이가능성"
    }
  ],
  "competitors": [
    {
      "code": 74,
      "refutation": "두가설의차별예측을검증하는실험이아님"
    },
    {
      "code": 18,
      "refutation": "선속악등을논리모순이라고배제하면기록의일면성비판을놓침"
    },
    {
      "code": 80,
      "refutation": "독자의태도문항이지만구체오독은시세특수성을무시한법칙적전망"
    }
  ],
  "counterfactual_probe": "②를과거성패의원인과특수여건을다시검토한다로바꾸면⑤와가까워짐.과거사실로부터어떠한정보도배울수없다는강한회의는도출안함.",
  "confidence": 0.95,
  "passage_group": "G274",
  "sdss_disclosed": false
}
```
