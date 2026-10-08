

<!-- luna-raw:BIW-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G442",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "본문의지나친Wnt불활성기전을완화하는방향은β카테닌증가이다.원인경로안의정성예측으로한정한다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외및본문기전범위유지."
  ]
}
```


<!-- luna-raw:BIW-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G442",
  "sdss_seen": false,
  "general_task": "신호경로의병적변화와조절방향추론",
  "decisive_relation": "Wnt불활성이원인인경우그작용을회복하는방향은β카테닌증가",
  "primary": {
    "code": 49,
    "scope": "②",
    "reason": "Wnt작용과β카테닌농도·뼈형성의방향을연결한다."
  },
  "auxiliary": [
    {
      "code": 59,
      "scope": "②",
      "reason": "본문의문제원인을완화하는대책방향을추론."
    },
    {
      "code": 46,
      "scope": "③④⑤",
      "reason": "APC복합체·인산화·분해의경로위치를보존."
    },
    {
      "code": 50,
      "scope": "④⑤",
      "reason": "복합체결함이나인산화불가가분해경로를막는다."
    },
    {
      "code": 52,
      "scope": "⑤",
      "reason": "β카테닌감소경로의억제는농도상승및복제유지쪽이다."
    }
  ],
  "surface": [
    {
      "code": 54,
      "reason": "실제약물의모든효능을충분보장하는일반명제가아니라본문기전상방향이다."
    }
  ],
  "competing_codes": [
    {
      "code": 19,
      "verdict": "②보조가능",
      "refutation": "부족한신호의보완이라는표상은가능하지만정확한정답은어느단백질농도가어느방향으로변하는지로판정한다."
    },
    {
      "code": 20,
      "verdict": "주기각",
      "refutation": "여러치료수단을대체가능성으로비교하는문항은아니다."
    },
    {
      "code": 43,
      "verdict": "주기각",
      "refutation": "실험변수통제설계를평가하는것이아니라주어진경로에서개입방향을추론한다."
    }
  ],
  "counterfactual": "APC결함을고치는수리작용이따로주어졌다면④농도회복가능성을검토할수있지만Wnt추가에는그런기능이명시되지않았다.정상물질이라는말로복구효과를추가하지않는다.",
  "unresolved": "정상범위회복과과도한활성의위험은다르며②를현실투약의무제한활성권고로확장하지않는다.",
  "confidence": 0.98
}
```
