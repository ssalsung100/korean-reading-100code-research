

<!-- luna-raw:BCP-answer_check-20261002-01 -->
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
  "logic_without_codes_fixed": "항원을 먼저 만난 엄마가 항체를 만들고 이 항체가 태아의 표적 혈구를 파괴한다. 반복 노출의 원인을 태아 보체 증가로 돌릴 수 없다. 이전 혈액 노출이 있으면 첫 임신도 최초 항원 노출이 아니다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": "ㄱ은 표적 파괴의 기능적 확대이고 실제 생의학 분류 동일성의 독립 증명은 아님"
}
```


<!-- luna-raw:BCP-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G386",
  "primary_codes": [
    46
  ],
  "auxiliary_codes": [
    69,
    3,
    5
  ],
  "surface_codes": [
    17
  ],
  "decisive_operation": "엄마 항원 노출→항체 생성→태반 통과→태아 혈구 파괴의 경로를 보존하고 이전 노출이 있으면 첫 임신도 재노출이 될 수 있음을 복원한다.",
  "competitor_refutations": [
    {
      "code": 69,
      "reason": "ㄱ의 균 파괴/혈구 파괴 기능 대응은 독립 필수 하위행동이다. 그러나ㄴ 보체 증가 배제와ㄹ 이전 노출의 영향은 대응만으로 끝나지 않아 문항 전체 주46을 둔다."
    },
    {
      "code": 3,
      "reason": "임신 순번과 실제 노출 순서는 다르다. 선후 확인은 항체 생성 경로의 선행 조건이며 단순 시간 순서 암기가 아니다."
    },
    {
      "code": 5,
      "reason": "보체가 면역 반응으로 늘지 않는다는 불변성을ㄴ에 적용한다. 이 부분은 주46과 구별되는 보조 판단이다."
    }
  ],
  "boundary_note": "ㄱ69와ㄴ5와ㄹ46/3은 서로 다른 하위선지에 분포. 주46이 모든 선지의 단일 연산이라고 주장하지 않는다.",
  "confidence": 0.89,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
