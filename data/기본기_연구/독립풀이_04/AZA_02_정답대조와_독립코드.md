

<!-- luna-raw:AZA-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G357",
  "first_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "약정없어도경업금지의무가있는영업양도가약정필요성의반례다.",
  "group_barrier": "전체blind저장후정답공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AZA-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G357",
  "primary": [
    10,
    36
  ],
  "auxiliary": [
    24,
    2
  ],
  "surface": [
    79,
    12
  ],
  "decisive_operation": "합법적 경업제한→약정존재라는 필요조건을 무약정 영업양도 사례로 반증한다.",
  "competing_codes": [
    {
      "code": 24,
      "rejection": "예외의 존재로 일반명제를 배제하는 동작이36과 중첩;단순히 예외라는 어휘만으로 핵심을 설명하지 않음."
    },
    {
      "code": 12,
      "rejection": "조건문으로 동일관계를 표현하지만 필요요건이라고 주장된 약정의 부재가 핵심."
    },
    {
      "code": 2,
      "rejection": "④가능과보장 구별에 보조.②의직접오류는필요조건누락가능성을 부정함."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.92,
  "quota_status": "unavailable"
}
```
