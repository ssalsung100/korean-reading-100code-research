

<!-- luna-raw:AKE-answer_check-20260926-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G227",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "계층법은 클러스터 개수를 사전에 정하지 않아도 된다는 마지막 문단을④가 보존한다.",
  "official_answer_source": "자료/LEET_언어이해/원본/2022/2022_answer_2022_LEET_언어이해_정답표_배포용.pdf",
  "verification_scope": "정본 연결 sealed 공식답 필드 대조; 이번 단계에서 공식 PDF 답 셀 직접 판독 아님",
  "barrier_verified": "G227 전체 blind raw 저장 후 공식답 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AKE-independent_code-20260926-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    10
  ],
  "auxiliary": [
    17
  ],
  "surface": [
    3,
    96
  ],
  "judgment_reason": "계층법은 사전 개수 지정이라는 선행 요건 없이 수행 가능하다는 직접 설명을④가 보존한다. 필요 요건의 부재를 읽는10을 작업 대표로 기록하되 직접 재진술96과 독립 연산으로 중복 계수하지 않는다.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "보조",
      "reason": "개수 사전 지정은 분할법의 요건이고 계층법에는 요구되지 않음을 기법별로 귀속."
    },
    {
      "code": 3,
      "verdict": "표면",
      "reason": "미리라는 시간 표현이 있으나 개수 결정 시점의 순서 추론보다 사전 결정 필요 여부가 핵심."
    },
    {
      "code": 96,
      "verdict": "재진술 후보",
      "reason": "본문 문장을 직접 보존하는 읽기다.10과 별도 연산으로 셈하지 않으며 유일 주에 대한 일반 기준은 아직 부족."
    },
    {
      "code": 9,
      "verdict": "⑤·도식 보조",
      "reason": "수평선 높이와 추상화 수준은⑤ 오답 판정에 쓰이며④ 직접 확인의 주가 아님."
    }
  ],
  "minimal_change_test": "④를 개수를 미리 정해야 한다로 바꾸면 요건의 긍정/부정이 달라져 오답.미리라는 말만 바꾸는 선후 문제로 축소하지 않는다.",
  "confidence": 0.9,
  "passage_group": "G227",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
