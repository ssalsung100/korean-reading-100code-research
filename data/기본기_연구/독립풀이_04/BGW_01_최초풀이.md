

<!-- luna-raw:BGW-blind-20261002-r4-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G424",
  "selected_answer": 5,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BGW.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G424_visual03.tif",
    "data/기본기_연구/prepared_backlog/blind_sources/G424_conditions_restored_20261002.md"
  ],
  "necessary_information": [
    {
      "location": "복원 조건",
      "evidence": "도를 으뜸음으로, 한 마디 하나의 화음"
    },
    {
      "location": "보기 악보",
      "evidence": "솔도도 / 도라도파미 / 레솔파 / 미솔솔미도"
    },
    {
      "location": "본문 화음 설명",
      "evidence": "도-미-솔, 3도를 더 쌓은7화음, 근음5도 위/아래 주요3화음"
    }
  ],
  "minimal_logic_without_codes": "도 중심의 주요화음 구성음을 마디 음들과 대응한다. 도미솔 / 파라도미 / 솔시레파 / 도미솔의 화음이 각각 맞고, 마디 첫음 솔·도·레·미는 각 화음 근음 도·파·솔·도와 다르므로⑤가 부적절하다.",
  "intermediate_reasoning": [
    "㉠솔도도는 으뜸3화음 구성음이며 미가 악보에서 생략되어도 화음 구성음으로 내재한다.",
    "㉡도라도파미는 파라도미의 버금딸림7화음, ㉢레솔파는 솔시레파의 딸림7화음에 해당한다.",
    "마지막 미솔솔미도도 으뜸화음이므로④는 맞다. 화음의 근음과 선율의 첫 음을 동일시하면⑤를 잘못 수용한다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "선율에 미가 직접 적혀 있지 않다는 이유로 화음에도 미가 없다고 오판한다. 본문은 선율 속 화음 구성음의 내재를 말하며, 표면적으로 나온 음 목록과 해당 화음 전체를 구분한다."
  },
  "source_restoration": "조건 누락 hold 후 공식 조건 두 항목을 Luna가 blind-only 부록으로 복원. 공식 답·SDSS 공개 전 직접 읽고 완결했다. BGW-hold-source 원기록 보존.",
  "source_limitations": [
    "주요화음 및 본문의 구성음-화음 대응 아래 판정. 임의 비화성음과 모든 가능한 화성화까지 유일성 증명한 것은 아니다."
  ]
}
```
