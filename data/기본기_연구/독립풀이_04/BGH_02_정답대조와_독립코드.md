

<!-- luna-raw:BGH-answer_check-20261002-r3-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G419",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "answer_verification": "봉인 official_answer 전사필드 대조. 원정답표 독립 시각 대조 미실시.",
  "official_answer_source": "자료/LEET_언어이해/원본/2010/2010_answer_2010_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "분급·회수는 국가가 직역자에게 부여한 권리를 관리하고 중복수급을 막는 제도다.ㄴㄷㄹ은맞고 사적조업전의원칙이라는ㄱ은아니다.",
  "unresolved": null,
  "sdss_disclosed": false
}
```


<!-- luna-raw:BGH-independent_code-20261002-r3-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G419",
  "general_task": "분급·회수 제도의 의미 추론",
  "decisive_relation": "직역·나이·생존 자격에 따른 권리 부여와 회수",
  "primary": [
    12
  ],
  "auxiliary": [
    15,
    46
  ],
  "surface": [
    79,
    3
  ],
  "code_rationale": {
    "12": "직역·생애조건에 따른 분급과 회수",
    "15": "수급 자격과 사적 계승을 구별",
    "46": "미회수와 중복수급 폐단의 연결"
  },
  "competing_codes": [
    {
      "code": 10,
      "rebuttal": "직역은 필요요건으로 표현되지만 전체는 분급·회수의 조건 적용.독립행동으로 중복계수하지 않음."
    },
    {
      "code": 79,
      "rebuttal": "규범 내용보다 대상·회수조건의 구조가 결정적."
    },
    {
      "code": 3,
      "rebuttal": "20세/60세 시간표는 부분 근거일 뿐ㄱ~ㄹ의 전체판정은 자격·관리 의미다."
    }
  ],
  "confidence": 0.91,
  "sdss_disclosed": false
}
```
