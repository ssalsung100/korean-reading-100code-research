

<!-- luna-raw:BFJ-answer_check-20261002-r2-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G410",
  "all_group_blind_records_before_any_group_answer_check": true,
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "세 비교 모두 생산·위치 차이에 따른 정낭 표면 온도라는 가설의 예측을 시험한다.",
  "unresolved": "외기·연령 관련 다른 변수의 통제가 명시되지 않아 유일한 인과 입증으로 확대하지 않음.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BFJ-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G410",
  "general_task": "가설 검증에 관련된 실험 선택",
  "decisive_relation": "생산 열·정소 위치 차이에서 정낭 표면 온도 예측으로 연결",
  "primary": [
    {
      "code": 63,
      "reason": "어떤 비교 관찰이 가설의 예측을 지지·반박할 정보를 줄 수 있는지 판단한다."
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "생산→열→표면 전도·방출→표면 온도 경로를 복원한다."
    },
    {
      "code": 43,
      "reason": "외기·체격·대사 등 다른 변수를 통제해야 실제 인과 지지력을 평가할 수 있다."
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "동면·계절 전후가 비교 형식이지만 단순 시간 순서만으로 원인을 식별하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 74,
      "rejection": "75와 통합된 경쟁군이지만 여기서는 두 가설의 상반 예측 중 하나를 고르지 않고 한 가설의 검증 관련성을 판정한다."
    },
    {
      "code": 53,
      "rejection": "관찰 차이와 원인 차이 연결에 필요하나 통제 부재 상태에서 차이만으로 원인을 확정하지 않는다."
    },
    {
      "code": 36,
      "rejection": "아직 관찰 결과가 제시되지 않아 확정 반례를 고르는 단계가 아니다."
    }
  ],
  "confidence": 0.94,
  "sdss_disclosed": false
}
```
