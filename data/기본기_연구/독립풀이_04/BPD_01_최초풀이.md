

<!-- luna-raw:BPD-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G497",
  "selected_answer": 4,
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
      "location": "세 모델 설명",
      "evidence": "심포니는 악보의 절대성을, 시네마는 시나리오를 토대로 현장에 따라 수정함을, 조각은 과정 중 새 영감과 애초 구상을 비교해 선택함을 강조한다."
    }
  ],
  "minimal_logic_without_codes": "조각 모델은 제작 도중의 영감에 따라 초기 구상과 희곡을 바꿀 수 있다. 작가의 말을 확고한 지침으로 고정한④는 심포니식 절대성을 옮긴다.",
  "intermediate_reasoning": [
    "① 심포니 모델은 지시문의 권위가 연기를 제약한다.",
    "② 시네마 모델은 대본을 골격으로 다른 구성 요소와 조율한다.",
    "③ 극장 규모 같은 현장 여건에 맞게 각색할 수 있다.",
    "⑤ 작업 중 생긴 배우의 몸짓이라는 영감도 초기 구상과 비교해 활용 가능하다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "시나리오를 골격으로 삼는다는 것을 수정할 수 없는 최종 지침으로 읽으면 현장 여건에 따른 각색을 배제한다."
  }
}
```
