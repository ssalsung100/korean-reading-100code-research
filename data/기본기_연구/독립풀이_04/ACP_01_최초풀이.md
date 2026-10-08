

<!-- luna-raw:ACP-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G180",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "2문단 모든 소리 크기에 균일한 개수의 비트 할당, 크기에 따라 이진수 값은 달라짐.",
    "1문단 아날로그 홈 기록;5문단 청각 특성에 따른 디지털 신호 압축."
  ],
  "minimal_logic_without_codes": "압축 전에는 소리 크기별 값이 달라도 각 값을 표시하는 비트 수는 같으므로③. 값의 차이와 표현 자리 수의 차이를 구분한다.",
  "intermediate_reasoning": [
    "① 초기 녹음은 아날로그다.",
    "② 홈뿐 아니라 이진수도 저장된 소리에 대응한다.",
    "④ 비트 증가로 데이터가 커져 전송의 난점이 커진다.",
    "⑤ 압축 후 아날로그로 저장한다는 설명은 없다."
  ],
  "most_attractive_wrong_answer": 2,
  "exact_error": "표현 형태가 달라지는 사실을 디지털 이진수는 소리에 대응하지 않는다는 부정으로 확대한다.",
  "quota_status": "unavailable"
}
```
