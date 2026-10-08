

<!-- luna-raw:ATC-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G306",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "strict_blind_eligible": false,
  "logic_without_codes": "지표의 수와 측정 방식의 수, 입력 지표의 단위와 최종 분류 단위를 분리한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ATB",
    "ATC",
    "ATD"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ATC-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G306",
  "primary": [
    39
  ],
  "auxiliary": [
    17,
    45
  ],
  "surface": [
    31
  ],
  "decisive_operation": "객관/주관 측정의 입력 지표 수와 측정 방식 수를 같은 비교 축으로 맞추고 단위 교체를 배제한다.",
  "competing_codes": [
    {
      "code": 31,
      "rebuttal": "수의 비교라는 표면은 있지만 집합의 수와 원소 수라는 정확 구조로 억지 대응하지 않는다."
    },
    {
      "code": 45,
      "rebuttal": "측정 절차의 입력과 방식은 내용상 유효하며 전체 과업은 두 절차의 비교다."
    },
    {
      "code": 80,
      "rebuttal": "주관 귀속이 인식이라는 사실보다 두 측정 설계의 지표/방식 구별이 정답을 가른다."
    }
  ],
  "independence_limit": "G306 기존 소재 예시 사전 노출. 무노출 코드 성과 제외.",
  "confidence": 0.96,
  "sdss_seen": false
}
```
