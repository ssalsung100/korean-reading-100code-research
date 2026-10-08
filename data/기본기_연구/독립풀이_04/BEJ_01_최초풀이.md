

<!-- luna-raw:BEJ-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G402",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "1문단 전자기 유도와 비접촉",
    "2문단 다중 태그 충돌 해결",
    "4문단 고정 암호의 경로 노출 한계",
    "5문단 전자기장 세기와 공급 전력"
  ],
  "minimal_logic_without_codes": "내용을 암호화해도 동일한 표지가 계속 나타나면 이동 위치를 연결할 수 있다고 본문이 말한다. 내용 보호와 위치 관계 은폐는 다르다.",
  "intermediate_reasoning": [
    "① 일반적 암호화만으로 경로 노출까지 방지한다고 한정 없이 말하면 4문단과 어긋난다.",
    "② 태그는 리더 전자기장의 유도 전력을 필요로 한다.",
    "③ 충돌 해결 알고리즘으로 거의 동시 정보 읽기가 가능하다.",
    "④ 전자기장 세기를 늘려 공급 전력을 높이려 한다는 설명이 있다.",
    "⑤ 직접 접촉 없이 읽는 편의가 명시된다."
  ],
  "attractive_wrong": {
    "choice": 4,
    "exact_error": "세기 증가의 간섭 부작용을 전력 공급 증가 자체의 불가능으로 오인한다. 부작용과 국소 기능 개선은 양립한다."
  },
  "scope": "기술 내용은 제공된 국어 독해 자료의 주장으로만 다룸."
}
```
