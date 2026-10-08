

<!-- luna-raw:BKE-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G453",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2019/2019_answer_2019_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "(나)는 같은 시료 영역을 더 큰 배율로 관찰한 상이다. 본문의 전류-초점 거리-배율 관계를 적용하면 (나)의 코일 전류가 더 큰 ④가 적절하다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_limit_preserved": "visual02 아래쪽 눈금의 글자가 일부 잘려 있으나 사각형 대응과 배율 증가 및 visual01 30nm 눈금은 확인 가능하다. 잘린 눈금의 단위나 정확한 확대비를 추정해 답의 근거로 사용하지 않았다."
}
```


<!-- luna-raw:BKE-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G453",
  "minimal_logic_without_codes": "동일 시료 부분이 더 크게 보이는 상에서 배율 증가를 확인하고 본문의 코일 전류 증가→초점 거리 감소→배율 증가 관계로 ④를 고른다.",
  "primary": [
    {
      "code": 46,
      "reason": "관찰한 배율 차이를 본문에 제시된 전류·초점 거리 기제로 연결한다. 원문 모형 안에서의 적용이며 모든 가능한 장치에 대한 원인의 유일 식별은 아니다."
    }
  ],
  "auxiliary": [
    {
      "code": 86,
      "reason": "표시된 물체 크기와 실제 물체 크기를 분리하고 같은 영역의 화면상 크기 증가를 읽는다."
    },
    {
      "code": 16,
      "reason": "① 배제에서 해상도를 화면상 점 크기가 아닌 구분 한계 거리로 유지한다."
    },
    {
      "code": 62,
      "reason": "⑤의 배율 변화→전자 속력 3배 감소라는 정량 결론의 근거 부족을 판정한다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "눈금과 배수는 보이지만 ④ 선택에 정확한 확대비 계산은 필요 없다."
    }
  ],
  "competing_codes": [
    {
      "code": 49,
      "rejection": "전류와 배율의 최종 방향은 표현할 수 있으나 초점 거리를 거치는 기제가 선택 근거다."
    },
    {
      "code": 43,
      "rejection": "동일 시료라는 조건은 보존하지만 그림 두 장으로 모든 실험 변수를 통제했다는 증명이나 유일한 원인 식별을 하지는 않는다."
    },
    {
      "code": 84,
      "rejection": "확대 배율을 비율로 적을 수 있어도 분모 변화 계산이 정답 핵심은 아니다."
    }
  ],
  "boundary_note": "BKE 사진으로 코일 전류만이 유일 원인이라는 보편 명제를 만들지 않는다. 제시문이 제공한 배율 조절 경로를 선택지에 적용한 것으로 제한한다.",
  "source_limit": "visual02 눈금 문자 일부 잘림 보존; 추정 확대비를 근거로 쓰지 않음.",
  "confidence": 0.9,
  "sdss_seen": false
}
```
