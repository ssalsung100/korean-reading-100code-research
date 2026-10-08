

<!-- luna-raw:AWE-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G333",
  "initial_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2023/2023_answer_언어이해정답.pdf",
  "code_free_logic": "작은배경차이존재를완전무관으로바꾼오류.",
  "barrier": "group 전체 blind 저장 후 공개"
}
```


<!-- luna-raw:AWE-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    1,
    17
  ],
  "auxiliary": [
    2,
    19
  ],
  "surface": [
    92,
    43
  ],
  "decisive_operation": "사회경제적배경에따른약간의차이를무관이라는완전부정으로교체한②를배제.",
  "competitor_refutations": [
    {
      "code": 43,
      "reason": "식별문제통제는주요본문내용이나②는배경차이의존재판정이다."
    },
    {
      "code": 92,
      "reason": "P-A=C계산은①확인이고정답오류는양적차이/무차이구분."
    },
    {
      "code": 19,
      "reason": "우회방법의존재는완전해결을뜻하지않으나정답②직접경로는아님."
    }
  ],
  "confidence": 0.98,
  "passage_group": "G333",
  "sdss_seen": false
}
```
