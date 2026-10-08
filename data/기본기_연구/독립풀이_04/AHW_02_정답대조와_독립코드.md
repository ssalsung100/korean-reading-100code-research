

<!-- luna-raw:AHW-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G209",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "괴로움 이유를 다시 물으며 자신의 삶의 결여를 돌아보는 흐름이다. 없다 반복은 자기응시·반성으로 읽혀④가 적절하다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2020__국어_국어_정답표.pdf",
  "verification_scope": "sealed필드와 대조했으며 공식PDF 정답셀의 직접시각대조는 아직 아님",
  "barrier_verified": "G209 전체 blind3 저장 후 answer필드만 공개; SDSS 미공개",
  "strict_blind_qualification": "작품친숙성과 stem의편집유형표제 노출기록 보존.완전무오염성과로 단정안함",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHW-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G209",
  "primary": [],
  "primary_candidates": [
    80,
    96
  ],
  "working_representative": 80,
  "auxiliary": [
    97,
    39
  ],
  "surface": [
    46,
    3
  ],
  "judgment_reason": "자기 괴로움의 이유를 되묻고 자신의 결여를 응시하는 발화맥락에서 반성적 태도를 읽는다. 내면의 자기인식80과 일상언어 맥락판독96은 이 정답에서 겹쳐 유일주유보.",
  "competing_codes": [
    {
      "code": 97,
      "verdict": "보조",
      "reason": "없을까의 질문기능은 이유없음 단정이 아니며 자기재검토. 화자의 전달의도를 넘겨 외부청자 설득으로 만들지 않음"
    },
    {
      "code": 46,
      "verdict": "특정오답",
      "reason": "③ 사랑결여·시대슬픔결여 병치를 인과로 만드는 근거가 없음"
    },
    {
      "code": 39,
      "verdict": "보조",
      "reason": "흐르는자연과 선발 대비를 읽으나④ 직접근거는 없다 반복을 통한 자기응시"
    },
    {
      "code": 96,
      "verdict": "후보",
      "reason": "부정반복과자기질문을 문맥에서읽는동일작업"
    }
  ],
  "minimal_change_test": "없을까라는 자기질문을 단순확정으로 바꾸면②기각과④반성근거가 약해진다. 한 피동표현만으로 순응태도를 생성하지 않는다.",
  "sdss_seen": false,
  "confidence": 0.91,
  "quota_status": "unavailable"
}
```
