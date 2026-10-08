

<!-- luna-raw:AKH-answer_check-20260926-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G228",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "벌리가 주주의 유일 청구권을 부정하는 것과 당장 회사법상 신인의무 대상을 확대해도 된다는 것은 다르다. 준비가 없는 상황에서는 주주로 한정해야 한다는 명시적 제한에④가 어긋난다.",
  "official_answer_source": "자료/LEET_언어이해/원본/2022/2022_answer_2022_LEET_언어이해_정답표_배포용.pdf",
  "verification_scope": "정본 연결 sealed 공식답 필드 대조; 이번 단계에서 공식 PDF 답 셀 직접 판독 아님",
  "barrier_verified": "G228 전체 blind raw 저장 후 공식답 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AKH-independent_code-20260926-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    12
  ],
  "auxiliary": [
    64,
    79
  ],
  "surface": [
    44
  ],
  "judgment_reason": "법적 근거·사회적 수용 준비가 없는 경우 신인의무 대상을 확장하지 말라는 조건부 규범을④가 누락한다. 공동체 지향의 궁극 원칙을 회사법상 즉각적 의무 확장에 적용한 영역 교체도 포함.",
  "competing_codes": [
    {
      "code": 64,
      "verdict": "보조·주 후보",
      "reason": "회사법과 회사법 바깥 영역을 나누는 것이④ 오류 설명에 중요.12의 준비 조건 검사와 겹치며 유일 주 우선성 단정 안 함."
    },
    {
      "code": 79,
      "verdict": "보조",
      "reason": "확장해서는 안 된다는 금지와 한정해서는 안 된다는 금지 대상 반전을 확인."
    },
    {
      "code": 44,
      "verdict": "배경",
      "reason": "주주 보호가 공동체 이익을 위한 출발점이지만④에서는 준비 없는 상황에서 범위를 확대한다는 조건 오류가 직접적."
    },
    {
      "code": 4,
      "verdict": "주 기각",
      "reason": "유일한 청구권 부정의 양화 자체는 벌리와 맞으며 그로부터 무조건 의무 확대를 도출한 연결이 문제."
    }
  ],
  "minimal_change_test": "④의 결론을 준비 없는 상황에서는 주주로 한정해야 한다로 바꾸면 본문의 현실적 제약을 복구한다. 궁극 공동체 지향을 철회할 필요는 없다.",
  "confidence": 0.94,
  "passage_group": "G228",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
