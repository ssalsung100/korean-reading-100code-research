

<!-- luna-raw:BFE-answer_check-20261002-r2-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G409",
  "all_group_blind_records_before_any_group_answer_check": true,
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "정당 수 산정은 체계의 상호작용·이념분포·안정성 분석 지표이며 개별 정당의 여론 전달 기능 평가가 아니다.",
  "source_restore_reference": "BFE-boundary_revision-20261002-r2-01",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BFE-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G409",
  "general_task": "분석 지표의 역할 확인",
  "decisive_relation": "개별 정당 수준과 정당 체계 수준의 기능 구별",
  "primary": [
    {
      "code": 17,
      "reason": "여론 전달 기능의 평가를 개별 정당에서 정당 체계의 수량 지표로 옮기는 오류를 판정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 40,
      "reason": "단일 정당과 정당군이라는 분석 수준 차이가 관계 구분의 배경이다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "지표가 수량이지만 이 문항에는 수식 계산이 없다."
    }
  ],
  "competing_codes": [
    {
      "code": 41,
      "rejection": "부분 속성을 모두 합쳐 전체에 부여하는 구체 추론보다는 분석 기능의 범주 이동이다."
    },
    {
      "code": 44,
      "rejection": "목적을 묻는 발문으로 기술할 수 있으나 구분 기준은 개별/체계의 분석 대상이다."
    },
    {
      "code": 39,
      "rejection": "두 차원의 비교가 있으나 정답은 그 속성을 잘못 옮긴 대상 범주 오류다."
    }
  ],
  "confidence": 0.95,
  "sdss_disclosed": false
}
```
