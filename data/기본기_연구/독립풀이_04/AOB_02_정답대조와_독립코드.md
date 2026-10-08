

<!-- luna-raw:AOB-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G262",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2013/2013_answer_2013_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "직접 해당 규정 부재에서 유사 조문을 찾아 적용하는 원칙.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AOB-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 69,
      "reason": "직접 규정 없는 상전 모해를 국가에 대한 반역 조문에 대응시켜 적용"
    }
  ],
  "auxiliary": [
    {
      "code": 60,
      "reason": "실제 절차가 전제하는 적용 원칙을 역으로 복원"
    },
    {
      "code": 19,
      "reason": "직접 규정의 공백을 유사 조문으로 보충"
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "형률 소재 자체가 정답의 당위 추론은 아님"
    }
  ],
  "competitors": [
    {
      "code": 12,
      "refutation": "기존 규칙의 조건 적용은 후속이지만 직접 조문이 없는데 적용 가능한 이유가 유추"
    },
    {
      "code": 8,
      "refutation": "두 법의 경중 우선순위를 정한 동시 성립 사안으로 주어지지 않음"
    },
    {
      "code": 24,
      "refutation": "기존 원칙에 대한 예외를 신설하지 않고 유사 규정을 끌어옴"
    }
  ],
  "counterfactual_probe": "상전모해의직접조문이주어져그대로적용했다면①의유추전제는필수아님.현재는규정공백과유사조문선택이명시됨.",
  "confidence": 0.96,
  "passage_group": "G262",
  "sdss_disclosed": false
}
```
