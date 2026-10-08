

<!-- luna-raw:API-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G274",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "④만중국규범중심의조선대위.나머지는병렬·상대관점.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:API-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 15,
      "reason": "중국중심틀의유지/거부라는분류기준적용"
    }
  ],
  "auxiliary": [
    {
      "code": 25,
      "reason": "인용문들을두관점으로분류"
    },
    {
      "code": 75,
      "reason": "노론대위와이익독립국가관점구별"
    },
    {
      "code": 80,
      "reason": "중심·내외의관점상대성"
    }
  ],
  "surface": [
    {
      "code": 42,
      "reason": "내외단어보다중심독점의인식기준이핵심"
    }
  ],
  "competitors": [
    {
      "code": 3,
      "refutation": "인용문의연대순서를묻지않음"
    },
    {
      "code": 26,
      "refutation": "문화차이를전부소거하는배타해체가아니라세계관분류"
    },
    {
      "code": 17,
      "refutation": "조선/중국이름만으로는④와다른선지구분안됨.중국규범의독점인지확인"
    }
  ],
  "counterfactual_probe": "④의중국옷·말을보편유교예악과각나라독자성으로고치면중국중심규범색채약화.중국밖에서중화가능하다는한점만으로이익과동일시못함.",
  "confidence": 0.96,
  "passage_group": "G274",
  "sdss_disclosed": false
}
```
