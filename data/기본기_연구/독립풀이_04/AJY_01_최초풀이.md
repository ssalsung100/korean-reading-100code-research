

<!-- luna-raw:AJY-blind-20260926-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G225",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가; 엄격한 무노출 성과 확정 제외"
  },
  "needed_information_and_location": [
    "2문단: 전체 이미지와 같은 경로로 이동하는 부분에는 특정 종류 신경절세포가 출력하지 않음",
    "1문단: 안구는 계속 움직이며 마이크로칩은 망막에서 발생한 신호 관찰",
    "5문단: 밝기 변화 직후 최대 뒤 감소·증폭률 동적 조절"
  ],
  "minimal_logic_without_codes": "정지 물체의 상은 안구 움직임에 따른 전체 이미지 이동과 같은 경로로 움직이므로 특정 종류 신경절세포가 신호를 내지 않는다. 따라서 그러한 세포가 존재한다는③이 맞다.",
  "intermediate_inferences": [
    "① 신호를 증폭하고 줄이므로 원래 세기 그대로 출력한다고 할 수 없음.",
    "② 한곳을 응시해도 안구가 움직여 이미지 떨림 발생.",
    "④ 빛 반응은 광수용체의 역할이고 칩은 망막 전기 신호를 관찰.",
    "⑤ 밝기 변화 뒤 유지되는 상황에서도 반응은 최대 이후 감소할 수 있음."
  ],
  "most_attractive_wrong_answer": {
    "choice": 5,
    "attraction": "입력 밝기가 같으면 출력도 같다고 단순 대응시키기 쉽다.",
    "error": "본문에 명시된 반응의 시간 의존성을 누락한다. 밝기만으로 세기를 결정할 수 없다."
  },
  "quota_status": "unavailable"
}
```
