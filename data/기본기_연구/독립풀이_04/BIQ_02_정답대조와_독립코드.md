

<!-- luna-raw:BIQ-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G440",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "다중정체성·차별배제와기존국민국가관점전환의국소공통점을대조한다.공통점이각입장의모든세부조건동일성을뜻하지않는다.",
  "limitations": [
    "봉인공식전사답대조.원정답표시각재대조미실시.unknown strict제외.BIQ[A]범위공식복원대기."
  ]
}
```


<!-- luna-raw:BIQ-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G440",
  "sdss_seen": false,
  "general_task": "서로다른공동체입장의국소공통점·차이비교",
  "decisive_relation": "정체성차별배제와기존국가관점전환이라는두축에서공통점확인",
  "primary": {
    "code": 75,
    "scope": "전체",
    "reason": "[A]·(가)·(나)·(다)의차별·문화·국가·헌정질서에대한견해를정확히귀속."
  },
  "auxiliary": [
    {
      "code": 23,
      "scope": "④",
      "reason": "두쌍에서각기다른공통요소를찾음.전체입장의동일성을주장하지않는다."
    },
    {
      "code": 39,
      "reason": "같은비교축에서공통과차이를판별."
    },
    {
      "code": 4,
      "scope": "①③⑤",
      "reason": "특정윤리나지배문화와의결합거부를모든윤리차이불용으로,헌정원리존중을모든현상질서유지로확대하지않음."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "규범적주장이소재이나어느규범이도덕적으로옳은지평가하는것이아님."
    }
  ],
  "competing_codes": [
    {
      "code": 74,
      "verdict": "통합군유지",
      "refutation": "규범적입장이므로75만이라는배타기준은쓰지않는다.현재는가설결과예측보다명시견해귀속이다."
    },
    {
      "code": 13,
      "verdict": "국소보조",
      "refutation": "②⑤의양립불가를찾을수있지만정답④는국소교집합을확인하는경로다."
    },
    {
      "code": 63,
      "verdict": "주기각",
      "refutation": "어느입장이더설득력있는지새증거로평가하지않는다."
    }
  ],
  "counterfactual": "(가)의적대에도지속되는환대라는더강한조건을[A]에추가귀속하면원문근거가없다.④는차별배제라는한정된공통점만진술하여가능하다.",
  "source_restoration": {
    "source": "자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2017/page_012.png",
    "supplement": "data/기본기_연구/prepared_backlog/blind_sources/BIQ_range_restoration.md",
    "verified_by_primary_visual_read": true,
    "timing": "전체blind·공식답대조후SDSS전",
    "finding": "[A]는하지만이는부터마지막확장되어야한다까지최종문단전체.최초추정과일치.",
    "original_blind_preserved": true
  },
  "confidence": 0.98
}
```
