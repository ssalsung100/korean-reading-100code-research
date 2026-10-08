

<!-- luna-raw:BPJ-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G499",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "같은 입력으로 여러 규칙이 동시에 만족될 수 있으면 오버랩을 금지하는 기본 유일 정책을 사용할 수 없으므로①이 맞는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BPJ-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G499",
  "minimal_logic_without_codes": "둘 이상의 규칙이 동시에 참일 수 있는 구조는 동시에 하나만 허용하는 유일 정책의 요구와 충돌한다.",
  "primary": [
    {
      "code": 13,
      "reason": "같은 입력의 복수 적중 가능성과 유일 정책의 무중복 요건이 양립할 수 없음을 판정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 15,
      "reason": "적중 정책의 선택 기준을 규칙의 중복 여부에 적용한다."
    },
    {
      "code": 12,
      "reason": "복수 적중이 가능하면 기본 유일 정책을 쓸 수 없다는 조건을 도출한다."
    },
    {
      "code": 23,
      "reason": "여러 조건 열은 모두 참이어야 하는 AND 결합임을 유지한다."
    },
    {
      "code": 45,
      "reason": "하위 출력이 상위 입력이 되는 간접 경로와 전달 방향을 판독한다."
    }
  ],
  "surface": [
    {
      "code": 8,
      "reason": "우선순위 정책은 다른 대안이지만①은 기본 정책의 적용 가능성이 쟁점이다."
    }
  ],
  "competing_codes": [
    {
      "code": 18,
      "rejection": "논리적으로 모든 명제가 모순이라는 판단이 아니라 특정 규칙 집합과 정책 요구의 불일치다."
    },
    {
      "code": 4,
      "rejection": "하나/여럿의 수량이 있어도 범위 확대 오류보다 두 요구의 양립 불가가 직접 결론이다."
    },
    {
      "code": 50,
      "rejection": "직접 연결 부재가 간접 경로 차단을 뜻하지 않는다.④를 판정할 때 상위 전달을 삭제하지 않는다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
