

<!-- luna-raw:AEY-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "MCH의 추가 수소만 최소6원자로 암모니아의3원자보다 많음.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 아님",
  "group_barrier": "AEX/AEY/AEZ/AFA 전체 blind raw 저장 후 answer 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AEY-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "primary": [
    86
  ],
  "auxiliary": [
    40
  ],
  "surface": [
    31,
    92
  ],
  "logic_without_codes_fixed": "MCH 한 분자에 새로 붙은 수소만6원자이므로 전체 수소 원자 수는6이상이고 암모니아3원자보다 많다.",
  "evidence": [
    "톨루엔 한 분자에 수소 분자3개, 각 수소 분자는 탄소-수소 결합2개 형성.",
    "암모니아 분자당 수소 원자3개."
  ],
  "primary_scope": "정확한 전체값 대신 하한으로 크기 비교를 확정",
  "auxiliary_scope": "분자3개를 원자6개로 바꾸기 위해 구성 단위를 유지. MCH전체와 새로 붙은 부분의 크기를 구분.",
  "competitors_rejected": [
    {
      "code": 31,
      "reason": "집합 수와 원소 수라기보다 분자를 이루는 원자 구성 단위다. 단위 혼동이라는 넓은 동치 기술은 가능하나 집합 개수의 별도 연산을 추가하지 않음."
    },
    {
      "code": 92,
      "reason": "분자식 전체를 알고 정확한 값으로 계산할 필요가 없다. 원문의 결합 수만으로 하한 비교 가능."
    },
    {
      "code": 39,
      "reason": "두 물질 속성 비교라는 발문 수준 설명은 맞으나 정답④의 결정적 중간 행동은 수소 원자 수 하한 산출이다."
    }
  ],
  "counterfactual_test": "톨루엔에 원래 수소가 몇 개 있는지 바꾸어도 새로 붙는6개만 유지하면④의 비교는 변하지 않는다. 따라서 정확한MCH 전체 분자식 암기는 불필요.",
  "boundary_note": "전체량이 불명인 상태에서도 하한이 상대의 확정값을 초과하면 비교를 확정할 수 있다. 부분량을 전체량의 정확한 값으로 단정하지 않는다.",
  "confidence": 0.97,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
