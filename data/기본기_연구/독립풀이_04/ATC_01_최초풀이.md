

<!-- luna-raw:ATC-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G306",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": true,
    "strict_blind_eligible": false,
    "prior_exposure_detail": "핵심8코드 기준문서의 중산층 점수표 예시 사전 노출; 같은 묶음 전체에 보수적으로 적용.",
    "supplement_seen": "G306_visual01.md"
  },
  "needed_information_locations": [
    "객관:직업·소득·자산·교육합산",
    "주관:계층귀속의식하나를중산층/중간층두방식",
    "개인마다잣대다름·두차원결합시불일치포착"
  ],
  "minimal_logic_without_codes": "객관 측정은 여러 지표를 하나의 합산 방식으로,주관 측정은 귀속 의식이라는 지표를 두 질문 방식으로 측정하므로⑤다.",
  "intermediate_reasoning": [
    "①주관적단계는상층포함.②둘다개인위치판별.③불일치는두차원결합해야포착.④주관잣대는개인마다다름.⑤지표수와방식수구별."
  ],
  "attractive_wrong_answer": 2,
  "exact_error": "가구 소득이라는 입력 지표의 단위와 최종 분류 대상인 개인의 단위를 혼동한다.",
  "quota_status": "unavailable"
}
```
