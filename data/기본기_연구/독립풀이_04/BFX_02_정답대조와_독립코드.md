

<!-- luna-raw:BFX-answer_check-20261002-r3-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G415",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "answer_verification": "봉인 official_answer 전사필드 대조. 원정답표 독립 시각 대조 미실시.",
  "official_answer_source": "자료/LEET_언어이해/원본/2010/2010_answer_2010_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "거리 최소인 A,D를 먼저 묶고 재계산하면 그 묶음에 C가 먼저 결합,마지막 B가 결합한다.시각자료08의 구조를 선택한다.",
  "unresolved": "이미지에 원선지 번호가 없고 JSON choices가 같은 placeholder여서 visual05~09 순차대응으로④를 기록.구조답과 번호대응의 확신을 분리하며 사후 정답으로 소급 blind 승격하지 않음.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BFX-independent_code-20261002-r3-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G415",
  "general_task": "표에서 계통수 산출",
  "decisive_relation": "차이 비율 계산→최소값 결합→거리 재계산의 반복",
  "primary": [
    92
  ],
  "auxiliary": [
    45,
    86
  ],
  "surface": [
    25,
    23
  ],
  "code_rationale": {
    "92": "AD2/8,갱신AD-C3/8,AD-B5/8 등 산술이 분기를 결정",
    "45": "표 입력→거리→갱신군의 순차 처리",
    "86": "최솟값 비교"
  },
  "competing_codes": [
    {
      "code": 15,
      "rebuttal": "규칙 준수라는 상위 설명은 되나 핵심 단계별 수치와 재계산을 지운다."
    },
    {
      "code": 23,
      "rebuttal": "공유파생만 묶는 BFW 규칙을 적용하면 처음AB를 묶는 다른 답이 나온다."
    },
    {
      "code": 25,
      "rebuttal": "트리형 산출물이라는 형식만으로 어떤 가지가 먼저 결합할지 결정되지 않는다."
    }
  ],
  "confidence": 0.98,
  "sdss_disclosed": false,
  "unresolved": "번호④는 원문 선지번호 대응 검증 대기.구조답은 visual08."
}
```
