

<!-- luna-raw:BFQ-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G413",
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
      "location": "베이즈 정의 문단",
      "evidence": "증거의 힘=사후-사전, 신뢰도를 바꾸지 않는 증거 힘0"
    },
    {
      "location": "확률 범위·마지막 문단",
      "evidence": "확률0~1, 규범 이론에 대한 기술적 불일치 비판"
    }
  ],
  "minimal_logic_without_codes": "증거 힘0이 가능하면 사후=사전이 가능하다. 같을 수 없다는①을 배제한다.",
  "intermediate_inference": [
    "② 수치 순서 가능,③ 최대 상승폭은1-사전,④ 당위와 실제의 차이가 곧 규범 반증은 아니다.",
    "⑤의 부합을 긍정적으로 지지하는 증거로 읽으면 상승한다는 지문 설명에 맞지만, 단순 양립으로 읽으면 무정보 증거도 가능해 항상 상승이 보장되지 않는다."
  ],
  "attractive_wrong_answer": 5,
  "exact_error": "⑤는 부합을 단순 양립으로 엄격히 읽으면 문제이나, 문항은 지지 증거의 뜻으로 쓴 것으로 읽었다.①은 본문의0 정의와 직접 충돌한다.",
  "unresolved": "⑤ 부합=양립/확률상승 지지 구별 및 정답 유일성의 엄격한 한계"
}
```
