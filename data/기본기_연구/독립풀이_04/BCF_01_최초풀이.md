

<!-- luna-raw:BCF-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G383",
  "selected_answer": 3,
  "confidence": 0.86,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BCF.json",
  "needed_information_and_location": [
    "1문단 액체 물의 온도 범위·탄소와유기화합물",
    "마지막 문단 우리 은하·항성 생성률·고등 문명 존속 기간·생명 가능 행성/탄생 확률"
  ],
  "minimal_logic_without_codes": "예측 대상은 우리 은하의 문명 수이며,온도와원소 종류는 생명 가능 조건에 연결된다.문명 존속 기간과 항성 평균 수명,하나의 은하 안의 수와 은하 개수를 바꾸지 않는다.",
  "intermediate_reasoning": [
    "ㄱ 행성 온도는 액체 물 및생명 가능한 행성 수/탄생 확률에 영향.",
    "ㄹ 구성 원소는 탄소·물의 확보 및생명 조건과 연결.",
    "ㄴ 우리 은하로 범위 고정했으므로 다른 은하의 개수는 곱할 요소 아님.",
    "ㄷ 방정식의 시간 인자는 통신 가능한 고등 문명의 존속 기간이지 항성 평균 수명이 아님.물리적 간접 영향은 가능해도 본문이 연결 근거를 주지 않음."
  ],
  "most_attractive_wrong_answer": {
    "choice": 2,
    "exact_error": "생명에 알맞은 항성이라는 말과 문명 존속 기간의 시간 인자를 결합해 항성의 평균 수명을 직접 고려요소로 바꾼다.반면 원소 종류는 첫 문단의 생명 조건으로 명시적 연결이 있다."
  },
  "residual_uncertainty": "고려 요소라는 넓은 발문에서항성수명의간접영향을배제하는범위는본문조건한정.물리적무관함을뜻하지않음.",
  "quota_status": "unavailable"
}
```
