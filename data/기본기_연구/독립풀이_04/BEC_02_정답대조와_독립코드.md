

<!-- luna-raw:BEC-answer_check-20261002-r2-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G399",
  "all_group_blind_records_before_any_group_answer_check": true,
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "ㄱ 전열 제거·후열 이동, ㄴ 후열 제거·전열 유지. 제거와 이동을 열별로 따로 분류.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BEC-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G399",
  "primary": [
    {
      "code": 15,
      "reason": "정치·감주·이주 각각의 판별 기준을 열별 사례에 적용한다."
    }
  ],
  "auxiliary": [
    {
      "code": 39,
      "reason": "ㄱ과 ㄴ에 적용된 기법 유무를 대조한다."
    },
    {
      "code": 92,
      "reason": "내부8개·4개의 기본 배치를 재구성해 없어진 열을 확인한다."
    }
  ],
  "surface": [
    {
      "code": 44,
      "reason": "공간 활용 목적은 배치 변화의 배경이며 정답은 제거 위치의 기준 적용으로 결정된다."
    }
  ],
  "competing_codes": [
    {
      "code": 21,
      "rejection": "15와 독립 연산으로 구분하기 어렵다. 정의 적용을 달리 부른 통합 후보로 보존한다."
    },
    {
      "code": 42,
      "rejection": "내부라는 단어는 부재 범위일 뿐 내부/외부 관계 자체가 정답을 가르지 않는다."
    },
    {
      "code": 78,
      "rejection": "건축 목적을 새로 추론할 필요 없이 주어진 배치를 분류한다."
    }
  ],
  "boundary_note": "15/16/21은 정의·기준 적용의 실질 중첩 후보. 여기서는 판단 행동 대표로15를 쓴다.",
  "confidence": 0.95,
  "sdss_disclosed": false
}
```
