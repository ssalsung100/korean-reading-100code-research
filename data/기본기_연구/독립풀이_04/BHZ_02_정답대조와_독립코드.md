

<!-- luna-raw:BHZ-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G435",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2013/2013_answer_2013_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "지역구 의원·상임위 사이의 거래를 정당 사이 거래로 바꾸지 않는다.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 및 최초 유보 유지."
  ]
}
```


<!-- luna-raw:BHZ-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G435",
  "sdss_seen": false,
  "general_task": "세 이론의 대표 주체·조직 기능·목적 대조",
  "decisive_relation": "투표 거래의 당사자 단위를 상임위 소속 의원에서 정당으로 바꾼 오류",
  "primary": {
    "code": 98,
    "scope": "①",
    "reason": "거래라는 같은 행위라도 누구와 누구 사이인지를 보존해야 한다."
  },
  "auxiliary": [
    {
      "code": 75,
      "scope": "전체",
      "reason": "이익분배·정보확산·정당이익 이론에 견해를 정확히 귀속."
    },
    {
      "code": 17,
      "scope": "①",
      "reason": "의원·상임위·정당은 정치적 소속이 중첩되어도 동일 분석 단위가 아니다."
    },
    {
      "code": 39,
      "scope": "②~⑤",
      "reason": "기능·배정·대표성·목표의 같은 축에서 두 이론을 비교."
    }
  ],
  "surface": [
    {
      "code": 74,
      "reason": "경쟁이론이지만 새 조건에 대한 상반 예측을 계산하지 않고 명시 견해를 대조한다.74/75의 전역 배타경계는 아님."
    }
  ],
  "competing_codes": [
    {
      "code": 40,
      "verdict": "보조 후보",
      "refutation": "의원이 정당의 구성원이라는 포함만으로 해당 의원의 지역구 거래를 정당 간 행위로 귀속시킬 수 없다."
    },
    {
      "code": 41,
      "verdict": "국소유사",
      "refutation": "부분행동을 전체에 옮긴다는 기술은 가능하지만 성질의 합성 일반화보다 거래 주체의 잘못된 교환을 복원하는98이 직접적이다."
    },
    {
      "code": 93,
      "verdict": "주 기각",
      "refutation": "지지 요청이 소통으로 이루어지더라도 메시지 전달·해석이 아니라 거래 단위가 정답을 결정한다."
    }
  ],
  "counterfactual": "①정당 간을 서로 다른 상임위의 의원 간으로 바꾸면 이익분배 이론에 부합한다.정당소속이라는 배경사실만으로 원문에 없는정당대표 거래를 추가하지 않는다.",
  "confidence": 0.98
}
```
