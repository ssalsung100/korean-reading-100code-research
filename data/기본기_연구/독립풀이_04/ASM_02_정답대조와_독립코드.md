

<!-- luna-raw:ASM-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G301",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "사망 사실에서 시점·살해·보복 원인을 새로 도출할 수 없다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASM",
    "ASN",
    "ASO"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASM-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G301",
  "primary": [
    46
  ],
  "auxiliary": [
    3,
    2
  ],
  "surface": [
    78
  ],
  "decisive_operation": "남편의 사망 사실에 부임 이후 살해와20년전 사건의 원인 연결을 근거 없이 추가한 것을 배제한다.",
  "competing_codes": [
    {
      "code": 3,
      "rebuttal": "시점 부가는 독립 오류지만 살해 원인도 함께 추가되어46과 중첩된다."
    },
    {
      "code": 78,
      "rebuttal": "복수 동기는 연락관에게 있으나 그 동기가 이 사망을 일으킨 행동으로 실현됐다는 근거가 없다."
    },
    {
      "code": 2,
      "rebuttal": "가능한 이야기를 사실처럼 확정한 강도 문제로도 기술 가능하나 추가된 시점·인과를 구체화해야 한다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
