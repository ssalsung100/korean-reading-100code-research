

<!-- luna-raw:AFO-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "실질통화량은물가경직시상승했다가물가조정으로원래수준복귀하여c. 금리는하락후반등해a. 환율은오버슈팅후하락하지만증가한명목통화량·물가를반영한더높은장기환율에수렴하므로b.④.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조는 이번 stage에서 수행하지 않음.",
  "group_barrier": "AFO 원그래프/범위/선지표 직접확인 후 전체6 blindraw 저장을 확인하여 answer필드만 공개.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFO-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "logic_without_codes_fixed": "실질통화량은상승뒤이전수준,c. 금리는하락뒤이전수준,a. 환율은오버슈팅뒤하락하지만이전보다높은새균형,b. 최초상승·하락뿐아니라시간별기준수준을함께맞춘다.",
  "primary": [
    3,
    45
  ],
  "primary_roles": {
    "3": "충격직전/직후/장기수렴시점을분리하고각시점의수준을보존.",
    "45": "각경제변수의시간경로를a/b/c그래프표상에대응."
  },
  "auxiliary": [
    84,
    86
  ],
  "auxiliary_scope": {
    "84": "M/P의장기복귀와P/P외국의새장기수준을구별하여두상승곡선을나눔.",
    "86": "곡선최종수준을각곡선의충격이전수준과비교."
  },
  "surface": [
    49,
    87
  ],
  "evidence": [
    "공식그래프a↓후원수준,b↑후일부하락·새높은수준,c↑후원수준.",
    "공식[가]㉠실질통화량증가후원수준,㉡금리하락후반등,㉢장기균형환율수렴."
  ],
  "competing_codes": [
    {
      "code": 49,
      "reason": "초기증감방향만으로a를분리할수있지만b/c는둘다증가한다. 장기기준수준까지복원해야실질량/환율을정확히구별."
    },
    {
      "code": 87,
      "reason": "수렴기울기·속도의정량비교를요구하지않으며보기는변수별수렴기간이다를수있다고명시. 곡선의경사크기에서정확한기간을추정하면과잉."
    },
    {
      "code": 46,
      "reason": "인과경로는각변화형태를설명하는본문근거지만문항의직접작업은정해진변수경로를시간그래프와대응하는것. 새인과메커니즘추론은없음."
    }
  ],
  "falsification_probe": "b의장기종착점만충격이전수준으로내리면환율과실질량을가르는결정정보가사라진다. 초기급등높이만다르다는이유로두변수를확정해서는안된다.",
  "confidence": 0.99,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
