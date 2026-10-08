

<!-- luna-raw:BEP-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G404",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "2문단 유식하는 사람 다수·옛날 없던 의복음식 제도",
    "3문단 땅·가호 불변, 재해·전쟁 의외 지출 없음",
    "4문단 수입으로 반년 용도도 못 지탱"
  ],
  "minimal_logic_without_codes": "본문은 백성의 궁핍을 사치·과세 부담과 연결하며 재해로 인한 예외 지출은 없었다고 말한다. 잦은 천재지변을 원인으로 넣은②는 근거와 맞지 않는다.",
  "intermediate_reasoning": [
    "① 수입으로 반년 지출도 못 감당하므로 일치.",
    "② 재해·전쟁으로 인한 의외 지출이 없었던 것이 다행이라고 했으며 빈곤의 서술 원인은 과도한 지출과 과세다.",
    "③ 옛날에 없던 사치스러운 의복·음식이 생김.",
    "④ 유식하는 사람 다수.",
    "⑤ 땅이 더 열리지 않았다고 명시."
  ],
  "attractive_wrong": {
    "choice": 3,
    "exact_error": "본문이 유행이라는 단어를 직접 쓰지 않아도 새 의복·음식 제도가 퍼지는 것이 그 내용이다."
  },
  "scope": "재해 지출이 없었다는 문장을 모든 자연재해가 전혀 없었다는 보편 사실로 과강화하지 않는다."
}
```
