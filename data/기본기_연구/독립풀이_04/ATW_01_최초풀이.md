

<!-- luna-raw:ATW-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G313",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "prior_exposure": "이 세션의 사전 해설·정답·SDSS 노출 없음; 과거 노출 미확인",
    "official_answer_seen": false,
    "sdss_seen": false
  },
  "strict_blind_eligible": "과거 노출 미확인으로 확정 집계 보류",
  "needed_information_and_location": [
    "1문단 세포별 효소·산물·기능",
    "2문단 COX1 혈소판/COX2 면역/COX3 시상 하부",
    "3문단 위 점막 보호 약화"
  ],
  "minimal_logic_without_code": "세포→효소 종류→산물→기능의 경로를 고정하고 효소 억제가 산물과 기능을 감소시키는지 확인한다.",
  "intermediate_reasoning": [
    "① 혈소판 트롬복산은 응고 작용이므로 통증 결론이 틀림",
    "② 면역 세포는 프로스타글란딘 경로",
    "③ 중추 신경의 효소는 COX3",
    "④ 혈관 내피 프로스타글란딘은 응고 억제",
    "⑤ 위 점막 프로스타글란딘 보호 기능 약화가 일치"
  ],
  "most_attractive_wrong_answer_and_error": "③: 산물·발열 감소는 맞지만 효소2를3으로 바꾸어야 한다.",
  "source_scope": "시험 원문 내부 독해; 현재 의료 판단으로 확장하지 않음"
}
```
