

<!-- luna-raw:AVA-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G323",
  "initial_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "official_answer_source": "sealed 공식 페이지 검증 정본",
  "code_free_logic": "결맞음 길이>국소화 길이의 비교 방향 보존.",
  "barrier": "group 전체 blind 저장 후 공개"
}
```


<!-- luna-raw:AVA-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    10,
    86
  ],
  "auxiliary": [
    17
  ],
  "surface": [
    49,
    46
  ],
  "decisive_operation": "국소화 발생에 필요한 두 길이의 부등식 방향을 확인한다.",
  "competitor_refutations": [
    {
      "code": 49,
      "reason": "두 길이의 증감 공변이 아니라 어느쪽이 더 커야 하는지의 조건 비교다."
    },
    {
      "code": 11,
      "reason": "필요조건으로 주어진 관계를충분조건까지 포함한동치로 만들지 않는다."
    },
    {
      "code": 46,
      "reason": "온도 경로는③ 확인이며정답①은 비교조건 반전이다."
    }
  ],
  "confidence": 0.98,
  "passage_group": "G323",
  "sdss_seen": false
}
```
