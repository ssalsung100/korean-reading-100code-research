

<!-- luna-raw:AOW-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G269",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "current_session": "blind-only본문·G269_visual01표만읽음;답·태그미열람",
    "historical": "unknown;기존참조0"
  },
  "required_information": [
    "1문단:특정생리각성→특정정서.실험:A/B같은에피네프린,C식염수."
  ],
  "minimal_logic_without_codes": "제임스의 이론을 적용하면 동일한 각성을 가진 A와 B는 사전정보·협력자 태도와 무관하게 같은 정서를 보여야 한다.",
  "intermediate_reasoning": [
    "①동일각성동일정서",
    "②A/C각성다른데동일행동동조예측은아님",
    "③B/C각성이다름",
    "④C맥락따른변화를예측하지않음",
    "⑤맥락만으로모든그룹동조아님"
  ],
  "attractive_wrong_answer": 3,
  "exact_error": "B/C의실제관측무반응을이론의예측으로복사하면안됨.이문항은실험결과아닌제임스가예측할결과를묻는다."
}
```
