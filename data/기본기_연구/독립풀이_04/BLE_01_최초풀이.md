

<!-- luna-raw:BLE-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G462",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "㉠",
      "evidence": "생명체의필수작업을직접수행하는물질은단백질이라는주장."
    },
    {
      "location": "㉡",
      "evidence": "암세포에서양이증가/감소한단백질을발암/암억제후보로분류."
    },
    {
      "location": "㉢",
      "evidence": "펩타이드분자량분석으로원단백질을알아내는식별방법."
    }
  ],
  "minimal_logic_without_codes": "단백질없는생명체는필수작업주체의단백질한정을약화한다.양증가가비활성화로이어지는경우는양을기능증가의지표로읽는추론을약화한다.다른단백질의펩타이드질량중복은식별력을높이지않으므로ㄷ은거짓.ㄱㄴ만맞아③.",
  "intermediate_reasoning": [
    "ㄱ은생명체라면필수작업이이뤄져야한다는문맥에서단백질없이그것이가능한가를묻는반례다.외부RNA세계의실제존재를확정하지않는다.",
    "ㄴ은단백질의양과작용활성이항상같은방향이라는잠재연결을차단한다.후보전체가무효라는전면반증으로확대하지않는다.",
    "ㄷ은한펩타이드질량의공통성이식별증거의특이성을낮출수있다는것이다.나머지펩타이드조합으로식별가능성이남을수있으므로전체방법불가능까지단정하지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "같은분자량데이터가반복되면항상측정신뢰도가높아진다고읽고,서로다른원단백질을구별하는특이성문제라는점에서ㄷ의효과방향을놓친다."
  }
}
```
