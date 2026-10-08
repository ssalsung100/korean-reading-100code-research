

<!-- luna-raw:BKD-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G453",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2019/2019_answer_2019_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "ㄱ은 파장 증가→속도 감소→힘 감소여서 거짓. ㄴ은 전압 증가→속도 증가→파장 감소→회절 원반 감소가 가능하여 참. ㄷ은 전류 감소→초점 거리 증가→최소 해상도 수치 증가여서 거짓. ㄴ만 선택한다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_limit_preserved": "새로운 원문 제한 없음"
}
```


<!-- luna-raw:BKD-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G453",
  "minimal_logic_without_codes": "전압·속도·파장, 전류·자기장·초점 거리, 초점 거리·해상도의 연결 방향을 조합해 ㄴ만 성립함을 확인한다.",
  "primary": [
    {
      "code": 46,
      "reason": "ㄴ과 ㄷ은 중간 작용 위치를 통과하는 방향 연결을 복원해야 하며 단일 증감 문장 확인으로 끝나지 않는다."
    }
  ],
  "auxiliary": [
    {
      "code": 91,
      "reason": "파장은 속도에 반비례하고 힘은 속도에 비례한다. 해상도는 초점 거리에 비례한다."
    },
    {
      "code": 43,
      "reason": "ㄱ에서 질량·자기장, ㄴㄷ에서 비교 대상 외 렌즈 조건을 고정해 각 효과 방향을 읽는다. 실험 설계나 인과 식별을 했다고 확대하지 않는다."
    },
    {
      "code": 16,
      "reason": "해상도는 구별 가능한 두 점 간 한계 거리이며 수치 감소가 성능 향상이라는 정의를 적용한다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "비례식을 쓸 수 있지만 수치 계산 없이 방향 합성만으로 결정한다."
    }
  ],
  "competing_codes": [
    {
      "code": 49,
      "rejection": "각 단계의 방향을 기술하는 실질 후보지만 파장과 힘, 전류와 해상도의 중간 연계를 생략하면 정확한 결론이 안 나온다. 46을 경로 복원 작업 대표로 둔다."
    },
    {
      "code": 45,
      "rejection": "함수 합성으로 같은 경로를 기술할 수 있어 전역 배타성은 주장하지 않는다. 이 사례는 물리 작용을 명시하므로 46 대표."
    },
    {
      "code": 43,
      "rejection": "다른 조건 고정은 필요하지만 처치군과 대조군에서 효과를 식별하는 과제가 아니라 주어진 관계망의 적용이다."
    }
  ],
  "boundary_note": "ㄱ의 파장→속도는 반비례식의 환산이며 파장을 변화시키는 원인이 속도라는 본문의 인과 방향을 역전했다고 주장하지 않는다. 관계 환산과 작용 경로를 함께 보존한다.",
  "confidence": 0.91,
  "sdss_seen": false
}
```
