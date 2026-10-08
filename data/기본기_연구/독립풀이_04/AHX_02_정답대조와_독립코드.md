

<!-- luna-raw:AHX-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G209",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "움직이는 바람과 서 있는 발의 대비를 바람이 발을 반석으로 옮기는 인과적 힘으로 바꾼②은 부적절하다.두 상태의 병치만으로 이동원인·도착의미를 만들 수 없다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2020__국어_국어_정답표.pdf",
  "verification_scope": "sealed필드와 대조했으며 공식PDF 정답셀의 직접시각대조는 아직 아님",
  "barrier_verified": "G209 전체 blind3 저장 후 answer필드만 공개; SDSS 미공개",
  "strict_blind_qualification": "작품친숙성과 stem의편집유형표제 노출기록 보존.완전무오염성과로 단정안함",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHX-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G209",
  "primary": [
    46
  ],
  "auxiliary": [
    39,
    64
  ],
  "surface": [
    50,
    100
  ],
  "judgment_reason": "②은 바람의 움직임과발의정지 병치를 바람이발을반석으로 이끈다는 작용인과로 바꿈. 시적 소재의 힘이라는 안내도 개별시구에 없는 이동원인을 허가하지 않는다.",
  "competing_codes": [
    {
      "code": 39,
      "verdict": "보조",
      "reason": "바람동세와화자정지의 대비를 유지해 인과오독기각"
    },
    {
      "code": 64,
      "verdict": "보조후보",
      "reason": "시구근거없는 행위추가라는 범위기술가능하지만 구체적오류는 대비→인과 전환.대표46을독점으로단정하지않음"
    },
    {
      "code": 50,
      "verdict": "기각",
      "reason": "실제 이동경로가있다가 차단되는 서술이 아니라 이동원인 자체가주어지지않음"
    },
    {
      "code": 100,
      "verdict": "표면",
      "reason": "시적소재라고 모든오류가비유대응문제는 아님.②은 구체적작용을 잘못추론"
    }
  ],
  "minimal_change_test": "②의 반석위로이끄는힘을 반석위에선나와대조되는움직임으로 바꾸면 근거에맞음. 본문이 바람때문에발이이동했다고 명시한다면 현재기각사유가 사라짐.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
