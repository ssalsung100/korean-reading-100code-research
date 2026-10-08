

<!-- luna-raw:AMX-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 2,
  "blind_answer": 2,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "여성을 얻기 어려워지고 종전의 교환·유대가 무너진다는 것과 여성을 얻어도 위세가 높아지지 않는다는 것은 다르다.위세추구수단이라는기능은남아있다.",
  "correction": "없음",
  "passage_group": "G251",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:AMX-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    5
  ],
  "primary_candidates": [
    5,
    44,
    1
  ],
  "working_primary": 5,
  "unique_primary_confirmed": false,
  "auxiliary": [
    17
  ],
  "surface": [
    9
  ],
  "judgment_reason": "교환방식과확보난이도는변했지만여성을통해위세를높이려는기능은유지된다.②는체계변화를그기능소멸로확대.",
  "competing_codes": [
    {
      "code": 44,
      "verdict": "공동 후보",
      "reason": "여성획득이라는수단이위세목적에여전히연결됨."
    },
    {
      "code": 1,
      "verdict": "공동 후보",
      "reason": "확보어려움·유대약화를위세효과전무로강화한오류."
    },
    {
      "code": 9,
      "verdict": "배경",
      "reason": "영역별위계가흔들려도개별위세재의효과까지없어졌다는근거는아님."
    }
  ],
  "minimal_change_test": "②를여성을얻는비용이올라확보가어려워짐으로바꾸면본문과맞음.불리한변화가모든기능의부재를뜻하지않는다.",
  "confidence": 0.96,
  "passage_group": "G251",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
