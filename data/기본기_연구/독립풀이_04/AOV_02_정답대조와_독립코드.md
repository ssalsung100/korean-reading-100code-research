

<!-- luna-raw:AOV-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G269",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "A/C비교의변화요인은각성이고사전정보는변하지않음.⑤가원인변인을교환.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false,
  "provenance_limit": "봉인원장공식페이지검증정본연결을사용.이번대조에서공식정답표원본을새로열지는않음."
}
```


<!-- luna-raw:AOV-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 43,
      "reason": "비교집단의고정요인과변경요인을명시하여효과귀속검증"
    }
  ],
  "auxiliary": [
    {
      "code": 53,
      "reason": "사전정보차이가없는A/C에서정보차이효과를설명못함"
    },
    {
      "code": 17,
      "reason": "조건표와관측칸대응"
    },
    {
      "code": 63,
      "reason": "각관측이가설을지지하는범위판정"
    }
  ],
  "surface": [
    {
      "code": 46,
      "reason": "정서원인효과지만관측차이의통제구조가필수"
    }
  ],
  "competitors": [
    {
      "code": 49,
      "refutation": "정서점수증감방향보다어떤변인을바꿨는지확인이핵심"
    },
    {
      "code": 10,
      "refutation": "각성이필요한지와충분한지를섞지않음.B무반응은각성의충분성한계일뿐필요성반증아님"
    },
    {
      "code": 36,
      "refutation": "몇칸의무반응으로각성효과0의보편결론을세우지않음"
    }
  ],
  "counterfactual_probe": "⑤사전정보제공여부를생리적각성으로고치면A/C와가/나비교의변경요인에맞는다. B/C무반응을각성무효로일반화하면A/C차이를설명못함.",
  "confidence": 0.98,
  "passage_group": "G269",
  "sdss_disclosed": false
}
```
