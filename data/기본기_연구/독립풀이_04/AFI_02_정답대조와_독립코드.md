

<!-- luna-raw:AFI-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "가장 낮은 진동수110Hz의 부분음이 기본음이고 그 막대 높이가 가장 크므로③. 기본음의 정의와 실제그림 높이 비교를 결합한다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 이번stage에서공식배포답표직접대조아님.",
  "group_barrier": "G194 전체 유효blindraw저장확인후 answer필드만공개. 원문범위·그림·밑줄hold는후속직접확인으로해소하고최초기록보존.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "source_boundary_residue": "AFK말미 ##2018학년도 잔재;group식별미확정"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFI-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "logic_without_codes_fixed": "가로축에서최소진동수110Hz의부분음을기본음으로선정한뒤세로축막대높이를비교하면그세기가최대다. 최소진동수와최대세기는서로다른축의판정이다.",
  "primary": [
    15,
    86
  ],
  "primary_roles": {
    "15": "기본음=최소진동수부분음이라는정의기준으로대상을선정.",
    "86": "선정한기본음막대의높이를다른부분음과비교하여최대임을확인."
  },
  "joint_operation_note": "두개의다른단계가연결되지만코드번호자체가서로배타라는주장은아님. 기준의수량적적용과세기의비교를한넓은86행동으로기술할수도있어독립증거2개로계수하지않음.",
  "auxiliary": [
    45
  ],
  "auxiliary_scope": "②복합음의지각된음고는기본음진동수,⑤음색은부분음들의진동수·상대세기에대응함을구분.",
  "surface": [
    40
  ],
  "evidence": [
    "원그림110Hz가가장왼쪽이며막대높이최대.440Hz높이는330Hz보다높아진동수순서와세기순서는일치하지않음.",
    "본문기본음정의·음색의결정요소·가로축진동수세로축세기명시."
  ],
  "competing_codes": [
    {
      "code": 84,
      "reason": "수량그래프지만정답③에는분모분자의비를계산하는행동이없다. 축값과막대높이비교로충분."
    },
    {
      "code": 40,
      "reason": "복합음을부분음들이구성한다는배경은있으나부분의성질을전체로전이하는문제가아니다. 최소기준선정과다른축비교가필요."
    },
    {
      "code": 45,
      "reason": "음고/음색의입출력대응은②·⑤오답배제에실질기여하지만③의기본음최대세기확인은실제그림의높이를봐야하며함수대응만으로보장되지않는다."
    }
  ],
  "falsification_probe": "110Hz막대의높이를다른막대보다낮게바꾸어도기본음의정체는같지만③은거짓이된다. 기본음은항상가장세다는일반화를반박하는가상점검.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
