

<!-- luna-raw:BLS-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G467",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "ㄱ은후방분사후더멀리도달하는큰타원진입이라참.ㄴ은각에너지가일정하다는주장이라거짓.ㄷ은에너지증가로최대도달거리가커져최대중력위치에너지도커지므로참.ㄱㄷ인③.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true,
  "background_knowledge_limit_preserved": "별도추가없음"
}
```


<!-- luna-raw:BLS-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G467",
  "minimal_logic_without_codes": "분사후중력만작용하면K+U가일정하지만각항은거리변화에따라반대로변한다.분사로전체에너지를늘린경우최대도달거리와최대U도늘어난다.",
  "primary": [
    {
      "code": 85,
      "reason": "ㄴ의합일정조건을각항일정으로오독하는문제를막고K와U의상보적변화를유지한다."
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "ㄱㄷ의후방분사→에너지증가→큰타원·먼거리도달경로."
    },
    {
      "code": 49,
      "reason": "지구중심거리증가에따른U수치증가방향."
    },
    {
      "code": 43,
      "reason": "분사중전체에너지변화와분사후중력만작용하는보존구간의조건을분리한다."
    }
  ],
  "surface": [
    {
      "code": 84,
      "reason": "U의분수식형태는있지만ㄱㄷ은본문의거리-에너지증감문장으로판정가능하다."
    }
  ],
  "competing_codes": [
    {
      "code": 40,
      "rejection": "운동·위치에너지가전체의구성항이라는기술만으로는합보존에따른반대변화관계를특정하지못한다."
    },
    {
      "code": 91,
      "rejection": "K와U의합이고정된관계는단순한정비례·반비례식으로동일시하지않는다."
    },
    {
      "code": 5,
      "rejection": "보존과변화의명명보다보존되는합과변하는항을구분하는것이구체근거다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
