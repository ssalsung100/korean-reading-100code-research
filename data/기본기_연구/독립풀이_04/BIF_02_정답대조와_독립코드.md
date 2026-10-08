

<!-- luna-raw:BIF-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G437",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "㉠은지급불능우려가실현되지만㉣위기는상승지속낙관이깨진결과다.중간가격상승과최종붕괴를나눈다.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 유지."
  ]
}
```


<!-- luna-raw:BIF-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G437",
  "sdss_seen": false,
  "general_task": "금융위기 설명 시각의 예측 내용과 결과 대조",
  "decisive_relation": "예상 자체가 실현되는 경로와 예상이 깨져 위기가 되는 경로의 구분",
  "primary": {
    "code": 75,
    "scope": "⑤",
    "reason": "각 시각에서 예상하는 내용과 위기의 의미를 정확히 귀속한다.74/75 통합군의 명시 설명 대조형."
  },
  "auxiliary": [
    {
      "code": 98,
      "scope": "⑤",
      "reason": "예상이라는 명사만같고그내용은지급불능/지속상승으로다르다."
    },
    {
      "code": 46,
      "scope": "㉠㉣",
      "reason": "예상→행동→중간가격→최종위기의경로를분리한다."
    },
    {
      "code": 3,
      "scope": "⑤",
      "reason": "㉣중간상승기와최종붕괴기의결과를혼동하지않는다."
    }
  ],
  "surface": [
    {
      "code": 77,
      "scope": "④",
      "reason": "귀납적접근은㉣의근거성격설명이지이문항에서새표본을일반화하는행동은아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 74,
      "verdict": "통합연구군유지",
      "refutation": "경쟁설명이라는점은맞으며75와유일주를사실/규범구분으로강제하지않는다."
    },
    {
      "code": 63,
      "verdict": "주기각",
      "refutation": "어느이론이더강하게입증되는지새증거로평가하지않는다."
    },
    {
      "code": 18,
      "verdict": "국소보조가능",
      "refutation": "상승지속과붕괴는반대지만핵심은각이론의예상내용과시간단계를복원하는것이다."
    }
  ],
  "counterfactual": "㉣에서가격상승이계속되어거품붕괴가없다면예상이실현되는단계는말할수있으나본문이설명한금융위기결과는아직발생하지않는다.",
  "confidence": 0.97
}
```
