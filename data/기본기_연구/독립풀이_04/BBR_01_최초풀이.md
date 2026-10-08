

<!-- luna-raw:BBR-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G379",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BBR.json",
  "needed_information_and_location": [
    "2문단 해/달 주기 차이와 윤달 보정",
    "3~4문단 천체 운행을 통한 천의 해석",
    "마지막 문단 목성 12년 주기와 해의 식별"
  ],
  "minimal_logic_without_codes": "목성의 12년 주기 위치는 어느 해인지 표시하는 데 쓰인다. 이를 한 해 내부의 계절 변화를 가장 잘 알려 주는 수단으로 바꿀 수 없다.",
  "intermediate_reasoning": [
    "① 해/달 외 행성 관측을 포함한 역법 산물 및 목성 위치 활용에서 허용.",
    "② 354.36일과365.25일 차이를 윤달로 맞춤.",
    "③ 세성은 연도를 식별하는 기능인데 계절 판별과 행성 간 최상 비교로 바꿈.",
    "④ 천체를 통한 천의 해석이 행성 관측 확장의 문맥.",
    "⑤ 연365.25일의 소수부 누적을4년에 하루로 보정하는 추론."
  ],
  "most_attractive_wrong_answer": {
    "choice": 5,
    "exact_error": "본문에 윤일이라는 단어가 없다는 이유로 배제하면365.25일의0.25일 누적에서4년1일 보정이라는 주어진 수치 추론을 놓친다."
  },
  "quota_status": "unavailable"
}
```
