

<!-- luna-raw:AOM-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G266",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2013/2013_answer_2013_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "법의근거와법/선관계전도를단순전통연장으로바꿈.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AOM-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 5,
      "reason": "고전관계의유지가아닌법/선관계전환"
    }
  ],
  "auxiliary": [
    {
      "code": 8,
      "reason": "선에따른법에서법에따른선으로규정의우선방향변화"
    },
    {
      "code": 81,
      "reason": "존재본질근거와선험실천이성근거구별"
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "이전/이후가있지만시간만맞춰도근거전도를놓칠수있음"
    }
  ],
  "competitors": [
    {
      "code": 19,
      "refutation": "자연법위기에대한해결기획이라는구조가있으나전통의내용단순보충이아님"
    },
    {
      "code": 75,
      "refutation": "들뢰즈의칸트해석을귀속하되정답은옛근거연속성단정"
    },
    {
      "code": 26,
      "refutation": "법/선을서로배타적존재로만드는것아니며정당화관계방향변화"
    }
  ],
  "counterfactual_probe": "①전통을연장한을기존관계를재규정한으로고치면참.새근거가같은문제를다룬다고옛이론을그대로잇는것아님.",
  "confidence": 0.94,
  "passage_group": "G266",
  "sdss_disclosed": false
}
```
