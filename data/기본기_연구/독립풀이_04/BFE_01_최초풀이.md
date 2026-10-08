

<!-- luna-raw:BFE-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G409",
  "selected_answer": 2,
  "confidence": 0.8,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "1문단 개별 정당의 여론 조직화 평가와 정당 체계의 상호작용 분석 구별",
    "정당 수가 이념 분포·안정도 지표라는 설명"
  ],
  "minimal_logic_without_codes": "발문 대상이 문맥상 정당 수 산정이라면 그 역할은 정당 체계 분석이며 개별 정당의 여론 전달 평가와 구별된다.",
  "intermediate_reasoning": [
    "①③④⑤는 정당 체계와 그 지표의 의의에 해당한다.",
    "②는 개별 정당 분석의 기능을 정당 체계 차원의 지표에 옮긴다."
  ],
  "attractive_wrong": {
    "choice": 3,
    "exact_error": "정당 수라는 수량 지표만 생각하면 상호작용 분석과 무관해 보이나 본문이 그 분석의 핵심 역할이라고 연결한다."
  },
  "source_gap": "본문 핵심 대상과 발문 대상이 [시각 자료1]로 치환됐으나 제공된 visual01에는 BFF 보기만 있다. 정확 표지·대상 문자열이 누락되어 조건부 풀이로 보존하고 blind 성공으로 확정하지 않는다. group blind 완료 후 정본 복원 필요."
}
```
