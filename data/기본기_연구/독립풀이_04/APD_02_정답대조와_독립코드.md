

<!-- luna-raw:APD-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G272",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "초상화는대상그자체의실재를주목하게하는문맥적기능.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APD-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 100,
      "reason": "초상화라는확장표현을대상자체주목의기능으로해석"
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "문맥상의초상화뜻을장르명과구별"
    },
    {
      "code": 80,
      "reason": "친숙함을벗어난대상인식"
    }
  ],
  "surface": [
    {
      "code": 40,
      "reason": "배경/주대상구성비중을설명한것아님"
    }
  ],
  "competitors": [
    {
      "code": 69,
      "refutation": "두영역대응으로새결론을추론하는논증보다표현의문맥적뜻풀이"
    },
    {
      "code": 97,
      "refutation": "글쓴이표현의도와관련되지만발화행위기능이아닌어휘확장뜻"
    },
    {
      "code": 44,
      "refutation": "대상확인도구로그림을사용한다는④는실재에대한새주목과다름"
    }
  ],
  "counterfactual_probe": "초상화를대상자체가고유한존재로말하게하는그림으로풀면과일/풍경에도적용.인물이나배경생략조건을넣으면원문범위를좁힘.",
  "confidence": 0.94,
  "passage_group": "G272",
  "sdss_disclosed": false
}
```
