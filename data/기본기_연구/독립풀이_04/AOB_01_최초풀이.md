

<!-- luna-raw:AOB-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G262",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "current_session": "blind-only,답·태그미열람",
    "historical": "unknown;기존노출참조0"
  },
  "required_information": [
    "2문단:상전 모해 규정은 없으나 모반/모반대역 두 조문 비교."
  ],
  "minimal_logic_without_codes": "직접 해당 조문이 없어 유사한 범죄 유형의 조문을 끌어와 죄명·형량을 정하므로①의 유추 적용 원칙이 필요하다.",
  "intermediate_reasoning": [
    "①실제절차와대응",
    "②새법제정없음",
    "③과거특별판례의원용문제없음",
    "④조문없이처벌아니고적용조문선택",
    "⑤하나의행위에두죄모두성립한전제아님"
  ],
  "attractive_wrong_answer": 5,
  "exact_error": "두조문을비교했다는사실을두죄가모두성립했다는사실로바꾸면안됨.쟁점은어느조문을적용할지이다."
}
```
