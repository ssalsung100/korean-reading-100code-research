

<!-- luna-raw:BKJ-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G455",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2019/2019_answer_2019_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "ㄱ은 포식 제거의 순효용이 양으로 평가되면 의무가 나올 수 있다는 본문 논증에 맞고 ㄹ은 비결과주의 평가 기준에 맞는다. ㄴ의 반비례는 없고 ㄷ은 의무의 필요 요건인 능력을 충분조건으로 뒤집는다. 따라서 ㄱ·ㄹ인 ②.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BKJ-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G455",
  "minimal_logic_without_codes": "의무를 지니는 데 능력이 필요하지만 능력이 있다는 것만으로 의무가 보장되지는 않는다. 효용 비교와 행위 자체 평가를 각 이론에 맞춰 ㄱ·ㄹ만 남긴다.",
  "primary": [
    {
      "code": 10,
      "reason": "ㄷ은 의무→능력의 필요조건을 능력→의무의 충분조건으로 뒤집는다. ㄷ 포함 여부가 선택지 소거의 중요한 분기다."
    }
  ],
  "auxiliary": [
    {
      "code": 12,
      "reason": "ㄱ의 제시된 효용 조건 적용과 ㄷ의 조건 방향 검토. 10과 같은 방향 검토를 중복 계수하지 않는다."
    },
    {
      "code": 88,
      "reason": "ㄱ은 포식 제거로 얻는 쾌락 총량과 고통 총량의 차이를 비교한다."
    },
    {
      "code": 79,
      "reason": "의무·능력의 연결이라는 의미 내용과 ㄹ의 도덕 평가를 규정한다."
    }
  ],
  "surface": [
    {
      "code": 91,
      "reason": "ㄴ의 반비례 표현은 지문이 보장하지 않는 정량 관계이다. 실제 비례 계산을 한 것으로 분류하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 2,
      "rejection": "반드시라는 양상 강화가 있지만 더 구체적인 오류는 필요조건을 충분조건으로 바꾸는 방향이다."
    },
    {
      "code": 15,
      "rejection": "ㄹ의 결과/행위 자체 기준 구분은 필요하나 ㄷ의 방향 오류까지 대신 설명하지 못한다."
    },
    {
      "code": 92,
      "rejection": "수치 없이 쾌락과 고통의 대소 및 조건 방향으로 판정하며 계산 수행은 없다."
    }
  ],
  "scope_limit": "ㄱ 수용을 모든 양의 효용 행동의 무조건적 의무화로 일반화하지 않는다. 제시된 포식 방지 대안의 비교 문맥에 한정.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
