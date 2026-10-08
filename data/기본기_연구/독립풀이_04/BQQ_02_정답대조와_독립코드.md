

<!-- luna-raw:BQQ-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G510",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2017/2017_answer/table_001.md (공식 HWP 추출 홀수형 11~13)",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "선출·지분 할당으로 이해관계를 조정하는 혼합정체의 기능을 대내적 균형으로 재진술한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_verification_limit": "공식 HWP에서 추출된 표 확인. 이번에 HWP 원본 직접 렌더링 재검증은 하지 않음.",
  "incidental_answer_exposure": "정답표 행 출력으로 2017 홀수·짝수 1~3,21~23,31~33 정답이 함께 노출됨. 이후 해당 문항은 엄격 blind 실적에서 제외. 원문·SDSS는 미열람."
}
```


<!-- luna-raw:BQQ-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G510",
  "sdss_seen": false,
  "primary": [
    {
      "code": 44,
      "reason": "혼합정체의 선출·지분 배분이라는 제도 수단을 경쟁 집단 간 균형이라는 목적·기능과 대응한다."
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "정치 지분의 분할이 이해관계 조정을 돕는 기능적 효과를 읽는다."
    },
    {
      "code": 8,
      "reason": "③의 안전보다 연대라는 근거 없는 가치 순위를 배제한다."
    }
  ],
  "surface": [
    {
      "code": 70,
      "reason": "국가 규모의 딜레마는 지문 구조이나 ⑤ 직접 확인에 두 손실의 동시 검토는 불필요하다."
    }
  ],
  "competing_codes": [
    {
      "code": 39,
      "rejection": "고대와 현대가 언급되지만 ⑤ 판정은 두 체제의 차이표를 작성하지 않아도 혼합정체 기능 진술로 끝난다."
    },
    {
      "code": 43,
      "rejection": "규모와 결속의 여러 변수가 있어도 실험적 통제로 효과를 분리하지 않는다."
    },
    {
      "code": 70,
      "rejection": "딜레마는 연방제 설명의 배경이다. 선택 답은 그 해결 여부가 아니라 혼합정체의 균형 기능이다."
    }
  ],
  "confidence": 0.91,
  "scope_limit": "44와46은 같은 기능 연결을 목적과 효과 관점에서 기술한다. 독립 연산 두 개로 중복 계수하지 않고 44를 작업 대표로 쓴다."
}
```
