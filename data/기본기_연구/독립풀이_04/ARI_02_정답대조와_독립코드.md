

<!-- luna-raw:ARI-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G291",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "단일 금리 수준 수렴을 국가 간 격차 심화로 반전했다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ARI",
    "ARJ",
    "ARK"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ARI-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G291",
  "primary": [
    49
  ],
  "auxiliary": [
    86,
    5
  ],
  "surface": [
    46
  ],
  "decisive_operation": "금융 이동으로 금리 격차가 줄어드는 수렴을 격차 증가로 바꾼 방향 반전을 찾는다.",
  "competing_codes": [
    {
      "code": 46,
      "rebuttal": "국제 시장 작동이라는 인과 배경이 있지만 중간 경로를 새로 복원하지 않고 명시된 변화 방향의 반전을 대조한다."
    },
    {
      "code": 86,
      "rebuttal": "비교량은 국가 간 금리 차이다. 실질 수치 계산보다 차이의 증감 방향이 정답의 직접 기준이다."
    },
    {
      "code": 5,
      "rebuttal": "변화라는 넓은 내용과 중첩되지만 수렴/발산의 방향을49가 더 구체화한다."
    }
  ],
  "boundary_note": "49를 통계적 상관만으로 한정하지 않는 기존 범위에 따르며 금리 수준 자체와 국가 간 격차를 혼동하지 않는다.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
