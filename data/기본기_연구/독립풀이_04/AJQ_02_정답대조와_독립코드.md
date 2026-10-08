

<!-- luna-raw:AJQ-answer_check-20260922-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G222",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "훈령 자체가 상위 법률의 위임 범위를 벗어나 국민을 구속한 것이 문제다. 훈령대로 단속한 하급 기관이 훈령을 발한 상급 기관의 지침을 어긴다는 ⑤는 다른 관계를 주장하므로 부적절하다.",
  "official_answer_source": "자료/LEET_언어이해/원본/2022/2022_answer_2022_LEET_언어이해_정답표_배포용.pdf",
  "verification_scope": "정본 연결 검증된 sealed 공식답 필드 대조. 부모가 PDF 답 셀을 직접 판독한 것은 아님.",
  "barrier_verified": "G222 AJP·AJQ·AJR의 blind raw 3건 저장 후 공식답 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJQ-independent_code-20260922-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G222",
  "primary": [
    17
  ],
  "auxiliary": [
    9,
    79
  ],
  "surface": [
    63
  ],
  "judgment_reason": "⑤는 훈령이 상위법·헌법을 어기는 관계를 하급 기관이 상급 기관의 지침을 어기는 관계로 교체한다. 위반 주체와 위반 대상의 층위를 고정하는 것이 결정적이다.",
  "evidence_scope": {
    "correct_choice": "2문단: 훈령의 위임 범위 일탈과 법률 유보 위배, 하급기관의 훈령 불복종 근거는 없음",
    "other_choices": "① 법규 위계, ② 위임 목적 범위, ③ 법률 유보, ④ 포괄 정의"
  },
  "competing_codes": [
    {
      "code": 9,
      "verdict": "보조",
      "reason": "법규 위계와 기관 위계를 구분하는 입력이지만 높낮이만 알아서는 서로 다른 두 위계를 교체한 오류를 찾지 못함."
    },
    {
      "code": 79,
      "verdict": "보조",
      "reason": "위임·권한의 규범적 제한을 보존해야 하나 정답은 규범 일반보다 그 위반 관계의 대상을 바꾸는 오류."
    },
    {
      "code": 63,
      "verdict": "주 기각·발문 표면",
      "reason": "비판 발문이지만 새 증거의 지지 변화가 아니라 본문에 있는 비판 관계를 정확히 귀속해야 함."
    },
    {
      "code": 12,
      "verdict": "주 기각",
      "reason": "예외적 위임 조건은 ①~③을 이해하는 바탕이나 ⑤는 그 조건의 역·대우를 적용한 오류가 아님."
    }
  ],
  "minimal_change_test": "⑤의 하급기관→상급기관 지침을 훈령→상위법의 제한으로 바꾸면 비판의 타당성이 회복된다. 위계라는 일반어는 두 경우 동일하므로 번호9만으로는 교체를 포착하지 못한다.",
  "sdss_seen": false,
  "confidence": 0.97,
  "quota_status": "unavailable"
}
```
