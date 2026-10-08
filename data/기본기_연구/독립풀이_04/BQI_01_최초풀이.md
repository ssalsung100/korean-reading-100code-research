

<!-- luna-raw:BQI-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G507",
  "selected_answer": 2,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "G506_visual01의옆단에서이지문전반부를이미봄",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "대한광복회설명",
      "evidence": "전제군주제폐지와민주공화독립국건설,나라에왕이없으므로민국을세웠다고진술."
    },
    {
      "location": "신한혁명당설명",
      "evidence": "독립전쟁을위한군비·중국동맹·독일보증을추진하며외국지원에유리한제정을표방."
    }
  ],
  "minimal_logic_without_codes": "대한광복회는새정부로공화제를선택했으므로군주를두는입헌군주제와구분된다.②가가장명확하게지지된다.",
  "intermediate_reasoning": [
    "① 신한혁명당의제정선택은외국지원에유리하다는이유이고황제주권이라는근거로서술되지않았다.이상설도인민을상전으로본다.",
    "③ 신한혁명당은제정을표방했으므로제정부정이라는공통성은틀린다.",
    "④ 두단체모두군비·독립군·무력투쟁을준비했다.",
    "⑤ 대한광복회에일본의국제고립활용이명시되지만신한혁명당도일본을상대로한전쟁과외국의지원을활용하려했다.이를대한광복회만의명확한차이로단정하기어렵다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "한단체설명에고립이라는표현이있다는것만으로다른단체의국제정세활용을배제한독점적차이를만든다."
  },
  "scope_limit": "신한혁명당에도국제고립이라는동일표현이직접있다고기록하지않는다.⑤배제는서술상차이를독점적전략차이로바꾸기어렵다는독해이며②의명시근거를우선한다."
}
```
