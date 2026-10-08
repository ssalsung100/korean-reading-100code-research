

<!-- luna-raw:ARL-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G292",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "명제의 진위와 그것을 아는 명료성은 다르다. 적음의 불분명함에서 반대 명제의 분명함으로 건너갈 수 없다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ARL",
    "ARM",
    "ARN"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ARL-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G292",
  "primary": [
    80
  ],
  "auxiliary": [
    18,
    15
  ],
  "surface": [
    49
  ],
  "decisive_operation": "명제 P의 진위와 P를 분명히 인식하는지의 층위를 구별해 P의 불명료성에서 인접 대상의 비P 명료성을 도출하는 비약을 판별한다.",
  "competing_codes": [
    {
      "code": 18,
      "rebuttal": "배중률이 대상의 참/거짓을 가르지만 인식이 불분명하다는 사실은 명제의 거짓과 다르다.18만 적용하면 오히려 층위를 혼동할 수 있다."
    },
    {
      "code": 49,
      "rebuttal": "불분명할수록 반대가 분명해진다는 증감 형식은 선지 표면이다. 그 상관을 왜 추론 못하는지 인식 층위를 설명해야 한다."
    },
    {
      "code": 15,
      "rebuttal": "기준 존재와 기준을 앎의 차이를 명시하는 데 보조이며 정답의 직접 비약은 지식 상태와 명제 내용의 혼동이다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
