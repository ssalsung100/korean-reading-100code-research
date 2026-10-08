

<!-- luna-raw:AXG-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G342",
  "first_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "물의 과냉각은 이력 특성 없이 가능하고 우무의 상태에는 이력 정보가 필요하다. 제한된 과냉각을 전 온도 영역의 상전이 불가능으로 확장할 수 없다.",
  "answer_source": "자료/LEET_언어이해/원본/2014/2014_answer_2014학년도_법학적성시험_언어이해_정답표.hwp",
  "group_barrier": "all_group_blind_records_before_any_group_answer_check 확인",
  "strict_blind_eligible": false,
  "qualification": "helper AXH 답·태그 우발노출 및 AXH source 경로 이탈 보존; Astra SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AXG-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    16
  ],
  "auxiliary": [
    14,
    4,
    45
  ],
  "surface": [
    24,
    5
  ],
  "decisive_operation": "과냉각과 이력 특성의 정의를 분리한다. 물 사례로 비이력∧과냉각의 공존을 확인하고, 우무의 동일현재조건·상이직전상태를 구성한다. ㄷ에서는 어느 온도까지라는 범위를 보존한다.",
  "scope": "ㄱ은14,ㄴ은45의 입력 부족,ㄷ은4; 세 판단을 개념 구별16으로 묶되 단일 연산으로 환원하지 않음",
  "competing_codes": [
    {
      "code": 13,
      "rejection": "과냉각과 비이력이 양립불가라는 생각을 물 사례가 깨뜨린다. 배타 자체가 주 연산이 아니다."
    },
    {
      "code": 2,
      "rejection": "가능이라는 어미는 있으나 ㄷ의 핵심은 일정 온도 범위를 전부로 넓힌 것이다."
    },
    {
      "code": 24,
      "rejection": "과냉각은 예외 소재이나 이력 특성과의 동치 여부를 따지는 데 규칙-예외 위계만으로 부족하다."
    },
    {
      "code": 21,
      "rejection": "명시적 쌍조건을 전칭 증명하지 않는다. 정의 특징 분리16과 중첩 여지는 유지하되 독립 필요충분 추론은 미확인."
    }
  ],
  "confidence": 0.84,
  "passage_group": "G342",
  "sdss_seen": false,
  "original_judgment_preserved": true,
  "quota_status": "unavailable"
}
```
