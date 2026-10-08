

<!-- luna-raw:AHK-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G205",
  "blind_answer": 1,
  "official_answer": 1,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "발생하는은 표면장력이 생겨남을 뜻한다. 올라오는은 상승·출현 이동의 의미를 더해 원문의 생성 관계를 보존하지 않으므로①.",
  "official_answer_source": "canonical answer field 기계 연결; 공식 정답표 직접 검증 아님",
  "barrier_verified": "G205 전체 blind4 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHK-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G205",
  "primary": [],
  "primary_candidates": [
    96,
    39
  ],
  "working_representative": 96,
  "auxiliary": [
    46
  ],
  "surface": [
    3
  ],
  "judgment_reason": "발생과 올라옴의 문맥상 의미를 비교하여 생성 관계의 보존 여부를 판단한다. 일상어 의미96과 두 표현 비교39가 같은 교체 판독으로 겹친다.",
  "competing_codes": [
    {
      "code": 39,
      "verdict": "후보 유지",
      "reason": "원표현과 대체표현이 같은 문맥 의미를 갖는지 대조하는 동일 연산"
    },
    {
      "code": 46,
      "verdict": "보조",
      "reason": "분자 인력으로 표면장력이 생긴다는 인과 문맥이 발생의 의미를 고정하지만 인과법칙의 진위를 평가하는 문제는 아님"
    },
    {
      "code": 99,
      "verdict": "주 기각",
      "reason": "지시어나 생략된 지시대상을 복원하는 대용 관계가 아니다"
    },
    {
      "code": 100,
      "verdict": "주 기각",
      "reason": "비유·상징의 원관념을 추론하는 것이 아니라 직접적 생성 동사의 의미 치환"
    }
  ],
  "minimal_change_test": "올라오는을 생겨나는으로 바꾸면 생성 의미가 보존되어 오류 해소. 과학 소재 때문에 인과만 주로 삼지 않는다.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
