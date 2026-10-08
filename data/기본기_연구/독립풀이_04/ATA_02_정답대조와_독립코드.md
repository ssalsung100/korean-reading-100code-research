

<!-- luna-raw:ATA-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G305",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "위험 증가와 전원 발병, 관찰군 특성과 치료 효과를 구별한다. 본문 연구에 비춘 가상 선지 평가로 제한한다.",
  "official_answer_source": "sealed/answer_sdss.jsonl 공식 정답 필드; official-page-verified canonical transcript",
  "group_blind_barrier_verified": [
    "ASY",
    "ASZ",
    "ATA"
  ],
  "sdss_seen": false
}
```


<!-- luna-raw:ATA-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G305",
  "primary": [
    2
  ],
  "auxiliary": [
    4,
    43,
    49
  ],
  "surface": [
    88
  ],
  "decisive_operation": "연구의 위험 증가·감소를 가능한 효과로 해석하고 전원 발병·치료 필요성 확정으로 강화하지 않는다.ⓓ에서는 선택 편향과 치료 효과를 분리한다.",
  "competing_codes": [
    {
      "code": 4,
      "rebuttal": "모두 발병이라는 양화도 함께 바뀌므로2와 중첩한다. 가능성 증가와 전칭 결과를 따로 기록한다."
    },
    {
      "code": 43,
      "rebuttal": "ⓓ 배제의 핵심은 교란 변수이나ⓐⓒ 직접 수용은 위험 방향·양상 해석이다."
    },
    {
      "code": 88,
      "rebuttal": "실제 개인의 종합 비용편익 계산 자료는 없다. 연구 수치로 개인 처방을 결정하는 과업으로 바꾸지 않는다."
    }
  ],
  "boundary_note": "ⓑ는 이 연구에서 해당 금기를 도출할 근거가 없다는 의미이며 실제 임상 금기의 유무를 판정하지 않는다.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
