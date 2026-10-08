

<!-- luna-raw:AXI-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "selected_answer": 2,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "미확정",
  "required_information_and_location": [
    "2문단: 이력 특성은 상변화 방향별 임계점 차이",
    "보기 ⓐ: 출산율에도 이력 특성 주장",
    "②: 저→고와 고→저의 지원 규모가 일치"
  ],
  "minimal_logic_without_codes": "이력 특성이라면 현재 조건 외 과거 상태가 필요하다. 서로 반대 방향의 전이 경계가 동일하다는 관측은 이력 구간이 있다는 주장을 반박한다.",
  "intermediate_reasoning": [
    "① 지원 감소에도 고출산 유지하는 관성은 이력과 양립한다.",
    "② 방향별 문턱 일치는 이력 특성의 핵심 차이를 없앤다.",
    "③ 요인 영향력 차이는 직전 상태에 따른 차이와 별개다.",
    "④ 수단별 효과 차이는 이력 여부를 판정하지 못한다.",
    "⑤ 급격한 변화는 전이에 부합하며 임계값 측정 곤란은 이력 부정이 아니다."
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "임계값을 수치화하지 못한 것과 경로 의존이 존재하지 않는 것을 혼동한다.",
  "passage_group": "G342",
  "quota_status": "unavailable"
}
```
