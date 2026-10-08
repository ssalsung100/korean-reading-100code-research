

<!-- luna-raw:APB-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G271",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "A변성/B탈출/C골극성장/D추간공협착.직접우회경로와중간순서를함께보존.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false,
  "source_quality": "APB노드명은blind문자도식,화살표는blindPNG로확인.정답원본새열람없이봉인정본답연결사용."
}
```


<!-- luna-raw:APB-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 46,
      "reason": "원인과결과의방향및직접/매개경로를도식에대응"
    }
  ],
  "auxiliary": [
    {
      "code": 45,
      "reason": "각노드의들어오는/나가는연결로역할식별"
    },
    {
      "code": 17,
      "reason": "노드명과화살표역할귀속"
    },
    {
      "code": 3,
      "reason": "골극성장뒤협착이라는순서"
    }
  ],
  "surface": [
    {
      "code": 40,
      "reason": "척추구성요소소재지만배열은해부학부분위치아닌인과관계"
    }
  ],
  "competitors": [
    {
      "code": 50,
      "refutation": "추간공협착으로신경이눌리지만그래프는정보/인과전달중단을분석하는문항아님"
    },
    {
      "code": 47,
      "refutation": "공통원인분기가있어도전체판정에는합류와우회직접경로모두필요"
    },
    {
      "code": 49,
      "refutation": "단순증감방향보다중간원인의위치와직접경로유무가핵심"
    }
  ],
  "counterfactual_probe": "B의직접신경근증화살표를삭제하면A/B의초기원인둘을구별하는단서가약해진다.C/D교체는골극→협착방향을뒤집음.",
  "confidence": 0.97,
  "passage_group": "G271",
  "sdss_disclosed": false
}
```
