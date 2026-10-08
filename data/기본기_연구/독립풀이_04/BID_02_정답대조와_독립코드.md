

<!-- luna-raw:BID-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G436",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2013/2013_answer_2013_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "바깥쪽 양극성 결정물질은 표층에 남고 내부에 없으며 이 차이가 CDX2 분포에 관련된다.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 유지."
  ]
}
```


<!-- luna-raw:BID-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G436",
  "sdss_seen": false,
  "general_task": "표층·내부 세포에서 물질과 억제작용의 분포 대조",
  "decisive_relation": "바깥쪽 결정물질의 표층 존재와 내부 부재 차이 보존",
  "primary": {
    "code": 42,
    "scope": "⑤및①~③",
    "reason": "배아 표층/내부에 따라 물질 분포 및 접촉 조건을 다르게 적용해야 한다."
  },
  "auxiliary": [
    {
      "code": 98,
      "reason": "CDX2가OCT4를 억제하는 위치와 그 반대 억제의 위치를 바꾸지 않는다."
    },
    {
      "code": 49,
      "scope": "①③④",
      "reason": "접촉→히포활성→CDX2감소 및 억제 방향을 전파."
    },
    {
      "code": 84,
      "scope": "④",
      "reason": "OCT4/CDX2에서 감소하는 CDX2는 분모임을 유지.양의 분모인 구간의 정성 판단."
    },
    {
      "code": 1,
      "scope": "⑤",
      "reason": "결정물질 존재/부재의 차이를 양의 차이로 읽음."
    }
  ],
  "surface": [
    {
      "code": 85,
      "reason": "두 물질이 서로억제하더라도 합계가항상일정하다고 명시되지는 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "verdict": "보조",
      "refutation": "기전 인과는 배경이나⑤직접확인은 위치별물질분포차이로 충분하다."
    },
    {
      "code": 52,
      "verdict": "국소 후보",
      "refutation": "히포가CDX2발현물질을억제하는경로를통해OCT4억제해제까지추론할수있으나그이중억제는정답⑤의필수도출은아니다."
    },
    {
      "code": 43,
      "verdict": "주 기각",
      "refutation": "표층/내부 관찰조건을대조하지만 실험통제의정당성을평가하는문항은아니다."
    }
  ],
  "counterfactual": "OCT4와CDX2의 합이 변해도 위치별감소·잔류 설명은성립한다.따라서④비율판정에고정총량85를추가할필요가없다.",
  "unresolved": "CDX2가완전히0인종점에서는비율수치가정의되지않으며유한한비율값을억지로주지않는다.",
  "confidence": 0.97
}
```
