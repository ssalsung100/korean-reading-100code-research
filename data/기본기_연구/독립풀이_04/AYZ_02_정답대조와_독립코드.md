

<!-- luna-raw:AYZ-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G356",
  "first_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "비트확장은상태공간·한번의처리기능을늘리지만클록으로정하는전환빈도자체증가는보장하지않는다.",
  "group_barrier": "전체blind저장후정답공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AYZ-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G356",
  "primary": [
    17,
    45
  ],
  "auxiliary": [
    43,
    84,
    86
  ],
  "surface": [
    91,
    46
  ],
  "decisive_operation": "작업완료속도와 상태전환빈도를 다른 출력변수로 두고 N의 영향과 클록의 영향을 분리한다.",
  "competing_codes": [
    {
      "code": 43,
      "rejection": "N만 바뀔 때 클록을 고정하는 반사실적 비교조건에 보조로 필요."
    },
    {
      "code": 84,
      "rejection": "작업시간은 전환횟수×간격 관점으로 복구 가능하나 수치분수계산은 요구안함."
    },
    {
      "code": 91,
      "rejection": "2의N제곱 상태수증가를 정비례라고 오인하지 않으며④는 함수형태보다 종속변수 교환 오류."
    },
    {
      "code": 46,
      "rejection": "N→기능다양성→작업시간의 인과는있지만 클록자체가 증가한다고 잇는 경로는없음."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.92,
  "quota_status": "unavailable"
}
```
