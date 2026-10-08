

<!-- luna-raw:AJP-answer_check-20260922-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G222",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "국가는 단속하고 민간 기관은 국가보조금을 받으며 수용·규율 기능을 수행했다. 두 기관은 정책 수행에서 역할을 나누었으므로 ③이 맞다.",
  "official_answer_source": "자료/LEET_언어이해/원본/2022/2022_answer_2022_LEET_언어이해_정답표_배포용.pdf",
  "verification_scope": "정본 연결 검증된 sealed 공식답 필드 대조. 부모가 PDF 답 셀을 직접 판독한 것은 아님.",
  "barrier_verified": "G222 AJP·AJQ·AJR의 blind raw 3건 저장 후 공식답 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJP-independent_code-20260922-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G222",
  "primary": [],
  "primary_candidates": [
    96,
    17
  ],
  "working_representative": 96,
  "auxiliary": [],
  "surface": [
    44
  ],
  "judgment_reason": "③은 경찰의 단속·수용과 민간기관의 보조금 수령·규율을 정책 수행의 협력 관계로 묶는 재진술이다. 96 관계 의미 복원과 17 역할 귀속은 이 경로에서 국소 중첩하므로 유일 주를 강제하지 않는다.",
  "evidence_scope": {
    "correct_choice": "4·6문단의 국가→보조금→기관 운영 및 경찰→단속/기관→규율",
    "specific_wrong_choices": {
      "1": "3·5: 명분/실태의 대조를 시기적 이동으로 오인",
      "2": "79·1: 보호 기간 규정의 존재와 실제 준수 여부 혼동",
      "5": "17: 정책 전체의 복지 성격과 치안 기능 혼동"
    }
  },
  "competing_codes": [
    {
      "code": 17,
      "verdict": "주 후보",
      "reason": "국가와 민간이 맡은 행위의 귀속을 보존해야 한다. 협력의 의미와 별도 필수 연산으로 분리되지는 않음."
    },
    {
      "code": 19,
      "verdict": "주 기각",
      "reason": "민간 참여가 국가 책무를 대신한다고 해서 부족분 보충이 정답에 명시된 핵심 요건은 아니다. 이익이나 목적의 완전 일치도 요구하지 않는다."
    },
    {
      "code": 3,
      "verdict": "① 오답에 한정",
      "reason": "시기별 초점은 ①의 오류이나 ③을 직접 확인하는 필수 시간 추론은 아니다."
    },
    {
      "code": 79,
      "verdict": "② 오답에 한정",
      "reason": "규정과 준수의 구별은 ②에 필요하나 ③은 규범 타당성 판단이 아니다."
    }
  ],
  "minimal_change_test": "국가보조금·위탁·규율 분담을 제거하고 민간이 국가 단속과 무관하게 독자 구제만 한다면 같은 부랑인 대상이어도 ③의 협력 근거가 사라진다. 명분/실태 대조를 시간순 변화로 읽지 않아도 ③은 그대로 성립한다.",
  "sdss_seen": false,
  "confidence": 0.86,
  "quota_status": "unavailable"
}
```
