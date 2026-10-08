

<!-- luna-raw:BFK-blind-20261002-r3-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G411",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "prior_exposure": "unknown",
    "official_answer_read": false,
    "sdss_read": false,
    "existing_case_analysis_read": false,
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "15년 기록 황종관·황종척 길이",
      "evidence": "황종관 9치, 여기에 1치를 더하여 황종척"
    },
    {
      "location": "15년 기록 최초 관과 밀랍 관 비교",
      "evidence": "해주산 검은 기장 관은 중국음보다 높음; 밀랍 관은 중국음과 맞음"
    },
    {
      "location": "12년 2월 발언 및 blind visual02",
      "evidence": "전적은 쌓는 법을 기록. 산지 규정은 없다. ㄱㄴㄷㄹ 복원 자료를 직접 읽음"
    }
  ],
  "minimal_logic_without_codes": "길이의 기준, 제작 목표음, 두 관의 실제 음을 각각 확인하면 ㄱ·ㄷ 참, ㄴ·ㄹ 거짓이다.",
  "intermediate_inference": [
    "황종척 전체는 10치이고 관은 그중 9치다.",
    "검은 기장 관≠중국음, 밀랍 관=중국음이므로 두 관은 같지 않다.",
    "쌓는 법의 전적 기재를 산지 규정으로 바꿀 수 없다."
  ],
  "attractive_wrong_answer": 1,
  "exact_error": "①의 ㄴ은 전적이 정한 항목을 쌓는 법에서 기장의 산출지로 바꾼다.",
  "source_quality_note": "JSON의 placeholder 및 manifest visual_placeholder=false와 별개로 실제 보기는 visual02.md이며 visual01.tif는 편경 그림이다. 연결을 직접 확인했다."
}
```
