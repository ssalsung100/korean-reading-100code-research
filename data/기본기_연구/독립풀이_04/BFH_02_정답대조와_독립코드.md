

<!-- luna-raw:BFH-answer_check-20261002-r2-01 -->
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
  "fixed_logic_without_codes": "역류 열전달은 지속되는 혈액 공급을 전제로 유입 혈액의 열을 낮추는 기제를 설명한다.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BFH-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G410",
  "general_task": "이론의 설명 범위 확인",
  "decisive_relation": "전제된 혈류의 존재와 설명 대상인 온도 유지의 구분",
  "primary": [
    {
      "code": 56,
      "reason": "이론이 무엇을 설명하는지 피설명항을 고정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "혈액 공급과 온도 조절이라는 대상 과정의 범위가 다르다."
    },
    {
      "code": 46,
      "reason": "망사 열전달의 국소 인과 기제를 복원한다."
    }
  ],
  "surface": [
    {
      "code": 10,
      "reason": "혈액 공급은 정상 기능의 필요 배경이지만 이론이 그 공급의 성립 기제를 설명한 것은 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 19,
      "rejection": "두 이론의 보완은 지문 전체 구조이며④의 오류는 설명 대상을 바꾼 것이다."
    },
    {
      "code": 50,
      "rejection": "혈류 차단이나 경로 중단 후 효과를 묻지 않는다."
    },
    {
      "code": 43,
      "rejection": "정답 판정에 실험 통제 비교가 필요하지 않다."
    }
  ],
  "confidence": 0.96,
  "sdss_disclosed": false
}
```
