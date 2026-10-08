

<!-- luna-raw:ATS-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G311",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "해당 조항의 체계적 적용 범위 확정과 모든 법적 규율의 부재를 구별한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ATQ",
    "ATR",
    "ATS"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ATS-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G311",
  "primary": [
    10
  ],
  "auxiliary": [
    17,
    60,
    24
  ],
  "surface": [
    79
  ],
  "decisive_operation": "체계적 해석으로 특정 조항의 적용 요건을 확정하고 그 요건에 들지 않는 대상에 대한 적용 제외를 설명한다.",
  "competing_codes": [
    {
      "code": 17,
      "rebuttal": "특정 조항/법체계 전체의 범위 구별은② 배제의 핵심이며10과 다른 선택 경로다."
    },
    {
      "code": 24,
      "rebuttal": "다른 일반 규정의 적용 가능성은 특별규정의 예외를 새로 만든다는 뜻은 아니며 적용 규범의 범위를 구별한다."
    },
    {
      "code": 79,
      "rebuttal": "법 규범이 소재이지만 개인 행위의 당위보다 조항 해석과 적용 요건의 범위를 묻는다."
    }
  ],
  "boundary_note": "현행법 전반의 처벌 여부를 판단하지 않고 지문에 제시된 결정의 논리를 복원한다.",
  "confidence": 0.97,
  "sdss_seen": false
}
```
