

<!-- luna-raw:AGO-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G200",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "ㄱ은고유DNA와박테리아같은이분분열,ㄹ은박테리아막특성카디오리핀을확인해본문기원판단근거와맞는다.ㄴ·ㄷ은핵심박테리아특징이부족하여ㄱㄹ②.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 미수행.",
  "group_barrier": "전체6 blindraw저장후answer필드만공개.",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGO-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G200",
  "logic_without_codes_fixed": "ㄱ의고유DNA·이분분열과ㄹ의카디오리핀은본문의박테리아기원근거와맞는다. 일반막·수송단백질또는진핵리보솜으로는같은지지역할을확보못함.",
  "primary": [
    63
  ],
  "auxiliary": [
    39,
    17
  ],
  "surface": [
    15,
    22,
    74
  ],
  "evidence": [
    "5문단박테리아같은이분분열·카디오리핀·박테리아리보솜과유사성이기원근거."
  ],
  "competing_codes": [
    {
      "code": 15,
      "reason": "본문의근거목록을판단기준으로적용한다는넓은기술가능.다만각특성이박테리아기원을뒷받침하는이유를평가하는것이지필요충분정의로종을분류하지않는다."
    },
    {
      "code": 22,
      "reason": "박테리아기원이라유사속성이남았다는설명에서공유속성만있으면반드시같은기원이라는역의보편법칙을새로만들지않는다. 본문이채택한지지근거범위에한정."
    },
    {
      "code": 74,
      "reason": "다른모든가능기원의대체예측표가제시되지않았으므로경쟁가설을완전히소거하는증명이라고과장하지않음."
    }
  ],
  "falsification_probe": "특정수송단백질포린을일반수송단백질존재로완화하면진핵세포도갖는특징이되어기원식별력이달라진다. 속성의구체성을보존.",
  "confidence": 0.96,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
