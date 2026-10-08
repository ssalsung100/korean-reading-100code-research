

<!-- luna-raw:AKZ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G234",
  "official_answer": 5,
  "blind_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2023/2023_answer_언어이해정답.pdf",
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "logic_without_codes": "목적지별 합성 장소를 역으로 찾아 두 단백질의 출발 장소를 비교하면 미토콘드리아행과 세포막행은 다르다.",
  "correction": "없음",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AKZ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    39
  ],
  "primary_candidates": [
    39,
    17
  ],
  "working_primary": 39,
  "unique_primary_confirmed": false,
  "auxiliary": [
    45
  ],
  "surface": [
    42
  ],
  "judgment_reason": "미토콘드리아행은 독립 리보솜,세포막행은 소포체 리보솜이라는 대응을 복원하고 합성 장소가 같다는⑤를 배제한다.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "공동 주 후보",
      "reason": "두 단백질의 합성 계통 귀속으로 같은 오류를 설명한다."
    },
    {
      "code": 45,
      "verdict": "보조",
      "reason": "합성 위치→최종 위치 대응이 비교의 자료지만 수량적 출력 계산은 없다."
    },
    {
      "code": 42,
      "verdict": "표면",
      "reason": "두 합성 장소 모두 세포 안이다.세포 안팎 자체가⑤의 비교축은 아님."
    }
  ],
  "minimal_change_test": "⑤의 같은 곳을 다른 곳으로 바꾸면 맞는다.리보솜이라는 기관 종류만 비교하면 차이를 놓친다.",
  "confidence": 0.97,
  "passage_group": "G234",
  "sdss_seen": false,
  "all_group_answer_check_complete": true,
  "quota_status": "unavailable"
}
```
