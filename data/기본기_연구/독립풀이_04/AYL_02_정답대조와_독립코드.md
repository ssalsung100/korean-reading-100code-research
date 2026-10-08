

<!-- luna-raw:AYL-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G352",
  "first_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "D=A+B-C-E를간접산출한다. 직접온도·융해량측정으로서술한④는틀림.",
  "group_barrier": "전체3개blind 저장 후 정답만공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AYL-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G352",
  "primary": [
    45
  ],
  "auxiliary": [
    92,
    56,
    17
  ],
  "surface": [
    46,
    80
  ],
  "decisive_operation": "측정된A,B,C,E를입력으로D를산출하는절차와D를직접관측하는절차를구분한다.",
  "competing_codes": [
    {
      "code": 46,
      "rejection": "따뜻한해수→융해는실제원인이지만그물리원인을측정방법이라고바꿔읽으면④에속는다."
    },
    {
      "code": 92,
      "rejection": "질량수지식이간접산출을명료하게하나정답결정은수치계산없이방법대조로가능."
    },
    {
      "code": 43,
      "rejection": "통제실험의효과식별이아니라어떤측정치를입력으로쓰는지확인한다."
    },
    {
      "code": 80,
      "rejection": "앎/추정방식이라는넓은해석은가능해도측정절차의입출력교환이라는구체판정을우선한다."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.91,
  "quota_status": "unavailable"
}
```
