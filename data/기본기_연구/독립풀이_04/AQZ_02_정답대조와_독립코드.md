

<!-- luna-raw:AQZ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G288",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "원인으로 조절 복잡성을 언급하는 것과 조절의 구체 과정을 설명하는 것은 다르다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "AQZ",
    "ARA",
    "ARB"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:AQZ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G288",
  "primary": [
    56
  ],
  "auxiliary": [
    64
  ],
  "surface": [
    45,
    46
  ],
  "decisive_operation": "본문이 제공한 설명의 수준과 질문이 요구하는 설명의 수준을 대조한다. 발현 조절이라는 원인 항목의 제시는 조절이 어떻게 일어나는지의 메커니즘 설명이 아니다.",
  "competing_codes": [
    {
      "code": 46,
      "rebuttal": "④의 왜 제한적인가에는 인과 설명이 있지만 정답③은 바로 그 원인 내부의 작동 과정에 관한 설명 공백이다."
    },
    {
      "code": 45,
      "rebuttal": "입력-처리-출력 대응을 복원할 자료가 주어지지 않은 점을 확인하는 문항이며 실제 함수 구조를 계산하지 않는다."
    },
    {
      "code": 64,
      "rebuttal": "정보 범위 확인이라는 과업으로 중첩되나 설명의 깊이 차이가 구체 결정 기준이다."
    }
  ],
  "boundary_note": "본문에 설명이 없다는 것과 과학에서 전혀 모른다는 것을 동일시하지 않는다. 마지막 미개발 진술은 원문 시점의 내용으로만 취급한다.",
  "confidence": 0.91,
  "sdss_seen": false
}
```
