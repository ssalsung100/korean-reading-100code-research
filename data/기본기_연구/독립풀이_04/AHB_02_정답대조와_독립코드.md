

<!-- luna-raw:AHB-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G203",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "official_answer_source": "sealed/answer_sdss.jsonl의 canonical answer 기계 연결; 공식 정답표 직접 검증과 구별",
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "추가된 활동의 예인지 확인하려면 기존 다섯 활동과 새 활동을 구별한 다음 저자 입장에서 구성 순서를 생각하는 행동과 대응시킨다.",
  "barrier_verified": "G203 3개 blind raw 저장 후 answer만 선택 공개. SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHB-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G203",
  "primary": [],
  "primary_candidates": [
    37,
    17
  ],
  "working_representative": 37,
  "auxiliary": [
    16,
    40
  ],
  "surface": [
    78
  ],
  "judgment_reason": "정의에 맞는 예를 찾는 37과 기존/추가 활동 집합에 귀속하는 17이 같은 판정에서 겹친다. 작업 대표는37, 단일 주 확정은 유보.",
  "competing_codes": [
    {
      "code": 16,
      "verdict": "보조",
      "reason": "관점 바꾸기의 행동 정의를 복원한 후⑤에 적용한다. 정의 분석만으로 기존/추가 범위 구별은 생략할 수 없다."
    },
    {
      "code": 40,
      "verdict": "보조",
      "reason": "①②③은 기존 SQ3R 구성 활동이라 추가된 활동의 예에서 제외한다."
    },
    {
      "code": 78,
      "verdict": "표면",
      "reason": "④ 수동과⑤ 능동의 대비가 있으나 욕구나 동기를 도입하여 행위를 설명하는 문제가 아니다."
    },
    {
      "code": 10,
      "verdict": "주 기각",
      "reason": "사례의 요건 검사는 가능하나 글의 순서를 생각하는 것이 모든 관점 바꾸기의 필수 행동이라는 강한 명제를 만들지 않는다."
    }
  ],
  "minimal_change_test": "⑤에서 저자 입장만 지우거나 순서 구성을 수동 수용으로 바꾸면 예시 적합성이 깨진다. 37/17은 같은 요건 대입으로 작동한다.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
