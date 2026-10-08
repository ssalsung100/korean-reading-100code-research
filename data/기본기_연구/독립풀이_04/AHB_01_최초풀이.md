

<!-- luna-raw:AHB-blind-20260921-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G203",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "대화 및 기억에서 해당 사례 노출은 확인되지 않으나 사전학습 노출 여부는 검증 불가"
  },
  "needed_information_and_location": [
    "4문단 ㉠ 뒤 관점 바꾸기·숙고하기 정의",
    "2문단 기존 다섯 활동"
  ],
  "minimal_logic_without_codes": "추가된 활동의 예인지 확인하려면 기존 다섯 활동과 새 활동을 구별한 다음 저자 입장에서 구성 순서를 생각하는 행동과 대응시킨다.",
  "intermediate_inferences": [
    "① 암송·② 답 찾으며 읽기·③ 훑어보기는 기존 활동이므로 추가 예 아님",
    "④ 저자 언급은 있으나 수동 수용은 관점 바꾸기의 명시적 부정 대상",
    "⑤ 저자 입장에서 첫머리 내용을 고민하는 것은 구성 순서 검토"
  ],
  "most_attractive_wrong_answer": {
    "choice": 4,
    "attraction": "저자의 의도라는 표면 표현이 관점 바꾸기를 연상시킴",
    "error": "저자 입장에서 능동적으로 구성하는 행동을 저자 뜻의 수동 수용으로 바꾸었다."
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/AHB.json",
  "quota_status": "unavailable"
}
```
