

<!-- luna-raw:AHA-blind-20260921-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G203",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "대화 및 기억에서 해당 사례 노출은 확인되지 않으나 사전학습 노출 여부는 검증 불가"
  },
  "needed_information_and_location": [
    "4문단 마지막: 읽은 뒤 배경지식과 이해 내용 연결",
    "1문단 목적·2문단 재검토·4문단 관점 바꾸기"
  ],
  "minimal_logic_without_codes": "정의된 활동의 시점과 행동을 선지와 맞춘다. 읽은 뒤 연결하여 이해하는 활동을 읽기 전 자료 선택으로 바꾼 ①이 불일치.",
  "intermediate_inferences": [
    "② 지식 습득 목적 일치",
    "③ 파악·기억 필수 일치",
    "④ 마지막 재검토와 일치",
    "⑤ 저자 입장 읽기→분석적 읽기 일치"
  ],
  "most_attractive_wrong_answer": {
    "choice": 5,
    "attraction": "관점 바꾸기라는 이름만 보면 관점의 다양화로 오해할 수 있음",
    "error": "원문은 저자의 입장에서 분석적으로 읽는 효과를 명시하여 옳은 선지다."
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/AHA.json",
  "quota_status": "unavailable"
}
```
