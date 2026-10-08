

<!-- luna-raw:BLC-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G462",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "정상세포와암세포는분화·단백질조합및양변화에따라단백질체정보가동일하지않으므로⑤가맞는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BLC-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G462",
  "minimal_logic_without_codes": "정상에서암으로분화하면단백질조합과양이변하므로두단백질체정보전체가같지않다.",
  "primary": [
    {
      "code": 5,
      "reason": "분화에따른단백질체정보의변화를⑤에대응한다."
    }
  ],
  "auxiliary": [
    {
      "code": 29,
      "reason": "②의유전체·전사체·단백질체정보포함방향을유지한다."
    },
    {
      "code": 4,
      "reason": "①의일부RNA→모든RNA번역확대를배제한다."
    },
    {
      "code": 17,
      "reason": "인간간세포와생쥐간세포를같은기관명만으로동일정보대상으로합치지않는다."
    }
  ],
  "surface": [
    {
      "code": 46,
      "reason": "분화·기능의원인설명이있지만⑤는본문이명시한조합변화의확인이다."
    }
  ],
  "competing_codes": [
    {
      "code": 40,
      "rejection": "정보의포함과세포의부분성은배경이나정상/암의단백질체동일성판정은분화에따른변화다."
    },
    {
      "code": 13,
      "rejection": "두단백질체가동일하지않다고공통단백질이전혀없다는배타성을도출하지않는다."
    },
    {
      "code": 86,
      "rejection": "단백질양이달라질수있으나특정량의수치비교를하지않는다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
