

<!-- luna-raw:APX-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G278",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "동등설명력과성공한허구존재자는성공에서실재믿음으로의연결을약화.실패이론존재는직접반박아님.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:APX-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 63,
      "reason": "설명성공이실재믿음을뒷받침한다는논증을약화하는자료선택"
    }
  ],
  "auxiliary": [
    {
      "code": 62,
      "reason": "성공→참/실재연결의충분성에의문"
    },
    {
      "code": 74,
      "scope": "ㄷ",
      "reason": "동등하게성공한대체이론의경쟁"
    },
    {
      "code": 36,
      "scope": "ㄹ",
      "reason": "성공하지만존재자는허구인반례후보"
    }
  ],
  "surface": [
    {
      "code": 81,
      "reason": "존재론명제지만철학적입장자체를직관으로선택하지않음"
    }
  ],
  "competitors": [
    {
      "code": 73,
      "refutation": "과학성공이라는사실을없다고부정하지않고성공에서실재로가는연결을문제삼음"
    },
    {
      "code": 18,
      "refutation": "상이한이론이동등설명한다고반드시논리모순이라는전제는없음"
    },
    {
      "code": 4,
      "refutation": "실재론을모든실패이론까지참이라는전칭명제로바꿔ㄴ을선택하면허수아비화"
    }
  ],
  "counterfactual_probe": "ㄴ을실패이론많다가아니라성공이론의존재자가허구로확인됨으로바꾸면ㄹ처럼직접약화.ㄷ의동등성만으로유일선택불가이지모든이론거짓은아님.",
  "confidence": 0.96,
  "passage_group": "G278",
  "sdss_disclosed": false
}
```
