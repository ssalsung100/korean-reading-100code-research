

<!-- luna-raw:BLE-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G462",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "단백질없는생명체는필수작업주체의단백질한정을약화한다.양증가가비활성화로이어지는경우는양을기능증가의지표로읽는추론을약화한다.다른단백질의펩타이드질량중복은식별력을높이지않으므로ㄷ은거짓.ㄱㄴ만맞아③.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BLE-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G462",
  "minimal_logic_without_codes": "새가정들이단백질의필수작업,양과활성의연결,분자량을통한식별에주는효과를각기판정해ㄱㄴ만수용한다.",
  "primary": [
    {
      "code": 63,
      "reason": "각보기의새로운가정을수용했을때세주장의설득력이강해지는지약해지는지직접평가한다."
    }
  ],
  "auxiliary": [
    {
      "code": 36,
      "reason": "ㄱ의단백질없는생명체는필수작업의단백질한정에대한반례기능."
    },
    {
      "code": 62,
      "reason": "ㄴ은단백질양증가에서기능촉진으로이어지는관계를비활성화가능성으로약화한다."
    },
    {
      "code": 45,
      "reason": "ㄷ은서로다른단백질이같은펩타이드질량을낼수있어관측값에서원인을식별하는역대응이불확실해짐을판정한다."
    }
  ],
  "surface": [
    {
      "code": 49,
      "reason": "ㄴ에양과활성의방향이있지만문항의핵심은그새관계가후보선정논거에주는효과다."
    }
  ],
  "competing_codes": [
    {
      "code": 73,
      "rejection": "ㄱ은전제부정기능도있지만ㄴ은연결약화,ㄷ은식별특이성문제여서전체를하나의전제부정으로압축하지않는다."
    },
    {
      "code": 74,
      "rejection": "ㄷ의대체원단백질가능성은국소관련되지만ㄱㄴ까지대체가설간예측대조를요구하지않는다."
    },
    {
      "code": 11,
      "rejection": "하나의분자량으로원단백질이유일하게정해지는일대일관계를새로전제하지않는다.전체분자량패턴은추가식별정보가될수있다."
    }
  ],
  "boundary_note": "BKX는주어진비판의대상식별이었으나BLE는새가정에따른설득력효과를직접판정한다.약화와전면반증을구분한다.",
  "confidence": 0.95,
  "sdss_seen": false
}
```
