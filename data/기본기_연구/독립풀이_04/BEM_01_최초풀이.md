

<!-- luna-raw:BEM-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G403",
  "selected_answer": 5,
  "confidence": 0.95,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "2문단 RVOD 사용자별 채널",
    "4문단 시간분할의 동일 콘텐츠 전체 반복",
    "5문단 데이터분할의 블록수=채널수·블록크기2배 증가"
  ],
  "minimal_logic_without_codes": "같은 전송률로 블록을 보내는 비교에서는 반복시간은 블록크기에 비례한다. 다음 블록의 크기가2배이므로 주기도2배다.",
  "intermediate_reasoning": [
    "① RVOD는 사용자 수에 비례해 총 데이터양이 증가한다.",
    "② 시간분할은 선택한 채널의 전체 콘텐츠를 받으므로 데이터분할처럼 블록마다 채널을 바꾸지 않는다.",
    "③ 서로 다른 블록을 반복하는 것은 데이터분할이다.",
    "④ 전체 길이를 채널수만큼의2배 증가 블록으로 나누므로 첫 블록 크기도 채널수에 종속된다.",
    "⑤ 각 채널의 전송률이 같다는 통상 비교 모형에서 블록크기와 반복주기가 함께2배가 된다."
  ],
  "attractive_wrong": {
    "choice": 4,
    "exact_error": "첫 블록을 적당한 크기로 만든다는 표현을 임의 자유 선택으로 읽고 전체 콘텐츠와 채널수의 합 제약을 삭제한다."
  },
  "uncertainty": "⑤의 정확한2배 주기는 동일 채널 전송률을 전제한다. 본문은 최소2배 이상이라는 하한도 제시하므로 서로 다른 채널 전송률까지 허용하면 자동 성립하지 않는다."
}
```
