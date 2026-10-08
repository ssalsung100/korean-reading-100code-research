

<!-- luna-raw:AFJ-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "음정은진동수의차가아니라높은값/낮은값이다. P-Q=550/440=5/4, Q-R=660/550=6/5이며1.25>1.2이므로P-Q가더넓다.②의더좁다는틀림.",
  "official_answer_source": "sealed canonical answer 기계 연결; 이번stage에서공식배포답표직접대조아님.",
  "group_barrier": "G194 전체 유효blindraw저장확인후 answer필드만공개. 원문범위·그림·밑줄hold는후속직접확인으로해소하고최초기록보존.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "source_boundary_residue": "AFK말미##2018학년도잔재보존;group식별미확정"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFJ-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "logic_without_codes_fixed": "P-Q와Q-R의주파수차는둘다110Hz이나음정은각높은진동수/낮은진동수다.550/440=5/4와660/550=6/5를비교하면전자음정이더넓어②가틀리다.",
  "primary": [
    84,
    86
  ],
  "primary_roles": {
    "84": "음정을차가아닌비율로정의하고서로다른분모440과550으로정규화.",
    "86": "정규화한비율5/4와6/5의크기를비교."
  },
  "auxiliary": [
    15,
    32
  ],
  "auxiliary_scope": {
    "15": "③약분된3/2가차를리노의기준에맞는지확인.⑤본문순서대로옥타브2/1과단3도6/5의협화도비교.",
    "32": "④P의2배부분음과S기본음이880Hz로겹침. 두음의전체동일성으로확대하지않음."
  },
  "surface": [
    87,
    91
  ],
  "evidence": [
    "공식표P440Q550R660S880. 공식[A]높은진동수/낮은진동수로음정을표현한다고명시.",
    "①장3도5/4,③완전5도3/2,⑤옥타브2/1과단3도6/5."
  ],
  "competing_codes": [
    {
      "code": 87,
      "reason": "진동수차110Hz가같다는것은음정의같음이나좁음을뜻하지않는다. 변화량과비율을혼동하면정답판정실패."
    },
    {
      "code": 91,
      "reason": "비례관계를새로추정하는문제가아니라주어진비의정의를서로다른기준값에적용한다. 기본음정수배는④에관련되나②결정점아님."
    },
    {
      "code": 15,
      "reason": "장3도·협화음정의유형기준은①·③판정에쓰이지만②는유형명암기만으로충분하지않고실제비율의대소를보존해야한다."
    }
  ],
  "falsification_probe": "분모를고정했을때는진동수차와비율의대소가함께변할수있지만여기서는비교쌍의기준진동수가다르다. 같은차⇒같은음정은반증된다.",
  "generation_principle": "같은절대차·다른기준값을주어차와비율을갈라놓고,비율의대소와약분분모·분자의작음에따른협화도도별개로판정하게한다.",
  "confidence": 0.99,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
