

<!-- luna-raw:BPA-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G496",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "잠금 기법·2단계 잠금 설명",
      "evidence": "기본 잠금은 독점 사용을 제공하지만 직렬화 가능한 실행을 보장하지 못한다.2단계 잠금은 이를 보장한다."
    },
    {
      "location": "격리 수준·읽기 유형 정의",
      "evidence": "최고 격리는 순차 실행과 같은 결과, 낮은 격리는 독립성이 약함. 팬텀 읽기는 삽입과 반복 질의로 다른 레코드 세트를 얻는 경우다."
    }
  ],
  "minimal_logic_without_codes": "독점 사용이라는 기본 잠금 속성만으로 직렬화·완전 격리가 보장되지는 않는다.⑤는 기본 기법에2단계 잠금의 보장을 옮긴다.",
  "intermediate_reasoning": [
    "① 최고 격리에서는 순차 실행과 같은 결과여서 상호 간섭에 의한 갱신 분실을 막는다.",
    "② 최저 단계는 모든 모순된 읽기가 가능하다.",
    "③ 최고에서 최저로 낮추면 독립성이 약해진다.",
    "④ 갱신 작업만 있고 질의·삽입이 없다면 정의된 팬텀 읽기의 조건이 없다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "동시 실행에서 문제가 생길 수 있다는 일반 서술을 모든 문제 유형이 반드시 가능하다는 말로 읽어, 팬텀의 질의·삽입 요건을 놓친다."
  },
  "scope_limit": "기출의 데이터베이스 모형만 판독하며 실제 시스템 조작이나 원문 밖 기법 확장을 하지 않는다."
}
```
