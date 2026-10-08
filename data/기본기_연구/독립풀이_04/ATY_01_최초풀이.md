

<!-- luna-raw:ATY-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G313",
  "selected_answer": 1,
  "confidence": 0.98,
  "exposure": {
    "prior_exposure": "이 세션의 사전 해설·정답·SDSS 노출 없음; 과거 노출 미확인",
    "official_answer_seen": false,
    "sdss_seen": false
  },
  "strict_blind_eligible": "과거 노출 미확인으로 확정 집계 보류",
  "needed_information_and_location": [
    "진료기록: 동맥경화 예방 아스피린과 류머티즘 치료 셀레콕시브 병용·수술 예정",
    "2문단 비가역 억제·혈소판 효소 재생 불가",
    "3문단 장기 복용 위장 부작용 및 선택적 COX2 약물"
  ],
  "minimal_logic_without_code": "공통 작용 계열만으로 환자의 서로 다른 질환·목적에 필요한 약제를 중복이라고 제거할 수 없다. 수술 전후는 출혈 위험과 장기 혈전 예방 목적을 나누어 평가한다.",
  "intermediate_reasoning": [
    "① 셀레콕시브의 관절염 치료 역할을 무시한 중복 판단",
    "② 동맥경화 병력에 혈전 예방 목적 유지",
    "③ 5년 복용에 위장 부작용 검사 연결",
    "④ 비가역 억제된 혈소판이 회복 안 되면 정상 혈소판 보충 고려",
    "⑤ 수술 전 출혈 부작용을 줄이는 조치"
  ],
  "most_attractive_wrong_answer_and_error": "④: 약 중단만으로 이미 억제된 혈소판의 효소가 재생되지 않는다는 조건이 있어 보충 조치는 본문과 양립한다.",
  "source_scope": "시험 원문 내부 독해; 현재 의료 판단으로 확장하지 않음"
}
```
