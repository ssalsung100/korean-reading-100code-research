

<!-- luna-raw:AVG-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G325",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "1문단 제품 사이 각 성분 비율의 일정함 정도",
    "3문단 함량비 분산 작을수록 균일도 높음"
  ],
  "minimal_logic_without_codes": "균일도는 단일 성분 함량비 값이 아니라 여러 제품에서 비율이 얼마나 일정한지다.",
  "intermediate_reasoning": [
    "③ 측정값과측정값 간 분포 특성을 혼동",
    "① 공정 중 반복 확인",
    "② 품질 판단 기준",
    "④ 분산으로 측정",
    "⑤ 미리 정한 기준 도달 시 종료"
  ],
  "attractive_wrong_answer_and_error": "④: 분산은 함량비의 퍼짐을 나타내므로 정의와 부합한다.",
  "quota_status": "unavailable"
}
```
