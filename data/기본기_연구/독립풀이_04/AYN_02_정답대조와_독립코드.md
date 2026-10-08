

<!-- luna-raw:AYN-answer_check-20260928-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G352",
  "first_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes": "서남극아문센은따뜻한해수접근등으로높은융해두께를보인다. 전체유입속도를빙산분리량하나로식별하지않는다.",
  "group_barrier": "전체3개blind 저장 후 정답만공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AYN-independent_code-20260928-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G352",
  "primary": [
    46,
    84
  ],
  "auxiliary": [
    39,
    2,
    43,
    92
  ],
  "surface": [
    45
  ],
  "decisive_operation": "서남극의따뜻한해수유입·융해조건을높은단위면적융해량S와연결해②를지지한다.⑤는C만으로A의속도를알수없고③는시간·양상강화다.",
  "competing_codes": [
    {
      "code": 84,
      "rejection": "②는융해두께=S비교이므로주기여지만실제나눗셈계산없이해역의조건과본문높은S를연결해판정가능."
    },
    {
      "code": 12,
      "rejection": "조건적용으로쓸수있으나환경조건이융해량에영향을주는기제를살려46으로구체화."
    },
    {
      "code": 43,
      "rejection": "⑤의유입식별에서다른항변화배제가없다는제한에보조.②의직접근거는지역융해경향."
    },
    {
      "code": 4,
      "rejection": "③수년고갈은주로시간과성립강도왜곡이며대상전체양화만으로기록하지않음."
    }
  ],
  "sdss_seen": false,
  "confidence": 0.91,
  "quota_status": "unavailable"
}
```
