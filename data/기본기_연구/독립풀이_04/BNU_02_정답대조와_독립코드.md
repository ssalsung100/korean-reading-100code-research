

<!-- luna-raw:BNU-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G485",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "A의 녹색광 조건은 항산화제로 생존율이0에서80으로 회복되지만 적색광에서는80으로 변하지 않는다. 따라서A가 녹색보다 적색에서 더 많은 활성산소종을 낸다는②의 비교 방향은 맞지 않는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "inference_limit_preserved": "생존율 무변화만으로 모든 분자 수준 활성산소 생성량이 엄밀히0임을 증명하지는 못한다.④⑤는 본문의 단순 광반응·독성 모형에서 읽으며 포화 효과나 미검출량을 별도로 실증한 것으로 기록하지 않는다."
}
```


<!-- luna-raw:BNU-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G485",
  "minimal_logic_without_codes": "감광제A를 고정하고 녹색/적색 및 항산화제 유무의 생존율을 비교하면 녹색에서만80%포인트 회복된다. 녹색의 활성산소 효과가 더 적다는②는 이 비교와 반대다.",
  "primary": [
    {
      "code": 43,
      "reason": "감광제·빛·항산화제 중 비교할 요인을 제외한 조건을 맞춘 대조쌍을 선택해 활성산소에 의한 성분을 구별한다."
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "항산화제가 활성산소를 제거해 사멸을 완화하는 기제와 무광 독성을 분리한다."
    },
    {
      "code": 86,
      "reason": "A 녹색0→80과적색80→80의 회복 크기를 비교한다."
    },
    {
      "code": 49,
      "reason": "생존율 회복의 방향을 활성산소 관련 사멸의 방향과 연결한다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "자외선A의32=80%×40 계산은 기저 독성 설명과 일관되지만 독립적인 곱셈 법칙이 본문에 명시된 것은 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 47,
      "rejection": "빛이나 물질이 공통으로 등장한다는 것만으로 관측 상관의 숨은 공통원인 모형을 적용하는 실험이 아니다."
    },
    {
      "code": 52,
      "rejection": "항산화제가 사멸을 억제한다는 부호 합성은 가능하나②의 결정 작업은 대조쌍 비교이며 억제의 억제 두 단계만으로 부족하다."
    },
    {
      "code": 91,
      "rejection": "활성산소량과 생존율 사이 일정 비례식을 가정하지 않는다. 회복 차이를 정확한 생성 분자량 차이로 환산하지 않는다."
    }
  ],
  "inference_limit": "표의 단순 광반응 모형에서는②를 배제할 수 있으나 생존율 무변화에서 미검출 생성량까지0으로 확정하는 것은 추가 가정이다.④⑤의 엄밀한 생성량 식별은 유보한다.",
  "confidence": 0.92,
  "sdss_seen": false
}
```
