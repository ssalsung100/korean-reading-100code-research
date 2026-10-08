

<!-- luna-raw:BIO-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G440",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "전선불분명·수평조정은비조직성과동일하지않다.본문은게릴라의정교한조직을명시.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.BIQ[A]범위공식복원대기."
  ]
}
```


<!-- luna-raw:BIO-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G440",
  "sdss_seen": false,
  "general_task": "서술된전쟁양상의정확한속성대조",
  "decisive_relation": "위계·전선의불명확성과조직자체의부재를구별",
  "primary": {
    "code": 17,
    "scope": "⑤",
    "reason": "조직형태의차이를조직성자체없음으로바꾼다.수평조정은조정의한형태다."
  },
  "auxiliary": [
    {
      "code": 1,
      "scope": "⑤",
      "reason": "특정방식의부재와모든조직부재라는질적유무를구분."
    },
    {
      "code": 98,
      "reason": "게릴라에명시된정교함을비조직성으로잘못귀속."
    },
    {
      "code": 25,
      "reason": "관료적명령과수평조정이라는조직유형을구분."
    }
  ],
  "surface": [
    {
      "code": 93,
      "reason": "네트워크라는어휘가있지만통신절차나메시지전달의정확성을판정하지않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 26,
      "verdict": "국소대비후보",
      "refutation": "위계/수평의대비를조직/비조직의이항분할로바꾸면오류가된다."
    },
    {
      "code": 46,
      "verdict": "주기각",
      "refutation": "전쟁발생원인의효과를추정하는것이아니라기술된조직속성을확인한다."
    },
    {
      "code": 5,
      "verdict": "배경",
      "refutation": "전쟁의변화가주제이나새로움전체의타당성을검증하는문항은아니다."
    }
  ],
  "counterfactual": "⑤의비조직적으로를수평적으로조정되거나정교하게조직되어로바꾸면본문과맞는방향이다.상하명령이없다는하나의부정을조직부정으로확장하지않는다.",
  "confidence": 0.98
}
```
