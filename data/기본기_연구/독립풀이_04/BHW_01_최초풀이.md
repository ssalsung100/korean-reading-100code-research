

<!-- luna-raw:BHW-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G434",
  "selected_answer": 1,
  "confidence": 0.96,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BHW.json",
  "necessary_information": [
    {
      "location": "1문단",
      "evidence": "가스 냉매는 압축/팽창에 따라 열 방출/흡수."
    },
    {
      "location": "3문단",
      "evidence": "자기장은 쌍극자 정렬을 바꾸어 온도 변화와 열 교환을 일으킴.두 장치 모두 내부열을 외부로 옮김."
    }
  ],
  "minimal_logic_without_codes": "대응은 압력↔자기장,기체 냉매↔자기물질,압축·팽창 상태 변화↔쌍극자 배열 변화다.온도 변화는 뒤따르는 공통 열적 상태 변화이므로 부피변화와 자기물질 온도변화를 같은 단계의 역할로 잇는①이 부적절하다.",
  "intermediate_reasoning": [
    "②는 외부 제어 조건의 대응.③은 열을 운반하는 작용물질의 대응.④는 순환 과정이라는 공통 구조.⑤는 내부에서 외부로 열을 옮기는 공통 기능.",
    "①도 부피 변화와 온도 변화가 모두 순환과 관련 있다는 넓은 공통점은 있지만 대응하는 작용 단계가 다르다.단어의 닮음이 아니라 원인/상태/열교환 역할을 맞춘다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "압력과 자기장이 물리적으로 다른 양이라는 이유만으로 대응을 부정하면 두 순환에서 외부 조절 변수라는 동일 역할을 놓친다."
  }
}
```
