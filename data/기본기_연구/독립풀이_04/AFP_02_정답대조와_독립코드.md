

<!-- luna-raw:AFP-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "미세조정은추세자체를바꾸는것이아니라그추세를용인하면서과도한단기변동의위험을완화한다.③은자금통제로추세변경을목표로하므로범위를벗어난다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조는 이번 stage에서 수행하지 않음.",
  "group_barrier": "AFO 원그래프/범위/선지표 직접확인 후 전체6 blindraw 저장을 확인하여 answer필드만 공개.",
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


<!-- luna-raw:AFP-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "logic_without_codes_fixed": "미세조정은기초여건을반영한추세를허용한채단기과도변동위험을완화한다.③은추세변경을목표로해정책목적과범위를벗어난다.",
  "primary": [],
  "primary_candidates": [
    44,
    15
  ],
  "working_representative": 44,
  "auxiliary": [
    64
  ],
  "surface": [
    43,
    46
  ],
  "evidence": [
    "마지막문장 추세는용인하되단기급등락위험에사전/사후미세조정.",
    "③ 해외자금유출입통제로환율추세를바꿈."
  ],
  "competing_codes": [
    {
      "code": 15,
      "reason": "미세조정의목적·범위를분류기준으로삼아③의적합성을판정하는행동은44와국소중첩. 후보로보존하며유일주우위유보."
    },
    {
      "code": 43,
      "reason": "③의자금통제는정책수단의행위이지효과를식별하기위한실험변수통제가아니다. 통제라는단어로43을부여하면잘못된소재분류."
    },
    {
      "code": 46,
      "reason": "정책들이결과에영향을주지만③배제에는효과의정확한인과량을추정할필요없다. 허용된목표와다른목표를명시했다는점이결정적."
    }
  ],
  "falsification_probe": "③의추세변경목표를단기과도변동위험완화로바꾸더라도그특정수단의적합성은별도근거가필요하다. 목표오류수정만으로모든통제수단을자동승인하지않는다.",
  "generation_principle": "정책수단의이름보다무엇을바꾸고무엇을허용하는지명시해목표범위의교환을검증한다.",
  "confidence": 0.97,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
