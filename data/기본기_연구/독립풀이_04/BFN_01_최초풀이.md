

<!-- luna-raw:BFN-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G412",
  "selected_answer": 5,
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
      "location": "1문단",
      "evidence": "파수견은 개인이 아니라 언론기관의 제도적 표현 자유이며 국민 알 권리의 필수조건"
    },
    {
      "location": "2문단",
      "evidence": "국가접근권/국가견제/상업폐해에도 보호"
    }
  ],
  "minimal_logic_without_codes": "국민 알 권리를 위한 기관의 자유를 개인 표현 자유의 전제로 바꾼⑤는 본문의 권리 주체·목적 대응을 벗어난다.",
  "intermediate_inference": [
    "① 접근권은 기능 강화,② 국가 견제,③ 알 권리,④ 상업폐해보다 국가남용 위험 크다는 근거가 있다.",
    "개인 자유와 기관 자유가 전혀 양립 불가라는 뜻은 아니며,⑤의 필수 전제 관계가 본문에 주어지지 않았다."
  ],
  "attractive_wrong_answer": 4,
  "exact_error": "④의 상업폐해를 보호 배제 사유로 오독하면 안 된다. 본문은 폐해에도 보호해야 한다고 한다.",
  "source_quality_note": "visual01은 BFO 보기,visual02는 BFP 사례. 반복 placeholder 번호를 실제 내용으로 대조함."
}
```
