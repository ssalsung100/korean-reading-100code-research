

<!-- luna-raw:BIX-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G443",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2018/2018_answer_2018학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "인권보호취지는정당성의필요조건이다.약한보호는미적용이아니다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.주어진역사적지문모형의독해범위로한정."
  ]
}
```


<!-- luna-raw:BIX-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G443",
  "sdss_seen": false,
  "general_task": "차별금지정당성과보호정도의명시관계확인",
  "decisive_relation": "인권취지부합없음→정당성없음의대우를적용",
  "primary": {
    "code": 10,
    "scope": "①",
    "reason": "인권보호취지부합은정당한차별금지법규의필요조건이다."
  },
  "auxiliary": [
    {
      "code": 12,
      "scope": "①",
      "reason": "¬인권부합→¬정당의대우 정당→인권부합으로같은관계를표현."
    },
    {
      "code": 1,
      "scope": "⑤",
      "reason": "보호정도의약함과보호의부재를구분."
    },
    {
      "code": 39,
      "scope": "②④",
      "reason": "장애속성·차별사유에따른보호효과차이를보존."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "정당성이라는규범주제가있지만원문밖규범평가보다주어진필요조건과정도관계를읽는다."
    }
  ],
  "competing_codes": [
    {
      "code": 11,
      "verdict": "기각",
      "refutation": "인권보호취지를갖추면모든법규가정당하다는역방향근거는없다."
    },
    {
      "code": 2,
      "verdict": "보조",
      "refutation": "정당성보장강도는관여하지만정답직접근거는조건의필요관계."
    },
    {
      "code": 54,
      "verdict": "기각",
      "refutation": "인권취지나정책목적하나가정당성을충분히결정한다고하지않는다."
    }
  ],
  "counterfactual": "①를인권취지를지니면정당하다고뒤집으면다른제약조건이남아본문만으로성립하지않는다.필요조건의방향이핵심이다.",
  "confidence": 0.98
}
```
