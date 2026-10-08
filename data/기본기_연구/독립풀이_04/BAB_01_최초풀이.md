

<!-- luna-raw:BAB-blind-20261001-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "blind_source_seen": true,
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가; 이번 세션에서 사전 노출 없음. 엄격 blind 성과 자동 확정 안 함"
  },
  "source_read": [
    "BAB.json",
    "G365_visual01.md"
  ],
  "source_quality": "시각자료 자리표시자의 보기와 ㄱ·ㄴ·ㄷ은 지정된 blind-only 보충 MD에 모두 존재하여 직접 확인함.",
  "required_information_and_location": [
    "5문단: 소 제기 날짜 확인 실패 같은 현저한 법적 기준 위반은 특별 위법 사정",
    "5문단: 불복 절차가 마련되어 있는 경우에 절차 미경유를 제한",
    "보기: 적법 기간 내 11월 4일 제출, 14일로 오인, 당시 불복절차 부재"
  ],
  "minimal_logic_without_codes": "접수일 오인은 소 제기 날짜 확인 실패에 해당하여 독립성으로 보호할 단순 판단 차이를 벗어난다. 불복절차가 없었던 경우에는 존재하는 절차를 이용하지 않았다는 이유로 배상을 막을 수 없다. ㄱ과 ㄴ은 맞고 ㄷ은 틀리다.",
  "intermediate_reasoning": [
    "ㄱ: 전원일치라는 사정도 날짜 오인의 성격을 바꾸지 않는다. 직무상 독립만으로 배상책임을 일률 부정할 수 없다.",
    "ㄴ: 실제 제출일 11월 4일을 확인하고 날짜 오인을 현저한 기준 위반으로 평가해 위법성을 인정할 수 있다. 이는 실제 배상 판결의 결과 전체를 확정한다는 말은 아니다.",
    "ㄷ: 절차가 마련되어 있는 경우라는 적용 조건을 건너뛰고, 절차가 없는 사건에도 미경유 불이익을 부과한다. 본문은 부재 자체를 배상 배제 사유로 정하지 않는다.",
    "ㄱ·ㄴ 조합은 ④이다."
  ],
  "most_attractive_wrong_answer": {
    "choice": 5,
    "why_attractive": "ㄴ을 인정하면서도 불복을 거친 적 없으므로 ㄷ도 맞는다고 생각할 수 있다.",
    "exact_error": "이용 가능한 절차의 미경유와 절차 자체의 부재를 혼동한다. 또한 ㄱ은 날짜 확인의 현저한 잘못 때문에 참인데 조합에서 빠진다."
  },
  "passage_group": "G365",
  "quota_status": "unavailable"
}
```
