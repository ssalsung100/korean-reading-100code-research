

<!-- luna-raw:BPM-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G500",
  "selected_answer": 3,
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
      "location": "스볼릭·루오와쉐보르스키 비교",
      "evidence": "첫 모델은 정책 이념 효용과 민주주의 훼손 손실, 두번째는 현재 후보의 매력과 미래 교체 능력의 효용을 비교한다."
    }
  ],
  "minimal_logic_without_codes": "③은 각 모델에서 유권자가 비교하는 두 효용을 정확히 구분하여 대응한다.",
  "intermediate_reasoning": [
    "① 두번째 모델은 미래 도전자와 교체 능력을 명시적으로 고려한다.",
    "② 두 모델의 퇴행이 심해지는 조건을 유사성으로 단순화할 수 없다. 두번째는 집권자 매력의 양극단을 설명한다.",
    "④ 두번째가 과거·미래 프리미엄의 차이를 최적화한다는 계산식은 없다.",
    "⑤ 두번째에서 높은 매력으로 조작을 용인받는 주체는 집권자이지 도전자가 아니다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "첫 모델의 득표-감표 차이라는 명시 비교를 두번째에도 같은 형식으로 복제하면서 원문에 없는 프리미엄 차이 계산을 추가한다."
  }
}
```
