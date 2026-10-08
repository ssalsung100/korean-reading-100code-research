

<!-- luna-raw:BDP-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G395",
  "selected_answer": 5,
  "official_answer": "⑤",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "스키 방법이라는 지식·능력이 자기 안에 없어서 행위를 못 하므로 내적이면서 소극적인 속박이다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": null
}
```


<!-- luna-raw:BDP-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G395",
  "primary_codes": [
    25
  ],
  "auxiliary_codes": [
    1,
    42,
    37,
    10
  ],
  "surface_codes": [
    2
  ],
  "decisive_operation": "자기 심신 안팎과 장애요인의 존재/조건 부재라는 두 축을 독립 적용하여 내적·소극적의 교차 칸을 찾는다.",
  "competitor_refutations": [
    {
      "code": 1,
      "reason": "적극/소극은 장애 존재/필요조건 부재의 유무축.최종분류25를만드는실제하위검사다."
    },
    {
      "code": 42,
      "reason": "내외축은심신이라는명시경계를기준으로삼아야한다.내적인것이모두소극적인것은아님."
    },
    {
      "code": 37,
      "reason": "사례찾기/요건10과 같은국소행동이지만 여기서는두축의교차분류가명시돼25를작업대표로선택."
    }
  ],
  "boundary_note": "공포증 있음과 용기 부족은임의동의어치환하면존재/부재축이흐려진다.문항이제시한직접장애를고정한다.",
  "confidence": 0.91,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
