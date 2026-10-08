

<!-- luna-raw:AGS-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "공식[A]crop은모션트래킹시스템구성·역할에서HMD장면변경·체험현실감까지문단전체.",
    "문단후반:가상환경변화에따라트레드밀속도·방향·기울기가변경되기도함."
  ],
  "minimal_logic_without_codes": "아바타가경사로를만나는환경변화에따라트레드밀기울기가변경될수있다는③은본문허용가능성을적용한다.",
  "intermediate_reasoning": [
    "① 관성측정은속도변화율·회전속도,뛰는힘은압력센서이므로역할교환.",
    "② HMD장면은사용자·트레드밀변화의결과이며바닥제어주체는컴퓨터.",
    "④ 사용자동작→아바타동작의동기화방향을역전.",
    "⑤ 사용자의방향이센서·컴퓨터를통해바닥제어에반영되는것과아바타환경변화조건을섞어아바타방향이사용자방향을정한다는별도경로를만듦."
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "가상환경변화에따른바닥변화가능이라는문장으로아바타의임의방향전환→바닥→사용자방향전환경로전체를보장할수없다. 사용자동작과가상환경이라는서로다른입력을혼동.",
  "visual_verification": "data/기본기_연구/prepared_backlog/blind_sources/AGS_A_range_official_crop_20260920.png의대괄호·첫끝문장직접확인. 최초rangehold보존.",
  "quota_status": "unavailable"
}
```
