

<!-- luna-raw:AJE-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G219",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "바른듯삿된것은실상있는소리의범주에가능하지만좋은소리는실제로바름에합당해야한다.④은상위범주의가능성을하위의좋은소리에옮김.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G219전체blind5후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJE-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G219",
  "primary": [],
  "primary_candidates": [
    10,
    17,
    25
  ],
  "working_representative": 10,
  "auxiliary": [
    16,
    23
  ],
  "surface": [
    22
  ],
  "judgment_reason": "좋은소리는듣기좋고글로쓰이고바름에합당해야함.상위실상소리의삿됨가능성을하위좋은소리에옮기면필요요건위반.요건10·범주귀속17·단계분류25중첩.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "후보",
      "reason": "상위범주의삿된가능성을좋은소리에잘못귀속"
    },
    {
      "code": 25,
      "verdict": "후보",
      "reason": "실상소리와좋은소리의분류단계구별"
    },
    {
      "code": 22,
      "verdict": "주 기각",
      "reason": "상위일부의속성을모든하위에상속할수없음.보편속성상속과부분가능성전이는다름"
    },
    {
      "code": 23,
      "verdict": "보조",
      "reason": "여러요건의동시충족이좋은소리선별근거"
    }
  ],
  "minimal_change_test": "④대상을좋은소리에서실상있는소리로바꾸면바른듯삿됨가능성이허용됨.좋은소리정의에서바름요건삭제시에도현재반증근거사라짐.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
