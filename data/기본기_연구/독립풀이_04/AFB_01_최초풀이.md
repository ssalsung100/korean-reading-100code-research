

<!-- luna-raw:AFB-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "sdss_linkage_absence_disclosed_before_blind": true,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "1문단합의알고리즘의예로작업증명이있음.",
    "원학습지이미지④는합의알고리즘이작업증명의한예라고하고O로판정."
  ],
  "minimal_logic_without_codes": "작업증명이합의알고리즘의예인방향을뒤집은문장은틀리므로X여야한다. 학생은O로표시했으므로④가부적절하다.",
  "intermediate_reasoning": [
    "①특성과마지막한계제시가있으므로O맞음.",
    "②구조설명은있지만구체응용분야소개는없어두내용을합친진술에X맞음.",
    "③장점은있지만다른기술과경쟁양상은없어X맞음.",
    "⑤체인블록집합저장컴퓨터가노드이므로O맞음."
  ],
  "most_attractive_wrong_answer": 2,
  "exact_error": "복합진술의첫절인구조분석만참인것을보고응용분야소개까지참으로승인하면학생X를틀렸다고오인한다.",
  "visual_reading": "원HWPX내BMP표를PNG로형식변환하여직접판독.1~5번호와판정O/X/X/O/O및문장대응확인. 새조판/의미보완없음.",
  "strict_blind_qualification": "사이트연결부재정보사전노출기록으로완전무오염성과제외;실제답과태그는미노출.",
  "quota_status": "unavailable"
}
```
