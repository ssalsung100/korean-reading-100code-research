

<!-- luna-raw:AHC-blind-20260921-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G203",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "대화 및 기억에서 해당 사례 노출은 확인되지 않으나 사전학습 노출 여부는 검증 불가"
  },
  "needed_information_and_location": [
    "3문단 훑어보기의 배경지식·적응력·속도 효과",
    "3문단 타인 질문에도 효과, 스스로 질문하면 능동성 더욱 강화",
    "보기 A/B와 C/D 실험 조건·결과"
  ],
  "minimal_logic_without_codes": "제공받은 질문도 선별·집중·기억에 도움 되지만 직접 질문을 만들면 능동성은 더 커진다. 질문 효과의 존재와 능동성 정도를 구별하면 ④의 유사함은 본문의 강화 방향에 어긋난다.",
  "intermediate_inferences": [
    "① A의 제목·요약문→배경지식 활성화",
    "② 적응력 상승→A 읽기시간 단축",
    "③ C 질문→중요 내용 선별",
    "⑤ C 답 찾기→집중·장기 기억으로 D보다 우수"
  ],
  "most_attractive_wrong_answer": {
    "choice": 5,
    "attraction": "C는 스스로 질문하지 않아 효과가 없다고 오해할 수 있음",
    "error": "타인이 제공한 질문도 집중·기억 효과가 발생할 수 있다고 본문에 명시되어 있다."
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/AHC.json",
  "quota_status": "unavailable"
}
```
