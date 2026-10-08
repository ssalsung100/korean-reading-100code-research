

<!-- luna-raw:BER-blind-20261002-r2-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G404",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer": false,
    "sdss": false,
    "prior_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "needed_information": [
    "본문1·6문단 소비감소→절용→민생회복",
    "보기 소비하지 않음→생산자·기술 소멸→궁핍",
    "양쪽 우물 비유의 다른 작동 관계"
  ],
  "minimal_logic_without_codes": "본문은 소비를 줄여 재물을 보존하자고 하지만 보기는 소비가 생산과 기술을 유지한다고 본다. 소비 억제의 회복 효과를 반대 인과관계로 비판하는④가 맞다.",
  "intermediate_reasoning": [
    "① 본문은 농산물 유통 억제를 주장하지 않는다.",
    "② 국가 경비가 중심 문제이며 지방 재정에만 관심을 둔 글이 아니다.",
    "③ 농업기술 퇴보는 보기의 서술이지 본문이 내세운 궁핍 원인이 아니다.",
    "④ 보기의 소비→생산 유지 논거로 본문의 절용 처방을 직접 공격한다.",
    "⑤ 보기는 사민 모두 가난해 서로 도울 길이 없다고 하므로 상호부조 우선과 맞지 않는다."
  ],
  "attractive_wrong": {
    "choice": 3,
    "exact_error": "국외 유출·농업기술 쇠퇴라는 보기에 등장하는 말을 조합하지만, 비판 대상인 본문이 기술 퇴보를 원인으로 제시한 적 없다."
  }
}
```
