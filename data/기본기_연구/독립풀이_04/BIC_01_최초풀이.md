

<!-- luna-raw:BIC-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G436",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BIC.json",
  "necessary_information": [
    {
      "location": "2문단",
      "evidence": "8상실배아의 분화분열로16단계 내부세포 처음생김.32내부→속세포덩어리."
    },
    {
      "location": "양극성가설 및 마지막문단",
      "evidence": "내부세포는 바깥쪽 양극성결정물질이없고 OCT4/CDX2 차이가 세포유형 분화에관여.내부세포 총수를 결정하는 물질의종류는없음."
    }
  ],
  "minimal_logic_without_codes": "어떤세포유형으로분화하는지에관여하는물질은설명하지만 그유형세포의수를결정하는물질은제시하지않았다.따라서④.",
  "intermediate_reasoning": [
    "①분화분열→내부세포→속세포덩어리 경로를알수있다.③최초내부세포는16상실배아단계.⑤분화분열이라는분열방식이명시됨.",
    "②내부세포는세포바깥쪽에쏠린양극성결정물질이없으므로표층처럼양극성분포를유지하지않는다는점이설명된다.",
    "④본문에세포수8/16/32가등장해도특정내부세포수를결정하는물질정보는별개다.모른다는것이그물질이실제로없음을뜻하지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "양극성결정물질의전체목록이미제시라는이유로내부세포의양극성존재여부도모른다고하면안된다.본문은바깥쪽에집중된결정물질의내부세포부재를명시한다."
  }
}
```
