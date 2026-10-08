

<!-- luna-raw:AVC-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G323",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "4문단 자기장→두방향 위상 차이→약한 국소화 거의 사라짐",
    "3문단 온도 증가→결맞음 길이0 접근→발생 조건 불충족"
  ],
  "minimal_logic_without_codes": "자기장은 전자 이동 방해 경로를 줄여 저항을 낮춘다.온도는 올려 결맞음 길이를 줄이면 앤더슨 발생 필요조건을 깨뜨릴 수 있다.",
  "intermediate_reasoning": [
    "A: 국소화 때 저항 증가,자기장으로 그 효과 소실→저항 감소",
    "B: 온도 올림→요동·상호작용 증가→결맞음 감소→국소화 유지 불가",
    "③ 작아진다/높인다 조합"
  ],
  "attractive_wrong_answer_and_error": "④: A는 맞으나온도 내림은 결맞음을 더 유지시키므로 제거 방향 반대.",
  "quota_status": "unavailable"
}
```
