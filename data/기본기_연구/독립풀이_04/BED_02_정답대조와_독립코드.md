

<!-- luna-raw:BED-answer_check-20261002-r2-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G400",
  "all_group_blind_records_before_any_group_answer_check": true,
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "달만·스미스 모두 개별 경지보다 큰 공동 목축의 효율을 전제한다. 공통점을 차이로 제시한④를 배척.",
  "unresolved": "⑤는 해당 제도의 설명 방식 요약. 모든 제도의 합리성으로 일반화하지 않는다.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BED-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G400",
  "primary": [
    {
      "code": 39,
      "reason": "두 설명의 공유 전제를 차이로 잘못 표시한④를 비교 판정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 75,
      "reason": "보험·생산·공동목축·기회주의 설명의 입장별 귀속이 필요하다."
    },
    {
      "code": 58,
      "reason": "달만과 스미스의 공동 목축 규모 이점이라는 공통 전제 확인."
    }
  ],
  "surface": [
    {
      "code": 77,
      "reason": "⑤가 일반화 표현을 사용하지만 문맥 범위 밖 보편 명제의 타당성을 묻는 중심 과제는 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 74,
      "rejection": "설명 경쟁은 존재하지만 신규 관찰의 서로 다른 예측을 검사하지 않는다."
    },
    {
      "code": 88,
      "rejection": "효율성이 소재이나 비용 편익 최적 비교 계산은 없다."
    },
    {
      "code": 86,
      "rejection": "개별/목축 규모 비교는 공통 내용이며 두 견해의 차이 여부가 정답 결정 행동이다."
    }
  ],
  "confidence": 0.93,
  "sdss_disclosed": false
}
```
