

<!-- luna-raw:AOY-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G270",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "fixed_logic_without_codes": "2차원평면에서일반훌라후프의몸통/고리/회전축배치불가.모든원운동불가능아님.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장확인",
  "sdss_disclosed": false,
  "provenance_limit": "봉인공식페이지검증정본연결.정답표원본별도재열람없음."
}
```


<!-- luna-raw:AOY-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 42,
      "reason": "몸통주위를두르는고리의안팎과평면내교차가능성을검토하는작업대표"
    }
  ],
  "auxiliary": [
    {
      "code": 40,
      "reason": "몸통·고리·축의배치조건"
    },
    {
      "code": 37,
      "reason": "2차원운동제약을스포츠사례에적용"
    },
    {
      "code": 69,
      "reason": "바퀴축불가와고리몸통배치의구조대응"
    }
  ],
  "surface": [
    {
      "code": 91,
      "reason": "원형이라는말이비례관계뜻하지않음"
    }
  ],
  "competitors": [
    {
      "code": 50,
      "refutation": "길이막혀이동불가라는표현으로기술가능하나생물·인과경로차단보다공간교차제약"
    },
    {
      "code": 45,
      "refutation": "입출력변환보다는공간에서구성요소를양립시킬수있는지판정"
    },
    {
      "code": 100,
      "refutation": "그림과가상세계가있어도은유해석아닌명시적기하조건적용"
    }
  ],
  "counterfactual_probe": "세번째공간방향을허용하면허리와고리의교차없는배치가가능해짐.평면내원이돌아가는모든운동을금지하는규칙은원문밖과장.",
  "boundary_status": "100코드중공간배치제약의정확대표번호미확정.42/40/37/69는다른관점의후보이며유일주확정아님.",
  "confidence": 0.86,
  "passage_group": "G270",
  "sdss_disclosed": false
}
```
