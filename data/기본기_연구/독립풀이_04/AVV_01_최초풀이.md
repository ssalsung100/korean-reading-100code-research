

<!-- luna-raw:AVV-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G330",
  "selected_answer": 3,
  "confidence": 0.96,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "1문단 비가시성·형식 유지",
    "3문단 손실없는양방향변환",
    "4문단 삽입값이공간에서잡음·연산량증가"
  ],
  "minimal_logic_without_codes": "워터마크는 원본에 더해진 식별 정보로 표현 영역을 바꾸어도 원본에 대한 추가 성분이다.③을 수용하며 나머지는 명시 조건과반대다.",
  "intermediate_reasoning": [
    "① 비가시성낮추기아님",
    "② 변환손실없음",
    "④ 저장형식유지·다시공간으로복귀",
    "⑤ 주파수방식연산량이더큼",
    "③ 공간잡음은명시,주파수에서도추가식별성분을원본대비잡음으로해석"
  ],
  "attractive_wrong_answer_and_error": "③의주파수잡음은본문직접문구보다표현변환과추가정보의동일성에기댄확장임을보존.",
  "visuals_reviewed": [
    "G330_visual01.jpeg"
  ],
  "source_scope": "원문속워터마크특성·독해판정만분석;외부기술절차추가없음",
  "quota_status": "unavailable"
}
```
