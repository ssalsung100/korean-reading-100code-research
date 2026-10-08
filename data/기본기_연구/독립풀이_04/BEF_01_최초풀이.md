

<!-- luna-raw:BEF-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G400",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "5문단 사적 소유·공동 이용의 동의 장애와 공동 소유·사적 이용의 남용",
    "6문단 사적 경작/공동 목축과 편익 사유화·손해 전가"
  ],
  "minimal_logic_without_codes": "배제권이 강하면 공동 이용이 막히고, 공동 소유의 사적 이용에서는 남용이 문제다. 두 유형을 모두 강한 배제권의 결과로 묶으면 맞지 않는다.",
  "intermediate_reasoning": [
    "① 동의 장애는 과소 이용, 공동자원 남용은 과다 이용과 대응한다.",
    "② 스미스의 문제는 같은 경지의 작은 규모 경작과 큰 규모 목축의 공존에서 발생한다.",
    "③ 공유자원 비극은 타인의 이용 배제가 강해서가 아니라 각자의 사적 이용이 자원 남용으로 이어지는 문제다.",
    "④ 반공유·반공유의 공유는 공동 이용, 공유자원의 공유는 공동 소유 자원에 대한 각자 이용이라는 대비로 읽는다.",
    "⑤ 자원 소유의 단위와 이용·효과의 단위 불일치가 동의 거부·남용·편익 집중 유인을 만든다."
  ],
  "attractive_wrong": {
    "choice": 4,
    "exact_error": "세 공유를 모두 같은 법적 공동소유의 의미로 읽으면 ④를 배척하게 된다. 원문은 사적 소유자들이 공동 이용하는 구조를 따로 제시한다."
  }
}
```
