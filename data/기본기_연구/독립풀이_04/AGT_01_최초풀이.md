

<!-- luna-raw:AGT-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G201",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "보기:카메라는실제피사체반사광과컬러이미지를이용해검출된사용자의골격이미지를제공.",
    "본문:동작추적센서는사용자동작을파악,HMD는시차영상으로가상공간입체감전달.",
    "원그림:얼굴은머리쪽연결점하나로표시되며표정의세부변화에대응하는점들이없음."
  ],
  "minimal_logic_without_codes": "키넥트센서가파악하는것은실제피사체사용자의입체·동작정보다. 가상공간물체들사이거리측정으로입체감을구현한다는①은측정대상과장치역할을바꿨다.",
  "intermediate_reasoning": [
    "② 사용자춤동작정보를아바타동작에적용가능.",
    "③ 동작추적은자세,관성측정은속도변화율을담당.",
    "④ 주어진골격의연결점배치만으로눈·입등표정세부변화를전달할수없음.",
    "⑤ 적외선입체와RGB컬러를결합한골격정보로사용자동작파악."
  ],
  "most_attractive_wrong_answer": 4,
  "exact_error": "RGB원본컬러영상에얼굴정보가있을수있다는사실을25개연결점으로만된골격이미지에모두보존된다고확대하면④를틀리다고오인한다. 제한대상은전체센서의모든정보가아니라골격이미지다.",
  "visual_reading": {
    "source": "data/기본기_연구/prepared_backlog/blind_sources/assets/G201_Q16_figure.png",
    "findings": "머리·목·어깨·팔다리등의연결점을직접확인. 얼굴의눈입상세표정점없음. 그림밖기술성능으로보강하지않음."
  },
  "quota_status": "unavailable"
}
```
