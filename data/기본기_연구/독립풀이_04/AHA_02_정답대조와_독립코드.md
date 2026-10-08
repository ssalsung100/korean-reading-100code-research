

<!-- luna-raw:AHA-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G203",
  "blind_answer": 1,
  "official_answer": 1,
  "matches": true,
  "official_answer_source": "sealed/answer_sdss.jsonl의 canonical answer 기계 연결; 공식 정답표 직접 검증과 구별",
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "정의된 활동의 시점과 행동을 선지와 맞춘다. 읽은 뒤 연결하여 이해하는 활동을 읽기 전 자료 선택으로 바꾼 ①이 불일치.",
  "barrier_verified": "G203 3개 blind raw 저장 후 answer만 선택 공개. SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHA-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G203",
  "primary": [],
  "primary_candidates": [
    16,
    17
  ],
  "working_representative": 16,
  "auxiliary": [
    3
  ],
  "surface": [
    44
  ],
  "judgment_reason": "숙고하기의 명시적 정의를 복원하는 16과 그 활동에 틀린 행동을 귀속했는지 보는 17은 정답①에서 같은 교체를 검출한다. 단일 주 우위는 유보한다.",
  "competing_codes": [
    {
      "code": 3,
      "verdict": "보조",
      "reason": "읽은 뒤와 읽을 글 선택 전의 시점 차이는 오류 단서이나 시점만 읽은 뒤로 고쳐도 자료 선택은 숙고가 되지 않는다."
    },
    {
      "code": 21,
      "verdict": "주 기각",
      "reason": "정의의 필요충분성을 왕복 적용할 필요 없이 명시 행동의 불일치로 판정한다."
    },
    {
      "code": 44,
      "verdict": "표면",
      "reason": "지식 습득 목적은② 확인에 관여하나①의 잘못된 활동 귀속을 결정하지 않는다."
    }
  ],
  "minimal_change_test": "①을 읽은 뒤 배경지식과 연결하는 활동으로 고치면 16/17이 함께 해소된다. 번호 차이를 독립 증거로 계수하지 않는다.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
