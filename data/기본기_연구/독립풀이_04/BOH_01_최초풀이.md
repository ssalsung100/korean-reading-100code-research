

<!-- luna-raw:BOH-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G489",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "공식 보기 표 효소㉣ 병합셀",
      "evidence": "효소㉣은 포르피린C→D와 유로포르피리노젠I→코프로포르피리노젠I 두 반응을 담당한다."
    },
    {
      "location": "보기 조건·표 전체",
      "evidence": "효소 결핍 시 그 효소의 기질이 축적될 수 있다.㉢결핍으로B가축적되면 자발적으로유로포르피리노젠I이된다. 혼합은㉥ E→F 결핍, 조혈기성프로토포르피린증은㉦ F→헴 결핍이다."
    }
  ],
  "minimal_logic_without_codes": "흡혈귀와 공통 증세의 원인물질은 코프로포르피리노젠I이다. 이를 생성하는 효소㉣이 결핍되면 유로포르피리노젠I에서 그 물질로 전환할 수 없으므로㉣·㉤ 결핍 상황의③이 맞는다.",
  "intermediate_reasoning": [
    "① 도스포르피린증은㉠기질 델타아미노레불린산의 축적이지㉠·㉡산물의 축적이 아니다.",
    "② ㉢산물C를 코프로포르피리노젠I의 기질로 바꿨다. 또한 만발성피부 질환은㉣ 결핍이므로 그 반응이 원활하다고 할 수 없다.",
    "④ 조혈기성프로토포르피린증은㉦기질F가 쌓이며F는㉥의 산물과 같은 물질이다.",
    "⑤ 혼합 포르피린증은㉥의 기질E가 쌓이는 경우이지㉦기질F가 주된 축적 기질이 아니다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "같은 포르피린F가㉥의 산물이면서㉦의 기질이라는 상대적 역할을 놓치면, 산물은 축적되지 않는다는 잘못된 일반화를 한다."
  },
  "source_restoration": {
    "crop": "data/기본기_연구/prepared_backlog/blind_sources/BOH_official_table_crop.png",
    "astra_direct_seen": true,
    "resolved_before_answer_disclosure": true,
    "original_hold_preserved": true,
    "finding": "㉣ 효소 및 질환 셀이 두 반응 행에 걸쳐 병합돼 있음을 직접 확인했다."
  }
}
```
