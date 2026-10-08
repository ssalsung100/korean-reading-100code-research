

<!-- luna-raw:AOL-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G265",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2013/2013_answer_2013_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "A는우연외형변형이므로기저본질변화를목적으로했다는③오류.더큰영향은다른요인의영향0을뜻하지않음.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AOL-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 43,
      "reason": "외형변화와변화원인정보,첫부분/전체읽기조건을구별하여실험설계해석"
    }
  ],
  "auxiliary": [
    {
      "code": 5,
      "reason": "환경외형변화와기저본질유지구별"
    },
    {
      "code": 74,
      "reason": "판단일치여부에대한유사성/설명접근의예측대조"
    },
    {
      "code": 63,
      "reason": "관측불일치가립스가설을지지"
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "평균값은판단차이를확인할뿐복잡계산불필요"
    }
  ],
  "competitors": [
    {
      "code": 53,
      "refutation": "통제/실험차이가단서지만본문은통계적유의성이나완전통제증명을주지않음.가능한영향해석을독점인과로강화금지"
    },
    {
      "code": 13,
      "refutation": "외형기반과본질기반영향이완전배타적이라고하면④와충돌"
    },
    {
      "code": 36,
      "refutation": "불일치는유사성만으로판단한다는강한모형을흔들지만모든유사성기여를반박하는것아님"
    }
  ],
  "counterfactual_probe": "A변형을성숙의필연단계로바꾸면동일외형에도본질해석조건이달라진다.B유사성9.5→7.6은본질지식의영향가능성을보이므로유사성은외형만본다는단정불가.",
  "boundary_status": "43/74/63 설계·대체예측·증거평가의연속단계.기저본질정보와외형의상대영향을배타원인으로읽지않음",
  "confidence": 0.95,
  "passage_group": "G265",
  "sdss_disclosed": false
}
```
