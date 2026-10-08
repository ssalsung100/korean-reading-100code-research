

<!-- luna-raw:BNI-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G481",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "사물이 지성의 설계나 이상에 못 미친다는 것과 그 사물에 관한 명제가 사실에 맞는다는 것은 다른 판정이다. 그 사물의 실제 상태를 맞게 말하면 참 명제의 주어일 수 있으므로①이다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "exposure_note": "이전 crop의 지문 일부 노출 이력 보존; 정답 일치를 strict-blind 성과로 집계하지 않는다."
}
```


<!-- luna-raw:BNI-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G481",
  "minimal_logic_without_codes": "설계 기준에 못 맞춘 사물도 실제 성질을 맞게 말하는 명제의 주어가 될 수 있다. 사물의 참됨 실패에서 그 사물을 언급한 모든 명제의 거짓을 도출하지 않는다.",
  "primary": [
    {
      "code": 17,
      "reason": "사물 자체에 대한 판정과 그 사물을 주어로 하는 명제에 대한 판정을 교환하지 않는 것이①의 중심이다."
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "오르토테스와 베리타스의 적용 대상 및 정의 조건을 분해한다."
    },
    {
      "code": 10,
      "reason": "② 인식에는 좋음의 이데아가 필요하고④ 진릿값을 갖는 언표에는 사실성 주장이 필요하다."
    },
    {
      "code": 80,
      "reason": "실제 연결에 대한 명제의 인식적 적합성을 판단한다."
    },
    {
      "code": 2,
      "reason": "①은 논리적 가능성이지 아퀴나스의 세계관 아래 그런 사물의 현실적 존재를 확정한 말이 아니다."
    }
  ],
  "surface": [
    {
      "code": 81,
      "reason": "존재론적 진리라는 배경은 직접 관련되지만①을 정하는 작업은 두 판정 수준의 분리다."
    }
  ],
  "competing_codes": [
    {
      "code": 41,
      "rejection": "사물이 명제의 주어로 표현된다고 사물과 명제가 동일 종류의 부분/전체가 되는 것은 아니다. 물건의 거짓을 문장의 거짓으로 옮기는 것은 구성의 오류로 자동 분류할 수 없다."
    },
    {
      "code": 18,
      "rejection": "하나의 명제를 참이면서 거짓이라고 한 것이 아니라 다른 대상·판정 기준이므로 모순이 아니다."
    },
    {
      "code": 21,
      "rejection": "④에서 주어·술어 연결만 충분화하는 오류를 지적할 수 있지만 긍정 정답①의 두 차원 분리를 전부 대체하지 못한다."
    },
    {
      "code": 33,
      "rejection": "③의 없는 연결을 있다고 언표함은 이중부정 제거가 아니라 현실 연결과 주장 연결의 불일치다."
    }
  ],
  "confidence": 0.92,
  "sdss_seen": false,
  "unresolved": "사태적 거짓의 현실 사례를 본문에서 확보한 것으로 과대기록하지 않는다.①은 차원의 구별에 관한 가능성이다."
}
```
