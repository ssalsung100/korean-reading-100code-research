

<!-- luna-raw:AGE-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "㉠공인중개사직접매매는단속법규위반으로벌금·계약유효·급부의무유지.",
    "㉡의사/비의사동업은강행법규위반으로법적불이익·계약무효·이미준자금반환가능."
  ],
  "minimal_logic_without_codes": "둘다위법계약에법적불이익이있다는점은같지만계약효력과급부의무는다르다.①이공통.",
  "intermediate_reasoning": [
    "② 급부의무부정은㉡쪽이고㉠에는의무존속.",
    "③ 반환은㉡의이미지급한자금에서문제되며㉠은유효계약상급부.",
    "④ 무효는㉡만해당.",
    "⑤ 위법내용의계약을선택했다는것과계약효력을인정받는것은다름. 내용결정자체가불가능한것은아님."
  ],
  "most_attractive_wrong_answer": 4,
  "exact_error": "법규위반이라는공통점만으로계약효력도모두부정된다고확대한다. 단속법규는벌금과유효계약이함께성립.",
  "quota_status": "unavailable"
}
```
