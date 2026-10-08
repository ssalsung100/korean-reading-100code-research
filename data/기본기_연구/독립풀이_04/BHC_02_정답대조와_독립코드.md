

<!-- luna-raw:BHC-answer_check-20261002-r4-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G426",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "다른 조건 동일 아래 온도-파장 반비례, 밀도-산란 방향, 수증기-흡수-대기창 경로 적용.",
  "limitations": [
    "봉인 공식 전사 답 대조, 원정답표 독립 시각 대조 미실시. 과거노출unknown 유지."
  ]
}
```


<!-- luna-raw:BHC-independent_code-20261002-r4-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G426",
  "sdss_seen": false,
  "general_task": "변수 변경에 따른 관측 조건 변화 적용",
  "decisive_relation": "온도감소→파장증가, 밀도감소→산란감소, 수증기감소→흡수감소→통과창확대",
  "primary": {
    "code": 49,
    "scope": "ㄱㄴㄷ 전체",
    "reason": "주어진 관계의 방향을 각 변경 조건에 적용하여 역전된 계획을 배제한다. 사이트49가 촉진/억제 방향을 포괄한다는 기존 기준을 따른다."
  },
  "auxiliary": [
    {
      "code": 43,
      "scope": "보기 전제",
      "reason": "명시된 변화 이외의 조건이 동일하다는 전제가 원인 경로별 비교를 가능하게 한다."
    },
    {
      "code": 91,
      "scope": "ㄱ",
      "reason": "온도와 최대파장의 반비례 방향."
    },
    {
      "code": 52,
      "scope": "ㄷ",
      "reason": "흡수를 일으키는 수증기가 줄어 통과의 방해가 완화되는 이중 방향."
    },
    {
      "code": 46,
      "scope": "ㄴㄷ",
      "reason": "입자밀도·수증기량과 산란·흡수의 발생 경로."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "구체 파장 계산을 하지 않고 증감 방향만으로 모든 항목 판정 가능."
    }
  ],
  "competing_codes": [
    {
      "code": 50,
      "verdict": "ㄷ 국소 보조",
      "refutation": "막힌 경로의 통과를 다루지만 이 문항은 특정 파장 차단을 찾기보다 차단 원인이 줄 때의 변화를 적용한다."
    },
    {
      "code": 54,
      "verdict": "강한 보장으로는 기각",
      "refutation": "수증기 감소만으로 모든 파장에서 완전 통과한다고 결론 내리지 않는다. 다른 흡수체의 효과가 남는다."
    },
    {
      "code": 45,
      "verdict": "포괄 보조 후보",
      "refutation": "입력 변화에 출력이 변한다는 기술은 가능하나 각 관계의 부호와 경로를 별도로 남겨야 한다."
    }
  ],
  "falsification_attempt": "ㄷ의 대기창 확대는 수증기 흡수 완화 범위이다. 산소 등 다른 물질의 흡수가 큰 대역까지 모두 사용 가능해진다는 전칭은 나오지 않는다.",
  "confidence": 0.97
}
```
