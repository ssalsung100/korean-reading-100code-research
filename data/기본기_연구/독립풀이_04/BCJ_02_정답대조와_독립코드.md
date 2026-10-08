

<!-- luna-raw:BCJ-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G384",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "answer_source": "sealed/answer_sdss.jsonl official_answer; data/meet_questions.jsonl 정본전사",
  "verification_limit": "원 정답표 이번 세션 독립 재확인 없음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "남의것을마구취하는문맥과빌어얻는구걸은행위방식이다름.사전정의전문은미확인.정본답일치가사전풀이독립검증을뜻하지않음.",
  "original_blind_preserved": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BCJ-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G384",
  "primary": [
    {
      "code": 96,
      "reason": "문맥속낯선어휘를실제행위방식과대응해풀이가맞는지검사"
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "욕심껏취함과남에게빌어얻음의행위범주구별"
    },
    {
      "code": 16,
      "reason": "어휘뜻의구별성분을검사한다는국소층위"
    }
  ],
  "surface": [
    {
      "code": 100,
      "reason": "물외밭/뼈를곤돈의비유적대조가문맥근거이나표적은걸태질뜻풀이"
    }
  ],
  "competitors_rejected": [
    {
      "code": 97,
      "reason": "발화자가어떤의도로말했는지보다어휘행위의뜻판별."
    },
    {
      "code": 99,
      "reason": "대명사/지시어대용대상복원아님."
    },
    {
      "code": 78,
      "reason": "욕심이라는동기는문맥에있지만인물행위의동기를설명하는과제보다행위어뜻대응."
    }
  ],
  "boundary_note": "96의광범위한일상어분류만으로충분한세부연산이아니므로행위방식차이를필수기록.완전한사전정의검증과원문추론을구별.",
  "confidence": 0.86,
  "sdss_seen": false
}
```
