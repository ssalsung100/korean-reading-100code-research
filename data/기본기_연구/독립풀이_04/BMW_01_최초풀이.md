

<!-- luna-raw:BMW-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G477",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "2~4문단",
      "evidence": "해당작용은 포도당1개당 ATP2개·NADH2개. NADH1개를 산화적 인산화하면 ATP3개. 완전 전환 총ATP36 또는38개."
    }
  ],
  "minimal_logic_without_codes": "⑤의 비교값은 해당작용의 ATP2개와 NADH2개로 같으므로 전자가 더 많다는 주장이 틀리다.",
  "intermediate_reasoning": [
    "① 본문에서 NADH의 ATP 전환은 미토콘드리아의 산화적 인산화 경로다.",
    "② 유산소 해당작용의 암세포는 산소가 있어도 발효를 통해NAD+와젖산을 만든다.",
    "③ 미토콘드리아 몫은 전체36/38에서 세포질2를 뺀34/36이다.",
    "④ 해당작용 직접ATP2와 생성NADH2×3을 합하면8이다. 나머지 피루브산의 완전 산화까지 추가하지 않는다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "포도당 전체의 이론적 최종수율36/38을 이 부분 과정에 가져오거나,해당작용 직접ATP2를 빼먹어 총량 범위를 혼동한다."
  },
  "scope_limit": "수치와 생산 단계는 지문에 주어진 모형을 그대로 사용한다. 현대 교과서의 다른 수율값을 외부에서 대체하지 않는다."
}
```
