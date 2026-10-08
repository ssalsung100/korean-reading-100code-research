

<!-- luna-raw:AIM-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G214",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "손님이라는인격화는축복과은혜의긍정시선을뒷받침한다.④은이시선이축복은혜와대비된다고관계를뒤집는다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2023__국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIN범위crop은직접검증완료",
  "barrier_verified": "AIN해소후G214blind4저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIM-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G214",
  "primary": [],
  "primary_candidates": [
    39,
    96
  ],
  "working_representative": 39,
  "auxiliary": [
    100,
    80
  ],
  "surface": [
    97
  ],
  "judgment_reason": "손님이라는인격화와축복은혜라는시선은같은긍정방향인데④은대비관계로바꿈.관계대조39와대비라는말의문맥적합96이중첩.",
  "competing_codes": [
    {
      "code": 100,
      "verdict": "보조",
      "reason": "자연요소를손님으로인격화한것은맞으므로인격화유무만으로④기각못함"
    },
    {
      "code": 80,
      "verdict": "보조",
      "reason": "화자의긍정시선을복원해대비아님을확인"
    },
    {
      "code": 96,
      "verdict": "후보",
      "reason": "상응하는평가를대비라고말한관계표현오류판독"
    },
    {
      "code": 97,
      "verdict": "특정선지",
      "reason": "①체험권유기능에는관여하지만④오류는인격화와평가의관계"
    }
  ],
  "minimal_change_test": "④ 대비되는을뒷받침하는으로고치면인격화기술은그대로두고오류해소. 표현법이맞다고후반기능해석도맞는것아님.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
