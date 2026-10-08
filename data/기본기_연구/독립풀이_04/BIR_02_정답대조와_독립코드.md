

<!-- luna-raw:BIR-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G441",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "감각과판단의분리여부는다르지만판단이개념적절차라는점은공유한다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외및BIT지지/확정구분유지."
  ]
}
```


<!-- luna-raw:BIR-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G441",
  "sdss_seen": false,
  "general_task": "대립견해가공유하는주장찾기",
  "decisive_relation": "감각의개념성논쟁과판단의개념성합의를분리",
  "primary": {
    "code": 23,
    "scope": "②",
    "reason": "두견해의공통내용이판단과정의개념성이라는교집합임을확인한다."
  },
  "auxiliary": [
    {
      "code": 75,
      "reason": "비개념/개념주의의주장을각각보존."
    },
    {
      "code": 80,
      "reason": "감각경험과인식판단의단위를구분."
    },
    {
      "code": 17,
      "scope": "④",
      "reason": "감각에대한오류논의와판단·추론무오류를바꾸지않는다."
    }
  ],
  "surface": [
    {
      "code": 3,
      "scope": "③",
      "reason": "감각선행은한견해만의관계이며문항전체의공통판정이아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 39,
      "verdict": "국소중첩",
      "refutation": "공통점비교라는행동은23과겹친다.번호차이만으로별개필수연산으로세지않는다."
    },
    {
      "code": 74,
      "verdict": "통합군보조",
      "refutation": "경쟁견해지만새관측예측을산출하지않고공통명제를대조한다."
    },
    {
      "code": 18,
      "verdict": "주기각",
      "refutation": "대립한다고모든주장이모순되는것은아니다.공통요소를찾는것이핵심이다."
    }
  ],
  "counterfactual": "②의판단과정을감각경험으로바꾸면두견해의핵심쟁점이되어공통명제가아니다.대상의단어하나가판정을바꾼다.",
  "confidence": 0.98
}
```
