

<!-- luna-raw:ASQ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G302",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "조건적으로 사실을 인정해도 직책상 부적절하다는 반론을 사실 확인 불가라는 반론으로 바꾸었다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASP",
    "ASQ",
    "ASR"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ASQ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G302",
  "primary": [
    60
  ],
  "auxiliary": [
    28,
    17
  ],
  "surface": [
    63
  ],
  "decisive_operation": "상대 설명을 가정적으로 받아들인 뒤 직책상 적용을 반박하는 논증을 증거 확인 불가의 논증과 구별한다.",
  "competing_codes": [
    {
      "code": 73,
      "rebuttal": "반박은 은밀한 간언이 없다는 전제 부정이 아니다. 사실을 허용해도 간관의 직무와 안 맞는다고 한다."
    },
    {
      "code": 28,
      "rebuttal": "그렇다고 하더라도라는 양보 구조가 핵심 내용이며60의 말하기 전략 분류와 중첩된다."
    },
    {
      "code": 63,
      "rebuttal": "새 정보를 넣어 주장 지지력을 평가하기보다 실제 수행한 반박 방식의 기술 정확성을 묻는다."
    }
  ],
  "confidence": 0.97,
  "sdss_seen": false
}
```
