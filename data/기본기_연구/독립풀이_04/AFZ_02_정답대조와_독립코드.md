

<!-- luna-raw:AFZ-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "같은기초등급에서가>나. 같은매도자등급AA-에서나>라. 같은기초BBB-에서매도자등급AA->A+>A-이므로라>마>다. 전체가>나>라>마>다여서둘째나는②.",
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


<!-- luna-raw:AFZ-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "logic_without_codes_fixed": "두요인의영향크기가수치로주어지지않아도한요인을같게둔쌍의순서를연결해가>나>라>마>다를얻는다. 둘째나는②.",
  "primary": [
    43,
    86
  ],
  "primary_roles": {
    "43": "가/나의기초등급BB+고정,나/라의매도자등급AA-고정,라/마/다의기초등급BBB-고정.",
    "86": "각조건부대소를추이적으로연결해전체순서와두번째를선택."
  },
  "auxiliary": [
    49,
    17,
    9
  ],
  "auxiliary_scope": {
    "49": "기초등급하락→위험상승→프리미엄상승,매도자등급상승→프리미엄상승이라는방향적용.",
    "17": "두신용등급의소유주·역할보존.",
    "9": "AAA>AA>A>BBB>BB및동범주+>무표지>-의서열을이용. 따로수치간격을부여하지않음."
  },
  "evidence": [
    "공식표가BB+/AAA,나BB+/AA-,라BBB-/AA-,마BBB-/A+,다BBB-/A-.",
    "본문은다른요인동일시각방향,보기는나머지조건동일을명시."
  ],
  "competing_codes": [
    {
      "code": 45,
      "reason": "두입력의함수로표현가능하나수치함수가주어지지않았다. 순서를정하는핵심은동일조건쌍을고르고서열을연결하는것이며임의함수값계산은불필요."
    },
    {
      "code": 84,
      "reason": "프리미엄이요율이지만이문항은분자분모의값이나비율계산을요구하지않는다. 요율이라는소재와실제순위행동구분."
    },
    {
      "code": 91,
      "reason": "등급차가얼마만큼의프리미엄차를만드는지모르고비례관계도없다. 영향방향만으로비교가능한쌍의연결을사용한다."
    }
  ],
  "falsification_probe": "기초자산위험도높고매도자지급능력은낮은두거래만주어져효과가상충하면방향정보만으로순위가보장되지않는다. 현표는고정조건다리인나/라가있어전체순서가정해짐.",
  "boundary_note": "43을실험적순수인과효과추정에만한정하지않는다. 이문항의다변수조건부순위비교도고정된요인을명시하는실제행동이다. 공급량단순정규화만으로43을주로올리는것과구별.",
  "confidence": 0.99,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
