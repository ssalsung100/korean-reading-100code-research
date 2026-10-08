

<!-- luna-raw:AEZ-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "같은 공급량에서 전환율과 부반응 영향을 함께 보존하여 수소량을 비교. 정확한 B생성량 확정 불가.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 아님",
  "group_barrier": "AEX/AEY/AEZ/AFA 전체 blind raw 저장 후 answer 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AEZ-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "primary": [
    45
  ],
  "auxiliary": [
    84,
    86
  ],
  "surface": [
    43,
    46
  ],
  "logic_without_codes_fixed": "공급량→반응량(전환율)→의도한 분해에 쓰인 양→수소 생성량을 분리한다. 같은 공급량에서 A는높은전환율·부반응거의없음, B는낮은전환율·상당부반응이므로 B생성량이 적다.",
  "evidence": [
    "A 전환율0.9이상, 주반응 암모니아:수소=2:3, 부반응거의없음.",
    "B 공급10중6반응이므로 전환율0.6, 암모늄 등 부반응물 상당량 생성."
  ],
  "primary_scope": "연속 변환의 입력·중간량·출력 대응 보존. 전환율을 곧바로 수소 수율과 동일시하지 않음.",
  "auxiliary_scope": {
    "84": "전환율 분자=반응암모니아, 분모=공급암모니아. 수소몰수가 전환율 분자가 아님.",
    "86": "같은공급량에서B반응량상한과A의주반응생성량 비교. B정확량은 미정."
  },
  "competitors_rejected": [
    {
      "code": 43,
      "reason": "같은 공급량은 비교 기준을 맞추지만 다른 모든 조건을 통제하여 방식의 순수 인과효과를 추정하는 실험이 아니다. 계산상 정규화와 인과 식별을 구분."
    },
    {
      "code": 91,
      "reason": "주반응의2:3비는 일정하나 B전체 반응량에 무조건1.5를곱할 수 없다. 부반응 분배가 별도여서 단일 비례식만으로 실제 생성량을 확정하지 못함."
    },
    {
      "code": 46,
      "reason": "반응 메커니즘 세부 인과를 추론하지 않는다. 주어진 전환량·반응 분배·비율의 합성 적용이 결정적이다."
    }
  ],
  "counterfactual_test": "같은 반응량에서도 일부가 수소를 생성하지 않는 부반응물로 남으면 수소량은 달라진다. 따라서 전환율 같음→수소 생성량 같음은 일반적으로 성립하지 않는다.",
  "boundary_note": "A부반응거의없음을 정확히0으로 치환하지 않는다. 본문상A높은전환율과B낮은전환율·부반응이라는 결합 비교가 핵심이며B의 수소량9몰 확정은 금지.",
  "confidence": 0.94,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
