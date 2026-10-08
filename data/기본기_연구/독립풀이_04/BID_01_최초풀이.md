

<!-- luna-raw:BID-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G436",
  "selected_answer": 5,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BID.json",
  "necessary_information": [
    {
      "location": "양극성가설 문단",
      "evidence": "16단계표층은바깥쪽양극성결정물질분포유지,내부는그물질없음."
    },
    {
      "location": "마지막문단",
      "evidence": "표층CDX2→OCT4억제,내부OCT4→CDX2억제.접촉증가→히포활성→CDX2발현물질기능억제."
    }
  ],
  "minimal_logic_without_codes": "CDX2를바깥쪽에집중시키는양극성결정물질은표층에는남고내부에는없어두종류세포사이에양의차이가생긴다는⑤가맞다.",
  "intermediate_reasoning": [
    "①내부는접촉이커져히포활성으로CDX2발현물질기능이억제되는쪽이다.",
    "②보존분열로생긴세포는표층이므로내부처럼접촉증가에의한히포활성화를귀속할근거가없다.",
    "③표층에서는CDX2가OCT4를억제하여OCT4가점차없어진다.",
    "④내부에서OCT4는남고CDX2는줄어들므로OCT4/CDX2비율은감소방향이아니다.분모가완전히0인끝상태에서는비율수치가정의되지않으므로그상태의유한값은주장하지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "감소하는CDX2를분모로둔비율인데분자처럼읽어비율도줄어든다고오인한다.양쪽단백질의억제주체와잔류방향을함께보존해야한다."
  }
}
```
