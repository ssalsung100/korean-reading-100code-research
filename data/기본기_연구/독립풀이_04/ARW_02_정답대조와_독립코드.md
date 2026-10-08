

<!-- luna-raw:ARW-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G295",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "본문은 전후 긴축 강도 동일성을 요구하지 않는다. 단순 강도 차이 정보는 붕괴 후 긴축의 인과적 기여와 양립한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ARU",
    "ARV",
    "ARW"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ARW-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G295",
  "primary": [
    63
  ],
  "auxiliary": [
    62,
    3,
    85
  ],
  "surface": [
    86
  ],
  "decisive_operation": "새 진술이 본문의 실제 인과 전제나 기여도를 낮추는지 판단하며 요구되지 않은 전후 동일성을 부정하는③을 중립으로 판정한다.",
  "competing_codes": [
    {
      "code": 62,
      "rebuttal": "③의 관련성 부족을 구체적으로 설명하므로63과 공동 대표 가능. 전체는 다섯 정보의 지지 방향 대조다."
    },
    {
      "code": 3,
      "rebuttal": "②의 원인 후보가 결과 이후라는 시간 정보는 약화 근거지만③의 단순 전후 강도 차이와는 다르다."
    },
    {
      "code": 85,
      "rebuttal": "①④는 전체 소비 중 해당 감소 원인의 비중을 낮추는 경로에 유효하지만③의 무효 비판을 단독 설명하지 못한다."
    },
    {
      "code": 86,
      "rebuttal": "강도 차이라는 양적 비교가 있어도 그 차이가 결과 인과 설명을 약화하는 방향·크기가 주어지지 않았다."
    }
  ],
  "boundary_note": "부분 원인의 기여가 작다는 것은 기여0이나 전체 논증의 완전 반증을 뜻하지 않는다.⑤의 대체 책임 설명도 논증 약화로만 평가한다.",
  "confidence": 0.96,
  "sdss_seen": false
}
```
