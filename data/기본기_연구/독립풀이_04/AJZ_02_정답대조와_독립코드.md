

<!-- luna-raw:AJZ-answer_check-20260926-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G225",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "b의 최대 위치가 막대 왼쪽 앞 경계에 있으므로 이동은 왼쪽이다. 뒤쪽으로 밀린 a의 최대 위치는 빠른 이동에 대한 보상 부족을 나타낸다. 동일 속력에서 b가 c보다 보상이 잘 되므로 밝기 차는 b가 더 크다. ㄱ·ㄴ만 맞아④.",
  "official_answer_source": "자료/LEET_언어이해/원본/2022/2022_answer_2022_LEET_언어이해_정답표_배포용.pdf",
  "verification_scope": "정본 연결 sealed 공식답 필드 대조; 이번 단계에서 공식 PDF 답 셀 직접 판독은 아님",
  "barrier_verified": "G225 전체 blind raw 저장 후 공식답 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJZ-independent_code-20260926-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    45
  ],
  "auxiliary": [
    43,
    86
  ],
  "surface": [
    3,
    92
  ],
  "judgment_reason": "이동 방향·속력·밝기 차를 보상 정도와 최대점 위치에 연결하고, b/c의 속력이 같은 조건에서 밝기 차의 효과를 분리한다. 곡선 높이를 그대로 밝기 차로 읽지 않는다.",
  "evidence": "blind 원도식에서 b최대는 왼쪽 경계 부근,c는 그보다 오른쪽,a는 중심선 오른쪽. b/c 동일 속력 조건이 ㄷ 판정의 핵심 통제이다.",
  "competing_codes": [
    {
      "code": 43,
      "verdict": "보조 필수",
      "reason": "b/c 속력이 같다는 조건 없이는 c의 지연을 작은 밝기 차만으로 귀속하기 어렵다. 다만 방향과 a/b 속력까지 연결하는 전체 처리는45가 대표."
    },
    {
      "code": 86,
      "verdict": "보조",
      "reason": "속력·밝기 차의 크기와 최대점 위치를 비교한다. 무엇을 비교할지는 본문 기제에 의존."
    },
    {
      "code": 3,
      "verdict": "표면 및 기제 근거",
      "reason": "시간 지연이 공간의 뒤처짐으로 나타나지만 그래프 가로축은 시간이 아니라 위치. 좌우 순서를 그대로 시간 선후로 오독하지 않는다."
    },
    {
      "code": 46,
      "verdict": "국소 중첩 후보",
      "reason": "빠른 속력·작은 밝기 차가 보상 실패를 낳는 인과와45가 겹친다.45/46 전역 분리 확정 없이 다변수 기제 적용의 작업 대표45 선택."
    }
  ],
  "minimal_change_test": "b/c 동일 속력 조건을 지우면 최대점 차이를 밝기 차만으로 설명하는 ㄷ의 판정 근거가 약해진다. 최고점 높이만 바꾸고 위치를 유지한 도식은 같은 방식으로 처리할 수 없다.",
  "limitations": "a는 속력이 다르다는 실험 구성과 본문 기제에 따른 비교이다. 실제 모든 실험의 역추론이 유일하다고 일반화하지 않는다.",
  "confidence": 0.95,
  "passage_group": "G225",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
