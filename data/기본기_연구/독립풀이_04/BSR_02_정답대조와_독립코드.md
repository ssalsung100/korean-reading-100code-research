

<!-- luna-raw:BSR-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G530",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2012/2012_answer/table_001.md 홀수형27~29",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "[A]의갈등배경·충격·회피태도는읽히지만시간적긴박감은주어지지않는다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "hold_resolution": "BSR[A]원렌더직접확인후전체blind저장.원hold불변.당시답·SDSS값미노출."
}
```


<!-- luna-raw:BSR-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G530",
  "sdss_seen": false,
  "primary": [
    {
      "code": 64,
      "reason": "지정구간이뒷받침하는갈등·정서·행동의범위를넘어긴박성을추가할수없음을판정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "사건의격렬함과서술의시간적긴박감을구별한다."
    },
    {
      "code": 78,
      "reason": "갈등에직접맞서기보다이사를작정하는대응태도를읽는다."
    }
  ],
  "surface": [
    {
      "code": 3,
      "reason": "과거회고는있지만구체시간속도·기한급박성은없다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "rejection": "이사동기의원인설명은①에실재하지만②는인과순서로증명되지않는별개속성이다."
    },
    {
      "code": 100,
      "rejection": "꿩장/내면비유는충격의근거지만긴박성까지제공하지않는다."
    }
  ],
  "confidence": 0.94,
  "scope_limit": "⑤의소극성을장면한정으로해석하며모든행동능력의부재를전칭하지않는다."
}
```
