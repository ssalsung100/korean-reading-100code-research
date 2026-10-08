

<!-- luna-raw:AGW-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "identity_metadata_seen": "AGYblind supplement에서2022예시문항식별자확인;답/태그없음"
  },
  "required_information_and_location": [
    "2문단과충전양·과방전→수명감소,과충전온도상승위험.",
    "3문단전원전압>공칭전압,4문단최대온도제한;메모리효과는니켈카드뮴에만있음.",
    "공식문항전재본crop번호②=허용전류보다큰전류는수명감소."
  ],
  "minimal_logic_without_codes": "본문은충전양초과의수명영향을말하며허용전류초과라는전류세기조건의수명영향은제시하지않는다.②는원문근거를찾을수없다.",
  "intermediate_reasoning": [
    "① 전원전압조건은명시.",
    "③ 과온도를기준넘지않도록중지하는방식명시.",
    "④ 리튬은니켈카드뮴특유의메모리효과와달라수시충전제한근거없음.",
    "⑤ 과방전은수명감소명시."
  ],
  "most_attractive_wrong_answer": 4,
  "exact_error": "니켈카드뮴의부분방전후충전반복문제를리튬충전지로옮기면원문특정범위를확대한다.",
  "visual_verification": "AGW_Q31_official_crop_20260920.png에서5항목과①~⑤전체대응직접확인. 기존JSON첫항목stem밀림·빈choiceshold보존.",
  "source_qualification": "2022학년도예시문항의문제지전재본URLorbi.kr/download/united/40109864/1에서추출. 공식배포호스트직접검증이나실제시행기출로승격하지않음. 실제전기안전판정이아닌본문근거범위판정.",
  "quota_status": "unavailable"
}
```
