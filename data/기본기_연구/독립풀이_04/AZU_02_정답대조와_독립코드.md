

<!-- luna-raw:AZU-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G363",
  "first_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "공급원거리→Shh농도→역치충족→세포종류경로로ㄱㄷ참,ㄴㄹ거짓이다.",
  "group_barrier": "전체blind저장후정답공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AZU-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G363",
  "primary": [
    46,
    12
  ],
  "auxiliary": [
    49,
    86,
    43
  ],
  "surface": [
    54,
    45
  ],
  "decisive_operation": "척색의 제거·이동·Shh농도 변화가 전사인자와 분화에 미치는 순차경로를 역치 조건에 적용한다.",
  "competing_codes": [
    {
      "code": 49,
      "rejection": "거리-농도방향은한단계이며분화세포선택에는역치조건12가추가필요."
    },
    {
      "code": 43,
      "rejection": "실험에서다른외부공급이없다는제시모형조건을유지하나인과효과추정설계평가는아님."
    },
    {
      "code": 86,
      "rejection": "운동/사이신경역치순서비교는ㄹ보조.수치크기계산불필요."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.91,
  "quota_status": "unavailable"
}
```
