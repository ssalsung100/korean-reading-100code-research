

<!-- luna-raw:AGD-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "공식[A]첫문단전체:방충망수선의무주체,계약과법률우선순위,법적불이익질문.",
    "2문단수선의무는임의법규,달리계약하면계약우선·달리정하지않으면법률적용."
  ],
  "minimal_logic_without_codes": "계약에수선내용없으면법률상건물주의무이고침묵의불이익없다(ㄱ). 세입자수선약정이있으면계약대로세입자의무이며달리약정한불이익없다(ㄷ). 따라서②.",
  "intermediate_reasoning": [
    "ㄴ은계약침묵시에법률의임대인의무를세입자에게옮기고불이익도추가.",
    "ㄹ은세입자수선약정의효력은맞지만달리정한것을벌하는단속규정효과를임의규정에옮김.",
    "누가수선하는가와달리정한것에불이익있는가는별개의판정항목."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "ㄹ앞절의세입자의무만맞는것을보고불이익있다는뒷절도함께승인하면오류.",
  "visual_verification": "AGD_A_range_official_crop_20260920.png의[A]괄호상하단과첫끝직접확인. 최초marker누락hold보존.",
  "quota_status": "unavailable"
}
```
