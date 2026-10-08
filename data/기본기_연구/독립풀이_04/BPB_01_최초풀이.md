

<!-- luna-raw:BPB-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G496",
  "selected_answer": 4,
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
      "location": "공식 상황1",
      "evidence": "B갱신(1) 뒤 A가갑200조회(2), B롤백(3). C가을600갱신(4)·완료(5)한뒤 A가을600조회(6)."
    },
    {
      "location": "공식 상황2",
      "evidence": "A갑100조회(1), B갑200갱신(2)·완료(3), A갑200조회(4). A세트{갑,을}조회(5), C병삽입(6)·완료(7), A세트{갑,을,병}조회(8)."
    }
  ],
  "minimal_logic_without_codes": "상황2에서 같은 A트랜잭션의 읽기들 사이로 B와C가 끼어들었다. 개별 작업에 번호가 있다는 사실은 트랜잭션 전체가 하나씩 순차 실행됐다는 뜻이 아니므로④가 틀리다.",
  "intermediate_reasoning": [
    "① 갑200은 완료 전 읽은 뒤 롤백된 값이라 오염, 을600은 완료 후 값이라 이 정의의 오염이 아니다.",
    "② 미완료 읽기를 막으면 상황1의 오염된 읽기를 막을 수 있다.",
    "③ 상황1의 오염, 상황2의 반복 불가능 읽기와 팬텀으로 총3유형이다.",
    "⑤ 상황2의 팬텀까지 막으려면 최고 격리가 필요하며 이 수준은 상황1의 오염도 막는다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "서로 다른 문제 유형이므로 하나를 막는 설정은 다른 것을 못 막는다고 생각하면, 격리 수준이 낮은 단계의 보호를 포함하는 누적 구조를 놓친다."
  },
  "source_restoration": {
    "crop": "data/기본기_연구/prepared_backlog/blind_sources/BPB_official_scenarios_crop.png",
    "astra_direct_seen": true,
    "resolved_before_answer_disclosure": true,
    "original_hold_preserved": true
  },
  "scope_limit": "기출에 주어진 작업 번호와 상태 전이만 분석한다."
}
```
