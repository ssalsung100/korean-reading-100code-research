

<!-- luna-raw:BME-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G471",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2021/2021_answer_2021_LEET_언어이해_정답표_배포용.hwp",
  "minimal_logic_without_codes": "롤스의도덕적인격요건이없다는것은해당도덕관계의적용밖이라는뜻이지부도덕한인물이라는부정평가가아니므로①이틀리다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BME-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G471",
  "minimal_logic_without_codes": "도덕적인격의도덕적은도덕관계의적용범위에관한말이지훌륭함의평가가아니므로요건부재를부도덕으로바꿀수없다.",
  "primary": [
    {
      "code": 16,
      "reason": "본문이제한한도덕적인격의의미를가치평가의도덕적/부도덕과구별한다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "도덕관계의대상이아님과그대상에게내리는부정적평가를분리한다."
    },
    {
      "code": 15,
      "reason": "롤스의최소영역자격과싱어의감수능력·이익강도기준을구별한다."
    },
    {
      "code": 14,
      "reason": "평등한고려자격과강도에따른차등대우가싱어에서양립함을④에적용한다."
    }
  ],
  "surface": [
    {
      "code": 96,
      "reason": "같은도덕적어휘의문맥의미를읽지만그의미는본문이명시적으로정의했다."
    }
  ],
  "competing_codes": [
    {
      "code": 18,
      "rejection": "단순히도덕적의부정을부도덕으로놓으면서로다른의미축을같은명제와부정으로오해한다."
    },
    {
      "code": 83,
      "rejection": "사실/가치문제와관련될수있으나①의구체오류는자격개념과부정평가의의미교환이다."
    },
    {
      "code": 86,
      "rejection": "능력정도차이는다른선지에서인정되지만①은정도대소가아닌개념적용의종류문제다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
