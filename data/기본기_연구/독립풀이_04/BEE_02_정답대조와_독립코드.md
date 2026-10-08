

<!-- luna-raw:BEE-answer_check-20261002-r2-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G400",
  "all_group_blind_records_before_any_group_answer_check": true,
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "ㄱ 설명 대상의 분포,ㄷ 위험 분산의 전제,ㄹ 더 효율적인 대안으로 보험설 약화. ㄴ은 보험설과 양립.",
  "unresolved": "ㄱ은 다른 조건이 통제된 결정적 반증 아님.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BEE-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G400",
  "primary": [
    {
      "code": 63,
      "reason": "추가 관찰과 대안이 보험 설명의 설득력을 낮추는지 판단한다."
    }
  ],
  "auxiliary": [
    {
      "code": 73,
      "reason": "ㄷ은 산출 편차 충분성이라는 전제를 공격한다."
    },
    {
      "code": 88,
      "reason": "ㄹ은 생산 손실의 보험료보다 효율적인 위험 대비 대안을 제시한다."
    }
  ],
  "surface": [
    {
      "code": 43,
      "reason": "ㄱ의 결정적 인과 증명에는 통제가 필요하지만 발문은 비판 가능성이라 완전 통제는 요구되지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 36,
      "rejection": "ㄱ은 보험설과 양립 가능하며 논리적 보편명제의 확정 반례로 취급하면 과강화된다."
    },
    {
      "code": 74,
      "rejection": "ㄹ의 대안과 ㄱ의 방목 관련성은 있으나 모든 항목이 두 가설의 상반 예측 비교는 아니다."
    },
    {
      "code": 20,
      "rejection": "대안 존재만이 아니라 더 높은 효율성이ㄹ의 비판 힘을 만든다. 단순 복수실현만으로는 부족하다."
    }
  ],
  "confidence": 0.94,
  "sdss_disclosed": false
}
```
