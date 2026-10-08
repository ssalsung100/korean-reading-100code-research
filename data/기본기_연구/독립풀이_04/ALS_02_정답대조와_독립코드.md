

<!-- luna-raw:ALS-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 3,
  "blind_answer": 3,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "전극 기판→바이러스 부착→결정막 형성→몸통 제거의 단계 의존성을 유지한다.",
  "correction": "없음",
  "passage_group": "G240",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:ALS-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    3
  ],
  "primary_candidates": [
    3,
    45
  ],
  "working_primary": 3,
  "unique_primary_confirmed": false,
  "auxiliary": [
    10
  ],
  "surface": [
    46
  ],
  "judgment_reason": "단계마다 만들어진 대상이 다음 단계의 입력이므로 순서를 복원한다.가열은 결정막 형성 이후여야제거할몸통과남길막이있다.",
  "competing_codes": [
    {
      "code": 45,
      "verdict": "공동 후보",
      "reason": "단계 입력-산출을연결하면동일순서가나옴."
    },
    {
      "code": 10,
      "verdict": "보조",
      "reason": "뒤 단계의 수행에 앞 단계가 마련한 상태가 필요."
    },
    {
      "code": 46,
      "verdict": "보조적내용",
      "reason": "작용기제는근거지만문항행동은주어진절차순서배열."
    }
  ],
  "minimal_change_test": "ㄱ과ㄹ을교환하면결정막이없는상태에서매개체를제거하여이후제조경로가끊긴다.",
  "confidence": 0.97,
  "passage_group": "G240",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
