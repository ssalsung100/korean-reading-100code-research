

<!-- luna-raw:AMR-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 2,
  "blind_answer": 2,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "두 망에서 한 연결을 이동하는 행위가 편지 전달과 클릭으로 대응한다.",
  "correction": "없음",
  "passage_group": "G249",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:AMR-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    39
  ],
  "primary_candidates": [
    39,
    69
  ],
  "working_primary": 39,
  "unique_primary_confirmed": false,
  "auxiliary": [
    17
  ],
  "surface": [
    91
  ],
  "judgment_reason": "인간망의편지전달한단계와웹망의클릭한단계를동일역할로대응시킨다.",
  "competing_codes": [
    {
      "code": 69,
      "verdict": "공동 후보",
      "reason": "서로다른영역의구조적유사성으로방법대응을읽음."
    },
    {
      "code": 17,
      "verdict": "보조",
      "reason": "사람/문서노드와전달/클릭간선을역할별로귀속."
    },
    {
      "code": 91,
      "verdict": "⑤오답",
      "reason": "규모와거리의정비례부정은⑤검사이지②직접관계아님."
    }
  ],
  "minimal_change_test": "②의편지전달을편지를받는사람으로바꾸면노드를클릭간선에잘못대응하는오류가됨.",
  "confidence": 0.97,
  "passage_group": "G249",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
