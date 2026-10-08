

<!-- luna-raw:AOQ-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G267",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2014/2014_answer_2014학년도_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "①은법이위험대출을유도했다는정부주범론을지지하므로그반박이아님.다른논거의약화강도한계는보존.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:AOQ-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 63,
      "reason": "제시증거가정부원인설을강화하는지약화하는지방향판정"
    }
  ],
  "auxiliary": [
    {
      "code": 74,
      "reason": "증권화/정부개입의대체원인설비교"
    },
    {
      "code": 46,
      "reason": "법→대출완화→거품→위기경로"
    },
    {
      "code": 73,
      "scope": "③④",
      "reason": "법과서브프라임중심전제의적용범위약화"
    }
  ],
  "surface": [
    {
      "code": 36,
      "scope": "⑤",
      "reason": "법없이위기발생은필요성에대한반례후보이나특정국가의기여0입증아님"
    }
  ],
  "competitors": [
    {
      "code": 43,
      "refutation": "국가·지역비교의완전통제자료없으므로순수법효과차이를확정못함"
    },
    {
      "code": 53,
      "refutation": "소득과무관한연체를원인차이0의증명으로바꾸면다른위험차이와파급경로를누락"
    },
    {
      "code": 62,
      "refutation": "인과연결의충분성반박은일부논거역할이나①은오히려법에서완화로연결하는근거추가"
    }
  ],
  "counterfactual_probe": "①법이한도를높이도록유도를한도를제한하도록으로바꾸면정부주범론에불리해진다.⑤는해당법없이도위기가능함을보일뿐미국내효과없음을보장못함.",
  "boundary_status": "63방향과강도분리,74대체설과43인과식별조건구별",
  "confidence": 0.95,
  "passage_group": "G267",
  "sdss_disclosed": false
}
```
