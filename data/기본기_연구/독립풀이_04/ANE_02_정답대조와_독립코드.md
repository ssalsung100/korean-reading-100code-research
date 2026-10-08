

<!-- luna-raw:ANE-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G254",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2009예비/2009예비_answer_2009법학적성시험_예비_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "압축의 단계 배열을 경험의 속성으로 옮김. 공식 평가와 사전 계획은 별개.",
  "original_blind_preserved": true,
  "barrier": "all_group_blind_records_before_any_group_answer_check 확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:ANE-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G254",
  "primary": [
    {
      "code": 17,
      "reason": "활동 순차 배열이라는 방법의 소속 전략을 보존"
    }
  ],
  "auxiliary": [
    {
      "code": 39,
      "reason": "두 전략의 예측가능·반복적 방법 차이를 비교"
    },
    {
      "code": 14,
      "scope": "④",
      "reason": "공식 평가와 비사전계획의 양립을 유지"
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "순서 배열이 소재지만 문항 자체는 선후 추론보다 방법의 귀속 교환"
    }
  ],
  "competitors": [
    {
      "code": 75,
      "refutation": "대조적인 전략이나 상반 주장 논쟁의 승패를 묻지 않음. 운영 방식의 속성 귀속"
    },
    {
      "code": 45,
      "refutation": "조건별 개발 과정은 입력/출력으로 기술 가능해도⑤ 배제에 과정 전체 실행은 필요 없음"
    },
    {
      "code": 44,
      "refutation": "가속화라는 공통 목적은 맞으므로 목적만 알아서는⑤의 잘못된 수단 소속을 가르지 못함"
    }
  ],
  "counterfactual_probe": "발문의 경험을 압축으로 바꾸면⑤는 적절해진다. 단④의 공식적을 사전 계획된으로 바꾸면 경험에는 부적절. 두 형용사는 동치 아님.",
  "boundary_status": "17/39 소속 대조 중첩,3을 표면 단어 순서만으로 주코드 승격 금지",
  "confidence": 0.95,
  "sdss_disclosed": false
}
```
