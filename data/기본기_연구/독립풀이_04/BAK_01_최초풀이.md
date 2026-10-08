

<!-- luna-raw:BAK-blind-20261001-restored-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "necessary_information_locations": [
    "인쇄면14 Q31:두498Hz 스피커,공명500Hz,오른쪽v로 공명",
    "인쇄면14 보기:ㄱ왼쪽v,ㄴ오른쪽2v,ㄷ왼쪽 스피커 끄고 왼쪽v",
    "인쇄면13:접근/이격 주파수 차는 상대 속도에 비례"
  ],
  "minimal_logic_without_codes": "v로 접근할 때 +2Hz이므로 반대쪽으로 같은v 이동해도 접근하는 스피커가 켜져 있으면500Hz다.2v는+4Hz여서502Hz가 되고,이격 측은494Hz다.왼쪽 스피커를 끄고 왼쪽 이동하면 남은 오른쪽 소리는496Hz이므로 ㄱ만 공명.",
  "intermediate_reasoning": [
    "기준:오른쪽 스피커 접근498+2=500,왼쪽 이격498-2=496.",
    "ㄱ:왼쪽 스피커 접근500,오른쪽 이격496→공명.",
    "ㄴ:오른쪽 접근502,왼쪽 이격494→어느 쪽도500 아님.",
    "ㄷ:접근하는 왼쪽이 꺼졌고 오른쪽과 이격496→불공명."
  ],
  "most_attractive_wrong_answer": 4,
  "exact_error": "ㄷ도v로 움직인다는 속력만 보면 공명처럼 보이지만 접근하는 음원이 꺼져 있다.남은 음원에 대한 이동 방향을 보존해야 한다.",
  "passage_group": "G368",
  "selected_answer": 1,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "official_question_full_pages_directly_seen": true
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/G368_restore_page13.png",
    "data/기본기_연구/prepared_backlog/blind_sources/G368_restore_page14.png"
  ],
  "provenance": "공식2016 LEET 홀수형 HWP 등록 렌더 인쇄면13~14 직접 확인. page13 상단 이전완료 BAH도 보이나 신규 미풀이 외부문항 없음.",
  "original_hold_preserved": true,
  "source_repair": "누락 기호·BAK v/2v 확인 완료. 첫crop 불완전 기록은 보존.",
  "quota_status": "unavailable"
}
```
