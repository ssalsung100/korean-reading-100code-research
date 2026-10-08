

<!-- luna-raw:AIQ-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "blind_answer": 1,
  "official_answer": 1,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "나무그림자가벽에나타나는장면은자연의영향을인간역사의공간이받는것이다.①은인간역사가자연모습에영향준결과로방향을역전.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2024__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIR범위crop은직접검증완료",
  "barrier_verified": "AIR해소후G215blind6저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIQ-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G215",
  "primary": [
    46
  ],
  "auxiliary": [
    17,
    100
  ],
  "surface": [
    3,
    5
  ],
  "judgment_reason": "자연이나무그림자를인간역사의벽에드리우는방향을인간역사가자연모습에영향주는방향으로바꾼①. 영향의주체와수용대상을고정해인과방향검사.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "보조후보",
      "reason": "영향자/피영향자의역할귀속으로같은반전기술가능.46을구체적작업대표로채택하되전역독점주장안함"
    },
    {
      "code": 100,
      "verdict": "보조",
      "reason": "문=인간역사·자연의재생이라는보기대응사용"
    },
    {
      "code": 3,
      "verdict": "주 기각",
      "reason": "천년쇠락이라는시간보다영향방향교환이최소오류"
    },
    {
      "code": 5,
      "verdict": "보조",
      "reason": "쇠락/생성변화는배경이나①은변화유무가아닌작용방향"
    }
  ],
  "minimal_change_test": "①인간역사가자연모습에영향을 자연이인간역사의공간에영향으로고치면방향복원.선후만고쳐서는오류남음.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
