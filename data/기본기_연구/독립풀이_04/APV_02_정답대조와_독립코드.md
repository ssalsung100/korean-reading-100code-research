

<!-- luna-raw:APV-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G278",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "실재론의내용보다과학성공을통한실재론정당화가핵심질문.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APV-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 60,
      "reason": "실재론을옹호하는논증의중심질문복원"
    }
  ],
  "auxiliary": [
    {
      "code": 56,
      "reason": "과학의성공을설명하는실재론의설명력"
    },
    {
      "code": 64,
      "reason": "개별이론진위와실재론자체정당화범위구별"
    },
    {
      "code": 74,
      "reason": "다른철학적관점보다성공을잘설명하는지비교"
    }
  ],
  "surface": [
    {
      "code": 81,
      "reason": "실재존재는명제내용이지만글핵심은믿음정당화"
    }
  ],
  "competitors": [
    {
      "code": 16,
      "refutation": "실재론정의는중간설명일뿐글전체핵심을다담지못함"
    },
    {
      "code": 77,
      "refutation": "수많은과학자가받아들인다는빈도귀납이아님"
    },
    {
      "code": 80,
      "refutation": "믿음의대상은중요하나무슨이유로믿는지를복원해야함"
    }
  ],
  "counterfactual_probe": "실재론정의만남기고과학성공을설명하는마지막논증을삭제하면①의핵심성이사라짐.④는정의내용이지만옹호질문을포괄못함.",
  "confidence": 0.96,
  "passage_group": "G278",
  "sdss_disclosed": false
}
```
