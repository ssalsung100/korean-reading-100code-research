

<!-- luna-raw:AQA-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G279",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "공개평판이연결망의정보·특성표지기능을대체.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AQA-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 20,
      "reason": "정보제공기능이약한연결외에공개평판으로도실현"
    }
  ],
  "auxiliary": [
    {
      "code": 45,
      "reason": "기업평판·학교전공표지→직장/지원자특성정보"
    },
    {
      "code": 56,
      "reason": "고학력집단연결망활용낮음을대체정보원으로설명"
    }
  ],
  "surface": [
    {
      "code": 9,
      "reason": "학교·기업서열은정보표지조건이지판독서열자체가정답아님"
    }
  ],
  "competitors": [
    {
      "code": 19,
      "refutation": "연결망부족을더많은연결망으로보충한것아니라다른정보경로가역할대체"
    },
    {
      "code": 53,
      "refutation": "한미차이의순수원인을완전통제로입증한자료는아님.본문설명에따른기능추론"
    },
    {
      "code": 75,
      "refutation": "연구자간가치입장경쟁보다같은정보기능의수단차이"
    }
  ],
  "counterfactual_probe": "공개평판이직장·지원자정보를전혀주지않으면연결망활용감소설명이약해짐.대체는정보기능범위이며관계의모든효과가동일하다는뜻아님.",
  "confidence": 0.97,
  "passage_group": "G279",
  "sdss_disclosed": false
}
```
