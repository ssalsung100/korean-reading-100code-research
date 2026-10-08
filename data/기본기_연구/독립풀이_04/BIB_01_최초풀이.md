

<!-- luna-raw:BIB-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G435",
  "selected_answer": 4,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BIB.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G435_visual01.md",
    "data/기본기_연구/prepared_backlog/blind_sources/G435_visual02.tif",
    "data/기본기_연구/prepared_backlog/blind_sources/G435_visual03.md",
    "data/기본기_연구/prepared_backlog/blind_sources/G435_visual05.md",
    "data/기본기_연구/prepared_backlog/blind_sources/BIB_source_restoration.md"
  ],
  "necessary_information": [
    {
      "location": "[A]입법절차/그림",
      "evidence": "문지기 회부거부나 규칙미부여면 사장.수정불가는 상임위안을 본회의에서 가부,수정허용은 다른안 제출 가능."
    },
    {
      "location": "보기표",
      "evidence": "현행정책2,발의정책1.위원회정책1선호13/25과반.본회의정책3선호125/245과반."
    }
  ],
  "minimal_logic_without_codes": "앞단계에서 막히면 현행2유지.수정불가로1과2만 비교하면본회의의2·3선호195명이2를택해2유지.수정허용이면과반125명이선호하는3이통과하므로2,2,2,3인④.",
  "intermediate_reasoning": [
    "㉠문지기 권한 행사로1을회부하지않으면현행2.㉡상임위에서는1이13표로통과하나규칙미부여면사장되어2.",
    "㉢수정불가시정책1은50표,현행2는70+125=195표.정책3선호자는강화1보다유지2를더가깝게본다.1부결,2유지.",
    "㉣수정허용시정책3은125명이가장선호하여어떤다른안과맞붙어도245명과반을확보한다.정책3수정안이허용·제출되는문항의표준경로에서3확정.",
    "수정불가라는말은법안자동가결을뜻하지 않는다.수정이불가해도본회의는원안을부결할수있다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "앞단계사장또는수정불가를발의정책1의자동채택으로오인한다.의안폐기는현재시행정책2의유지이고수정불가에도가부표결은남는다."
  },
  "source_restoration": {
    "record": "BIB-hold-source-20261003-01",
    "status": "blind전구조복원완료",
    "supplement": "data/기본기_연구/prepared_backlog/blind_sources/BIB_source_restoration.md",
    "official_source_year": 2013,
    "source_page": 4,
    "original_hold_preserved": true
  },
  "unresolved": "본문은수정허용시수정안이제출되면심사한다고조건을단다.㉣은정책3이제안가능한대안으로표결된다는문항경로의예측이며수정안이아예제출되지않는현실상황까지자동통과로일반화하지않는다."
}
```
