

<!-- luna-raw:AID-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G211",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "백성의애도와윤리적지지는있지만태보가국운을실제로회복한사건은없다.⑤은도덕적고양을현실적성공으로바꾼다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2022__국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조. AIC 공식PDF범위직접검증과정답셀직접대조는구별",
  "barrier_verified": "AICscope해소후유효blind4개모두저장한다음G211첫answer공개; SDSS미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AID-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G211",
  "primary": [],
  "primary_candidates": [
    17,
    64
  ],
  "working_representative": 17,
  "auxiliary": [
    39,
    2
  ],
  "surface": [
    63,
    46
  ],
  "judgment_reason": "도덕적영웅의인정과실제국운회복의성공은다르다.⑤은 윤리적책무의인정을 현실적성과에 옮겨 귀속17/근거없는성과추가64가동일오류를검출.",
  "competing_codes": [
    {
      "code": 64,
      "verdict": "후보",
      "reason": "작품에국운회복사건이없고보기는대결패배를명시"
    },
    {
      "code": 2,
      "verdict": "보조후보",
      "reason": "사후염원과현실성취의양상차가배경에있으나⑤은소망을직접인용한것이아닌성과범주추가"
    },
    {
      "code": 63,
      "verdict": "표면",
      "reason": "백성들의지지·추대는사건내평가이며어떤논증을강화하는새증거의가치를묻는것아님"
    },
    {
      "code": 46,
      "verdict": "주 기각",
      "reason": "민심이영웅추대를낳는경로보다실제회복이라는전제사건이주어지지않음"
    }
  ],
  "minimal_change_test": "⑤ 국운을회복한영웅을윤리적책무를지킨영웅으로바꾸면보기와부합. 다른정권의회복사건을외부역사로보충하지않음.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
