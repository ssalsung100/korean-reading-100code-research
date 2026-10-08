

<!-- luna-raw:ANW-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G260",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "특수 이익 대표의 행정부 역할을 의회주의로 교환.",
  "original_blind_preserved": true,
  "barrier": "group 전체 blind 저장 확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:ANW-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 17,
      "reason": "특수이익 대표 기능의 행정부 귀속을 보존"
    }
  ],
  "auxiliary": [
    {
      "code": 40,
      "reason": "입법부/행정부의 국가기관 구성 구별"
    },
    {
      "code": 5,
      "reason": "의회의 절대성 약화와 행정부 대표성 확대"
    }
  ],
  "surface": [
    {
      "code": 75,
      "reason": "두 기관은 견해 논쟁 주체라기보다 기능 분담 대상"
    }
  ],
  "competitors": [
    {
      "code": 26,
      "refutation": "입법과행정의 모든 속성이 배타적인 것이 아니라 대표 기능의 중심 변화"
    },
    {
      "code": 44,
      "refutation": "특수 이익 대표라는 기능 자체는 맞고 담당 기관이 다름"
    },
    {
      "code": 46,
      "refutation": "노동정당 성장의 인과 배경은 있으나③을 고치려면 기관 귀속을 바꿔야 함"
    }
  ],
  "counterfactual_probe": "③의 의회주의를 행정부의 위원회로 바꾸면 참. 같은 대표라는 단어로 기관을 합치지 않는다.",
  "confidence": 0.96,
  "passage_group": "G260",
  "sdss_disclosed": false
}
```
