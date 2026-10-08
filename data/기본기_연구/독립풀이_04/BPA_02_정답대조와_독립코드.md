

<!-- luna-raw:BPA-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G496",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "독점 사용이라는 기본 잠금 속성만으로 직렬화·완전 격리가 보장되지는 않는다.⑤는 기본 기법에2단계 잠금의 보장을 옮긴다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BPA-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G496",
  "minimal_logic_without_codes": "독점 사용이라는 기본 잠금 속성만으로 직렬화 보장이라는 결과를 얻을 수 없고 추가 기법의 구조가 필요하다.",
  "primary": [
    {
      "code": 62,
      "reason": "기본 잠금을 완전 격리의 충분한 보장으로 보는⑤의 연결을 부정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "기본 잠금과2단계 잠금에 귀속된 보장을 바꾸지 않는다."
    },
    {
      "code": 15,
      "reason": "격리 수준별로 막을 수 있는 문제를 구분한다."
    },
    {
      "code": 10,
      "reason": "팬텀 읽기에 필요한 반복 질의·삽입 요건을④에서 확인한다."
    },
    {
      "code": 25,
      "reason": "갱신 분실과 세 종류의 읽기 문제를 구분한다."
    }
  ],
  "surface": [
    {
      "code": 9,
      "reason": "격리 수준 위계는 있으나⑤는 어느 단계의 보장을 일반 잠금에 옮겼는지가 중요하다."
    }
  ],
  "competing_codes": [
    {
      "code": 50,
      "rejection": "접근을 막는다는 표현은 있지만 문제는 잠금이 어떤 전체 실행을 보장하는지이며 차단 하나로 모든 간섭을 제거했다고 할 수 없다."
    },
    {
      "code": 13,
      "rejection": "동시성과 격리성의 긴장이 있다고 모든 동시 실행과 안전한 결과가 양립 불가능한 것은 아니다."
    },
    {
      "code": 91,
      "rejection": "격리와 성능의 방향을 일정 비례 법칙으로 읽지 않는다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
