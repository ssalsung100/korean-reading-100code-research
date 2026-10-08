

<!-- luna-raw:AFM-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "기존담당부서가복지카드혜택을늘리는것은새부처를만드는것보다기존조직활용정도가높아⑤가맞다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조는 이번 stage에서 수행하지 않음.",
  "group_barrier": "AFO 원그래프/범위/선지표 직접확인 후 전체6 blindraw 저장을 확인하여 answer필드만 공개.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFM-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "logic_without_codes_fixed": "자동성은 정책 규모나 기계화 정도가 아니라 기존 조직 활용 정도다. 기존 부서에서 혜택을 늘리는 경우는 새 전담 부처를 만드는 경우보다 자동성이 높다.",
  "primary": [],
  "primary_candidates": [
    15,
    16
  ],
  "working_representative": 15,
  "auxiliary": [
    86
  ],
  "surface": [
    1,
    44
  ],
  "evidence": [
    "1문단 자동성=별도행정기구를설립하지않고기존조직활용정도.",
    "⑤기존담당부서의혜택확대vs전담부처신설."
  ],
  "competing_codes": [
    {
      "code": 16,
      "reason": "자동성 정의의 핵심 속성을 분해해 적용하는 행동과15기준 적용이 국소 중첩한다. 유일 주 우위는 유보하고 후보로 보존."
    },
    {
      "code": 86,
      "reason": "두 사례의 높고낮음을 비교하지만 무엇을 측정하는지 결정하려면 자동성의 정의를 먼저 적용해야 한다. 금액·혜택수준의 양적 비교가 아님."
    },
    {
      "code": 1,
      "reason": "조직신설 유무로 해당 사례를 구별할 수 있으나 유무 자체가 모든 정책 속성의 순위를 정하는 기준은 아니다. 가시성·강제성·직접성은 각각 다른 속성을 보존해야 함."
    }
  ],
  "falsification_probe": "기존 부서의 복지카드 지원액을 더 키우더라도 그것만으로 별도 조직 신설 여부가 달라지지 않아 자동성 판단은 유지된다. 정책 규모와 조직 활용 기준을 분리.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
