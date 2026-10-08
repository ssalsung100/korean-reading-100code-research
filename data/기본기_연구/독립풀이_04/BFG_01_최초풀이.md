

<!-- luna-raw:BFG-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G409",
  "selected_answer": 1,
  "confidence": 0.9,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "3문단 이항방식의 정부형태 교차분석 한계·내각 미참여 실체 배제",
    "4문단 내각 참여 막론 비율 지수·선거와총선 비교",
    "끝 문단 형태·상황에 국한되지 않는 기준"
  ],
  "minimal_logic_without_codes": "지수화의 도입 목적은 내각 참여 여부에 갇히지 않는 공통 기준이다. 내각 참여 정당만의 상대 영향력 비교를 도입 배경으로 좁히는①은 글의 핵심 방향과 맞지 않는다.",
  "intermediate_reasoning": [
    "②④⑤ 정부 형태·선거 종류를 넘어 같은 기준으로 비교하려는 요구와 직접 부합.",
    "③ 득표와 의석 비율을 각각 지수로 바꾸므로 선거/의회 체계도 비교 가능.",
    "①은 내각 참여 여부를 막론하고 반영하려는 설계 목적을 참여 정당 내부의 비교로 축소한다."
  ],
  "attractive_wrong": {
    "choice": 3,
    "exact_error": "본문이 대통령 선거와 총선 비교를 예로 든다는 이유로 선거 지수/의회 지수의 비교도 불가능하다고 생각한다. 동일 비율 공식이 두 지수를 제공한다."
  },
  "uncertainty": "지수 방식으로 내각 참여 정당의 영향력을 비교하는 것 자체가 불가능한 것은 아니다.①은 기능적 불가능이 아니라 본문에 제시된 도입 배경의 부적합으로 한정한다."
}
```
