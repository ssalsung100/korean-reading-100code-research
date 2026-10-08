

<!-- luna-raw:BLA-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G461",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "ⓓ는3년을,ⓔ는첩모를위한상복을요구하므로두입장모두상복을입지않아도된다는⑤가명시적주장과맞지않는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BLA-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G461",
  "minimal_logic_without_codes": "ⓓ와ⓔ 모두 특정한 복상을 요구하는데⑤는두입장이복상의무를인정하지않는다고귀속한다.",
  "primary": [
    {
      "code": 75,
      "reason": "관료별입장의실제복상처방을각주체에게귀속해공통점과차이를판정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 4,
      "reason": "어느쪽이든상복없음이라는⑤의공통귀속은ⓓ의3년만으로도반박된다."
    },
    {
      "code": 17,
      "reason": "적처지위와모친대우·복상의무를별개판단차원으로유지한다."
    },
    {
      "code": 39,
      "reason": "ⓑⓒ의지위인정과ⓒⓓ의복상여부를비교한다."
    }
  ],
  "surface": [
    {
      "code": 86,
      "reason": "1년·3년의수량차이는처방식별에쓰이나⑤의결정은기간계산보다복상유무다."
    }
  ],
  "competing_codes": [
    {
      "code": 74,
      "rejection": "동일관측의대체원인을설명하기보다규정해석에따른서로다른처방을귀속한다.사실/규범이란소재만으로배타구분하지않는다."
    },
    {
      "code": 79,
      "rejection": "복상의무가소재이나본문밖의도덕원칙으로옳은입장을선택하는과제가아니다."
    },
    {
      "code": 13,
      "rejection": "처방차이가있다고적처지위와차등복상이논리적으로양립불가하다고추론하지않는다."
    }
  ],
  "scope_limit": "ⓔ의정확한복상기간은본문이정하지않아미확정.ⓒ의미래법식비판을과거적처지위박탈로확대하지않음.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
