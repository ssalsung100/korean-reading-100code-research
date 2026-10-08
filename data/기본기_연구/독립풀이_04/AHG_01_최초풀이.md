

<!-- luna-raw:AHG-blind-20260921-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G204",
  "selected_answer": 5,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_and_location": [
    "2문단 ⓐ는 AI 활용 제품·서비스 사업자에 표시의무, 광고 제작자·플랫폼 확대는 주장",
    "5문단 ⓑ 실명확인 미조치 언론사 제재 규정은 다수 의견에 의해 위헌",
    "보기: 언급 안 된 법률 적용 금지·을의 다수 이름 게시"
  ],
  "minimal_logic_without_codes": "ⓑ의 헌재 결론은 실명확인 미조치 제재 규정의 위헌이므로 그 결론에 따라 플랫폼 B가 제재된다는⑤은 반대이다. ⓐ 현행 적용대상과 확대 주장을 분리하면①②도 참이다.",
  "intermediate_inferences": [
    "① A는 광고 유통 플랫폼으로 확대 주장의 대상이지 현재ⓐ 대상 아님",
    "② 갑은 식품 판매·광고 제작자이지 AI 제품·서비스 제공자로 주어진 것 아님",
    "③ 사상 경쟁으로 판단하려는 다수 취지에 표현자를 처벌하자는 정책은 어긋남",
    "④ 다수 이름의 반복 게시가 시민 의견으로 오인되어 입법되었다면 소수의 왜곡 우려 지지 가능"
  ],
  "most_attractive_wrong_answer": {
    "choice": 2,
    "attraction": "갑이 AI를 써서 동영상 제작했으므로 AI제품·서비스 사업자라고 혼동",
    "error": "AI를 이용한 광고 제작과 AI 제품·서비스 제공은 다르며 광고자 의무 확대는 아직 주장이다."
  },
  "quota_status": "unavailable"
}
```
