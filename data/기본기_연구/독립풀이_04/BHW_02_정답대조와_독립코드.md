

<!-- luna-raw:BHW-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G434",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2012/2012_answer_2012_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "제어변수·작용물질·배열/부피 상태·온도 변화의 역할을 맞춰 대응해야 한다.부피 변화와 온도 변화는 같은 단계 대응이 아니다.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 및 최초 유보 유지."
  ]
}
```


<!-- luna-raw:BHW-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G434",
  "sdss_seen": false,
  "general_task": "두 냉각장치에서 대응하는 요소의 역할 비교",
  "decisive_relation": "외부 제어→작용물질 상태→열적 변화라는 연쇄의 같은 위치끼리 대응",
  "primary": {
    "code": 45,
    "scope": "①②③",
    "reason": "입력 조절인 압력/자기장과 물질 상태 변화,온도 변화의 단계 역할을 맞춰야 한다."
  },
  "auxiliary": [
    {
      "code": 39,
      "scope": "전체",
      "reason": "서로 다른 장치의 공통 구조와 다른 구현을 동일 기준에서 비교."
    },
    {
      "code": 98,
      "scope": "①",
      "reason": "부피 변화에 대응시켜야 할 작용을 온도 변화에 잘못 귀속."
    },
    {
      "code": 44,
      "scope": "④⑤",
      "reason": "열순환이라는 수단으로 냉장고 내부 열을 외부로 옮기는 공통 목적."
    }
  ],
  "surface": [
    {
      "code": 1,
      "reason": "부피·온도의 증감이라는 양의 표면만으로 올바른 역할 대응이 정해지지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 69,
      "verdict": "국소 중첩",
      "refutation": "구조 대응이라는 유추적 행동과 겹친다.새 미지 성질을 추론하지 않는다는 이유만으로69를 전면 배제하지 않는다.45와유일주유보."
    },
    {
      "code": 46,
      "verdict": "보조",
      "refutation": "작용의 인과 연쇄는 대응 기준이지만 어느 요소가 같은 기능 단계인지 식별하는 비교가 핵심."
    },
    {
      "code": 40,
      "verdict": "주 기각",
      "refutation": "장치 구성요소를 나열하는 것만으로 부피와온도의 잘못된 대응을 고치지 못한다."
    }
  ],
  "counterfactual": "①의 온도 변화를 쌍극자의 배열 변화로 바꾸면 물질 상태의 대응이 성립하는 방향이다.두 장치에 모두 온도 변화가 있다는 이유만으로 모든 상태변수를 서로 치환할 수 없다.",
  "unresolved": "원문은 가스 냉매의 압축/팽창 과정을 짧게만 제시하므로 기체 순환의 상세 상태식을 외부에서 보충하지 않는다.45/69 유일 주 우선은 유보.",
  "confidence": 0.96
}
```
