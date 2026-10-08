

<!-- luna-raw:BCA-blind-20261002-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G382",
  "selected_answer": 2,
  "confidence": 0.95,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BCA.json",
  "needed_information_and_location": [
    "머스매 입적 당시 동생이 어려 입적 뜻 몰랐음",
    "작년 갓난애 입적을 보고 놀란 뒤 지난달 출생 의심",
    "꿈속 앞집 엄니 손가락을 돌려주려고 거위 목을 비튼 과거",
    "현재 윤서기-처녀의 대화"
  ],
  "minimal_logic_without_codes": "과거 입적의 순서는 현재 대사에 언급되는 순서와 다르다.머스매 입적→작년 갓난애 입적→출생 공포와 거위 사건→현재 꿈 이야기 전달.",
  "intermediate_reasoning": [
    "ㄴ은 동생이 어렸을 때,ㄱ은 작년이므로ㄴ<ㄱ.",
    "ㄱ을 보고 출생 의심과 공포가 생겼으며 거위 사건은 그 공포·꿈에 따른 행동이므로ㄱ<ㄷ.정확한 달은 제시되지 않아 연쇄 근거 수준으로 한정.",
    "ㄹ은 지금 윤서기가 처녀에게 듣는 대화이므로 이미 일어난ㄷ보다 뒤.",
    "현재 말하는 순서에서ㄱ이 먼저 나왔다고 사건 시점도 앞서는 것은 아님."
  ],
  "most_attractive_wrong_answer": {
    "choice": 1,
    "exact_error": "대사에서 갓난애를 먼저 말한 순서를 사건 순서로 오인해 머스매 입적이 더 이르다는 회상 단서를 무시한다."
  },
  "quota_status": "unavailable"
}
```
