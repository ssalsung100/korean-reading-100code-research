

<!-- luna-raw:BFF-answer_check-20261002-r2-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G409",
  "all_group_blind_records_before_any_group_answer_check": true,
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "선거 후 단순3·이항3, 의회 지수25/9. 따라서 이항 정당수>의회 지수.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BFF-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G409",
  "general_task": "세 산정방식의 적용·비교",
  "decisive_relation": "동일 사례의 단순 개수·참여조건 개수·비율제곱 역수 구분",
  "primary": [
    {
      "code": 92,
      "reason": "의회 지수1/(.4²+.4²+.2²)=25/9를 구해 이항3과 비교한다."
    }
  ],
  "auxiliary": [
    {
      "code": 15,
      "reason": "단순·이항의 포함 기준이 서로 다르다."
    },
    {
      "code": 86,
      "reason": "실제 정당수와 가중 지수의 크기를 비교한다."
    }
  ],
  "surface": [
    {
      "code": 31,
      "reason": "원소수/집합수 자체를 혼동한 문제가 아니라 개수와 비율 가중 지수의 구별이다."
    }
  ],
  "competing_codes": [
    {
      "code": 84,
      "rejection": "분수식을 포함하지만 핵심은 여러 비율 제곱합의 계산과 방식별 산정이다.92의 특수 표현과 중첩 가능."
    },
    {
      "code": 85,
      "rejection": "총 득표율의 합 제약은④ 검증 보조이나 정답③에 비율 변화의 경쟁 효과를 추론할 필요가 없다."
    },
    {
      "code": 90,
      "rejection": "정당 조합수·확률을 계산하지 않는다."
    }
  ],
  "confidence": 0.96,
  "sdss_disclosed": false
}
```
