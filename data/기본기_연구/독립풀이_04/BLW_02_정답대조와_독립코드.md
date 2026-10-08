

<!-- luna-raw:BLW-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G468",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "B입장에서연구를사용했다는사실은편견위험을증가시키는당사자적극대변자를선정했다는추론을뒷받침하지않고오히려그런위험을배제하는기준과어긋난다.③이부적절하다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true,
  "source_scope_verified": "公式crop직접확인:[A]예시한문단,[B]마지막한문단.잘못된초기부록범위는정정됨."
}
```


<!-- luna-raw:BLW-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G468",
  "minimal_logic_without_codes": "세입장의채택조건과배제조건을사안별로적용한다.B의증거채택에서당사자적극대변자라는속성을추론할수없다.",
  "primary": [
    {
      "code": 15,
      "reason": "일반적승인·관련성·편견예외·신뢰성이라는다른증거채택기준을적용한다."
    }
  ],
  "auxiliary": [
    {
      "code": 10,
      "reason": "A의채택에는전문가일반적승인이필요함을①②에적용한다."
    },
    {
      "code": 24,
      "reason": "B는관련성이있어도편견가능성등배제사유가있으면채택하지않는다."
    },
    {
      "code": 12,
      "reason": "C의관련성∧신뢰성→채택을⑤에적용할때관련성이주어진문맥을유지한다."
    },
    {
      "code": 62,
      "reason": "B의연구채택→연구자가피해자입장을적극대변한다는③의연결에근거가없다."
    }
  ],
  "surface": [
    {
      "code": 63,
      "reason": "증거의활용기준에관한문제이며새증거가원소송주장을얼마나강화하는지판정하지않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 73,
      "rejection": "피해발생사실이나나이테자료자체의참거짓을부정하는것이아니라채택의조건을읽는다."
    },
    {
      "code": 66,
      "rejection": "⑤를형식적대우로재기술가능하나관련성전제를빠뜨리면미채택에서불신뢰만단독도출할수없다.12와같은단계를중복계수하지않는다."
    },
    {
      "code": 79,
      "rejection": "법원의규칙을적용하는것이지증거규칙의도덕적정당성을새로평가하지않는다."
    }
  ],
  "remaining_uncertainty": "⑤는관련성이충족된다는문맥전제에조건부로성립한다.일반적인미채택자료전체에신뢰성실패를귀속하지않는다.",
  "confidence": 0.92,
  "sdss_seen": false
}
```
