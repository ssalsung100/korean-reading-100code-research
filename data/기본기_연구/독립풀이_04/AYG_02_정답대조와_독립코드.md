

<!-- luna-raw:AYG-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G350",
  "first_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "완전최적과불완전상태의 차이는 불완전한 상태들 사이에서 충족개수와효율이 단조대응하지 않는다는 명제의 증거가 아니다.",
  "group_barrier": "해당group 전체blind raw 저장 후 정답만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AYG-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G350",
  "primary": [
    64,
    63
  ],
  "auxiliary": [
    43,
    75,
    2
  ],
  "surface": [
    86,
    31
  ],
  "decisive_operation": "검증하려는명제의범위는하나이상조건이이미깨진상태들사이의비교다.②는완전최적과불완전의차이를보여다른명제를검증하므로관련증거가아니다.",
  "competing_codes": [
    {
      "code": 43,
      "rejection": "이미결손인조건을공통전제로고정하는범위통제기능에유효하지만실험의효과크기식별은아님."
    },
    {
      "code": 10,
      "rejection": "전체조건충족의필요성확인과일부충족개수의효율관계는다른문제.②는전자의영역."
    },
    {
      "code": 75,
      "rejection": "학자별귀속을유지하나②의결정오류는실제제시증거가주장대상범위에서벗어난것."
    },
    {
      "code": 31,
      "rejection": "조건개수와조건집합이라는표상이있지만집합의수/원소수혼동은아님."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.9,
  "quota_status": "unavailable"
}
```
