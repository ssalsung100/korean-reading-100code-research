

<!-- luna-raw:AHJ-blind-20260921-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G205",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_and_location": [
    "5문단 오네소르게 수의 점도 및 표면장력×밀도×노즐지름 의존",
    "6문단 적정범위보다 큼→분사불가, 작음→위성방울",
    "보기 초기 둘다 안정·2개월 파랑 불변"
  ],
  "minimal_logic_without_codes": "점도와 표면장력을 유지하고 밀도×지름을 2×1/2로 바꾸면 곱이 보존된다. 오네소르게 수를 결정하는 값들이 보존되어③이 참이다.",
  "intermediate_inferences": [
    "① 초기 빨강도 안정 범위였으므로 달리라는 비교 오류",
    "② 빨강 점도 증가로 적정 상한 초과 후 정상화하려면 오네소르게 수 감소",
    "④ 2개월 파랑은 조건 불변이므로 기존 적정 상태 유지",
    "⑤ 점도 증가로 수가 커지는 방향은 낮은 범위에서 생기는 위성방울과 반대"
  ],
  "most_attractive_wrong_answer": {
    "choice": 5,
    "attraction": "점도가 변하면 인쇄불량이 생길 수 있다는 넓은 유사성",
    "error": "위성방울은 수가 너무 작은 경우인데 점도 증가는 수를 올린다. 불량 유형의 방향을 구별해야 한다."
  },
  "quota_status": "unavailable"
}
```
