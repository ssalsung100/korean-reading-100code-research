

<!-- luna-raw:BDM-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G394",
  "selected_answer": 1,
  "official_answer": "①",
  "match": true,
  "official_answer_source": "data/meet_questions.jsonl (official-page-verified canonical transcript)",
  "answer_verification_scope": "봉인 공식 정답 필드 대조; 원 정답표 독립 시각 확인 미실시",
  "logic_without_codes_fixed": "지방세포는 남성 호르몬을 새로 합성하는 장소로 제시되지 않는다. 비만으로 커지는 것은 이를 여성 호르몬으로 바꾸는 작용이다.①은 입력 물질의 전환과 합성 증가를 혼동한다.",
  "original_blind_preserved": true,
  "sdss_seen": false,
  "group_blind_barrier_verified": true,
  "remaining_uncertainty": "⑤는 난소 효소 저하라는 제시 설명 방향에 따른 판단. 기질량과 효소량을 정량 결합한 생산량 보장은 주어지지 않음."
}
```


<!-- luna-raw:BDM-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G394",
  "primary_codes": [
    45
  ],
  "auxiliary_codes": [
    17,
    46,
    49,
    86
  ],
  "surface_codes": [
    1
  ],
  "decisive_operation": "지방세포의 남성호르몬 유입/소모와 여성호르몬 생성·저장을 구별하여①의 합성 증가 귀속을 배제한다.",
  "competitor_refutations": [
    {
      "code": 49,
      "reason": "증감 방향은②③⑤에 필요하지만①은 증감 부호만 반전한 것이 아니라 그 장소에서 무엇을 생성하는지부터 틀림."
    },
    {
      "code": 17,
      "reason": "지방세포/고환/난소와남성/여성호르몬의 교환은 주45의역할 판독과 중첩한다."
    },
    {
      "code": 86,
      "reason": "③남녀의혈중변화량 비교에 적용되는 오답 수용 행동.정답①에는상대량/절대량 구별 불필요."
    }
  ],
  "boundary_note": "혈중/난소내/지방세포내를 동일한 농도 변수로 합치지 않는다.효소 감소와기질증가가동시에있을때순생산량의정량단정은유보.",
  "confidence": 0.92,
  "sdss_seen": false,
  "group_answer_check_complete": true
}
```
