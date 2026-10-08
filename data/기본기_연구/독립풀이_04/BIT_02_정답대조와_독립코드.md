

<!-- luna-raw:BIT-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G441",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "오타의정상읽기는채워넣기에부합하며판단독립감각의특유한지지근거는아니다.양립가능성과지지력을구분한다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외및BIT지지/확정구분유지."
  ]
}
```


<!-- luna-raw:BIT-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G441",
  "sdss_seen": false,
  "general_task": "관찰사례의이론별설명과지지근거판별",
  "decisive_relation": "채워넣기와양립하는정상읽기사례에서독립감각의지지를곧바로도출하지않음",
  "primary": {
    "code": 63,
    "scope": "④",
    "reason": "주어진사례가비개념주의의판단독립감각주장을지지할근거인지평가한다."
  },
  "auxiliary": [
    {
      "code": 62,
      "scope": "④",
      "reason": "오타보정읽음과감각·판단의독립성사이직접지지연결이부족."
    },
    {
      "code": 75,
      "scope": "①~⑤",
      "reason": "각이론이받아들이는감각/인지관계를보존."
    },
    {
      "code": 80,
      "reason": "감각의발생과그내용을알아챔을구분."
    },
    {
      "code": 2,
      "scope": "⑤",
      "reason": "시각영역활성이자료로활용가능함과감각동일성을완전히보장함을분리."
    }
  ],
  "surface": [
    {
      "code": 18,
      "reason": "(다)가비개념주의와논리적으로절대양립불가라는주장을요구하지않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 14,
      "verdict": "보조구분축",
      "refutation": "이론과사례가양립할수있다는것은그이론을독립적으로지지한다는것과다르다."
    },
    {
      "code": 36,
      "verdict": "주기각",
      "refutation": "비개념주의전체를거짓으로만드는결정적반례로(다)를확정하지않고지지근거의적합성만판정한다."
    },
    {
      "code": 43,
      "verdict": "주기각",
      "refutation": "(라)에비교관찰이있으나실험설계의통제변수를수정하는문항은아니다."
    }
  ],
  "counterfactual": "(다)에서실제오타의시각정보가인지이전단계에독립적으로표상되었다는추가증거가주어지면비개념주의지지연결은강해질수있다.현재정상읽기결과만으로그독립성을확정하지않는다.",
  "unresolved": "⑤의뇌활성자료는내용동일성의충분증명이아니며④의배제는이론적양립불가확정이아니다.",
  "confidence": 0.96
}
```
