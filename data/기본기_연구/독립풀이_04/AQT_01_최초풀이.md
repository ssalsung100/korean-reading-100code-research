

<!-- luna-raw:AQT-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G286",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "2문단 변경설: 관습법은 법률 배제 가능",
    "3~4문단 보충설: 법률 없는 사항에 관습법 적용",
    "끝문단 어느 편이든 관습법 확인과 판결의 관련성"
  ],
  "minimal_logic_without_codes": "두 견해 모두 관습법의 법적 효력을 인정하고 법원이 그 존재를 고려한다. 충돌 시 법률을 배제할 수 있는지는 다르다.",
  "intermediate_reasoning": [
    "① 변경설은 법률 뒤의 법적 확신을 근거로 배제를 허용하므로 우선 원칙 불적용에 둘 다 동의한다고 못한다.",
    "② 법적 확신 부족을 법률 규정 부재와 동일시하면 보충설을 왜곡한다.",
    "③ 효력 범위에는 차이가 있지만 관습법 존재의 고려는 공통이다.",
    "④는 보충설,⑤는 변경설에 가까우며 공통이 아니다."
  ],
  "attractive_wrong_answer": 2,
  "exact_error": "법적 확신이 없는 법률과 법률 규정이 없는 경우를 혼동하여 공백의 의미를 바꾼다.",
  "quota_status": "unavailable"
}
```
