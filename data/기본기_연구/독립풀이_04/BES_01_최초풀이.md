

<!-- luna-raw:BES-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G405",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "2문단 충돌 전 해양 지각 섭입·고압 변성",
    "2문단 충돌 후 대륙 지각 고압 변성",
    "4·5문단 산둥·홍성 산출"
  ],
  "minimal_logic_without_codes": "에클로자이트는 충돌 전 섭입된 해양 지각에서도 이미 만들어진다. 충돌 후에야 처음 생성된다는④는 앞선 생성 경로를 지운다.",
  "intermediate_reasoning": [
    "①③ 고압을 받은 현무암질 화성암 변성이라고 명시.",
    "② 다비-수루와 홍성에서 발견.",
    "④ 충돌 전에 해양 지각 섭입 단계에서 이미 생성되므로 틀림.",
    "⑤ 본문은 충돌대 에클로자이트를 이전 해양의 증거로 해석한다."
  ],
  "attractive_wrong": {
    "choice": 5,
    "exact_error": "충돌 후 대륙 지각에서 생성되는 경로만 보고 앞서 해양이 존재했다는 전체 과정 설명을 빠뜨린다."
  }
}
```
