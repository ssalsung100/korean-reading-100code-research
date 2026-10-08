

<!-- luna-raw:AEY-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "2문단: 톨루엔 분자 하나에 수소 분자3개가 결합해MCH 한 분자 생성. 수소 분자마다 탄소-수소 결합2개 형성.",
    "3문단: 암모니아 한 분자에 수소 원자3개."
  ],
  "minimal_logic_without_codes": "MCH 한 분자에 새로 결합한 수소만 세 분자×두 원자=여섯 원자이므로 암모니아의 세 원자보다 많다. 톨루엔의 원래 수소 수를 몰라도④ 확정 가능.",
  "intermediate_reasoning": [
    "① MCH는 증발 기체에 따른 누출 위험 거의 없음.",
    "② 암모니아 높은 독성 있음.",
    "③ 기존 인프라로 대규모 투자 없이 운송 가능.",
    "⑤ 둘 다 기존 인프라 활용 가능."
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "MCH는 석유 인프라, 암모니아는 비료 산업 인프라라는 종류 차이를 기존 인프라 활용 여부 차이로 바꾼다.",
  "scope_limit": "MCH의 정확한 전체 분자식을 외부 지식으로 보충하지 않는다. 원문으로 보장되는 최소 여섯 수소 원자만으로 비교 충분.",
  "quota_status": "unavailable"
}
```
