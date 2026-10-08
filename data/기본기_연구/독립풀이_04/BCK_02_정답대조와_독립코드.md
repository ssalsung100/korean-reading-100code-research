

<!-- luna-raw:BCK-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G385",
  "selected_answer": 3,
  "official_answer": "③",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 패킷의 공식 정답 필드 대조. 원 정답표의 독립 시각 대조는 미실시.",
  "logic_without_codes_fixed": "대사로 등장한 인물을 모두 화면에 골고루 비추었다고 할 수 없다. 명시된 화면 밖 전달 방식과 선지③의 고른 촬영 지시가 충돌한다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": null
}
```


<!-- luna-raw:BCK-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G385",
  "primary_codes": [
    42
  ],
  "auxiliary_codes": [
    4,
    36
  ],
  "surface_codes": [
    44,
    93
  ],
  "decisive_operation": "화면에 실제로 보이는 인물과 음성만 전달되는 인물을 나눈 뒤 골고루 표정이 제시된다는 진술을 반증한다.",
  "competitor_refutations": [
    {
      "code": 4,
      "reason": "골고루라는 대상 범위의 과잉은 중요하나 먼저 화면 밖 발화와 시각 제시를 구별해야 한다. 주42의 판독에 뒤따르는 보조다."
    },
    {
      "code": 44,
      "reason": "기법·효과 발문 전체는 수단/목적이지만 정답③은 효과의 적합성이 아니라 촬영 지시 존재 여부에서 탈락한다."
    },
    {
      "code": 93,
      "reason": "채널 구별은 겹치나 발신·수신자 메시지 대응을 복원하지 않고도 화면 경계로 결정 가능하다."
    }
  ],
  "boundary_note": "42와93은 시청각 채널의 한 측면에서 중첩한다. 화면 밖 근거를 단순 부재로 취급하지 않고 Ⓔ라는 양성 표지를 사용한다.",
  "confidence": 0.88,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
