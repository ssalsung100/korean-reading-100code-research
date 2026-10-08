

<!-- luna-raw:BMF-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G471",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2021/2021_answer_2021_LEET_언어이해_정답표_배포용.hwp",
  "minimal_logic_without_codes": "병의일시적능력상실은잠재적도덕능력의영구적부재와다르므로롤스가비평등대상으로보리라는④는틀리다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BMF-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G471",
  "minimal_logic_without_codes": "일시적으로실현하지못하는것과잠재능력의영구적부재는다르다.병은잠재능력을요건으로삼는롤스기준에서곧바로배제되지않는다.",
  "primary": [
    {
      "code": 2,
      "reason": "가능능력과현재실현여부의양상을구분한다."
    }
  ],
  "auxiliary": [
    {
      "code": 10,
      "reason": "롤스의필요요건은잠재능력이며현재행사능력을새필수요건으로추가하지않는다."
    },
    {
      "code": 15,
      "reason": "갑·을·병을각철학자의서로다른최소자격기준에대입한다."
    },
    {
      "code": 3,
      "reason": "회복불가능·선천적결여·일시상실이라는지속조건을구별한다."
    }
  ],
  "surface": [
    {
      "code": 86,
      "reason": "②에서고통의상대강도를비교하지만④의결정은능력실현의양상이다."
    }
  ],
  "competing_codes": [
    {
      "code": 24,
      "rejection": "병을임의의예외로봐주는것이아니라애초의잠재능력기준을그대로적용한다."
    },
    {
      "code": 19,
      "rejection": "실제능력을보충해야자격이생긴다는해결책을추가하지않는다."
    },
    {
      "code": 5,
      "rejection": "상실이라는변화만보지않고잠재성의지속과현재실현의부재를분리해야한다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
