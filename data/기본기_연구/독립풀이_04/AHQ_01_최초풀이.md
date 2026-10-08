

<!-- luna-raw:AHQ-blind-20260921-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G207",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_and_location": [
    "2문단 정전압소자 출력 고정",
    "4문단 비교회로는 기준전압에 출력 맞춤",
    "변압기 변화입력 원리·주파수/크기 관계"
  ],
  "minimal_logic_without_codes": "선형의 목표 출력은 고정출력 소자로, 스위칭은 비교 기준으로 정해진다. 출력 변경 시 각각 소자와 기준전압을 바꾼다는③이 적절하다.",
  "intermediate_inferences": [
    "① 직류는 선형의 첫 변압기에 변화입력 제공 못함",
    "② 선형은 변압기로 낮춘뒤 정류, 스위칭 첫 정류는220V",
    "④ 낮은주파수 선형 변압기가 더 큼",
    "⑤ 에너지저장소자는 변동 억제 역할이고 손실처리 방식이 아님"
  ],
  "most_attractive_wrong_answer": {
    "choice": 4,
    "attraction": "스위칭의 더 높은 주파수 진술은 맞음",
    "error": "낮은 주파수일수록 크기가 커진다는 뒤 관계의 비교 방향을 뒤집음."
  },
  "quota_status": "unavailable"
}
```
