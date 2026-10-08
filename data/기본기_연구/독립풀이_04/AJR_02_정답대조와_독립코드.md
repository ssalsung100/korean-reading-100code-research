

<!-- luna-raw:AJR-answer_check-20260922-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G222",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "보기는 안전장치를 운영하는 과정에서 몸을 훈련시키는 기술이 동원된다고 설명한다. 보호 법체계에 배제가 포함된다는 본문은 이 두 요소가 서로 배척한다는 근거가 아니므로 ⑤가 틀리다.",
  "official_answer_source": "자료/LEET_언어이해/원본/2022/2022_answer_2022_LEET_언어이해_정답표_배포용.pdf",
  "verification_scope": "정본 연결 검증된 sealed 공식답 필드 대조. 부모가 PDF 답 셀을 직접 판독한 것은 아님.",
  "barrier_verified": "G222 AJP·AJQ·AJR의 blind raw 3건 저장 후 공식답 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJR-independent_code-20260922-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G222",
  "primary": [],
  "primary_candidates": [
    13,
    14
  ],
  "working_representative": 13,
  "auxiliary": [
    17,
    16
  ],
  "surface": [
    25,
    9
  ],
  "judgment_reason": "⑤가 단언한 두 요소의 배척을 보기의 실제 결합 관계로 반박한다. 13의 부정과 14의 확인은 같은 최소 판단 연산이므로 번호 차이로 별도 본질을 만들지 않는다.",
  "evidence_scope": {
    "correct_choice": "보기: 안전장치로 위험을 조절하는 그 과정에서 순종적 몸을 만드는 기술이 동원된다. 본문 보호/배제 대립을 장치/기술 관계에 옮길 수 없음.",
    "specific_wrong_choice": "③을 배제하려는 고전 인종 기준의 적용은 변형된 국가인종주의 정의를 무시함"
  },
  "competing_codes": [
    {
      "code": 14,
      "verdict": "동일 최소 연산의 주 후보",
      "reason": "결합 사용의 원문 근거로 배척을 부정하는 것이므로 13과 반대 방향 이름으로 같은 판정을 기술한다."
    },
    {
      "code": 17,
      "verdict": "보조",
      "reason": "본문의 보호/배제와 보기의 장치/기술을 서로 다른 비교쌍으로 유지해야 함. 다만 비교쌍을 고정한 뒤에도 배척 관계의 거짓을 판정해야 한다."
    },
    {
      "code": 16,
      "verdict": "보조",
      "reason": "변형된 인종주의 정의가 ①~④ 적용을 지지하지만 ⑤의 결정적 오류는 장치/기술의 관계."
    },
    {
      "code": 25,
      "verdict": "주 기각·소재 층위",
      "reason": "건전/비건전과 생산적/미달 분류는 지문 내용이며 ⑤에서 잘못 나눈 분류 가지를 재구성하는 문제가 아니다."
    }
  ],
  "minimal_change_test": "장치와 기술의 명칭을 유지하고 '배척 관계'를 '동원·결합 관계'로 바꾸면 보기와의 충돌은 해소된다. 다만 본문의 보호/배제 내재만으로 그 결합을 독립 증명한 것은 아니므로 선지 전체 타당성 회복까지 단정하지 않는다.",
  "redivision_condition": "어떤 두 속성의 양립 불가능성을 새로 도출하는 사례와 특정 배척 주장을 공존 근거로 반박하는 사례는 추론 방향의 하위 유형으로 비교하되 13/14 전역 통합은 추가 반례 검토 뒤 판단한다.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
