

<!-- luna-raw:BPO-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G501",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "①은 현량과가 기존 과거제의 인재 등용·통치 보조 목적을 유지하며 선발 방식을 보완했다는 내용과 맞는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BPO-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G501",
  "minimal_logic_without_codes": "선발 방식과 평가 범위를 바꾸려 해도 인재를 등용해 교화와 통치를 돕는 기존 목적은 공유한다.",
  "primary": [
    {
      "code": 44,
      "reason": "같은 인재 등용 목적과 서로 다른 선발 수단을 구분한다."
    }
  ],
  "auxiliary": [
    {
      "code": 19,
      "reason": "현량과는 기존 과거가 놓치는 덕행 등을 보완하려는 제도다."
    },
    {
      "code": 17,
      "reason": "생원·진사의 응시 자격과 문과 최종 합격의 관직 자격을 나눈다."
    },
    {
      "code": 4,
      "reason": "누구나 응시할 수 있다는 표현에 붙은 노비 제외 범위를 유지한다."
    }
  ],
  "surface": [
    {
      "code": 46,
      "reason": "현량과가 실제로 어떤 정치 효과를 냈는지는 있지만①은 표방 목적의 비교다."
    }
  ],
  "competing_codes": [
    {
      "code": 20,
      "rejection": "보완 제도가 생겼다고 기존 과거제가 완전히 불필요해졌다는 주장은 없다."
    },
    {
      "code": 58,
      "rejection": "목적을 공유하는 것을 논증의 동일 전제를 공유한다는 말로 자동 치환하지 않는다."
    },
    {
      "code": 86,
      "rejection": "합격 인원과 품계가 나오지만①의 판단은 수량 계산이 아니다."
    }
  ],
  "confidence": 0.96,
  "sdss_seen": false
}
```
