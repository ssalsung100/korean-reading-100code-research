

<!-- luna-raw:BCH-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G384",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "answer_source": "sealed/answer_sdss.jsonl official_answer; data/meet_questions.jsonl 정본전사",
  "verification_limit": "원 정답표 이번 세션 독립 재확인 없음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "순진한촌티와빈데의넉넉함은부족함을긍정하는평가태도공유.고장/실패의표면적결함동일성만으로⑤선택불가.",
  "original_blind_preserved": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BCH-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G384",
  "primary": [
    {
      "code": 100,
      "reason": "촌티/빈데의문맥함축을외적부족함속순진함/넉넉함의긍정가치로복원"
    }
  ],
  "auxiliary": [
    {
      "code": 23,
      "reason": "두해석의공통평가태도확인"
    },
    {
      "code": 80,
      "reason": "평가주체가대상에부여하는호감/혐오/농담을보존"
    }
  ],
  "surface": [
    {
      "code": 1,
      "reason": "빈데/모자람/실패라는결핍어만으로정서가치결정불가"
    }
  ],
  "competitors_rejected": [
    {
      "code": 69,
      "reason": "미지속성을유추하지않고각문맥함축을독립해석후비교."
    },
    {
      "code": 58,
      "reason": "공통논거를찾는것아닌공통의미찾기."
    },
    {
      "code": 18,
      "reason": "부족함을긍정함은모순이아니라평가기준의전환."
    }
  ],
  "boundary_note": "BBV와같이100은함축복원,23은복원결과비교.한연산만이유일주라고강제하지않음.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
