

<!-- luna-raw:AOP-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G267",
  "selected_answer": 1,
  "confidence": 0.98,
  "exposure": {
    "current_session": "blind-only,답·태그미열람",
    "historical": "unknown;기존참조0"
  },
  "required_information": [
    "1~2문단:광범한투자자에게리스크전가,신종증권을다양한투자자가보유."
  ],
  "minimal_logic_without_codes": "서브프라임 증권 보유는 일부 고수익 투자자에 한정되지 않고 광범위했다.①은 투자자 범위를 축소한다.",
  "intermediate_reasoning": [
    "①광범위보유와일부한정충돌",
    "②개별위험전가가과신·차입·연쇄위험으로연결",
    "③자금회수재대출로주택시장자금확대",
    "④유동화안전성과가격에대한과신이확대기여",
    "⑤원인이증권화/정부개입인지규명해야규제판단가능"
  ],
  "attractive_wrong_answer": 2,
  "exact_error": "개별기관이위험을전가했다는설명만보고전체위험도반드시낮아졌다고읽으면②를오판.연쇄연결과과도차입이라는추가경로가있음."
}
```
