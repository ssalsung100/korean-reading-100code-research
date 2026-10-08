

<!-- luna-raw:AQV-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G286",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "판결이 이미 성립한 법을 확인하는지 법 지위를 부여하는지 구분하면[A]는 국가 인정의 필요성을 강조한③에 가깝다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "AQT",
    "AQU",
    "AQV"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:AQV-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G286",
  "primary": [
    10
  ],
  "auxiliary": [
    75,
    80
  ],
  "surface": [
    3,
    5
  ],
  "decisive_operation": "판결에 의한 승격은 국가 인정이 관습의 법 지위에 구성적으로 필요하다는 입장이다. 이미 있는 법을 사후 확인한다는 견해와 구분한다.",
  "competing_codes": [
    {
      "code": 80,
      "rebuttal": "확인과 성립을 혼동하지 않는 데 필요하지만[A]는 지식 획득보다 법적 지위 성립 요건을 강조한다."
    },
    {
      "code": 75,
      "rebuttal": "두 관점을 귀속하는 과업과 중첩된다.10은 그 관점 차이의 결정 내용이며 배타적인 번호 분류는 아니다."
    },
    {
      "code": 3,
      "rebuttal": "성립 시점이 달라질 수 있지만 순서만으로 국가 인정의 구성적 지위와 단순 확인을 구별할 수 없다."
    }
  ],
  "boundary_note": "[A]에 가장 가까운 견해를 고르는 과업이며③의 국가 정립 일반론 전체를[A]가 엄밀히 논리 함축한다고 주장하지 않는다.",
  "confidence": 0.92,
  "sdss_seen": false
}
```
