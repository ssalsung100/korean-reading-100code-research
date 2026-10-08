

<!-- luna-raw:BLH-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G463",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "입술을꽉다무는행동은증여를명시적으로거부하는장면인데⑤는증여윤리를의식적으로수용하려는태도로뒤집는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BLH-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G463",
  "minimal_logic_without_codes": "돈을받지않겠다는말과입술을다무는동작은그시점의거부다.나중마지못한수령을이전의적극수용으로소급하지않는다.",
  "primary": [
    {
      "code": 78,
      "reason": "발화와행동을통해계봉의해당시점태도가수용인지거부인지를판독한다."
    }
  ],
  "auxiliary": [
    {
      "code": 97,
      "reason": "받을수없소라는명시적거부발화가동작의기능을확정한다."
    },
    {
      "code": 3,
      "reason": "처음거부와뒤의마지못한수령을구별한다."
    },
    {
      "code": 14,
      "reason": "고마움·기쁨과자존심에따른무색함·거부는같은인물에게양립가능하다."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "증여윤리라는표현이있지만선지는특정인물의태도를사실과맞추는문제다."
    }
  ],
  "competing_codes": [
    {
      "code": 100,
      "rejection": "입술을다무는실제동작을문맥없이증여윤리수용의상징으로읽지않는다.명시발화가해석을제한한다."
    },
    {
      "code": 80,
      "rejection": "타인의뜻에대한추측과실제동기를분리하는보조관점은있으나⑤의직접오류는행동태도의반전이다."
    },
    {
      "code": 13,
      "rejection": "감사하면거부할수없다는양립불가를전제하지않는다.장면은상반감정의동시존재를명시한다."
    }
  ],
  "scope_limit": "승재의오해가능성추측을실제사심의존재증거로확정하지않음.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
