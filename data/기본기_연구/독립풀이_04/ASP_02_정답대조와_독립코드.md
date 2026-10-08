

<!-- luna-raw:ASP-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G302",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "공유 규범ㄴㄷ과 나만의 상황별 직무 규범ㄱㄹ을 구분한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASP",
    "ASQ",
    "ASR"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASP-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G302",
  "primary": [
    23
  ],
  "auxiliary": [
    75,
    79
  ],
  "surface": [
    5
  ],
  "decisive_operation": "상대별로 규범의 수용을 확인하여 공유하는 비공격·비명예추구만 추출한다.",
  "competing_codes": [
    {
      "code": 75,
      "rebuttal": "주체별 규범 귀속은 필수이지만 최종은 그 공통부분 추출로23과 중첩된다."
    },
    {
      "code": 79,
      "rebuttal": "당위가 내용이나 모든 당위를 둘이 공유하는 것은 아니다."
    },
    {
      "code": 5,
      "rebuttal": "덕의 지속/상황 변화는 입장의 차이를 설명하며 공통점의 직접 대표는 아니다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
