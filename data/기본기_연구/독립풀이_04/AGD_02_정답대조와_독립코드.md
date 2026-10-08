

<!-- luna-raw:AGD-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "계약에수선내용없으면법률상건물주의무이고침묵의불이익없다(ㄱ). 세입자수선약정이있으면계약대로세입자의무이며달리약정한불이익없다(ㄷ). 따라서②.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조는 이번 stage에서 수행하지 않음.",
  "group_barrier": "AGD공식[A]확인뒤5문항전체blindraw저장검증. answer필드만공개.",
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


<!-- luna-raw:AGD-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "logic_without_codes_fixed": "임의법규에서다른약정이없으면법정임대인의무,약정이있으면그계약의세입자의무를적용한다. 어느경우에도임의규정과다르게정하거나정하지않았다는사실만으로불이익없다.ㄱ·ㄷ②.",
  "primary": [
    12
  ],
  "auxiliary": [
    15,
    17
  ],
  "surface": [
    24,
    10
  ],
  "evidence": [
    "2문단당사자가달리정하지않으면법률규정,달리정하면계약우선. 수선의무는임의규정.",
    "ㄹ은계약상의무주체는맞지만임의규정위반불이익을추가."
  ],
  "competing_codes": [
    {
      "code": 24,
      "reason": "기본규정과달리정한계약의우선관계를원칙/예외로도기술가능하나법규의예외적제재인단속/강행과혼동하면안됨. 여기서는약정유무의조건분기가직접행동."
    },
    {
      "code": 10,
      "reason": "특정급부의무가생기려면항상명시계약이필요한것은아니다. 계약침묵시법정의무가적용되는대안이있어명시약정을유일필요조건으로만들지않음."
    },
    {
      "code": 16,
      "reason": "임의법규정의확인이출발점이지만ㄱ/ㄷ과ㄴ/ㄹ구별에는상황별의무주체와불이익여부를적용해야한다. 정의소개만으로판독을대체못함."
    }
  ],
  "falsification_probe": "같은세입자수선약정이라도해당규정이단속법규라면불이익항목의판정은달라질수있다. 의무주체하나가맞다는것으로전체복합진술을승인하지않는다.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
