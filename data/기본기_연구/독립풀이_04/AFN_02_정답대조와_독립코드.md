

<!-- luna-raw:AFN-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "blind_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "B의금리가하락하면B투자매력이낮아져A에서B로의자금유출압력이완화되므로A환율급등도진정되는방향이다.①의A오버슈팅더커짐은이경로와반대.",
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


<!-- luna-raw:AFN-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "logic_without_codes_fixed": "B금리하락→B자산기대수익감소→A에서B로향하는자금이동압력완화→A통화가치하락/환율급등압력완화의경로다. B의금리하락을A자국금리하락처럼적용하면방향이뒤집힌다.",
  "primary": [
    46
  ],
  "auxiliary": [
    17,
    49
  ],
  "primary_scope": "이자율 변화와 국가간 자금 이동을 거쳐 A환율에 이르는 중간 경로 추적.",
  "auxiliary_scope": {
    "17": "금리 변화의 주체는B,판정 대상 환율은A라는 국가 역할을 유지.",
    "49": "경로의 각 증감 방향을 결합."
  },
  "surface": [
    75,
    52
  ],
  "evidence": [
    "보기 A자금B유출로A환율급등, B통화량증가에따른금리변동이A급등진정으로이어진다고명시.",
    "본문 해당국금리하락→투자수익감소→자금유출/유입위축."
  ],
  "competing_codes": [
    {
      "code": 75,
      "reason": "갑의 견해를 읽지만 복수 경제학자의 경쟁 입장을 비교하는 단계는 없다.①기각에는 두 국가의 자금 경로를 보존하는 것이 핵심."
    },
    {
      "code": 49,
      "reason": "단순히 금리하락→환율상승이라는 한 국가의 방향을 복사하면①을 승인하게 된다. 국가 역할과 자금 경로의 중간 단계를 거쳐야 같은 방향식의 잘못된 이식을 막는다."
    },
    {
      "code": 52,
      "reason": "B투자유인이약해져A환율상승압력이완화되는관계를이중억제로표현할수있어도원문에없는억제자를새로세울필요는없다.46의구체경로를대체하는독점코드로올리지않음."
    }
  ],
  "falsification_probe": "하락하는 금리가B가 아니라A로 바뀌면 본문 상황에서는A자금 유출·A환율 상승 압력이 커지는 방향이 된다. 같은 금리하락 어휘도 대상 국가가 달라지면 최종 결론이 달라짐.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
