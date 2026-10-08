

<!-- luna-raw:BGN-answer_check-20261002-r3-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G421",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "answer_verification": "봉인 official_answer 전사필드 대조. 원정답표 독립 시각 대조 미실시.",
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "기업들 사이의 협력 네트워크를 개별 기업 내부의 소통 네트워크로 바꾼⑤가 틀리다.",
  "unresolved": null,
  "sdss_disclosed": false
}
```


<!-- luna-raw:BGN-independent_code-20261002-r3-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G421",
  "general_task": "지역발전 사례의 내용확인",
  "decisive_relation": "기업간 관계를 기업내 관계로 바꾼 연결범위 오류",
  "primary": [
    42
  ],
  "auxiliary": [
    17,
    40
  ],
  "surface": [
    93,
    19
  ],
  "code_rationale": {
    "42": "한기업을기준으로밖의기업간연결/안의구성원연결구별",
    "17": "네트워크구성단위가기업인지내부구성원인지보존",
    "40": "하나의기업과기업공동체의단위차이"
  },
  "competing_codes": [
    {
      "code": 19,
      "rebuttal": "영세성보완은배경이지만보완수단의연결범위를바꾼것이오류."
    },
    {
      "code": 93,
      "rebuttal": "소통이라는단어만으로전달기제가중심이라고할수없다."
    },
    {
      "code": 41,
      "rebuttal": "부분성질을전체로상속한것이아니라연결상대와경계를치환."
    }
  ],
  "confidence": 0.99,
  "sdss_disclosed": false
}
```
