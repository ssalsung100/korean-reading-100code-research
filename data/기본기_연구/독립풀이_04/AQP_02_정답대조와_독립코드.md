

<!-- luna-raw:AQP-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G284",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "문사 등용의 적절성과 군주 자신의 학문 수양은 다른 평가 항목이다. 후자는 본문 근거 없다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "AQN",
    "AQO",
    "AQP"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:AQP-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G284",
  "primary": [
    15
  ],
  "auxiliary": [
    37,
    17
  ],
  "surface": [
    100
  ],
  "decisive_operation": "구체적 왕 평가 근거를 상벌·직언·인사·백성 돌봄이라는 평가 항목으로 추출하고 선지 원칙과 대응하여 학문 수양 항목의 부재를 찾는다.",
  "competing_codes": [
    {
      "code": 37,
      "rebuttal": "선지 원칙의 사례를 본문에서 찾는 관점과 실질적으로 중첩한다.15는 평가 기준 추출이라는 내용 층위이며 별개 행동으로 중복 계수하지 않는다."
    },
    {
      "code": 100,
      "rebuttal": "목수 비유는④를 수용하기 위한 표현 해독에 적용되나 정답①의 평가 요소 부재를 결정하지 않는다."
    },
    {
      "code": 16,
      "rebuttal": "학문이나 인정의 정의를 새로 분석하는 것이 아니라 이미 주어진 평가 항목의 대응을 확인한다."
    }
  ],
  "boundary_note": "학문이 중요하지 않다는 가치 판단이 아니라 이 글의 평가 근거에 없다는 범위 제한이다.15/37 유일 주 우선순위 전역 확정 없음.",
  "confidence": 0.88,
  "sdss_seen": false
}
```
