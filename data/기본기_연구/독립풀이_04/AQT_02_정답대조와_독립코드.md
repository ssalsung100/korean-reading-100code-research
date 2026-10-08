

<!-- luna-raw:AQT-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G286",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "공통은 관습법의 법적 지위와 법원의 고려다. 법률 충돌 시 배제 가능성은 공통이 아니다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "AQT",
    "AQU",
    "AQV"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:AQT-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G286",
  "primary": [
    23
  ],
  "auxiliary": [
    75,
    17
  ],
  "surface": [
    19,
    8
  ],
  "decisive_operation": "관습법의 효력 범위에 대한 서로 다른 두 입장의 동의 명제를 각각 확인해 공통 부분을 선택한다.",
  "competing_codes": [
    {
      "code": 75,
      "rebuttal": "입장별 귀속 유지가 필수라 보조로 둔다. 마지막 선택은 견해 차이 자체보다 공통으로 승인하는 내용의 추출이다.23과 과업 층위 중첩 가능."
    },
    {
      "code": 19,
      "rebuttal": "보충적 효력설의 구조를 설명하지만 변경설까지 공유하는 명제를 단독으로 고르지는 못한다."
    },
    {
      "code": 8,
      "rebuttal": "법률/관습법 우선성은 양설의 차이이며 정답 공통 명제의 핵심 내용은 아니다."
    }
  ],
  "boundary_note": "확신 없는 법률과 법률 규정 없음의 차이는②의 공통성 오독을 막는 대상 범위 구별이다.",
  "confidence": 0.92,
  "sdss_seen": false
}
```
