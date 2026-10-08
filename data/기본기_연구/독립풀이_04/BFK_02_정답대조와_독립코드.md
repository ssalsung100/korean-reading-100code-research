

<!-- luna-raw:BFK-answer_check-20261002-r3-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G411",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "answer_verification": "봉인 official_answer 전사필드와 대조. 원 HWP 정답표 독립 시각 대조는 미실시.",
  "official_answer_source": "자료/LEET_언어이해/원본/2009예비/2009예비_answer_2009법학적성시험_예비_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "관9치·척10치, 원기장관은 중국음보다 높고 밀랍관은 중국음과 같음. ㄱㄷ.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BFK-independent_code-20261002-r3-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "general_task": "복수 진술의 본문 부합 여부 확인",
  "decisive_relation": "두 제작물의 음과 중국 기준음의 같음/다름을 분리하고 길이·기재 항목을 정확히 귀속",
  "primary": [
    39
  ],
  "auxiliary": [
    17,
    86
  ],
  "surface": [
    15,
    92
  ],
  "code_rationale": {
    "39": "ㄹ의 서로 다른 두 관을 같은 것으로 만들 수 없고 ㄷ은 중국음과 밀랍관의 대응이다.",
    "17": "ㄴ의 산출지/쌓는 법 대상 교체",
    "86": "ㄱ의 9치 관과 10치 척의 크기 대응"
  },
  "competing_codes": [
    {
      "code": 15,
      "rebuttal": "황종이 기준음이기는 하나 새 사례를 정의 조건으로 분류하는 것이 핵심은 아니다."
    },
    {
      "code": 92,
      "rebuttal": "9+1=10은 보조 확인이며 ㄴ·ㄹ 오류는 계산으로 검출되지 않는다."
    },
    {
      "code": 46,
      "rebuttal": "재료 변경과 음 변화의 원인 기제를 복원하지 않고 기록된 음의 일치 여부만으로 판정된다."
    }
  ],
  "confidence": 0.84,
  "unresolved": "39는 문항 전체의 작업 대표이며 ㄴ은17, ㄱ은86으로 다른 국소 행동이다. 단일 관계로 압축하지 않는다.",
  "passage_group": "G411",
  "sdss_disclosed": false
}
```
