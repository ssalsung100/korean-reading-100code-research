

<!-- luna-raw:AKU-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G232",
  "official_answer": 1,
  "blind_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2023/2023_answer_언어이해정답.pdf",
  "answer_evidence": "prepared sealed의 공식 정답 필드만 공개; SDSS 미공개",
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "logic_without_codes": "실제 판단 과정은 모호한 법의 창의적 해석이고 공식 표명은 기계적 법 적용이다. 공식 발언의 내용을 실제 과정으로 바꾸지 않는다.",
  "correction": "없음",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AKU-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    93
  ],
  "primary_candidates": [
    93,
    80
  ],
  "representative_primary": 93,
  "primary_uniqueness": "미확정: 발언 내용과 그 대상인 실제 과정을 분리하는 행동에서93/80 중첩",
  "auxiliary": [],
  "surface": [
    42,
    97
  ],
  "decisive_evidence": "4문단에서 실제 창의적 법해석을 하고도 판사는 법률을 기계적으로 적용할 뿐이라고 말한다. ①은 실제 재량과 공식 부인을 동시에 보존한다.",
  "operation": "발화자/메시지/메시지가 기술하는 실제 대상을 나누고, 실제 창의적 해석과 메시지의 기계적 적용을 각각 맞는 층위에 둔다.",
  "competing_codes": [
    {
      "code": 80,
      "verdict": "유효 공동 후보",
      "reason": "판사가 진정으로 믿는 해석과 외부에 제시한 설명·실상의 대응을 보존하는 표상 판독도 동일 연산을 설명한다."
    },
    {
      "code": 42,
      "verdict": "표면",
      "reason": "내심/공식이라는 표현은 있으나 공간적 내외나 부분 경계가 아니라 발언의 진실성 문제다. 실제 행위를 공개 행동으로 바꿔도 거짓 메시지와 구분하는 과제는 남는다."
    },
    {
      "code": 97,
      "verdict": "배경",
      "reason": "패소자를 설득하려는 발화 목적은 동기 설명이다. 설득 목적을 삭제해도 실제/공식의 대조로① 선택 가능하다."
    },
    {
      "code": 7,
      "verdict": "일반적 기술",
      "reason": "창의/기계 방식의 차이는 있으나 무엇이 실제이고 무엇이 공식 주장인지 귀속하지 않으면②·⑤를 가르지 못한다."
    }
  ],
  "deletion_test": "공식적으로는이라는 표지를 없애면①의 뒷부분을 실제 재량 부정으로 오독한다. 반대로 설득 목적을 삭제해도 정답은 그대로다.",
  "boundary_decision": "진솔하지 않은 표상 판독에서93/80 국소 중첩 유지.42를 내심이라는 어휘로 승격하지 않음.",
  "confidence": 0.91,
  "passage_group": "G232",
  "sdss_exposed": false,
  "all_group_answer_check_complete": true,
  "quota_status": "unavailable"
}
```
