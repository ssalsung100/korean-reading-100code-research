

<!-- luna-raw:AFL-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "장기에실질통화량이원래수준으로돌아와도자국물가수준은높아졌으므로장기균형환율은상승한다.①은실질통화량불변을환율불변으로잘못연결한다.",
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


<!-- luna-raw:AFL-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "logic_without_codes_fixed": "실질 통화량=M/P가 장기에 일정해도 P가 일정하다는 뜻은 아니다. M증가를 P증가가 상쇄할 때 장기 환율=P/P외국은 높아질 수 있으며 본문은 이 상승을 명시한다.",
  "primary": [
    84
  ],
  "auxiliary": [
    17,
    3
  ],
  "primary_scope": "서로 다른 분수 관계의 분자·분모를 구별하여 한 비율의 불변을 다른 비율의 불변으로 옮기지 않는다.",
  "auxiliary_scope": {
    "17": "실질 통화량과 환율의 변수 정의·기준 귀속을 보존.",
    "3": "단기 물가 경직과 장기 물가 조정을 구분."
  },
  "surface": [
    49,
    43
  ],
  "evidence": [
    "3문단 통화량 증가유지→장기 자국물가 상승→장기 환율 상승,실질 통화량 불변.",
    "① 실질 통화량 불변이므로 환율 불변이라는 잘못된 연결."
  ],
  "competing_codes": [
    {
      "code": 49,
      "reason": "증감 방향으로도①을 기각할 수 있으나 왜 실질량 불변이 환율 불변을 보장하지 않는지 설명하려면 서로 다른 비율의 구성 변수를 보존해야 한다. 방향 표시는 결과이고84는 오류 근거를 드러내는 대표."
    },
    {
      "code": 43,
      "reason": "외국 물가에 새 충격을 주지 않는 본문 상황의 비교 조건은 유지하되, 서로 다른 집단을 통제하여 순수 효과를 추정하는 실험은 아니다."
    },
    {
      "code": 45,
      "reason": "M/P와P/P외국이라는 함수 대응으로 넓게 기술 가능하다. 그러나 구체적인 분자·분모의 역할을 생략하면 잘못된 비율 전이를 놓치므로84를 작업 대표로 둔다. 전역 배타 경계는 주장하지 않음."
    }
  ],
  "falsification_probe": "M과P가 함께 같은 비율로 증가하면M/P는 일정하지만P외국이그대로일때P/P외국은증가한다. 비율하나불변→다른비율불변의보편규칙은성립하지않음.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
