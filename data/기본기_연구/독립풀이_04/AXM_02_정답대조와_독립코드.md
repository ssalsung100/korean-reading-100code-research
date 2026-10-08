

<!-- luna-raw:AXM-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G344",
  "first_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "일부 유형의 개별 효과 입증을 생략하므로 전체 집행 비용은 절약된다.",
  "group_barrier": "전체3개blind 저장 후 정답만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AXM-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G344",
  "primary": [
    49
  ],
  "auxiliary": [
    88,
    46
  ],
  "surface": [
    25,
    77
  ],
  "decisive_operation": "일부 유형 심사 생략→입증 부담 감소→전체 집행 비용 절약의 방향을 확인하고④의 증가를 배제한다.",
  "competing_codes": [
    {
      "code": 88,
      "rejection": "비용-오류 절충은 배경이나④는 절충 최적점 비교 아닌 비용 증감 역전이다."
    },
    {
      "code": 25,
      "rejection": "두 유형 분류만 알아도 비용 방향을 따로 확인해야 한다."
    },
    {
      "code": 43,
      "rejection": "비교 실험의 다른 변수 통제는 없다."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.9,
  "quota_status": "unavailable"
}
```
