

<!-- luna-raw:AWK-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G335",
  "initial_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2023/2023_answer_언어이해정답.pdf",
  "code_free_logic": "N/√N=√N이므로출력증가시산탄신호대잡음비증가.",
  "barrier": "group 전체 blind 저장 후 공개"
}
```


<!-- luna-raw:AWK-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    84,
    92
  ],
  "auxiliary": [
    91,
    17
  ],
  "surface": [
    49,
    46
  ],
  "decisive_operation": "신호N과잡음√N의서로다른증가율을비율로합성.",
  "competitor_refutations": [
    {
      "code": 49,
      "reason": "잡음증가와정확도감소의단순연상으로는분자증가를놓친다."
    },
    {
      "code": 86,
      "reason": "절대잡음과상대신호대잡음비라는비교대상을먼저나눠야한다."
    },
    {
      "code": 46,
      "reason": "출력기제는재료지만정답은분수관계의증감이다."
    }
  ],
  "confidence": 0.98,
  "passage_group": "G335",
  "sdss_seen": false
}
```
