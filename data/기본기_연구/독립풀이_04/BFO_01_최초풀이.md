

<!-- luna-raw:BFO-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G412",
  "selected_answer": 3,
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
      "location": "마지막 두 문단",
      "evidence": "언론 노력은 법원 인식을 확대했으나 소송 결과에는 영향 없음; 파수견 역할 인정; 진실 보도 강조"
    }
  ],
  "minimal_logic_without_codes": "파수견 역할 인정과 개별 소송 면책은 별개다. ㄱ·ㄹ은 거짓,ㄴ·ㄷ·ㅁ은 참이다.",
  "intermediate_inference": [
    "ㄱ은 인식 변화의 성과를 판결 결과 변화로 옮긴다.",
    "ㄹ은 면책 불허를 파수견 기능 자체 부인으로 바꾼다.",
    "ㄴ 불리한 법 적용 대응,ㄷ 복잡성 수용 요구,ㅁ 진실 보도 요건은 각각 근거가 있다."
  ],
  "attractive_wrong_answer": 5,
  "exact_error": "⑤는 ㄹ을 포함한다. 법원은 파수견 기능을 인정하면서도 진실성을 요구했으므로 면책 불허가 역할 부인이 아니다.",
  "source_quality_note": "visual01은 BFO 보기,visual02는 BFP 사례. 반복 placeholder 번호를 실제 내용으로 대조함."
}
```
