

<!-- luna-raw:BFP-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G412",
  "selected_answer": 1,
  "confidence": 0.98,
  "exposure": {
    "prior_exposure": "unknown",
    "official_answer_read": false,
    "sdss_read": false,
    "existing_case_analysis_read": false,
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "2문단 전통시각",
      "evidence": "규제 최소, 공익 보도라면 명예훼손 성립 불가까지 주장"
    },
    {
      "location": "visual02",
      "evidence": "S신문사는 공무원 비리를 취재해 공익 보도했다고 항변"
    }
  ],
  "minimal_logic_without_codes": "공익적 권력 감시 보도에 넓은 보호를 주는 입장을 사례에 적용하면 면책 요건을 넓게 읽는①이 맞다.",
  "intermediate_inference": [
    "㉠은 글리슨 시대 법원 견해가 아니라 전통적 시각이다.",
    "② 불가피한 경우 제한,④ 장기 연재 제한,⑤ 대상에 따른 차등은 제시되지 않는다.",
    "③은 일반적 제소 가능성에 관한 상식으로 읽지 않고 발문이 요구한 공익 보도에 대한 보호 입장의 지지 여부로 판단한다."
  ],
  "attractive_wrong_answer": 3,
  "exact_error": "③은 법원에 소를 제기할 현실적 권리와 본문 입장이 공익 보도의 명예훼손 성립을 인정하는지를 섞기 쉽다. 본문은 공익 보도를 넓게 보호한다.",
  "source_quality_note": "visual01은 BFO 보기,visual02는 BFP 사례. 반복 placeholder 번호를 실제 내용으로 대조함."
}
```
