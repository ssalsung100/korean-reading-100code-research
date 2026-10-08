

<!-- luna-raw:ARM-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G292",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "첫문단 한 톨 추가의 미세 변화는 더미 여부를 안바꾼다고 반복하지만 끝에서는 더미",
    "선지③ 한 판자씩 교체하여 결국 원래 배인지 의문"
  ],
  "minimal_logic_without_codes": "매 작은 변화에서는 같은 범주를 유지한다고 보지만 누적 후 그 범주 귀속이 의심되는 구조가 배 판자 교체와 같다.",
  "intermediate_reasoning": [
    "① 작은 작업 누적이 큰 결과를 낳는다는 정상 누적 설명으로 범주 유지와 끝점 충돌이 없다.",
    "② 뜻의 연쇄 동일성은 있으나 점진적 차이가 누적되는 과정이 아니다.",
    "③ 한 판자 교체 때 동일 배로 인정해 온 판단이 누적된 교체 끝에서 흔들린다.",
    "④ 동일한 두 선택지 때문에 선택하지 못하는 문제다.",
    "⑤ 먹이사슬 연쇄이지 미세 차이를 무시해 범주 결론이 모순되는 구조가 아니다."
  ],
  "attractive_wrong_answer": 2,
  "exact_error": "연쇄라는 표면만 공유한다. 작은 차이에 대한 판정 불변을 반복한 뒤 끝점과 충돌한다는 요건이 없다.",
  "quota_status": "unavailable"
}
```
