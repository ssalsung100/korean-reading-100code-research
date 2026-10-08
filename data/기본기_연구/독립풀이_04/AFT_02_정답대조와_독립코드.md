

<!-- luna-raw:AFT-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G196",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "의원들이관심을두지않았다는것을서양의학의한계를직접지적했다는행위로바꾼③은제시된이유가아니다.",
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


<!-- luna-raw:AFT-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G196",
  "logic_without_codes_fixed": "본문의 의원들은 무관심했고, 전래 의학 내용 부족은 서술자가 제시한 제한 요인이다.③은 두 정보를 합쳐 의원들이 한계를 지적했다는 새 행위를 만들어 이유로 삼는다.",
  "primary": [
    17
  ],
  "auxiliary": [
    56,
    64
  ],
  "surface": [
    46,
    63
  ],
  "evidence": [
    "3문단의원들의관심에서도비껴나있음/내용면에서도부족/윤리문제/금지조치.",
    "③의원들이한계를지적했다는주장행위는본문에없음."
  ],
  "competing_codes": [
    {
      "code": 56,
      "reason": "영향미미의이유를찾는발문이지만다른정당한이유와③을구별하는결정점은설명유형분류가아니라누가한계를지적했는지의증거유무다."
    },
    {
      "code": 46,
      "reason": "여러제약이영향미미에기여하는인과맥락은있다. 그러나③은원인효과방향을뒤집은것이아니라근거가없는의원행위를새로추가."
    },
    {
      "code": 63,
      "reason": "한계를지적한다는말은비판처럼보이지만새증거로논증을강화·약화하는문항이아니다. 그비판행위가제시되었다는사실자체가없다."
    }
  ],
  "falsification_probe": "의원들이구체한계를지적했다는원문문장을추가하면③의부재근거가해소된다. 내용부족평가만반복해도그행위주체의증거는새로생기지않는다.",
  "generation_principle": "서술자의평가와등장인물의발화·행위를분리하고둘을합성한오답을검증한다.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
