

<!-- luna-raw:AMW-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "official_answer": 3,
  "blind_answer": 3,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "logic_without_codes": "외부 화폐 도입이 고유한 경제·혼인·유대 체계에 미친 변화를 그 사회의 맥락에서 설명한다.",
  "correction": "없음",
  "passage_group": "G251",
  "quota_status": "unavailable",
  "all_group_blind_records_before_any_group_answer_check": true,
  "original_blind_preserved": true
}
```


<!-- luna-raw:AMW-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    80
  ],
  "primary_candidates": [
    80,
    64
  ],
  "working_primary": 80,
  "unique_primary_confirmed": false,
  "auxiliary": [
    60
  ],
  "surface": [
    79
  ],
  "judgment_reason": "글쓴이가티브의고유교환규범과유대체계의맥락에서변동을파악한다는관점을복원한다.",
  "competing_codes": [
    {
      "code": 64,
      "verdict": "공동 후보",
      "reason": "내적동인·정치교체·성평등등제시되지않은논점과실제초점을구별."
    },
    {
      "code": 60,
      "verdict": "보조",
      "reason": "전통체계와외부변화의설명구조를보고글의관점을추론."
    },
    {
      "code": 79,
      "verdict": "표면",
      "reason": "여성교환서술이있어도글쓴이의성평등규범주장이제시된것은아님."
    }
  ],
  "minimal_change_test": "여성이라는소재를다른교환권리로바꾸어도고유체계변동의관점은남는다.소재만으로규범입장을부여하지않음.",
  "confidence": 0.96,
  "passage_group": "G251",
  "quota_status": "unavailable",
  "sdss_seen": false,
  "all_group_answer_check_complete": true
}
```
