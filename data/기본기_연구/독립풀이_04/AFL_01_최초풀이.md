

<!-- luna-raw:AFL-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "3문단 장기 환율=자국물가/외국물가;국내통화량증가유지시자국물가도높아져장기환율상승.",
    "4문단 단기실질통화량증가→금리하락→자금유출→추가환율상승;물가상승으로실질통화량원래수준복귀."
  ],
  "minimal_logic_without_codes": "장기에실질통화량이원래수준으로돌아와도자국물가수준은높아졌으므로장기균형환율은상승한다.①은실질통화량불변을환율불변으로잘못연결한다.",
  "intermediate_reasoning": [
    "② 물가가신축적이면통화량증가의실질통화량증가분을흡수하므로금리하락작음.",
    "③ 조정속도차이가오버슈팅원인이라고명시.",
    "④ 금리하락에더민감한자금유출은추가환율상승을키움.",
    "⑤ 물가경직성이클수록지속성이크므로균형수렴시간길어짐."
  ],
  "most_attractive_wrong_answer": 2,
  "exact_error": "명목통화량증가를실질통화량증가와동일시하면물가의신축성이금리변화폭에미치는차이를놓친다. 실질량의분모도변한다.",
  "quota_status": "unavailable"
}
```
