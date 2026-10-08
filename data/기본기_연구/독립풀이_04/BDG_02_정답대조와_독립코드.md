

<!-- luna-raw:BDG-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G392",
  "selected_answer": 5,
  "official_answer": "⑤",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "세종13년에는 국왕이2품이상 관원의 퇴장을 지켜보지만 수정 오례에서는 관원이 지켜보는 가운데 국왕이 먼저 나간다. 이를 계승한 국조오례의가 세종13년 의식보다 편의를 더 고려한다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": null
}
```


<!-- luna-raw:BDG-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G392",
  "primary_codes": [
    39
  ],
  "auxiliary_codes": [
    3,
    44,
    5
  ],
  "surface_codes": [
    86
  ],
  "decisive_operation": "의식별 국왕과 관원의 입퇴장 순서를 대응한 뒤 국왕의 대기 부담/부동성을 비교하고 수정 오례와 국조오례의의 동일 형식을 보존한다.",
  "competitor_refutations": [
    {
      "code": 3,
      "reason": "입퇴장 선후가 비교의 핵심 입력이다.단순 연대 나열만으로 편의 정도를 알 수 없어39와44가 함께 필요하다."
    },
    {
      "code": 44,
      "reason": "군주상과 편의라는 두 목적의 반영을 판단한다. 순서 변형이 어떤 목적을 더 만족하는지39와 층위 중첩."
    },
    {
      "code": 86,
      "reason": "더 고려라는 말이 있지만 수치의 절대량/상대량 교환이 아니다. 절차상 대기·관람 여부의 질적 비교이다."
    }
  ],
  "boundary_note": "태조→태종→세종이라는 시간 순서를 편의의 단조 증가로 읽지 않는다. 오례→국조오례의는 실제 형식 변화 없음.",
  "confidence": 0.89,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
