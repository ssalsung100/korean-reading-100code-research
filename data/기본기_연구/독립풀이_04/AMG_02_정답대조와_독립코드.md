

<!-- luna-raw:AMG-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 1,
  "blind_answer": 1,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "본문의 변화 관계에서 출발 언어 피진을 없애도 결과 크레올이 생긴다는①은 필요한 기반을 삭제한다.",
  "correction": "없음",
  "passage_group": "G245",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:AMG-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    10
  ],
  "primary_candidates": [
    10,
    16,
    3
  ],
  "working_primary": 10,
  "unique_primary_confirmed": false,
  "auxiliary": [
    45
  ],
  "surface": [
    6
  ],
  "judgment_reason": "피진에서크레올로변화하는본문의정의에서입력기반을삭제한①배제.",
  "competing_codes": [
    {
      "code": 16,
      "verdict": "공동 후보",
      "reason": "크레올화의정의에출발점피진이포함됨."
    },
    {
      "code": 3,
      "verdict": "공동 후보",
      "reason": "변화이전의피진환경과이후결과를보존."
    },
    {
      "code": 6,
      "verdict": "⑤관련",
      "reason": "선천능력필요는⑤이지만①직접오류는피진기반의부정."
    }
  ],
  "minimal_change_test": "①의 없어도를 기반으로로 교체하면 본문 관계에 맞는다.본문 밖 언어학의 모든 발생모형으로 확장하지 않는다.",
  "confidence": 0.95,
  "passage_group": "G245",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
