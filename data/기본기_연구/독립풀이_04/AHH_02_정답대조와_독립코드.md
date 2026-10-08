

<!-- luna-raw:AHH-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G205",
  "blind_answer": 5,
  "official_answer": 5,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "노즐은 잉크를 분사하는 장치의 출구로 제시된다. 앞문단의 기포 합침 현상을 노즐의 기능으로 옮긴⑤은 근거가 없다.",
  "official_answer_source": "canonical answer field 기계 연결; 공식 정답표 직접 검증 아님",
  "barrier_verified": "G205 전체 blind4 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHH-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G205",
  "primary": [],
  "primary_candidates": [
    17,
    45,
    64
  ],
  "working_representative": 17,
  "auxiliary": [
    40,
    46
  ],
  "surface": [
    91
  ],
  "judgment_reason": "⑤은 기포 결합 현상을 노즐에 귀속했다. 대상 귀속17, 장치 입력·산출 기능45, 지문이 보장하지 않는 기능의 근거범위64가 같은 오류를 기술할 수 있어 유일 주를 유보한다.",
  "competing_codes": [
    {
      "code": 45,
      "verdict": "후보 유지",
      "reason": "분사 장치의 기능을 작은 방울 합침으로 바꿔 입력·출력과 기능을 교환"
    },
    {
      "code": 64,
      "verdict": "후보 유지",
      "reason": "본문은 노즐 분사만 제시하여 합침 기능을 근거로 삼을 수 없음. 현실 불가능성으로 확대하지 않음"
    },
    {
      "code": 40,
      "verdict": "특정 선지 보조",
      "reason": "④ 지질은 물질 성분이라고 하며 전체 기능을 성분 단독 기능으로 옮기지 않는다"
    },
    {
      "code": 91,
      "verdict": "표면",
      "reason": "지문에 반비례식이 있어도⑤ 기각에 압력 계산은 불필요"
    }
  ],
  "minimal_change_test": "⑤을 잉크를 분사하는 통로 역할로 고치면 대상·기능·근거범위 기술이 함께 해소된다. 세 코드의 단독 주 우위를 확정할 수 없다.",
  "sdss_seen": false,
  "confidence": 0.93,
  "quota_status": "unavailable"
}
```
