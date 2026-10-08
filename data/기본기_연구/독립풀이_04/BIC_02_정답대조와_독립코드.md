

<!-- luna-raw:BIC-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G436",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2013/2013_answer_2013_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "세포 유형을 결정하는 물질은 제시되지만 해당 유형의 세포 수를 결정하는 물질 종류는 미제시.정보 부재를 실제 대상 부재로 확장하지 않는다.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 유지."
  ]
}
```


<!-- luna-raw:BIC-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G436",
  "sdss_seen": false,
  "general_task": "질문의 정보 요구와 본문 제공 범위 대조",
  "decisive_relation": "분화 유형의 결정과 특정 유형 세포 수의 결정을 구분",
  "primary": {
    "code": 17,
    "scope": "④",
    "reason": "설명된 변수인 세포 유형과 질문된 변수인 세포 수는 다른 대상 범주다."
  },
  "auxiliary": [
    {
      "code": 98,
      "scope": "④",
      "reason": "결정하는 물질이라는 표현에서 무엇을 결정하는지가 바뀐다."
    },
    {
      "code": 64,
      "scope": "문항전체",
      "reason": "본문이 답하는 과정·분열 방식·시기와 답하지 않는 수결정 요인을 구분."
    },
    {
      "code": 3,
      "scope": "③",
      "reason": "내부세포의 최초 등장 시점16단계를 확인."
    }
  ],
  "surface": [
    {
      "code": 95,
      "reason": "알수없음을 실제 수결정물질 부재로 바꿀 수 없다.존재필요조건을 추론하는 문항이 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 1,
      "verdict": "국소표상보조",
      "refutation": "질적유형과양적수량 구분을 기술할수있으나 정보부재를판정하는데 어떤변수가설명되었는지 확인해야한다."
    },
    {
      "code": 46,
      "verdict": "배경",
      "refutation": "분화 원인은 설명되지만 수결정 원인이 설명되지는 않았다.인과가 등장한다는 이유만으로 질문의 대상차이를 지울 수 없다."
    },
    {
      "code": 31,
      "verdict": "주 기각",
      "refutation": "원소수/집합수의 수리구별이 아니라 세포유형과 해당세포수에 대한 정보범위 구별이다."
    }
  ],
  "counterfactual": "④의 세포의 수를 세포의 유형으로 바꾸면 OCT4/CDX2·양극성결정물질 설명에서 관련 근거를 얻을 수 있다.반대로8/16/32 총세포수만으로 내부세포수를 결정하는 물질을 알 수는 없다.",
  "confidence": 0.97
}
```
