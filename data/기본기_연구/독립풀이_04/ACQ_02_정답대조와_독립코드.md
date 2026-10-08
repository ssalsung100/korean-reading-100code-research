

<!-- luna-raw:ACQ-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G180",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "차폐음에서 다른 주파수까지의 거리가 대역 전체 폭을 초과하면 대역 밖이다. 대역 대칭성 가정이나 역 추론은 필요 없다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 아님",
  "group_barrier": "ACO/ACP/ACQ/ACR 전체 blind raw 저장 후 answer 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:ACQ-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G180",
  "primary": [
    12
  ],
  "auxiliary": [
    86,
    16
  ],
  "surface": [
    49
  ],
  "logic_without_codes_fixed": "차폐음 주파수 f0가 대역[L,U] 안에 있을 때 |f-f0|>U-L이면 f는 대역 밖이다. 차폐 가능 범위를 벗어나므로 차폐가 일어나지 않는다.",
  "evidence": [
    "4문단 임계대역은 차폐가 일어날 수 있는 최저~최고 주파수 구간.",
    "⑤는 차폐음과 다른 소리의 주파수 차이가 전체 폭보다 크다는 충분한 외부 조건을 제시한다."
  ],
  "primary_scope": "주파수 차이 조건으로 대역 밖을 도출한 뒤 차폐 불가를 적용",
  "auxiliary_scope": {
    "86": "전체 구간 폭과 기준점으로부터 거리를 비교하여 대역 외부를 확정.",
    "16": "최소가청강도는 크기, 임계대역은 주파수 구간, 차폐음은 큰 소리라는 개념 요소를 유지하여①~④ 배제."
  },
  "competitors_rejected": [
    {
      "code": 11,
      "reason": "대역 폭보다 주파수 차이가 작은 경우 반드시 차폐됨은 성립하지 않는다.⑤는 필요충분조건이 아니다."
    },
    {
      "code": 49,
      "reason": "주파수 차이가 클수록 차폐가 덜 일어난다는 방향만으로는⑤의 폭 초과 기준을 충분히 설명하지 못한다. 범위 밖 판정이 필요하다."
    },
    {
      "code": 10,
      "reason": "같은 관계를 차폐의 필요조건으로 재기술할 수 있으나 실제⑤의 추론은 주어진 폭 초과에서 차폐 불가로 진행한다. 별개 본질적 논리식으로 분리하지 않는다."
    }
  ],
  "counterfactual_test": "대역[100,200], f0=150, f=220이면 차이70은 폭100보다 작아도 대역 밖이다. 따라서 폭 초과는 외부의 충분조건일 뿐 필요조건이 아니다. 이 수치는 원문 밖 기술 실행이 아닌 구간 관계 반례다.",
  "boundary_note": "차폐음이 대역 중앙에 있다는 대칭성은 가정하지 않는다.12/10의 기술 동치 가능성을 보존하고 폭과 거리 연산86을 삭제하지 않는다.",
  "confidence": 0.96,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
