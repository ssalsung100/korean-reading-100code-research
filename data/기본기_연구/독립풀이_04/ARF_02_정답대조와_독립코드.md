

<!-- luna-raw:ARF-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G290",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "필요·전제 관계를 개념의 상하위 분류로 바꾼 오류다. 분류상 같은 층위와 가치 우선순위도 구분한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ARF",
    "ARG",
    "ARH"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ARF-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G290",
  "primary": [
    25
  ],
  "auxiliary": [
    10,
    9
  ],
  "surface": [
    8,
    44
  ],
  "decisive_operation": "실정성과 안정성의 전제 관계를 종류의 포함 관계로 잘못 바꿨는지 판정한다. 같은 법이념 수준이라는 분류와 실천적 우선성은 구별한다.",
  "competing_codes": [
    {
      "code": 10,
      "rebuttal": "원문의 실제 연결이 필요조건이라는 내용 관점에서 공동 주 후보가 가능하다.25는 잘못 제시된 하위 개념 분류 검증이라는 과업 대표다."
    },
    {
      "code": 9,
      "rebuttal": "상하위의 층위 표현은 있지만 가치의 높낮이 서열과 개념 분류를 동일시하지 않는다."
    },
    {
      "code": 8,
      "rebuttal": "안정성 우선이라는 실천 선택은③의 분류상 동등성을 부정하지 않는다."
    }
  ],
  "boundary_note": "25/10은 원관계와 오독된 관계의 두 끝을 설명하므로 전역 배타 분할하지 않는다.",
  "confidence": 0.93,
  "sdss_seen": false
}
```
