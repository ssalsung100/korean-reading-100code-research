

<!-- luna-raw:ANF-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G254",
  "selected_answer": 1,
  "confidence": 0.94,
  "exposure": {
    "current_session": "blind source만 읽음; 공식답·태그 미열람",
    "historical": "manifest unknown; 저장소 참조0"
  },
  "required_information": [
    {
      "location": "1~3문단",
      "evidence": "압축은 예측 가능 단계·계획·협력업체·다부서 팀"
    },
    {
      "location": "4~5문단",
      "evidence": "경험은 불확실 시장·첨단 기술·직관·강력 리더"
    }
  ],
  "minimal_logic_without_codes": "두 전략 모두 개발 가속화를 지향하므로 허용 시간이 다르면 어느 전략을 골라야 하는지는 글이 제시하지 않는다. 선택 조건은 예측·계획 가능성, 시장·기술의 불확실성과 이를 수행할 인적 역량이다.",
  "intermediate_reasoning": [
    "①시간 단축은 공통 목적이고 허용 기간에 따른 분기는 없음",
    "②예측·계획 가능한 단계인지가 압축 수행과 연결",
    "③시장 불확실성은 경험 선택 조건",
    "④다부서 협력과 강력 리더·직관 등 수행 역량 요구",
    "⑤첨단 기술의 불확실성이 경험 선택과 연결"
  ],
  "attractive_wrong_answer": 4,
  "exact_error": "명시적으로 선택 조건이라고 부르지 않았더라도 성공 수행에 필요한 팀과 리더 역량을 고려할 수 있다. 반면 시간에 관한 설명은 두 전략 모두 빠르게 하려는 목표만 제공한다.",
  "limitation": "현실 경영에서 허용 시간을 고려할 수 없다는 뜻이 아니라 본문에서 두 전략의 선택 조건으로 도출할 근거가 없다는 판단."
}
```
