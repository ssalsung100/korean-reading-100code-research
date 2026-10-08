

<!-- luna-raw:BOB-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G487",
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
      "location": "협약의 한계 문단",
      "evidence": "면접교섭권 침해에는 전담기관의 지원이 가능하지만 그 구제를 위한 재판제도는 없다."
    },
    {
      "location": "보기·반환 예외 규칙",
      "evidence": "병10세, 양 본국 가입.1년 이상 체류와 적응이 결합된 예외, 위험이 있어도 보호조치와 반환 인용 가능."
    }
  ],
  "minimal_logic_without_codes": "면접교섭권 침해에도 기관 지원은 받을 수 있다. 재판제도가 없다는 한계를 지원 자체 불가능으로 바꾼④가 틀리다.",
  "intermediate_reasoning": [
    "① 제3국으로의 무단 이동에도 협약이 적용되며 Z국도 가입국이다.",
    "② 반환재판에서 양육권자 적합성 변경 주장은 판단할 수 없다.",
    "③ 3년이 지나도 생활에 적응하지 못하면 체류·적응의 결합 예외가 성립하지 않고 병은13세로16세 미만이므로 반환 가능하다.",
    "⑤ 중대한 위험이 있어도 자녀 보호조치를 명해 반환을 인용할 수 있다고 명시된다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "체류1년 이상과 생활 적응이라는 결합 요건에서 체류 기간만 충족하면 자동 반환 거절이라고 읽는다. 보기의 적응 실패를 누락한다."
  },
  "scope_limit": "예외가 인정되면 반드시 거절한다는 규칙을 추가하지 않으며 본문 가능성 표현을 유지한다."
}
```
