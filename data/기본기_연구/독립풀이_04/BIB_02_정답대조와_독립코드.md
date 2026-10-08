

<!-- luna-raw:BIB-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G435",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2013/2013_answer_2013_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "사장시현행2유지,수정불가시1부결로2유지,수정허용시과반125의정책3이대안으로상정되면3통과.2,2,2,3.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 및 최초 유보 유지."
  ]
}
```


<!-- luna-raw:BIB-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G435",
  "sdss_seen": false,
  "general_task": "절차의 분기별 최종 정책 산출",
  "decisive_relation": "차단 시 현상유지와 표결 시 과반 선호를 단계별로 결합",
  "primary": {
    "code": 45,
    "scope": "㉠~㉣",
    "reason": "회부·규칙부여·수정가능성·표결을 분기 입력으로 최종 정책을 계산한다."
  },
  "auxiliary": [
    {
      "code": 50,
      "scope": "㉠㉡",
      "reason": "앞단계에서 막히면 후속 표결로 진행하지 못함."
    },
    {
      "code": 5,
      "scope": "㉠㉡㉢",
      "reason": "새 의안이 통과하지 않으면 현행정책2가 유지됨."
    },
    {
      "code": 86,
      "scope": "㉢㉣",
      "reason": "13/25,125/245 및195/245의 과반을 판단."
    },
    {
      "code": 12,
      "scope": "수정규칙",
      "reason": "수정불가이면 원안 가부만,수정허용이면 대안 표결 가능."
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "표결의 역순 규칙이 있으나125명 과반이정책3을가장선호하므로 이번조건에서는 대안3의 상정후순서에따른결과변동이핵심은아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 92,
      "verdict": "보조",
      "refutation": "표수의 덧셈은 필요하지만 계산만으로 차단후현행유지나수정불가의의미를알수없다."
    },
    {
      "code": 85,
      "verdict": "보조가능",
      "refutation": "투표인원은 고정이나득표비율의경쟁적변동을일반식으로추론하는것보다선호에따른표결을직접대응한다."
    },
    {
      "code": 78,
      "verdict": "배경",
      "refutation": "정책선호가 이미주어져있어동기를추측하지않는다."
    }
  ],
  "counterfactual": "본회의 정책3선호가 과반 미만이면 수정안 간 순서와 나머지의 근접 선호가 최종 결과에 중요해질 수 있다.이번 과반 구조를 모든 입법의 순서무관성으로 일반화하지 않는다.",
  "source_restoration": "BIB 발문과[A]범위는 group답공개전 공식2013문제에서 blind-only supplement로 복원.최초source hold보존.",
  "unresolved": "정책3수정안이 실제로상정된다는표준경로에서㉣=3.수정허용 자체가 수정안 제출을 필연보장한다는해석은유보.",
  "confidence": 0.98
}
```
