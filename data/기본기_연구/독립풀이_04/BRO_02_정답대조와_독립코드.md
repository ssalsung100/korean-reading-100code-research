

<!-- luna-raw:BRO-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G521",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2009/2009_answer/table_001.md Q8~10; 공식 HWP 추출 표 및 candidate canonical_connection 공식답 필드 일치",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "자격증의 낮은 주류 인정도를 취업 용이성으로 바꾼③이 틀리다.교육이 사업 능력에 도움되는 것과 주류 취업 자격 인정은 구별한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BRO-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G521",
  "sdss_seen": false,
  "primary": [
    {
      "code": 46,
      "reason": "학력·자격증 인정의 부족이 선호 직업 접근을 막는 방향을 취업 용이성으로 뒤집은③을 판정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 15,
      "reason": "영어가 다른 집단보다 높은 것과 주류 취업 기준 충족을 구별한다."
    },
    {
      "code": 39,
      "reason": "교육의 취업 효과와 사업 역량 효과를 구별한다."
    }
  ],
  "surface": [
    {
      "code": 86,
      "reason": "자영업 비중70%나 상대 교육수준은 있으나 정답에서 수치 계산을 하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 43,
      "rejection": "교육수준과 직업의 비교가 있지만 통제된 인과실험으로 효과를 식별하지 않는다."
    },
    {
      "code": 19,
      "rejection": "자원이 사업을 돕는 구조는 있지만③은 부족 보완보다 주어진 원인 방향의 반전이다."
    },
    {
      "code": 53,
      "rejection": "집단 간 차이가 언급돼도 차이만으로 다른 차이를 추론하는 논증은 요구되지 않는다."
    }
  ],
  "confidence": 0.94
}
```
