

<!-- luna-raw:BHU-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G433",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "타인과의 교수적 상호작용 및 학습자의 자기조절·의미 이해를 함께 보존한다.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 유지."
  ]
}
```


<!-- luna-raw:BHU-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G433",
  "sdss_seen": false,
  "general_task": "학습 원리의 두 핵심 요소를 보존하는 요약 선택",
  "decisive_relation": "사회적 소통을 매개로 하되 인식 주체가 의미를 능동적으로 구성",
  "primary": {
    "code": 80,
    "scope": "④ 대③",
    "reason": "외부 정보의 수동 복사가 아니라 주체의 이해·자기조절을 통한 내면화라는 인식 과정을 보존한다."
  },
  "auxiliary": [
    {
      "code": 93,
      "scope": "④ 대⑤",
      "reason": "개인의 숙고만이 아니라 교수자와 학습자 사이 상호작용이라는 사회적 매개가 필요."
    },
    {
      "code": 23,
      "reason": "소통과 능동적 구성이라는 두 요소를 함께 충족해야 함."
    },
    {
      "code": 45,
      "reason": "심리 간 상호작용→자기조절→심리 내 습득의 변환을 요약."
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "학습 단계가 등장하지만 단계적 설명이라는 말만으로③주입을 정당화하지 못한다."
    }
  ],
  "competing_codes": [
    {
      "code": 78,
      "verdict": "보조 후보",
      "refutation": "능동성이 있으나 학습자의 욕구·목적이 행위를 설명하는 동기 추론보다 인식과정의 주체 역할이 핵심이다."
    },
    {
      "code": 19,
      "verdict": "배경",
      "refutation": "타인의 도움이 부족을 보완하지만④와③차이는 도움의 존재보다 학습자의 능동적 구성이다."
    },
    {
      "code": 97,
      "verdict": "주 기각",
      "refutation": "발화자의 숨은 의도를 추정하지 않고 명시된 교수적 소통 원리를 요약한다."
    }
  ],
  "counterfactual": "능동적 형성만 남기면 사회적 상호작용을 제거한⑤식 설명과 구분되지 않고,소통만 남기면 수동적 주입③을 배제할 수 없다.두 요소가 서로 다른 오답 배제에 기여한다.",
  "unresolved": "80/93 중 문항 전체 유일 주는 경로에 따라 달라질 수 있어 고정하지 않는다.",
  "confidence": 0.97
}
```
