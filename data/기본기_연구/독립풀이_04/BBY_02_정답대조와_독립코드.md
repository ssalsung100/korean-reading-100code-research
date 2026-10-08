

<!-- luna-raw:BBY-answer_check-20261002-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G381",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "answer_source": "sealed/answer_sdss.jsonl official_answer; data/meet_questions.jsonl 정본전사",
  "verification_limit": "원 정답표 이번 세션 독립 재확인 없음",
  "all_group_blind_records_before_any_group_answer_check": true,
  "minimal_logic_without_codes": "뇌충 유전자 기준으로 개미는 외부 환경이며 행동 조종을 통해 소 숙주 도달.내부 형질 적응과 외부 조종을 구별.",
  "original_blind_preserved": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BBY-independent_code-20261002-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G381",
  "primary": [
    {
      "code": 42,
      "reason": "뇌충 운반자 기준으로 내부 형질 변화와 외부 개미 행동 조종을 구분"
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "분비물→개미 행동→소에게 먹힘→복제기회 경로"
    },
    {
      "code": 17,
      "reason": "누구의 유전자/운반자인지 논항 고정"
    },
    {
      "code": 37,
      "reason": "㉠ 조건에 부합하는 사례 검사라는 과제층위"
    }
  ],
  "surface": [
    {
      "code": 44,
      "reason": "복제 이득 전략은 수단/목적 표현으로 겹치나 내부/외부 작용 위치가 결정적"
    }
  ],
  "competitors_rejected": [
    {
      "code": 49,
      "reason": "복제가 늘어난다는 방향은ㄴㄷ에도 있으므로 방향만으로㉠ 사례 판별 불가."
    },
    {
      "code": 40,
      "reason": "유전자와 운반자의 구성관계 자체보다 환경에 작용하는 위치 구별."
    },
    {
      "code": 70,
      "reason": "ㄷ 장기 불리함은 선택되는 사례가 아니며 모든 선택이 손실인 딜레마 구조도 아님."
    }
  ],
  "boundary_note": "42와17은 기준 대상 고정에 중첩하지만42는 그 대상의 경계를 넘는 작용 여부를 추가 명시.둘을 독립 필수 연산으로 중복 계수하지 않음.",
  "confidence": 0.93,
  "sdss_seen": false
}
```
