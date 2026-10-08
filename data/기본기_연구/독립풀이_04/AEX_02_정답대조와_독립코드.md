

<!-- luna-raw:AEX-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "도착점은 환원극으로 같지만 이온의 전해질 경로와 전자의 도선 경로를 구분.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 아님",
  "group_barrier": "AEX/AEY/AEZ/AFA 전체 blind raw 저장 후 answer 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AEX-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "primary": [
    45
  ],
  "auxiliary": [
    17
  ],
  "surface": [
    40,
    46,
    50
  ],
  "logic_without_codes_fixed": "동일하게 환원극으로 이동하더라도 수소 이온의 통로는 전해질, 전자의 통로는 도선이다.",
  "evidence": [
    "마지막 문단 수소 이온은 전해질을 통해, 전자는 도선을 통해 환원극으로 이동."
  ],
  "primary_scope": "입자별 이동 경로 대응을 보존하고 한쪽 경로를 다른 입자에 옮긴⑤ 배제",
  "auxiliary_scope": "17은 입자와 통로의 귀속 구분이라는 국소 기술.45와 다른 독립 연산으로 계수하지 않음.",
  "competitors_rejected": [
    {
      "code": 40,
      "reason": "구성 요소 목록을 아는 것만으로는 입자별 통로를 구분할 수 없다. 부분의 존재보다 작동 경로 대응이 결정점."
    },
    {
      "code": 50,
      "reason": "통로가 막히거나 개입되어 후속 진행이 중단된 사례가 아니다. 경로라는 단어만으로50 부여 불가."
    },
    {
      "code": 46,
      "reason": "전기 생성 전체는 인과 과정이나⑤는 한 단계의 입자-통로 대응을 교환한다.45와 넓게 중첩 가능하지만 인과 경로 전체 추적은 요구되지 않는다."
    }
  ],
  "counterfactual_test": "두 입자의 목적지를 바꾸지 않고⑤의 도선을 전해질로 고치되 전자와 마찬가지라는 동일성 표현도 제거하면 원문 대응을 회복한다.",
  "boundary_note": "같은 출력·도착점이 같은 처리 경로를 함축하지 않는다.45/17의 국소 중첩은 전역 통합 근거가 아니다.",
  "confidence": 0.94,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
