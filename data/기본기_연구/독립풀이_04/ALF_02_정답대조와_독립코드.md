

<!-- luna-raw:ALF-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 1,
  "blind_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2023/2023_answer_언어이해정답.pdf",
  "logic_without_codes": "이익추구를헌신중심여성상으로분류한①배제.",
  "correction": "없음",
  "passage_group": "G236",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:ALF-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    15
  ],
  "primary_candidates": [
    15,
    17
  ],
  "working_primary": 15,
  "unique_primary_confirmed": false,
  "auxiliary": [
    16
  ],
  "surface": [
    79,
    83
  ],
  "judgment_reason": "가정·국가헌신/이익추구라는작품해석의기준을적용하여피양댁을좋은여성상으로귀속한①을배제.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "공동후보",
      "reason": "인물특성을어느형상범주에귀속할지판단하는같은행동."
    },
    {
      "code": 16,
      "verdict": "보조",
      "reason": "좋은여성이라는명칭의문맥상정의를확인하며일반도덕평가로바꾸지않음."
    },
    {
      "code": 79,
      "verdict": "표면",
      "reason": "당위명령을도출하는문제가아니라작품의평가기준에따른분류."
    }
  ],
  "minimal_change_test": "좋은을이익을좇는여성상으로바꾸면충돌해소.실제인물의도덕적좋고나쁨을외부에서심판하지않는다.",
  "confidence": 0.96,
  "passage_group": "G236",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
