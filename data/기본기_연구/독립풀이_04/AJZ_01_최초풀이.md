

<!-- luna-raw:AJZ-blind-20260926-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G225",
  "selected_answer": 4,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가; 엄격한 무노출 성과 확정 제외"
  },
  "needed_information_and_location": [
    "본문5·6문단: 이동 앞쪽 경계에서 신호 최대, 속력 과대·밝기 차 작음이면 보상 약화",
    "공식 blind 도식 직접 판독: 막대 왼쪽 경계 부근 b최대, c는 그보다 오른쪽, a최대는 중심선 오른쪽; b와c 속력 동일"
  ],
  "minimal_logic_without_codes": "b의 최대 위치가 막대 왼쪽 앞 경계에 있으므로 이동은 왼쪽이다. 뒤쪽으로 밀린 a의 최대 위치는 빠른 이동에 대한 보상 부족을 나타낸다. 동일 속력에서 b가 c보다 보상이 잘 되므로 밝기 차는 b가 더 크다. ㄱ·ㄴ만 맞아④.",
  "intermediate_inferences": [
    "ㄱ: 세 곡선의 같은 이동 방향과 앞 경계의 최대 위치를 연결하면 오른쪽→왼쪽.",
    "ㄴ: a의 최대점은 b보다 이동 방향의 뒤에 있어 속력이 큰 경우에 해당.",
    "ㄷ: 같은 속력에서 밝기 차가 작으면 보상이 약해지므로 b보다 뒤인 c가 작은 밝기 차."
  ],
  "most_attractive_wrong_answer": {
    "choice": 5,
    "attraction": "b·c 곡선 높이만 보고 밝기 차를 대응시키거나 좌우 이동 방향을 거꾸로 잡기 쉽다.",
    "error": "핵심은 봉우리 높이 자체가 아니라 이동 앞 경계와 최대 위치의 상대적 지연이다. ㄱ은 참이고 ㄷ은 반대이다."
  },
  "quota_status": "unavailable"
}
```
