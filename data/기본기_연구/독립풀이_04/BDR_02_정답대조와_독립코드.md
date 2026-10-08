

<!-- luna-raw:BDR-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G396",
  "selected_answer": 4,
  "official_answer": "④",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "세포 안에서 이미 응집한 폴리펩티드가 자발적으로 원구조를 회복한다는④는 응집 전 리폴딩과 실험적 재현의 조건을 지운다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": null
}
```


<!-- luna-raw:BDR-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G396",
  "primary_codes": [
    3
  ],
  "auxiliary_codes": [
    2,
    17,
    10
  ],
  "surface_codes": [
    5
  ],
  "decisive_operation": "응집 전 리폴딩과 응집 후의 비가역 경향,세포 내 도움과 실험 조건을 구별해④의 시간·조건 전이를 반증한다.",
  "competitor_refutations": [
    {
      "code": 2,
      "reason": "대부분 비가역을 모든경우 절대불가능으로 확대하지 않는다.④를 배제해도 BDT의실험적회복과 양립 가능해야 함."
    },
    {
      "code": 17,
      "reason": "세포 내/시험관,응집 전/후의 대상 상태 귀속이3과 중첩한다."
    },
    {
      "code": 5,
      "reason": "구조변화는소재이지만변화가있다는사실보다언제어떤조건으로돌아가는지의제약이정답핵심."
    }
  ],
  "boundary_note": "리폴딩이세포안에서응집전에일어난다는설명을모든실험회복의불가능성으로전칭화하지않음.",
  "confidence": 0.9,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
