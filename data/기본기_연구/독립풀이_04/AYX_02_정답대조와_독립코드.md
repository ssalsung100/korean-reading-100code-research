

<!-- luna-raw:AYX-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G356",
  "first_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "조합 출력은 저장 입력이며 인버터를 거쳐 저장 출력은 반전된다.",
  "group_barrier": "전체blind저장후정답공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AYX-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G356",
  "primary": [
    45
  ],
  "auxiliary": [
    17,
    12
  ],
  "surface": [
    40,
    46
  ],
  "decisive_operation": "회로의 출력 위치를 고정하고 조합출력→저장입력→인버터→저장출력 순서의 변환을 추적한다.",
  "competing_codes": [
    {
      "code": 40,
      "rejection": "부품이 여러개라는 구성은 배경. 결론은 그 사이 입력출력 변환에 의해 정해진다."
    },
    {
      "code": 46,
      "rejection": "회로작동은 물리인과이나 세부 전기기제 대신 명시된 논리함수로 판정 가능."
    },
    {
      "code": 17,
      "rejection": "서로다른회로출력대상을같게읽은범위교환이 보조로 필요하지만 반전함수45가 직접근거."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.92,
  "quota_status": "unavailable"
}
```
