

<!-- luna-raw:ARQ-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G293",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "diagram_seen": true
  },
  "needed_information_locations": [
    "보기: 전기장 속 절연체 변위와 용수철의 신장 대응",
    "blind_sources/G293_visual01.png 직접 확인: 도체판 사이 절연체·오른쪽 변위 화살표·전지 연결",
    "본문 연속 매질의 역학적 모형 설명"
  ],
  "minimal_logic_without_codes": "전기장 속 연속 매질인 절연체가 힘에 의해 변형되는 것을 용수철의 변형에 대응하여 설명하므로②의 역학적 모형 해석이다.",
  "intermediate_reasoning": [
    "① 매질 역할은 도체판이 아니라 사이의 절연체이고 전기 입자 전달 설명이 아니다.",
    "② 연속 매질의 힘·변위를 기계적 변형으로 모델링한다.",
    "③ 원격 작용은 매질 없이 건너가는 힘의 설명이므로 보기의 매질 변형 전달과 다르다.",
    "④ 그림과 보기 모두 절연체로 채운 공간이며 빈 공간이 아니다.",
    "⑤ 질점의 집합체라고 환원하지 않고 연속 매질의 변형을 기술한다."
  ],
  "attractive_wrong_answer": 3,
  "exact_error": "힘 전달에 매질이 있다는 설명과 매질 없이 작용하는 원격 작용을 섞는다.",
  "resolved_hold": "ARQ-hold-20260927-01",
  "source_correction": "기존 hold의 실제 자료 누락 및 metadata 불일치 판단은 철회한다. ARQ.json에 visual_supplements로 이미지 경로가 이미 있었으나 Astra가 passage_text/stem/choices만 출력하여 놓쳤다. 연결 이미지 존재·내용을 직접 확인했고 신규 복원은 불필요. 원 hold는 불변 보존.",
  "quota_status": "unavailable"
}
```
