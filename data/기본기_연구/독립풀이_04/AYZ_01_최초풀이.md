

<!-- luna-raw:AYZ-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G356",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "visual_seen": "blind-only G356_visual01.tif가 뷰어에서 지원되지 않아 같은 디렉터리에 RGB PNG로 형식변환한 그림 직접확인;내용추가없음"
  },
  "strict_blind_eligible": "미확정",
  "required_information_and_location": [
    "1문단 상태수많으면동일데이터처리시간감소",
    "5·6문단 N비트확장·CPU클록의상태변경속도"
  ],
  "minimal_logic_without_codes": "N이 커지면 명령과 상태의 종류 및 한 번에 처리할 기능이 늘지만 상태를 변경하는 시간간격은 클록이 정한다.전체 작업 속도와 상태전환 빈도를 혼동하지 않는다.",
  "intermediate_reasoning": [
    "①N비트명령공간확대",
    "②③상태가짓수2의N제곱 증가",
    "④N만으로클록증가결론불가",
    "⑤같은클록에서더많은기능처리로작업시간감소"
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "상태변경속도가그대로라는사실로 전체작업처리속도도그대로라 단정하면 1문단의 기능다양성을 놓친다.",
  "quota_status": "unavailable"
}
```
