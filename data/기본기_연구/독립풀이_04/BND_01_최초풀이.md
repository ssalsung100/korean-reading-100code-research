

<!-- luna-raw:BND-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G479",
  "selected_answer": 3,
  "confidence": 0.89,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "보기 표·처리규칙",
      "evidence": "(a): {1,4},{2,3},{5,6}으로 크기2 집합3개. (b): {1,2,3,4},{5,6}으로 크기4·2 집합2개. 모든 집합의 민감속성 서로다른값은2개."
    },
    {
      "location": "ℓ 정의·삭제 예시",
      "evidence": "단일 민감값 집합은 ℓ-다양성을 만족하지 못해 삭제된다고 명시. 공식PDF에 별도 ℓ≥2 수식은 없음."
    }
  ],
  "minimal_logic_without_codes": "본문의 단일값 집합 삭제 설명을 따라 ℓ≥2인 유효 다양성 조건으로 읽으면 ㄱ은 참,ㄴ은 집합수3대2로 거짓,ㄷ은(a) k≤2·ℓ=2와(b) k=3또는4·ℓ=2가 되어 참이다.③을 선택한다.",
  "intermediate_reasoning": [
    "ㄱ 같은k·ℓ에서(b)만 더 많이 남으려면 k=3또는4이고ℓ≤2여야 하므로(a)는 모두 삭제된다.",
    "ㄴ 양쪽100%이어도(a)의 집합수3과(b)의 집합수2는 달라진다.",
    "ㄷ (b)의 가능한 중간 잔존율은4/6뿐이며 크기2 집합은 삭제되고 크기4 집합은 남는다.따라서k_b는3또는4,k_a≤2.",
    "ℓ≥2라는 해석에서 모두 서로다른민감값수가2인 집합을 남기려면 양쪽ℓ=2다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "ℓ=1도 허용한다고 읽으면ㄷ의같은ℓ결론이성립하지않아①이가능해진다.이읽기는본문의단일값집합삭제설명과의관계검토가필요하다."
  },
  "explicit_interpretive_assumption": "ℓ≥2는 별도 수식으로 직접 표기된 것이 아니라 단일값 집합을 삭제한다는 본문의 적용 설명에 근거해 채택한 해석이다.원문에 명시된 부등식으로 소급하지 않는다.",
  "countermodel_if_ell1_allowed": "k_a=2,ℓ_a=1이면(a)6개 유지;k_b=3,ℓ_b=2이면(b)4개 유지.이때ㄷ의전반조건은만족하지만ℓ값은다르다.따라서하한해석을달리하면ㄷ판정이달라진다.",
  "source_restoration": {
    "appendix": "data/기본기_연구/prepared_backlog/blind_sources/BND-hold-source-20261003-appendix.md",
    "official_crops_seen": true,
    "finding": "별도ℓ≥2표기나보기추가주석누락은확인되지않음",
    "resolved_before_answer_disclosure": true,
    "original_hold_preserved": true
  },
  "scope_limit": "기출에 제시된 가상 표의 집합 크기와 값 개수만 계산했다. 실제 개인정보 재식별은 수행하지 않았다."
}
```
