

<!-- luna-raw:BPU-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G503",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "2문단",
      "evidence": "역인과·누락 제3요인·측정오차가 있으면 관측 기울기가 원인 효과를 제대로 반영하지 못한다."
    },
    {
      "location": "3문단",
      "evidence": "발전된 제도와 소득의 양의 기울기만으로 제도의 효과를 뒷받침하지 못한다."
    }
  ],
  "minimal_logic_without_codes": "기울기가0이 아닌 관계는 다른 경로로도 발생하므로 그 사실만으로 원인 효과를 확정한④는 과도하다.",
  "intermediate_reasoning": [
    "① 포용적 제도를 발전시킨 지역이 빠르게 성장한다는 본문과 맞는다.",
    "② 과거 부유/현재 가난, 과거 가난/현재 부유의 반대 경향을 뜻하는 일상적 반비례라면 본문과 맞는다. 곱이 일정한 정확한 역비례 함수로 읽으면 본문은 입증하지 않는다.",
    "③ 부유했던 지역의 착취적 제도와 가난했던 지역의 포용적 제도 대비에 맞는다.",
    "⑤ 두 변수에 연관된 다른 요인이 있어 관측 관계만으로 직접 원인을 확정하지 못한다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "반비례를 엄밀한 y=k/x로 해석하면 지지되지 않으나, 본문은 부유 순위가 반대로 바뀌는 경향을 설명한다.④에는 이 해석 차이와 무관한 명시적 반증이 있다."
  },
  "scope_limit": "②의 반비례는 질적 반대 경향으로만 채택하고 수식 법칙으로 확대하지 않는다."
}
```
