

<!-- luna-raw:AKJ-answer_check-20260926-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G228",
  "blind_answer": 2,
  "official_answer": 5,
  "matches": false,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "준공공회사는 소유와 지배가 이미 분리된 현대 회사 구조를 지칭한다. 1·2차 뉴딜은 그 구조에서 재산권을 보호하고 공동체 이익을 구현하는 제도이지 그 구조로의 변화 자체를 추구한다고 본문이 말하지 않는다.⑤가 목적을 바꾼다.②는 1차 개혁의 회사법상 주주 이익 보호 원칙을 말하며 그것만이 궁극 목적이라는 배타적 주장이 아니다.",
  "official_answer_source": "자료/LEET_언어이해/원본/2022/2022_answer_2022_LEET_언어이해_정답표_배포용.pdf",
  "verification_scope": "정본 연결 sealed 공식답 필드 대조; 이번 단계에서 공식 PDF 답 셀 직접 판독 아님",
  "barrier_verified": "G228 전체 blind raw 저장 후 공식답 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable",
  "error_analysis": "blind에서⑤의 정의 충돌을 정확히 발견했으나 일관된 공동체 지향이라는 글 전체 주제를 우선하여 명시되지 않은 넓은 뜻으로 구제했다. 반대로②에 유일한 궁극 목적이라는 말을 덧붙여 기각했다. 결과적으로 명시 정의는 느슨하게, 경쟁 선지는 과도하게 강하게 읽었다.",
  "correction_basis": [
    "2문단: 이런 의미에서 소유와 지배가 분리된 현대 회사를 준공공회사라고 부름",
    "마지막 문단: 주주 이익을 우선할 신인의무는 공동체 지향의 현실적 출발점으로 허용",
    "보기:1차는 실제로 주주 신인의무·재산권 엄격 보호 원칙 확립"
  ],
  "initial_ambiguity_preserved": "blind의②선택·0.90확신·⑤문구 의심 그대로 보존. 공식답 대조 후 수정이며 새로운 blind 성과 아님.",
  "remaining_limit": "공식답 필드와 원문 재검토에 의한 교정. 공식 해설의 이유를 읽은 것은 아님."
}
```


<!-- luna-raw:AKJ-independent_code-20260926-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    16
  ],
  "auxiliary": [
    17,
    44
  ],
  "surface": [
    5,
    63
  ],
  "judgment_reason": "공식답 대조 후 고정된 구조: 준공공회사의 정의는 소유와 지배의 분리이다.⑤는 이미 주어진 회사 구조를 개혁이 새로 추구하는 변화 목표로 바꾸므로16의 정의 보존과17의 구조/정책 목표 귀속을 함께 요구.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "보조·주 후보",
      "reason": "회사 구조의 명칭을 정책의 목적에 옮기는 층위 교체.16과 같은 오류 위치를 기술하여 유일 주 전역 우선성 확정 안 함."
    },
    {
      "code": 44,
      "verdict": "보조",
      "reason": "뉴딜의 목적은 구조를 바꾸는 것이라고 명시되지 않고 구조 아래에서 재산권/공동체 이익을 구현하는 것. 목표 왜곡을 구체화."
    },
    {
      "code": 5,
      "verdict": "표면",
      "reason": "변화를 추구한다는 말은 있지만 시간 변화 유무보다 무엇으로의 변화인지 정의를 고정해야 함."
    },
    {
      "code": 63,
      "verdict": "발문 구조",
      "reason": "벌리의 반응을 묻지만 근거는 개념 내용의 부당 확대. 정책에 찬반하는 일반 논쟁만으로⑤ 정답을 못 얻음."
    }
  ],
  "minimal_change_test": "⑤의 준공공회사로의 변화를 공동체 이익을 위한 회사 운영의 제도화로 바꾸면 두 정책의 일관성을 평가할 수 있다.②에 오로지/궁극적으로라는 말을 임의로 추가하면 별개의 오답을 만들게 됨.",
  "original_blind_preserved": true,
  "post_answer_correction": true,
  "confidence": 0.95,
  "passage_group": "G228",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
