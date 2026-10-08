

<!-- luna-raw:ANC-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G253",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2009예비/2009예비_answer_2009법학적성시험_예비_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "자기 억압에 따른 원한은 성공자에게도 배제되지 않으며 특히 대중이라는 강조가 배타적 한정은 아니다.",
  "original_blind_preserved": true,
  "barrier": "group 전체 blind 저장 확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:ANC-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G253",
  "primary": [
    {
      "code": 46,
      "reason": "자기 억압→원한 경로가 성공 집단에도 적용됨을 복원"
    }
  ],
  "auxiliary": [
    {
      "code": 4,
      "reason": "특히 대중을 대중만으로 축소하지 않음"
    },
    {
      "code": 49,
      "reason": "억압할수록 원한 증가라는 방향 보존"
    },
    {
      "code": 12,
      "reason": "자기 억압을 수행한 성공자에 원문의 결과 관계 적용"
    }
  ],
  "surface": [
    {
      "code": 47,
      "reason": "복수 억압의 공통 결과가 있으나 원한을 공통원인으로 추정하지 않음"
    }
  ],
  "competitors": [
    {
      "code": 48,
      "refutation": "자기 억압과 타인 지배는 원한이라는 공통 결과에 관여하나 그 둘의 상관을 새로 추정하는 오류는 아님. 정답②는 한 경로 적용으로 배제 가능"
    },
    {
      "code": 2,
      "refutation": "원한 없음이라는 강한 진술 문제도 있지만 가능/필연만 완화하면 항상 참이 되는 것이 아니라 원문의 억압→원한 방향을 확인해야 함"
    },
    {
      "code": 53,
      "refutation": "성공자/실패자 차이가 원한 유무 차이를 설명한다는 통제 비교가 제시되지 않음. 성공 차이로 결과 부재를 만들 수 없음"
    }
  ],
  "counterfactual_probe": "②의 성공한 사람을 실패한 사람으로 바꿔도 강한 자기 억압과 원한 없음의 충돌은 남는다. 성공이 원한 발생을 차단한다는 별도 전제를 추가해야 무원한 결론이 가능해진다.",
  "boundary_status": "46/49는 경로 존재와 증감방향의 국소 중첩. 특히→오직 전환4는 별도 범위 오류 후보",
  "confidence": 0.93,
  "sdss_disclosed": false
}
```
