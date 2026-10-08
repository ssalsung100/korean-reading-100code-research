

<!-- luna-raw:ALA-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G234",
  "official_answer": 5,
  "blind_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2023/2023_answer_언어이해정답.pdf",
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "logic_without_codes": "신호가 없어도 해당 신호 보유 단백질과 결합하면 이동할 수 있으나 핵 밖인 세포질과 세포 외부는 다르다.⑤의 독립 리보솜 유래 단백질은 세포 외부 이동을 보장하지 않는다.",
  "correction": "없음",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:ALA-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    42
  ],
  "primary_candidates": [
    42,
    17,
    45
  ],
  "working_primary": 42,
  "unique_primary_confirmed": false,
  "auxiliary": [
    12
  ],
  "surface": [
    10
  ],
  "judgment_reason": "⑤는 NLS/NES로 핵과 세포질을 오가는 계통의 결합을 세포 외부 분비 계통으로 잘못 옮긴다.핵 밖/세포 밖의 경계와 합성 출발-목적지 대응을 함께 유지한다.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "공동 주 후보",
      "reason": "핵 유출 대상과 분비 대상을 다른 계통에 귀속시키는 동일 오류."
    },
    {
      "code": 45,
      "verdict": "공동 주 후보",
      "reason": "독립 리보솜 계통의 산출 이동 범위를 유지하는 대응 판단으로도⑤를 배제 가능하여42 독점성 미확정."
    },
    {
      "code": 10,
      "verdict": "보조 후보",
      "reason": "자체 신호서열은 결합 운반 때문에 이동의 필수요건이 아니다.그러나⑤의 오류는 신호가 반드시 있어야 한다는 단정이 아님."
    },
    {
      "code": 12,
      "verdict": "보조",
      "reason": "신호 보유자와 결합하면 지정 장소로 이동 가능하다는 적용으로③④를 확인한다."
    }
  ],
  "minimal_change_test": "핵 밖을 세포 밖으로 바꾸면 본문 경로의 종점이 달라진다.⑤의 결합 상대를 소포체 리보솜 유래의 외부 분비 단백질로 바꾸면 잘못된 계통 연결은 해소되나 세포외 이동의 실제 성립까지 추가로 확정하지 않는다.",
  "confidence": 0.94,
  "passage_group": "G234",
  "sdss_seen": false,
  "all_group_answer_check_complete": true,
  "quota_status": "unavailable"
}
```
