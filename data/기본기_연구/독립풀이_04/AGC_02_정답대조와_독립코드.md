

<!-- luna-raw:AGC-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "비례원칙은국가의계약자유제한에적용된다. 단속법규도법적불이익으로제한하므로이를비례원칙적용에서제외한③은틀리다.",
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


<!-- luna-raw:AGC-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G198",
  "logic_without_codes_fixed": "국가의계약자유제한에는비례원칙이적용된다.단속법규의불이익도그제한에속하므로③처럼단속유형을제외할근거가없다.",
  "primary": [
    22
  ],
  "auxiliary": [
    17,
    20,
    24
  ],
  "primary_scope": "계약자유제한이라는상위범주에적용되는비례원칙을그하위사례인단속법규개입에도유지한다.",
  "auxiliary_scope": {
    "17": "단속법규도국가개입·자유제한에속함을확인.",
    "20": "④약한제한으로목적달성가능하면추가무효가필요없다는최소제한논리를확인.",
    "24": "⑤강행위반의반환원칙과비도덕급부예외구별."
  },
  "evidence": [
    "마지막문단국가개입시필요최소한의제한이라는비례원칙.",
    "단속법규는계약유효하더라도벌금등법적불이익을부과."
  ],
  "competing_codes": [
    {
      "code": 17,
      "reason": "③의단속법규를비례원칙적용대상에서빼는범주오류로도같게기술가능.22는상위규칙의하위적용을강조하는대표이며유일주배타성유보."
    },
    {
      "code": 4,
      "reason": "단속유형만제외하는적용범위변경이지만단순모두/일부어휘가핵심인것은아니다. 단속개입이상위조건에속한다는근거를확인해야함."
    },
    {
      "code": 20,
      "reason": "④의최소제한논리는오답배제에실질기여하지만③직접기각은그유형에도비례원칙이적용된다는귀속판정. 정답주와특정오답행동을분리."
    }
  ],
  "falsification_probe": "계약효력이유지된다는사실만으로자유제한이전혀없다고보면벌금의법적불이익을누락한다. 효력과제한유무는다른축.",
  "confidence": 0.97,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
