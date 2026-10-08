

<!-- luna-raw:BAB-answer_check-20261001-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G365",
  "selected_answer": 4,
  "official_answer": 4,
  "is_correct": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2016/2016_answer_2016학년도_법학적성시험_언어이해_정답표.hwp",
  "answer_access": "blind-only 풀이 3건 저장 검증 후 sealed에서 official_answer·official_answer_source만 출력하여 대조",
  "group_blind_barrier": {
    "rule": "all_group_blind_records_before_any_group_answer_check",
    "verified": true,
    "blind_record_ids": [
      "AZZ-blind-20261001-01",
      "BAA-blind-20261001-01",
      "BAB-blind-20261001-01"
    ]
  },
  "fixed_logic_without_codes": "날짜 오인은 명시된 현저한 기준 위반 사례에 해당한다. 존재하는 불복절차의 미경유 제한을 절차 부재에 적용할 수 없어 ㄱ·ㄴ만 참이다.",
  "original_blind_preserved": true,
  "reasoning_revision": "없음",
  "sdss_seen": false,
  "prior_project_judgment_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:BAB-independent_code-20261001-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    12
  ],
  "auxiliary": [
    15,
    10,
    24
  ],
  "surface": [
    3,
    79
  ],
  "primary_reason": "실제 접수일 오인을 현저한 기준 위반 규칙에 대입하고, 불복절차 존재라는 적용 조건이 없는 사건에 미경유 제한을 적용한 ㄷ을 배제한다.",
  "code_free_logic_anchor": "날짜 오인은 보호받는 단순 판단 차이를 벗어나며, 없는 절차를 이용하지 않았다는 이유로 배상을 배제할 수 없다.",
  "evidence": [
    {
      "location": "5문단·보기",
      "text": "소를 제기한 날짜를 확인하지 못한 것 / 11월 4일을 14일로 오인",
      "operation": "주어진 사례를 현저한 법적 기준 위반에 포섭하여 ㄱ·ㄴ 수용"
    },
    {
      "location": "5문단·보기 ㄷ",
      "text": "불복 절차가 마련되어 있는 경우 / 불복 절차가 마련되어 있지 않았기 때문에 … 받아들이지 않았을 것",
      "operation": "적용 범위 밖 사건에 제한을 확장한 오류 배제"
    }
  ],
  "auxiliary_roles": {
    "15": "날짜 확인 실패가 현저한 기준 위반에 해당하는지 판정; #12 포섭의 기준 측면",
    "10": "절차 이용이 요구되는 범위가 절차 존재 및 특별사정 유무에 한정됨을 확인; 배상에는 언제나 불복이 필수라고 하지 않음",
    "24": "ㄱ에서 직무상 독립의 일반 보호 범위에 특별한 위법 사정을 구분. ㄷ의 절차 부재는 명시 예외인 법관 귀책과 동일하지 않음"
  },
  "surface_reason": {
    "3": "접수일과 연도는 사실 소재지만 전후 순서 비교가 ㄷ의 법적 판단을 결정하지 않는다.",
    "79": "당위는 능력을 함축한다는 철학적 원리를 외부에서 보충하지 않고 지문의 명시 조건만으로 해결 가능."
  },
  "competing_codes": [
    {
      "code": 10,
      "verdict": "보조; #12와 국소 중첩",
      "refutation": "불복 이행을 결과의 무조건 필요조건으로 읽으면 오답이다. 먼저 그 의무가 적용되는 전건 범위를 확정해야 한다."
    },
    {
      "code": 24,
      "verdict": "ㄱ 보조·ㄷ의 주 코드 배제",
      "refutation": "ㄷ은 절차가 있으나 법관 귀책으로 미경유한 예외가 아니라 절차 자체가 없는 경우다. 규칙의 적용 범위 밖과 예외를 같게 기록하지 않는다."
    },
    {
      "code": 95,
      "verdict": "독립 주 배제·국소 재검토 가능",
      "refutation": "절차가 있어야 그 미이용을 문제 삼는다는 재진술은 가능하다. 하지만 #10/#12와 별도 필수 행동이 확보되지 않았으므로 번호를 추가할 근거가 약하다."
    },
    {
      "code": 2,
      "verdict": "주 배제",
      "refutation": "인정할 수 있다와 같은 강도도 보존해야 하나 ㄱㄴㄷ의 차이는 구체 위법사정과 절차 존재 조건으로 결정된다."
    }
  ],
  "invalid_inference_guard": "절차 부재→배상책임 확정이라는 전건부정·과잉 추론은 하지 않는다. ㄷ에 제시된 배제 이유가 성립하지 않는다는 범위에서만 부정한다.",
  "merge_or_split": "#12/#10/#95는 이 조건 범위를 다른 초점으로 기술할 수 있다. #15는 그 조건 적용의 기준 측면이며 별개 연산으로 중복 계수하지 않는다.",
  "revision_trigger": "절차는 존재하되 법관 귀책으로 불복하지 못한 사례라면 ㄷ 경로도 #24 예외 적용이 중심이 될 수 있다.",
  "confidence": 0.94,
  "passage_group": "G365",
  "sdss_seen": false,
  "prior_project_judgment_seen": false,
  "all_group_answer_check_completed": true,
  "quota_status": "unavailable"
}
```
