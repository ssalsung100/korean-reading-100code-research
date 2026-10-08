

<!-- luna-raw:BHN-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G431",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "동일 기업규모 증가가 부채비율에 주는 효과를 두 이론이 반대 방향으로 예측한다.",
  "limitations": [
    "봉인 공식 전사 답 대조.원정답표 시각 재대조 미실시.unknown strict 제외 유지."
  ]
}
```


<!-- luna-raw:BHN-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G431",
  "sdss_seen": false,
  "general_task": "경쟁 이론의 명시된 예측과 전제 대조",
  "decisive_relation": "동일한 규모 증가에 대한 부채비율 증가/감소의 상반성",
  "primary": {
    "code": 74,
    "scope": "④",
    "reason": "같은 입력 조건에 대한 서로 다른 이론의 상반된 예측을 대조한다."
  },
  "auxiliary": [
    {
      "code": 49,
      "scope": "④",
      "reason": "기업규모-부채비율의 방향 부호를 각 이론에 유지."
    },
    {
      "code": 98,
      "scope": "전체",
      "reason": "예측 및 전제를 어느 이론에 귀속하는지 구분."
    },
    {
      "code": 8,
      "scope": "③",
      "reason": "내부자금→부채→주식의 자금조달 우선순위를 보존."
    },
    {
      "code": 73,
      "scope": "⑤",
      "reason": "불완전시장 이론이 비판한 표적은 완전시장 전제임을 확인."
    }
  ],
  "surface": [
    {
      "code": 84,
      "reason": "비율이 등장하지만 분자분모의 수리 연산은 요구하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 75,
      "verdict": "통합 연구군의 국소중첩",
      "refutation": "여기서는 명시 예측을 귀속해 읽는 행동이므로74/75 유일 주를 사실/규범 차이로 강제하지 않는다."
    },
    {
      "code": 63,
      "verdict": "주 기각",
      "refutation": "새 관측으로 어느 이론이 더 강한지 평가하지 않는다."
    },
    {
      "code": 43,
      "verdict": "주 기각",
      "refutation": "같은 변수를 비교하지만 실제 데이터에서 효과를 분리하는 통제 설계 문항은 아니다."
    }
  ],
  "counterfactual": "규모 대신 성장성을 넣어도 본문에서는 상반 예측이나 각 이론의 방향이 바뀐다.두 입력을 혼합하지 말고 변수명을 유지해야 한다.",
  "confidence": 0.98
}
```
