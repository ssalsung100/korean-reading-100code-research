

<!-- luna-raw:BLI-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G464",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "개량에의한수익을제외한토지수익을불로소득으로환수하자는주장이므로개량되지않은토지임대료를불로소득으로본다는①이맞는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BLI-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G464",
  "minimal_logic_without_codes": "개량기여를제외한토지임대수익을불로소득으로환수한다는정의를①에대응한다.",
  "primary": [
    {
      "code": 16,
      "reason": "불로소득과과세대상의정의에서노력·기여에따른개량수익의제외를유지한다."
    }
  ],
  "auxiliary": [
    {
      "code": 40,
      "reason": "사용·처분·수익의권리구성요소중어디에제약이붙는지구분한다."
    },
    {
      "code": 62,
      "reason": "④의효율성에서공정성으로가는인과연결은각각의별도장점설명만으로확보되지않는다."
    },
    {
      "code": 4,
      "reason": "⑤는토지밖자유시장옹호라는범위를모든경제규제로확대한다."
    }
  ],
  "surface": [
    {
      "code": 88,
      "reason": "세금의비용과효율성은소재지만①을고르는데비용편익수치비교는없다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "rejection": "④의두장점사이에인과를새로만들면오류다.정답①은정의범위의일치이다."
    },
    {
      "code": 15,
      "rejection": "과세기준적용으로같은행동을기술가능해16과의유일주우선은유보.16은불로소득개념의포함범위를대표한다."
    },
    {
      "code": 79,
      "rejection": "조지의규범입장을귀속하지만독자가새로운조세당위를판단하지않는다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
