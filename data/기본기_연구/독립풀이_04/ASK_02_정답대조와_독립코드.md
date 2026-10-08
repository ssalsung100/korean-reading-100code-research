

<!-- luna-raw:ASK-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G300",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "㉠의 화성 기원·생명 흔적과 우주 체류 기간의 지표를 구분한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASJ",
    "ASK",
    "ASL"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASK-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G300",
  "primary": [
    64
  ],
  "auxiliary": [
    60,
    17
  ],
  "surface": [
    63
  ],
  "decisive_operation": "증거별로 어떤 주장을 지지하는지 연결해 화성 기원/생명 흔적이라는 지정 논의 밖의 체류기간 지표를 제외한다.",
  "competing_codes": [
    {
      "code": 63,
      "rebuttal": "기존 주장에 반대 증거를 더하는 것이 아니라 관련된 증거인지 범위를 판단한다."
    },
    {
      "code": 60,
      "rebuttal": "증거-주장 연결 구조는 유효하며64의 관련 범위 판정과 중첩된다."
    },
    {
      "code": 3,
      "rebuttal": "ⓒ가 시간 정보인 것은 내용이지만 날짜 순서를 복원해야 답이 갈리는 것은 아니다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
