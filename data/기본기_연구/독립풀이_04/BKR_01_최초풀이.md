

<!-- luna-raw:BKR-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G458",
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
      "location": "2문단",
      "evidence": "하위 개념이 상위 개념의 모든 속성을 상속한다."
    },
    {
      "location": "3문단",
      "evidence": "OWL Lite⊂DL⊂Full로 표현력 확장,DL까지 계산학적 완전성·결정 가능성 보장."
    }
  ],
  "minimal_logic_without_codes": "ㄱ은 한 온톨로지를 공통으로 표현 가능하다고 언어 전체 표현력이 같을 필요는 없어 거짓.ㄴ의 모든 빵은 장미는 빵이 하위·장미가 상위인데 뒤집어 거짓.ㄷ은 계산 보장보다 최대 표현력을 원하면Full을 선택하므로 참.따라서③.",
  "intermediate_reasoning": [
    "ㄱ 반모형:Lite가 표현하는 단순 온톨로지는 그 확장인Full로도 표현 가능하지만 두 언어의 전체 표현력은 다르다.",
    "ㄴ 모든 x에 대해 빵(x)→장미(x)이므로 빵 개체 집합이 장미 집합에 포함된다.실제 식물·음식 상식으로 명제를 평가하지 않는다.",
    "ㄷ DL까지 보장된다는 것과 Full의 모든 추론이 실패한다는 것은 다르다.선지는 보장 없이 표현력을 최대화하는 선택이다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "ㄴ에서 조건문의 앞에 나오는 빵을 상위 개념으로 착각한다.충분조건인 빵이 더 좁은 집합이다."
  }
}
```
