

<!-- luna-raw:AGQ-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G200",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "④는관찰로사실이드러나확인되는것을대상을비추어주목·검토하는뜻으로바꾸어문맥을보존하지못한다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 미수행.",
  "group_barrier": "전체6 blindraw저장후answer필드만공개.",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AGQ-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G200",
  "logic_without_codes_fixed": "밝혀짐은관찰로사실이드러나알려지는사건이고조명은대상을비추어주목·검토하는행위의뜻이어서같은발견사건을보존하지못한다.",
  "primary": [],
  "primary_candidates": [
    96,
    39
  ],
  "working_representative": 96,
  "auxiliary": [],
  "surface": [
    80,
    63
  ],
  "evidence": [
    "별도DNA·리보솜사실이밝혀지면서공생발생설부각.④조명되면서로치환."
  ],
  "competing_codes": [
    {
      "code": 39,
      "reason": "두어휘의문맥용법비교로96과국소중첩하여후보유지."
    },
    {
      "code": 80,
      "reason": "새사실을안다는인식사건이소재지만이문항은그인식의성립조건을추론하는것이아니라어휘치환의의미보존을묻는다."
    },
    {
      "code": 63,
      "reason": "새증거가이론을지지하는맥락은AGN/AGO에관련되나여기서는어휘용법이결정점이다. 같은문장배경을같은주코드로복제하지않음."
    }
  ],
  "uncertainty_preserved": "드러남·주목의근접의미가능성은원문발견맥락안에서판정하며공식답일치를사전적모든용법의완전배타성입증으로삼지않음.",
  "confidence": 0.95,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
