

<!-- luna-raw:AOF-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G263",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2013/2013_answer_2013_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "수양을전제로하는사회실천관계를역전.함양이이발에도확장됨을보존.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AOF-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 10,
      "reason": "사회실천의전제로수양을요구하는방향보존"
    }
  ],
  "auxiliary": [
    {
      "code": 8,
      "reason": "실천우선과수양선행의우선순위"
    },
    {
      "code": 3,
      "reason": "미발/이발단계"
    },
    {
      "code": 14,
      "scope": "③",
      "reason": "이발격물과함양공부의양립"
    }
  ],
  "surface": [
    {
      "code": 80,
      "reason": "인식수양소재"
    }
  ],
  "competitors": [
    {
      "code": 44,
      "refutation": "도덕실천이궁극목적이라는것은맞지만목표이므로수행순서상먼저라는결론은안됨"
    },
    {
      "code": 26,
      "refutation": "미발/이발구분을수양방법의완전배타로만들면마지막확장을놓침"
    },
    {
      "code": 12,
      "refutation": "조건문으로도기술가능하나실천에앞선필수수양에초점.10과독립논리로억지분리안함"
    }
  ],
  "counterfactual_probe": "②실천을우선시하면서를실천에앞서수양을갖추면서로고치면핵심오류완화.경과경전학습의수단관계는별도범위확인필요.",
  "boundary_status": "10/8/3필수전제·우선·시간은중첩하나목적44와다름",
  "confidence": 0.94,
  "passage_group": "G263",
  "sdss_disclosed": false
}
```
