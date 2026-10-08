

<!-- luna-raw:ALE-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 1,
  "blind_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2023/2023_answer_언어이해정답.pdf",
  "logic_without_codes": "처음·끝의지동일≠중간포기없이일관.만세의포기시도를보존한다.",
  "correction": "없음",
  "passage_group": "G236",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:ALE-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    5
  ],
  "primary_candidates": [
    5,
    4
  ],
  "working_primary": 5,
  "unique_primary_confirmed": false,
  "auxiliary": [
    3,
    23
  ],
  "surface": [
    78
  ],
  "judgment_reason": "만세의의지가중간에꺾였다회복되는변화를일관한지속으로바꾼①의앞절오류.",
  "competing_codes": [
    {
      "code": 4,
      "verdict": "공동후보",
      "reason": "전체기간의모든시점에의지가유지됐다는주장은중간포기시점하나로반증.5의시간적변화를양화로기술가능."
    },
    {
      "code": 3,
      "verdict": "보조",
      "reason": "포기→독려→회복의순서를유지하되단순선후교환이오류는아님."
    },
    {
      "code": 78,
      "verdict": "표면",
      "reason": "동기내용보다의지의지속여부가①의결정지점."
    }
  ],
  "minimal_change_test": "일관했다를포기하려다회복했다로수정하면오류해소.양끝태도만대조해서는못풂.",
  "confidence": 0.97,
  "passage_group": "G236",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
