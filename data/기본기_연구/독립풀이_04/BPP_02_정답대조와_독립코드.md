

<!-- luna-raw:BPP-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G501",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "현량과 시험은 합격 총원을 선발하지만 전시는 이미 뽑힌 사람의 등수·품계를 정한다.③은 두 시험의 결정 기능을 같게 만든다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BPP-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G501",
  "minimal_logic_without_codes": "전시 이전에 합격33명이 이미 정해졌고 전시는 그들의 등급을 정한다. 현량과 시험의 인원 선발 기능을 전시에 옮긴③이 틀리다.",
  "primary": [
    {
      "code": 17,
      "reason": "합격 총원 결정과 품계 배정이라는 기능을 각 시험 단계에 맞게 귀속한다."
    }
  ],
  "auxiliary": [
    {
      "code": 45,
      "reason": "응시자→합격자 선별과 합격자→등수·품계 배정의 입력·출력을 구분한다."
    },
    {
      "code": 3,
      "reason": "합격자 확정과 전시의 선후를 유지한다."
    },
    {
      "code": 39,
      "reason": "두 시험을 같은 기능으로 비교할 수 있는지 판단한다."
    }
  ],
  "surface": [
    {
      "code": 9,
      "reason": "품계는 서열을 주지만③은 서열의 높낮이보다 어느 단계가 무엇을 정하는지가 쟁점이다."
    }
  ],
  "competing_codes": [
    {
      "code": 31,
      "rejection": "인원 수가 나오지만 원소 수와 집합 수의 교환이 아니다. 선발과 등급 배정의 기능 차이다."
    },
    {
      "code": 10,
      "rejection": "선행 합격이 전시에 필요하다는 조건은 있으나③의 오류를 단순 필요조건 역전으로 환원하지 않는다."
    },
    {
      "code": 92,
      "rejection": "33과28을 계산해 답을 내는 것이 아니라 숫자가 확정되는 절차를 읽는다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
