

<!-- luna-raw:AIA-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G211",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "부인이 학발의관을 갖춘 이들을 보고 놀라 꿈을 깼다는②이 사건순서와일치한다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2022__국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조. AIC 공식PDF범위직접검증과정답셀직접대조는구별",
  "barrier_verified": "AICscope해소후유효blind4개모두저장한다음G211첫answer공개; SDSS미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIA-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G211",
  "primary": [],
  "primary_candidates": [
    17,
    96
  ],
  "working_representative": 17,
  "auxiliary": [
    3,
    2,
    44
  ],
  "surface": [
    46
  ],
  "judgment_reason": "정답②의 지각 주체·대상·후속 깨어남을 원문에 맞춘다. 사건 귀속17과 명시서술의 의미 일치96이 같은 판정. 오답③의 선후와④ 의도/실행·목적은 별도로 보존.",
  "competing_codes": [
    {
      "code": 96,
      "verdict": "후보",
      "reason": "학발의관 이들을 본 뒤 놀라 깨어남이라는 문맥 재진술 확인"
    },
    {
      "code": 3,
      "verdict": "특정 오답 보조",
      "reason": "초종례 후 집으로 옮김을 역순으로 바꾼③"
    },
    {
      "code": 2,
      "verdict": "특정 오답 보조",
      "reason": "이름을 묻고자함을 실제 물음으로 바꾼④은 의도와 실현의 차이"
    },
    {
      "code": 44,
      "verdict": "특정 오답 보조",
      "reason": "④은 노래를 들은 뒤 이름을 물으려함을 노래내용을 알기 위한 질문으로 목적도 교환"
    }
  ],
  "minimal_change_test": "②의 본 대상을 다른 인물로 바꾸면17/96의 일치가 함께 깨진다.③만 고친다고②의 판정근거가 변하지 않아 선지별 연산을 분리한다.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
