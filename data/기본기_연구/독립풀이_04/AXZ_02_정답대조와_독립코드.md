

<!-- luna-raw:AXZ-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G348",
  "first_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "장애물 부재가 우주통신을 허용하며 원거리 전달력 증가를 뜻하지 않는다. 낮은 주파수는 더 적은 기지국을 요구하는 방향이다. 디지털 주파수>아날로그만 참이다.",
  "group_barrier": "all_group_blind_records_before_any_group_answer_check 확인",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AXZ-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G348",
  "primary": [
    46,
    56
  ],
  "auxiliary": [
    49,
    86,
    12
  ],
  "surface": [
    25
  ],
  "decisive_operation": "ㄱ의 실제 사용 이유인 장애물 부재를 원거리 전달력 우수로 바꾼 설명을 기각하고,ㄴ은 주파수에 따른 전달력과 기지국 보완 필요의 방향을 이어 기각한다.ㄷ은 두 방송대역의 순서 비교.",
  "competing_codes": [
    {
      "code": 49,
      "rejection": "ㄴ에는 중요하지만 ㄱ은 방향 적용 이전에 용도를 설명하는 이유 자체가 바뀌었다. 보조 유지."
    },
    {
      "code": 43,
      "rejection": "우주통신에서 장애물이 없다는 전제는 쓰지만 대조실험의 타변수통제 또는 효과식별은 수행하지 않는다."
    },
    {
      "code": 44,
      "rejection": "기지국이 원거리 취약성 극복의 수단인 부분에는 적용되나 ㄱ의 잘못된 설명과ㄷ까지 단독 포괄하지 않는다."
    },
    {
      "code": 86,
      "rejection": "정답조합을 이루는ㄷ만 직접 비교. 옳은 명제 확인과 오답 배제 경로가 다름을 보존."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.89,
  "quota_status": "unavailable"
}
```
