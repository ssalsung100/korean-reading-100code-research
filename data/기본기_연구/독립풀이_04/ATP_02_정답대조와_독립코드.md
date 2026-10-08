

<!-- luna-raw:ATP-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G310",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "폐단의 지시 대상은 기존 문제와 새 제도의 예상 부작용으로 나뉘며 같은 단어만으로 합치지 않는다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ATN",
    "ATO",
    "ATP"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ATP-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G310",
  "primary": [
    99
  ],
  "auxiliary": [
    3,
    17,
    39
  ],
  "surface": [
    1
  ],
  "decisive_operation": "같은 폐단이라는 표현의 선행 내용과 시점을 추적하여 기존 군역 문제와 새 제도 부작용을 구별한다.",
  "competing_codes": [
    {
      "code": 3,
      "rebuttal": "기존/향후의 시간 차이는 지시 대상 구별의 핵심 근거이며99와 중첩된다."
    },
    {
      "code": 1,
      "rebuttal": "작은/큰은 발화자의 평가 강도지만 지칭 내용이 무엇인지가 먼저다."
    },
    {
      "code": 39,
      "rebuttal": "두 표현이 같은 대상인지 비교하는 과업으로99의 대용표현 해소와 겹친다."
    }
  ],
  "confidence": 0.98,
  "sdss_seen": false
}
```
