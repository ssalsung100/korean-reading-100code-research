

<!-- luna-raw:AGA-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "2011.10은재무악화후라기초채권위험이높고,2013.1은지급능력개선이반영된뒤라위험이낮다. 따라서Z가부도손실을입을가능성이작아진다는③이맞다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조는 이번 stage에서 수행하지 않음.",
  "group_barrier": "AFY공식범위와AFZ원표직접확인후전체5 blindraw저장검증,answer필드만공개.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "uncertainty_preserved": null,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGA-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "logic_without_codes_fixed": "2011.10은X재무악화후,2013.1은그전2011.8보다지급능력이개선된2012.12.30뒤다. 기초채권위험이낮아져위험부담자인Z의손실가능성이낮다.",
  "primary": [
    3,
    49
  ],
  "primary_roles": {
    "3": "사건일·월말등급조정·다음달1일계약갱신이후비교시점의상태를구분.",
    "49": "X지급능력개선→기초위험감소→Z손실가능성감소의방향적용."
  },
  "auxiliary": [
    17,
    43
  ],
  "auxiliary_scope": {
    "17": "X기초발행자/Y보장매입자/Z보장매도자및각등급변화의소유주유지.",
    "43": "2013.3과10월프리미엄비교에서X관련요인은유지되고Z등급만변한조건을확인하여④기각."
  },
  "surface": [
    86,
    46
  ],
  "evidence": [
    "2011.9.17X악화;2012.12.30X가2011.8보다개선;2013.9Z채권AAA→AA+;프리미엄매월1일변경.",
    "2013.10.2프리미엄100bp는Z등급하락후값."
  ],
  "competing_codes": [
    {
      "code": 86,
      "reason": "정확한프리미엄·위험수치를계산할자료가없다.③은시점별상태를복원한뒤손실가능성방향만비교하며수치보간하지않음."
    },
    {
      "code": 46,
      "reason": "지급능력변화의효과는인과적으로도기술가능하지만새메커니즘을추론하는것보다언제누구의변화가반영됐는지와주어진방향을적용하는것이결정적."
    },
    {
      "code": 15,
      "reason": "구체등급몇단계변경을산정하는점수기준은없다. 등급표를임의수치화해2013.1정확등급을확정할수없음."
    }
  ],
  "falsification_probe": "X개선과Z등급하락을같은주체의동일위험변화로합치면④의프리미엄방향이잘못된다. 시간축과주체축을동시에보존해야한다.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
