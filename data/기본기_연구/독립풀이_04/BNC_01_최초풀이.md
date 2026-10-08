

<!-- luna-raw:BNC-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G479",
  "selected_answer": 5,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "k-익명성 규칙",
      "evidence": "준식별자 기준으로 이미 만든 동질집합 중 크기가k 미만인 집합을 삭제한다."
    },
    {
      "location": "지표 정의",
      "evidence": "잔존율은 남은 레코드 수/원래 레코드 수이다.개인 추정 확률과 확정 재식별을 구분한다."
    }
  ],
  "minimal_logic_without_codes": "같은 분류에서k만 바꿔 잔존율이 증가했다면 문턱을 낮춰 이전에 탈락한 더 작은 동질집합을 추가로 남긴 것이다.남아 있는 집합 크기의 최솟값은 낮아지므로⑤가 맞는다.",
  "intermediate_reasoning": [
    "① k를 낮추면 삭제가 완화돼 잔존율은 감소하는 방향이 아니다.",
    "② k를 낮추는 것이 모든 집합의 크기를 같게 만드는 작업은 아니다.",
    "③ k를 높이면 작은 집합을 제거할 뿐 남은 각 집합의 내부 레코드를 줄이는 것은 아니다.",
    "④ k는 집합 크기의 조건이며 민감속성 값을 모두 같게 만드는 처리가 아니다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "크기가 최소k 이상이라는 하한 조건을 모든 집합의 크기가 정확히k라는 등호 조건으로 바꾼다."
  },
  "scope_limit": "원본·범주화·마스킹을 고정하고k만 바꾸는 본문의 삭제 모형을 적용한다.전후의 최솟값 비교는 기존 비식별 집합이 비어 있지 않아 최솟값이 정의되는 상황에 한정한다."
}
```
