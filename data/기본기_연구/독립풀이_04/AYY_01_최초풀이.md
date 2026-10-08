

<!-- luna-raw:AYY-blind-20260928-01 -->
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
    "3문단 S2닫고S1열면 상태유지",
    "4문단 B와C를 조합하여 A로 되먹임",
    "그림 내부두인버터 루프와 외부조합 루프"
  ],
  "minimal_logic_without_codes": "내부 되먹임은 두 번 반전으로 상태를 유지한다.외부 되먹임은 현재 B와 입력 C를 조합해 다음 상태를 정한다.따라서 저장/변경의 기능구별이④다.",
  "intermediate_reasoning": [
    "①루프의 부품 역할 교환",
    "②내부는 기존상태,외부는 B와C 두입력",
    "③외부입력을 그대로 유지하지 않음",
    "④각루프 기능 맞음",
    "⑤내부 S2와외부 S1의 연결조건 교환"
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "둘 다 피드백이라는 공통구조만 보고 외부입력을 그대로 저장하는 동일기능으로 묶는다.",
  "quota_status": "unavailable"
}
```
