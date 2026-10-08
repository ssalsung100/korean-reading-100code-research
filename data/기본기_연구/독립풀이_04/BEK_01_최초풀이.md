

<!-- luna-raw:BEK-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G402",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "ⓐ 원치 않는 개인정보의 외부 파악",
    "㉠ 다중 정보 충돌 해결",
    "㉡ 태그 불능화",
    "㉢ 리더 종류에 따른 선별 전달",
    "㉣ 분실·도난 방지용 인체 이식"
  ],
  "minimal_logic_without_codes": "원치 않는 정보 제공을 끊거나 허용 대상에만 제한하는 수단을 고른다. 다중 정보를 잘 읽게 하거나 태그를 잃지 않게 하는 수단은 그 자체로 정보 제공 차단이 아니다.",
  "intermediate_reasoning": [
    "㉠은 송신정보 얽힘 해소이므로 읽기의 편의를 높인다.",
    "㉡은 작동 자체를 없애므로 이후 원치 않는 판독을 막는다.",
    "㉢은 리더 종류에 따라 허용 내용만 제공한다.",
    "㉣은 공유키가 분실·도난으로 노출되는 문제에 대응하며 불특정 리더 판독 자체의 차단은 아니다."
  ],
  "attractive_wrong": {
    "choice": 5,
    "exact_error": "본문의 보다 안전하다는 표현을 모든 정보 노출 문제에 대한 해결로 확대하여 ㉣을 포함한다. 해당 안전은 분실·도난 경로에 관한 것이다."
  }
}
```
