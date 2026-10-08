

<!-- luna-raw:BLU-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G468",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "이미생성된과거기록만관측하더라도그기록의경향·관계로미래를예측할수있으므로①은본문의활용방식을부정한다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true,
  "source_scope_verified": "公式crop직접확인:[A]예시한문단,[B]마지막한문단.잘못된초기부록범위는정정됨."
}
```


<!-- luna-raw:BLU-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G468",
  "minimal_logic_without_codes": "관측자료가과거의기록이라는사실에서그자료를이용한미래예측이불가능하다는결론은따라오지않는다.",
  "primary": [
    {
      "code": 62,
      "reason": "과거자료만관측가능→미래변동예측불가능이라는①의근거연결을부정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 45,
      "reason": "입력자료의시점과추론으로얻는출력내용의시점을구분한다."
    },
    {
      "code": 3,
      "reason": "이미형성된기록과아직발생하지않은대상의시간범위를유지한다."
    },
    {
      "code": 2,
      "reason": "예측가능성의부정을배제하며예측이언제나정확하다는필연명제로바꾸지않는다."
    }
  ],
  "surface": [
    {
      "code": 43,
      "reason": "④의차로변/배후지차이는원인추정의국소비교후보이나①의직접오류와는다르다."
    }
  ],
  "competing_codes": [
    {
      "code": 10,
      "rejection": "미래를예측하려면미래의관측자료가필수라는숨은전제를드러낼수있어62와국소중첩.독립필수연산으로중복계수하지않는다."
    },
    {
      "code": 77,
      "rejection": "과거기록에서일반적경향을도출할수있지만구체표본을일반화하는타당성검사까지요구되지는않는다."
    },
    {
      "code": 49,
      "rejection": "나이테폭과강수량관계는자료해석의배경이나①은관측과예측의관계를혼동한다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
