

<!-- luna-raw:ASO-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G301",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "과거 사건을 말하는 현재 대화와 과거 장면 자체의 교차를 구별한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASM",
    "ASN",
    "ASO"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASO-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G301",
  "primary": [
    93
  ],
  "auxiliary": [
    100,
    3
  ],
  "surface": [
    80
  ],
  "decisive_operation": "사건·주제가 현재 대사를 통해 전달되는지 장면 전환·내면 흐름으로 직접 제시되는지 구분하고 우의적 의미를 확인한다.",
  "competing_codes": [
    {
      "code": 3,
      "rebuttal": "ㄴ 배제는 사건의 과거 시점과 제시 장면의 현재 시점을 구분하는 국소 핵심이다. 전체는 전달 양식 판정이다."
    },
    {
      "code": 100,
      "rebuttal": "ㄷ의 정치 우의에 실질 근거가 있지만ㄱ 대사 전달과ㄴㄹ 형식 배제까지 단독 설명하지 않는다."
    },
    {
      "code": 80,
      "rebuttal": "내면 언급이 있다고 의식의 흐름이라는 제시 방식이 성립하지 않는다."
    }
  ],
  "confidence": 0.91,
  "sdss_seen": false
}
```
