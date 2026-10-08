

<!-- luna-raw:BCQ-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G386",
  "selected_answer": 5,
  "official_answer": "⑤",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "받는 개체에 외부의 이미 만들어진 항체가 들어오는 경우를 찾으면㉡㉣이다. 균을 주입해 자기 항체 생성을 유도하는㉠㉢과 구별한다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": null
}
```


<!-- luna-raw:BCQ-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G386",
  "primary_codes": [
    37
  ],
  "auxiliary_codes": [
    10,
    16,
    25
  ],
  "surface_codes": [
    42,
    78
  ],
  "decisive_operation": "정의에 있는 다른 개체의 이미 생성된 항체 주입이라는 요건을 각 사례에서 대조한다. 균 주입과 항체 주입을 가른다.",
  "competitor_refutations": [
    {
      "code": 10,
      "reason": "사례 부합 요건 확인이라는 점에서37과 같은 국소 연산이며 별개 단계로 중복 계수하지 않는다. 생리적 면역에 필요한 모든 조건을 묻는 문제는 아니다."
    },
    {
      "code": 25,
      "reason": "능동/수동 분류는 동일 판정의 출력이며 독립적인 추가 추론 아님."
    },
    {
      "code": 78,
      "reason": "능동/수동이라는 어휘는 개인의 의지·행위 동기를 뜻하지 않는다. 주사를 자발적으로 맞았는지는 기준을 바꾸지 않는다."
    }
  ],
  "boundary_note": "37/10 국소 중첩,16 정의 독해,25 결과 분류. 외부 주입이라는42만으로는 모든 사례가 걸려 항체 생성 주체를 구별 못함.",
  "confidence": 0.89,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
