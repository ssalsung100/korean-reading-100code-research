

<!-- luna-raw:BFW-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G415",
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
      "location": "분기론 문단·표1·visual10",
      "evidence": "-원시,+파생;둘 이상 공통인 파생만 묶음에 사용;표B만2+,B/C는3+"
    }
  ],
  "minimal_logic_without_codes": "같다고 모두 묶는 것이 아니라 공통이면서 파생이어야 한다.ㄱ의 공유 원시는 제외,ㄴ 자가파생·ㄷ 공유파생·ㄹ 최소 사건수 원칙은 맞다.",
  "intermediate_inference": [
    "1,4,5의 A/B 공통-는 원시이므로ㄱ 거짓.",
    "2는B만+이므로 자가파생이며 이것이 묶음에 쓰인다는 뜻은 아니다.",
    "3은B,C 공통+이므로 이들을 묶는다.",
    "최대 단순성으로 변화 사건이 적은 계통수를 택한다."
  ],
  "attractive_wrong_answer": 4,
  "exact_error": "④의 ㄱ은 공통성만 확인하고 파생성 조건을 누락한다.",
  "unresolved": null
}
```
