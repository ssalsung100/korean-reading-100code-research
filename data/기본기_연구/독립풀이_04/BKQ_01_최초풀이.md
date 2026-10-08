

<!-- luna-raw:BKQ-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G458",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "2문단",
      "evidence": "개념은 공통 속성을 공유하는 개체의 집합이며 상속은 하위 개념과 상위 개념 사이의 관계다."
    },
    {
      "location": "1·4~5문단",
      "evidence": "지식 공유·재사용을 위한 형식적 명세.같은 의료 영역에서도 여러 목적의 온톨로지가 구축된다."
    }
  ],
  "minimal_logic_without_codes": "④는 상위 개념과 하위 개념 사이의 상속 관계를 개념과 소속 개체 사이에 옮긴다.두 관계의 항목 유형이 다르므로 부적절하다.",
  "intermediate_reasoning": [
    "① 공유·재사용 목적의 공학적 구조물이라는 정의에 부합한다.",
    "② 개념과 논리 관계의 명시적 명세이다.",
    "③ 형식적이라는 정의가 기계 처리 가능한 표현을 요구한다.",
    "⑤ 동일 의료 영역에서 NCI·UMLS·SNOMED-CT 등 목적에 맞는 온톨로지가 존재한다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "공유된 합의라는 정의를 한 분야에는 반드시 유일한 온톨로지만 존재한다는 제약으로 강화한다.본문은 여러 목적·그룹의 구축을 허용한다."
  },
  "source_restoration": {
    "appendix": "data/기본기_연구/prepared_backlog/blind_sources/BKQ-hold-source-20261003-appendix.md",
    "restored_term": "온톨로지",
    "resolved_before_answer_disclosure": true,
    "original_hold_preserved": true
  },
  "scope_limit": "문항이 지정한 class-instance와 class-class 관계의 구분이다.외부 온톨로지 구현의 모든 속성 전달 규칙을 단정하지 않는다."
}
```
