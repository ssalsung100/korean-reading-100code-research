

<!-- luna-raw:BPB-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G496",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "상황2에서 같은 A트랜잭션의 읽기들 사이로 B와C가 끼어들었다. 개별 작업에 번호가 있다는 사실은 트랜잭션 전체가 하나씩 순차 실행됐다는 뜻이 아니므로④가 틀리다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BPB-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G496",
  "minimal_logic_without_codes": "A의 조회들 사이에 B와C의 쓰기가 들어가 있으므로 개별 작업의 번호 순서는 트랜잭션 전체의 순차 실행을 뜻하지 않는다.",
  "primary": [
    {
      "code": 40,
      "reason": "트랜잭션 전체와 그것을 구성하는 개별 작업을 구분한다."
    }
  ],
  "auxiliary": [
    {
      "code": 3,
      "reason": "조회가 갱신·완료·롤백보다 앞인지 뒤인지 추적한다."
    },
    {
      "code": 17,
      "reason": "각 작업이 A/B/C 중 어느 트랜잭션에 속하는지 유지한다."
    },
    {
      "code": 25,
      "reason": "값 변경, 롤백, 레코드 삽입에 따라 읽기 문제의 세 유형을 나눈다."
    },
    {
      "code": 12,
      "reason": "최고 격리가 팬텀을 막으면서 하위 오염도 막는 누적 보장 규칙을 적용한다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "잔액 숫자가 있지만 산술 금액 계산보다는 서로 다른 시점 값의 동일성·차이를 확인한다."
    }
  ],
  "competing_codes": [
    {
      "code": 41,
      "rejection": "부분의 순서 속성을 전체에 옮기는 오독으로도 기술할 수 있어40과 국소 중첩한다. 전형적 부분속성 합산 오류와 완전히 동일한 것으로 확정하지 않는다."
    },
    {
      "code": 18,
      "rejection": "모순된 읽기라는 기술 용어가 있지만 형식 논리의 p와¬p를 증명하는 문제가 아니다."
    },
    {
      "code": 43,
      "rejection": "같은 입력의 통제 실험이 아니라 주어진 작업 순서를 따라 상태와 조회 결과를 추적한다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
