

<!-- luna-raw:ARS-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G294",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "ㄱㄴㄹ은 되먹임 고리,ㄷ은 조건별 다른 결과 경로다.ㄷ을 엄밀한 카오스 충분조건 사례로 확대하지 않는다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ARR",
    "ARS",
    "ART"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ARS-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G294",
  "primary": [
    46
  ],
  "auxiliary": [
    25,
    45
  ],
  "surface": [
    49
  ],
  "decisive_operation": "각 보기에서 결과가 최초 원인으로 되돌아오는 닫힌 경로인지 조건 차이에 따른 결과 분기인지 복원하여 유형을 분류한다.",
  "competing_codes": [
    {
      "code": 25,
      "rebuttal": "분류는 과업이고 그 분류의 결정 근거는 인과 경로의 되먹임 여부다. 두 관점은 중첩된다."
    },
    {
      "code": 49,
      "rebuttal": "양의 증폭 방향이 있지만 여러 단계의 되먹임 고리를 직접 복원해야 단순 동반 증가와 구별된다."
    },
    {
      "code": 45,
      "rebuttal": "ㄷ은 조건에 따라 다른 출력을 내는 관계로 표현되나 전체 분류는 그 관계와 닫힌 인과 고리의 차이에 의존한다."
    }
  ],
  "boundary_note": "조건별 결과 분기만으로 일반적으로 카오스라고 판정하지 않는다.보기ㄷ의 본문상 상대적 분류와 엄밀 정의 충족은 별도다.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
