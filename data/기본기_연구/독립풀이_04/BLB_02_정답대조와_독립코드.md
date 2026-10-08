

<!-- luna-raw:BLB-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G461",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "노씨는첩이고처는김씨·허씨두명이므로세명의처를둔경우의규정을적용한다는⑤는틀리다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BLB-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G461",
  "minimal_logic_without_codes": "혼서·혼례기준으로노씨는첩,김씨·허씨는처로판정하므로처는두명이며세처규칙의전제가없다.",
  "primary": [
    {
      "code": 15,
      "reason": "처첩구분의명시기준을적용한뒤해당규정의대상자수를정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "세여성과의관계수를규정상처의수로바꾸지않는다."
    },
    {
      "code": 3,
      "reason": "1402혼인,1413사망및최초규정,1414수정,1415소제기를분리한다."
    },
    {
      "code": 12,
      "reason": "처의수와혼인·판결시점을해당규정의조건에대입한다."
    },
    {
      "code": 31,
      "reason": "분류된처집합의원소수는2이며등장여성전체의수3과다르다.집합수와원소수의혼동으로일반화하지않는다."
    }
  ],
  "surface": [
    {
      "code": 61,
      "reason": "첫아들의집안일주관은지정기준에없는배경이다.문항작성의도추정은하지않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 8,
      "rejection": "연장자·집안주관자의우선순위를새자격기준으로추가하지않는다."
    },
    {
      "code": 4,
      "rejection": "모든여성을처로묶는범위오류로기술할수있으나그앞의법적분류기준적용이핵심이다."
    },
    {
      "code": 3,
      "rejection": "①②④판정에필수이나⑤배제는혼인일이아니라처첩분류와처의수로가능하다.정답직접경로와다른선지검토를분리한다."
    }
  ],
  "confidence": 0.95,
  "sdss_seen": false
}
```
