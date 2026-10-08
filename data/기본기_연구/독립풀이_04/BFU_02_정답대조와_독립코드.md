

<!-- luna-raw:BFU-answer_check-20261002-r3-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G414",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "answer_verification": "봉인 official_answer 전사필드 대조. 원정답표 독립 시각 대조 미실시.",
  "official_answer_source": "자료/LEET_언어이해/원본/2010/2010_answer_2010_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "국전 관련규정이 있으면 국전,없으면 대명률을 적용하며 관찰사의 사형 선고 제한은 별도 절차다. ㄱㄴ 참,ㄷㄹ 거짓.",
  "unresolved": null,
  "sdss_disclosed": false
}
```


<!-- luna-raw:BFU-independent_code-20261002-r3-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G414",
  "general_task": "법 적용 사례 판정",
  "decisive_relation": "해당 국전규정 존재 여부에 따른 우선 적용과 별도 절차 제한 결합",
  "primary": [
    8
  ],
  "auxiliary": [
    12,
    19
  ],
  "surface": [
    79,
    24
  ],
  "code_rationale": {
    "8": "두 법에 모두 규정 있으면 국전 우선",
    "12": "국전 존재/부재에 따라 적용법을 선택",
    "19": "국전 빈틈은 대명률이 보충"
  },
  "competing_codes": [
    {
      "code": 12,
      "rebuttal": "8은 조건부 우선순위를 구체화한 관점이며 동일 규칙을12로도 표현 가능.별도 행동으로 중복 계수하지 않음."
    },
    {
      "code": 24,
      "rebuttal": "일반 대명률/특별 국전이라는 원칙예외 표상도 가능하나 결정적 행동은 병존 규정의 적용 순위."
    },
    {
      "code": 79,
      "rebuttal": "사형 소재보다 어떤 규칙을 우선 적용하는지가 직접 판단.법 일반 코드로 압축하지 않음."
    }
  ],
  "confidence": 0.95,
  "sdss_disclosed": false
}
```
