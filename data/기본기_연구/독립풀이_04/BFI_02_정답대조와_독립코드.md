

<!-- luna-raw:BFI-answer_check-20261002-r2-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G410",
  "all_group_blind_records_before_any_group_answer_check": true,
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "망사 교환의39→34·33→38.6과 정소 통과의34→33을 구간별로 구별.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BFI-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G410",
  "general_task": "구간별 현상과 기제 대응",
  "decisive_relation": "망사 열교환 구간과 정소 통과 냉각 구간 분리",
  "primary": [
    {
      "code": 46,
      "reason": "각 온도 변화가 어느 물체 사이의 열 전달로 일어나는지 추적한다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "같은 온도 하강이라도 위치·혈관·구간이 다르다."
    },
    {
      "code": 19,
      "reason": "역류 이론이 설명하지 못한 추가 냉각을 방열 가설이 보완한다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "숫자는 구간을 특정하지만 온도차를 계산하지 않아도④를 판정한다."
    }
  ],
  "competing_codes": [
    {
      "code": 3,
      "rejection": "변화 순서만으로는 망사 안팎의 기제 차이를 설명할 수 없다."
    },
    {
      "code": 91,
      "rejection": "표면적 비례는 열교환 효율 배경이며 온도 변화의 정비례를 계산하지 않는다."
    },
    {
      "code": 56,
      "rejection": "이론 범위 설명과 중첩하지만 이 문항은 개별 온도 변화의 원인 매핑이 직접 행동이다."
    }
  ],
  "confidence": 0.96,
  "sdss_disclosed": false
}
```
