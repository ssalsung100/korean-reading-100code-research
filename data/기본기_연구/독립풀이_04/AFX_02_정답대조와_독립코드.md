

<!-- luna-raw:AFX-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "발행자의지급능력이커지면미지급가능성인신용위험은낮아지는방향이다.②는반대로높아진다고하므로틀림.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조는 이번 stage에서 수행하지 않음.",
  "group_barrier": "AFY공식범위와AFZ원표직접확인후전체5 blindraw저장검증,answer필드만공개.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "uncertainty_preserved": null,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFX-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "logic_without_codes_fixed": "발행자의지급능력이높아지면미지급가능성인신용위험은낮아지는관계를②가높아짐으로뒤집는다.",
  "primary": [
    49
  ],
  "auxiliary": [
    16
  ],
  "surface": [
    2,
    46
  ],
  "evidence": [
    "신용위험은지급능력부족등으로이자·원금미지급가능성. 지급능력최상은최고등급,위험클수록낮은등급."
  ],
  "competing_codes": [
    {
      "code": 2,
      "reason": "위험정의가가능성을포함하지만②는가능을필연으로바꾼것이아니라지급능력과위험의증감방향을반전.⑤의약속≠확정지급은별도오답확인범위."
    },
    {
      "code": 46,
      "reason": "지급능력이미지급위험에영향을미치는인과적설명은가능하나주어진관계외의중간경로를추가복원하지않는다. 방향적용을대표49로기록."
    },
    {
      "code": 86,
      "reason": "높고낮음을비교하므로넓은수량비교기술은가능하지만실제오류는두변수간반대방향을같은방향으로바꾼것. 독립비교값계산은없음."
    }
  ],
  "falsification_probe": "보장매도자의지급능력과CDS프리미엄관계는같은지급능력증가라도동방향이다. 지급능력이라는변수이름만보고최종변수와방향을생략하면안됨.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
