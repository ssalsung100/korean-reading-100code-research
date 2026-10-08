

<!-- luna-raw:ASA-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G297",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "이성적 판단과 행동의 불일치 여부로 자제력 없음과 무절제를 구분한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASA",
    "ASB",
    "ASC"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASA-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G297",
  "primary": [
    39
  ],
  "auxiliary": [
    78,
    16
  ],
  "surface": [
    13
  ],
  "decisive_operation": "자제력 없음과 무절제에서 이성 판단-욕구 행동의 일치 여부를 같은 축으로 비교한다.",
  "competing_codes": [
    {
      "code": 78,
      "rebuttal": "행동과 욕구·선택의 관계라는 내용은 유효하며39의 비교 과업과 중첩된다."
    },
    {
      "code": 16,
      "rebuttal": "두 정의를 풀어야 하지만 결정은 공유 소재 아래 차별 요건인 판단/행동 일치 여부다."
    },
    {
      "code": 13,
      "rebuttal": "이성/욕구가 언제나 양립 불가한 것이 아니다. 무절제에서는 같은 방향이라는 반례가 있다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
