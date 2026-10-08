

<!-- luna-raw:AVI-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G325",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "3문단 일정 검체 수의 함량비로 분산",
    "7문단 연속 함량비를 정해진 개수씩 묶어 분산",
    "몇 종류 색은 성분 함량 환산의 채널"
  ],
  "minimal_logic_without_codes": "두 방법의 표본 단위와측정 채널을 대응한다. 검체 개수의 상대는 묶는 함량비 관측값 개수이며색 종류가 아니다.",
  "intermediate_reasoning": [
    "① 채취 표본/관측 영역 표본",
    "③ 한 표본의 크기 대응",
    "④ 시약/조사광은 분석 수단",
    "⑤ 반응량/반사광 세기는 함량 환산 관측량",
    "② 표본 수와성분 검출용 색 채널 수 혼동"
  ],
  "attractive_wrong_answer_and_error": "③: 질량과공간 영역은 단위가 달라도 한 표본이 포괄하는 양·범위라는 역할 대응이다.",
  "quota_status": "unavailable"
}
```
