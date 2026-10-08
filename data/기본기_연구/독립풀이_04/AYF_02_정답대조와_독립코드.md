

<!-- luna-raw:AYF-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G350",
  "first_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "실제 공급원이 최저비용C에서 더비싼B로 바뀌는 사례가 관세동맹의 효율악화 가능성을 지지한다.",
  "group_barrier": "해당group 전체blind raw 저장 후 정답만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AYF-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G350",
  "primary": [
    63,
    37
  ],
  "auxiliary": [
    36,
    39,
    86
  ],
  "surface": [
    12,
    25
  ],
  "decisive_operation": "관세동맹은효율을낮출수있다는주장을실제로구현하는공급비용상승사례를선택한다.②C→B는최저비용에서이탈하고③A→B의상대순서는미정.",
  "competing_codes": [
    {
      "code": 36,
      "rejection": "항상효율증가라는상대주장의반례로도동일사례를설명가능;바이너존재가능주장의지지63과국소중첩."
    },
    {
      "code": 88,
      "rejection": "총무역창출과전환을비교하는지문구조는있지만정답보기는직접공급원교체이며두효과량의합산없음."
    },
    {
      "code": 84,
      "rejection": "관세나가격비율계산이없고생산비용순서만필요."
    },
    {
      "code": 46,
      "rejection": "관세동맹의작용은배경이나지지사례선정에서결정적인것은전후공급원의비용차이."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.9,
  "quota_status": "unavailable"
}
```
