

<!-- luna-raw:AKA-blind-20260926-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G225",
  "selected_answer": 5,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가; 엄격한 무노출 성과 확정 제외"
  },
  "needed_information_and_location": [
    "본문4문단: 1/60초의 짧은 밝기 자극 후 약1/20초 지연·약1/20초 신호 지속",
    "본문2·5·6문단: 전체 경로와 다른 이동 검출·앞부분 증폭·밝기 차와 지연 보상"
  ],
  "minimal_logic_without_codes": "짧게 상이 사라지는 깜박임은 그 위치의 밝기를 짧게 변화시킨다. 제시 실험의 시간 반응에 따르면1/60초 자극 변화에 대해 약1/20초 동안 출력하므로 자극보다 오래 지속된다는⑤가 가장 적절하다.",
  "intermediate_inferences": [
    "① 속력 감소는 지연 보상에 유리한 것이지 개별 세포 지연 자체가 감소한다고 한 것은 아님.",
    "② 상하 배경 움직임과 수평 파리 움직임은 경로가 달라 검출 가능.",
    "③ 밝기 차가 클수록 보상이 잘 되므로 오차가 커진다는 방향 오류.",
    "④ 이동 앞쪽 머리 부분 신호를 먼저 크게 증폭하므로 몸통보다 작다는 것은 반대.",
    "⑤ 없어졌다 다시 나타나는 짧은 밝기 변화에 대해 출력 지속 시간이 자극 시간보다 길다."
  ],
  "most_attractive_wrong_answer": {
    "choice": 1,
    "attraction": "공의 속력이 느릴수록 잘 맞히므로 지연 시간도 짧아진다고 바꾸기 쉽다.",
    "error": "개별 세포 처리 지연과 여러 세포 출력의 선행 위치를 통한 지연 보상을 혼동한다."
  },
  "quota_status": "unavailable"
}
```
