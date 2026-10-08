

<!-- luna-raw:BGK-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G420",
  "selected_answer": 4,
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
      "location": "2문단마지막",
      "evidence": "주제영역과텍스트양식사이에필연적1대1대응없음"
    },
    {
      "location": "세장르설명",
      "evidence": "객관성장르도개성은드러날수있지만저자개인이직접등장하지않음"
    }
  ],
  "minimal_logic_without_codes": "주제와 표현양식은 다른 축이며, 개성 드러남과 저자 자신이 나로 등장함도 다르다.ㄱㄷ참,ㄴ거짓.",
  "intermediate_inference": [
    "ⓐⓑ도간주관성을주제로가능하므로ㄱ참.",
    "ⓐ는저자직접등장이없으므로ⓐⓒ둘다가능하다는ㄴ거짓.",
    "ⓑⓒ는사유·발화주체를통해개성이드러날수있음."
  ],
  "attractive_wrong_answer": 3,
  "exact_error": "③은ㄴ을포함한다.ⓐ에서문체상개성이드러난다는설명을저자자신의전면등장으로바꾼다.",
  "unresolved": null
}
```
