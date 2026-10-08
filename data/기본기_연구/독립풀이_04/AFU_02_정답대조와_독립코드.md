

<!-- luna-raw:AFU-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G196",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "감각부위의신기가통해감각을합한다는ㄴ과신체구성에따른생성·지각적응의ㄷ은일치. 심장자체를군주로삼는ㄱ,크고작은신기를나누어심장운용신기를따로두는ㄹ은불일치하여③.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조는 이번 stage에서 수행하지 않음.",
  "group_barrier": "전체6 blindraw 저장 확인 후 answer필드만 공개.",
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


<!-- luna-raw:AFU-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G196",
  "logic_without_codes_fixed": "ㄴ은통합된신기의감각통합,ㄷ은신체와의생성과경험에따른지각적응을보존한다.ㄱ·ㄹ은신기의심을물질기관심장또는분리된대소신기로바꾸어기각된다.",
  "primary": [],
  "primary_candidates": [
    80,
    17
  ],
  "working_representative": 80,
  "auxiliary": [
    16,
    40
  ],
  "alternative_paths": {
    "positive_confirmation": "80:신기가감각정보를통합하고경험으로지각내용을조정한다는ㄴ·ㄷ을직접승인.",
    "negative_elimination": "17:ㄱ·ㄹ이심장주관/별개대소신기를최한기에게귀속한오류를기각하면선택조합상ㄴ·ㄷ만남음."
  },
  "evidence": [
    "6문단신기는형체없고몸전체에분포하며하나로통합,신체와함께생성소멸,경험으로정보수용및조정.",
    "기존심주지각설의심장과달리최한기의심은신기의중심."
  ],
  "competing_codes": [
    {
      "code": 17,
      "reason": "오답배제경로의실질주후보로보존한다.긍정항확인경로만을근거로80이유일주라고선언하지않는다."
    },
    {
      "code": 16,
      "reason": "신기정의와각진술을대조하는넓은행동으로전체를기술할수있다.실제경로별로감각통합내용과심의지시대상구별을남기는것이더정보량높음;전역배타경계아님."
    },
    {
      "code": 81,
      "reason": "신기가존재하며신체와함께생성된다는설명은있으나ㄴ·ㄷ의직접판독은지각통합·경험적응의기능을보존해야한다. 존재유무만확인하는것으로대체못함."
    }
  ],
  "falsification_probe": "감각정보를합치는능력은하나로통합된신기의설명에근거한다.단순히몸여러곳에분포한다는것만으로통합능력까지보장되는것은아니다.",
  "confidence": 0.95,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
