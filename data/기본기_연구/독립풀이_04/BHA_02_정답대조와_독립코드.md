

<!-- luna-raw:BHA-answer_check-20261002-r4-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G426",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "관측 대상의 흡수는 물체 식별 정보, 전달 매질 대기의 흡수는 통과 방해. 주체·역할 분리.",
  "limitations": [
    "봉인 공식 전사 답 대조, 원정답표 독립 시각 대조 미실시. 과거노출unknown 유지."
  ]
}
```


<!-- luna-raw:BHA-independent_code-20261002-r4-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G426",
  "sdss_seen": false,
  "general_task": "동일 작용어가 쓰인 대상과 매질의 역할 구분",
  "decisive_relation": "광물의 흡수 특성=판독 정보 / 대기의 흡수=전달 방해",
  "primary": {
    "code": 17,
    "scope": "정답③",
    "reason": "흡수의 주체가 대상 광물인지 대기인지 구분해야 정답을 판단한다."
  },
  "auxiliary": [
    {
      "code": 98,
      "scope": "정답③",
      "reason": "A의 흡수에서 A를 옮겨 붙인 귀속 오류.17과 국소 중첩."
    },
    {
      "code": 45,
      "scope": "센서 시스템",
      "reason": "대상 특성·전달 경로·관측 출력을 역할별로 구분한다."
    },
    {
      "code": 46,
      "scope": "정답③ 및④",
      "reason": "동일 흡수 작용이 어느 위치에서 관측에 영향을 미치는지 추적한다."
    }
  ],
  "surface": [
    {
      "code": 49,
      "reason": "반사율의 수치가 등장하나 정답은 단순 증감 비교가 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 50,
      "verdict": "대기 경로 국소 보조",
      "refutation": "경로 차단은 대기 흡수를 설명하지만 광물 흡수는 물체 구별의 정보이므로 모든 흡수를 같은 차단으로 처리하면 오류."
    },
    {
      "code": 55,
      "verdict": "주로는 기각",
      "refutation": "흡수와 관측 곤란의 상관에서 원인을 잘못 추정하는 것보다 서로 다른 주체에 같은 효과를 전이하는 오류가 직접적."
    },
    {
      "code": 4,
      "verdict": "보조 후보",
      "refutation": "흡수 일반으로 확대했다고 기술할 수 있지만 범위 확대를 만드는 실제 대상 교체를17로 남겨야 한다."
    }
  ],
  "counterfactual": "같은 물체에 고유 흡수 차이가 없다면 자원 식별 단서가 줄 수 있다. 대기 흡수를 줄이면 통과는 개선된다. 흡수량이라는 한 축에 일률적 좋고 나쁨을 붙일 수 없다.",
  "confidence": 0.97
}
```
