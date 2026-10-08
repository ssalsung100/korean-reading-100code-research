

<!-- luna-raw:AFI-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "selected_answer": 3,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "source_boundary_residue": "AFK말미 ##2018학년도 잔재;group식별미확정"
  },
  "required_information_and_location": [
    "2문단 기본음은 부분음 중 최소 진동수이고 복합음의 지각된 진동수를 정함.",
    "3문단 스펙트럼은 가로축진동수·세로축세기이며 음색은 부분음 진동수·상대적 세기로결정.",
    "실제그림의 막대110/220/330/440/550Hz,110Hz막대가가장높음."
  ],
  "minimal_logic_without_codes": "가장 낮은 진동수110Hz의 부분음이 기본음이고 그 막대 높이가 가장 크므로③. 기본음의 정의와 실제그림 높이 비교를 결합한다.",
  "intermediate_reasoning": [
    "① 간격이110Hz로 일정하여 고른음이고 심벌즈의 시끄러운음이 아니다.",
    "② 복합음은최대550이아니라기본음110Hz로인식.",
    "④ 가로축은시간이아니라진동수다.",
    "⑤ 220Hz성분을제거하면 부분음구조가달라져음색이변함."
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "220Hz를지워도기본음110Hz가남아음고가같다는점을음색불변으로옮긴다. 음색은기본음하나가아니라부분음들의구조에의존.",
  "visual_reading": {
    "path": "data/기본기_연구/prepared_backlog/blind_sources/assets/G194_Q31_figure.png",
    "findings": "가로진동수·세로세기표지직접확인,110최고막대/550최저막대.막대높이정확수치는추정하지않음.",
    "metadata_note": "asset은AFH에연결돼있으나지문공통그림이며실제판독을요구하는문항은AFI.기계위치보강요청."
  },
  "quota_status": "unavailable"
}
```
