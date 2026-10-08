

<!-- luna-raw:AHN-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G206",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "시대 상황 이해에는 주방 사진이 있는 글을 읽었고 도해 조직자를 활용해 정리한 대상은 진로 관련 사건이다.④은 도구와 사용 단계·대상을 교환했다.",
  "official_answer_source": "canonical answer field 기계 연결; 공식 정답표 직접 검증 아님",
  "barrier_verified": "G206 전체 blind3 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AHN-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G206",
  "primary": [],
  "primary_candidates": [
    17,
    44,
    45
  ],
  "working_representative": 17,
  "auxiliary": [
    16,
    37
  ],
  "surface": [
    86
  ],
  "judgment_reason": "도해조직자 순서도의 용도가 사건 삶 파악인데④은 주방 사진 글의 배경지식 보강 단계에 옮긴다. 대상·단계 귀속17, 수단목적44, 처리대응45가 같은 교환을 기술할 수 있음.",
  "competing_codes": [
    {
      "code": 44,
      "verdict": "후보 유지",
      "reason": "목적별 사용 도구를 잘못 대응한 오류로 설명 가능"
    },
    {
      "code": 45,
      "verdict": "후보 유지",
      "reason": "자료·도구·결과의 단계별 대응에서 사진글과 순서도의 기능을 교환"
    },
    {
      "code": 37,
      "verdict": "보조",
      "reason": "순서도·대립척도·참고자료 활용의 예시를 정의에 대응시켜야 하나④의 최소 오류는 이미 주어진 도구의 귀속 교환"
    },
    {
      "code": 86,
      "verdict": "표면",
      "reason": "대립척도 점수가 있으나 점수 크기를 비교 계산해④을 결정하지 않음"
    }
  ],
  "minimal_change_test": "④의 도해조직자를 참고자료로, 정리하였다를 파악하였다로 고치면 보기에 부합. 주방 사진을 보았다는 것만으로 학생이 도해조직자를 구성했다는 행동을 보충하지 않는다.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
