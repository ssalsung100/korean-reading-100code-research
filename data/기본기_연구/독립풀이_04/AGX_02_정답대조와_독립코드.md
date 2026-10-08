

<!-- luna-raw:AGX-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "전류가일정하면각간격의전류값이실제와같아측정합의근사가잘맞는다. 전류가변할때보다일정할때추정오차가더커진다는부원2의주장이틀림.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 미수행.",
  "group_barrier": "AGW5선지표복원후전체5 blindraw저장검증. answer필드만공개.",
  "sdss_seen": false,
  "source_qualification": "2022학년도예시문항;실제시행기출과구분. 문제지전재본시각검증과공식배포호스트직접검증을구별.",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGX-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G202",
  "logic_without_codes_fixed": "전류적산ΣI측정Δt에서I가일정하면각측정값이그구간전류를대표하지만변하면측정시점사이의변화를놓칠수있다.일정전류때차이가더커진다는부원2의방향은틀림.",
  "primary": [
    92
  ],
  "auxiliary": [
    45,
    43,
    10
  ],
  "auxiliary_scope": {
    "45": "연속유입량과이산측정값합의추정대응구분.",
    "43": "부원4는주변환경이온도측정에영향주는경우의교란요인문제.",
    "10": "부원5는판정뒤실제전원차단이라는필요행동을확인."
  },
  "evidence": [
    "일정간격의전류측정값×간격을합산한다는본문절차.",
    "부원2는변하는전류보다일정전류에서추정차이가더크다고함."
  ],
  "competing_codes": [
    {
      "code": 87,
      "reason": "전류가기울기형태의율로읽힐수있어도문항핵심은기울기자체계산보다시간구간별곱과합의추정정확도.",
      "code_name": "기울기"
    },
    {
      "code": 86,
      "reason": "오차대소비교결론만으로는방향근거가없다. 합산방식과일정값의대표성이라는계산구조를복원해야함."
    },
    {
      "code": 43,
      "reason": "측정환경교란은부원4의타당한의견에해당.부원2를판정할때새기기오차를가정해일정전류추정의기본관계를흐리지않음."
    }
  ],
  "falsification_probe": "일정전류I이면측정시점을어디로옮겨도같은I를얻어I×총시간이된다. 변동전류에서는같은측정점값사이에다른곡선이가능해합산오차가생길수있음.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
