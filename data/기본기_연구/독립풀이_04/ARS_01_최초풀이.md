

<!-- luna-raw:ARS-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G294",
  "selected_answer": 1,
  "confidence": 0.96,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "ⓐ 바람→해류→해수 온도→바람의 되먹임",
    "ⓑ 초기 조건 차이의 후속 상태 분기",
    "보기ㄱ/ㄴ/ㄹ의 원인으로 되돌아가는 고리,ㄷ의 조건별 반대 결과",
    "G294_visual01.md 선택지표 직접 확인"
  ],
  "minimal_logic_without_codes": "ㄱ·ㄴ·ㄹ은 결과가 다시 처음 원인을 강화하는 닫힌 고리이고 ㄷ은 기상 조건 차이에 따라 태풍 증가/감소로 갈라지는 경로다.",
  "intermediate_reasoning": [
    "ㄱ 온도→냉방→폐열→온도.",
    "ㄴ 냉각·습윤→해무→복사 변화→냉각·습윤.",
    "ㄹ 이산화탄소→기공·증산 감소→강우 감소→우림 감소→이산화탄소.",
    "ㄷ은 증발 수증기의 조건별 사용·응결에 따라 결과 방향이 달라지며 원인으로 되돌아가는 고리는 제시되지 않는다.",
    "표에서ⓐㄱㄴㄹ/ⓑㄷ은①."
  ],
  "attractive_wrong_answer": 3,
  "exact_error": "해무가 원인이면서 결과라는ㄴ의 순환을 놓치고 복잡한 변화라는 이유로 카오스에 넣는다.",
  "uncertainty": "ㄷ은 본문 카오스 정의의 미미한 차이·시간에 따른 급속 확대를 모두 명시하지 않는다. 선택지 간 상대적 분류이며 과학적 충분조건을 충족한 엄밀 사례로 확대하지 않는다.",
  "quota_status": "unavailable"
}
```
