

<!-- luna-raw:BCR-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G387",
  "selected_answer": 3,
  "official_answer": "③",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "권리의 보호 대상은 성명·초상이 지닌 경제적 가치이므로 실제 수익 발생을 필수로 덧붙일 근거가 없다. 잠재적 가치를 지닌 것도 보호 대상이다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": null
}
```


<!-- luna-raw:BCR-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G387",
  "primary_codes": [
    2
  ],
  "auxiliary_codes": [
    16,
    17,
    10
  ],
  "surface_codes": [
    79
  ],
  "decisive_operation": "가치를 지님과 실제 이익 발생을 구별하여 보호 범위를 현실화된 수익에 한정하지 않는다.",
  "competitor_refutations": [
    {
      "code": 1,
      "reason": "수익의 유무가 표면에 있지만 잠재적 가치와 실현 이익의 차이는 가치 없음/있음만으로 환원되지 않는다. 주2가 현실화 여부를 드러낸다."
    },
    {
      "code": 10,
      "reason": "실제 이익 발생을 필수로 만들 수 없다는 부가요건 검사는2와 중첩하는 보조. 독립적인 별도 조건문 추론으로 세지 않는다."
    },
    {
      "code": 17,
      "reason": "②의 주체/목적 교환,④의 권리 성격 뒤바꿈에 직접 유효하나 정답③의 잠재성 판독과 범위를 구별한다."
    }
  ],
  "boundary_note": "2는 가능/필연 강도 외에 잠재 가치/현실화 판독의 국소 적용이다. 어떤 가능성만 있어도 모든 권리가 생긴다는 일반 명제 아님.",
  "confidence": 0.87,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
