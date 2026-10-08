

<!-- luna-raw:BLY-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G469",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2021/2021_answer_2021_LEET_언어이해_정답표_배포용.hwp",
  "minimal_logic_without_codes": "④는실제축적기록에서출발하는마이닝을예상로그에적용하는모델중심기법으로바꾼다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BLY-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G469",
  "minimal_logic_without_codes": "실제축적된로그에서출발하는분석을예상로그에적용하는모델중심기법으로바꾼④를배제한다.",
  "primary": [
    {
      "code": 45,
      "reason": "분석의입력과모델·데이터간처리방향을보존한다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "실제수행기록과가상적예상데이터의유형을구분한다."
    },
    {
      "code": 3,
      "reason": "로그수집이전의모델중심분석과로그확보이후의분석을구분한다."
    },
    {
      "code": 16,
      "reason": "향상에는기존모델수정과발견모델확장이모두포함된다는정의를⑤에적용한다."
    }
  ],
  "surface": [
    {
      "code": 63,
      "reason": "준수여부검증이있지만논증의설득력강약과같은검사가아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 74,
      "rejection": "기존모델과실제로그의차이를경쟁가설간새증거평가로바꾸지않는다.본문은진단·개선절차를설명한다."
    },
    {
      "code": 10,
      "rejection": "비정형업무분석가능성을인정하기위해정형성이라는불필요요건을기각하지만④의직접오류는입력·분석유형의교환이다."
    },
    {
      "code": 49,
      "rejection": "빈도와복잡도라는양은있지만④는증감방향문제가아니다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
