

<!-- luna-raw:BGQ-answer_check-20261002-r3-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G422",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "answer_verification": "봉인 official_answer 전사필드 대조. 원정답표 독립 시각 대조 미실시.",
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "뉴턴의 더 넓은 설명 안에서 작은 구간의 갈릴레오 법칙이 근사적으로 유효하므로 포섭 관계①이다.",
  "unresolved": "보기수식과변수기호의전사누락있으나중력가속도상수근사와포섭관계는문장으로판정가능.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BGQ-independent_code-20261002-r3-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G422",
  "general_task": "이론간 관계의 사례 대응",
  "decisive_relation": "제한조건 아래 유효한 옛이론의 포섭을 접경적 상보와 구별",
  "primary": [
    69
  ],
  "auxiliary": [
    12,
    39
  ],
  "surface": [
    19,
    40
  ],
  "code_rationale": {
    "69": "상대론/고전의관계구조를뉴턴/갈릴레오에대응",
    "12": "작은낙하구간이라는유효조건",
    "39": "포함관계와별도영역접경관계를비교"
  },
  "competing_codes": [
    {
      "code": 37,
      "rebuttal": "관계형사례찾기로도표현가능.같은행동의상위과제라배타경계안만듦."
    },
    {
      "code": 19,
      "rebuttal": "공백을다른영역이보완하는②보다한이론이다른이론의유효영역을포섭하는①이맞음."
    },
    {
      "code": 40,
      "rebuttal": "옛법칙의영역이부분이기는하나핵심은두관계형의구조대응이지구성요소열거가아님."
    }
  ],
  "confidence": 0.98,
  "sdss_disclosed": false,
  "unresolved": "수식전사누락한계는문장근거의범위로유지."
}
```
