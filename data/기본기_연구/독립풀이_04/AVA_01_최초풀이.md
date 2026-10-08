

<!-- luna-raw:AVA-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G323",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "3문단 결맞음 길이>국소화 길이가 발생 조건",
    "온도 상승→상호작용·요동 증가→결맞음 길이 감소",
    "2문단 위상 상쇄·다른 위치 확률0"
  ],
  "minimal_logic_without_codes": "국소화가 일어나려면 결맞음 길이가 국소화 길이보다 길어야 한다.①은 두 길이의 비교 방향을 뒤집는다.",
  "intermediate_reasoning": [
    "② 무작위 위상 합의 상쇄",
    "③ 상호작용 커지면 결맞음 감소",
    "④ 3차원에서 피해갈 경로로 도체 가능",
    "⑤ 다른점 이동확률이0에 가까운 현상",
    "① 필요 비교조건 반전"
  ],
  "attractive_wrong_answer_and_error": "④: 비결정질이라고 모두 부도체는 아니며 차원에 따른 경로 차이를 반영한다.",
  "quota_status": "unavailable"
}
```
