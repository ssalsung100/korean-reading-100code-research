

<!-- luna-raw:AJO-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G221",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "화자는연줄의힘으로임을이쪽으로낚아오고싶어한다.③은화자가임에게가려한다로움직이는주체와방향을교환했다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2026__국어_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,원답셀직접검증아님",
  "barrier_verified": "G221전체blind4후answer공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJO-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G221",
  "primary": [
    17
  ],
  "auxiliary": [
    96,
    44
  ],
  "surface": [
    46,
    100
  ],
  "judgment_reason": "임을낚아오는행위의대상을화자자신의이동으로바꿈.이동주체·목적지의역할귀속이최소오류.",
  "competing_codes": [
    {
      "code": 96,
      "verdict": "보조",
      "reason": "낚아오다의논항과방향뜻이역할귀속입력"
    },
    {
      "code": 44,
      "verdict": "보조",
      "reason": "연줄을이용해임을데려오려는수단목적을보존"
    },
    {
      "code": 46,
      "verdict": "표면",
      "reason": "대상힘→욕망촉발이라는앞부분은맞아도뒤의욕망내용이틀림"
    },
    {
      "code": 100,
      "verdict": "표면",
      "reason": "비현실적소망이라도행위의방향·주체를자유롭게교환할수없음"
    }
  ],
  "minimal_change_test": "③임에게가려고를임을자신에게데려오려고로고치면보기의대상촉발부분을그대로둔채오류해소.",
  "sdss_seen": false,
  "confidence": 0.96,
  "quota_status": "unavailable"
}
```
