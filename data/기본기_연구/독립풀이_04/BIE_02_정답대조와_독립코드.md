

<!-- luna-raw:BIE-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G436",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2013/2013_answer_2013_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "㉠㉡에는 조작후 접촉·노출 조건을,㉢에는 결정물질 기능억제를 적용하면 영양외배엽·영양외배엽·속세포덩어리.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 유지."
  ]
}
```


<!-- luna-raw:BIE-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G436",
  "sdss_seen": false,
  "general_task": "가설별 개입조건에서 기대되는 분화결과 산출",
  "decisive_relation": "환경접촉/노출 또는 결정물질기능이라는 가설별 원인변수를 조작후 값으로 적용",
  "primary": {
    "code": 74,
    "scope": "㉠㉡㉢",
    "reason": "행마다 지정된 가설에 따라 어떤 결과가 그 가설의 예측에 맞는지 산출한다."
  },
  "auxiliary": [
    {
      "code": 45,
      "reason": "조작후 조건을 입력으로 영양외배엽/속세포덩어리 출력을 대응."
    },
    {
      "code": 46,
      "reason": "가설이 원인으로 지목한 환경 또는 물질기능 변화의 효과."
    },
    {
      "code": 3,
      "scope": "㉠㉡",
      "reason": "조작전 내부위치보다 조작후 노출조건을 적용."
    },
    {
      "code": 50,
      "scope": "㉢",
      "reason": "결정물질의기능을억제하여그경로의작용을차단."
    }
  ],
  "surface": [
    {
      "code": 63,
      "reason": "가설을지지하는결과를묻지만실제관측으로지지강도를평가하기전예측산출단계다."
    }
  ],
  "competing_codes": [
    {
      "code": 75,
      "verdict": "통합연구군 유지",
      "refutation": "입장귀속과예측적용이결합하므로74/75를규범/사실차이로억지분리하지않는다."
    },
    {
      "code": 43,
      "verdict": "보조이나주기각",
      "refutation": "개입이있지만대조군·통제설계의충분성을선택하는문항은아니다.주어진조작에서예측되는유형을묻는다."
    },
    {
      "code": 36,
      "verdict": "주 기각",
      "refutation": "실제반례를찾아가설을거짓으로판정하는과제가아니라각가설에부합하는결과를채운다."
    }
  ],
  "counterfactual": "㉡에 원래내부라는출신만적용하면속세포덩어리로예측해환경변화원인가설을검증하지못한다.㉢에단독배양노출만적용하면환경가설과양극성가설을혼합한다.",
  "unresolved": "가설부합결과가다른가설을배타적으로기각하거나실제생물학적참을확정함을뜻하지않는다.",
  "confidence": 0.98
}
```
