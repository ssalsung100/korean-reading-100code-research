

<!-- luna-raw:AQF-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G281",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "설명/예측의동일연역구조와깃대사례의인과설명방향구별.ⓑ는뒤비판포함문맥으로읽으며ㄴ해석범위한계보존.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AQF-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 56,
      "reason": "연역가능성과왜발생하는지설명의충분성차이"
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "깃대→그림자의인과방향은역산방향과다름"
    },
    {
      "code": 60,
      "reason": "설명과예측의동일형식"
    },
    {
      "code": 3,
      "reason": "현상발생이전/이후라는사용시점구별"
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "기하학적역산은가능하나그것만으로설명성결정못함"
    }
  ],
  "competitors": [
    {
      "code": 12,
      "refutation": "양방향값도출이가능하다고양방향인과적설명이되는것아님.조건관계와설명관계구분"
    },
    {
      "code": 74,
      "refutation": "서로경쟁하는두원인모형의관측적승패를묻는사례아님"
    },
    {
      "code": 69,
      "refutation": "깃대예시는다른영역유추로주장을옮기기보다모형충분성에대한구체반례"
    }
  ],
  "counterfactual_probe": "그림자길이로깃대높이를계산할수있어도그림자를바꿨다는이유만으로깃대높이의발생이설명되지않음.예측/설명시점차이도초기조건과현상의자리교환이아님.",
  "boundary_status": "ⓑ의잠정귀결과후속비판을같이읽음.결과자료로원인을추정하는추론일반을금지한것으로확대하지않음.",
  "confidence": 0.96,
  "passage_group": "G281",
  "sdss_disclosed": false
}
```
