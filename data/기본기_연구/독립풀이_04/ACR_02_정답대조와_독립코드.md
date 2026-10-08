

<!-- luna-raw:ACR-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G180",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "문턱 초과량 C25와 D49를 비교하여 D에 더 많은 비트를 할당한다. 절대 크기 순위와 다르다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 아님",
  "group_barrier": "ACO/ACP/ACQ/ACR 전체 blind raw 저장 후 answer 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:ACR-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G180",
  "primary": [
    45
  ],
  "auxiliary": [
    86,
    49,
    12
  ],
  "surface": [
    43,
    46
  ],
  "logic_without_codes_fixed": "압축 비트는 절대 소리 크기가 아니라 소리 크기에서 각 대역의 차폐 문턱값을 뺀 초과량에 따라 달라진다. C25<D49이므로D에 더 많이 할당한다.",
  "evidence": [
    "5문단 크기와 문턱값 차이가 클수록 비트를 많이 할당.",
    "보기 C63-38=25, D55-6=49. A30<38은 제거되고 B30-20=10은 양수."
  ],
  "primary_scope": "두 입력을 차이로 변환한 판단량에 비트 할당을 대응하는 실제 규칙 복원",
  "auxiliary_scope": {
    "86": "절대값 순위 C>D와 초과량 순위 D>C를 계산으로 분리.",
    "49": "계산한 차이가 클수록 비트가 많다는 방향 적용;45와 독립 증거로 중복 계수하지 않음.",
    "12": "문턱 미만 제거와 문턱 초과 감지 조건으로①~③ 배제."
  },
  "competitors_rejected": [
    {
      "code": 43,
      "reason": "문턱값이 서로 다를 때 소리 크기만 비교해서는 안 되지만 이는 인과 효과를 분리하는 통제 실험이 아니다. 주어진 두 입력을 그대로 사용한다."
    },
    {
      "code": 46,
      "reason": "비트 할당 규칙 적용이지 관측 자료에서 소리 크기나 문턱의 인과 효과를 추정하지 않는다."
    },
    {
      "code": 84,
      "reason": "비율이 아니라 차이이다. 크기를 문턱으로 나누는 계산은 원문 규칙을 바꾼다."
    }
  ],
  "counterfactual_test": "C/D의 문턱을 같게 놓으면 절대 크기 순위와 초과량 순위가 같아지지만 원래 표에서는 서로 다르다.⑤를 결정하는 핵심은 대역별 기준값을 보존한 차이 계산이다.",
  "boundary_note": "45를 모든 표 계산에 자동 부여하지 않는다. 입력 두 개를 차이로 변환하고 그 값을 할당 결과와 연결하는 구체 대응이 존재한다.86/49는 이 대응의 부분 연산.",
  "confidence": 0.97,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
