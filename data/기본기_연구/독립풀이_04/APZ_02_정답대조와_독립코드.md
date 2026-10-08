

<!-- luna-raw:APZ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G279",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "사회적보증서는연결망효과의구체형태.약한관계와관계없음구별.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APZ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 16,
      "reason": "용어의문맥기능을정의하여서로유사한역할대응"
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "행위자·관계·효과·부재라는범주구별"
    },
    {
      "code": 22,
      "reason": "사회적보증이연결망효과의일종"
    }
  ],
  "surface": [
    {
      "code": 69,
      "reason": "다른소재유추라기보다일반개념과적용사례의대응"
    }
  ],
  "competitors": [
    {
      "code": 1,
      "refutation": "약한정도와없음구별은③배제에필요하지만정답④의역할유사성전체를대신못함"
    },
    {
      "code": 40,
      "refutation": "효과의한종류를물리적부분으로읽으면과도"
    },
    {
      "code": 98,
      "refutation": "용어문자유사성보다개념의주체/행위/효과역할확인이핵심"
    }
  ],
  "counterfactual_probe": "사회적보증서는연결망효과전체와완전동의어가아니라구체적하위효과.문맥유사성을정의전체동일성으로확대하지않음.",
  "confidence": 0.96,
  "passage_group": "G279",
  "sdss_disclosed": false
}
```
