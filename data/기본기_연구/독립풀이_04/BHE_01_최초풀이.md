

<!-- luna-raw:BHE-blind-20261002-r5-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G427",
  "selected_answer": 4,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BHE.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G427_visual01.md"
  ],
  "necessary_information": [
    {
      "location": "본문 끝문단",
      "evidence": "심의 기준안은 사법 심사제, 심의 후 별도 헌법위원회 채택. 양 기관 동수 구성. 후속 법률 제정 지연."
    },
    {
      "location": "보기 ⓑ/ⓒ/ⓓ",
      "evidence": "대법관5/국회의원5; 위헌결정은 3분의2 이상; 조직·절차는 법률로 정함."
    }
  ],
  "minimal_logic_without_codes": "제도 조항을 도입 단계 및 당사자 이해와 연결한다.동수 구성은 양 기관 균형, 후속 입법 요구는 시행 지연과 연결되므로(나)(라),④.",
  "intermediate_reasoning": [
    "(가)기준안은 법원이 심사하는 제도였으므로 헌법위원회에 제청하는ⓐ와 다르다.",
    "(다)강한 찬성 정족수는 국회 법률의 무효화를 어렵게 하는 장치이므로 국회보다 법원 편이라고 읽을 근거가 없다. 정족수만으로 실제 표결 결과를 예측하지 않는다.",
    "(라)헌법 명시 이후에도 조직·절차 법률이 필요했고 국회의 입법 지연이 제도 완비를 늦췄다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "(나)는 맞지만(다)의 위헌 심사 절차 존재를 곧 법원 이익 강화로 읽는다. 높은 위헌 결정 문턱은 법률 무효화를 제한하는 방향이다."
  },
  "source_limitations": [
    "보기 ⓐ~ⓓ는 전사에서 각 문장 뒤에 붙는다. 해당 앞 문장을 지시하는 것으로 읽었다."
  ]
}
```
