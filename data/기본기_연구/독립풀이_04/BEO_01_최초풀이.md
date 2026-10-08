

<!-- luna-raw:BEO-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G403",
  "selected_answer": 3,
  "confidence": 0.98,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "표 아침낮:요청자많음·콘텐츠적음·허용대기김",
    "표 저녁밤:요청자많음·콘텐츠보통·대기보통",
    "표 심야:요청자적음·콘텐츠많음·대기짧음",
    "2~7문단 방식별 장단점"
  ],
  "minimal_logic_without_codes": "소수 사용자가 많은 종류를 즉시 보려는 심야에는 사용자별 채널, 많은 사용자가 소수 콘텐츠를 오래 기다릴 수 있는 아침에는 시간분할, 그 사이 대기·콘텐츠 다양성 요구에는 데이터분할이 맞는다.",
  "intermediate_reasoning": [
    "심야는 콘텐츠당 사용자가 적어 NVOD 고정 채널이 낭비이므로RVOD.",
    "③⑤만 심야RVOD이다.",
    "저녁밤은 아침낮보다 콘텐츠 종류가 많고 허용 대기가 짧아 같은 대역으로 대기를 줄이며 콘텐츠 종류를 늘리는 데이터분할에 배정한다.",
    "아침낮은 긴 대기를 수용하고 소수 콘텐츠에 많은 사용자가 몰리므로 시간분할이 적합하다."
  ],
  "attractive_wrong": {
    "choice": 5,
    "exact_error": "대기 단축의 효익이 더 필요한 저녁밤 대신 이미 긴 대기를 허용하는 아침낮에 데이터분할을 배정해 비교 우선순위를 뒤집는다."
  },
  "scope": "정성적 조건에 따른 상대적 적합성 판정이며 구체 대역·비용 수치 없는 최적화 증명은 아니다."
}
```
