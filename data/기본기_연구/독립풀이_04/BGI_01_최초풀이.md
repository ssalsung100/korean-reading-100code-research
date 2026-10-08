

<!-- luna-raw:BGI-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G419",
  "selected_answer": 1,
  "confidence": 0.97,
  "exposure": {
    "prior_exposure": "unknown",
    "official_answer_read": false,
    "sdss_read": false,
    "existing_case_analysis_read": false,
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "visual02 마지막",
      "evidence": "왕은각부서에장단점논의요구;53명중18~19찬성나머지반대"
    },
    {
      "location": "본문·보기 입장",
      "evidence": "조준은태조법준수개혁,이색은옛법경솔변경반대,윤소종은조준찬동"
    }
  ],
  "minimal_logic_without_codes": "왕이 논의를 명령했다는 사실과 다수의 반대를 왕의 최종 반대 결정으로 바꾼①은 확인되지 않는다.",
  "intermediate_inference": [
    "② 양쪽모두옛법명분,③ 반대자대갓집출신은기득권보전동기의문맥추론을지지한다.",
    "④ 상서후논의가전개된연결,⑤ 조준의원인진단을포함한의론에찬동한다는문맥으로읽는다.",
    "③의내적동기와⑤의세부신념이직접인용됐다고확정하지않는다."
  ],
  "attractive_wrong_answer": 5,
  "exact_error": "⑤는윤소종이찬동했다고한의론의내용을본문에서복원하는진술이다.왕은찬동/반대입장이전혀명시되지않아①의확정이더직접적으로불가하다.",
  "unresolved": "③동기·④인과적계기·⑤세부입장귀속은문맥적추론이며강한연역보장으로올리지않는다."
}
```
