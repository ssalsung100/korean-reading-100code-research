

<!-- luna-raw:ARU-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G295",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "기대된 역할의 미수행을 역할 부재로 바꾸어 국내 물가 전념을 정당화했다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ARU",
    "ARV",
    "ARW"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ARU-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G295",
  "primary": [
    79
  ],
  "auxiliary": [
    46,
    17
  ],
  "surface": [
    78
  ],
  "decisive_operation": "최대 채권국에 기대한 최종 대부 역할과 실제 미수행을 분리하고 미수행에서 책임 부재를 도출한①의 정당화를 배제한다.",
  "competing_codes": [
    {
      "code": 78,
      "rebuttal": "국내 물가에 전념한 동기를 설명하는 형식이지만 핵심 오류는 요구된 제도적 역할의 부정이다."
    },
    {
      "code": 46,
      "rebuttal": "역할이 아니었기 때문에라는 인과를 새로 붙인 점도 유효한 반박 경로다.79는 원문의 규범적 기대/실제 행동 차이를 대표한다."
    },
    {
      "code": 10,
      "rebuttal": "국제 체계에 최종 대부자가 필요하다는 근거가 있지만 특정 국가의 미수행을 역할 없음으로 바꾼 오류 전체를 필요조건만으로 환원하지 않는다."
    }
  ],
  "boundary_note": "본문의 기대·책임과 실제 법적 임명/기관 지위를 구분한다. 외부 제도 사실로①을 판단하지 않았다.",
  "confidence": 0.88,
  "sdss_seen": false
}
```
