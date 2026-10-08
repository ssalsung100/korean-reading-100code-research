

<!-- luna-raw:ANY-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G261",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "기록 대상의 여러 가문과 편찬·간행의 한 가문 계보를 구별.",
  "original_blind_preserved": true,
  "barrier": "group 전체 blind 저장 확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:ANY-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 17,
      "reason": "기록된 인물과 편찬·간행 주체의 역할 구분"
    }
  ],
  "auxiliary": [
    {
      "code": 98,
      "reason": "누구의 업적인지와 누구의 편찬인지 구별"
    },
    {
      "code": 40,
      "scope": "④",
      "reason": "하나의 책에 여러 형식 글이 포함"
    }
  ],
  "surface": [
    {
      "code": 4,
      "reason": "여러라는 수량보다 그 수량을 귀속한 대상이 핵심"
    }
  ],
  "competitors": [
    {
      "code": 31,
      "refutation": "원소수와집합수를계산하는문제아니며편찬주체를구별하면충분"
    },
    {
      "code": 3,
      "refutation": "부자와후손의순서가도움되지만여러시대의기록을공동간행으로바꾼역할오류"
    },
    {
      "code": 93,
      "refutation": "글쓴이/독자소통의도보다실제편찬자식별이핵심"
    }
  ],
  "counterfactual_probe": "②의 여러가문이함께간행을한가문부자의저술을후손이간행으로고치면부합.다양한기록대상을다양한출판주체로치환하지않음.",
  "confidence": 0.95,
  "passage_group": "G261",
  "sdss_disclosed": false
}
```
