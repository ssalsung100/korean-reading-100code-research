

<!-- luna-raw:ARA-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G288",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "선택④는 공식 답과 일치. 계통 외 실험 방식도 달라 계통 단독 원인 귀속이 부적절하다.①의 동일 결과 예측을 엄밀히 입증된 명제로 승격하지 않는다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "AQZ",
    "ARA",
    "ARB"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ARA-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G288",
  "primary": [
    43
  ],
  "auxiliary": [
    46,
    17
  ],
  "surface": [
    53
  ],
  "decisive_operation": "결과가 다른 두 실험에서 동물 종류 외 할구 손상·분리 처치가 함께 달라졌음을 확인하여 계통 차이에 대한 단독 인과 귀속을 막는다. 성체 재생과 초기 발생의 대상 범위도 분리한다.",
  "competing_codes": [
    {
      "code": 46,
      "rebuttal": "잘못된 원인 귀속을 설명하지만 그 이유를 밝히는 결정 단계는 다른 변수가 통제되지 않았다는 확인이다."
    },
    {
      "code": 53,
      "rebuttal": "차이가 결과 차이를 설명한다는 표면은 있으나 동시에 여러 차이가 있으므로 어느 차이의 효과인지 분리할 수 없다."
    },
    {
      "code": 74,
      "rebuttal": "대체 설명 후보를 만들 수는 있지만 제공된 실험으로 두 가설의 예측을 독립 검증하는 과업은 아니다."
    }
  ],
  "boundary_note": "계통 효과를 입증하지 못했다는 것과 계통 효과가 전혀 없다는 단정은 다르다.①의 예측도 엄밀히 보장됐다는 주장으로 강화하지 않는다.",
  "confidence": 0.91,
  "sdss_seen": false
}
```


후속 depth_backfill raw: `AUDIT81-depth_backfill-20260927-01` — [원장 기록](../../../분석/기본기_연구/독립연구_04_절차와_진행기록.md)
