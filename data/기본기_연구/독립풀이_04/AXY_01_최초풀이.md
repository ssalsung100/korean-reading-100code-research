

<!-- luna-raw:AXY-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G348",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "미확정",
  "required_information_and_location": [
    "1문단 주파수×파장=일정",
    "2문단 높은 주파수→강한 직진성",
    "3문단 같은 비트당 파동수 조건에서 주파수↑→초당 정보↑",
    "끝문단 유효길이∝파장"
  ],
  "minimal_logic_without_codes": "직진성 약함은 낮은 주파수 쪽이며 같은 부호화 조건에서 정보 전송량도 적어진다.③은 마지막 방향을 반전한다.",
  "intermediate_reasoning": [
    "①반비례 재진술",
    "②전파를 빛보다 낮은 주파수라 명시",
    "③주파수-직진성-정보량의 일관된 방향을 뒤집음",
    "④동일 비례상수 적용 시 L800/L2300=2300/800=2.875≈3",
    "⑤높은 주파수이면 회절·투과 약화"
  ],
  "most_attractive_wrong_answer": 4,
  "exact_error": "주파수 비율을 안테나 길이 비율에 같은 방향으로 옮기면 역수를 놓친다.",
  "source_quality_note": "안테나 유효 길이의 정확한 분수 계수가 전사에서 누락. ④의 상대비는 공통 계수가 소거되는 조건으로 확인했고③의 오류는 이 결손과 무관하다. 누락을 복원한 것처럼 취급하지 않는다.",
  "quota_status": "unavailable"
}
```
