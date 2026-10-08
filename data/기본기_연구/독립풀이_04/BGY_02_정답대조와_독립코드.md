

<!-- luna-raw:BGY-answer_check-20261002-r4-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G425",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "사태 설명 서사와 규범적 처벌을 통한 혼란 극복·질서 정당성 공유가 A의 문화적 기능.",
  "limitations": [
    "봉인 공식 전사 답과 대조. 원정답표 독립 시각 대조 미실시. 과거노출unknown 유지."
  ]
}
```


<!-- luna-raw:BGY-independent_code-20261002-r4-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G425",
  "sdss_seen": false,
  "general_task": "지정 문단의 제도적·문화적 기능 요약",
  "decisive_relation": "재판의 설명 서사와 처벌→혼란 극복→질서 안전·정당성에 대한 공유된 믿음",
  "primary": {
    "code": 46,
    "scope": "정답⑤",
    "reason": "절차가 사람들에게 낳는 인식·심리 효과의 경로를 복원한다."
  },
  "auxiliary": [
    {
      "code": 56,
      "scope": "A 전반",
      "reason": "사태에 대한 서사를 구성하여 설명하는 기능을 포착한다."
    },
    {
      "code": 80,
      "scope": "정답⑤",
      "reason": "질서가 실제로 안전하다는 외부 사실이 아니라 사람들이 안전·정당성을 확인하는 인식 결과를 기록한다."
    },
    {
      "code": 44,
      "scope": "문항 기능 질문",
      "reason": "재판이 문화적 질서 회복에 기여하는 수단으로 기능한다. 효과 서술이 제도 설계자의 명시적 의도를 모두 입증하지는 않는다."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "인간 규범은 설명의 기준이지만 정답은 그 규범의 옳고 그름 평가가 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 78,
      "verdict": "주로는 기각",
      "refutation": "기능·효과의 서술에서 엘리트 개개인의 속마음이나 과시 욕구를 확정할 수 없다."
    },
    {
      "code": 4,
      "verdict": "④국소 보조",
      "refutation": "예외 없이 처벌된다는 과장이④를 배제하지만⑤의 긍정적 경로 전체는 설명하지 못한다."
    },
    {
      "code": 60,
      "verdict": "A국소 보조 가능",
      "refutation": "사태 설명 서사의 기능을 논증의 타당성 평가로 바꾸면 문화적 효과와 논리적 정당성을 혼동한다."
    }
  ],
  "falsification_attempt": "어떤 재판이 사람들에게 안도감을 주어도 동물 책임이나 신적 질서의 객관적 타당성이 입증되는 것은 아니다. 효과·믿음·실제 정당성을 분리한다.",
  "confidence": 0.96
}
```
