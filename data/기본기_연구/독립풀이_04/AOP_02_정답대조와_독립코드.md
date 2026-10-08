

<!-- luna-raw:AOP-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G267",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2014/2014_answer_2014학년도_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "광범위투자자보유를일부고수익투자자한정으로축소.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AOP-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 4,
      "reason": "투자자범위를광범위에서일부특정집단으로한정"
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "대출채무자신용과증권투자자성향을구별"
    },
    {
      "code": 46,
      "scope": "②③④",
      "reason": "증권화·과신·차입·거품·연쇄위기경로"
    }
  ],
  "surface": [
    {
      "code": 41,
      "scope": "②",
      "reason": "개별위험감소처럼보이는것을전체위험감소로합성하지않음"
    }
  ],
  "competitors": [
    {
      "code": 1,
      "refutation": "규모가작다는채권양과투자자분포범위는다름.정답은해당집단한정"
    },
    {
      "code": 43,
      "refutation": "위기원인논쟁있어도①배제에통제실험분석은필요없음"
    },
    {
      "code": 74,
      "refutation": "경쟁설설명은⑤배경이고①은광범보유명시로직접판정"
    }
  ],
  "counterfactual_probe": "①의일부에한정을다양한광범위투자자로바꾸면참.작은원대출규모에서좁은투자자범위를추론하지않음.",
  "confidence": 0.96,
  "passage_group": "G267",
  "sdss_disclosed": false
}
```
