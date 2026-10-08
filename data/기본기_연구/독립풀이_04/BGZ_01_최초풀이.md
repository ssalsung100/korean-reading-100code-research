

<!-- luna-raw:BGZ-blind-20261002-r4-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G425",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BGZ.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G425_visual01.md"
  ],
  "necessary_information": [
    {
      "location": "본문 자연법론",
      "evidence": "자연법에 반하는 인정법은 효력이 없다.㉠성서의 인간 지배권,㉡신이 명한 생존·번식권"
    },
    {
      "location": "보기",
      "evidence": "(가)현행법 해석으로 자연물의 주체성 가능,(나)성문·관습 근거 부재로 현행법상 당사자성 부정"
    }
  ],
  "minimal_logic_without_codes": "㉠이 근거로 삼은 신의 질서와 자연법은 인간이 정한 인정법에 우선한다. (나)는 성문·관습법인 현행법을 근거로 하므로㉠은 자기 근거법이 더 상위라고 본다.",
  "intermediate_reasoning": [
    "①(가)는 인간의 특별 지위를 부정하지만㉠은 인간의 자연 지배권을 주장한다.",
    "②(가)는 현행법 해석만으로 가능하다고 하며㉡도 신/자연법상 권리를 이미 인정하므로 법 변경 필요에 동의하지 않는다.",
    "④(나)의 현행법상 권리 접근과㉡의 자연법상 권리 접근을 같게 볼 수 없다. ⑤㉠㉡은 둘 다 신의 질서를 근거로 논쟁하므로 섭리 밖 문제가 아니다."
  ],
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "자연물 권리를 인정한다는 결론 유사성을 법 변경 필요라는 수단 요건의 일치로 바꾼다. 실제로 두 입장 모두 기존 법/질서에 근거한다."
  },
  "source_limitations": [],
  "scope": "본문과 보기의 가상·역사적 법관념 비교로만 한정."
}
```
