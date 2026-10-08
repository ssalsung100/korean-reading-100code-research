

<!-- luna-raw:BRU-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G523",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2009예비/2009예비_answer/table_001.md Q11~13 및 canonical_connection 공식 예비시험HWP 연결",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "랜스는 법을 지향했지만 실제 총을 썼고 실제 저격자는 톰이다.지향과 행위·결과의 원인을 구별한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_correction": "academic_year=2009만보고본시험Q11~13정답⑤④③을먼저조회했으나canonical_source_path와official_answer_source가2009예비임을확인하여예비정답④③⑤로정본연결수정.본시험답을본case공식답으로raw기록하거나최초풀이를수정하지않음.",
  "incidental_answer_exposure": "2009LEET본시험11~13답노출.이후해당case는미노출성과제외."
}
```


<!-- luna-raw:BRU-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G523",
  "sdss_seen": false,
  "primary": [
    {
      "code": 25,
      "reason": "힘/법이라는 시대 분류 기준에 인물의 실제 행위를 대응해 랜스가 법칙을 철저히 지켰다는④를 배제한다."
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "법의 지향과 실제 사용 수단을 구분한다."
    },
    {
      "code": 46,
      "reason": "톰의 저격이 랜스의 정치 진출에 기여한 결과를 추적한다."
    }
  ],
  "surface": [
    {
      "code": 26,
      "reason": "대립하는 시대 유형이 있어도 한 인물이 모든 행동에서 한쪽에만 속한다고 보장되지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 75,
      "rejection": "등장인물이 대표하는 가치 차이는 있지만 정답은 견해 비교보다 행위와 분류기준 불일치다."
    },
    {
      "code": 13,
      "rejection": "폭력 수단과 새 시대 도래가 양립 불가능하다고 할 수 없고 톰이 그 반례다."
    },
    {
      "code": 4,
      "rejection": "철저히라는 전칭 강도도 관련되나 위배하는 실제 총 사용을 기준에 대응해야 한다."
    }
  ],
  "confidence": 0.95
}
```
