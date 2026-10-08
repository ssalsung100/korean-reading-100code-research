

<!-- luna-raw:BLJ-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G464",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "토지·건물분리가능성은가치평가문제의완화인데⑤는원래토지가치세에서발생하지않는공급감소를해소한다고하고이를조세저항감소로연결한다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BLJ-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G464",
  "minimal_logic_without_codes": "토지·건물의평가구분문제해결이원래없는토지공급감소를해소하고재산권저항까지줄인다는⑤의연결을정당화하지못한다.",
  "primary": [
    {
      "code": 62,
      "reason": "평가가능성개선에서공급·가격문제해소와정치적저항감소로가는근거연결의비약을배제한다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "토지단독과세와건물포함부동산과세의대상을구분한다."
    },
    {
      "code": 59,
      "reason": "서로다른도입문제를하나의해결책이모두해소한다고읽지않는다."
    },
    {
      "code": 46,
      "reason": "본문의공급비탄력성→공급불변→초과부담없음경로와⑤의가정을대조한다."
    }
  ],
  "surface": [
    {
      "code": 86,
      "reason": "③의누진세폐지혜택비교는다른선지근거이며⑤의결정에는정량계산이없다."
    }
  ],
  "competing_codes": [
    {
      "code": 73,
      "rejection": "⑤가전제한토지공급감소자체도본문과충돌하므로73은국소실질후보다.62유일주확정은유보하며잘못된전제와미입증연결을모두보존한다."
    },
    {
      "code": 63,
      "rejection": "새경험증거의강약평가가아니라제시조건에서추론되는범위를판정한다."
    },
    {
      "code": 19,
      "rejection": "가치평가의결여를보충한다고재산권침해에대한반발까지자동해소되지않는다."
    }
  ],
  "confidence": 0.92,
  "sdss_seen": false
}
```
