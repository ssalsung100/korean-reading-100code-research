

<!-- luna-raw:BFS-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G413",
  "selected_answer": 2,
  "confidence": 0.88,
  "exposure": {
    "prior_exposure": "unknown",
    "official_answer_read": false,
    "sdss_read": false,
    "existing_case_analysis_read": false,
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "visual01",
      "evidence": "(가)는 왼손 지지,(나)는 오른손 지지, 둘 고려 후 A 확신 증가,(다)는 도움없음"
    },
    {
      "location": "증거 힘 정의",
      "evidence": "사후-사전"
    }
  ],
  "minimal_logic_without_codes": "긍정 증거와 부정 증거를 고려한 순변화가 양수이고 무정보 증거의 변화가0이므로 전체 순증가는 양수다. 이를②의 합으로 읽는다.",
  "intermediate_inference": [
    "(나)는 A를 낮추므로③ 거짓, (다)는0이므로⑤ 거짓.",
    "(나)+(다)만 반영하면 감소하여④ 거짓.",
    "①은 나가 더 크다는 서술로 전체 확신 증가와 맞지 않는다. 단 가/나의 독립적 증거 힘을 공통 사전에서 각각 측정했다면 단순 합성은 본문 정의만으로 보장되지 않는다."
  ],
  "attractive_wrong_answer": 4,
  "exact_error": "④는(다)가 중립이라는 사실로(나)의 부정적 기여까지 지워 버린다.",
  "unresolved": "②의 합이 연속 갱신의 증분 합인지 공통 사전에서 따로 평가한 값 합인지 명시되지 않음. 전자로 읽어 선택."
}
```
