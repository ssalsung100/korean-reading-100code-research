

<!-- luna-raw:BFX-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G415",
  "selected_answer": 4,
  "confidence": 0.95,
  "exposure": {
    "prior_exposure": "unknown",
    "official_answer_read": false,
    "sdss_read": false,
    "existing_case_analysis_read": false,
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "visual04/11 형질표",
      "evidence": "A+={3,6},B+={1,2,3,5,6,7},C+={3,4,8},D+={} "
    },
    {
      "location": "거리 산술평균 규칙·visual05~09",
      "evidence": "먼저 최소거리끼리 묶고 군간 거리를 재계산.이미지05~09를 순서상①~⑤로 대응"
    }
  ],
  "minimal_logic_without_codes": "거리 최소인 A,D를 먼저 묶고 재계산하면 그 묶음에 C가 먼저 결합,마지막 B가 결합한다.시각자료08의 구조를 선택한다.",
  "intermediate_inference": [
    "AD=2/8,AC=3/8,AB=4/8,BC=7/8,BD=6/8,CD=3/8.",
    "AD-C=(3/8+3/8)/2=3/8;AD-B=(4/8+6/8)/2=5/8;B-C=7/8.",
    "따라서((A,D),C),B의 이미지08.선지번호는 순서상④."
  ],
  "attractive_wrong_answer": 3,
  "exact_error": "③ 이미지07은 최초 A,D는 맞으나 재계산 뒤 더 먼 B를 C보다 먼저 묶는다.",
  "unresolved": "이미지에 원선지 번호가 없고 JSON choices가 같은 placeholder여서 visual05~09 순차대응으로④를 기록.구조답과 번호대응의 확신을 분리하며 사후 정답으로 소급 blind 승격하지 않음."
}
```
