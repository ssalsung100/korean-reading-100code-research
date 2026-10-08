

<!-- luna-raw:AKT-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G232",
  "official_answer": 3,
  "blind_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2023/2023_answer_언어이해정답.pdf",
  "answer_evidence": "prepared sealed의 공식 정답 필드만 공개; SDSS 미공개",
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "logic_without_codes": "법적 권리를 인정한다고 믿으면서도 도덕적 권리를 실현하려고 다른 합법적 해석을 내세워 그 권리를 부정한다. 법 형식을 사용하는 수단과 도덕적 결과라는 목적을 분리한다.",
  "correction": "없음",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AKT-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    44
  ],
  "primary_candidates": [
    44,
    78
  ],
  "representative_primary": 44,
  "primary_uniqueness": "미확정: 도덕적 결과라는 목적 복원과 그 목적에 따른 행위 설명이 국소 중첩",
  "auxiliary": [
    70
  ],
  "surface": [
    79,
    93
  ],
  "decisive_evidence": "2문단의 도덕적 권리를 지지하는 판사, 다른 합법적인 법해석, 법적 권리가 부정되는 것처럼 판결. ③은 그 행위를 법을 위한 충실성이라고 바꾼다.",
  "operation": "합법적 해석은 도덕적 권리 실현의 수단이다. 수단의 법적 외관을 행위 목적의 법적 충실성으로 대체한 오류를 찾는다.",
  "competing_codes": [
    {
      "code": 78,
      "verdict": "유효한 공동 후보",
      "reason": "판사가 무엇을 지지하여 그 행위를 택하는가를 복원하면 동일하게 ③을 배제한다. 목적-행위 연결과44의 수단-목적을 본 사례로 분리할 수 없다."
    },
    {
      "code": 70,
      "verdict": "보조",
      "reason": "법 적용/불적용 각각의 의무 위반이 우회 선택의 배경이다. 그러나 이 대립을 삭제하고 도덕적 권리를 위해 해석을 만든다는 문장만 남겨도③ 배제 가능하다."
    },
    {
      "code": 79,
      "verdict": "소재·다른 선지",
      "reason": "법과 양심의 의무는 등장하나③의 직접 오류는 의무 규칙 적용보다 실제 행위 목적의 교체다."
    },
    {
      "code": 93,
      "verdict": "표면",
      "reason": "법적 권리를 다르게 표명한다는 의사소통 구조는 있으나③은 전달 내용의 진위보다 무엇을 위해 행동하는지를 묻는다."
    }
  ],
  "deletion_test": "법을 위해를 도덕적 권리를 지키기 위해로 바꾸면 오류 중심이 해소된다. 합법적이라는 형식을 지워도 목적 오독은 남는다.",
  "boundary_decision": "44/78 유일성 보류. 법 소재를79로 일괄 분류하지 않는다.",
  "confidence": 0.91,
  "passage_group": "G232",
  "sdss_exposed": false,
  "all_group_answer_check_complete": true,
  "quota_status": "unavailable"
}
```
