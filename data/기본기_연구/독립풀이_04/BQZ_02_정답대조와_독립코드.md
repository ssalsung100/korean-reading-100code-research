

<!-- luna-raw:BQZ-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G513",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2017/2017_answer/table_001.md 홀수형33",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "낮은 보수의 원인 설명을 징계 면제 조건으로 바꾸는 근거는 없다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "exposure_correction": {
    "official_answer_seen_before_blind": true,
    "reason": "G510 정답표 행 출력에서2017 홀수33=①이 우발 노출되었다.익명blind 풀이 중 번호를 몰랐으나 provenance 공개 후 같은 문항임을 확인했다.",
    "past_exposure": "confirmed_this_session_answer",
    "initial_record_preserved": true,
    "performance_exclusion": "엄격 blind 성과와 신규 미노출 정답률 모두에서 제외.최초 기록의official_answer_seen=false는 해당 익명사례와의 연결 인지 전 진술로 보존하되 후속 정정한다."
  }
}
```


<!-- luna-raw:BQZ-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G513",
  "sdss_seen": false,
  "primary": [
    {
      "code": 24,
      "reason": "불성실 변호에 대한 징계·배상 규칙에 낮은 보수라는 명시되지 않은 면제 예외를 덧붙인①을 배제한다."
    }
  ],
  "auxiliary": [
    {
      "code": 62,
      "reason": "낮은 보수 때문에 변호 질이 떨어진다는 설명에서 책임 면제가 따라오지 않는다."
    },
    {
      "code": 46,
      "reason": "보수→변호 질의 영향은 제도 지원 근거이며 징계 면제의 인과·규범 근거와 다르다."
    },
    {
      "code": 3,
      "reason": "③ 대상 확대 뒤 질 보장으로 발전한 시점을 구분한다."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "성실 의무라는 규범이 소재이지만 구체 오류는 없는 예외 조건 추가다."
    }
  ],
  "competing_codes": [
    {
      "code": 12,
      "rejection": "불성실→제재 적용이라는 동일 관계를 기술할 수 있어24와 중첩한다.별개 필수 연산으로 중복 계수하지 않는다."
    },
    {
      "code": 63,
      "rejection": "보수 부족이 위반 판단을 약화하는 새 증거인지 묻기보다 면제 규칙이 본문에 있는지 판단한다."
    },
    {
      "code": 19,
      "rejection": "보수 지원은 변호 질 개선의 보충 수단이나①에서 의무 위반 제재가 사라진다는 결론을 보장하지 않는다."
    }
  ],
  "confidence": 0.94,
  "scope_limit": "원인 설명과 면책 근거 구분은 본문 규칙에 한정한다.실제 법률상 모든 감경 가능성을 부정하지 않는다.정답 사전노출 확인을 승계한다."
}
```
