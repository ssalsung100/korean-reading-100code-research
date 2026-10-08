

<!-- luna-raw:BHB-answer_check-20261002-r4-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G426",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "반사율 차이와 대기 통과조건을 함께 충족해야 영상 식별 가능.1.4의 신호차이는 흡수에 의해 무력화.",
  "limitations": [
    "봉인 공식 전사 답 대조, 원정답표 독립 시각 대조 미실시. 과거노출unknown 유지."
  ]
}
```


<!-- luna-raw:BHB-independent_code-20261002-r4-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G426",
  "sdss_seen": false,
  "general_task": "반사율·흡수율 그래프 결합 판독",
  "decisive_relation": "대기의 강한 흡수가 전달 경로를 막으면 물체 자체 반사율의 차이가 센서의 구별 신호가 되기 어렵다.",
  "primary": {
    "code": 50,
    "scope": "정답⑤ 및오답①③",
    "reason": "1.4·1.9에서 대기 흡수가 경로를 차단하고2.2에서는 차단이 작다는 위치별 판정이 필요하다."
  },
  "auxiliary": [
    {
      "code": 10,
      "scope": "정답⑤",
      "reason": "대기 통과가 물체 반사 특성을 관측하기 위한 필요조건으로 작동한다."
    },
    {
      "code": 45,
      "scope": "그래프 전체",
      "reason": "반사와 전달을 결합하여 센서에서 가능한 구별을 판단한다."
    },
    {
      "code": 86,
      "scope": "정답⑤ 및④",
      "reason": "대기가 통과하는 대역에서 A/B반사율 격차를 비교한다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "정밀 산술보다 곡선의 큰 차이와 거의100%흡수 여부가 중요."
    }
  ],
  "competing_codes": [
    {
      "code": 49,
      "verdict": "방향 비교 보조, 주로는 기각",
      "refutation": "A반사율 증가→더 밝음이라는 단일 방향만 적용하면①에 속는다. 중간 전달을 함께 고려해야 한다."
    },
    {
      "code": 43,
      "verdict": "주로는 기각",
      "refutation": "다른 원인을 통제하여 인과효과를 식별하는 실험이 아니라 주어진 세 그래프의 결합 적용이다."
    },
    {
      "code": 54,
      "verdict": "①충분성 과장 설명 후보",
      "refutation": "높은 반사율을 밝은 영상의 충분한 보장으로 본 오류는 맞지만 그 보장을 깨는 구체 관계는 대기 경로의 차단이다."
    }
  ],
  "countermodel": "1.4에서A반사율이 더 커져도 대기흡수가 거의 전부라면 전달 신호는 제한된다. 반대로 통과가 좋아도 A/B반사율이 같으면 구별에 충분하지 않다.",
  "confidence": 0.98
}
```
