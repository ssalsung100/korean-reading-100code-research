

<!-- luna-raw:BIE-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G436",
  "selected_answer": 2,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BIE.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G436_visual02.md",
    "data/기본기_연구/prepared_backlog/blind_sources/G436_visual03.md",
    "data/기본기_연구/prepared_backlog/blind_sources/G436_visual04.md"
  ],
  "necessary_information": [
    {
      "location": "두가설문단",
      "evidence": "내부외부가설은주변접촉·외부노출,양극성가설은결정물질분포가세포유형을결정."
    },
    {
      "location": "보기실험표",
      "evidence": "㉠내부세포를표층이동,㉡내부세포단독배양,㉢바깥쪽결정물질기능억제후단독배양."
    }
  ],
  "minimal_logic_without_codes": "각행에지정된가설을적용한다.㉠㉡은외부노출·낮은주변접촉을갖게되므로영양외배엽,㉢은바깥쪽결정물질기능이막혀속세포덩어리.따라서②.",
  "intermediate_reasoning": [
    "㉠원래내부였다는출신보다조작후표층환경을적용해야내부외부가설을지지한다.",
    "㉡단독배양이면주변세포접촉이줄고외부에노출되므로내부세포유래라도표층형예측.",
    "㉢단독배양의노출만보면다른가설과섞인다.해당행은양극성가설이므로결정물질기능억제로CDX2집중효과가없어지는쪽을적용한다.",
    "가설을지지하는결과를묻는것이지실제배양실험결과가이미관찰됐거나가설이독점적으로입증됐다는뜻은아니다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "㉡의세포가기존에내부였다는상태를유지한다고보아단독배양으로변한접촉·노출조건을무시한다."
  }
}
```
