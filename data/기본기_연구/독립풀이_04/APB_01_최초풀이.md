

<!-- luna-raw:APB-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G271",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "current_session": "blind본문·visual01~05만열람;답·태그미열람",
    "historical": "unknown;기존참조0"
  },
  "required_information": [
    "(가):탈출/생화학변화→높이소실→불안정/골극→추간공좁아짐→신경근증.탈출의직접경로별도."
  ],
  "minimal_logic_without_codes": "직접 신경근증으로도 이어지는 B는 탈출,다른 시작 A는 변성이다.높이 소실 이후 C는 골극,그 다음 D는 추간공 협착이다.",
  "intermediate_reasoning": [
    "B의우회경로가탈출식별",
    "A는생화학변화인변성",
    "C는골극성장",
    "D는골극등으로좁아진추간공",
    "②가네자리모두일치"
  ],
  "attractive_wrong_answer": 1,
  "exact_error": "①은골극과협착순서를거꾸로하여원인인성장과결과인좁아짐을교환.",
  "source_quality_note": "blind PNG는글자없는도형조각으로확인됨.노드표기는blind본문문자도식과선지표에의존했고PNG로분기·합류·직접우회화살표확인.별도공식페이지링크는blind단계열람안함."
}
```
