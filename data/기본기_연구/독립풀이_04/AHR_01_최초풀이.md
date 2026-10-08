

<!-- luna-raw:AHR-blind-20260921-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G207",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_and_location": [
    "4문단 변화 적은 전압은 변압기 출력 거의 없음",
    "4문단 온오프비 증가→출력상승, 노이즈 주파수 동일",
    "보기4.5V/5V·100kHz와 공식그림 비교회로 피드백"
  ],
  "visual_evidence": "blind supplement의 공식PDF 구조도 직접 확인: 정류→평활→스위치→변압기→정류→평활, 최종출력과5V기준이 비교회로로, 그 신호는 스위치로 귀환",
  "minimal_logic_without_codes": "계속 온이면 평활된 입력을 그대로 유지하여 변압기에 필요한 변화가 사라진다. 따라서 온 시간을 계속 늘리는 것과 계속 온 상태를 같게 보아5V까지 높아진다는①은 성립하지 않는다.",
  "intermediate_inferences": [
    "② 노이즈100kHz는 온오프 신호 주파수와 일치",
    "③ 정류·평활 후 단방향·변동적음",
    "④4.5<5이므로 출력 올리려면 온비율 증가/오프시간 감소",
    "⑤ 온은 입력=출력, 오프는0"
  ],
  "most_attractive_wrong_answer": {
    "choice": 4,
    "attraction": "출력이 부족하면 오프를 늘려야 한다고 부호 혼동",
    "error": "출력 올리려면 온비율을 키워야 하므로 같은 주기에서 오프시간은 줄어든다."
  },
  "quota_status": "unavailable"
}
```
