

<!-- luna-raw:ASR-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G302",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "직무를 알면서 수행하지 않음을 직무 지식 부족으로 설명하지 않는다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASP",
    "ASQ",
    "ASR"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASR-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G302",
  "primary": [
    75
  ],
  "auxiliary": [
    78,
    79
  ],
  "surface": [
    80
  ],
  "decisive_operation": "나의 인물 평가를 직무에 대한 지식 부족이 아닌 역할 수행의 회피로 고정해 가까운 묘사를 선택한다.",
  "competing_codes": [
    {
      "code": 78,
      "rebuttal": "행동·태도 설명은 내용상 핵심이며75의 평가 주체 귀속과 중첩된다."
    },
    {
      "code": 80,
      "rebuttal": "알고 있는지와 행동하는지는 다르다.③은 지식 부재라는 잘못된 이유를 붙인다."
    },
    {
      "code": 79,
      "rebuttal": "마땅한 직무가 평가 기준이나 정답은 그 규범에 비추어 양성이 실제 어떤 태도인지 묘사한다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
