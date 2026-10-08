

<!-- luna-raw:AYY-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G356",
  "first_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "내부 피드백은 상태보존,외부 피드백은 현재상태와외부입력에따른다음상태생성이다.",
  "group_barrier": "전체blind저장후정답공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AYY-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G356",
  "primary": [
    45,
    39
  ],
  "auxiliary": [
    5,
    42,
    12
  ],
  "surface": [
    40,
    46
  ],
  "decisive_operation": "동일한 피드백 구조에서 내부루프의 상태유지와 외부루프의 상태변경을 입력·스위치·출력 경로별로 비교한다.",
  "competing_codes": [
    {
      "code": 5,
      "rejection": "유지와변경이기능차이지만 그 단어만으로 어느루프인지 알 수 없어 경로를 추적해야 한다."
    },
    {
      "code": 42,
      "rejection": "점선안팎의위치는루프 구분에보조. 내부/외부 자체가기능을보장하지않음."
    },
    {
      "code": 40,
      "rejection": "한전체의부분들이지만 부분전체 성질전이를 다루지 않는다."
    },
    {
      "code": 49,
      "rejection": "값이반전되지만 일반 증감방향이아닌 이진함수변환이다."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.92,
  "quota_status": "unavailable"
}
```
