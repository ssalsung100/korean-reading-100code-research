

<!-- luna-raw:AUD-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G315",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "2문단 동일하면 질문 무의미→질문 유의미면 동일 아님",
    "3문단 춘원=이광수지만 동일인 질문은 유의미"
  ],
  "minimal_logic_without_codes": "비판 대상의 추론 규칙을 사실상 동일한 두 이름에 그대로 적용하여 다른 사람이라는 거짓 결론이 나오는 것을 드러낸다.",
  "intermediate_reasoning": [
    "질문 유의미라는 참 전제에 무어 규칙 적용",
    "그 결과 동일인 아님을 도출하지만 실제는 동일인",
    "④가 규칙의 부당한 결론을 정확히 재현",
    "③은 외연 동일이 항상 질문 유의미를 보장하는 것이 아니며 규칙의 모순 결과도 아님"
  ],
  "attractive_wrong_answer_and_error": "③: 질문 유의미성은 일부 사람의 지식 차이에서 나오며 외연 같음만으로 자동 산출되지 않는다.",
  "quota_status": "unavailable"
}
```
