

<!-- luna-raw:AYX-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G356",
  "selected_answer": 3,
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
    "3문단 인버터와 저장출력 반전",
    "4문단 조합출력→저장입력 연결",
    "G356_visual01.png 그림"
  ],
  "minimal_logic_without_codes": "조합 회로 출력 A는 저장 회로의 인버터를 거쳐 B에서 반대로 나온다. 서로 다른 위치의 출력값을 동일시한③이 틀리다.",
  "intermediate_reasoning": [
    "①기능-상태 일대일",
    "②인버터 반전",
    "③A와B 사이 반전 누락",
    "④명령코드로 상태변화",
    "⑤논리함수 출력"
  ],
  "most_attractive_wrong_answer": 1,
  "exact_error": "프로그램이 다양한 작업을 만든다는 이유로 CPU의 상태-기능 대응까지 임의로 변한다고 오해한다.",
  "quota_status": "unavailable"
}
```
