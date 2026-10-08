

<!-- luna-raw:ATA-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G305",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "유방암위험증가·대장암감소",
    "자궁내막암군간차이없음·골절감소",
    "체중혈압양호는관찰연구의교란요인이지치료효과아님"
  ],
  "minimal_logic_without_codes": "ⓐ는 확률 증가와 전원 발병을 구별하고 대장암 감소를 보존한다.ⓒ는 골절 위험 감소에 근거한다.ⓑ는 차이 없는 결과에서 금기를 도출하고ⓓ는 선택 편향을 치료 필요성으로 오독한다.",
  "intermediate_reasoning": [
    "ⓐ적합.ⓑ연구가해당암위험증가를보이지않음.ⓒ뼈관련이익가능성.ⓓ치료군의좋은건강상태가치료덕분이라는결론은관찰편향설명과반대."
  ],
  "attractive_wrong_answer": 4,
  "exact_error": "건강 위험이 있으니 치료가 필요하다는 외부 기대를 넣으면 본문이 제시한 부작용·선택 편향의 구별을 놓친다.",
  "scope_limit": "가상 상담 선지를 제시된 연구 결론에 대조한 것이며 실제 환자의 치료 권고나 금기 판단으로 확장하지 않는다.",
  "quota_status": "unavailable"
}
```
