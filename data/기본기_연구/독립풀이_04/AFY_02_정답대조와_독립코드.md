

<!-- luna-raw:AFY-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "갑은을채권을매입한보장매입자이고병과CDS를체결해위험을이전한다. 따라서보험회사병이신용위험을부담하는보장매도자여서④.",
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


<!-- luna-raw:AFY-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "logic_without_codes_fixed": "갑=기초채권보유자·보장매입자,을=기초채권발행자,병=위험부담·손실보상의보장매도자로역할을대응한다.④가일치.",
  "primary": [],
  "primary_candidates": [
    17,
    45
  ],
  "working_representative": 17,
  "auxiliary": [
    10
  ],
  "surface": [
    38,
    93
  ],
  "evidence": [
    "공식[A]갑은을채권을매입하고위험을피하려병과CDS계약.",
    "보장매도자는기초자산부도시손실보상,위험부담대가로보험료수취."
  ],
  "competing_codes": [
    {
      "code": 45,
      "reason": "위험과보험료의이전방향·역할을입출력대응으로기술하면17의주체귀속과국소중첩. 후보로보존하고유일주를강제하지않음."
    },
    {
      "code": 10,
      "reason": "⑤는부도를보험회사이득의필수조건으로잘못추가한오답이다.④직접확정은병의매도자역할대응이므로10은해당오답배제보조범위."
    },
    {
      "code": 38,
      "reason": "여러개인이등장하지만동일인여부나개체수계산이아니다. 세주체의금융계약역할을따로보존해야하며개체라는소재만으로주코드를추가하지않음."
    }
  ],
  "falsification_probe": "계약역할명을매입/매도라는일상물품거래연상으로만읽으면병을기초채권의발행자나투자자로혼동한다. 무엇을매입/매도하는지인보장을보존.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
