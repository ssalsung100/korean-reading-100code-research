

<!-- luna-raw:BRW-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G523",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2009예비/2009예비_answer/table_001.md Q11~13 및 canonical_connection 공식 예비시험HWP 연결",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "⑤는 감각적 즐거움의 활용에 초점을 한정해 본문이 요구한 사상·가치·예술정체성의 심층 읽기와 어긋난다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_correction": "academic_year=2009만보고본시험Q11~13정답⑤④③을먼저조회했으나canonical_source_path와official_answer_source가2009예비임을확인하여예비정답④③⑤로정본연결수정.본시험답을본case공식답으로raw기록하거나최초풀이를수정하지않음.",
  "incidental_answer_exposure": "2009LEET본시험11~13답노출.이후해당case는미노출성과제외."
}
```


<!-- luna-raw:BRW-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G523",
  "sdss_seen": false,
  "primary": [
    {
      "code": 15,
      "reason": "감각적쾌를넘어심층내용을읽는다는감상기준에다섯사례를대조한다."
    }
  ],
  "auxiliary": [
    {
      "code": 37,
      "reason": "각감상이사상·무의식·예술정체성등의조건을구현하는지확인한다."
    },
    {
      "code": 80,
      "reason": "감각적으로보는것과심안으로읽는것의인식방식을구별한다."
    }
  ],
  "surface": [
    {
      "code": 100,
      "reason": "본문의심안·텍스트비유는관점을설명하지만각선지에서비유대상을찾는과제는아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 88,
      "rejection": "편안한즐거움이선지에있어도편익계산으로감상의적절성을판정하지않는다."
    },
    {
      "code": 63,
      "rejection": "작품이론을강화·약화하는새증거가아니라주어진관점적용이다."
    },
    {
      "code": 93,
      "rejection": "작가의뜻을읽는넓은소통모형은가능하나작가·매체·수신자단계추적만으로⑤의감상기준위반을설명하지못한다."
    }
  ],
  "confidence": 0.94,
  "scope_limit": "⑤작품에심층내용이없다고판정하지않고제시된감상의초점을판정한다."
}
```
