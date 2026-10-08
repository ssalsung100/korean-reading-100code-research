

<!-- luna-raw:AKL-answer_check-20260926-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G229",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "민주주의 확대 속에 서로 다른 집단의 대변과 적대적 양극화가 커지면서 기존 규범이 붕괴해 두 번째 위기가 발생했다.③이 이 경로를 보존한다.",
  "official_answer_source": "자료/LEET_언어이해/원본/2022/2022_answer_2022_LEET_언어이해_정답표_배포용.pdf",
  "verification_scope": "정본 연결 sealed 공식답 필드 대조; 이번 단계에서 공식 PDF 답 셀 직접 판독 아님",
  "barrier_verified": "G229 전체 blind raw 저장 후 공식답 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AKL-independent_code-20260926-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    46
  ],
  "auxiliary": [
    3,
    5
  ],
  "surface": [
    39,
    83
  ],
  "judgment_reason": "참여 확대·집단 분화·당파 양극화·규범 붕괴가 위기로 이어지는 본문 인과 경로를③이 보존한다. 원인을 단순 시점 동시성으로 추정한 것이 아니라 명시 전개를 연결한다.",
  "competing_codes": [
    {
      "code": 3,
      "verdict": "보조",
      "reason": "시간상 뒤에 일어남은 인과 경로 정렬을 돕지만③은 왜 위기가 생겼는지를 말함."
    },
    {
      "code": 5,
      "verdict": "보조",
      "reason": "규범 회복/붕괴와 위기의 변화 상태를 구분. 독립 핵심은 확대와 붕괴의 원인 연결."
    },
    {
      "code": 39,
      "verdict": "표면",
      "reason": "두 위기를 함께 묻지만③은 두 번째 위기의 경로만으로 확인 가능. 전체 비교가 정답 필수 아님."
    },
    {
      "code": 83,
      "verdict": "② 오답",
      "reason": "차별의 비민주적 가치와 정치 안정 효과의 사실을 구별하는 것은② 배제에 유용하나③ 주가 아님."
    }
  ],
  "minimal_change_test": "③의 양극화가 규범 붕괴를 야기했다를 양극화가 규범 회복을 야기했다로 바꾸면 인과 방향이 틀림. 두 위기의 이름만 바꾸는 비교 문제로 축소 안 함.",
  "confidence": 0.96,
  "passage_group": "G229",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
