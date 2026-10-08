

<!-- luna-raw:ASK-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G300",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "㉠ 화성 기원과 생명 흔적의 두 주장",
    "ⓐ동위 비율·ⓑ이황화철의화성연결",
    "ⓒ우주복사선으로 생긴동위원소는체류기간",
    "ⓓ탄산염·ⓔ자철석의생명해석"
  ],
  "minimal_logic_without_codes": "ⓒ는 우주 체류 기간을 추정하는 지표이며 화성 기원 또는 생명 흔적이라는㉠의 두 주장에 직접 연결되지 않는다.",
  "intermediate_reasoning": [
    "ⓐⓑ는 기원,ⓓⓔ는 물/생명흔적을 지지한다.ⓒ만 체류기간이라는 다른 질문을 다룬다."
  ],
  "attractive_wrong_answer": 2,
  "exact_error": "ⓑ가 생명 증거가 아니라는 이유로 제외하면㉠이 화성 기원도 함께 주장한다는 복합 범위를 놓친다.",
  "quota_status": "unavailable"
}
```
