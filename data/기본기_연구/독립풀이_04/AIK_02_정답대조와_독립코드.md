

<!-- luna-raw:AIK-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G213",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "치료목적을넘어금지산책자체를원하는변화는자유의지심화이다.③은변질의부정적어감만따라자유필요망각과목적훼손으로뒤집는다.",
  "official_answer_source": "자료/평가원_정답표/원본/모의평가/2023_9월_국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님",
  "barrier_verified": "G213blind4저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIK-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G213",
  "primary": [],
  "primary_candidates": [
    96,
    17,
    100
  ],
  "working_representative": 96,
  "auxiliary": [
    5,
    39
  ],
  "surface": [
    44,
    63
  ],
  "judgment_reason": "변질은여기서치료를넘어자유실천의욕이심화됨. 부정적일상어감96만따라해석방향을뒤집으면보기의상징대응100·내용귀속17을함께깨뜨림.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "후보",
      "reason": "산책성격변화를자유의지심화대신자유망각에귀속"
    },
    {
      "code": 100,
      "verdict": "후보",
      "reason": "통증·산책·날개의보기상징대응을따라변화방향판정"
    },
    {
      "code": 44,
      "verdict": "특정오답 표면",
      "reason": "목적훼손이라는말은선지가잘못도입한해석. 본문은치료목적을넘는새동기의형성"
    },
    {
      "code": 63,
      "verdict": "주 기각",
      "reason": "비판이라는선지말만으로논증약화코드부여불가. 보기의해석기준과사건대응을검사"
    }
  ],
  "minimal_change_test": "③ 자유필요망각·목적훼손을치료를넘어자유실천의욕심화로바꾸면맥락복원. 변질이라는표현자체를삭제해도통증없어도계속산책하고싶다는근거가남음.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
