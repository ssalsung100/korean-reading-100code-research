

<!-- luna-raw:AQU-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G286",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "관습의 독자 형성은 법적 효력의 독립성을 보장하지 않는다.ⓓ는 입법 훼손 비용으로㉠,ⓒ는 대표성 간극으로㉡을 비판한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "AQT",
    "AQU",
    "AQV"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:AQU-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G286",
  "primary": [
    63
  ],
  "auxiliary": [
    75,
    62,
    88
  ],
  "surface": [
    19,
    79
  ],
  "decisive_operation": "제시된 진술이 각 입장의 근거나 결론에 반대 방향의 영향을 주는지 판정하고 관습 형성 사실과 법적 효력 사이의 관련성 간극을 확인한다.",
  "competing_codes": [
    {
      "code": 73,
      "rebuttal": "ⓒ는 대표 입법 의사와 실제 국민 의사의 일치를 흔들지만ⓓ는 전제를 거짓이라 하기보다 드문 이익 대비 제도 훼손 비용을 비판한다. 둘을 모두 전제 부정으로 단순화하지 않는다."
    },
    {
      "code": 62,
      "rebuttal": "ⓐ는 형성 자율성을 인정해도 효력 제한이 가능한 탓에 반론 관련성이 부족하다. 이 국소 단계는 보조이며 전체는 두 반론의 지지 방향 판단이다."
    },
    {
      "code": 88,
      "rebuttal": "ⓓ의 적은 해결 이익/큰 입법 훼손 위험 비교에 적용되나ⓒ의 대표성 비판까지 비용편익으로 바꾸지는 않는다."
    }
  ],
  "boundary_note": "반론은 상대 결론을 논리적으로 불가능하게 만드는 결정적 반증만을 뜻하지 않는다. 부적당하다는 비교 평가도 약화로 성립한다.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
