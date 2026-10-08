

<!-- luna-raw:BLP-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G466",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "동일의무·같은판정조건에서의무에맞음과어긋남은동시에성립할수없으므로①이부적절하다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BLP-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G466",
  "minimal_logic_without_codes": "의무에서비롯하면의무에맞지만그역은보장되지않으며,동일기준에서맞음과어긋남은동시에성립하지않는다.",
  "primary": [
    {
      "code": 13,
      "reason": "①은의무합치와위배를같은판정조건에서양립시키므로배제한다."
    }
  ],
  "auxiliary": [
    {
      "code": 12,
      "reason": "의무에서비롯함→의무에맞음이라는일방향포함을③에적용한다."
    },
    {
      "code": 10,
      "reason": "합치가의무동기의필요조건이지만충분조건은아님을②에서확인한다."
    },
    {
      "code": 78,
      "reason": "④에서행위의합치여부와유발동기동일성은별개다."
    }
  ],
  "surface": [
    {
      "code": 25,
      "reason": "세행위분류를그릴수있지만실제판정은포함·배타관계다."
    }
  ],
  "competing_codes": [
    {
      "code": 18,
      "rejection": "동일행위를맞으면서어긋난다고하는것은모순표상으로도가능하다.13/18유일주분리는유보하고양립불가검사를13으로대표한다."
    },
    {
      "code": 11,
      "rejection": "의무에서비롯함과합치를동치로만들면감정·이익동기의합치행위가설명되지않는다."
    },
    {
      "code": 75,
      "rejection": "경쟁학자입장의대조가아니라하나의본문이론안에서세범주의관계를분석한다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
