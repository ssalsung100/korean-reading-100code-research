

<!-- luna-raw:BPI-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G499",
  "selected_answer": 2,
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
      "location": "기존 개발 방식과DMN 비교 문단",
      "evidence": "코드에 규칙이 혼재하면 가시성이 낮고 변경이 개발자에 의존한다. DMN은 의사결정 로직을 분리해 명시적으로 모델링하여 담당자가 유연하게 바꾼다."
    }
  ],
  "minimal_logic_without_codes": "②는 의사결정 로직을 애플리케이션과 분리하면 구현·유지보수가 쉬워진다는 효과를 재진술한다.",
  "intermediate_reasoning": [
    "① 전략적 의사결정은 규칙이 불명확해자동화가어렵다.",
    "③ 경곗값을 제외하는 구간 표현도본문에제시된다.",
    "④ BPMN태스크가DMN테이블을호출하지테이블조건안에태스크를포함하는방향이아니다.",
    "⑤ FEEL로규칙을작성·변경하는것과애플리케이션코드자체를수정하는것은다르다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "업무담당자가규칙을직접바꿀수있다는설명을개발자처럼애플리케이션코드를수정한다는뜻으로바꾼다."
  },
  "source_limit": "공통그림은아직미확인이나②와나머지선지의결정정보는본문정의에있다."
}
```
