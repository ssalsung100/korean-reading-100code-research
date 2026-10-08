

<!-- luna-raw:ANV-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G260",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "소극적 부조의 초기 시점을 복지국가 이후로 옮긴 오류.",
  "original_blind_preserved": true,
  "barrier": "group 전체 blind 저장 확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:ANV-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 3,
      "reason": "초기 부조와 이후 복지의 시간 귀속 교환"
    }
  ],
  "auxiliary": [
    {
      "code": 5,
      "reason": "소극적 중재에서 적극적 사회관리로 변화"
    }
  ],
  "surface": [
    {
      "code": 59,
      "reason": "정책 해결책 소재"
    }
  ],
  "competitors": [
    {
      "code": 17,
      "refutation": "정책의 대상 귀속이라기보다 동일 국가의 시기별 역할이 바뀐 것.3과 중첩 가능"
    },
    {
      "code": 19,
      "refutation": "복지가 부조의 부족을 보완하는 구조는 있으나⑤ 오류는 이전 정책을 이후 대표책으로 옮김"
    },
    {
      "code": 2,
      "refutation": "가능/필연 강도보다 시기와 정책 대응이 직접 근거"
    }
  ],
  "counterfactual_probe": "⑤의 복지국가 개념 확립 이후를 제3공화국 초기로 고치면 본문과 맞음. 부조가 이후 전혀 없었다는 결론은 도출하지 않음.",
  "confidence": 0.96,
  "passage_group": "G260",
  "sdss_disclosed": false
}
```
