

<!-- luna-raw:BLC-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G462",
  "selected_answer": 5,
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
      "evidence": "RNA일부만번역,유전체→전사체→단백질체의기능정보범위축소."
    },
    {
      "location": "3~4문단",
      "evidence": "분화시단백질조합변화.정상세포에서암세포로바뀌는것도분화이며단백질의양차이발견."
    }
  ],
  "minimal_logic_without_codes": "정상세포와암세포는분화·단백질조합및양변화에따라단백질체정보가동일하지않으므로⑤가맞는다.",
  "intermediate_reasoning": [
    "① 일부RNA를모든RNA로확대한다.",
    "② 단백질체정보가유전체정보중일부라는포함방향을뒤집는다.",
    "③ 인간·생쥐간세포는유전체정보가다르고동일기관명만으로단백질체전체의동일성을확정할근거가없다.",
    "④ 정상→암세포를분화라고부르는본문과반대다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "간세포라는동일기능범주를종이달라도단백질체정보전체가동일하다는명제로확대한다."
  },
  "scope_limit": "지문모형의유전체·전사체·단백질체정보관계판정.현실암유전체의변이유무를본문밖에서추가하지않음."
}
```
