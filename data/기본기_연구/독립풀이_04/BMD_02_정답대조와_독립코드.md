

<!-- luna-raw:BMD-answer_check-20261003-01 -->
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
  "minimal_logic_without_codes": "형식적으로같은경우를같게대우하는규칙도내용이나부류구분에따라불평등한결과를낼수있으므로④가맞는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BMD-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G471",
  "minimal_logic_without_codes": "규칙의일관된적용만으로그내용에따른실질적평등까지보장하지않음을④에서확인한다.",
  "primary": [
    {
      "code": 62,
      "reason": "형식적정의충족→실질적정의보장이라는충분성연결을부정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 15,
      "reason": "운영의공평성과규칙내용의적절성이라는다른판단기준을분리한다."
    },
    {
      "code": 4,
      "reason": "유사한조건의사람에대한같은대우를모든사람의동일대우로확대하지않는다."
    },
    {
      "code": 2,
      "reason": "불평등할수있다는가능성과반드시불평등하다는주장을구분한다."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "정의의규범적소재가있지만새규범을정립하는것보다제시된조건의보장범위를판독한다."
    }
  ],
  "competing_codes": [
    {
      "code": 10,
      "rejection": "형식적정의가충분하지않다는것만으로그것이실질정의의필요조건이라고새로확정하지않는다."
    },
    {
      "code": 13,
      "rejection": "형식적정의와실질적불평등은양립가능할수있으므로무조건배타로두지않는다."
    },
    {
      "code": 86,
      "rejection": "평등의양적차이를계산하지않고규칙과결과의관계강도를확인한다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
