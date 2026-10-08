

<!-- luna-raw:ANJ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G256",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2009예비/2009예비_answer_2009법학적성시험_예비_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "책임 명확화→예측 가능성→경제 활동 확대의 경로.",
  "original_blind_preserved": true,
  "barrier": "group 전체 blind 저장 후 answer",
  "sdss_disclosed": false
}
```


<!-- luna-raw:ANJ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G256",
  "primary": [
    {
      "code": 46,
      "reason": "법적 책임 명확화→결과 예측→활동 범위 확장 경로를 재진술"
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "scope": "③",
      "reason": "관료제의 자체 행정 필요와 자본가의 경제 필요를 구별"
    },
    {
      "code": 56,
      "reason": "경제 활동 확대를 법의 수단으로 설명"
    }
  ],
  "surface": [
    {
      "code": 80,
      "reason": "예측이라는 인식 행위가 있지만 정답은 그 제도적 효과 연결"
    }
  ],
  "competitors": [
    {
      "code": 44,
      "refutation": "법이 경제활동을 촉진하는 수단이지만 자본가의 의도·목적만으로 결과 경로를 대체하지 못함.46와 중첩은 인정"
    },
    {
      "code": 45,
      "refutation": "입출력 대응보다 법적 안정이 활동을 촉진하는 이유가 제시됨; 함수 표상 필수 아님"
    },
    {
      "code": 19,
      "refutation": "기존 결함의 특정 보충 여부를 확인하지 않아도④ 경로를 직접 읽을 수 있음"
    }
  ],
  "counterfactual_probe": "①의 유연성을 엄격한 선례 구속이 제공하는 예측가능성으로 바꾸면 본문에 부합. 불문법이라는 소재에 흔한 유연성 속성을 붙이는 상식 보완을 경계.",
  "confidence": 0.95,
  "sdss_disclosed": false
}
```
