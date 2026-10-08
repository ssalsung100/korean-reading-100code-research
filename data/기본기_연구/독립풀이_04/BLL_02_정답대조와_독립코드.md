

<!-- luna-raw:BLL-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G465",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "영원주의와조건부결정론은서로다른시간존재관을가지지만과거로가는시간여행의가능성을함께인정하므로③이맞는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BLL-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G465",
  "minimal_logic_without_codes": "영원주의와조건부결정론은시간존재에대한근거가다르지만과거여행가능이라는결론을공유한다.",
  "primary": [
    {
      "code": 39,
      "reason": "비교항목을과거시간여행가능성으로고정해두입장의공통점을찾는다."
    }
  ],
  "auxiliary": [
    {
      "code": 75,
      "reason": "시간존재관과여행가능성을각입장에정확히귀속한다."
    },
    {
      "code": 81,
      "reason": "과거·현재·미래의실재여부를정신적표상과동일시하지않고입장별전제로보존한다."
    },
    {
      "code": 2,
      "reason": "시간여행가능성에대한견해를실제여행발생이나필연성으로바꾸지않는다."
    }
  ],
  "surface": [
    {
      "code": 23,
      "reason": "공통결론을교집합으로표상가능하지만별도집합계산은없다."
    }
  ],
  "competing_codes": [
    {
      "code": 74,
      "rejection": "두입장의대체설명구조는있지만새관측이각가설을지지하는효과를판정하지않는다."
    },
    {
      "code": 13,
      "rejection": "시간존재관이충돌한다고여행가능성의결론까지항상반대인것은아니다."
    },
    {
      "code": 3,
      "rejection": "과거·미래어휘가있어도정답은연대순서계산보다입장간동일결론의확인이다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
