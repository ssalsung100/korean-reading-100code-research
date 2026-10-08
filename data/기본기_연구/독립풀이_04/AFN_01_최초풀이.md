

<!-- luna-raw:AFN-blind-20260920-01 -->
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
    "보기 A금융불안→안전자산B채권수요→A자금B유출→A환율급등.",
    "B통화량증가로B금리변동예상→A환율급등진정.",
    "본문 통화량증가시단기금리하락→해당국투자기대수익하락·자금유출/유입위축."
  ],
  "minimal_logic_without_codes": "B의금리가하락하면B투자매력이낮아져A에서B로의자금유출압력이완화되므로A환율급등도진정되는방향이다.①의A오버슈팅더커짐은이경로와반대.",
  "intermediate_reasoning": [
    "② A의촉발원인은금융불안심리로보기와일치.",
    "③ 갑은시장조정으로균형환율수렴을기대.",
    "④ 수출증가의편익때문에시장개입자제를권고.",
    "⑤ A환율상승→수입가격상승→내수위축가능."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "현재환율급등이있다는사실만으로장기시장조정의가능성을부정하면갑의견해를왜곡한다. 단기괴리와장기수렴은양립한다.",
  "scope_limit": "본문과보기의두국가자금흐름만따르며실제투자·환율예측조언으로확장하지않음.",
  "quota_status": "unavailable"
}
```
