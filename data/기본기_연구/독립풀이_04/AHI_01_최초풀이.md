

<!-- luna-raw:AHI-blind-20260921-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G205",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_and_location": [
    "1문단 내부-외부 압력차는 표면장력에 정비례·반지름에 반비례",
    "3문단 같은 물질 두 기포 결합 후 더 큰 기포",
    "2문단 높은 압력에서 낮은 압력으로 공기 이동"
  ],
  "minimal_logic_without_codes": "같은 물질의 기포가 합쳐져 반지름이 커지면 표면장력 조건을 유지한 압력차는 작아진다. 따라서 새 기포 압력차는 원래 큰 기포보다 작다는④.",
  "intermediate_inferences": [
    "작은 기포의 압력차가 더 크므로 공기는 작은 쪽에서 큰 쪽으로 이동",
    "② 큰 기포도 표면장력 작용",
    "③ 압력 동일이 아니라 차이 때문에 이동",
    "⑤ 내부-외부 차이는 평형에서 표면장력 압력과 같음"
  ],
  "most_attractive_wrong_answer": {
    "choice": 1,
    "attraction": "큰 기포에 공기가 많으므로 작은 쪽으로 이동할 것처럼 보임",
    "error": "이동 방향은 공기 총량이 아니라 압력으로 정하며 작은 반지름 쪽의 내부압력이 더 높다."
  },
  "quota_status": "unavailable"
}
```
