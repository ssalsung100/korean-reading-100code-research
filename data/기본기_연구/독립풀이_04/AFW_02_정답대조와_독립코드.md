

<!-- luna-raw:AFW-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G196",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "맹신하지않음은무조건믿지않고검토한다는뜻인데가리지않음은구별·선별하지않는뜻이어서치환하면비판적수용을보존하지못한다.⑤.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조는 이번 stage에서 수행하지 않음.",
  "group_barrier": "전체6 blindraw 저장 확인 후 answer필드만 공개.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFW-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G196",
  "logic_without_codes_fixed": "맹신하지않음은무조건믿지않는태도이고가리지않음은선별하지않는태도다. 같은부정형을유지해도부정되는행위가달라져주체적수용의뜻을보존하지못한다.",
  "primary": [],
  "primary_candidates": [
    96,
    39
  ],
  "working_representative": 96,
  "auxiliary": [],
  "surface": [
    33,
    63
  ],
  "evidence": [
    "마지막문단서양의학을맹신하지않고주체적으로수용.",
    "⑤가리지로바꾸면가리지않고수용한다는뜻."
  ],
  "competing_codes": [
    {
      "code": 39,
      "reason": "원표현과교체표현의문맥의미를비교하는행동은96과국소중첩. 유일주번호확정대신후보/대표보존."
    },
    {
      "code": 33,
      "reason": "두표현모두않고를동반하지만같은명제를두번부정한것이아니다. 부정의외형만으로상쇄·동치판정못하며맹신과선별의어의차이를확인해야함."
    },
    {
      "code": 63,
      "reason": "비판적으로수용한다는태도가소재이지만어떤새근거가논증을약화하는지를평가하지않는다. 문맥어휘치환가능성을묻는다."
    }
  ],
  "falsification_probe": "않고라는형식이같다는것만으로뜻이같다면맹신하지않음과선별하지않음을같게보게된다. 술어내용이고정되지않은부정형비교는동치근거가될수없다.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
