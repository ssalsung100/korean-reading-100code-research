

<!-- luna-raw:BFU-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G414",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "prior_exposure": "unknown",
    "official_answer_read": false,
    "sdss_read": false,
    "existing_case_analysis_read": false,
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "마지막 용률조",
      "evidence": "일반은 대명률, 경국대전/속대전에 해당 규정 있으면 두 국전 우선"
    },
    {
      "location": "2문단",
      "evidence": "관찰사 직접 사형 불가, 부모 고발 국전 사형 규정"
    }
  ],
  "minimal_logic_without_codes": "국전 관련규정이 있으면 국전,없으면 대명률을 적용하며 관찰사의 사형 선고 제한은 별도 절차다. ㄱㄴ 참,ㄷㄹ 거짓.",
  "intermediate_inference": [
    "ㄱ 국전 우선과 절차 제한이 함께 성립한다.",
    "ㄴ 부모 고발 국전규정 우선,ㄷ 속대전규정이 있는데 대명률을 우선하여 오류.",
    "ㄹ 국전에 없다고 처벌불가가 되지 않는다.대명률은 신분 차등을 갖는 법으로 양반을 통째로 제외하지 않는다."
  ],
  "attractive_wrong_answer": 4,
  "exact_error": "④의 ㄹ은 보충 적용할 대명률이 있음을 무시하고 국전 부재를 처벌근거 전무로 바꾼다.",
  "unresolved": null
}
```
