

<!-- luna-raw:BEL-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G402",
  "selected_answer": 5,
  "confidence": 0.98,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "blind G402_visual01 보기: 같은 시스템 내 서로 다른 기술적 특성의 충돌",
    "5문단 기능 추가→부가 회로→전력 소모 증가",
    "4문단 인체 이식의 윤리 문제"
  ],
  "minimal_logic_without_codes": "기능 증가라는 기술적 이득과 소비 전력 증가라는 기술적 부담이 같은 시스템에서 맞물리는⑤가 정의에 맞다. 보안과 윤리의 충돌은 두 기술적 특성 사이의 충돌이 아니다.",
  "intermediate_reasoning": [
    "①③은 정보 노출 위험의 원인·결과이며 양쪽 기술 특성의 상충이 제시되지 않는다.",
    "②는 장의 세기와 통신 범위의 증가만 말해 한쪽 개선의 반대편 불이익을 명시하지 않는다.",
    "④는 보안 개선과 윤리 문제의 충돌이지만 보기의 기술적 특성끼리라는 범위를 벗어난다.",
    "⑤는 더 많은 기능을 얻으려 전력 소모 부담을 늘린다."
  ],
  "attractive_wrong": {
    "choice": 4,
    "exact_error": "이득과 문제의 공존만으로 판단하여 기술적 특성끼리라는 정의의 영역 제한을 삭제한다."
  }
}
```
